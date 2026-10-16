---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
---

Read [CODEX.md](../../CODEX.md) before this workflow. It owns tool translation, role selection, history, and external adapter gates.

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "$reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Locate the exact current conversation through CODEX.md history tools. Use complete events when available; otherwise pass a clearly labelled digest as the original workflow permits. Never infer identity from the newest file or read unrelated project chats.

## 2. Spawn three reviewers in parallel

Launch three report-only reviewers with the read tools their configured execution route provides. Use configured roles through CODEX.md; do not disable MCP access or pass unsupported read-only flags.

Resolve each role through CODEX.md. Use native subagents for supported local models and the multi-model adapter for external providers. Keep investigators report-only while retaining their read tools.

| Lens | Role line | Default `model` | Prompt template |
|---|---|---|---|
| Judgment | `reflect judgment, divergent, synthesizer` | inherit parent unless configured | `references/judgment-reviewer.md` |
| Tooling | `reflect tooling` | inherit parent unless configured | `references/tooling-reviewer.md` |
| Divergent | `reflect judgment, divergent, synthesizer` | inherit parent unless configured | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Reviewers return findings in the native subagent response body.

## 3. Synthesize

Resolve `reflect judgment, divergent, synthesizer` through CODEX.md and spawn the synthesizer with inherited read tools. Pass `references/synthesizer.md` verbatim with full reviewer outputs. It returns Accepted / Rejected / Backlog.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

File Backlog items only when the user authorised tracker writes. Otherwise present the proposed items. Only the Accepted list waits for approval.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to the Codex `skill-creator` workflow skill and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `skill-creator` and run its description-optimization loop.
- `new skill via create-skill: <kebab-name>`: hand creation to `skill-creator`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
