# pstack to Codex feature map

Source: `pstack` version **0.15.25**, commit `f713f14203cd6420cec13cd7c55c32d598dbab68`. The Cursor copy stays at `../pstack/`. This port keeps its 54 plugin skills, 23 playbooks, two delegate roles, scripts, reference material, and three dormant Benny procedures in a separate folder.

**This map does not certify live parity.** Retaining an instruction or passing a local test does not prove model, UI, service, scheduling, or restart behaviour. The acceptance table below records those gates separately.

## Reading the map

- **Direct** means the instruction or algorithm can remain, with portable metadata and paths.
- **Adapted** means a Codex runtime mechanism replaces a Cursor mechanism. Prove the replacement before claiming parity.
- **External** means full behaviour needs a configured service or provider outside the plugin. A contract is not a working adapter.
- **Pending** means no live parity result is established by this map. Every row below is Pending, including Direct rows.

All runtime substitutions follow [CODEX.md](../CODEX.md). External requirements are defined in [adapters.md](./adapters.md). Local subagents share a filesystem. Give writers separate worktrees or disjoint file ownership; do not describe them as isolated cloud machines. Do not silently substitute several same-family agents for a required mixed-family panel. Do not silently replace an event trigger with polling.

## The 30 workflow skills

Names match the original skill directory names. The 24 principle skills follow in their own table.

| Skill | Route | Function retained and remaining proof |
|---|---|---|
| `architect` | Adapted + External | Grounding, competing interface sketches, optional agreement panel, implementation, and redesign. Prove delegated model roles; mixed-family agreement needs a provider adapter. |
| `arena` | Adapted + External | Independent candidates, separate outputs, cross-judging, base selection, grafting, and final proof. Prove distinct families, blinded judging, and filesystem isolation. |
| `automate-me` | Adapted | Workspace-scoped history mining, direct user input, personal mode authoring, and prose review. Prove full Codex history access and real skill authoring validation. |
| `benchmark-checklist` | Direct | Limiter, tuning, errors, repeated measurements, relevance, and proof the measured work ran. Exercise on a real benchmark. |
| `blast-radius` | Adapted; External for mixed-model review | Trace downstream effects and prove the load-bearing safety fact with running code. Its wide-change Arena lane requires the same mixed-family adapter. |
| `bro` | Direct | Restate the last message in plain language. Check output on representative input. |
| `correct` | Direct | Mine repo evidence for repeated mistakes, enforce at the highest useful level, and prove checks catch past failures. Check a real correction end to end. |
| `create-verification-skill` | Adapted | Generate a project skill, launch/drive contract, feature map, evidence rules, and cleanup. Prove skill discovery and actual app driving. |
| `figure-it-out` | Adapted + External where required | Design an auditable playbook, run hypotheses, log decisions, and verify. Prove delegated roles and the independent audit trail lane. |
| `how` | Adapted | Parallel source explorers, explanation, and evidence coverage. Prove native subagent invocation and aggregation. |
| `in-your-own-words` | Direct | Restate the user's goal and problem before work. Check output and invocation policy. |
| `interrogate` | Adapted + External | Intent, independent model-family reviews, strict code-quality lens, synthesis, and lead judgment. Different personas on one family do not meet its design. |
| `ketchup` | Adapted | Read-only account of changes since the user's last message, live state, and actionable decisions. Prove thread/history access and timing boundaries. |
| `maintain-verification-skill` | Adapted | Source wave, serial live feature pass, health checks, retained evidence, cleanup, and at most one PR of proven corrections. Prove app and generated-skill integration. |
| `make-bot-ui` | External | Dashboard, wake buttons, sender-key handoff, Tailscale, and bot execution. Needs webhook receiver, authenticated execution bridge, and secret handoff. Cursor secret-card UI has no bundled equivalent. |
| `no-comments` | Adapted | Invoke Comment Sicko, inspect its report, apply accepted findings, and offer structural encodings. Prove role loading and report-only delegate behaviour. |
| `poteto-help` | Adapted | Choose a fitting skill, playbook, or principle and hand back a usable prompt. Prove Codex invocation and all guide references. |
| `poteto-mode` | Adapted + External where required | Router, exact playbook steps, principles, delegation, evidence, and reporting. Persistent use requires explicit opt-in project instructions; Cursor's custom-mode keyboard/UI behaviour changes. |
| `recall` | Adapted | Reconstruct scoped recent context from chat history, shared records, and live git/PR state. Prove project/time scope, full-event access, and child-chat handling. |
| `reflect` | Adapted + External where required | Three review lenses, synthesis, structural enforcement check, and concrete skill edits. Prove scoped history, configured roles, authoring, and connected-source access. |
| `setup-pstack` | Adapted | Detect available roles, retain deliberate overrides, select budget, validate, and save configuration. Codex role JSON separates model, reasoning effort, and speed. Prove actual model availability; Cursor slugs are not portable. |
| `sharpen` | Direct | Frame the task as an expert would without making the user's choices. Check output on representative tasks. |
| `show-me-your-work` | Adapted + External | TSV decisions, full-transcript audit, and review by a different model family. Prove log receipts against actual tool events and a genuinely different-family reviewer. |
| `swarm` | Adapted + External | Scoped workers, independent slices or races, aggregation, and one report. Native local workers cover local delegation; Cursor cloud execution and restart survival need a remote-worker adapter. |
| `tdd` | Direct | Cheap local failing test, minimal fix, and behaviour proof. Run a real red/green case. |
| `teach` | Adapted | Compose How and Why into one explanation with progressive diagrams. Prove both underlying evidence lanes and synthesis. |
| `technical-writing` | Direct | Retain the layered document standard and its rules for commits and PR prose. Review representative outputs. |
| `typescript-best-practices` | Adapted | Retain type guidance and examples. Replace Cursor `paths` triggering with Codex discovery or explicit scoped instructions; prove invocation in a TypeScript task. |
| `unslop` | Direct | Retain the prose cleanup rules. Review representative outputs. |
| `why` | Adapted + External | Discover evidence sources, investigate categories in parallel, qualify claims, and cite evidence. Needs authorised equivalents for each queried tracker, chat, docs, warehouse, observability, or error service. Missing categories remain visible gaps. |

