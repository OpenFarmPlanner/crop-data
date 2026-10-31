# Crop Research Rules

Read this before researching or editing a general crop note or a variety note
in `notes/` (Phase 1), and before preparing values for a private sync. The
always-on rules in [`CLAUDE.md`](../../CLAUDE.md) apply as well; the note
structure is [`templates/crop-note.md`](../../templates/crop-note.md).

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
