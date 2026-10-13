# Record Templates

Use only the sections needed in existing project records. These templates support the delivery cycle in [the operating model](operating-model.md); they do not require a separate document for every stage, batch, or task. Small work may keep the relevant facts in the current conversation. Brackets indicate fields to fill with actual project facts, not instructions to execute.

Keep confirmed requirements, working assumptions, and improvement suggestions separate. Existing authorization and user-required confirmation points determine what can proceed; a template field does not create a new approval gate. Use [task routing](task-routing.md) to reconcile instructions and decide when confirmation is actually needed.

Use the user's language for reports. Keep canceled or superseded requirements in concise history rather than the active brief. Instruction sources and revisions support internal traceability; user-facing reports should naturally synthesize all active requirements, without instruction-sequence labels or special emphasis on the latest additions unless requested. Include relevant evidence sources, candidate versions, and verification dates.

## A. Coordination Agreement / Main Checkpoint

```text
Revision / updated at:
Project / environment / actual version:
Project outcome / current stage / stage exit condition:
First or next usable result:
Explicit non-goals, compatibility constraints, and protected data:
Existing authorization: scope, source, limits
User-required confirmation points: decision or checkpoint / status / confirmation evidence
Sole integration lead:
Reporting agreement: language, detail, cumulative table scope, notification triggers

Current effective brief:
- Confirmed requirements: stable IDs / active constraints / acceptance conditions / source
- Working assumptions: basis / uncertainty / validation trigger / permitted provisional scope
- Superseded or withdrawn decisions: concise history links

Current delivery path: active authorized outcomes and their order
Current batch: ID / outcome / owner / integrator / end condition / evidence location
Next batch: candidate outcome / dependencies / proposed or already authorized
Decision queue: unresolved choice / options / decision owner / affected work / next action
Parked suggestions: expected benefit / cost or uncertainty / reconsideration trigger / adoption status

Workstream owners, consumers, and evidence locations:
Task table: requirement and batch ID / task / state / owner / dependencies / candidate / evidence validity / gaps / next step
Shared ownership: resource or interface / responsible owner / current writer / consumers / scope / baseline / release or receipt evidence
Operations in progress or with unknown outcomes:
Latest consequential decisions and reasons:
First safe step on resumption:
```

Link to detailed task briefs and evidence rather than copying them into the main record. Omit fields that do not apply. A decision queue can include choices the lead may make within existing authority; it is not automatically a queue for the user. Parked suggestions are not dispatched work. Large projects may link to dedicated registers, but one fact must not acquire two competing authoritative records.

## B. Delivery Batch / Executable Task Brief

Use this for a batch, or for a task linked to an existing batch. Shared batch facts need only a reference in each child task.

```text
Project outcome / stage / related requirement IDs:
Batch ID / task ID when applicable / brief revision:
Result the user or named consumer can accept:
Mandatory acceptance conditions and batch end condition:
Disposition if a required condition fails: responsible owner / bounded correction or investigation / decision needed / independent work that may continue
Outcome owner / assignee / consumers / integration owner:

Actual baseline and candidate inputs:
Contracts relied on: names or locations / versions / input-output meaning / compatibility constraints
Established facts:
Working assumptions and how they will be checked:
Original sources and constraints that must be read:
Permitted read/write scope; protected data and areas that must not be touched:
Dependencies, admission conditions, and shared ownership or locks:

Existing authorization and its limits:
Explicit user-required confirmation points, if any:
Autonomous decisions; conditions requiring a report, scoped decision, or safe stop:
Required verification: acceptance condition / evidence layer / environment / version / limits of real-sample coverage
Existing evidence to reuse and conditions that would invalidate it:
Budget / time window, only if actually set by the user or project:
Subagents permitted, maximum concurrency, and scope, according to actual authorization:
Delivery location / return checkpoint / next reporting milestone:
```

A brief dispatch may combine these fields, but retain the result, ownership, boundaries, dependencies, and required evidence. The assignee proceeds autonomously within existing authority. A new cost, contract change, or material scope risk is assessed through the relevant decision route; it does not justify repeatedly requesting permission already given. A simple stop or park instruction needs only its scope, required action, and acknowledgment.

## C. Workstream Return / Candidate Checkpoint

```text
Batch / task brief revision / related requirements:
Outcome owner / affected consumers / intended integrator:
Candidate location and identity: version, commit, diff, or file hash
Baseline and contract versions the candidate actually used:
Changes this round and acceptance conditions addressed:
Mandatory conditions met / unmet / not yet checked:
Observed behavior and evidence: location / version / environment / date / coverage
Evidence validity now: current / reusable for unchanged scope / invalidated / unknown, with reason
Unverified claims, working assumptions, and contrary evidence:
Changed files / shared diffs / protection of unrelated uncommitted changes:
Compatibility, consumer impacts, and unresolved dependencies:
Operations in progress or unknown outcomes:
Return status: ready for scoped review or integration / correction needed / decision needed / paused
Next action / responsible owner / expected return:
```

