# pstack for Codex

Pstack's engineering workflows for Codex. This package preserves the 54 original skills, 24 principle leaves, 23 playbooks, two delegate roles, scripts, guides, and dormant Benny pack. It also bundles `deslop`, `control-cli`, and `control-ui` from cursor-team-kit so verification and shipping have their companion procedures.

The separate `../pstack/` package is unchanged. Source baseline: pstack 0.15.25 at `f713f14203cd6420cec13cd7c55c32d598dbab68`. The original MIT licence and the companion skills' [licence](licenses/cursor-team-kit.txt) are retained. [Source map](docs/source-map.json) records each original resource and its port destination.

**This is a Codex port with explicit parity gaps, not a claim of full runtime equivalence.** Mixed-family panels, remote workers, webhook bots, and Benny's Slack triggers require external adapters. Every live acceptance check is listed in the [parity map](docs/parity.md). No service, schedule, model provider, or credential is installed automatically.

## Install locally

Requires a current local Codex client with plugins and subagents. Python 3.11+ runs the local helper and validation tools. Bun runs the preserved orchestration and PR-watcher tools. Git, GitHub CLI, jq, and repo-specific app harnesses are needed for the workflows that use them. Authenticate GitHub CLI separately.

This repository includes `.agents/plugins/marketplace.json` at its root. From the repository root, register its local marketplace if the client has not discovered it:

```sh
codex plugin marketplace add .
codex plugin add pstack-codex@gregory-codex-plugins
```

The CLI command installs into the active Codex home. Alternatively, in the desktop Plugins directory, select **Gregory Codex Plugins**, install **pstack for Codex**, and start a new chat. Restart the app if the marketplace has not appeared. For a trusted target project, an explicit project enable setting is:

```toml
[plugins."pstack-codex@gregory-codex-plugins"]
enabled = true
```

Merge that entry into the target's `.codex/config.toml` only when enabling the plugin there. Do not replace an existing config. The marketplace path is relative to this repository root. If moving the package to a different marketplace, update its source path. Do not add it to the Cursor marketplace.