## The 24 principle skills

All are **Direct; Pending**. Their rules remain instruction-level contracts. The runtime tool policy still governs any delegation, persistent work, or irreversible action they request.

| Exact skill name | Retained purpose |
|---|---|
| `principle-attack-the-premise` | Test a shared premise after repeated failed fixes. |
| `principle-boundary-discipline` | Validate at boundaries and keep internal logic simple. |
| `principle-build-the-lever` | Build a reusable tool or proof for non-trivial work. |
| `principle-encode-lessons-in-structure` | Enforce recurring lessons structurally. |
| `principle-exhaust-the-design-space` | Compare competing prototypes. |
| `principle-experience-first` | Prefer polished user behaviour. |
| `principle-explain-the-number` | Explain and validate measured results. |
| `principle-fix-root-causes` | Trace and fix the first failing mechanism. |
| `principle-foundational-thinking` | Settle core types, data structures, and ownership. |
| `principle-guard-the-context-window` | Delegate bulk and retain concise findings. |
| `principle-laziness-protocol` | Prefer deletion and the smallest useful change. |
| `principle-make-operations-idempotent` | Converge after partial runs. |
| `principle-migrate-callers-then-delete-legacy-apis` | Move callers and remove obsolete APIs. |
| `principle-minimize-reader-load` | Reduce indirection and hidden state. |
| `principle-model-the-domain` | Express the domain in data structures. |
| `principle-never-block-on-the-human` | Continue authorised reversible work; preserve required approval boundaries. |
| `principle-outcome-oriented-execution` | Converge on the intended architecture. |
| `principle-prove-it-works` | Verify the real artifact. |
| `principle-redesign-from-first-principles` | Design for the requirement from the foundation. |
| `principle-separate-before-serializing-shared-state` | Remove sharing before adding serial execution. |
| `principle-sequence-verifiable-units` | End each work unit in a verifiable state. |
| `principle-subtract-before-you-add` | Remove dead weight before adding structure. |
| `principle-test-behavior-not-implementation` | Assert public behaviour. |
| `principle-type-system-discipline` | Encode valid states and parse boundaries. |

