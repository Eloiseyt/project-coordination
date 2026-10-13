# The project operating model

This is a guide to running a whole project with Codex, from the first conversation through delivery and maintenance. It explains how to keep the work connected when one conversation becomes several, and how to keep the arrangement small when one agent is enough.

Start here when setting up a project, improving an ineffective collaboration, or taking over as lead. The six parts cover: the organization; project setup and planning; continuous delivery; requests and changes; state, reporting, and cost; improvement and continuity. Detailed procedures are linked where they become relevant.

## 1. Give the whole outcome an owner

In this guide, an **agent** is the assistant doing work. A **conversation** or **chat** is where that work and its context are discussed. A **workstream** is a continuing area of responsibility, such as importing documents. A **subagent** takes a finite assignment from another agent and returns a result. These terms describe how work is organized; they do not imply that one agent is inherently more capable than another.

The **integration lead**, shortened to **lead**, is responsible for turning the user's overall intent into a result whose parts work together. The current conversation can serve as the lead. There is no special model to unlock and no requirement to create a manager before doing useful work. On a small task, the same agent plans, implements, checks, and reports.

### Why a lead becomes useful

The unit of success is a result the user can use and accept. It is not an agent finishing its turn, a collection of completed subtasks, or a large amount of generated code.

A single agent has an advantage: one context contains the reasons behind its decisions. As a project grows, that same context must hold product intent, investigations, implementation details, changing requirements, failures, and release facts. Repeatedly loading all of this becomes expensive, while compressed summaries can omit the constraints that matter.

Splitting work creates a different problem. Each contributor sees a limited part of the project. They may implement different interpretations of the same rule, optimize incompatible interfaces, or call a locally passing component complete before the user journey works. More parallel work can make this problem larger.

The lead resolves this trade-off by preserving the **global decision context**, while workstream owners preserve **domain context** and bounded subagents process **temporary task context**. Artifacts, contracts, and evidence reconnect these views. This can reduce repeated reading and rework; whether it actually does so must be observed in the project.

The architecture therefore has four functions:

1. **Direction:** keep the complete outcome and constraints coherent.
2. **Execution:** produce domain work under explicit ownership.
3. **Integration:** make the parts function together and resolve disagreements.
4. **Learning:** improve both the product and the way work is organized.

These are functions, not four required agents. A small project may combine all of them in one conversation. A large project may distribute execution and review while retaining one accountable integration lead.

### Responsibilities and decision rights

| Role | Owns | May decide within its brief | Must return or escalate |
| --- | --- | --- | --- |
| User | Desired outcome, priorities, explicit constraints, consequential choices requiring their authority | Product direction and authorization | Feedback, acceptance, or a decision when a real trade-off cannot be settled within existing authority |
| Integration lead | Effective requirements, project plan, dependencies, shared ownership, integration, delivery judgment, and user report | Task boundaries, order, suitable delegation, bounded technical trade-offs, review depth, and routine continuation | Decisions exceeding authority; unresolved product conflicts; material failure or changed delivery conditions |
| Workstream owner | A coherent outcome across several checkpoints and its detailed context | Local implementation, investigation, tests, and permitted subdelegation | Changes to shared contracts, protected resources, cost/privacy scope, or acceptance; reviewable delivery with limitations |
| Bounded subagent | One finite question or artifact | Methods inside a narrow assignment | Evidence, artifact, findings, unknowns, and any scope conflict; it does not establish a competing roadmap |
| Reviewer | A findings-based assessment of an identifiable candidate | Which evidence to inspect within review scope | Concrete findings, coverage, remaining uncertainty; the author or integration owner performs fixes |

The lead does not need to know every line of implementation. They do need enough knowledge to explain what each workstream contributes, which assumptions connect them, why the evidence is sufficient, and what remains uncertain. Delegating work does not delegate that accountability to the user.

