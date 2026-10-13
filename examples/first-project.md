# A first project, from request to checkpoint

This is a worked illustration, not a real project report or a benchmark. Candidate names and evidence paths below are fictional. Do not reuse its passing results as evidence for your project.

## 1. Start with the user's outcome

> Help me add keyword and tag filtering to my book catalog. Export only the books currently visible. Preserve existing favorites. First organize and improve the requirements; let me confirm the architecture before implementation. Keep a complete progress table in English.

The current conversation acts as lead. This small project does not need another permanent chat. Before the architecture gate, it can inspect existing behavior and propose a coherent brief:

| Item | Effective brief |
| --- | --- |
| Outcome | Filter the catalog and export exactly the visible result |
| Required behavior | Keyword and tag filters combine; export uses the same visible-book set; favorites and IDs survive |
| Proposed clarification | An empty result exports headers without rows; confirm this choice with the architecture |
| Non-goals | No sync service, new account system, or favorites migration |
| Evidence | Combined filters, empty result, Unicode titles, export agreement, favorites persistence |
| Current authority | Inspect and plan; implementation waits for the user's architecture approval |
| Next result | One local end-to-end filtering and export slice |

This enriches the request without silently adopting a new feature. The lead proposes one shared `visibleBooks` result, used by the list and export adapter, rather than two interpretations of filtering.

## 2. Reconcile a supplement and permission

The user adds:

> Also support quoted book titles in the CSV. The architecture, including the empty-result behavior, is approved. Build it locally. You may use one subagent for export. Do not publish.

The lead retains filters, visible-only export, favorites, and full reporting. CSV quoting becomes another acceptance condition. Local implementation and one bounded subagent are authorized; publication is not. No second approval is needed for the unchanged plan.

## 3. Dispatch a finite task

After verifying a clean baseline and independent write boundaries, the lead handles filtering and sends this brief to the export subagent:

```text
Task: implement CSV export of the provided visibleBooks array.
Baseline: catalog-base, verified before dispatch.
Read: existing book type and CSV export tests.
Write: src/export/booksToCsv.ts and its focused tests only.
Contract: accept an ordered array of existing Book objects; export that exact
  order and set. Do not fetch, filter, mutate favorites, or change IDs.
Acceptance: correct CSV escaping, Unicode, headers-only empty input,
  no rows omitted or added. Use the existing language and test runner.
Return: candidate diff, checks with outcomes, limitations, and changed paths.
Stop/report: shared Book type or contract needs changing, or ownership conflicts.
Authority: local changes and checks only; no publishing or further delegation.
Checkpoint: return when the adapter and focused checks are ready for integration.
```

The lead does not poll every action. It works on the independent filter path and inspects the adapter when the agreed checkpoint arrives. If both tasks need the same file, one owner writes it; the other returns a proposal.

## 4. Receive evidence without overstating it

Suppose the subagent returns `export-candidate`: focused tests pass for escaping, empty input, Unicode, and order; no browser integration was performed. The lead records “adapter checked locally; integration pending,” reviews the diff, then integrates the adapter with the actual visible-books result.

Suppose a browser check at `catalog-candidate` reveals that the list uses filtered books but the export button passes the full catalog. The lead localizes the connection error and corrects that caller. It does not rewrite filtering or add another export service. It reruns the affected list-to-export path and retains unchanged adapter evidence.

## 5. Report the whole agreed result

If the following evidence were actually obtained, the report could read:

> The local filtering and export slice is ready for your review. Export now uses the same books as the visible list. The integration check caught and corrected a caller that still passed the full catalog. Nothing has been published.

| Requirement | Current state | Evidence at catalog-candidate | Remaining gap | Next action / owner |
| --- | --- | --- | --- | --- |
| Keyword and tag filtering | Local checks passed | Combined and empty-result cases; browser exercise | User acceptance | User tries the local candidate |
| Export visible books only | Integrated locally | Browser result IDs compared with CSV rows | User acceptance | Lead supplies the local candidate |
| CSV quoting and Unicode | Local checks passed | Focused adapter cases plus one integrated sample | Broader real-data coverage | Lead records future reported edge cases |
| Preserve favorites and IDs | Local regression passed | Existing IDs and favorites checked after filtering and reload | Coverage limited to exercised fixtures | Keep the compatibility condition for later changes |
| Publication | Outside current authority | No release performed | Any later release requires its own scope | No publication action |

In a real report, link actual evidence and identify the environment. Unrun checks stay unrun, regardless of what this example says.

## 6. Improve only where the evidence warrants it

The adapter contract was clear; the caller broke the integration boundary. The lead keeps one targeted end-to-end check for visible/exported agreement. It does not add a permanent second reviewer or full audit to every label change. At the next relevant batch, check whether this catches the same boundary error without excessive overhead; retain or revise the method accordingly.

Before a break, preserve the effective brief, candidate, evidence limits, owners, and next safe action in existing project records. A successor verifies that checkpoint and actual ownership before writing. Token savings remain unknown unless comparable, attributable usage was measured.
