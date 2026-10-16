---
name: setup-benny
description: Configure Benny and prepare its event-driven triage and repro workflows. Read directly when installing Benny or changing its Slack, tracker, repository, routing, control, model, adapter, or budget settings.
---

# Set up Benny for Codex

Benny is a dormant automation pack inside pstack-codex. Its setup and operational files are read directly, not exposed as slash skills. The entry point is the copied `FOR_AGENTS.md`.

The local Codex app supports schedules, but it does not provide Benny's new-Slack-report event trigger. A full installation needs a tested external event and execution adapter. An eligible ChatGPT web app-event task may supply the event trigger; remote repository execution and app control still need an adapter. Do not silently substitute scheduled polling or claim that local subagents provide remote execution.

Do not create or update a live automation until the user explicitly asks. Never put secrets in plugin files, prompts, or committed configuration. Read the plugin's `CODEX.md`, `docs/adapters.md`, and this pack's `PARITY.md` before preparing a live handoff. If those source files are unavailable after copying the pack, use the installed plugin's documented location or require the files before continuing.

## 1. Copy the pack and enable shared skills

Ask which repository will run the workflows unless it is already explicit. The source pack is the directory containing `FOR_AGENTS.md`. The destination is `<target-repository>/.agents/automations/benny/`.

1. Create the destination when absent and copy every source file to the same relative path.
2. Preserve destination-only files. Never delete unrelated files during install or refresh.
3. Keep user configuration, feature maps, and routing maps outside the destination.
4. Review conflicting source-managed files and merge without discarding local edits. Ask if ownership is ambiguous.
5. Verify the copied entry point, this setup file, both operational files, their references, templates, and `PARITY.md`.

If reading this file from the destination already, verify the copy and continue.

Follow the installed plugin's `setup-pstack` instructions to install and trust `pstack-codex` in the target project. Use supported `.agents/plugins` marketplace configuration and `.codex/config.toml` activation. Preserve unrelated settings and plugins. Do not invent a manifest or config key, edit Cursor settings, or activate a user-scoped plugin as a substitute for project scope.

Start a fresh Codex session rooted in that repository and verify project resolution of:

- `how`, `why`, `tdd`, `unslop`
- `principle-separate-before-serializing-shared-state`
- `principle-minimize-reader-load`
- `principle-guard-the-context-window`
- `principle-sequence-verifiable-units`
- `principle-fix-root-causes`
- `principle-prove-it-works`

Do not count skills already loaded in the setup session. Stop and report unresolved dependencies. Do not add `.agents/automations/benny/skills/` to a plugin manifest.

Tell the user that the pack, project plugin configuration, and referenced secret-free configuration must be committed before a live run. Commit only when authorised. Live prompts must read the exact committed operational files by stable repository-relative paths, never plugin cache paths or copied excerpts.

## 2. Adapt the configuration

Read `../../templates/configuration.example.yaml` and `../reproduce-and-fix-issues/references/feature-map.example.md`. Copy and fill them outside this pack, for example:

- `.agents/benny/configuration.yaml`
- `.agents/benny/feature-map.md`
- `.agents/benny/routing.md`
- An explicit user location such as `~/.config/benny/` when the execution adapter can access it securely

Never edit the pack examples as user configuration. Include one feature-map section per feature the automation may reproduce. Keep the map at the user point of view. Discover code paths at runtime.

Prefer committed secret-free files when a fresh checkout must read them. Otherwise paraphrase the required values into the reviewed prompt. Verify each referenced file exists in the same repository and exact revision the execution adapter will run.

## 3. Fill the required choices

Confirm:

- Source Slack channel ID and optional operations channel ID
- Repository URL and default branch
- Triage Slack identity
- Tracker type, team, project, labels, intake status and adapter actions
- Optional routing map
- Required control skill and completed feature-map path
- Status strings and pull request URL format
- Thread-polling and effort budgets
- Model and reasoning effort for triage, repro, code, and media review
- Event and execution adapter names, existing automation IDs when applicable, credential scopes, and run output location

Use only models reported available by the actual executor. Validate model ID and reasoning effort separately. Do not guess Cursor slugs or assume another provider is available. If a required role or model family is unavailable, stop that workflow and flag the missing adapter; do not silently substitute. Use the plugin-wide model adapter when an external model is explicitly required.

Fail setup when a required value is ambiguous. Run final names, descriptions, and prompt shims through `unslop`.

## 4. Check integration and execution capabilities

Triage requires source thread reads and replies, attachment metadata and downloads, repository and history reads, and tracker search, read, create, update, source links, and compensation.

Repro requires source thread reads and replies, optional operations posts and edits, repository and history access, draft pull request creation, the configured control adapter, and the completed feature map.

Prefer configured connector or adapter actions. `BENNY_SLACK_BOT_TOKEN` may fill only an explicitly configured narrow gap, such as downloading an attachment or editing one operations status. Store it outside prompts and YAML. Do not use undocumented endpoints.

