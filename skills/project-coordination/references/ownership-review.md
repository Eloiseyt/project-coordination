# Ownership, Structure, and Integration Review

## Main Record and Write Ownership

The lead maintains one main status record. Workstream owners write their own checkpoints and evidence, which the lead incorporates into the main status. Architecture, tasks, and evidence may live in separate files, but each fact has one authoritative source; other locations link to it.

A shared ownership record includes at least the resource or path, current writer, baseline version, permitted scope, start time, status, and evidence of release. It is a coordination agreement, not a lock that prevents a process from writing.

To acquire a shared resource: check the live branch and version, ownership of uncommitted changes, and current operations → the previous owner stops safely and explicitly releases it → the lead assigns a new owner → the new owner acknowledges receipt. A missing process, idle chat, or expired date does not replace confirmation. If the previous owner cannot be reached, preserve their changes, continue non-conflicting work, and tell the user precisely what cannot proceed.

For a prolonged loss of contact, use an evidence-backed recovery handoff: someone with the required authority approves the alternative handoff; recoverable content and diffs are preserved; verifiable runtime state or effective revocation of write access establishes that the previous assignee cannot keep writing; unresolved ownership is recorded without deleting the work; and the new owner accepts that snapshot. Do not take over a disputed resource without evidence that the previous writer cannot continue. A new worktree alone does not isolate shared databases or cloud operations.

When two tasks need the same file, prefer sequential writes, or have one integrator apply clearly identified diffs from both. Working on different functions does not make concurrent whole-file writes safe. Do not automatically stash, reset, clean, overwrite the whole file, or include the entire shared file in one task's commit.

## Interface Contracts

Before parallel work, clarify the following according to actual risk. Small functions do not require a formal protocol document:

- Input/output types, versions, field ownership, and who rejects invalid input.
- Identifiers, units, encoding, ordering, and the meaning of null and missing values.
- Handling of loading, cancellation, retries, timeouts, stale results, failures, and duplicate requests.
- When success is persisted, whether failures are recorded, and idempotency and transaction boundaries.
- Authentication and authorization, user consent, sensitive content, quotas, and external side effects.
- UI focus, closing and returning, narrow screens, themes, error messages, and state preservation.

Before changing an interface, notify its consumers and provide a compatibility plan. Do not leave modules to guess field meanings independently. Small experiments may use mock interfaces, but validate the real combination before integration.

## Structure Review for Each Batch

| Review area | What to check | Shortcut to avoid |
| --- | --- | --- |
| Rule ownership | Whether the same validation, lexical processing, permissions, or metering has a second implementation | Copying existing logic under a new name |
| Module boundaries | Whether dependencies among UI, business rules, persistence, and platform code follow existing boundaries | Inventing a separate directory scheme for every feature |
| File placement | Whether new logic belongs to the existing responsible module and public exports are minimal | Putting unrelated logic in catch-all components or utility modules |
| Complexity | Unnecessary state, pass-through layers, circular dependencies, or silent fallbacks | Judging complexity solely by line count or mechanically splitting files |
| Types and contracts | Use of the project's existing language and explicit boundary types in TypeScript projects | Hiding mismatches with `any`, disabled rules, or forced assertions |
| UI consistency | Reuse of existing components, color and spacing rules, and interaction conventions | Each assignee building a separate system of dialogs, buttons, and layouts |
| Data compatibility | Preservation of existing records, identifiers, bookmarks, history, and upgrade paths | Clearing data or changing existing identifiers to pass tests |
| Dependencies and code volume | Whether a new dependency or abstraction addresses real, current duplication or risk | Building a framework for hypothetical future needs |

Review the actual diff; this does not call for a repository-wide refactor. Record nearby pre-existing issues and decide whether they block the current goal. Put unrelated issues in separate task briefs.

## Bounded Review Process

1. Freeze an identifiable candidate: a commit, diff, or file hash. Do not silently replace it during review.
2. Give the reviewer the original requirements, candidate, and evidence, not just the author's summary that it passed.
3. Lead with findings: location, trigger, user impact, evidence, and the smallest correction. Separate confirmed defects from hypotheses that still need validation.
4. The author fixes the specified issues and returns the changes and new evidence. The lead decides whether related module interactions need another review.
5. Close rechecked issues; retain owners and risks for unresolved ones. A review with no findings does not prove there are no defects.

Do not ask multiple reviewers to repeat a full review of the same material. Divide complex reviews by risk; self-check simple tasks. Expand testing or review only when new evidence warrants it, rather than adding endless rounds.

## Integration Validation

Distinguish three decisions: **receive** a contributor's candidate, **integrate** it with the other parts, and **deliver** the complete result at the agreed evidence level. A valid return can still be waiting for integration. A working integrated candidate can still lack real-service checks, release authorization, or required user acceptance.

On receipt, compare the candidate's baseline and contract versions with the current brief and actual integration target. If they differ, identify the affected requirements and consumers before accepting its evidence. Changes to a contract, configuration, sample, or environment can invalidate a check even when the relevant source file did not change. Preserve unaffected evidence and explain what must be rechecked; do not rerun everything or reuse everything by default.

The lead checks a real user path through all involved modules and at least the relevant failure paths. Common checks include whether selections or input change when switching modules; duplicate requests create duplicate accounting entries; old results overwrite new ones; turning recording off actually prevents saving; permission failures are bypassed; and the UI remains usable with realistic content lengths.

Tie evidence to the candidate version. If code changes after all tests pass, the earlier evidence applies only to unaffected areas. A successful full build in a shared workspace does not prove that the current commit contains only the current task's changes.

Judge the batch against its original mandatory conditions. A failed condition needs a bounded correction, an explicitly scoped follow-up, or a user decision where required. If regrouping the work is authorized, the batch may be recorded as closed incomplete with a linked follow-up and owner. Its parent requirement remains unmet, and deliveries depending on that condition remain gated. Neither a smaller release nor a new task label silently changes what the user asked for.