## The 23 playbooks

Names below are exact filenames under `skills/poteto-mode/playbooks/`. All are **Pending**. Most compose several skills, so their acceptance includes the dependencies named above.

| Playbook | Route | Required Codex proof or external dependency |
|---|---|---|
| `authoring-a-skill.md` | Adapted | Use an available Codex authoring skill or its explicit draft/validate/iterate process. Validate metadata, links, structural examples, and discovery; a name substitution is not an equivalent eval loop. |
| `autonomous-run.md` | Adapted + External where required | Active-run Goals and authorised scheduled continuation replace Cursor loops only when supported. Prove stop, wake, cancellation, and recovery semantics. |
| `autopilot-full.md` | Adapted + External | One durable owner per PR, code-ready SHA, independent live verdicts, merge gates, and drift audit. Remote owners, mixed-family verification, and restart recovery need adapters. |
| `autopilot-stack.md` | Adapted + External | Preserve a linear base-branch stack and operator landing boundary. Prove owner replacement, exact-head verdicts, and authorised continuation. |
| `babysit.md` | Adapted | Preserve drive/background/threads-only/check modes, merge frontier, GitHub watcher, Origin fallback, and meaningful-change reporting. Prove watcher wakes and schedule lifecycle; no second polling loop. |
| `bug-fix.md` | Adapted | Reproduce, binary-search the mechanism, delegate a scoped fix, and verify runtime behaviour. Prove local app access and supported role configuration. |
| `eval.md` | Adapted + External | Preserve sanitized isolated candidate environments, organic prompts, blinded labels, a different-family judge, and tool-call history checks. Prove all five, including actual files opened. |
| `feature.md` | Adapted | Domain shape, interface sketch, delegated implementation, and real behaviour proof. Prove native role loading and control tools. |
| `hillclimb.md` | Adapted | Baseline, hypotheses, measurements, accepted wins, and commits. Prove a full cycle and any authorised long-run continuation. |
| `investigation.md` | Adapted + External where required | Read-only How/Why investigation. Prove source discovery and explicit gaps when a service is missing. |
| `multi-phase-plan.md` | Adapted + External | Preserve phased plan, PR dependencies, live/perf gates, prototype evidence, and program checks. Prove updated scheduling markers agree with `check-plan.mjs`. |
| `opening-a-pr.md` | Adapted | Separate worktree, ordered commits, Deslop, Comment Sicko, clear PR body, and no unsolicited babysit. Prove branch/WIP preservation and native PR attachment where available. |
| `orchestrate.md` | Adapted + External | Preserve standing orders, briefs, inbox, units, ledger keyed by PR/head, stacker ownership, and recovery. Store persistence is local; durable remote execution, status, cancellation, and restart survival need a backend. |
| `pause-safely.md` | Adapted | Stop delegated work, preserve owned changes and durable state, and write an exact resume action. Prove cancellation and no unrelated WIP inclusion. |
| `perf-issue.md` | Adapted | Trace a real metric from baseline through diagnosis and improvement. Prove control-tool and benchmark lanes. |
| `prototype.md` | Adapted | Independent disposable prototypes, comparison, and an empirical decision. Prove isolated outputs and clean retention/cleanup boundaries. |
| `refactoring.md` | Adapted | Preserve behaviour while changing structure, with scope and evidence. Prove delegated work and public behaviour checks. |
| `runtime-forensics.md` | Adapted + External where required | Live instrumentation, hypothesis elimination, and runtime proof. Requires the actual target environment and any observability integration. |
| `session-pickup.md` | Adapted + External where required | Rebuild context from full scoped history, durable state, branches, PRs, and actual worker status. Remote reattachment needs a backend; transcript mtime is not liveness. |
| `shipping.md` | Adapted + External | Independent verifier per PR, real control surface, exact verified head, contiguous bottom-up landing, and queued watcher. Original cloud verifiers need a remote backend. Merge still needs user authority. |
| `trace-forensics.md` | Adapted | Read captured profiling artifacts and confirm the proposed mechanism. Prove the artifact reader and runtime follow-up on a real target. |
| `visual-parity.md` | Adapted | Compare implementations on the actual UI, capture evidence, and iterate to parity. Prove the chosen control and screenshot tools. |
| `worktree-cleanup.md` | Adapted | Read-only size/git/PR/activity audit followed by explicit deletion authority. Codex history must replace Cursor paths; pinned/live chat and sibling-worktree usage need a current status check. |

