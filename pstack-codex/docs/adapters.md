# External adapters

The package includes an adapter process boundary, not implementations of external model providers, cloud workers, or webhook hosting. No adapter is configured by default. Features that require one report BLOCKED. Local native subagent work does not require these services.

Configure an adapter in the target repository's `.agents/pstack/config.json`:

```json
{"schema_version":1,"roles":{},"adapters":{"multi_model":{"command":["/absolute/path/to/approved-runner"]}}}
```

The command is an argv array, never shell code. Use an absolute executable path. Credentials belong in the adapter's environment or credential store; never the package, request payload, response, decision log, browser, or chat. Only call an operation within the user's authorised workflow. Do not place secrets in command arguments. Adapter stderr is not echoed by the helper.

```sh
python3 <plugin>/scripts/runtime.py --config <config.json> adapter multi_model run --input <request.json>
```

The input file is the payload object. The helper sends one JSON object to stdin:

```json
{"schema_version":1,"operation":"run","payload":{"role":"interrogate reviewers","model":"actual-provider-model","prompt_path":"/scoped/brief.md","output_directory":"/isolated/output"}}
```

The process returns one JSON object on stdout:

```json
{"schema_version":1,"status":"ok","result":{"provider":"actual-provider","model":"actual-model","family":"actual-family","report_path":"/isolated/output/report.md"}}
```

`status` is `ok`, `blocked`, or `error`. A blocked/error response exits the helper with code 2. A malformed response or failed process also fails. The helper validates the envelope only; the coordinator verifies the operation-specific result below. The driver buffers process stdout and stderr in memory. Return small JSON receipts and store bulk output in the named artifacts. `--timeout` defaults to 60 seconds. Long work should return a durable task ID promptly and expose status/result operations. Do not abandon a remote task merely because a local request timed out; reconcile by its request ID before retrying a mutation.

## Multi-model adapter

Provide `run`, and where asynchronous, `status`, `result`, `cancel`. The adapter must run the exact requested family/model, return actual provider and model identity, preserve scoped files, return full evidence paths, and report unavailable access without changing models. Budget, effort, and speed map to explicit supported provider fields, not suffix rewriting.

Panel role values are lists of seats. For example, configure `interrogate reviewers`, `arena runners`, `architect runners`, and `arena cross-judge pool` with at least two verified distinct families. Each seat has `model`, `family`, `execution` (`native` or `multi_model`), and optional `reasoning_effort` and `speed`. Resolve with `runtime.py role "interrogate reviewers" --distinct-families`. This verifies declared configuration only. Test actual identities, independent outputs, unavailable-model failure, rubric isolation, and different-family judgment before marking parity complete.

## Remote-worker adapter

Provide `start`, `status`, `result`, `cancel`, and `recover`. Start accepts an immutable revision, repository, bounded brief, exclusive environment/worktree, model seat, and request ID. Return a durable task ID, actual base SHA, execution placement, artifact location, and live status source. Result includes branch/head SHA, changed files, commands, evidence, deviations, and terminal state. Preserve full agent/tool transcripts for Eval and audit. Reject an unavailable base or unproven isolation. Recover must resolve the same task after a local restart. Prove cancellation, laptop-independent execution, lost-response reconciliation, and retention before claiming Cursor-cloud equivalence.

## Webhook and event adapter

Provide `create`, `inspect`, `test`, `disable`, and event delivery to the approved Codex executor. Provision a secret in a local credential store or secret manager outside the chat; return only its reference. The UI server retrieves the secret and authenticates its POST. Keep event bodies untrusted. Preserve action fields, immutable event coordinates, acknowledgements, durable failed-delivery storage, and idempotent event IDs. Do not invent a native Codex sender-key card or claim the model can never see a credential when the adapter exposes it.

For Benny, new top-level Slack messages must reach both procedures, with the trusted triage identity and original channel/thread timestamp intact. Desktop schedules cannot supply this event contract. Eligible ChatGPT web event tasks still need a tested bridge to repository execution and real app control. See `../automations/benny/PARITY.md`. No automatic polling fallback.

## Live acceptance

No real provider, worker host, webhook receiver, credential flow, or Slack trigger is provisioned by this conversion. Fixture process tests prove only request transport and failure handling. Record provider/environment, exact revision, request/task ID, result identities, evidence paths, restart outcome, and date when testing a real adapter. Configuration alone never changes a parity status to passed.
