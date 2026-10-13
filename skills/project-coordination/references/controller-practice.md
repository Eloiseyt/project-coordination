# Integration Lead Practice

The **integration lead** is responsible for the whole project outcome, as described in [the operating model](operating-model.md). This is a responsibility, not a special permission level or a mandatory extra chat. Use this procedure to choose and integrate the next useful work, improve the coordination method, and preserve enough context to continue safely.

## 1. Allocate attention before allocating agents

The lead's attention is a limited project resource. If it follows whichever message arrived last, easy local work can displace an unresolved interface, an approaching commitment, or a mandatory acceptance gap. If the lead personally checks every implementation detail, completed work queues behind them. Active coordination means choosing where a decision or intervention will advance the complete outcome, then leaving owners free to execute within settled boundaries.

Keep four views in the existing project record, or in the conversation for a small task. They are views of the same requirements, not four new systems:

| View | What belongs here | How it moves |
| --- | --- | --- |
| Delivery path | The current user outcome, complete acceptance conditions, and dependencies leading to the next meaningful delivery | Changes only through reconciled requirements, verified facts, or an authorized project decision |
| Next batch | Ready, authorized work that can be executed, reviewed, and integrated with available capacity | Admit a bounded slice; keep returned candidates visible until integration is resolved |
| Pending decisions | A specific unresolved choice, its decision owner, affected work, and any real deadline | Resolve within the team's authority or prepare a reviewable question for the user; independent work can continue |
| Parked suggestions | Useful possibilities outside the active plan, with enough context to reconsider them | Promote only after scope and authorization are established; being recorded does not authorize implementation |

Choose the next batch along the delivery path by considering acceptance impact, risk, dependencies, genuine deadlines, and total effort. Resolve a consequential unknown before building several consumers on an assumption. Unblock a shared dependency before producing more work that must wait for it. Account for deadlines the user or project actually set; do not invent urgency or promise unsupported completion times. A recent addition does not automatically outrank every other active requirement.

Count work awaiting review and integration as work in progress, not as capacity already freed. Before admitting more implementation, identify who can inspect and integrate its return. If that capacity is unknown, start with a small batch and observe its actual return. If candidates pile up, age into incompatible versions, or repeatedly wait on the lead, reduce new dispatches and clear the constraint. Let ongoing work finish a safe slice or park with acknowledgment; do not discard it or arbitrarily kill operations to shrink a queue.

## 2. Steer the existing delivery cycle

These are the lead's decisions within the operating model's delivery cycle, not a second loop to run alongside it. Enter at the decision currently needed; use the event table to choose review depth.

### Read the change and establish what is still true

**Input:** the current brief and checkpoint, new user input, owner reports, candidate evidence, and relevant runtime state.

**Action:** read the changes first. Reconcile additions and local replacements with the full effective requirements; retire only explicitly canceled or superseded scope. Check the affected revision, write ownership, and in-flight or unknown operations before acting. Read original material where a decision depends on it, rather than accepting an optimistic summary.

**Output:** a current brief, facts that changed, evidence that remains valid, and specific unknowns. Freeze only contested writes or actions that depend on an unknown outcome. Other authorized, independent work remains available for the next batch.

### Select the next result and who should produce it

**Input:** unmet acceptance conditions, the four work views, available owners, current review capacity, and authorization.

**Action:** identify the constraint on the next delivery and choose a bounded result that removes it or advances independent work. Select the execution form by context lifetime and coupling:

| Form | Choose it when | Keep the assignment bounded by |
| --- | --- | --- |
| Lead implements directly | The correction or integration is small, already understood, and cheaper than a handoff | Acquiring write ownership and reserving attention for other pending decisions; hand over at a safe point if implementation begins to dominate |
| Persistent workstream owner | The domain needs repeated decisions and retained detail across milestones | A coherent domain outcome, shared contracts, and closure conditions; reuse a suitable existing chat and create another only with applicable authorization |
| Short-lived subagent | One finite investigation, artifact, or isolated change can be checked independently | Minimum sufficient original evidence, a defined return, and no separate continuing roadmap |
| Read-only reviewer or investigator | A risky assumption or candidate needs focused challenge without another writer | An identifiable baseline, a specific question, original evidence including counterevidence, and findings rather than a new implementation |

