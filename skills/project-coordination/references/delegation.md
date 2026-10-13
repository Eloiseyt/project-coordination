# Delegation and Cost

## Decide Whether to Split the Work

Before splitting work, write one sentence identifying the independent deliverable, how it will be accepted, and its shared dependencies with the main task. If these are unclear, have one assignee investigate first. Adding agents does not resolve an ill-defined task.

Assess total cost: execution, reading new context, coordination, review, waiting, and rework. Parallel work may reduce elapsed time while increasing token use; report these separately. Do not promise this project performance gains measured elsewhere.

| Approach | Benefits | Costs and limitations | Lead's actions |
| --- | --- | --- | --- |
| One agent working directly | Consistent context; no handoff overhead | Long tasks can lose sight of the whole; self-review has blind spots | Keep small checkpoints; add independent review when risk warrants it |
| Short-lived subagents | Isolated investigation and focused review | Repeated reading; compressed conclusions can lose meaning | Supply the minimum original evidence; require references and limitations in the return |
| Persistent workstream chats | Preserve module knowledge and continuity across checkpoints | Divergent accounts, conflicting shared edits, and recovery overhead | Define workstream boundaries and common interfaces; integrate at checkpoints |
| One writer with several read-only investigators | Protect coupled code while comparing findings in parallel | The writer may become a bottleneck | Keep change batches small; ask investigators for specific recommendations |
| Parallel work in separate worktrees or branches | Separate code writes | Merge, data, service, and dependency conflicts remain possible | Fix a baseline; assign an integrator and plan tests of real module interactions in advance |

## Roles Define Responsibilities, Not Headcount

- **User**: Sets product direction, preferences, and authorizations that require their decision. The user is not responsible for carrying context between agents or merging their work.
- **Lead**: Maintains cumulative requirements, key dependencies, current authorizations, write ownership, major technical tradeoffs, and final acceptance. Handles inexpensive integration directly instead of merely forwarding messages.
- **Workstream owner**: Owns a complete outcome, manages its evidence and subtasks, and checks the work before delivery. Delivers more than a few disconnected files.
- **Subagent**: Completes a bounded task and returns. By default, has no authority over global state, releases, or cross-module decisions.
- **Reviewer**: Examines a candidate read-only and identifies specific defects, impact, and evidence. Does not edit the same content concurrently with its author.

One agent may fill several roles in a small project. Call a review independent only when a separate evaluator has not been steered toward a conclusion. Models can agree and still share the same error; critical paths still need real validation.

## Dispatch and Further Delegation

Use the relevant parts of a template to create a task brief instead of copying the entire history. Specify where to find the original requirements, key decisions, input version, permitted read/write paths, output location, and return checkpoint. Preserve ambiguities and contrary evidence; do not supply only the expected answer.

Separate user chats, background automations, and internal subagents are different resources; follow the current platform's authorization rules. Consent to collaborate does not authorize arbitrary chat creation, external messages, permission changes, or paid services.

Further delegation by a subagent requires all of the following: platform and user permission, allowance in the parent task brief, divisible scope, remaining concurrency and budget capacity, and a parent owner able to review the results. Adding a level usually requires reassessment by the lead. Do not allow unbounded recursive delegation, mutual wakeups, or loops that dispatch work back to the same task.

For cross-module disagreements, the relevant owners first exchange facts about the same version. The lead resolves matters involving the user contract, shared ownership, or priorities. Do not make the user relay the same decision across multiple chats.

## Checkpoints and Monitoring Frequency

- **Routine checkpoints**: New evidence, a runnable slice, a settled interface, or a discovered blocker. Report the change and continue autonomously when work is on track.
- **Major checkpoints**: A complete feature works end to end, a shared contract changes, data migrates, a release goes live, the user accepts a result, or the lead hands over. The lead must inspect the actual deliverable and its impact.
- Do not repeatedly request updates, restart, or launch a duplicate task for a long command that is still running without new evidence.
- Read compact status and the evidence index first. Expand full logs only for a new checkpoint, an exception, or a risk at a module boundary. Check less often when nothing changes.
- Monitoring tools schedule work. A timer firing proves neither task completion nor that a lock can safely be taken over.

## Practical Ways to Reduce Cost

1. Keep each requirement's full definition only in the main record. Task briefs reference it and state the current differences.
2. Give new assignees the minimum sufficient context instead of inheriting every chat by default. Point to the original when the original is needed.
3. Workstream owners return conclusions, evidence locations, and uncertainties, not thousands of lines of terminal output.
4. Keep the version associated with each piece of evidence. Reuse validation for unchanged paths when conditions are unchanged; when key conditions change, rerun only the affected layers.
5. Independent reads may run in parallel. Perform edits, approvals, and dependent operations in sequence.
6. Limit work in progress to integration capacity. When reviews pile up, integrate first or reduce dispatches instead of generating more output.
7. If coordination consistently costs more than direct work, return the coupled parts to one owner.
8. Provide a complete cumulative table when the user requests one. Update it from the main record instead of reinvestigating every settled item, and identify what has not been rechecked.

Optional measures include causes of rework, duplicate tool calls, waiting time, review backlog, missed acceptance criteria, and actual token use when tools expose it. Report unmeasured values as unknown; do not invent savings percentages. Simple projects do not need a new monitoring system.