Official references: [plugin packaging](https://developers.openai.com/plugins/build/plugins), [skills](https://learn.chatgpt.com/docs/build-skills), [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Start a task

Invoke the name shown in your client, such as:

```text
$pstack-codex:poteto-mode investigate why the cache survives logout. keep this read-only and cite the runtime path.
```

Plugin-qualified names may appear in the selector. Existing explicit-only skills stay explicit-only. Poteto routes to them by reading their SKILL.md files. `$setup-pstack` configures role models and reasoning. Unconfigured ordinary roles inherit the parent. Required diverse panels do not silently fall back to same-family agents.

Read [CODEX.md](CODEX.md) for the actual runtime contract. Native subagents share the filesystem. Cloud-required work needs the remote-worker adapter. Codex's persistent project instructions replace the effect of a sticky mode only if the user opts in. Goals and scheduled heartbeats replace continuation where supported; local scheduling does not survive a powered-off machine.

## Configure delegates and models

From the target repository, use the installed plugin's absolute path:

```sh
python3 <plugin>/scripts/runtime.py doctor
python3 <plugin>/scripts/runtime.py install-agents --project <target-repo>
```

The second command previews installation. Add `--apply` to copy both TOML roles into the target's `.codex/agents/`. It refuses conflicting files and is idempotent. Agent files are not auto-discovered from the plugin root. CODEX.md also defines a full-prompt fallback when the named role is unavailable.

Copy `templates/config.example.json` to the target `.agents/pstack/config.json`, then run `$setup-pstack` to choose actual available models. Keep secrets out of that file. See [adapter contracts](docs/adapters.md) before configuring external providers. `check-config` checks structure; it never claims credentials or provider access work.

## Available workflows

| skill | use it when |
|---|---|
| [`$poteto-mode`](./skills/poteto-mode/SKILL.md) | default entry point for any non-trivial task. |
| [`$poteto-help`](./skills/poteto-help/SKILL.md) | you're new to pstack, or unsure which skill, playbook, or principle fits. finds out what you're trying to do, answers that part, and hands you a prompt to type. runs only when you type `$poteto-help`. |
| [`$in-your-own-words`](./skills/in-your-own-words/SKILL.md) | you want the agent to play back your goal and the problem before it starts. runs only when you type `$in-your-own-words`. |
| [`$sharpen`](./skills/sharpen/SKILL.md) | you want a task approached the way a top expert would, aimed at what you're really after, without overspecifying it or deciding your choices for you. |
| [`$how`](./skills/how/SKILL.md) | you want a walkthrough of how a subsystem works. |
| [`$why`](./skills/why/SKILL.md) | you want to know why something was built this way. discovers available MCPs at run time and queries each evidence category in parallel (source control, issue tracker, long-form docs, real-time chat, infra observability, error tracking, analytics warehouse). |
| [`$recall`](./skills/recall/SKILL.md) | you're starting or resuming work and want your recent context on a topic rebuilt from your own chat history and the shared record, handed back as a tight current-state brief. |
| [`$ketchup`](./skills/ketchup/SKILL.md) | you want what changed in this chat since your last message, in a few plain sentences and small visuals, with just enough context on each action item to make the call. |
| [`$blast-radius`](./skills/blast-radius/SKILL.md) | you have a small-looking change and want to know what else it could break, with the one fact it's safe because of proven by running code, not asserted. |
| [`$architect`](./skills/architect/SKILL.md) | you're about to write code that crosses a function boundary and want the caller's usage, types, and module shape settled first. |
| [`$arena`](./skills/arena/SKILL.md) | you want N parallel attempts at the same thing, then to grab the best parts of each. |
| [`$swarm`](./skills/swarm/SKILL.md) | you want N parallel workers across different slices or races, then one aggregated report. |
| [`$interrogate`](./skills/interrogate/SKILL.md) | you have a diff and want different models to try to break it, including a strict code-quality lens. |
| [`$automate-me`](./skills/automate-me/SKILL.md) | you want your own `-mode` skill, drafted from how you've actually worked. |
| [`$make-bot-ui`](./skills/make-bot-ui/SKILL.md) | you want a page or dashboard whose buttons wake a configured bot through the webhook adapter, including the sender-key handoff and Tailscale. |
| [`$setup-pstack`](./skills/setup-pstack/SKILL.md) | you want to pick which models pstack uses per role. detects your models and writes a config rule. |
| [`$reflect`](./skills/reflect/SKILL.md) | a long task landed and you want the recipe captured as a skill edit. |
| [`$correct`](./skills/correct/SKILL.md) | you keep correcting agents for the same mistakes. mines history for mistake classes, fixes each at the highest level that works (architecture, then types, lint, and ci, then tests, with docs last), and keeps a table pairing each rule with what enforces it. |
| [`$teach`](./skills/teach/SKILL.md) | you want to actually understand a change or subsystem, not just have it summarized. runs how + why and weaves one plain explanation, built up diagram by diagram. |
| [`$tdd`](./skills/tdd/SKILL.md) | you're fixing a bug and there's a cheap local test path. write the failing test first, then the fix. |
| [`$benchmark-checklist`](./skills/benchmark-checklist/SKILL.md) | you ran a benchmark or measured a speedup or regression. vets the number (limiter, tuning, errors, repeat runs, end-to-end relevance) before you report or act on it. |
| [`$no-comments`](./skills/no-comments/SKILL.md) | strip comments before review; spawns Comment Sicko, fixes accepted findings, offers encodings for claimed constraints. |
| [`$typescript-best-practices`](./skills/typescript-best-practices/SKILL.md) | you're reading or editing typescript. grounds the type-system-discipline principle in syntax. |
| [`$figure-it-out`](./skills/figure-it-out/SKILL.md) | no bundled playbook fits. designs a rigorous, auditable playbook for the task. |
| [`$show-me-your-work`](./skills/show-me-your-work/SKILL.md) | you want a reviewable decision trail. logs decisions to a tsv you can commit. |
| [`$create-verification-skill`](./skills/create-verification-skill/SKILL.md) | your project has no scripted way to prove app behavior. generates a project-local verify skill with a feature map, for any language or platform. |
| [`$maintain-verification-skill`](./skills/maintain-verification-skill/SKILL.md) | your verify skill's feature map has drifted from the app. source wave + one live pass, at most one PR of proven corrections. |
| [`$unslop`](./skills/unslop/SKILL.md) | you're cleaning up writing. removes AI tells. |
| [`$bro`](./skills/bro/SKILL.md) | you want the last message restated in plain human language, no jargon. |
| [`$technical-writing`](./skills/technical-writing/SKILL.md) | layered doc standard (Diátaxis + Google developer style + STE + Global English) for docs, RFCs, readmes, PR descriptions, commit messages. |



All 24 principles remain under `skills/principle-*/`. All 23 playbooks remain under `skills/poteto-mode/playbooks/`; the [complete map](docs/parity.md) names each one. The [guide](docs/guide/README.md) covers prompting, design, building, verification, shipping, and long runs. Its illustrations are inherited explanatory artwork, not screenshots of Codex or evidence of live parity.

## Benny and webhook bots

Benny remains a dormant pack. Point Codex at [Benny's entry file](automations/benny/FOR_AGENTS.md) and name the target repository. Its operational files stay outside the registered skill catalog. The [Benny parity checklist](automations/benny/PARITY.md) lists Slack event delivery, worker isolation, tracker compensation, app control, and before/after evidence gates. Desktop time schedules cannot silently replace Slack events.

`$make-bot-ui` retains the dashboard and Tailscale workflow, but requires an authenticated webhook and execution bridge. No Cursor routine API, native secret-request card, or opaque credential guarantee is assumed.

## Validate the package

From this repository root:

```sh
python3 pstack-codex/scripts/validate.py
python3 -m unittest discover -s pstack-codex/tests -v
cd pstack-codex/skills/poteto-mode/scripts
bun install --frozen-lockfile
bun test orch watch-pr check-plan.test.ts
bun run typecheck
```

Validation checks resource retention, original source hashes, skill metadata/policy, TOML roles, and local links. Runtime tests use temporary fixtures and a local adapter process. They do not contact model providers, Slack, or other live services. Retained helper tests exercise orchestration storage, PR policy/query parsing, and plan validation. Fresh-client plugin discovery and live workflow tests stay separate in the parity map.
