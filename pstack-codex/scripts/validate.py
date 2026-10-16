#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib

root = Path(__file__).resolve().parents[1]
repo = root.parent
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


manifest = json.loads((root / "plugin.json").read_text())
check(manifest["name"] == "pstack-codex", "wrong plugin identity")
check(manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "portable manifest schema missing")
source_map = json.loads((root / "docs/source-map.json").read_text())
source_paths = [entry["source"] for entry in source_map["files"]]
source_inventory = {str(file.relative_to(repo / "pstack")) for file in (repo / "pstack").rglob("*") if file.is_file() and "node_modules" not in file.parts}
check(set(source_paths) == source_inventory, "source inventory differs from source-map entries")
check(len(source_paths) == len(set(source_paths)), "duplicate source mapping")
for entry in source_map["files"]:
    source = repo / "pstack" / entry["source"]
    target = root / entry["destination"]
    check(target.is_file(), f"lost resource: {entry['source']}")
    check(source.is_file() and hashlib.sha256(source.read_bytes()).hexdigest() == entry["sha256"], f"Cursor source changed: {entry['source']}")
original_skills = {f.parent.name for f in (repo / "pstack/skills").glob("*/SKILL.md")}
skills = list((root / "skills").glob("*/SKILL.md"))
check(original_skills <= {f.parent.name for f in skills}, "original skill missing")
for file in skills:
    text = file.read_text()
    parts = text.split("---", 2)
    if len(parts) != 3:
        errors.append(f"missing skill frontmatter: {file}")
        continue
    front = parts[1]
    name = re.search(r"^name: (.+)$", front, re.M)
    check(bool(name) and name[1] == file.parent.name, f"skill name mismatch: {file}")
    check(bool(re.search(r"^description: .+", front, re.M)), f"missing description: {file}")
    check(not re.search(r"^(disable-model-invocation|paths|icon|color):", front, re.M), f"unsupported frontmatter: {file}")
    original = repo / "pstack/skills" / file.parent.name / "SKILL.md"
    if original.exists() and "disable-model-invocation: true" in original.read_text().split("---", 2)[1]:
        policy = file.parent / "agents/openai.yaml"
        check(policy.exists() and "allow_implicit_invocation: false" in policy.read_text(), f"lost explicit-only policy: {file}")
for file in (root / "agents").glob("*.toml"):
    agent = tomllib.loads(file.read_text())
    check(all(isinstance(agent.get(k), str) and agent[k] for k in ["name", "description", "developer_instructions"]), f"invalid custom role: {file}")
for file in root.rglob("*.md"):
    if "node_modules" in file.parts:
        continue
    text = file.read_text()
    text = re.sub(r"(?ms)^```.*?^```\s*$", "", text)
    text = re.sub(r"`[^`\n]+`", "", text)
    for match in re.finditer(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", text):
        target = match[1].split("#", 1)[0].strip("<>")
        if not target or "://" in target or target.startswith(("mailto:", "/")):
            continue
        check((file.parent / target).exists(), f"broken local link: {file.relative_to(root)} -> {target}")
market = json.loads((repo / ".agents/plugins/marketplace.json").read_text())
entry = next(x for x in market["plugins"] if x["name"] == manifest["name"])
check((repo / entry["source"]["path"]).resolve() == root.resolve(), "marketplace points at another package")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
playbooks = list((root / "skills/poteto-mode/playbooks").glob("*.md"))
agents = list((root / "agents").glob("*.toml"))
print(f"PASS: {len(skills)} skills, {len(playbooks)} retained playbooks, {len(agents)} roles, {len(source_inventory)} source resources and Cursor hashes, policies, marketplace, local links")
