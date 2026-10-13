# Validation record

Version 0.2.1 · 2026-10-14.

This patch shortens the entrypoint, adds role-aware entry, and improves installation, examples, and maintainability. It preserves the full operating model. The records below distinguish new checks from historical evidence.

## Version 0.2.1 checks

| Check | Result | Scope and limit |
| --- | --- | --- |
| Behavioral exercises M–O | Independent evaluator completed all three using only the candidate skill and raw scenario inputs | Read entrypoint, task routing, and recovery; no live actions or full-suite rerun |
| Observed decisions | Kept reviewer ownership, accumulated the keyboard requirement, proceeded after existing approval, verified succession, held migration-dependent release, preserved independent work | Written decisions, not product acceptance |
| Package checks | Passed public checker, skill-creator quick_validate, and whitespace check | Narrow package conventions; no security certification |
| Checker challenge | Clean candidate accepted; seven isolated defects rejected | Missing link target, outside-root link, unclosed fence, license drift, private path, misplaced metadata version, and stale current-version declaration; not exhaustive parser testing |
| Bounded editorial review | Independent reviewer read both overviews, walkthrough, contribution guide, and checker; two checker weaknesses corrected and exercised by the author | No new architecture review; targeted negative cases verify the corrections, not a full independent re-review |
| Installation | Skills CLI 1.7.2 installed public 0.2.0 and local 0.2.1 in separate clean project directories; all 13 candidate skill files matched source hashes; CLI listed the installed skill for Codex | Windows, project scope, copy mode, noninteractive confirmation; public 0.2.1 download not yet exercised |
| Client loading | Not independently exercised through fresh desktop discovery | Reading the skill explicitly in an evaluator is not proof of automatic client discovery |
| Existing local installation | Verified all 13 previous files against the saved 0.2.0 fingerprint, preserved a backup, previewed the update, then verified all 13 updated files against 0.2.1 source | File-level installation integrity; does not claim a newly opened desktop session loaded it |
| Real project efficiency | Not measured | No percentage savings or reliability guarantee |

The new public `scripts/check_package.py` is a standard-library, read-only convention checker. It does not parse arbitrary YAML, verify remote links or Markdown heading anchors, execute behavioral scenarios, or certify security. External directory and security-review status must be verified separately.

Installation tests disabled CLI telemetry and npm lifecycle scripts. An initial Git HTTPS failure came from the test machine's certificate-file configuration; a process-scoped Windows certificate backend resolved it with TLS verification still enabled. This is environment recovery, not a skill behavior fix. No global Git configuration was changed.

The entrypoint decreased from 2,142 to 1,132 whitespace-separated words. The full operating model remains available on demand. Word-count reduction is not a measured token or project-cost reduction.

## Historical release: 0.2.0

This release expands the skill into a complete project operating model: a beginner-facing explanation of the integration lead, planning at project/batch/task level, continuous delivery, request routing, reporting and cost, and improvement and continuity. English is the canonical rule set; the Chinese README is an overview.

## Version 0.2.0 checks

| Check | Result | Scope and limit |
| --- | --- | --- |
| Skill format | Revised skill passed skill-creator quick_validate | Metadata and entrypoint checks, not behavioral reliability |
| Package integrity | Revised candidate passed relative-link, code-fence, metadata, language, bounded sensitive-marker, and whitespace checks | Pattern scanning is not a comprehensive security audit |
| Editorial and architecture review | Separate evaluator reviewed five documents, then rechecked targeted corrections | Retained architecture; clarified approval scope, planning outputs, conditional improvement, acceptance wording, terminology, and duplicated continuation guidance |
| Behavioral exercises | Fresh evaluator completed J, K, and L without the rubric or author discussion; three affected cases received a post-correction recheck | Written coordination decisions only; no real migration, dispatch, release, or background monitoring |
| Installed copy | Previous version verified unchanged; update preview completed; all 13 installed files match source by SHA-256; installed entrypoint passed quick_validate | Local installation only, not testing in every compatible client |
| Long-term project results | Not measured | No demonstrated token-saving percentage, reliability rate, or comparative efficiency claim |

The raw responses and file fingerprints are retained locally. Public scenarios and criteria are in [SCENARIOS.md](evaluations/SCENARIOS.md); private paths and project records are not published. Editorial review, simulated decisions, package checks, and real project acceptance are different evidence layers.

## Observed behavior in version 0.2

