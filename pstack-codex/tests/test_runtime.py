import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PLUGIN = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("runtime", PLUGIN / "scripts/runtime.py")
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class RuntimeTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def session(self, name, cwd, body="", source="cli"):
        path = self.root / "sessions" / (name + ".jsonl")
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"type": "session_meta", "payload": {"id": name, "cwd": str(cwd), "source": source}}) + "\n" + body)
        return path

    def test_history_scopes_exact_workspace_and_excludes_children(self):
        project = self.root / "project"
        self.session("ours", project, '{"type":"function_call","payload":"real command"}\n')
        self.session("other", self.root / "other", "private unparseable body\n")
        self.session("nested", project / "nested")
        self.session("child", project, source={"subagent": {"parent": "ours"}})
        self.assertEqual([m["id"] for _, m in runtime.sessions(self.root, project)], ["ours"])
        self.assertEqual({m["id"] for _, m in runtime.sessions(self.root, project, children=True)}, {"ours", "child"})

    def test_history_order_is_modification_time(self):
        project = self.root / "project"
        older = self.session("zzzz", project)
        newer = self.session("aaaa", project)
        os.utime(older, (100, 100))
        os.utime(newer, (200, 200))
        self.assertEqual([m["id"] for _, m in runtime.sessions(self.root, project)], ["aaaa", "zzzz"])

    def test_history_read_keeps_tool_events_and_refuses_cross_workspace_id(self):
        project = self.root / "project"
        body = '{"type":"response_item","payload":{"type":"function_call","name":"exec","arguments":"actual command"}}\n'
        path = self.session("ours", project, body)
        self.session("private", self.root / "private", "secret\n")
        base = [sys.executable, str(PLUGIN / "scripts/runtime.py"), "history", "read", "--cwd", str(project), "--codex-home", str(self.root)]
        ok = subprocess.run(base + ["--id", "ours"], text=True, capture_output=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(ok.stdout, path.read_text())
        denied = subprocess.run(base + ["--id", "private"], text=True, capture_output=True)
        self.assertEqual(denied.returncode, 2)
        self.assertNotIn("secret", denied.stdout + denied.stderr)

    def test_no_history_is_unknown(self):
        result = subprocess.run([sys.executable, str(PLUGIN / "scripts/runtime.py"), "history", "latest", "--cwd", str(self.root / "missing"), "--codex-home", str(self.root)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "unknown")

    def test_role_inherits_but_diversity_never_silently_falls_back(self):
        self.assertEqual(runtime.role_seats({}, "how explorer")[0]["model"], "inherit-parent")
        with self.assertRaisesRegex(ValueError, "BLOCKED"):
            runtime.role_seats({}, "interrogate reviewers", distinct=True)
        config = {"roles": {"panel": [{"model": "one", "family": "same"}, {"model": "two", "family": "same"}]}}
        with self.assertRaisesRegex(ValueError, "distinct families"):
            runtime.role_seats(config, "panel", distinct=True)

    def test_distinct_external_seat_requires_adapter(self):
        config = {"roles": {"panel": [{"model": "one", "family": "a"}, {"model": "two", "family": "b", "execution": "multi_model"}]}}
        with self.assertRaisesRegex(ValueError, "multi_model adapter"):
            runtime.role_seats(config, "panel", distinct=True)
        config["adapters"] = {"multi_model": {"command": [sys.executable]}}
        self.assertEqual(len(runtime.role_seats(config, "panel", distinct=True)), 2)

    def test_config_keeps_model_effort_speed_separate(self):
        path = self.root / "config.json"
        model = "actual-model-id"
        path.write_text(json.dumps({"schema_version": 1, "roles": {"code": [{"model": model, "reasoning_effort": "high", "speed": "standard"}]}}))
        self.assertEqual(runtime.load_config(path)["roles"]["code"][0]["model"], model)

    def test_malformed_configuration_is_an_actionable_error(self):
        path = self.root / "config.json"
        for value in [[], {"schema_version": 1, "roles": []}, {"schema_version": 1, "roles": {"code": []}}, {"schema_version": 1, "adapters": {"webhook": {"command": "shell code"}}}]:
            path.write_text(json.dumps(value))
            with self.subTest(value=value), self.assertRaises(ValueError):
                runtime.load_config(path)

    def test_missing_adapter_does_not_launch_anything(self):
        with self.assertRaisesRegex(ValueError, "not configured"):
            runtime.run_adapter({}, "webhook", "create", {}, 5)

    def test_adapter_receives_json_without_shell_interpolation(self):
        code = "import json,sys; r=json.load(sys.stdin); print(json.dumps({'schema_version':1,'status':'ok','result':r}))"
        config = {"adapters": {"multi_model": {"command": [sys.executable, "-c", code]}}}
        payload = {"prompt": "literal $(touch should-not-exist) `code`", "model": "exact-id"}
        result = runtime.run_adapter(config, "multi_model", "run", payload, 5)
        self.assertEqual(result["result"]["payload"], payload)
        self.assertEqual(result["result"]["operation"], "run")

    def test_adapter_errors_do_not_echo_private_stderr(self):
        config = {"adapters": {"webhook": {"command": [sys.executable, "-c", "import sys; print('private-key',file=sys.stderr); sys.exit(7)"]}}}
        with self.assertRaisesRegex(ValueError, "exited 7") as error:
            runtime.run_adapter(config, "webhook", "inspect", {}, 5)
        self.assertNotIn("private-key", str(error.exception))

    def test_adapter_rejects_invalid_result(self):
        config = {"adapters": {"remote_worker": {"command": [sys.executable, "-c", "print('{}')"]}}}
        with self.assertRaisesRegex(ValueError, "invalid response"):
            runtime.run_adapter(config, "remote_worker", "status", {}, 5)

    def test_agent_install_is_preview_then_idempotent_apply(self):
        project = self.root / "target"
        planned = runtime.install_agents(PLUGIN, project)
        self.assertEqual(len(planned), 2)
        self.assertFalse(project.exists())
        runtime.install_agents(PLUGIN, project, apply=True)
        before = {f: Path(f).read_bytes() for f in planned}
        runtime.install_agents(PLUGIN, project, apply=True)
        self.assertEqual(before, {f: Path(f).read_bytes() for f in planned})

    def test_agent_conflict_prevents_all_writes(self):
        project = self.root / "target"
        conflict = project / ".codex/agents/poteto-agent.toml"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("user-owned agent")
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            runtime.install_agents(PLUGIN, project, apply=True)
        self.assertEqual(conflict.read_text(), "user-owned agent")
        self.assertFalse((conflict.parent / "comment-sicko.toml").exists())


if __name__ == "__main__":
    unittest.main()
