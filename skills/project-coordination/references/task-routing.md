# Handling requests within an ongoing project

A message changes the project's current brief; it does not create a new project by default. First locate the work it affects, then choose the appropriate response. A long message may contain a product requirement, a suggestion, a status question, and an instruction to continue. Handle each part without dropping the rest of the project.

## 1. Establish what the user is asking for

Read the complete request and the effective brief. Identify the intended outcome, the problem behind the request, constraints, acceptance conditions, and any explicit limits on what may happen next. Distinguish these three kinds of information:

| Kind | How to use it |
| --- | --- |
| Confirmed requirement | Keep it in active scope until the user changes or withdraws it. Preserve its acceptance conditions. |
| Working assumption | State it when it could affect the result. Verify consequential assumptions before dependent decisions; do not report them as user choices or observed facts. |
| Suggestion or possibility | Evaluate its value and trade-offs. Keep it separate from committed work until selected within the user's authorization. |

Summarize the intended result in the user's language. Improve the framing where useful: identify a missing failure state, a simpler approach, or an overlooked dependency. Do not convert every helpful idea into a mandatory feature. If the user has asked to review this understanding before diagnosis or writing, stop at that gate; unrelated authorized work may continue.

The user is not required to finish all possible thinking before work can begin. Settle the next meaningful decision, keep later uncertainty explicit, and use the authorization already given. A new idea arriving during implementation updates its applicable scope; it does not automatically interrupt the entire project.

## 2. Choose the work path

| Request | First response and authorized work | What makes the next step valid |
| --- | --- | --- |
| Explore an idea or plan a project | Organize the outcome, enrich the options, and identify unknowns. Produce the requested planning output at the agreed stage; confirm understanding first if the user reserved that gate before architecture. Do not move into implementation or deliverables outside the planning scope. | Any requested understanding and architecture gates are satisfied before dependent work; implementation additionally requires execution authority. |
| Write or implement an approved plan | Reconcile the latest constraints, verify the baseline, and execute the next bounded batch. | The work remains within the approved outcome, authority, and acceptance conditions. No repeated start confirmation is needed. |
| Report a bug | Establish symptoms, expected behavior, impact, and evidence. Diagnose the responsible layer when authorized; a report alone may call for intake rather than modification. | Follow any requested intake confirmation. Before changing code, have a supported causal explanation, a bounded fix, and authority to implement it. |
| Explicitly fix a bug now | Briefly state the understood problem; investigate, challenge the proposed cause, implement the supported fix, and verify the original failure. | The fix stays within scope. Escalate only a consequential new choice, permission boundary, or unresolved ambiguity. |
| Review or audit only | Inspect the specified evidence and return findings, coverage, and uncertainties. | Separate authorization is needed to turn a read-only review into edits. |
| Refactor or migrate | Establish the behavior to preserve, actual need, affected consumers, migration path, and recovery. Keep discovery separate from irreversible operations. | The concrete plan and effects fit the user's authority and requested gates. |
| Ask a question, request status, or clarify a requirement | Answer and update the current brief where needed. | Existing authorized work continues unless the message changes, pauses, or cancels it. |
| Continue, resume, pause, cancel, or hand off | Determine the exact scope and inspect the relevant checkpoint and runtime state. Use [recovery](recovery.md). | A request to stop is not evidence that processes stopped; a request to resume is not proof that an old baseline is still valid. |

When intent is mixed, preserve each applicable path. For example, a request to fix an approved bug and discuss a future redesign authorizes the bounded fix while leaving the redesign at the planning stage.

## 3. Use confirmation gates deliberately

There are four different decisions a user may reserve:

1. **Understanding:** Have we captured the right problem and all requirements?
2. **Approach:** Is this the architecture, scope, or trade-off they want?
3. **Execution:** May the concrete work or external action proceed?
4. **Acceptance:** Does the delivered result meet their needs?

These are decision boundaries, not four compulsory messages for every task. Honor explicit requests to confirm them separately. Explicit authorization can cover several at once, such as “use your judgment, diagnose and fix this now.” Do not infer confirmation from silence, impatience, or a generic acknowledgment when the decision remains ambiguous. Do not reopen an unchanged gate merely because another agent takes over.

Use only the confirmation boundaries the user actually reserved. For example, when they request both understanding and architecture approval, the sequence is: consolidate and enrich requirements → confirm understanding → develop the full architecture with your own analysis → review it with the user → challenge the agreed architecture once more → execute after authorization. A request to approve only the architecture does not add a separate requirements-approval exchange. Preparation and self-review are not additional approval requests. The final self-review looks for missing dependencies, contradictions, unnecessary process, and unsupported assumptions. Return consequential scope changes to the user; resolve routine drafting and implementation choices yourself.

For a bug, root-cause work replaces speculative architecture: capture the failure → satisfy any requested intake gate → reproduce and locate the violated contract → propose and challenge the smallest effective correction → implement within authority → verify the original failure and affected interactions. Do not make an unsupported promise of a root cause before examining evidence.

Before a requested approval, complete the already-authorized preparation needed to make the choice concrete. Present the candidate, effects, recommendation, and exact remaining decision. Do not ask the user to approve vague future work that could already have been made reviewable.

## 4. Reconcile changes without losing the project

Keep one effective brief. Add new requirements; clarify existing ones; replace only clauses explicitly changed; retire withdrawn choices from active scope. Unmentioned requirements remain active. Repetition reaffirms importance without granting extra authority. Higher-priority instructions still apply.

Preserve a light trace to the relevant instruction or decision so a successor can resolve conflicts. User-facing output should read as one coherent plan, not a list of amendments labeled by their message of origin. Report actual changes in results and risks when useful; do not spotlight every new instruction unless asked.

| Impact | Lead action | Evidence and communication |
| --- | --- | --- |
| Within one task's existing contract | Update its brief and let the owner continue. | Recheck affected behavior; do not restart unrelated tasks. |
| Across a batch or shared interface | Reconcile providers and consumers; adjust ownership, dependencies, and integration checks. | Identify which previous evidence still applies. Notify affected owners with the changed contract. |
| Changes the project goal, mandatory acceptance, cost, or authorization | Make the trade-off explicit and seek a decision when it is not already authorized. | Preserve prior work and unmet requirements; do not silently redefine success. |
| Pauses or cancels identified work | Stop new dependent assignments and establish actual operation status. | Record acknowledgments and unknown outcomes, keeping independent authorized work separate. |

Example: a user asks for an offline reader with stable bookmarks, then adds optional selected-text translation, then limits the beta to invited testers. The current brief retains offline reading and stable bookmarks, adds only the authorized online exception, and applies the access restriction. It does not permit whole-document uploads or discard the original reading work. If paragraph translation was explicitly deferred, retain it as deferred rather than treating the entire translation requirement as canceled.

For a small, clear, authorized edit, this reasoning may take only a few sentences. The purpose is to choose the correct action, not to turn every message into a planning ceremony.
