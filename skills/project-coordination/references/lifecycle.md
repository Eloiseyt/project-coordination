# Lifecycle and Entry Points

The lifecycle describes where a project enters the delivery cycle in [the operating model](operating-model.md). It is not a second process to run alongside it. Choose stages according to actual risk and uncertainty; not every project needs every stage.

Keep the hierarchy visible: **project outcome → current stage → acceptable delivery batch → executable tasks**. The project outcome gives the lasting direction. A stage focuses the next uncertainty or delivery boundary. A batch produces a bounded result with an explicit end condition. Tasks contribute to that result; finishing every task does not prove the batch is accepted. For a small correction, these levels may collapse into one action and one check, without new records or roles.

## Enter at the Actual Project Position

| Entry point | First action in the delivery cycle | Next meaningful checkpoint |
| --- | --- | --- |
| New project | Establish the user problem, target users, first usable result, non-goals, and data, cost, and release boundaries; inspect existing capabilities | A minimal real path from entry to result, with its critical assumption checked and failure paths understood |
| Inherited project | Reconcile actual versions, ownership, effective requirements, open work, and available evidence before selecting the next unfinished batch | A trustworthy continuation baseline and the next unresolved integration or acceptance boundary |
| New long instructions during ongoing work | Reconcile the message through [task routing](task-routing.md), then update only affected batches, dependencies, and acceptance evidence | A coherent current brief and a clear next action without losing unaffected work |
| Short, isolated task | Keep the result and boundaries in the current conversation; implement and check directly when appropriate | The requested result and proportionate evidence; no extra project structure |
| Bounded expansion | Use the first working path to settle shared contracts, then divide independently verifiable outcomes | Compatible candidates ready for integration on identifiable versions |
| Release | Identify the candidate, actual target environment, authority, configuration, data operations, and recovery plan | A verified authorized release, followed by whatever acceptance the user requires |
| Maintenance | Triage real feedback and regressions against the current product contract and compatibility requirements | The original reported scenario and affected interactions rechecked, or a clearly scoped next release |
| Waiting on a dependency | Record the blocking fact and the event or evidence needed; continue independent authorized work or integrate ready returns | New evidence that changes the decision, rather than another unchanged status check |
| No active authorized work | Finish necessary records, preserve a resumption point, and close completed temporary monitoring when authorized | A new authorized outcome; otherwise stop |
| Pause or handoff | Stop new affected dispatches, preserve work, distinguish confirmed stops from unknown outcomes, and follow [recovery and handoff](recovery.md) | A recoverable checkpoint, an authorized current owner, and the next safe action |

## Choose and Close a Delivery Batch

Start a batch from the current effective brief and an actual baseline. State the user-visible result or decision it will produce, its mandatory acceptance conditions, the relevant contracts and consumers, the owner of each outcome, and who will integrate it. Resolve dependencies that prevent safe execution before dispatch; a finite investigation may be the right batch when the contract is still unclear.

For a first implementation, use a small end-to-end path through the relevant UI, rules, data, and services. Assign shared rule owners before multiplying implementations. As contracts settle, independent work may proceed in parallel while shared writes remain sequential. The lead can integrate a narrow return directly after acquiring write ownership, or assign one integration writer when the work warrants it.

Declare the batch's end condition before execution and inspect the actual return against it:

- **Accepted within scope:** the required behavior or decision has evidence on the identified candidate. Update the stage and select the next authorized batch.
- **Incomplete:** a mandatory condition or required evidence is missing. Preserve the candidate, identify the responsible boundary, and return a bounded correction or investigation. Do not move the gap into an optional suggestion to close the batch.
- **Closed incomplete for replanning:** where existing authority permits regrouping work, end the current batch as incomplete and link a scoped follow-up with an owner. Keep the parent requirement unmet and all dependent delivery gates in place. This records a change in the work plan, not successful delivery or permission to relax acceptance.
- **Blocked or awaiting a real decision:** identify the specific dependency or authority needed and which independent work may continue. Prepare a reviewable choice before requesting a consequential decision.
- **Paused or superseded:** preserve work and evidence, record the affected scope, and follow the applicable routing or recovery procedure. Do not silently restart an old batch.

