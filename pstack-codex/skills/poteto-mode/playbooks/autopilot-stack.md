### Autopilot-stack

Run the Autopilot-full playbook, but do not merge. Verify each PR at its current head and hand it to the operator. After handoff, nobody pushes or changes its base without the operator's go.

1. **Keep independent PRs independent.** Run owners in parallel from trunk, as in Autopilot-full step 3. Stack a PR only when it depends on another PR. Base the dependent PR on its parent's branch, using the rules in **Size and stacks** in `playbooks/opening-a-pr.md`.
2. **Verify the dependency chain.** A dependent PR is verified against its current base and head. When a lower PR changes before handoff, update and reverify affected children. Use the patch-id rule in `playbooks/shipping.md` only where it proves the child's patch is unchanged.
3. **Stop at handoff.** Do not merge, enable auto-merge, push, or rebase after handing off. Report each PR, its current head, verdict, base, and dependencies. Wait for the operator to land the work.

Autopilot-full is for a queue whose merge authority the user's request grants. Autopilot-stack is for a queue handed to the operator to land. Both keep independent PRs separate and stack only real dependencies.

**Reply:** list each PR with its current head, base, dependency, verdict, and link. State that the queue is handed off and no further writes will occur without the operator's go.
