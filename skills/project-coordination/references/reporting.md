# Reporting

## Agree on reporting at the start

Record the user's language, preferred technical detail and table format, notification timing, and decisions they need to make. Use established preferences without asking again each turn. For projects coordinated across chats, keep this agreement in the existing main status or project adapter file; do not create a record for a small, one-off task. Write user-facing reports in the user's language; the English wording of this skill and its templates does not require English reports.

Maintain one current effective brief by reconciling cumulative requirements. Requirements remain active when later messages omit them, and repetition reaffirms them. An explicit amendment replaces only the part it changes; update the affected acceptance conditions, dependencies, and work orders together. Move canceled or superseded requirements out of the active brief and into history so old decisions remain traceable without governing current work. An addition does not automatically interrupt or cancel ongoing authorized work.

Synthesize the full effective brief naturally in user-facing reports. Keep instruction sources and revisions in internal records; do not highlight the latest amendments or label report sections by the order in which instructions arrived unless the user asks. Continue reporting actual completed work, material risks, and decisions needed; these concern project outcomes, not the source or recency of instructions.

For projects with several substantial issues in parallel, use a cumulative table in formal reports by default. When the user asks for a full report every time, repeat every agreed section in each formal progress report, including unchanged, paused, and unfinished items. Before repeating an earlier conclusion, check for new evidence; if it has not been rechecked, state the date and version of the latest evidence.

The distinction between formal and interim reports is only a default. If the user explicitly requires a complete table in every status update, follow that requirement; do not narrow it by calling an update a brief. This does not require extra messages when nothing has changed.

The lead explains what happened, what it affects, what the user can use now, and who does what next. Put tool details and logs behind evidence links. “Many tests ran” is not a product conclusion.

## Report according to the event

| Event | Report | Follow-up |
| --- | --- | --- |
| Routine checkpoint | New findings or changes, current uncertainties, next step | Continue within authorization; do not turn an update into a permission request |
| Formal status request | Overall judgment first, then the cumulative table and changes this round | A progress question does not cancel the active objective |
| Major delivery milestone | Cumulative table, candidate version, acceptance evidence, remaining risks, next milestone | After review, the lead states whether to continue or correct course |
| Failure or departure from scope | Symptoms, known facts and hypotheses, impact, actions taken, smallest next step | Pause affected actions; independent tasks may continue |
| User decision needed | Reviewable result, differences between options, recommendation and reasons, why existing authorization is insufficient | Specify exactly which actions are waiting; silence is not approval |
| User pause | Scope to stop, each executor's acknowledgment, operations in progress or with unknown outcomes, resumption entry point | Pause related monitoring; do not keep developing to tidy up the finish |
| Completion or release | Actual delivery location, target environment, verification, accepted limitations, recovery or rollback entry point | Close related monitoring; do not automatically begin the next phase |
| Routine monitoring with no change | Do not repeat the full table or invent progress | If the user explicitly requests scheduled full reports, report the unchanged state as requested |

Brief updates during execution and formal cumulative reports serve different purposes: give short progress updates during long operations as the platform requires, and provide the full table at key milestones or in the turn's final response. A brief interim update does not satisfy a request for a complete report. The user's explicit requirement for a complete table in every update still takes precedence.

## Cumulative table

Each row represents an issue with user acceptance criteria, not a chat or file. Stable identifiers prevent items from disappearing when renamed.

Retain the original requirement source and every mandatory acceptance condition for each issue. Conditions within a compound requirement may be listed separately in the same row. If any mandatory condition is unmet, the parent item remains only partially satisfied unless the user explicitly changes the acceptance scope. Do not quietly reclassify a missing requirement as a future improvement.

| ID / user issue | Changes this round and work done | Status / evidence level | Remaining gaps or blockers | Next step / owner |
| --- | --- | --- | --- | --- |
| R-01 File import failure | Fixed the identified encoding path | Real sample passed locally; candidate c1, 2026-01-01, evidence E1; test build not deployed | Not rechecked on the device where the issue was reported | Integrator prepares the test build; workstream owner retests the original file |
| R-02 Online translation | Client interaction implemented | Implementer reports mock tests passing; version, date, and original evidence still needed; not yet tested with the real service | Resource binding needs verification | Service owner performs the authorized read-only check |

These are formatting examples, not the status of a real project. Group a long list by the user's subject areas while retaining every item. Details may go in an attachment, but an attachment link alone does not satisfy a request for a complete table.

## Evidence wording

- **Implemented:** Code or an artifact exists; this does not imply testing or release.
- **Passed local verification:** State the sample and test scope; distinguish mocks, real services, and real documents.
- **Passed integration verification:** The actual modules were verified together at the same version.
- **Released to the test environment or production:** Evidence identifies the target environment and version; behavior still needs verification.
- **Accepted by the user:** Requires explicit user confirmation, not an inference from silence.
- **Implementer reports a pass; awaiting lead review:** Use this when the evidence has not been independently checked.
- **Unverified, partially satisfied, paused, or blocked:** Give the specific reason and next step; do not summarize these as complete.

Do not add test counts from different rounds to inflate the number passed. Avoid undefined completion percentages and unsupported ETAs. State dependencies and uncertainties with any time estimate.

## Quick check before sending

Are all requirements included? Does the status match the evidence? Are this round's changes distinguished from earlier evidence? Are the actual remaining issues visible? Does each action have an owner? Is there a specific decision for the user? Is there unnecessary technical noise or repeated apology?

When the user points out an omission or confusion, correct the main table and reporting agreement rather than merely promising to do better. If a status file conflicts with messages, check the current facts first; do not choose the more optimistic account.
