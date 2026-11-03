---
name: interrogate
description: "Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Adversaries try to break a change or design, and only findings proven by a run survive."
---

Read [CODEX.md](../../CODEX.md) before this workflow. It owns tool translation, role selection, history, and external adapter gates.

# Interrogate

Adversaries try to break a change or a design. A finding survives only when a run proves it. Report findings. Do not apply fixes.

## Frame

The scope is what the user names. Otherwise review the branch diff from its merge base with the base branch through the working tree. State the intent with the **in-your-own-words** skill, using the user's message, commits, and PR description. Ask the user only when the intent is unclear.

## Fan out

Run Phase A steps 3 and 4 and Phase B of the **arena** skill with these four changes. Keep the configured `interrogate reviewers` seat count and require the distinct model families CODEX.md specifies. If any required family or adapter is unavailable, report BLOCKED; do not skip or replace a reviewer with another seat from the same family.

1. Resolve `interrogate reviewers` in place of `arena runners`.
2. Give each reviewer an isolated writable worktree with the exact review scope, including uncommitted changes copied into that worktree. Reviewers may write repros there, but must not fix the reviewed code or write to the user's worktree.
3. Spawn report-only adversaries through the native subagent or configured external-model adapter route. Confirm actual provider and model identities when results return.
4. Replace the artifact task and rationale with the scope, intent, and this brief:

> Break this change. Prove each finding with a run against the real code, such as a failing test, a repro script, or command output that shows the wrong behavior. For a design or plan, run a prototype or probe the current tree. Keep repros in your worktree. Report each finding with a title, the exact command, the output it printed, and the output the intent requires. Leave out anything you did not run. That covers style, naming, structure, and risks that need a future change to matter. No findings is a valid result. Do not edit or fix the reviewed code.

## Verify

Rerun each reported command against the same isolated worktree. Keep a finding only when the output proves a failure that breaks the intent. Drop the rest and record why. Merge findings that share a root cause.

Skip arena Phases C, D, and E. Adversaries seek different failures, so retain every verified finding rather than selecting one adversary's list.

## Output

- **Intent**: the restatement.
- **Findings**: each verified finding, its command and output, how it breaks the intent, and the adversaries that found it. Say "no verified findings" when none survive.
- **Dropped**: for each adversary, the count of dropped findings and why.
- **Blocked**: any reviewer, family, adapter, or execution evidence that was unavailable.
