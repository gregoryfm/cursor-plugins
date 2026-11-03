### Orchestrate

**You coordinate the program, never write its code.** Author the briefs, keep the work moving, verify what lands, and report decisions. Use this for a project that outlives one agent turn: multiple tracks, many PRs, or work that needs a standing coordinator. A task one agent can finish within this session routes to **Autonomous run**. A bespoke multi-step run routes to **figure-it-out**.

## Roles and boundaries

- **Coordinator.** This chat owns the goal, dependency graph, briefs, queue, verification decisions, and user report. It does not edit worker code. Keep state in the existing project tracker and its `notes.md`, when available, plus the **show-me-your-work** decision trail. If no tracker exists, use the durable notes record in `.agents/pstack/runs/<run-id>/` selected through CODEX.md. Do not create an executable database or use a bookkeeping CLI.
- **Owner.** Assign one owner to each PR. Give each writer its own branch or isolated writable worktree. The owner writes only its assigned code and owns its branch, rebase, and PR base changes when the coordinator orders them within the user's grant. The coordinator orders dependency changes; it does not write another owner's branch. Pause for any force-push approval required by Autonomy. Program workers default to a fresh remote environment through the configured `remote_worker` adapter; verify its accepted base SHA. Use a native local worktree only when the work needs this machine's app control, transcripts, simulator, or local-only authentication. A native local subagent is not a remote worker. If the required adapter is absent or cannot prove placement, report BLOCKED; do not silently substitute a local worker. An explicitly user-approved local alternative is a recorded parity change under CODEX.md.
- **Sub-coordinator.** Add one only when a track has more work than this coordinator can drain. It owns its unit briefs and returns one rollup, not raw child reports. Keep the depth to coordinator, track, and owner. Use the host's actual nesting and concurrency limits.
- **Verifier.** Assign a verifier who did not write the unit for every PR. Resolve a distinct configured model family through CODEX.md and confirm the actual provider and model identity. If that family or adapter is unavailable, report BLOCKED; do not replace it with a same-family seat or let the coordinator stand in for the verifier.
- **Landing.** Merge only when the user's actual request grants merge authority for that PR. Otherwise stop at merge-ready and hand it to the user. Never infer authority from this playbook, old chats, or a worker's report.

## Runtime and events

Read `<plugin>/CODEX.md` first. Use native subagent, thread, and app tools that are available in this session. Use native completion notifications for local subagents. Remote task survival, cloud placement, and reattachment require a configured adapter that proves those capabilities.

Use native CI or PR event subscriptions when the session provides them. Use a configured event adapter only when the needed native subscription is absent. If neither is available, report that wake path as BLOCKED. Do not replace event delivery with polling, a sleep loop, or a time-based schedule. A user-authorised scheduled check may use the native scheduling tool when available, but it is not event delivery and does not survive app or machine shutdown unless that service proves it.

Record the absolute installed plugin root and version for this run. Read workflow resources from that pinned plugin path, such as `<plugin>/skills/poteto-mode/playbooks/opening-a-pr.md`. Do not tell workers to read `pstack/skills/...` from the target application's trunk. A source refresh is valid only when the recorded plugin source checkout contains the converted Codex resources.

## Frame and pilot

1. State the done predicate as something that can be checked against the real artifacts. Quantify the units, tracks, dependencies, expected PRs, verification bar, and time budget.
2. Route here only when the work exceeds one agent's session budget. If it does not, use Autonomous run. If the merge authority is withheld, use Autopilot-stack for the PR queue.
3. Separate independent units from true dependencies. Independent units get separate PRs based on trunk. Stack only a PR that depends on another PR, as described in **Size and stacks** in `playbooks/opening-a-pr.md`.
4. Put the predicate, units, owners, dependencies, PRs, latest head SHAs, verifier, verdicts, and open user gates in the existing project tracker or CODEX.md's durable notes record. Use the **show-me-your-work** trail for decisions and evidence. Do not create a parallel runtime database.
5. Run one representative unit through its brief, implementation, PR, verification, and authorised landing or handoff. Fix gaps in the brief or acceptance criteria before expanding. For near-identical units, the first unit is the pilot and later units can start once its checks prove the recipe.

## Brief and fan-out

Each brief stands alone. It names:

- The goal and done predicate.
- The exact paths the owner may change and the paths it must leave alone.
- Required context, including full upstream reports when the unit depends on them.
- Acceptance criteria and the exact verification commands or live-surface procedure.
- The expected base branch and SHA, worktree or branch ownership, and whether remote placement is required.
- Actions that need separate user authority, such as merge, force-push, deployment, deletion, or external messages.
- The report fields: status, branch, current head SHA, PR, checks run, evidence, blockers, and follow-ups.

Use a rolling window sized to what the coordinator can supervise. Start dependent units only after their required inputs are available. Native subagents run in their isolated local worktrees. Remote units go through the configured adapter. Never let two writers share a branch or worktree.

## Drain and verify

At each native completion notification or authorised event, update the tracker and inspect the artifact. Do not treat an agent summary as evidence. Read the diff, check the reported commands, and read the live PR state through the selected forge.

Before accepting a result, read the PR's current head SHA from the forge and compare it with the reported and verified SHA. If they differ, the verdict is stale. Reconcile the new diff and rerun the checks that the new head invalidated. Record verdicts against the exact current head.

Every PR gets an independent verifier who did not author it, on a different model family. The verifier checks the relevant commands and real behavior, using the control skill named by the plan for live surfaces. The coordinator reads the evidence and verifies the result against the current head SHA. CI is evidence, not a verdict. A missing lane or unavailable verifier is BLOCKED, not a pass.

For a PR stack, the coordinator sequences dependency changes and asks each PR owner to update its own branch and PR base. Recompute the dependency order and current head SHAs after each merge or restack. Do not close, force-push, or merge a PR without the authority required for that action.

## Failure and close

Do not resume an idle agent merely to check its status. Use native status tools, task IDs from the adapter, branch updates, and current PR state. Retry by cause and cap retries at two. A late result must be reconciled against the PR's current head before any part is accepted. If work is abandoned, record what failed, its last evidence, and whether its acceptance criteria remain covered.

Ask the user only for a real product decision, an irreversible action, missing authority, or a dead end that remains after a grounded replan. Keep reversible work moving and route around a gate when possible.

Close only after checking the done predicate against the real artifacts, reconciling every worker, and confirming each PR's current state and verdict at its current head. Keep the tracker and decision trail intact.

**Reply:** what landed or was handed off against the goal, each PR's current state and head-specific verdict with its link, what was dropped and why, any adapter or verification gaps, and the decisions waiting on the user.
