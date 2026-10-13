# Project Coordination

A practical guide to keeping a Codex project on track, from the first idea to delivery and maintenance.

[Chinese overview](README.zh-CN.md)

You describe what you want, Codex starts building, and the project grows. Soon there are several conversations, unfinished fixes, new ideas, and people saying their part is done. Someone needs to preserve the full goal, check that the parts work together, and explain what is actually ready.

Project Coordination gives that responsibility a name: the **integration lead**. This is the conversation that keeps the whole project connected. It holds the current requirements, chooses the next useful result, assigns work when that helps, checks the combined outcome, and gives you one coherent report.

Think of it as the project's coordinating brain. It does not need to do every task or retain every implementation detail. It needs to know how the work fits together and what the evidence supports. The current agent can fill this role; a small task needs no extra agents or management files.

The skill provides both the overall architecture and the practical steps: how to start, when to split work, how to supervise it, what to report, and how to recover when the plan stops working. It is useful whether you are directing a project in plain language or already working closely with the code.

## Get started

Start with [SKILL.md](skills/project-coordination/SKILL.md), or read the [complete operating model](skills/project-coordination/references/operating-model.md) to understand the architecture. Install the `skills/project-coordination` directory through a tool that supports Agent Skills, or ask your agent to read the entrypoint. The optional `agents/openai.yaml` provides Codex interface metadata.

> Use $project-coordination to lead this project. Establish the complete goal and current state, recommend the smallest useful team, and define the next usable result and reporting format. Keep work within my existing authorization and honor any confirmation steps I request.

For an existing project, provide the location of its current records and work. The lead should verify them and continue from the next unfinished step, without replacing the project's established structure just to match a template.

For a planning conversation, you can say: “Help me organize and improve the requirements first. Let me confirm the architecture before you begin implementation or change the product.” For an approved task, you can say: “Proceed with this plan and verify the result.” The skill distinguishes these requests so planning does not turn into premature execution, and approved work does not stall on repeated permission questions.

The canonical skill and references are in English. Agents should still communicate in the user's language. The Chinese overview is documentation, not a second set of skill rules.

Review the contents before installing. This package includes no runtime scripts, dependency installer, or configuration hooks.

## How the work fits together

```mermaid
flowchart TD
  U[User goals and authorization] --> L[One integration lead]
  L --> D[Handle small tasks directly]
  L --> W[Ongoing workstream owners]
  L --> S[Finite subagent assignments]
  W --> C[Bounded child tasks when useful]
  D --> E[Artifacts and verification evidence]
  S --> E
  C --> W
  W --> E
  E --> R[Bounded review and real integration]
  R --> L
  L --> P[Consistent cumulative reporting]
```

The roles differ by responsibility and context lifetime:

| Form | Use it when | What comes back |
| --- | --- | --- |
| Lead works directly | The task is small, closely coupled, or cheaper to do than hand off | A checked result |
| Subagent | A finite investigation, isolated change, or review can be clearly bounded | An artifact, evidence, and limitations |
| Workstream owner, often in a separate chat | A domain needs continuing attention and repeated decisions across milestones | Reviewed progress toward an ongoing outcome |
| Independent reviewer | A consequential decision or complex candidate needs a fresh challenge | Specific findings tied to the actual candidate |

Separate chats are used only when authorized and worthwhile. More contributors create more integration work, so the lead limits active work to what can be reviewed and combined. When tools do not support delegation, one agent can carry the same responsibilities.

## The full project workflow

Plan at three horizons: the overall project, the current stage and next delivery batch, and the tasks that make that batch possible. Keep later work coarse until it becomes relevant. Then repeat one delivery cycle:

1. **Understand the outcome.** Consolidate requirements, improve the framing, and separate commitments from assumptions and suggestions.
2. **Verify the starting point.** Establish what exists, what is unverified, who owns current work, and which operations are still in progress.
3. **Choose the next useful result.** Set boundaries, dependencies, essential interfaces, and evidence needed to finish the batch.
4. **Execute with clear ownership.** Work directly or delegate a complete brief, then let the owner proceed within it.
5. **Review and integrate.** Inspect the return, resolve real findings, and check the complete user path at an identifiable version.
6. **Report and decide.** Present the cumulative state and choose the next action: continue, correct, seek a decision, pause, or deliver.
7. **Improve and continue.** Fix causes of repeated confusion, adjust the organization when needed, and preserve continuity through maintenance or handoff.

New instructions enter this workflow at the relevant point. They do not erase earlier requirements or restart the project by default. A returned task is not automatically an integrated feature; an integrated feature is not automatically released or accepted by the user.

## What is in the skill

| Part of the system | What it explains |
| --- | --- |
| Purpose and organization | Why someone owns the whole outcome; decision rights; when each form of delegation helps |
| Project setup and planning | New and inherited projects; priorities; stages and delivery batches; dependencies and exit conditions |
| Continuous delivery | Dispatch, checkpoint supervision, review, shared writes, interface consistency, and integration |
| Instructions and change | Planning versus execution; confirmation gates; cumulative requirements; scope changes and bug diagnosis |
| State, reporting, and cost | Authoritative records; complete status reports; valid evidence; attention, context, and delegation cost |
| Improvement and continuity | Lead self-review; preventive checks; maintenance; pauses, recovery, and succession |

The [operating model](skills/project-coordination/references/operating-model.md) connects these parts and walks through an example. Focused references and [templates](skills/project-coordination/references/templates.md) supply the procedures. Load them when needed rather than copying the entire package into every assignment.

## What this should feel like in practice

You should be able to ask “Where are we?” and get a clear account of the whole project: what works, what evidence supports that claim, what remains, and who does what next. Contributors should receive enough context to act independently, without inventing incompatible product rules. A small bug should get a bounded diagnosis and fix, not automatically become a redesign.

The lead also reviews its own method. If tasks keep waiting for the same interface, settle it earlier. If finished work arrives faster than it can be integrated, reduce concurrency. If a workstream no longer needs a separate owner, fold it back into direct work. Improving the process can mean removing a layer.

## Limits

This is a coordination skill, not an agent runtime. It grants no deployment authority and starts no background monitoring. It does not promise a percentage of token savings, zero rework, or official certification.

See [validation](VALIDATION.md), [evaluation scenarios](evaluations/SCENARIOS.md), and [sources](skills/project-coordination/references/sources.md). Report issues with a sanitized scenario, expected behavior, and observed difference; do not upload credentials or user documents.

Version 0.2.0 · MIT License.
