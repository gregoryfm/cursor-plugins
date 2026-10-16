# Triage automation prompt

> Source material for the reviewed adapter handoff. Use only after verifying that the copied pack and referenced configuration are committed at the exact repository revision the executor will run. The local Codex scheduler does not supply a Slack event trigger; a tested event and execution adapter is required.

Read and follow `.agents/automations/benny/skills/triage-issue-reports/SKILL.md` for this run.

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

The reviewed adapter definition must describe this as a new top-level report in the configured source Slack channel.

Treat the source channel and root thread timestamp as immutable. If either is missing or does not match configuration, stop without posting or writing to the issue tracker.

The committed operational file owns classification, attachment review, cause tracing, routing, dedupe, tracker writes, and the final verdict. Post no progress messages. Never post a root message in the source channel.

Require the configured adapters and model roles to pass setup. Reject unauthenticated or ambiguous trigger payloads. Preserve timestamps as exact strings. Do not poll for new reports as a silent fallback.

The coordinator is the only Slack poster. Codex workers may inherit tools and credentials: delegate only when the executor removes all Slack credentials and write capabilities; otherwise keep the work in the coordinator. Any delegated worker must be read-only, return findings only, and receive an explicit ban on every Slack write action.

End the single verdict with exactly one configured marker:

```text
[benny:bug]
[benny:performance]
[benny:other]
```

A bug or performance marker may add `tracker=<URL>`.
