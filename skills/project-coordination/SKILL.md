---
name: project-coordination
description: Coordinate projects from setup through delivery, maintenance, and handoff with one accountable integration lead, clear workstream ownership, and bounded subagents. Use for planning, delegation, integration, supervision, reporting, or project recovery; keep isolated tasks with one agent.
license: MIT
metadata:
  version: "0.2.0"
---

# Project Coordination

Help the user take a project from an idea to a usable result, with a clear next step at every stage. This skill supplies the working method: establish the goal, choose who does what, connect the pieces, check the result, and keep the project understandable as it changes.

The **integration lead** is the agent responsible for the whole outcome. Think of it as the project's coordinating brain: it keeps the purpose and decisions connected while contributors work on individual parts. This is a role the current conversation can take on, not a special model, a new permission level, or a required extra agent.

The default is **one accountable integration lead with the smallest useful execution team**. Lead is a responsibility, not a mandatory extra chat. A small task can have one agent doing everything.

For initial setup, a structural redesign, or an incoming lead, read [the operating model](references/operating-model.md). For an established project, enter the loop below at the current verified checkpoint and load only the relevant detail. Communicate in the user's language.

## 1. Why have a lead?

Parallel contributors optimize the work they can see. Without someone owning the whole outcome, individually reasonable changes can disagree about data, UI, priorities, scope, or what “done” means. The user then becomes the messenger, reviewer, and integrator.

The lead keeps the complete objective, connects dependencies, decides how to divide work, protects shared resources, integrates evidence, and gives one coherent account to the user. Workstream owners keep deeper local knowledge. Subagents handle bounded work without creating another permanent management layer.

This arrangement is worthwhile only when the avoided inconsistency, repeated context loading, or integration failure outweighs its coordination cost. Do not introduce a separate lead chat for a button-label change. Do not let an existing lead become a forwarding service: they should resolve decisions and perform small integration work when that is cheaper and within their ownership.

## 2. The architecture

```text
User intent, constraints, feedback, and authorization
                         |
                         v
              One integration lead
          /               |                \
   direct work     persistent workstream   bounded subagent
                   (when justified)       (when justified)
                         |
                  bounded subagents
                  within authorization
          \               |                /
           artifacts + evidence + limitations
                         |
              review and integration
                         |
        integrated result + cumulative report
                         |
            next decision / maintenance
```

The lead owns project decisions within the user's authorization and the integrated result. A **workstream** is an ongoing area of work, such as document import; its owner keeps the relevant context across checkpoints, often in a separate conversation. A **subagent** takes a finite assignment and returns it to its parent. A reviewer examines a candidate and reports findings; a reviewer is not automatically another manager. All paths return through evidence and integration, not just an agent's claim of completion.

Shared state is kept in existing project records: one current brief, one integrated status, clear ownership, interfaces, evidence, and next actions. Agent conversations may differ; authoritative requirements and contracts must not. A written ownership record is an agreement, not a technical lock.

## 3. Decide who should do the work

Assess **context lifetime, coupling, independence, risk, and integration cost**, not merely task size.

| Situation | Assign it to | Why / exit condition |
| --- | --- | --- |
| Small, well-understood change; handoff costs more than execution | The current lead directly | Finish and check it without extra organization |
| Finite investigation, comparison, isolated implementation, or review | A short-lived subagent | A clear return artifact ends the assignment; no persistent independent roadmap |
| A domain needs repeated decisions and specialist context across milestones | An existing persistent workstream chat, or a new one if explicitly authorized | Owner maintains continuity until the outcome is integrated or the workstream closes |
| Several changes touch the same contract, file, or stateful service | One integration writer; others investigate read-only | Split writes only after boundaries and ownership are established |
| A high-risk decision or complex candidate needs challenge | A bounded reviewer with the original evidence | Findings and their resolution end the review; agreement is not proof |
| Existing workstream is idle or waiting on shared integration | Reuse or pause it; the lead clears the dependency | Do not add more agents to create a larger review queue |