The lead may implement a small cross-module adapter, finish a narrow correction, or perform a release check directly when that avoids a costly handoff. They first acquire ownership and reserve enough attention to integrate other active work. “Lead” is not a prohibition on implementation, and “doing useful work” is not a reason to abandon supervision.

### Communication routes

- The user normally speaks to the lead. The lead incorporates instructions and routes only affected changes.
- Owners return checkpoint summaries and evidence to the parent responsible for integration. A parent consolidates child output before reporting upward.
- Owners may exchange interface facts directly when the platform and user authorize it. Agreements affecting the project contract return to the lead's main record.
- If the user speaks directly to an owner, preserve that instruction and reconcile its project impact with the lead before conflicting shared work. Do not reject genuine user direction merely because it bypassed the preferred route.
- Findings and risks travel upward immediately when they change scope, safety, interfaces, or acceptance. Routine implementation detail stays local until its checkpoint.

This avoids both extremes: the lead forwarding every small message, and modules making incompatible global decisions without anyone noticing.

### Choose the smallest useful organization

First decide whether to split at all.

Write down the intended return artifact and how it can be checked. Then ask:

1. Can the assignee proceed without repeatedly asking for the lead's unstated context?
2. Can its writes be separated, or can it investigate without writing?
3. Will the context be useful only for this assignment or repeatedly across milestones?
4. Does parallel execution or independent challenge justify dispatch, review, and integration cost?
5. Is someone available to inspect and integrate the return?

An unclear answer calls for a bounded investigation or direct work first. A large task is not automatically parallelizable. A small high-risk decision may justify an independent reviewer.

Then select the execution form.

| Form | Choose it when | What to provide | When to close or change it |
| --- | --- | --- | --- |
| Lead works directly | The change is small, tightly coupled, or already understood; transferring context costs more | Current brief and relevant evidence already in context | Deliver it, or split only if a genuinely independent outcome emerges |
| Short-lived subagent | There is a finite deliverable with a clear completion test: inspect an interface, reproduce a bug, compare sources, implement an isolated function, review a candidate | Minimum sufficient original evidence, exact task, boundaries, output and return condition | Close after the return; reopen only for a specific correction or follow-up |
| Persistent workstream chat | The same domain will need repeated investigation and decisions over several project checkpoints; retaining its context avoids recurring reconstruction | Domain outcome, common contracts, milestone path, permitted writes, escalation conditions, evidence and status locations | Close when the domain outcome is integrated or the remaining work is small enough to absorb; a dormant chat is not a reason to invent more work |
| One writer with parallel investigators | Work is coupled but diagnosis or review can be divided | One writer's baseline; independent read-only questions and clear return artifacts | End the investigations, integrate their findings, then reconsider whether writes can separate |
| Persistent owner with bounded subagents | An established workstream contains independent short tasks, and the owner can review them within actual permissions | Parent brief plus narrower child scopes; no duplicate responsibility for the same artifact | Parent integrates child output; remove the extra level when it stops saving work |

A persistent chat is a continuity mechanism, not a status symbol or mandatory promotion for a long task. A subagent is a bounded execution mechanism, not an inherently less capable worker. Their difference is the lifetime and accountability of their context.

Use the existing suitable chat before proposing another. Creating a new standalone chat requires the platform's and user's applicable authorization; a recommendation to create one is not a dispatch. If tools do not support it, use the same workstream record within the current task.

Split by outcome and dependency.

Prefer workstreams that can return something meaningful to a user or consumer: a file-import path, a search capability, a billing boundary. Splitting solely into “all frontend” and “all backend” often leaves no owner for the connection; it can still work when one integrator owns a settled interface and the complete path.

Before concurrent implementation, identify shared types, persistence identities, errors, cancellation, UI behavior, and external resources. Pick one owner for each shared rule. If the first slice cannot run end to end, investigate the missing contract before multiplying implementations.

Keep the number of active tasks within the lead's capacity to review and integrate. An idle CPU is less costly than several finished branches waiting on an unresolved interface. Reassess organization when dependencies change; do not defend an earlier split just because work has started.

