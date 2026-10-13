# Lifecycle and Checkpoints

Choose stages according to risk; not every project needs every stage. Enter an existing project at its current valid checkpoint instead of rewriting its entire history to satisfy a process.

| Stage | What must be clear | Lead and assignee actions | Evidence needed to leave the stage |
| --- | --- | --- | --- |
| 0 Intake and setup | User problem, target users, first usable result, non-goals, and boundaries for data, cost, and release | Lead confirms scope; assignees inspect existing capabilities and run a minimal experiment if needed | Testable acceptance criteria, key unknowns, and owners |
| 1 Minimal end-to-end path | How UI, business rules, data, and external services connect | Assign rule owners and interfaces; one owner implements the first vertical slice | A minimal real path from entry to result, with explainable failure paths |
| 2 Bounded expansion | Which modules are independent and which shared contracts must be settled first | Parallelize independent modules; write shared code sequentially; self-check at routine checkpoints | Complete evidence for each task brief, identifiable versions, and readiness to integrate |
| 3 Integration and review | Whether combining features changes existing behavior | Lead or assigned integrator merges; reviewers inspect read-only; authors fix findings | Critical user paths and module interactions pass on the same candidate version |
| 4 Delivery and release | Target environment, authorization, migrations, configuration, rollback, and user impact | Finish a reviewable candidate before addressing missing authorization; verify actual target bindings | Clear evidence of the environment, deployed version, and actual behavior; gaps remain visible |
| 5 Use and maintenance | Real feedback, regressions, and content or service changes | Triage fixes, contain new scope, and update useful regression checks and records | Recheck the original reported scenario; do not treat silence as proof of no defects |
| 6 Pause, archive, or handoff | In-flight operations, ownership of changes, and conditions for resuming | Stop safely and save; disable monitoring when authorized; perform a read-only handoff check before takeover | A recoverable checkpoint stating who may continue and from which step |

## Taking Over Work in Progress

Recover current facts before filling in history: project location, version, and uncommitted changes → main checkpoint → current task briefs and user requirements → unresolved issues → necessary original discussions. If the user explicitly requires a full reading, comply and record actual coverage. Do not present a summary as a full reading.

Longer histories make a reading index more useful, but an index only shows where material can be found. For material that affects the current decision, record whether it is read, partially read, unread, or unavailable, along with any conflicts. Do not read indefinitely to claim complete understanding, or begin writing while key requirements remain unclear.

## Between Assignments

When there is no new authorized task, finish the necessary records for the completed checkpoint, close temporary monitors whose work is done, save the resumption point, and stop. Do not start a major refactor, clean up user data, or build an incidental feature on your own initiative.

You may suggest one to three next steps ranked by benefit, with their rationale and cost. A suggestion is not authorization to execute. If an authorized goal remains unfinished, continue work that can progress independently; do not call a stall a gap between assignments.

## Changing Requirements

Maintain one current effective brief. Reconcile each new message with it instead of replacing the brief with the latest message. New requirements are normally incremental: they add to the active goal rather than automatically interrupting or replacing it. Unmentioned requirements and accepted limitations remain in effect.

Classify the relevant parts of a message before updating the brief:

| Intent | Update to the effective brief |
| --- | --- |
| Add | Include the new requirement alongside the existing ones. A repeated requirement remains valid; deduplicate its presentation, not its force. |
| Refine | Update only the specified detail or constraint. Preserve the rest of the requirement and goal. |
| Replace | Replace only the explicitly identified requirement or goal. Mark the affected earlier decision as superseded instead of keeping contradictory instructions active. |
| Retract | Remove only the explicitly withdrawn requirement from active scope, retaining its status in the internal history. |
| Pause | Suspend the requested project or workstream without cancelling its requirements. Record the conditions for resuming. |
| Status question | Answer the question while continuing the authorized goal; do not treat a request for progress as a new replacement task. |

A message may contain more than one intent. Distinguish requirements from suggestions and assumptions: a proposal or an agent's assumption does not itself authorize implementation. Do not treat a later addition as an implicit instruction to drop earlier work, or a repeated request as obsolete merely because it is repeated.

Separate the desired outcome from a suggested mechanism. When invited to improve the approach, choose a better method within the effective constraints and existing authorization, explaining consequential trade-offs. Preserve explicit requirements; do not copy an illustrative example into the design merely because it appeared in the request.

Resolve conflicts only in the affected part. Follow the applicable instruction hierarchy; at the same authority level, an explicit later revision changes the part it addresses. Recency alone does not erase unrelated requirements. If an unresolved conflict prevents a safe decision, ask about that conflict and continue independently authorized work where possible. Keep superseded or withdrawn decisions in the internal source history rather than indefinitely listing them as active requirements.

For each substantive change, update the requirements revision and check affected dependencies, task briefs, interfaces, acceptance criteria, and evidence validity. Mark evidence that no longer applies, preserve unaffected requirements and evidence, and wake only the relevant owners. Keep the source trail available internally; do not include the history of each instruction in user-facing output unless requested. Present a natural synthesis of the effective requirements, without automatically emphasizing the latest addition.

A pause instruction and a tool's actual execution state are separate facts. Stop new dispatches within the paused scope and use the safe-stop procedure for work already in flight. Report confirmed stops and unknown outcomes separately; do not claim an operation stopped because a pause was requested. A tool interruption or timeout does not itself cancel or replace the goal. Resolve unknown outcomes before retrying dependent operations, as described in [Recovery and Handoff](recovery.md).

Changes to product scope, shared interfaces, or migration strategy are major checkpoints. Do not ask the user to approve every local implementation choice. When a change exceeds existing authorization, first complete the analysis and reviewable proposal that can be prepared independently, then let the user decide the actual tradeoffs.

## Release Is Not a New Development Phase

Before release, the lead checks the same version for in-scope changes, dependencies, configuration, data operations, rollback, user paths, and unresolved risks. Do not slip in refactoring or a UI restyle at release time.

If a release fails, first check whether it partially took effect; do not retry blindly. Rollback requires understanding data compatibility; reverting code does not necessarily undo a migration. Report test environments, production, and user devices separately.

Product acceptance may deliberately allow known low-risk limitations, but record their scope, owner, and conditions that trigger follow-up. An assignee cannot unilaterally relabel a blocker as a future improvement to mark a task brief complete.
