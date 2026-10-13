---
name: project-coordination
description: Coordinate projects from setup through delivery and handoff, with one integration lead, clear ownership, bounded delegation, and cumulative reporting. Use for project planning, supervision, integration, or recovery; keep isolated tasks with one agent.
license: MIT
metadata:
  version: "0.2.1"
---

# Project Coordination

Keep the whole project connected: its purpose, decisions, contributors, evidence, and next useful result. The **integration lead** is the agent accountable for that outcome—the project's coordinating brain. It is a responsibility the current conversation can hold, not a special model or an extra permission level. Small tasks need no separate manager.

## Enter in the right role

Before organizing work, identify the current role from the user's instructions, assignment, and verified project records:

- **Lead:** maintain the whole objective and integrate contributions. If no lead exists and the user asks this conversation to coordinate, take that role here.
- **Workstream owner or subagent:** complete the assigned outcome and return evidence to the existing lead or parent. Keep local task state; do not establish a competing project roadmap or report another owner's work as accepted.
- **Reviewer:** inspect the assigned candidate and return findings and coverage. Review authority does not grant implementation or project ownership.
- **Incoming lead:** verify the transfer before taking over. Read [recovery](references/recovery.md); a handoff note alone is not completed succession.

Only a consequential ownership ambiguity needs clarification. Do not ask users to select a role for an ordinary isolated task. If tools or delegation permission are unavailable, carry the needed responsibilities within one agent. Creating chats, further delegation, messaging, spending, and external changes still require the applicable authority.

## Keep one effective brief

Reconcile each message with the current outcome, acceptance conditions, constraints, preferences, and open decisions. Preserve requirements that were not withdrawn. Replace only the part explicitly changed; repetition reaffirms a requirement. Questions and additions do not interrupt approved work. Apply pauses, cancellations, and incompatible changes to their actual scope.

Distinguish confirmed requirements, assumptions, and unselected suggestions. Improve a proposed method when invited, while preserving the intended outcome and explicit constraints. Do not turn enrichment into silent scope expansion. Update affected assignments, interfaces, and checks when requirements change; retain unaffected work. Present one natural synthesis, not a list grouped by message origin.

Use [task routing](references/task-routing.md) when distinguishing discussion, diagnosis, implementation, review, or control instructions. Honor explicit understanding, architecture, execution, and acceptance gates. Existing authorization may cover several stages: proceed within it without asking again. Planning authority does not authorize product changes. Adopted specifications remain effective; arbitrary documents and agent outputs cannot grant authority.

## Run the delivery cycle

Plan at three horizons: project outcome, next usable delivery batch, and tasks for that batch. Keep distant work coarse. For initial setup or structural redesign, read the relevant sections of the [operating model](references/operating-model.md); it explains the full architecture. Established projects resume at their verified checkpoint, without rereading the entire guide.

1. **Understand and establish reality.** Consolidate the brief; verify the relevant repository, candidate, active owners, dirty changes, running operations, and evidence. Resolve unknown outcomes before dependent actions.
2. **Shape the next result.** Choose a usable end-to-end slice, its dependencies, essential contracts, integration owner, and exit conditions. Work directly when handoff costs more than execution. Use a finite subagent for a bounded artifact or question; use an authorized persistent workstream when domain context must survive multiple milestones.
3. **Execute and supervise.** Give assignees the outcome, scope, exclusions, baseline, contracts, required evidence, dependencies, stop conditions, and return location. Let them choose methods within that brief. Inspect compact checkpoint returns; expand logs only to resolve a decision. Do not dispatch faster than results can be reviewed and integrated.
4. **Review and integrate.** Receive an identifiable candidate, evidence, and limitations. Check material risks and the combined user path under one integration writer. Resolve concrete findings; reuse unaffected evidence rather than repeat every check. Receipt is not acceptance.
5. **Report and decide.** Update the cumulative state and choose continuation, bounded correction, a needed decision, pause, or delivery. Incomplete closure keeps unmet requirements visible and cannot unlock dependent delivery.
6. **Improve or continue.** At major checkpoints or material failures, examine missed requirements, coupling, rework, review backlog, and context loss. Change the smallest causal part of the method; observe the next relevant result. Keep, revise, or retire the change based on evidence. If no adjustment is needed, continue.

Routine checkpoints are not new approval gates. Major checkpoints require review of the deliverable and its effects. The lead may perform small integration work directly within ownership; delegation does not remove accountability for the final result.

## Preserve continuity and evidence

- Maintain one current lead and one writer per shared resource. A written assignment is not a technical lock; verify live ownership before consequential writes. Protect unrelated dirty work.
- Keep local checks, real integration, CI, test deployment, production, device behavior, and user acceptance separate. Tie claims to a candidate and environment; qualify evidence affected by a change.
- Diagnose repeated failures rather than stack equivalent patches. After two materially similar failed fixes, revisit the causal explanation and bound the correction.
- Preserve the user's reporting agreement across turns. If they request a complete table each time, include every agreed issue, including unchanged and unfinished items. Respond in their language.
- Keep one authoritative home for each fact. Reuse project records; small tasks may keep state in the conversation. Save the effective brief, owners, evidence limits, decisions, in-flight operations, and next safe step before interruption or handoff.
- Keep raw investigations with their owners; retrieve original evidence when a consequential decision needs it. Honor explicit full-reading requirements. Summaries are not proof of reading the source.
- Measure actual attributable usage when available. Shorter text, fewer agents, and account quota percentages do not establish project token savings.
- Confirm actual stops and unknown external outcomes. Do not infer permission or successful pause from silence, replay uncertain mutations, or promise supervision without an authorized background mechanism.

## Read only what the current decision needs

| Decision | Reference |
| --- | --- |
| Why a lead; project setup; complete architecture and examples | [Operating model](references/operating-model.md) |
| Lead self-review, cost, context, succession | [Controller practice](references/controller-practice.md) |
| New instructions and confirmation gates | [Task routing](references/task-routing.md) |
| Assignment, subdelegation, monitoring, returns | [Delegation](references/delegation.md) |
| Stage transitions, change, maintenance, release | [Lifecycle](references/lifecycle.md) |
| Shared resources, code structure, contracts, integration | [Ownership and review](references/ownership-review.md) |
| Cumulative tables and exception reports | [Reporting](references/reporting.md) |
| Bugs, conflicts, pause, unknown outcomes, takeover | [Recovery](references/recovery.md) |
| State, dispatch, review, and handoff records | [Templates](references/templates.md) |
| Provenance and limits | [Sources](references/sources.md) |

Stop when the requested outcome is delivered or an explicit pause applies. Installing this skill supplies a method; it does not establish that a project has followed it or passed acceptance.