## 2. Establish the project and plan the next useful result

### Start from the project's actual position

For a new project, establish the problem, intended users, constraints, and first useful result. Choose a suitable workspace and identify the consequential unknowns before committing to a large design. For an existing project, recover effective requirements and verify the actual implementation, owners, and evidence; preserve accepted decisions unless new facts justify revisiting them. The same operating model applies to maintenance, interrupted work, and mid-project expansion. [Lifecycle](lifecycle.md) gives the entry and exit conditions for each situation.

Establish enough shared context to answer six questions: What result matters? What must remain true? What exists now? What is uncertain? Who can change what? What evidence will let us move forward? Do not demand complete knowledge of every file before taking a bounded next step. Record unread or unverified areas that could affect that step.

Agree on the reporting format and any user confirmation gates at the outset. A user may want to approve the requirements and architecture before implementation. Another may authorize the whole bounded task immediately. Neither preference should turn into a new permission ritual on every tool call.

### Plan at three horizons

| Horizon | What it contains | How much detail it needs |
| --- | --- | --- |
| Project | User outcome, enduring constraints, acceptance, major risks, and the broad sequence of stages | Stable direction; no speculative inventory of every future task |
| Current stage and next delivery batch | The next usable result, dependencies, owners, key contracts, review point, and exit conditions | Enough detail to coordinate and integrate real work |
| Executable task | Exact outcome, baseline, permitted changes, evidence, stop conditions, and return location | Enough detail for an assignee to act without guessing the missing context |

A stage groups related progress toward the project outcome. A **delivery batch** is the next bounded set of changes that can be reviewed together. A task contributes to that batch. A short project may need one batch and one task; the hierarchy is a way to connect decisions, not a requirement to create three documents.

Work backward from the next useful result. Identify the most consequential unknown and the minimum path that tests it. Prefer an early end-to-end slice over several disconnected components. Separate research that can change the plan from implementation whose interface is already stable.

### Keep a queue, not an expanding list of active promises

Maintain four views of existing work: the current delivery path, the next batch, items awaiting a decision or dependency, and unselected ideas. Choose the delivery path from user priorities and commitments, risk reduction, dependency order, and effort. An interesting improvement should not displace an agreed delivery without a reason.

Do not dispatch more work than the lead and integrator can inspect and combine. A blocked batch may need a smaller slice or a resolved interface, not another contributor. Assign an owner to each unresolved dependency and define what will unblock it. [Controller practice](controller-practice.md) describes these decisions in detail.

Before execution, define the batch's exit: what artifact will exist, which conditions must pass, which evidence is required, and who will integrate it. Also define the failure route: bounded correction, a separately scoped follow-up, a changed plan requiring a decision, or a recoverable pause. Moving an unmet requirement to a later batch does not make it satisfied.

## 3. Run one continuous delivery cycle

Enter this cycle at the last verified checkpoint. Do not repeat completed planning or approval just because a new message arrives. A major project stage may contain several iterations of the same cycle.

### Step 1 — Convert intent into a current brief

**Input:** original request, all effective amendments, existing project decisions, and current authorization.

**Lead action:** define the user-visible result, mandatory acceptance conditions, exclusions, protected data, open choices, and reporting agreement. Separate requirements from assumptions and suggestions. Enrich the framing with missing dependencies or a better method, and honor any requested confirmation of this understanding before moving on.

**Output:** one current brief that can answer “what must be true for this to count as delivered?” Small work can keep this in the conversation; ongoing work uses the existing project record.

**Failure route:** clarify only consequential ambiguity, while continuing independent authorized work. Do not confuse a clear goal with a fully specified implementation.

### Step 2 — Establish the actual baseline

**Input:** project location, current records, active contributors, version and environment evidence.

**Lead and owner action:** verify repository or artifact version, uncommitted changes, ownership, in-flight and unknown operations, existing behavior, and actual available tools. Classify evidence as current, historical, partial, or unavailable.

