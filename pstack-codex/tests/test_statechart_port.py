import os
from pathlib import Path
import stat
import subprocess
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[2]
SOURCE = REPO / "pstack/skills/statechart"
PORT = REPO / "pstack-codex/skills/statechart"
LAUNCHER = PORT / "scripts/statechart"


class StatechartPortTest(unittest.TestCase):
    def test_resource_executable_modes_match_upstream(self):
        for source in SOURCE.rglob("*"):
            if source.is_file() and source.name != "SKILL.md":
                relative = source.relative_to(SOURCE)
                with self.subTest(resource=str(relative)):
                    target = PORT / relative
                    self.assertEqual(
                        stat.S_IMODE(source.stat().st_mode) & 0o111,
                        stat.S_IMODE(target.stat().st_mode) & 0o111,
                    )

    def test_launcher_works_directly_and_through_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            scratch = Path(temp).resolve()
            inner = scratch / "inner"
            inner.mkdir()
            relative_link = inner / "statechart"
            relative_link.symlink_to(os.path.relpath(LAUNCHER, inner))
            absolute_link = scratch / "statechart"
            absolute_link.symlink_to(relative_link)
            env = os.environ.copy()
            env.update(HOME=temp, TMPDIR=temp, XDG_CACHE_HOME=temp)
            env.pop("TLA2TOOLS", None)
            env.pop("JAVA", None)
            for launcher in (LAUNCHER, absolute_link):
                with self.subTest(launcher=str(launcher)):
                    result = subprocess.run(
                        [str(launcher)], env=env, capture_output=True, text=True, timeout=20
                    )
                    if result.returncode == 127 and "statechart needs Node" in result.stderr:
                        self.skipTest("No supported TypeScript runtime is available")
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIn("Give one SPEC.tla.", result.stderr)
                    self.assertIn("Usage: statechart SPEC.tla", result.stderr)


if __name__ == "__main__":
    unittest.main()