If the result or interface is unclear, investigate before multiplying assignees. If delegation tools or permissions are unavailable, keep the responsibilities within the current agent. Use [Delegation](delegation.md) for the actual dispatch and return procedure.

**Output:** the next batch, its owners, baselines, acceptance evidence, and reporting checkpoints. Choosing a team is not permission to create chats, contact others, spend money, or change external state.

### Execute with explicit decision rights

**Input:** the agreed slice and its boundaries.

**Action:** let the owner choose local implementation and verification methods inside the brief. Coordinate changes that affect shared interfaces, identities, resources, or other owners before those changes spread. The lead resolves project-level trade-offs within existing authority; the user decides actual scope or authority gaps and consequential ambiguity that cannot be resolved from the current brief.

Do not add routine approval requests to authorized work. Equally, preserve a user-specified confirmation, review, or acceptance point: local autonomy does not waive an explicit gate. Complete the analysis and reviewable proposal that can safely proceed before asking for a missing decision. State exactly which dependent action waits, and continue independent work.

**Output:** a progressing slice with known autonomy and escalation conditions, rather than a stream of requests for permission to take ordinary steps.

### Inspect at the event that can change the next decision

**Input:** a result, meaningful new evidence, a boundary change, or an exception.

| Event | Lead action | Output |
| --- | --- | --- |
| Routine checkpoint: a runnable slice, settled local question, or evidence update | Confirm alignment with the brief and inspect the evidence needed for the next dependency; let the owner continue if still within scope | Updated facts and the next local action, without another routine approval gate |
| Major checkpoint: an end-to-end feature, shared contract change, migration, release, required acceptance, or handoff | Inspect the actual candidate and affected interactions, check the complete acceptance boundary, and run the brief health check below | Continue to the next stage, correct a named gap, or retain an explicit decision or acceptance gate |
| Exception: disputed ownership, incompatible versions, missing mandatory behavior, repeated failure, or unknown external outcome | Contain affected actions, preserve state, and distinguish fact from hypothesis; use [Recovery](recovery.md) | A specific diagnosis, safe continuation boundary, and evidence needed to proceed |

Events drive attention. A timer can request a status snapshot, but it does not prove completion or justify restarting work. Use compact reports and expand logs only when the decision needs them. Follow [Reporting](reporting.md), including any user requirement for a full table in every update.

### Receive the artifact, then integrate the result

**Input:** a returned candidate, original acceptance conditions, evidence, and limitations.

**Action:** first confirm that the return is identifiable and within its brief. Record it as received or awaiting integration; do not call the project delivered. Review the material risks, correct specific findings, and have one authorized integration writer combine the affected work. Verify the combined user path and relevant failures at one candidate version using [Ownership and review](ownership-review.md).

Delegate detailed review and integration where suitable; the lead retains the final project judgment. A review with no findings is not proof of all behavior. Reuse evidence whose relevant conditions remain unchanged, and rerun only affected checks unless new evidence justifies broader verification.

**Output:** an integrated result with its actual evidence level, or a bounded correction with an owner. Delivery requires the complete effective requirements at the agreed environment and any explicitly required acceptance. Neither receipt, an agent ending its turn, nor passing module tests establishes that boundary.

### Report, adjust the method, and choose again

Return to the operating model's report-and-decide step with the integrated evidence and unresolved requirements. Use the improvement procedure below only when observed friction warrants a change. When no authorized work remains, preserve the next safe entry point and stop; do not manufacture work or promise background supervision without an authorized mechanism.

## 3. Improve the method before it becomes a crisis

At a major checkpoint, briefly look ahead as well as back: are all mandatory requirements still represented; are the next shared contracts settled; can incoming candidates be integrated; does the lead still have capacity and recoverable context; and have upcoming risks or commitments changed? Use existing artifacts and records. This is a lightweight preventive check, not a mandatory meeting, a new full audit, or a reason to reopen unchanged passing work. If nothing requires adjustment, continue.

