---
name: setup-pstack
description: "Configure pstack for Codex: local installation, per-role models and reasoning, agent roles, and external adapter readiness."
---

Read [CODEX.md](../../CODEX.md) before this workflow.

# Set up pstack for Codex

1. Confirm the target repository and installed plugin root. Follow the package README for marketplace installation; do not modify Cursor settings. Run `python3 <plugin>/scripts/runtime.py doctor` from the target repository.
2. Inspect `.agents/pstack/config.json` if present. Otherwise use `templates/config.example.json`. Preserve valid user choices and unknown user-owned fields. Do not overwrite another project's configuration.
3. Enumerate models supported by this session's spawn tools and any configured external provider. Ask for a budget: unlimited (max), large (xhigh), medium (high), or small (medium). These are requested effort levels, not promises of model support. Confirm every selected model and effort. Keep `auto` and `inherit-parent` aliases. Do not change model strings to encode effort or speed.
4. Show every original role below with its current model, effort, speed, execution placement, and any adapter gap. Let the user accept or change it. Panel list length sets seat count. Cross-judge pool selects one distinct-family judge. Keep reruns idempotent and retain deliberate user overrides. A retired role may be removed only after showing that change.

| Single-seat roles | Panel roles |
| --- | --- |
| feature, refactoring; bug-fix; perf-issue; hillclimb | arena runners |
| judgment and prose; hardest tasks | architect runners |
| how explorer; how explainer | interrogate reviewers |
| why investigators; why synthesizer | arena cross-judge pool |
| reflect tooling; reflect judgment, divergent, synthesizer; swarm workers | |

5. Write the agreed secret-free JSON in the target repository. The template deliberately leaves diverse panels unconfigured. Configure each required family with a real available model and execution route; do not fill it with invented defaults. Run `check-config` and each configured panel's `role <name> --distinct-families` command. A successful config check does not prove provider access.
6. Preview `python3 <plugin>/scripts/runtime.py install-agents --project <repo>`, then apply if the user chose installation. It checks conflicts before writes. Restart or reload the client and verify custom role discovery. If installation is unavailable, CODEX.md defines the full-prompt delegate fallback. Do not claim plugin `agents/` loads automatically.
7. Ask whether the user wants Poteto as standing project behaviour. If yes, add a scoped AGENTS.md instruction to read the installed absolute poteto-mode path for relevant work. Explain that this differs from Cursor's mode picker. Do not change global instructions or install hooks silently.
8. Report installed versus pending items. Test a real requested workflow only within its authorised scope. Offer `$create-verification-skill` once if the project has no real app-driving harness.

Ordinary unset roles inherit the parent. Required multi-family panels, remote execution, and webhook events remain BLOCKED until their adapters are configured and proved. Read `docs/parity.md` before reporting full parity.