A stage closes when its agreed outcomes have the required evidence and any accepted limitations are explicit. Record the scope, owner, and follow-up trigger for a known low-risk limitation; an assignee cannot accept it unilaterally on the user's behalf. A build, deployment, finished agent turn, or set of passing module checks does not substitute for the stage's acceptance conditions.

Use the relevant sections of [the templates](templates.md) in existing records. A batch does not automatically require a new document, reviewer, conversation, or confirmation gate.

## Taking Over Work in Progress

Recover current facts before filling in history: project location, version, and uncommitted changes → main checkpoint → current tasks and user requirements → unresolved issues → necessary original discussions. Preserve protected data and others' changes. Do not select the most optimistic summary as authoritative when records conflict; resolve the affected facts and freeze only contested writes or dependent actions.

If the user explicitly requires a full reading, comply and record actual coverage. A reading index shows where material is located, not that it has been read. For material affecting the current decision, record whether it is read, partially read, unread, or unavailable, along with conflicts. Do not present a summary as a full reading, read indefinitely to claim complete understanding, or begin writing while key requirements remain unclear.

Continue from the verified checkpoint. Do not rewrite project history, repeat accepted work, or reorganize the repository merely to fit this lifecycle. Reconcile in-flight operations and unknown outcomes through [recovery](recovery.md) before retrying or taking over affected resources.

## New Instructions During a Stage

Use [task routing](task-routing.md) for instruction classification, requirements reconciliation, authorization, and explicit confirmation points. The same route applies to a short correction and a long new specification; message length does not itself reset the project.

The lifecycle consequence is local: reassess affected batch boundaries, consumers, interfaces, acceptance conditions, and evidence validity. Preserve unaffected requirements, candidates, and evidence. A product-scope, shared-interface, or migration-strategy change is a major checkpoint; a routine implementation choice within authority is not a new user approval gate. Finish independently possible analysis and a reviewable proposal before seeking authorization for a change outside the existing scope.

Keep requirements, working assumptions, and improvement suggestions distinct in the current record. A parked idea is not the next batch until adopted within the applicable authority. New instructions, an actual tool interruption, and a confirmed safe pause are different events; use [recovery](recovery.md) for execution-state checks.

## Waiting and Idle Periods

Waiting is still part of an active goal. A pending dependency may leave room for authorized independent work, review, or integration. Keep the next useful event or check explicit. Do not repeatedly restart, poll, or duplicate the same work when there is no new evidence, and do not label an unfinished authorized goal as idle.

When no authorized action remains available, save a compact checkpoint and a recovery entry point. Use an existing authorized monitor when appropriate; without one, do not promise background follow-up. If the goal is complete and no new task is authorized, finish necessary records, close completed temporary monitors when authorized, and stop.

You may offer one to three next steps ranked by benefit, with their rationale and cost. Keep them in the suggestion queue until adopted. Do not start a major refactor, clean up user data, or develop an incidental feature to keep contributors busy.

## Release and Maintenance Boundaries

Before release, the lead checks the same candidate for in-scope changes, dependencies, configuration, data operations, rollback, user paths, and unresolved risks. Finish a reviewable candidate before addressing missing authorization, and verify its actual target binding. Do not add unrelated refactoring or a UI restyle to the release batch.

If a release fails, first establish whether it partially took effect. Do not retry blindly or assume that reverting code undoes a data migration. Recovery requires an understanding of data compatibility. Report test environments, production, and user devices separately, including the candidate version, observed behavior, and remaining gaps.

Maintenance re-enters the same cycle through a reported problem or an authorized improvement. Preserve existing data and compatibility, retest the original failure, and update useful regression evidence and records. No new feedback is not proof of reliability. Closing a release does not automatically authorize a new development phase.

## Pause, Resume, and Handoff

Preserve the project outcome, current stage, unfinished batch, ownership, evidence, and unknown operations when pausing. A pause request does not prove that an executor or remote operation has stopped. Pause related monitoring according to actual authority and record whether it was confirmed, while retaining the configuration needed for recovery.

Before resuming or accepting a handoff, reconcile actual versions, uncommitted changes, write ownership, available evidence, in-flight operations, and authorization. Follow [recovery and handoff](recovery.md) for safe stopping, conditional resumption, and transfer of responsibility. Resume the first safe action in the existing delivery cycle; do not blindly replay old commands or invent a new project plan merely because the conversation changed.