## Agents, helpers, and bundled dependencies

All rows are **Pending**. Custom agent configuration is an optional explicit install step; merely shipping a TOML file does not register it in every Codex host.

| Source component | Route | Preserved contract and proof needed |
|---|---|---|
| `agents/poteto-agent.md` | Adapted | Delegate reads Poteto Mode in full before work, including principles, while the parent owns the playbook. Prove custom-agent installation/discovery or the documented explicit-prompt fallback. |
| `agents/comment-sicko.md` | Adapted | Scoped comment review with its exception list, evidence checks, and report-only boundary. Prove role loading and that the delegate does not edit application code. |
| `show-me-your-work/scripts/log.sh` and `references/decision-log-template.tsv` | Direct | Keep TSV schema and logger behaviour. Test actual rows and audit against full tool events. |
| `poteto-mode/scripts/orch/orch.ts` and `orch/store.ts` | Adapted | Keep board/inbox/unit/ledger state and locking; use Codex storage paths. Local files do not spawn, wait, wake, or establish remote-agent liveness. Prove restart reconciliation separately. |
| `poteto-mode/scripts/watch-pr/` | Direct | Keep CLI, GitHub reads, policy, rendering, types, launcher, tests, and current-head verdict logic. Cursor Bugbot identity matches refer to the external GitHub bot and may remain. Test fixtures do not prove live GitHub/Origin integration. |
| `poteto-mode/scripts/check-plan.mjs` and `check-plan.test.ts` | Adapted | Original validator requires literal `/loop 1h`. Port the validator and plan template together to the explicit Codex continuation contract. Preserve unit/live/perf gates and lane/evidence checks. |
| `poteto-mode/scripts/worktree-audit.sh` | Adapted | Preserve size, age, base/merge, WIP, remote, PR, activity, and review buckets. Replace Cursor transcript lookup. Missing activity or unavailable status must not certify a worktree safe to remove. |
| `poteto-mode/scripts/bootstrap.ts`, `package.json`, `bun.lock`, and helper tests | Adapted | Retain Bun/Commander bootstrap, frozen dependency installation, helper tests, and TypeScript checks. Prove runtime availability and dependency install separately from tests. |
| Skill `references/`, playbook references, guide pages/images, logo, and MIT licence | Adapted | Keep source material and relative links; update runtime instructions and provenance. Static link checks do not prove the described UI flow. |
| Companion `deslop` from `cursor-team-kit` | Adapted | Bundle the formerly external cleanup procedure with its source provenance. Prove invocation before commit. |
| Companions `control-cli` and `control-ui` from `cursor-team-kit` | Adapted + External where required | Bundle the formerly external control procedures. A supported browser/device/CLI driver and target app access remain runtime requirements; prose alone does not drive an app. |
| Cursor built-in `create-skill` | Adapted | Use a real Codex skill authoring procedure with metadata/link checks, structural cases, and iteration. Description optimisation and evaluation require their own evidence; do not claim automatic equivalence. |
| Cursor custom mode, `Task`, `ReadMcpResource`, `AskQuestion`, and `/loop` surfaces | Adapted | Use explicit mode instructions, available native delegation/tool discovery, supported questions, and authorised Goals/schedules. Report missing capabilities rather than inventing tool support. |

## Benny's three dormant procedures

