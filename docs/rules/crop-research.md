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

## General-Crop-Only Values

OpenFarmPlanner lets a variety inherit almost every value from its general
crop, but some values cannot differ per variety at all. Research them in the
general crop note only:

- plant family, nutrient demand, and rotation break (fixed per crop species)
- good and bad neighbours (companion planting)

A variety note never sets these. If a variety source contradicts them,
document it as a source conflict or an identity question. Seed type
(open-pollinated or F1 hybrid) is the opposite case: it exists only on
varieties, needs a source that states it, and is never inferred from the
variety name.

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

Perennials are planned differently: a recurring yearly harvest period (for
example early May to mid-June for asparagus), the number of years from
planting to the first harvest, and the standing time in years. Research these
instead of forcing a perennial into growth duration and harvest window.

Sowing and planting periods depend on local climate and altitude. Record them
as regional guidance with the region or climate the source assumes, at month
or third-of-month resolution, never as day dates. OpenFarmPlanner keeps such
periods as project data and does not publish them to the crop library.

## Germination, Site And Hardiness Values

These fields use fixed choices. Map source wording explicitly:

- Light germinator (`Lichtkeimer`), dark germinator (`Dunkelkeimer`), or no
  light requirement; cold germinator (`Kaltkeimer`) or frost germinator
  (`Frostkeimer`), with stratification duration and temperature if given.
- Unknown and "none" are different. Leave a requirement open when no source
  covers it; record "none" only when a source says the crop has no such
  requirement.
- Keep one source's germination temperature range or time range intact.
  When sources disagree, document the conflict instead of averaging.
- Check consistency: a light germinator with a deep sowing depth, or a frost
  germinator sown in summer, is a source conflict to resolve or document.
- Light at the site is a list: record every condition the sources call
  suitable (full sun, partial shade, shade).
- Winter hardiness depends on climate. Name the frost limit or climate the
  source assumes, and distinguish hardy from hardy with protection.

## Pests And Diseases

Record pests and diseases as plain prose: what to watch for, which conditions
favour them, and practical prevention. Name organisms precisely where sources
allow (for example carrot fly, *Psila rosae*), and do not merge similar labels
such as different powdery mildews into one organism.

OpenFarmPlanner also has a structured plant-health catalogue. Do not link crop
notes to catalogue entries yet: researching the catalogue and its crop-host
links is a separate task (crop-data issue #8). A missing pest in a note does
not mean the crop is safe from it.

Variety resistance claims come from breeders and seed suppliers. Paraphrase
them with their exact scope (resistant, tolerant, or field-tolerant, and
against which organism or race) and do not turn tolerance into resistance.

## Companion Planting

Much traditional companion-planting advice has little research behind it.
OpenFarmPlanner therefore only warns about bad neighbours and never blocks a
plan, and the notes must make the evidence level visible:

- Each neighbour needs a source and a reason. Use the planner's reasons:
  competition for space, light, water or nutrients; inhibits the other plant;
  repels or lures away pests; improves the soil; shares pests or diseases;
  other.
- Say whether a claim rests on trials or extension research, or only on
  gardening tradition. Prefer extension services and trials over garden blogs;
  a claim found only in blogs that copy each other stays marked as tradition.
- Name each neighbour by its precise crop identity (the official crop species
  name) or by plant family. Broad groups such as "herbs" or "cabbages" cannot
  be published to the crop library; resolve them to species or a family, or
  document them as an open mapping question.
- Shared pests and diseases usually follow the plant family. Name the family
  as the neighbour unless a source says the relation is specific to one crop.
- A pair reads the same from both sides. When a note lists a neighbour that
  has its own general crop note, check that note and add the same relation or
  document the disagreement.
- Do not list the same neighbour as both good and bad. If sources disagree,
  document the conflict and leave the relation out until it is resolved.
- If sources state that a crop has no known bad neighbours, record that as a
  general statement, not as a neighbour.
- Neighbours belong to the general crop only (see "General-Crop-Only
  Values").

## Respect Field And Form Constraints

Structured live values must satisfy the strictest known constraint from the API,
UI form, and data model. If the API accepts decimals but the UI form only allows
integers, the integer rule applies for live sync.

Do not silently write derived decimal values into structured fields that expect
integers. Choose a plausible integer value, document the rounding, and keep the
mathematical derivation as an explanation only. If no plausible rounding is
possible, leave the value open and mark the case as a mapping question.

Keep ranges as ranges where the model stores them: sowing depth, germination
temperature, germination time, and stratification each have a lower and an
upper bound. Do not collapse a source range into one value for these fields.

Convert rotation-break wording explicitly. The planner counts the years
between two crops of the same family on one bed, so "every 4 years" or "a
4-year rotation" is a break of 3. Write the source wording and the converted
value in `Planning Value Derivations`.

## Content With Its Own Field

Germination, site, winter hardiness, pests and diseases, rotation, and
neighbours now have their own OpenFarmPlanner fields (see
[`docs/culture-field-mapping.md`](../culture-field-mapping.md)). Put that
information into the matching note section, not into `Notes`, so a sync can
map it to the right field. `Notes` keeps care advice and caveats that have no
field.

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
