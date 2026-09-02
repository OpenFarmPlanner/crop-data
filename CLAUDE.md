# OpenFarmPlanner Crop Data

## Purpose

This public repository is the primary workspace for researching and documenting
reusable crop data for OpenFarmPlanner. It is not a live database and must not
contain private OpenFarmPlanner project details.

## Public-First Rule

Everything committed here must be safe for a public repository:

- no API tokens or secrets
- no private project names or project IDs
- no production IDs
- no private live-sync reports
- no personal operational notes

Keep private sync work in an ignored local directory or a separate private
repository.

## Two-Phase Workflow

- Phase 1: research, source review, and public notes in this repository.
- Phase 2: optional private sync into an OpenFarmPlanner project using
  `PHASE2_PROMPT.md` or project-specific tooling outside this public repo.

Do not write to a live API during Phase 1.

Do not create a parallel private research note when the information is reusable.
Research improvements belong here first. Private files are only for credentials,
temporary sync logs, project-specific IDs, or information that cannot be made
public safely.

## Language

All public content is English by default:

- documentation
- templates
- crop notes
- examples
- commit messages

Localized crop names may be included in parentheses when helpful.

## Copyright And Source Style

Do not copy source text verbatim or preserve promotional source wording. Facts,
numbers, and variety characteristics must be paraphrased in plain, neutral
language.

When a source is mentioned in flowing text, write the source name as a direct
Markdown link, for example:
`[ReinSaat](https://example.org/source)`.

Do not use footnote markers for source references. Avoid bare source names when
the reader may not know whether the name refers to a person, company, or
publication.

## Explicit, Not Silent

Source conflicts, identity questions, duplicate suspects, and mapping questions
must always be documented explicitly in the note. Do not make a silent choice
when the correct source, crop identity, or OpenFarmPlanner field is unclear.

## Compare Varieties Explicitly

General crop data and variety data must never be silently treated as the same,
even if only one variety exists. Each variety is researched independently and
explicitly compared with the general crop values.

Variety-specific deviations must be justified with variety-specific sources.
Intentional matches must also be documented, for example:
`no reliable variety-specific yield source found; the general crop planning value was intentionally reused`.

## Always Carry General Crop Data

Every variety note must have a corresponding general crop note. If it is
missing, create or research the general crop note first.

A variety must not remain the only maintained data record for a crop. The
general crop note must contain reliable general facts, known source ranges, and
open uncertainties. If a structured general value would be falsely precise
because varieties, crop cycles, harvest methods, or overwintering logic differ
strongly, leave the value open and document the reason.

If the crop identity itself is unclear, do not create a silent general crop
entry. Document the case as an identity or mapping question.

## Intentional General Planning Values

If no reliable variety-specific value is found but a reliable general crop
planning value exists, first verify and maintain the general crop value. The
variety may then intentionally reuse that value if it fits botanically and no
variety-specific source contradicts it.

Document the reuse in:

- `Comparison With General Crop Data`
- `Planning Value Derivations`, when applicable
- `Research Status`
- live notes during any private sync, when useful to users

Do not present a reused general value as a variety-specific source claim.

If neither a reliable general value nor a variety-specific value exists, leave
the value open and mark it as an open research or mapping question.

## Keep Yield Units Consistent Per Crop

Within one crop, use the same yield unit for the general crop and its varieties
whenever possible. This keeps OpenFarmPlanner tables comparable.

Preferred rule:

- If the general crop uses kg/m², varieties should also use kg/m².
- If a reliable variety source gives head weight, piece weight, or kg/plant,
  convert it to kg/m² using the documented spacing or plant density.
- Document the source value, calculation, rounding, and uncertainty in
  `Planning Value Derivations`.
- If the per-plant value is only an old project value or otherwise not
  source-backed, do not convert it into a falsely precise kg/m² value. Reuse a
  reliable general crop planning value instead and document that reuse.
- Keep a different yield unit only when the crop's harvest logic truly needs
  it. Mark unclear cases as mapping questions.

## Model Calendar Values Deliberately

General crop records must not contain falsely precise calendar values when
varieties, crop cycles, harvest forms, or overwintering logic differ strongly.
In those cases, leave values such as growth duration or harvest window open and
document the source ranges.

Variety records should contain concrete growth duration and harvest window
values whenever possible, because the crop calendar needs them. If a value can
only be inferred from wording such as "ongoing", "several weeks", or a source
range, the inferred planning value may be used only when the source basis,
derivation, and uncertainty are documented. Never present an inferred planning
value as a direct source value.

## Respect Field And Form Constraints

Structured live values must satisfy the strictest known constraint from the API,
UI form, and data model. If the API accepts decimals but the UI form only allows
integers, the integer rule applies for live sync.

Do not silently write derived decimal values into structured fields that expect
integers. Choose a plausible integer value, document the rounding, and keep the
mathematical derivation as an explanation only. If no plausible rounding is
possible, leave the value open and mark the case as a mapping question.

## Live Notes With Sources

If notes from this repository are copied into a live OpenFarmPlanner instance,
the live-visible notes may include traceable sources, practical additional
information, and derivations of planning values when useful to users.

Allowed in live notes:

- practical cultivation guidance
- short source lists
- concise explanations for inferred planning values
- relevant crop-specific caveats

Not allowed in live notes:

- private sync status
- production IDs
- API jargon
- token or project details
- raw copied shop text such as prices, delivery dates, or availability text

## Commits

Use English commit messages. Keep commits focused by crop, research session, or
workflow change.