The return identifies what was actually built and checked. “Ready for integration” is an assignee's submission state, not a claim that the integrated result or user acceptance has passed. Changes to the candidate or its contracts require reassessing affected evidence; preserve evidence that remains applicable.

## D. Review Conclusion

```text
Reviewer / date and time / candidate version or diff:
Original acceptance conditions / baseline / contracts reviewed:
Coverage, unread material, and unavailable evidence:
Findings: location / trigger / user impact / evidence / smallest recommended correction
Judgment: proceed within this scope / proceed conditionally / resolve blockers first
Unmet mandatory conditions and their disposition:
Additional verification needed:
Existing verification still applicable and why it need not be repeated:
Correction owner / affected consumers / integration follow-up:
```

A conditional judgment must name its limits and the authority for accepting them. It cannot relabel a mandatory blocker as an optional improvement or substitute for a required user decision.

## E. Formal User Report

Generate the report from the authoritative cumulative record. Include every agreed reporting area and mandatory acceptance condition, including unchanged, incomplete, blocked, paused, and previously accepted items. Use the latest applicable evidence; if an earlier result has not been rechecked, state its version or date rather than presenting it as a new verification.

```markdown
Overall judgment: what is usable now, the current stage, and whether the course needs adjustment.

Changes in this batch: actual new results and material changes.

| ID / user outcome and mandatory acceptance conditions | Work done and changes this batch | Status / evidence layer / environment / version / date / source | Remaining gaps or dependencies | Next step / owner |
| --- | --- | --- | --- | --- |
| [One row for each agreed outcome; retain unchanged and unresolved rows] | [Actual work] | [Supported status and applicable evidence] | [Specific gap or none] | [Action and responsible owner] |

Current direction and next batch: the authorized delivery path and what follows.
Coordination decisions: material changes to contracts, ownership, priorities, or plans, with reasons.
User decisions needed, only when real: reviewable result, options, tradeoffs, recommendation, and why existing authority does not settle the decision.
Evidence: a few clickable links to the main supporting artifacts.
```

Fill the table in the actual report; a link to an internal ledger or a promise to provide the table later does not satisfy a request for a complete cumulative report. Routine interim updates can be shorter unless the reporting agreement requires the full table every time. Do not use unsupported percentages, combine test counts from different versions, or treat silence as user acceptance.

## F. Bug Record

```text
Issue / related requirement / delivery batch:
Symptoms, expected behavior, impact:
Version / environment / original or minimal input:
Established facts:
Working hypotheses and how to disprove them:
Missing evidence:
First failing boundary and root-cause evidence:
Minimal fix / non-goals / owner / affected consumers:
Existing authorization and any actual decision needed:
Regression checks and retest of the original scenario:
Candidate / evidence validity / remaining limitations:
Batch disposition if the failure remains:
Unrelated improvement suggestions, if any: link to parked suggestions
```

Keep the observed failure separate from hypotheses and optional improvements. A synthetic sample may support regression checks but does not by itself establish that the user's original case passed.

## G. Pause and Handoff Acknowledgment

```text
Pause scope / source of the user's instruction:
Project outcome / stage / unfinished batch:
Each assignee: acknowledgment time / confirmed stopped, still active, or unknown / saved-work location
Related monitoring: confirmed paused / unconfirmed / absent; retained configuration location
Last known code, artifact, and environment versions:
Uncommitted changes / ownership / protected data / recoverable candidate:
In-flight operations and unknown outcomes, with available request or receipt references:
Last applicable verification and unverified items:
Current delivery path / pending decisions / parked suggestions:
Resumption conditions / first safe action / who is authorized to resume:

For a handoff, add:
Incoming owner:
Verified facts and evidence / unread material and conflicts:
Authority for the transfer, including an authorized recovery handoff when applicable:
Previous owner's safe-stop and release evidence; for recovery takeover, evidence that their writes cannot continue:
Preserved changes and any unresolved authorship or ownership:
Incoming owner's acceptance acknowledgment:
Effective responsibility transfer recorded in the main checkpoint:
```

Follow [recovery and handoff](recovery.md) and [ownership and review](ownership-review.md). The acknowledgment records observed facts; filling it out does not stop a process, resolve an unknown remote operation, or grant write authority.

## H. Optional Coordination Improvement Note

Add a short entry to the existing checkpoint only when observed friction warrants a change. This is not a mandatory retrospective after every task.

```text
Observed coordination problem and evidence:
Working hypothesis about the cause:
One bounded adjustment within existing authority:
Protected product requirements and unaffected work:
Next relevant batch or checkpoint at which to observe the effect:
Observed result, including unknown or unmeasured effects:
Decision: retain / revise / revert the adjustment; reason
```

Keep product changes and coordination changes distinct. An improvement hypothesis does not authorize a product feature, a permanent skill rewrite, new external permissions, or background monitoring. Report token use or elapsed time only when measured; otherwise describe the observed duplication, delay, or rework without inventing savings.
