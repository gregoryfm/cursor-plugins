# Benny automation intent for Codex

## What I want to automate

I want two event-driven automations that work together in one Slack issue channel.

### Automation 1: triage issue reports

- Trigger on each new top-level report in my configured source Slack channel and retain its original thread coordinates.
- Read the thread and attachments. Classify the report as a bug, performance issue, feature request, question or feedback, or reroute. Trace the likely owning layer before routing.
- Search my tracker for duplicates. Update a confident duplicate and create a ticket only for a clear new bug.
- Use configured Slack thread reads and replies, my tracker integration, and my optional routing map.
- Post exactly one verdict in the source thread with `[benny:bug]`, `[benny:performance]`, or `[benny:other]`. A bug or performance marker may include the tracker URL.
- Never post a root message in the source channel.

### Automation 2: reproduce and fix confirmed bugs

- Start from the same top-level report, or a supported trigger explicitly chosen during setup, then wait for the trusted triage marker in the original thread.
- Stop when someone clearly owns the fix. If an existing pull request or merged commit may fix the report, verify it instead of creating a competing change.
- Use my control adapter and feature map. Reproduce the exact symptom twice through the real UI. Capture screenshots, video, and a read-only state cross-check.
- Verify existing pull requests without editing them. After a confirmed repro, attempt at most one bounded root-cause fix, use TDD when a test is cheap, smoke the blast radius, and open a draft pull request only after before-and-after proof passes.
- Use configured Slack thread reads and replies, repository and history access, draft pull request creation, tracker access, and the control adapter.
- Report evidence and verified results in source or optional operations threads. Keep updates short.
- Never post a root message in the source channel.

### Shared rules

- Source channel and root thread coordinates remain immutable for the whole run.
- Utility and debug bots are evidence, not delegation or fix ownership.
- Subagents may help only when their capabilities and credentials enforce the required isolation. They cannot post to Slack or receive Slack credentials. Prompt wording alone is not isolation.
- Commit this entire pack at `.agents/automations/benny/`. Its `SKILL.md` files are direct instructions, not registered plugin skills.
- Install `pstack-codex` in project scope for `how`, `why`, `tdd`, `unslop`, and the required principle skills. Follow its `CODEX.md` and `setup-pstack`; preserve unrelated marketplace and `.codex/config.toml` settings.
- Every live prompt reads its committed operational file directly. Do not use plugin cache paths, copied excerpts, or slash-skill discovery.
- Keep user configuration, feature maps, routing maps, and secrets outside the copied pack.
- Fail closed when coordinates, tracker access, required event or execution capabilities, app control, feature map, or model availability are missing or uncertain.
- Open draft pull requests only. Do not merge or deploy.

### My configuration

- Source Slack channel: `<channel ID>`
- Optional operations channel: `<channel ID or none>`
- Repository and default branch: `<repo>`, `<branch>`
- Tracker: `<type, team, project, labels, intake status>`
- Routing map: `<path or none>`
- Triage identity: `<Slack identity>`
- Event adapter: `<new-report trigger and authenticated event handoff>`
- Execution adapter: `<repository checkout, app control, evidence, credentials and bounded-run support>`
- Control skill: `<configured skill or adapter>`
- Feature map: `<committed same-repo path outside this pack>`
- Models: `<available model and reasoning effort for triage, reproduce, code and media review>`
- Status emoji strings: `<seen, reproducing, reproduced, blocked, fixing, failed, pull request opened>`
- Budgets: `<thread polling, verdict wait, follow-up, repro, rejection, fix>`
- Optional bot token capability: `<none, file download, or editable operations status>`

Start from the copied configuration and feature-map examples. Put completed copies under `.agents/benny/` or an explicit external configuration location. Keep secrets in a secret manager or environment.

## For the agent

1. Ask which repository will run the automations unless it is already explicit.
2. Treat the directory containing this file as the source pack. Merge it into `<target-repository>/.agents/automations/benny/`.
3. Preserve destination-only files. Review conflicting source-managed files and merge local edits. Ask only if ownership is ambiguous.
4. Verify that the copied entry point, setup instructions, operational instructions, references, templates, and parity checklist exist.
5. Read `.agents/automations/benny/skills/setup-benny/SKILL.md` directly from the target repository and follow it.

Verify shared dependencies from a fresh Codex session rooted in the target project. Existing session context or a user-scoped install is not project verification. Do not register the Benny operational directory as a plugin skill root.

Prepare the configuration and reviewable adapter handoff before requesting activation. Do not create or update a live automation until I explicitly ask. Do not assume this plugin conversion authorises Slack posts, tracker writes, live services, or automation activation.

The local Codex scheduler is not an equivalent Slack event trigger. An external event and execution adapter, or an eligible ChatGPT web app-event task plus remote execution adapter, must satisfy `PARITY.md`. Do not silently substitute scheduled polling. For existing automations, inspect the configured adapter's existing IDs and update in place only when asked. Do not create duplicates.
