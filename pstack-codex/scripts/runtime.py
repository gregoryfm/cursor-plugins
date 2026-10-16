#!/usr/bin/env python3
"""Local helpers for pstack workflows. No model or service is contacted implicitly."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ADAPTERS = {"multi_model", "remote_worker", "webhook"}
EFFORTS = {"none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"}


def load_config(path):
    if not path.is_file():
        return {"schema_version": 1, "roles": {}, "adapters": {}}
    value = json.loads(path.read_text())
    if not isinstance(value, dict) or value.get("schema_version") != 1:
        raise ValueError("configuration needs schema_version 1")
    if not isinstance(value.get("roles", {}), dict) or not isinstance(value.get("adapters", {}), dict):
        raise ValueError("roles and adapters must be objects")
    for role, seats in value.get("roles", {}).items():
        if not isinstance(seats, list) or not seats:
            raise ValueError(f"role {role} needs a nonempty list of seats")
        for seat in seats:
            if not isinstance(seat, dict) or not isinstance(seat.get("model"), str) or not seat["model"]:
                raise ValueError(f"role {role} needs a model in every seat")
            if seat.get("reasoning_effort") not in EFFORTS | {None}:
                raise ValueError(f"role {role} has an invalid reasoning_effort")
            if seat.get("speed", "inherit") not in {"inherit", "standard", "fast"}:
                raise ValueError(f"role {role} has an invalid speed")
            if seat.get("execution", "native") not in {"native", "multi_model"}:
                raise ValueError(f"role {role} has an invalid execution")
            if seat.get("model") in {"auto", "inherit-parent"} and seat.get("execution", "native") != "native":
                raise ValueError(f"role {role}: inherited models must use native execution")
    for name, adapter in value.get("adapters", {}).items():
        if name not in ADAPTERS:
            raise ValueError(f"unknown adapter {name}")
        if not isinstance(adapter, dict):
            raise ValueError(f"adapter {name} must be an object")
        argv = adapter.get("command")
        if not isinstance(argv, list) or not argv or not all(isinstance(x, str) and x for x in argv):
            raise ValueError(f"adapter {name} needs a nonempty command argv")
        if not Path(argv[0]).is_absolute():
            raise ValueError(f"adapter {name} executable must be an absolute path")
    return value


def role_seats(config, name, distinct=False):
    seats = config.get("roles", {}).get(name)
    if seats is None:
        if distinct:
            raise ValueError(f"BLOCKED: configure {name} with distinct model families; see docs/adapters.md")
        seats = [{"model": "inherit-parent", "execution": "native"}]
    if distinct:
        families = [s.get("family") for s in seats]
        if len(seats) < 2 or any(not isinstance(f, str) or not f.strip() for f in families) or len(set(families)) != len(families):
            raise ValueError(f"BLOCKED: {name} needs explicit distinct families in every seat")
        if any(s["model"] in {"auto", "inherit-parent"} for s in seats):
            raise ValueError(f"BLOCKED: {name} needs explicit models for family verification")
    if any(s.get("execution") == "multi_model" for s in seats) and "multi_model" not in config.get("adapters", {}):
        raise ValueError("BLOCKED: multi_model adapter is not configured")
    return seats


def session_metadata(file):
    with file.open() as stream:
        try:
            event = json.loads(stream.readline())
        except json.JSONDecodeError:
            return None
    if not isinstance(event, dict):
        return None
    payload = event.get("payload", {})
    if not isinstance(payload, dict) or event.get("type") != "session_meta" or not isinstance(payload.get("id"), str) or not isinstance(payload.get("cwd"), str):
        return None
    return payload


def sessions(home, cwd, children=False, archived=False):
    target = cwd.resolve()
    roots = [home / "sessions"]
    if archived:
        roots.append(home / "archived_sessions")
    matches = []
    for directory in roots:
        if not directory.exists():
            continue
        for file in directory.rglob("*.jsonl"):
            if file.is_symlink():
                continue
            meta = session_metadata(file)
            if not meta or Path(meta["cwd"]).resolve() != target:
                continue
            source = meta.get("source", "")
            if not children and isinstance(source, dict) and "subagent" in source:
                continue
            matches.append((file, meta))
    return sorted(matches, key=lambda row: row[0].stat().st_mtime, reverse=True)


def install_agents(plugin, project, apply=False):
    planned = []
    for source in sorted((plugin / "agents").glob("*.toml")):
        target = project / ".codex" / "agents" / source.name
        if target.exists() and target.read_bytes() != source.read_bytes():
            raise ValueError(f"refusing to overwrite an existing custom agent: {target}")
        planned.append((source, target))
    for source, target in planned:
        if apply:
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                with target.open("xb") as stream:
                    stream.write(source.read_bytes())
    return [str(target) for _, target in planned]


def run_adapter(config, name, operation, payload, timeout):
    adapter = config.get("adapters", {}).get(name)
    if not adapter:
        raise ValueError(f"BLOCKED: external adapter {name} is not configured; see docs/adapters.md")
    request = {"schema_version": 1, "operation": operation, "payload": payload}
    completed = subprocess.run(adapter["command"], input=json.dumps(request), text=True, capture_output=True, timeout=timeout)
    if completed.returncode:
        # External stderr may contain credentials. Do not echo it.
        raise ValueError(f"adapter {name} exited {completed.returncode}; inspect its private logs")
    response = json.loads(completed.stdout)
    if not isinstance(response, dict) or response.get("schema_version") != 1 or response.get("status") not in {"ok", "blocked", "error"}:
        raise ValueError(f"adapter {name} returned an invalid response envelope")
    return response


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path(".agents/pstack/config.json"))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor")
    sub.add_parser("check-config")
    role = sub.add_parser("role")
    role.add_argument("name")
    role.add_argument("--distinct-families", action="store_true")
    install = sub.add_parser("install-agents")
    install.add_argument("--project", required=True, type=Path)
    install.add_argument("--apply", action="store_true")
    history = sub.add_parser("history")
    history.add_argument("action", choices=["list", "read", "latest"])
    history.add_argument("--cwd", required=True, type=Path)
    history.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME", str(Path.home()/".codex"))))
    history.add_argument("--id")
    history.add_argument("--exclude")
    history.add_argument("--since", help="ISO date or timestamp, in UTC unless an offset is given")
    history.add_argument("--children", action="store_true")
    history.add_argument("--archived", action="store_true")
    adapter = sub.add_parser("adapter")
    adapter.add_argument("name", choices=sorted(ADAPTERS))
    adapter.add_argument("operation")
    adapter.add_argument("--input", required=True, type=Path)
    adapter.add_argument("--timeout", type=float, default=60)
    args = parser.parse_args(argv)
    plugin = Path(__file__).resolve().parent.parent
    try:
        if args.command == "install-agents":
            print(json.dumps({"applied": args.apply, "paths": install_agents(plugin, args.project.resolve(), args.apply)}))
        elif args.command == "history":
            records = sessions(args.codex_home, args.cwd, args.children, args.archived)
            if args.exclude:
                records = [r for r in records if r[1]["id"] != args.exclude]
            if args.since:
                since = dt.datetime.fromisoformat(args.since.replace("Z", "+00:00"))
                if since.tzinfo is None:
                    since = since.replace(tzinfo=dt.timezone.utc)
                records = [r for r in records if r[0].stat().st_mtime >= since.timestamp()]
            if args.action == "read":
                if not args.id:
                    raise ValueError("history read requires --id")
                records = [r for r in records if r[1]["id"] == args.id]
                if len(records) != 1:
                    raise ValueError("session ID is absent or ambiguous inside the selected workspace")
                sys.stdout.write(records[0][0].read_text())
            elif args.action == "latest":
                print(dt.datetime.fromtimestamp(records[0][0].stat().st_mtime, dt.timezone.utc).strftime("%Y-%m-%d") if records else "unknown")
            else:
                print(json.dumps([{"id": m["id"], "cwd": m["cwd"], "path": str(p), "modified_at": p.stat().st_mtime} for p,m in records]))
        else:
            config = load_config(args.config)
            if args.command == "doctor":
                print(json.dumps({"tools": {n: shutil.which(n) for n in ["codex", "bun", "node", "gh", "git", "jq", "python3"]}, "configured_adapters": sorted(config.get("adapters", {})), "live_parity": "pending"}))
            elif args.command == "check-config":
                print(json.dumps({"valid": True, "path": str(args.config), "present": args.config.is_file()}))
            elif args.command == "role":
                print(json.dumps(role_seats(config, args.name, args.distinct_families)))
            else:
                response = run_adapter(config, args.name, args.operation, json.loads(args.input.read_text()), args.timeout)
                print(json.dumps(response))
                return 0 if response["status"] == "ok" else 2
        return 0
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