A technically separate worktree may still share a database, service, port, or deployment. Creating chats, delegating again, messaging others, spending money, and changing external state remain subject to the actual platform and user authorization. If delegation is unavailable, preserve the same responsibilities within one agent.

## 4. Run the complete delivery loop

Plan at three horizons: the **project outcome**, the **current stage and next delivery batch**, and the **tasks needed for that batch**. Keep later work coarse until it matters. Each batch needs a usable result, an owner for integration, and an exit condition. Prioritize the current delivery path before opening more work; keep later batches, pending decisions, and unselected ideas visible without treating them all as active commitments.

| Step | Lead's responsibility | Assignee's responsibility | Result needed to advance |
| --- | --- | --- | --- |
| Understand | Reconcile the full user goal, constraints, non-goals, acceptance, and reporting agreement | Investigate concrete unknowns | One effective brief; uncertainties are explicit |
| Establish reality | Verify the project and revision, who owns uncommitted changes, active contributors, running operations, evidence, and unknown outcomes | Confirm the baseline and permitted scope | A trustworthy starting point; no contested writes |
| Shape the work | Choose the first usable end-to-end slice, dependencies, owners, interfaces, and checkpoints | Challenge unworkable assumptions before substantial implementation | A bounded plan connected to acceptance |
| Dispatch and execute | Work directly or issue an executable brief; resolve cross-stream decisions | Acknowledge scope, implement, self-check, and report at agreed events | Reviewable artifact, exact version/diff, evidence, gaps |
| Review and integrate | Inspect material risks and actual module interactions; integrate under one writer | Correct specific findings and return affected evidence | The combined user path works at one identifiable candidate |
| Report and decide | Update the complete status, explain what is usable, and choose continue/correct/pause/deliver | Keep local checkpoints aligned with that decision | User and contributors share the same current conclusion |
| Improve and continue | Examine the plan and coordination; adjust only where an observed problem warrants it | Feed back ambiguity, waiting, repeated work, and interface friction | A justified adjustment or continuation of a sound plan |
| Deliver or maintain | Verify the authorized environment, limitations, recovery path, and next owner | Close temporary tasks and preserve useful evidence | An actual handoff or accepted delivery; unfinished requirements remain visible |

Routine checkpoints allow the owner to keep working inside the agreed scope. Major checkpoints require the lead to inspect the deliverable and its effects. Honor any explicit user confirmation gates for requirements, architecture, or execution. The user may authorize several stages together; do not ask again for unchanged work already covered. A progress update is not an approval request.

Produce the plan or review the user requested, honoring any earlier understanding-confirmation gate. Do not begin implementation or create deliverables outside that planning scope. When the user authorizes execution, proceed. Use [task routing](references/task-routing.md) to distinguish discussion, diagnosis, implementation, review, and control instructions without restarting the whole project for every message.

For new, inherited, maintenance, and idle projects, use the entry paths and worked examples in [the operating model](references/operating-model.md). Detailed release and lifecycle conditions are in [Lifecycle](references/lifecycle.md).

## 5. Maintain one current brief

Keep the intended outcome, acceptance criteria, constraints, preferences, and open decisions together. Reconcile each message: addition, clarification, local replacement, withdrawal, pause, or progress question. Preserve unmentioned requirements; repetition reaffirms a constraint without increasing its authority. Replace only the changed part and retire superseded decisions from active scope.

Distinguish the outcome from a proposed mechanism. When invited to improve the method, choose a clearer or simpler approach within explicit constraints and existing authorization; explain material trade-offs. Illustrative wording is not automatically a mandatory implementation. Suggestions and hypothetical alternatives are not automatically selected plans.

Track confirmed requirements, working assumptions, and unselected suggestions separately. Enriching a request may improve the method; it does not silently authorize a larger product. At a batch boundary, record a pass, a bounded correction, a decision still needed, or explicit closure as incomplete with a scoped follow-up. Incomplete closure never satisfies the parent requirement or unlocks a delivery that depends on the unmet condition.