When a failure or warning warrants action, follow a causal sequence:

1. **Fact:** identify the observed omission, rework, waiting, coupling, or repeated reading, with its candidate or checkpoint. Distinguish a user-requested scope change from avoidable coordination failure.
2. **Cause:** check whether the problem came from implementation, an incomplete brief, an unstable contract, missing original context, or insufficient integration capacity. Do not automatically blame the owner.
3. **One method adjustment:** change the smallest useful part of the arrangement: clarify a brief, settle a shared interface, shrink a batch, move a small integration to the lead, or assign a specific independent review. When safe, vary one main factor so its effect can be observed; take all necessary protective actions immediately when risk requires them.
4. **Next observation:** name the next relevant checkpoint and what should differ. For example, check whether the next return covers the omitted condition or whether a candidate can integrate without renegotiating the same field.
5. **Retain or withdraw:** keep the adjustment if the evidence supports it, revise or remove it if it does not, and mark an inconclusive result as such. Do not turn an untested preference into a permanent rule.

Keep the record short: fact, causal judgment and uncertainty, changed method, owner, next observation, result. Place it in existing project decisions rather than creating another management system.

Retire process debt as well as adding safeguards. At the next relevant observation, merge duplicate instructions and remove obsolete project procedures when their original reason no longer applies. Preserve the decision history and any still-effective user requirement. A project-method cleanup does not authorize editing the shared skill or erasing an explicit constraint.

Separate three kinds of change. A **product fix** corrects behavior and needs appropriate regression evidence. A **project-method change** alters how this project divides, reviews, or resumes work and is checked at its next relevant checkpoint. A **permanent skill or memory update** affects future work and requires the applicable explicit authorization and validation. Success in one project does not automatically authorize that third change.

For example, an omitted acceptance condition may require both a product correction and a better brief. Adding a reviewer without fixing the brief does not address that cause. Repeated interface rework may instead require one contract owner and fewer concurrent writers. If the review queue keeps growing, do not dispatch more implementation to make the activity look productive.

## 4. Preserve decision context, not every detail

The lead keeps direction, complete acceptance, shared contracts, important decisions and reasons, dependencies, ownership, risk, and uncertainty. Workstream owners retain detailed investigations, local implementation knowledge, and supporting evidence. Temporary task detail returns as an artifact, findings, references, and limitations. Each authoritative fact has one home; other records point to it.

Start each decision with the effective brief, current checkpoint, and new evidence. Open detailed records when original wording matters, a claim conflicts with other evidence, conditions changed, or a consequential unknown cannot be resolved from the summary. An index is not proof of reading, and a summary is not original-file validation. Honor explicit full-reading requirements and record partial or unavailable coverage honestly.

Evidence expires through relevant changes in requirements, candidate, contract, environment, configuration, or sample, not merely because a conversation grew longer. Mark the affected scope stale and preserve unaffected results. Recheck volatile runtime state and ownership before consequential actions rather than trusting an old checkpoint.

Before context compression or a planned break, preserve the effective brief and original-source index, current baseline, write ownership and protected changes, evidence locations and limits, unresolved decisions, in-flight or unknown operations with query identifiers, and the next safe action. Do not omit counterevidence or an unmet requirement to make the summary smaller.

After compression, recover from that checkpoint and verify the actual baseline, owners, operations, and next dependency before writing. Fetch only the original material needed to resolve a mismatch. Compression or a model change does not create a new lead, cancel the objective, or justify replaying an uncertain operation. Follow the precise resumption safeguards in [Recovery](recovery.md).

## 5. Decide when leadership should continue or transfer

Keep the current lead when they preserve the goal and can handle the important decisions and integration. Prefer a bounded context refresh or compression when the issue is repeated reading or recoverable context pressure. A long chat alone is not a reason to replace the lead, and unavailable context-usage measurements must not be presented as a known limit.

