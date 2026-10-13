# Contributing

Keep the full project method coherent while making everyday use cheaper. Prefer a focused correction over another universal rule. English is canonical; keep the Chinese overview aligned when public usage changes.

## Report an issue

Include the skill version or commit, relevant role and project stage, a sanitized request, expected decision, observed decision, and impact. Say which parts were simulated and which occurred in a real project. Omit credentials, private transcripts, customer documents, and identifying paths. Do not attach sensitive evidence to a public issue; describe the symptom without exposing it.

## Propose a change

1. Identify the decision or usability problem. Check whether an existing reference already owns that guidance.
2. Make the smallest coherent change. Preserve explicit user gates, existing authorization, cumulative requirements, shared ownership, and evidence limits. Retire redundant wording instead of copying it elsewhere.
3. Run `python scripts/check_package.py` with Python 3.10 or newer. It has no third-party dependencies and writes no files. It validates this repository's narrow metadata conventions, not arbitrary YAML or every Agent Skills feature.
4. For a behavioral rule change, exercise the affected scenario from [the evaluation set](evaluations/SCENARIOS.md), or add a concrete new scenario. Give a fresh evaluator only the request, candidate skill, and necessary raw artifacts; keep the scoring rubric out of its input. Do not run real migrations, message people, or publish as part of a simulation.
5. Record the candidate, input scope, observed response, finding, correction, and any targeted retest. Identify author review versus independent evaluation. Pure editorial changes need proportionate inspection, not a full scenario rerun.
6. Update [validation](VALIDATION.md) and [release notes](CHANGELOG.md) without turning historical results into current passes. In a pull request, explain the problem, resulting behavior, validation, and remaining limits.

## Release and installation checks

Tie a release to an exact commit and version tag. Check metadata, documentation, license copies, links, and the final diff. Test discovery and installation in an isolated directory without an existing copy; compare installed files with the intended version. Check actual client loading separately when available. Keep local customizations recoverable when updating an existing installation.

Do not publish test logs containing private machine details. Do not advertise a directory listing, security badge, or performance gain without a verifiable source and reviewed version. MIT licensing is not certification. External community messages or paid services require their own authorization.

## Learn from real use

Use a small existing project log: version, task and acceptance scope, participants, actual completion boundary, omitted requirements, avoidable rework, review waiting, and evidence coverage. Separate user-requested scope changes from failures. If attributable token receipts exist, count distinct calls across contributors without duplicating aggregate usage; otherwise record token use as unknown. Compare sufficiently similar tasks before making causal or percentage claims. Remove process that adds cost without addressing an observed problem.