**Output:** a known starting point and protected boundaries. Do not present a planning document as deployed behavior.

**Failure route:** freeze only contested writes or dependent operations, preserve their state, and resolve discrepancies. Never restart an unknown migration or deployment to find out whether it worked.

### Step 3 — Design the first usable slice and its organization

**Input:** effective brief, baseline, major unknowns, dependencies.

**Lead action:** choose a small end-to-end result that tests the most consequential assumption. Settle essential interfaces, then select direct work, bounded subagents, or persistent owners. Challenge the plan for unnecessary complexity, missing requirements, and failure paths. Honor any requested architecture gate; define routine checkpoints and the next major review.

**Output:** a dependency-aware plan with owners, a concrete next slice, acceptance evidence, and conditions that require intervention. A plan should make the next action clear without predicting every later implementation detail.

**Failure route:** if the result is still difficult to define, run a finite feasibility investigation. Do not turn uncertainty into a large speculative implementation.

### Step 4 — Dispatch a contract, then allow execution

**Input:** a bounded task brief with outcome, baseline, original evidence, write scope, contracts, checks, dependencies, autonomy, and return location.

**Owner action:** verify the baseline, acknowledge ownership, surface incompatible assumptions early, and execute. Subdelegate only when authorized and useful. Self-check the complete assigned outcome before returning it.

**Lead action:** monitor the critical dependencies and new evidence; continue useful integration work. Do not continually ask “are you done?” or make every routine step await a new instruction.

**Output:** an identifiable artifact or diff, its baseline and contract versions, observed behavior, verification evidence, remaining gaps, changed ownership, and the proposed next step. Receipt of this return starts review; it does not itself establish integration or delivery.

**Failure route:** return the narrow blocking fact and what can still continue. Scope expansion is a decision, not an automatic part of fixing the current problem.

### Step 5 — Review the return and integrate

**Input:** original acceptance conditions, candidate version, actual artifact, evidence, and limitations.

**Lead action:** distinguish owner claims from inspected facts. Review the risky decisions and interfaces; use an independent reviewer when warranted. Do small integrations directly or assign a single integration writer. Verify a real path through the combined components and relevant failures at the same candidate.

**Owner action:** address concrete findings and rerun affected checks. Keep unaffected evidence instead of recreating all results for appearance.

**Output:** a candidate cleared for the next step, usable only within stated limits, or still incomplete, with specific reasons. Keep returned work, integrated work, authorized release, and user acceptance distinct. Module tests are necessary evidence where applicable; they do not replace integration evidence. Check which prior evidence remains applicable after a change; rerun affected checks without discarding valid unrelated results.

**Failure route:** identify whether the failure comes from implementation, an ambiguous task brief, an incorrect shared contract, or an unrealistic acceptance assumption. Correct the responsible layer, including the lead's planning when appropriate.

### Step 6 — Report the project and choose the next move

**Input:** integrated evidence, all current requirements, unresolved issues, and the reporting agreement.

**Lead action:** regenerate the cumulative status from authoritative records. Explain what the user can use, what changed, what is still incomplete, and who owns the next action. Follow the user's preferred language and detail. A full-report request cannot be satisfied by a single latest success.

**Decision:** continue the plan; correct one workstream; reduce concurrency and integrate; seek a consequential user decision; pause; or deliver. The lead makes routine continuation decisions within authorization.

**Output:** one shared project conclusion and updated assignments. The user should not have to reconcile contradictory reports from different chats.

### Step 7 — Improve the system and close the stage

**Input:** the actual effort, waiting, findings, repeated work, and missed conditions from the stage.

**Lead action:** run the bounded self-review in [controller practice](controller-practice.md). Change the cause of coordination failure, then check the effect in the next relevant slice. Keep product fixes separate from process changes.