The event adapter must supply authenticated new top-level Slack report events, preserve exact channel and timestamp strings, and reject reply events as new reports. The execution adapter must provide the configured repository revision, tools, secrets, bounded waits, artifacts, run status, and cleanup. It must deliver both workflows the same source event, preserve the configured triage identity, prevent duplicate active handling of the same report, and record completion or failure. Do not claim event delivery is exactly once unless tested; retain the operational permalink dedupe and side-effect checks.

Normalise the trigger to `source_channel_id`, `ts`, and optional `thread_ts`. A provider field such as `message_ts` must be explicitly mapped to `ts` at the adapter boundary without rounding timestamps. Never derive coordinates from model text. Unsupported or uncertain capabilities leave both live workflows disabled.

Codex subagents may inherit tools and credentials. A prompt ban is not an isolation boundary. Unless the executor removes all Slack write capabilities and credentials from a worker, perform the work in the coordinator. This includes media review and code workers.

## 5. Prepare routing and app control

If reroutes or owner pings are wanted, copy `../triage-issue-reports/references/routing.example.md` outside the pack, fill every placeholder, and keep pings off by default. Allow only a configured feature owner or a confirmed likely regression author. Without a routing map, do not guess a destination or owner.

Read `../reproduce-and-fix-issues/references/control-adapter.md` and the completed map. Confirm app startup, mapped user navigation and states, real UI actions, read-only state inspection, screenshots, video recording, and cleanup. Missing capability leaves repro disabled.

Run the nine-step harmless control-adapter setup check. It must not post to the source Slack channel. Record observed capability results, not assumed tool availability.

## 6. Prepare live automation handoffs

Determine whether these are new or existing automations. Read the copied `FOR_AGENTS.md` as the primary intent source and the matching template as secondary material.

For a new installation, prepare one complete, reviewable adapter definition at a time:

1. Fill trigger, source channel, repository, branch, identity, tools, model role, configuration and operational file paths.
2. Confirm all referenced files are committed and readable from a fresh executor checkout at the selected revision.
3. Verify the executor can read and follow the committed operational file, rather than a copied summary.
4. Show the natural-language prompt, event mapping, execution permissions, secret references, budgets, run output and failure behaviour for review.
5. Obtain activation authorisation only after the definition is concrete and the harmless checks can run.
6. Use the configured adapter's documented creation or editor flow. Verify the saved result, ID, prompt and disabled test state before preparing the second workflow.

For triage, the reviewed definition must retain:

- Name `benny-triage`
- Direct read of `.agents/automations/benny/skills/triage-issue-reports/SKILL.md`
- New top-level source report trigger and immutable source coordinates
- Thread reads and replies, attachment inspection, repository cause tracing and tracker access
- Classification, cause-aware routing, dedupe, conservative ticket creation and compensation
- One source-thread verdict ending in exactly one configured marker, with an optional tracker URL
- No source-channel root post or progress narration

For repro, retain:

- Name `benny-reproduce`
- Direct read of `.agents/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`
- The same new report event, repository and branch, or another explicitly chosen supported trigger
- Tracker, control adapter, feature map, evidence storage, draft pull request and thread-only actions
- Trusted-marker wait and ownership gates
- Two real UI repro attempts with media and read-only state evidence
- Existing-fix verification without competing edits
- Optional bounded fix only after the repro and rejection gates, followed by twice-run after proof
- No source-channel root post, merge, or deployment

For existing automations, find the configured IDs through the adapter and inspect their current definitions before preparing changes. Preserve unrelated fields. Show the same concise field checklist above and update in place only when asked. Never create a duplicate because discovery or update is unsupported.

The Codex local scheduler cannot stand in for the required Slack event adapter. If a user chooses scheduled polling, state the trigger, latency and dedupe differences and record that parity exception before setup. Do not deploy a live service as part of this source conversion.

## 7. Test thread safety before normal traffic

Use an authorised harmless test report or test channel. First verify that project plugin configuration, this pack, and every referenced secret-free file are committed at the executor revision. Confirm both saved prompts read their exact operational file.

Verify:

1. Triage stores root `thread_ts` and posts exactly one verdict as a reply.
2. The verdict has exactly one configured marker.
3. Repro accepts only the configured triage identity in the exact original thread.
4. Repro retains immutable source coordinates through operations status changes.
5. No source-channel root message appears.
6. A delegated worker cannot use any Slack write action or credentials; otherwise no worker is launched.
7. Missing coordinates, a deleted parent, or failed preflight produces no post and no tracker issue.
8. Duplicate event delivery does not create duplicate tickets or marker posts.
9. A tracker issue created before a failed verdict is compensated and the compensation is verified.

Record results in the deployment's parity checklist. A source review is not a live pass. Keep normal traffic disabled until the thread-safety checks and required execution adapter checks pass.