Consider a planned handoff when the user requests it, the current lead has a known departure, responsibilities materially change, or foreseeable delivery and review load exceeds available capacity. A handoff can prevent a failure; it need not wait for loss of control. Use evidence from availability, upcoming commitments, context quality, and the queue, and consider whether smaller batches or delegated integration would solve the problem more cheaply. Persistent failures despite those adjustments are another reason to reassess.

A planned handoff still needs applicable authorization, a viable receiving owner, and time to transfer context. Preparing the handoff is not itself a transfer of authority. Use the exact pause, resumption, and lead-handoff sequence in [Recovery](recovery.md), together with [shared-write ownership](ownership-review.md). The transfer is complete only when the outgoing owner has stopped safely, the incoming owner has verified and accepted the transferred state with its gaps, and the main record has changed. Preserve history and allow only one current integration lead.

If contact or ownership cannot be verified, use those recovery procedures rather than treating silence, a missing process, or an old ownership date as permission to take over. Continue independent work where possible. Include handoff reading, review, and transition effort in cost accounting rather than hiding it as a fresh start.

## 6. Measure the whole effort; report time separately

Resource cost includes **execution + input reading + communication + review + rework** across the lead, workstreams, and subagents. It includes failed attempts, repeated context loading, integration, and handoff. These categories help explain cost; overlapping diagnostic tags must not be added as separate measured usage. Elapsed time and waiting are separate dimensions: parallelism can reduce time while increasing resources.

Use existing usage receipts and checkpoint timestamps where available, without building a monitoring system for a simple task:

- Record actual token fields with their request or run identifiers, time, role, and coverage. Sum distinct calls, not duplicate receipt records. Count real retries even when they serve the same logical operation.
- Respect the provider's field definitions: cached input may already be included in input, reasoning tokens may already be included in output, and a parent's aggregate may already include its children. Do not count them twice. Partial visibility is partial usage, not a project total.
- If token measurements are unavailable, say unknown. Account-wide quota percentages, text length, and intuition are not actual project-token measurements.
- Use attributable billing records for actual charges, retaining their currency and coverage. Do not invent prices or savings. Resource usage and billed money are related measurements, not interchangeable values.
- Measure elapsed time from the agreed project start to the relevant acceptance boundary, or report elapsed time so far. Do not sum concurrent task durations and call that the user's wait. Record review and dependency waits with their intervals; overlapping waits are not additive project duration.
- Track useful signals such as missing acceptance conditions, rework causes, repeated reads, interface conflicts, and review backlog. Interpret them with context; a legitimate scope change is not automatically a quality failure.

Compare methods only when scope, evidence level, measurement coverage, and conditions are sufficiently comparable. A smaller team or shorter report does not prove savings. Without a defensible baseline, describe observed changes and remaining uncertainty instead of claiming a percentage. Do not optimize measured token use by dropping acceptance conditions, necessary authorization, or critical verification.

## 7. Brief example

Consider a catalog feature with keyword and tag filtering, export of the currently visible entries, and preservation of existing favorites. This is an illustration, not a measured project result.

The lead first sees that filtering and export depend on one definition of a visible entry. They establish a small working slice with one writer, then assign the export adapter as a bounded task. At the routine checkpoint, the adapter exports all entries. The lead checks the original requirement and finds that their brief omitted “currently visible.” They keep the candidate awaiting integration, correct the product gap, and adjust the brief to link each mandatory condition to its evidence. The next return must demonstrate agreement between visible and exported entries; that observation determines whether the briefing change helped.

Before the major checkpoint, the lead notices two candidates awaiting integration and an upcoming delivery commitment. They admit no additional implementation, use an available integration owner for the settled work, and inspect the combined filtering, export, and favorites behavior at one version. Detailed export traces stay with the owner; the lead retains the contract, evidence links, and unresolved risks. If that candidate meets the agreed delivery and confirmation conditions, the lead reports the whole result. Otherwise, the missing condition stays open. Unknown token use remains unknown; fewer active tasks alone does not establish a saving.