**Delivery action:** verify the required environment and release authority, record limitations and recovery, transfer maintenance responsibility, and retire finished monitoring and temporary tasks. Preserve unresolved requirements with owners; do not silently convert them into optional future improvements.

**Output:** a delivered stage, a smaller next batch, or an explicit pause with a recoverable entry point. Ending an agent turn is not this stage boundary.

### Worked example: one project through the architecture

Consider an existing offline reading application adding an optional online explanation service. A separate import defect also needs repair. This is an illustrative case, not a prescription to use these features or services.

1. **The lead establishes the outcome:** a reader can import a document, select text, request an explanation with consent, and return to the same location. Existing books and history must remain usable. The user receives a complete project table.
2. **The lead verifies the baseline:** identifies the active checkout, current selection contract, data identities, existing UI patterns, and both owners' uncommitted work. Unverified cloud configuration remains an explicit gap.
3. **The lead chooses two persistent domains only if they warrant continuity:** import fidelity and online explanation. The first implementation slice settles a shared selection snapshot and error contract. Shared reader assembly stays with one integration writer.
4. **The import owner uses a bounded investigation:** a subagent examines problematic character mappings and returns evidence. It does not redesign the reader or open its own roadmap. The import owner evaluates the result before proposing a fix.
5. **The explanation owner implements the consent/request/result path:** an isolated reviewer examines retry and accounting semantics. Local mocks verify only local behavior; actual service binding remains a separate gate.
6. **A routine checkpoint shows a mismatch:** import can display a damaged region but cannot provide trustworthy text. The lead coordinates one missing-text contract so the explanation path cannot silently send an incomplete selection. This is a shared product issue, not two unrelated owner bugs.
7. **At the major checkpoint, the lead reviews the integrated journey:** import, selection, consent, result, cancellation, history preference, and return location. If one mandatory condition is missing, the combined feature stays incomplete despite passing module tests.
8. **The lead reports the whole state:** visual fidelity, extracted text, UI, real-service evidence, old-data compatibility, and release status remain distinct. Unchanged gaps remain visible.
9. **The lead improves the next batch:** if both owners repeatedly waited on selection types, settle that contract before further parallel work. If one owner's remaining work is a small adapter, the lead may finish it after acquiring ownership instead of keeping an idle workstream alive.
10. **The stage closes at actual delivery:** only the verified, authorized environment is called released. Temporary reviewers finish. Maintenance retains the relevant failures and evidence, not all raw conversation history in every new context.

The same model becomes much smaller for a label correction: the current agent changes it, checks the relevant display, reports it, and stops. No domain owner, subagent, or new management file is needed.

## 4. Handle instructions and changes without restarting the project

The delivery cycle is the project's backbone. New messages fit into it: some change the goal, some refine the next batch, some ask a question, and some authorize a previously discussed step. First determine their effect on the current work. Then use [task routing](task-routing.md) for planning, bug reports, implementation, review, and control instructions.

Keep one effective brief. Retain requirements omitted from later messages; replace only the affected parts of an explicit revision; remove withdrawn choices from active scope while preserving their history. Do not organize the user's report around the sequence in which messages arrived.

For planning, organize and improve the user's ideas before committing to a design. Follow requested understanding and architecture confirmations, then challenge the agreed approach before writing or implementing. For diagnosis, locate the responsible layer before proposing a correction. Existing authorization can cover these steps together; a clear request to execute should not lead to another round of routine permission questions.

Assess changes at task, batch, and project level. Update affected contracts, assignees, acceptance conditions, and evidence. Continue independent authorized work. A new requirement does not automatically invalidate the entire project, and a passing old test does not automatically validate the new requirement.

## 5. Keep state, reporting, and cost under control

### One source of truth for each fact

Use existing project records. The following are logical views, not mandatory files:

| View | Authoritative content | Normal owner |
| --- | --- | --- |
| Effective brief | Outcome, requirements, constraints, acceptance, authorization, assumptions, and open choices | Lead |
| Plan and integrated status | Delivery path, stages, batches, dependencies, cumulative issue status, and next actions | Lead |
| Ownership and contracts | Permitted writes, shared resource ownership, interface decisions, providers, consumers, and integration responsibility | Lead with the relevant owners |
| Workstream checkpoint | Local progress, candidate version, in-flight operations, gaps, and return evidence | Workstream owner |
| Evidence | Original artifacts, test scope, version and environment, findings, limitations, and review decisions | Producer; lead verifies the conclusions used in reporting |

Avoid copying detailed facts into several independently maintained summaries. Link from the main record to the evidence and original instructions when a decision needs support. Mark whether a conclusion is current, historical, self-reported, inspected, or still uncertain. A tidy workspace has known ownership and recoverable work; it need not have an empty list of uncommitted files.

### Give the user one coherent account

Lead with the overall judgment: what is usable, what is incomplete, and whether the current plan still makes sense. Then show the agreed cumulative view: issue, progress this round, evidence and its limits, remaining gap, next action, and owner. Do not let a completed subtask hide an unfinished parent requirement.

Routine checkpoints, major milestones, failures, decisions, pauses, and final delivery call for different levels of detail. Respect the user's explicit preference for a complete table at every update. With no change and no requested periodic report, avoid repeated notifications. [Reporting](reporting.md) defines the formats and evidence wording.

### Spend context where it changes a decision

The lead retains the goal, dependencies, contracts, status, and uncertainty. Owners retain the implementation detail needed for their domain. Temporary investigators receive only the original evidence needed for their assignment. Summaries should preserve decisions and constraints; raw logs remain available for disputed or risky conclusions.

Count the full cost of delegation: preparation, repeated reading, execution, review, waiting, corrections, and integration. Short messages are not savings if they cause rework. More agents are not faster when returns accumulate unreviewed. Use compact event-based checkpoints and retrieve deeper evidence only for a decision, a meaningful change, or a detected inconsistency. Measure savings only when comparable project evidence exists.

## 6. Improve the method and preserve continuity

### Check the lead before the project becomes confused

At a major checkpoint, the lead should be able to explain the current goal, delivery path, owners, dependencies, evidence, uncertainties, and next action without reconstructing everything from raw history. Missing answers are an early warning. Reconcile the affected records, reduce work in progress, or arrange a planned handoff before continuing dependent work.

Self-improvement is part of delivery, not an endless separate project. Identify a repeated problem, form a causal explanation, change one relevant part of the process, and observe the next checkpoint. A recurring interface mismatch may justify earlier contract review; one typo does not justify a new permanent approval layer. Distinguish product corrections, project-specific process changes, and proposed permanent skill changes. [Controller practice](controller-practice.md) supplies the detailed procedure.

### Continue, hand off, or stop deliberately

Maintenance enters the same loop through real feedback and current evidence. During a genuine idle period, preserve the next options and stop rather than inventing work. Pause the relevant monitoring when the project pauses or its purpose ends.

A lead handoff transfers responsibility as well as context. Plan it when continuity, capacity, or availability requires it, not only after the current lead becomes ineffective. Preserve the effective brief and evidence index, verify the live baseline, resolve shared ownership and unknown operations, and establish one incoming coordinator. Context compaction alone does not discard obligations or justify a competing lead. [Recovery](recovery.md) defines the transfer and resumption checks.

### Is the architecture helping?

A useful setup makes the next action, owner, contract, and evidence clear. It lets owners proceed without constant permission, gives the lead visibility without requiring every detail, and allows the user to understand one coherent project state.

Warning signs include repeated re-explanation, incompatible local plans, several implementations of one rule, work arriving faster than it can be reviewed, unowned integration tasks, recurring missing requirements, and reports whose “complete” claims later reverse. Treat these as evidence for changing the organization, not merely reasons to ask everyone to be more careful.

The architecture is allowed to shrink. Closing an unnecessary workstream, merging tightly coupled responsibility, or returning to one agent can be the correct improvement.
