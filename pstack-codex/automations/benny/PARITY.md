# Benny conversion and parity

This pack preserves the source workflows as dormant, directly read instructions. No live automation was created or enabled. No Slack message, tracker write, app-control run, webhook service, or scheduled task was performed during conversion.

## Source mapping

Every file under `pstack/automations/benny/` has the same relative path here. The two operational workflows and all four reference files retain their classification, dedupe, thread, reproduction, evidence, existing-fix and bounded-fix rules. The README, setup entry and setup workflow replace Cursor installation and automation-editor steps with Codex project installation and a reviewed adapter handoff. Both prompt templates retain the same workflow entry points.

Copied operational location: `.agents/automations/benny/`. User configuration location: `.agents/benny/` or an explicitly configured external location. Shared dependency: project-scoped `pstack-codex`. No operational Benny file is registered as a plugin skill.

The configuration example uses schema version 2: runtime adapter fields and separate model/effort fields replace Cursor-specific action preference and model strings. It is an example, not an automatic migration of a live configuration.

The source prompt templates used `message_ts`, while operational files read `trigger.ts`. The Codex port uses one normalised `ts` field. The event adapter must map provider timestamp fields without rounding, preserve optional root `thread_ts`, and retain the original event for audit. This is a setup contract; a live bridge has not been implemented here.

## External adapters required

| Capability | Requirement | Status |
| --- | --- | --- |
| New Slack report event | Authenticated top-level report trigger with exact source channel and timestamp strings. Both workflows receive the same source event. Reject reply events as new reports. | External adapter required; live parity pending. |
| Execution | Exact repository revision, tools, bounded waits, run status, credentials, evidence storage and cleanup. Preserve per-report coordination across event retries and executor interruption. | External adapter required; live parity pending. |
| Eligible ChatGPT web task | May provide an app-event trigger where available. Repository execution, real app control and evidence still require a tested remote execution adapter. | Availability and parity pending. |
| Slack and tracker actions | Exact thread replies, attachment reads, identity verification, permalink lookup, dedupe, tracker updates and verified compensation. | Configured connectors or adapters required; live parity pending. |
| App control | All seven capabilities in `references/control-adapter.md`, including real UI actions, recording and cleanup for baseline and patched revisions. | App-specific adapter required; live parity pending. |
| Worker isolation | Remove Slack write tools and credentials from every child environment. Prompt prohibitions alone do not qualify. If unavailable, coordinator performs the work. | Executor capability pending; safe coordinator fallback retained. |
| Models | Use actual models and reasoning settings reported by the executor. External model families require the plugin's model adapter. Never guess or silently substitute. | Setup validation pending. |

The local Codex scheduler is suitable for schedules. It does not provide Benny's Slack event semantics. Scheduled report polling changes latency and delivery behaviour and is allowed only as an explicit, documented user choice. The `poll_seconds` budget is for waiting on the already selected source or operations thread within a run.

## Retained invariants

- Immutable source channel and root timestamp; parent preflight before writes; no source-channel root post or fallback thread.
- One triage verdict and marker; marker accepted only from the configured identity in the original thread.
- Source-permalink dedupe, conservative tracker creation, and verified compensation after failed handoff.
- Utility bots are evidence; explicit human fix ownership stops competing work.
- Existing fix artifacts switch to verification without edits or competing pull requests.
- Exact discriminating symptom twice through real UI actions; read-only state confirmation; screenshot and recording evidence reviewed before a fix.
- One bounded root-cause fix only after confirmed repro and rejection window; patched UI proof twice, focused checks and blast-radius smoke.
- Draft pull requests only; no merge or deployment. Coordinator owns Slack posts, final review, commits and pull request.
- Worker tool and credential isolation, explicit write prohibition, artifact retention and cleanup.

## Live acceptance checklist — all pending

Static source inspection cannot establish these checks. Keep normal traffic disabled until the required checks pass in the target installation.

- [ ] Fresh project session resolves shared skills without relying on current session context or a user installation.
- [ ] Fresh executor checkout can read the exact committed pack and configuration revisions.
- [ ] New top-level Slack report triggers both workflows; reply events do not create new runs.
- [ ] Duplicate delivery and overlapping execution produce one issue and one marker verdict.
- [ ] Exact source coordinates survive operations-thread creation, waits and executor interruption.
- [ ] Trusted triage marker accepted; forged author, conflicting marker, wrong thread and timeout rejected.
- [ ] Missing coordinates, deleted parent and failed preflight produce no Slack or tracker write.
- [ ] Failed verdict compensates a newly created issue; compensation is read back and verified.
- [ ] Child environment cannot access Slack credentials or write actions; otherwise no worker launches.
- [ ] Attachment downloads and media inspection work without leaking credentials or artifacts.
- [ ] The nine-step harmless app-control check succeeds and cleanup preserves user work.
- [ ] Baseline reproduces the discriminating symptom twice with video, screenshot and state evidence.
- [ ] Existing-fix mode tests baseline and patched UI twice without changing the fix.
- [ ] Bounded fix path observes rejection and ownership gates, proves after behaviour twice, and opens only a draft pull request.
- [ ] Follow-up windows, cancellation, run output, retention and cleanup work at configured budgets.
- [ ] Saved live definitions preserve their IDs on update and no duplicate automations are created.