Benny stays a directly read automation pack, not three automatically registered slash skills. User configuration, feature maps, routing maps, and secrets stay outside source-managed pack files. See [Benny's parity checklist](../automations/benny/PARITY.md) for the operational acceptance gates.

| Procedure | Route | Retained behaviour and gap |
|---|---|---|
| `setup-benny` | Adapted + External | Copy/merge the pack, preserve destination-only files, validate config and shared skills from a fresh target-repo session, then configure two automations only when requested. Prove project-scoped discovery, trusted identities, permissions, and event backend readiness. |
| `triage-issue-reports` | External | Read the original thread and attachments, classify, trace ownership, deduplicate tracker issues, and send one marked reply in that thread. Needs Slack event delivery, Slack/tracker tools, trusted identity, and idempotency proof. No silent scheduled-polling substitute. |
| `reproduce-and-fix-issues` | External | Wait for trusted triage, respect existing ownership/fixes, reproduce twice through real UI, retain media/state evidence, attempt a bounded fix, and open a draft PR only after proof. Needs event/execution bridge, repo runtime, control adapter, media review, and service credentials. |

The immutable source channel/thread, no root posts in the source channel, no Slack credentials or posting access for delegates, fail-closed prerequisites, draft-only PRs, and no merge/deploy authority remain required contracts. No Slack automation is enabled by installing this plugin.

## Acceptance evidence

Keep these gates separate in the PR and any later parity report. A completed lower gate does not satisfy a higher one.

| Gate | Evidence required | Status in this map |
|---|---|---|
| Source coverage | Exact source skill/playbook/agent/procedure inventory, companion provenance, and unchanged Cursor tree. | Inventory mapped here; implementation checks reported separately. |
| Local static validation | Manifest/metadata validation, relative links, reference existence, no executable Cursor-only APIs, and matching plan markers. | Passed locally: package validator; source hashes, resource destinations, skill policies, TOML agents, links, and marketplace path. |
| Local helper behaviour | Bun helper suites, TypeScript checks, shell syntax, role-config and scoped-history fixtures, including full tool-event preservation. | Passed locally: 69 Bun tests, strict TypeScript, 23 Python runtime, retention and shell-fixture tests, shell syntax. Service fixtures do not establish live parity. |
| Fresh install/discovery | Fresh Codex project session finds the plugin and intended skills; manual-only invocation remains manual; optional custom agents resolve after explicit installation. | Passed CLI install and app-server discovery on Codex 0.162.1 in an isolated home: 57 enabled namespaced skills, zero loader errors, Benny absent. Desktop UI and invocation-policy behaviour still pending. |
| Local workflow parity | Representative How, TDD, comment review, generated verification skill, CLI/UI control, and persistent-mode opt-in/opt-out. | Pending live test. |
| Model/provider parity | Actual supported role models, separate effort/speed handling, different-family candidates/reviewers, blinded judge, and explicit failure when unavailable. | External adapters and live tests pending. |
| Remote execution parity | Isolated worker launch, status, cancellation, branch/artifact transfer, exact-head verification, parent restart, and reattachment without duplicate work. | External adapter and live tests pending. |
| History parity | Active/project/time scoping, child relationships, archived or inaccessible gaps, full command/file/tool events, and truthful log/Eval audits. | Pending real-session test. |
| Continuation parity | Authorised active Goal or schedule, watcher wake, cancellation, quiet unchanged state, stop conditions, and restart behaviour. | Pending host-specific live test. |
| GitHub/forge parity | Real PR head/readiness, Bugbot thread handling, merge frontier, queued stack, and independent verifier receipts. Origin is a separate supported fallback, not implemented by the GitHub watcher. | Pending live service test. |
| Bot UI parity | Authenticated webhook, sender key, secure secret handoff, event receipt, dashboard action, and real Codex wake/result. | External backend and live tests pending. |
| Benny parity | Committed target-repo pack, fresh dependency discovery, Slack event/thread identity, tracker dedupe, real reproduction/media proof, and draft PR. | External backend and live tests pending. |

Full parity can be claimed only when every required external adapter is implemented and the relevant live gates pass. Until then, report each unsupported or untested lane with its concrete missing prerequisite. Do not turn a skipped lane into a pass.
