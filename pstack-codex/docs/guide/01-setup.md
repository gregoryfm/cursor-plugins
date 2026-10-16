# Set up pstack for Codex

Follow the package [installation instructions](../../README.md#install-locally). Install through the repository's Codex marketplace, then invoke `$setup-pstack`. Keep Cursor's pstack installed separately if you use it there.

## Choose models and a budget

Setup reads `.agents/pstack/config.json` in the target repository. It shows every role and asks for a budget and actual supported models. The four budget labels are unlimited (max effort), large (xhigh), medium (high), and small (medium). These are requests, validated against the selected executor. Model, reasoning effort, and speed remain separate.

Ordinary missing roles inherit the parent. Mixed-family panels require configured distinct families and verified provider access. They remain BLOCKED until available. Do not replace them silently with multiple personas. See [adapter requirements](../adapters.md).

## Run your first task

```text
$poteto-mode explain how job cancellation reaches the worker. cite the source and keep this read-only.
```

Use the qualified skill name shown by the client if needed. Poteto reads the full skill and routes to the matching playbook. Explicit-only leaves stay available through routing or explicit invocation.

For standing behaviour, opt in to a scoped AGENTS.md instruction that reads the installed absolute poteto-mode path for relevant turns. This is a different activation mechanism from Cursor's sticky mode. No global instructions or hooks change during installation.

Local delegates share filesystem state. Setup can install the two TOML agent roles after a dry-run preview; CODEX.md supplies the full-prompt fallback. Put parallel writers in separate worktrees and isolate ports/data. Remote placement requires the external worker adapter.

Next: [Route a task through Poteto](./02-poteto-mode.md).
