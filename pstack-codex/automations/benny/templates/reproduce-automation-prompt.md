# Reproduce automation prompt

> Source material for the reviewed adapter handoff. Use only after verifying that the copied pack and referenced configuration are committed at the exact repository revision the executor will run. The local Codex scheduler does not supply a Slack event trigger; a tested event and execution adapter is required.

Read and follow `.agents/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` for this run.

Configuration source. Include this repository-relative path only when it is committed in the same target repository. Otherwise paraphrase the configured values. Never use a plugin source or cache path:

```text
{{BENNY_CONFIG_PATH}}
```

Trigger:

```json
{
	"source_channel_id": "{{SLACK_CHANNEL_ID}}",
	"ts": "{{SLACK_MESSAGE_TS}}",
	"thread_ts": "{{SLACK_THREAD_TS_OR_EMPTY}}"
}
```

The reviewed adapter definition must describe this as a new top-level report in the configured source Slack channel. It should include the configured repository, default branch, issue tracker, control adapter, feature map, and draft pull request capability.

Treat the source channel and root thread timestamp as immutable. If either is missing or does not match configuration, stop without posting.

Wait for a configured triage marker from the configured triage identity in this exact thread. Proceed only for `[benny:bug]` or `[benny:performance]`.

Require the configured control-adapter skill before attempting a repro. Reproduce the exact discriminating symptom twice through the real UI. Verify existing pull requests or commits without authoring over them. Attempt a bounded fix only after a confirmed repro and the operational file's fix gate.

Require the configured adapters and model roles to pass setup. Reject unauthenticated or ambiguous trigger payloads. Preserve timestamps as exact strings. Do not poll for new reports as a silent fallback.

The coordinator is the only Slack poster. Codex workers may inherit tools and credentials: delegate only when the executor removes all Slack credentials and write capabilities; otherwise keep the work in the coordinator. Every child prompt must forbid `SendSlackMessage`, `PostToSlack`, `chat.postMessage`, and all other Slack writes. Children return findings only.

Never post a root message in the source channel.
