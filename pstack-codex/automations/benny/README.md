# Benny for Codex

Benny contains two dormant automation workflows for Slack issue reports. One triages each report. The other reproduces confirmed bugs and may prepare a small draft fix. These files are direct instructions, not registered slash skills.

The full workflow needs an **external event and execution adapter**. The local Codex app can schedule work, but it does not supply the new-Slack-report event trigger used by Benny. Do not replace that trigger with polling without the user's explicit choice. An eligible ChatGPT web task may supply an app event, but it still needs a tested execution adapter for the repository, app control, history, and evidence.

## Set it up

1. Point Codex at [`FOR_AGENTS.md`](./FOR_AGENTS.md) and name the target repository.
2. Merge this whole directory into the target at `.agents/automations/benny/`. Preserve destination-only files and merge local edits after review.
3. Install and trust `pstack-codex` in that project using the plugin's `CODEX.md` and `setup-pstack` instructions. Project installation uses a supported `.agents/plugins` marketplace and activation in `.codex/config.toml`. Never copy Cursor settings into Codex.
4. Keep user configuration outside the copied pack, for example in `.agents/benny/`. Adapt [`configuration.example.yaml`](./templates/configuration.example.yaml) and [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md). Keep secrets in the configured secret store.
5. Commit the pack, plugin project configuration, and referenced secret-free Benny configuration before a live run. Do not commit captures or tokens.
6. Validate the event and execution adapters, review one automation at a time, then run the harmless thread-safety and app-control checks before enabling normal traffic.

This conversion does not install, register, enable, or send messages from either automation. Read [`PARITY.md`](./PARITY.md) for the adapter contract and live checks still pending. The plugin-wide tool contract is in `pstack-codex/CODEX.md`; external integration requirements are in `pstack-codex/docs/adapters.md`.