| Exercise | Observed decision | What it does not prove |
| --- | --- | --- |
| J: novice project and later approval | Explained the lead plainly, used one conversation, proposed supporting requirements without silently adopting them, honored requested gates, and proceeded conditionally after explicit execution authority without inventing the missing approved design | No planner was implemented, and no actual user approval occurred |
| K: changed contract and unknown migration | Kept old candidates but qualified affected evidence, retained all requirements in a Chinese cumulative table, separated visual/text and mock/live evidence, held dependent release work, and allowed an independent local fix | No candidate, service binding, migration outcome, or real fix was verified |
| L: integration backlog and planned departure | Selected the two needed candidates, reused existing owners, bounded review, preserved other work, and prepared continuity before departure without opening unauthorized chats | No work was dispatched or handed off; savings were not measured |

The behavioral evaluator read the entrypoint and six references in full: operating model, task routing, reporting, recovery, lead practice, and ownership/review. The initial exercise did not cover every reference. It identified three local wording risks: incomplete batch closure, succession authority, and the exploration row's treatment of an understanding-first gate. After correction, a bounded recheck also consulted the relevant lifecycle passages and confirmed that incomplete closure keeps dependent delivery blocked, existing succession authority avoids renewed approval, and requested architecture writing does not invent another confirmation gate.

The editorial evaluator inspected the README and four core documents. Targeted rechecking closed the substantive findings; one final README example was then clarified by the author, with the corresponding Chinese overview wording aligned. This was a local wording correction, not another full independent review. The older A-I exercises below were not all rerun for this release.

## Historical checks: versions 0.1.0 and 0.1.1

Recorded on 2026-10-13. These results describe earlier candidates and are not counted as a complete rerun of version 0.2.0.

| Check | Result | Scope and limit |
| --- | --- | --- |
| Skill format | Passed skill-creator quick_validate for the initial package and English revision | Metadata and entrypoint, not behavioral reliability |
| Local references and interface metadata | Relative links, code fences, skill name, and invocation prompt passed in the English revision | No claim of installation testing in every client |
| Public content | File review, bounded sensitive-marker scan, and canonical-language check passed | Chinese overview is intentionally separate; pattern scanning is not a comprehensive security audit |
| Independent exercises | Two evaluators without the author's discussion completed six initial scenarios | Not external human certification; no real migrations or background operations |
| Bounded correction review | Ten concrete ambiguities were corrected and rechecked, with one additional scenario per evaluator | No remaining definite finding within that scope; not proof of universal correctness |
| Requirement reconciliation | A fresh evaluator completed one exercise using only the English entrypoint | Preserved effective requirements, handled a narrow exception, and produced a coherent Chinese report; no product work occurred |
| Long-term project outcomes | Not measured | No claim of token savings, zero rework, or an efficiency ranking |

See [SCENARIOS.md](evaluations/SCENARIOS.md) for inputs and criteria. Raw evaluation files contain local execution paths and are not published verbatim. The method and observed outcomes are summarized below.

## Observed decisions

| Scenario | Observed behavior in the initial exercises |
| --- | --- |
| A Small edit | Direct edit; no new agents, state files, or ceremonial tests |
| B Ownership conflict | No takeover from a stale note; preserved differences and continued independent investigation |
| C Pause with unknown migration | Separate acknowledgment and scheduler state; no migration replay or invented pause confirmation |
| D Cumulative report | All requirements visible; visual/extracted, mock/live, test environment/user acceptance kept distinct |
| E Repeated failed patch | Stopped the third retry layer; investigated charging ownership without a login rewrite or new database |
| F Missing monitoring tools | Continued authorized local work without inventing background monitoring |
| G Authorized succession | Effective revocation and recovery evidence permitted transfer; unknown historical authorship was preserved |
| H Specification and retry | Adopted specification remained effective; unmet criteria blocked completion; requestId alone did not justify retry |
| I Current brief (English revision) | Kept PDF images, data identities, offline reading, existing panel, and full Chinese reporting; retained sentence translation while deferring paragraphs; did not invent implementation evidence or open a new chat |

Corrections addressed lost-owner recovery, unavailable status queries, small-task exemptions, concise parking messages, conditional resumption, compound acceptance, complete-report preferences, idempotency semantics, evidence metadata, and the scope of adopted specifications.

English publication preserves one canonical rule set. User-facing responses follow the user's language; the Chinese README is an overview only. Six operational references were translated in two bounded assignments and reviewed by the integration lead; the entrypoint, public overview, sources, and evaluation documents were also reviewed. The English entrypoint received the targeted requirement-reconciliation exercise above. The same evaluator then reviewed two added paragraphs about improving a proposed method within existing authorization and constraints, finding no new concrete ambiguity within that scope. The eight earlier exercises evaluated the preceding Chinese version; they were not all rerun after translation.

This is an initial usable rules package. Improve it from observed failures and retest affected scenarios. Publication or directory listing is distinct from independent security or quality certification.
