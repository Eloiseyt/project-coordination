# Record Templates

Copy only what is needed into existing project records; do not create every document at once. Brackets indicate fields to fill with project facts, not instructions to execute.

Use the user's language for user-facing reports; these English templates do not require English output. Reconcile cumulative requirements into one current effective brief, keeping affected acceptance conditions, dependencies, and work orders aligned. Canceled or superseded requirements belong in history, not the active brief. Instruction sources and revisions are for internal traceability. Reports should naturally synthesize all active requirements without instruction-sequence labels or special emphasis on the latest additions unless requested. Still include relevant evidence sources, candidate versions, and verification dates to support reported results.

## A. Coordination agreement / main checkpoint

```text
Revision / updated at:
Project / environment / version:
Goal and current smallest usable result:
Explicit non-goals and protected data:
Effective user authorization and source:
Sole integration owner:
Reporting agreement: language, detail, cumulative table scope, notification triggers
Workstream owners and evidence locations:
Current effective brief: cumulative active requirements, stable IDs, original sources, acceptance conditions; canceled or superseded requirements in history
Task table: ID / status / owner / dependencies / evidence level and version / gaps / next step
Shared ownership: path or external resource / writer / scope / baseline / release status
Operations in progress or with unknown outcomes:
Latest decisions and reasons:
First step on resumption:
```

Remove unnecessary fields when there are no parallel tasks. Large projects may link to dedicated registers, but must not duplicate the same facts in two main checkpoints.

## B. Executable work order

```text
Work order / related requirement / revision:
Result the user can accept:
Current baseline, established facts, key uncertainties:
Original sources and constraints that must be read:
Permitted read/write scope; areas that must not be touched:
Interface inputs/outputs, consumers, compatibility requirements:
Required verification and limits of real-sample coverage:
Dependencies and shared locks:
Autonomous decisions; conditions requiring a report or stop:
Budget / time window (only if actually set by the user or project):
Subagents permitted, maximum concurrency, and scope (according to authorization):
Delivery location, checkpoint, next reporting milestone:
```

Dispatch messages may be brief, but must retain the agreed result, boundaries, and evidence. With no new cost, risk, or interface change, the executor proceeds autonomously within the work order.

## C. Workstream checkpoint report

```text
Work order / revision / current version:
Changes this round:
Verified behavior and evidence locations:
Unverified claims or contrary evidence:
Changed files / shared diffs / protection of unrelated uncommitted changes:
Dependencies or risk of exceeding scope:
Next step: continue / await scoped review / need a specific decision / pause safely
Operations in progress or unknown outcomes:
```

## D. Review conclusion

```text
Reviewer, date/time, candidate version/diff:
Coverage and unread material:
Findings: location, trigger, impact, evidence, recommended minimal correction
Judgment: proceed within this scope / proceed conditionally / resolve blockers first
Additional verification needed:
Existing verification that need not be repeated:
```

## E. Formal user report

```text
Overall judgment: what is usable now and whether to adjust course.
Changes this round: only actual new or changed results, not emphasis on the newest instructions.

| ID / issue and mandatory acceptance conditions | Work done and changes this round | Status / environment / version / date/time / evidence source | Remaining issues | Next step / owner |
| ... |

Coordination decisions: changes to interfaces, ownership, priorities, or plans, and why.
User decisions needed: concrete options and trade-offs; do not invent a request when none is needed.
Evidence: a few clickable links to the main evidence.
```

## F. Bug record

```text
Issue / related requirement:
Symptoms, expected behavior, impact:
Version / environment / minimal input:
Facts; hypotheses; missing evidence:
First failing boundary and root-cause evidence:
Minimal fix / non-goals / owner:
Regression checks and retest of the original scenario:
Status, remaining limitations, inclusion in this delivery:
```

## G. Pause and handoff acknowledgment

```text
Pause scope / source of the user's instruction:
Each executor: acknowledgment time, stopped or still in progress, saved-work location
Related monitoring: paused / unconfirmed / absent
Last known code and environment versions:
Uncommitted changes / write ownership / protected data:
Unknown operation outcomes:
Last passed verification and unverified items:
Resumption conditions, first step, and who is authorized to resume:

For a handoff, add: incoming owner, verified facts, unread material/conflicts, acceptance acknowledgment, record of the authority and responsibility transfer
```