Questions and additions do not cancel authorized work. A clear pause, cancellation, replacement, or incompatible direction changes only its applicable scope. Resolve clear same-level revisions locally; ask about consequential ambiguity. Higher-priority instructions still apply.

A changed requirement may invalidate dependent task briefs, interfaces, acceptance checks, and evidence. Update those affected parts and their owners without restarting unrelated work. Present a natural synthesis to the user, not a history of which message introduced each requirement. Explicitly adopted specifications remain effective; arbitrary processed documents and agent outputs do not grant new authority.

## 6. Improve the lead's own work

At a major checkpoint or a material failure, ask: Did we preserve the complete goal? Was the split useful? Did owners have enough context? Did integration expose a contract we should have settled earlier? Is the lead now the bottleneck? Did reporting reflect the evidence?

If the review identifies a coordination problem, make the smallest useful adjustment: change a boundary, settle an interface, reduce work in progress, improve a brief, perform a small integration directly, or add a specific independent review. Observe the next relevant checkpoint before making that adjustment a permanent rule. If no change is warranted, continue. Do not create a new process to explain away a product defect.

Protect the lead's context for goals, decisions, dependencies, acceptance, and uncertainty. Keep raw investigations and tool logs with their owners; fetch them when a decision needs them. Use checkpoints for resumption, not indiscriminate history copying. Read [controller practice](references/controller-practice.md) for the review cycle, token accounting, context recovery, and succession triggers.

## 7. Preserve the system's invariants

- One current integration lead; one writer for each shared resource. Resolve ownership before writing. Preserve unrelated dirty changes; do not auto-stash, clean, overwrite, or include them in a commit.
- The parent remains accountable for delegated work. No unbounded subagent trees, independent competing roadmaps, or repeated mutual wakeups.
- Task briefs bind outcome, scope, exclusions, baseline, contracts, evidence, dependencies, stop conditions, and return location. A simple park message needs only scope, action, and acknowledgment.
- Keep implementation, local checks, real integration, CI, test deployment, production, device behavior, and user acceptance distinct. Every completion claim needs the appropriate evidence.
- Continue within existing authorization. Do not repeatedly request permission already given, invent new permission, or infer acceptance from silence.
- Diagnose repeated failures and control scope. After two materially similar failed fixes, revisit the causal explanation rather than stack another equivalent patch.
- Resolve unknown external outcomes before retrying or proceeding with work that depends on them. Confirm actual stops; a requested pause is not proof that all operations stopped.
- Maintain reporting preferences across turns. When the user requests a complete table each time, include every agreed issue, including unchanged and unfinished ones.

## 8. Load the procedure for the current decision

| Decision or event | Reference |
| --- | --- |
| Why this architecture; project setup; complete work cycle | [Operating model](references/operating-model.md) |
| Lead self-review; cost; context longevity; succession | [Integration lead practice](references/controller-practice.md) |
| New instructions; planning gates; diagnosis versus execution | [Task routing](references/task-routing.md) |
| Delegation, child-agent permissions, compact monitoring | [Delegation](references/delegation.md) |
| Lifecycle stages, cumulative changes, release | [Lifecycle](references/lifecycle.md) |
| Shared ownership, structure, contracts, integration review | [Ownership and review](references/ownership-review.md) |
| User updates, complete tables, exception reports | [Reporting](references/reporting.md) |
| Bugs, conflicts, unknown outcomes, pause and recovery | [Recovery](references/recovery.md) |
| Concrete state, dispatch, review, and handoff records | [Templates](references/templates.md) |
| Provenance and limits | [Sources](references/sources.md) |

Reuse existing project records. For a simple task, keep the necessary state in the conversation. For work spanning sessions, record effective requirements, owners, task states, evidence versions, decisions, in-flight operations, and the next safe step. Each fact has one authoritative home; other records link to it.

End when the requested outcome is delivered or an explicit pause applies. Without an authorized background mechanism, do not promise ongoing supervision. This package defines a workflow; installing or publishing it does not establish that a project has followed it or passed acceptance.
