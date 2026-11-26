## Short Description
- Variety traits or crop-specific characteristics
- Botanical name: *Genus species* (subspecies/variety/group if relevant)
- Life cycle: annual/biennial/perennial (for biennials grown as annuals, say
  so); perennials: standing time of about X years
- Seed type: open-pollinated/F1 hybrid *(variety notes only, and only when a
  source states it; never inferred from the name)*
- Soil and site requirements
- Growth duration: X-Y days

## Sowing & Planting

### Transplants
- Description: plain-language cultivation guidance
- Sowing: month range, with the region or climate the source assumes
- Outdoor planting: X-Y weeks after sowing

### Direct Sowing
- Description: plain-language cultivation guidance
- Sowing: month range, with the region or climate the source assumes
- Sowing depth: X-Y cm

### Overwintering Crop
- Description: plain-language cultivation guidance
- Sowing: month range, with the region or climate the source assumes
- Move to cold frame/greenhouse: timing
- Harvest: timing

*(Remove cultivation variants that do not apply. Do not leave empty sections.)*

- Spacing: X cm between rows; Y cm within the row
- Canopy diameter: X cm *(only for individually placed plants such as
  perennials or large fruiting crops)*

## Germination
- Optimal germination temperature: X-Y °C; minimum: Z °C
- Germination time: X-Y days
- Temperature requirement: none/cold germinator/frost germinator; for cold or
  frost germinators: stratification X-Y days at A-B °C
- Light requirement: none/light germinator/dark germinator
- Pretreatment: soaking, scarifying, or none

*(Leave a line out when no source covers it. "None" is a statement and needs a
source, just like a positive requirement.)*

## Site & Plant Health
- Light: full sun/partial shade/shade (all that the sources call suitable)
- Water need: low/medium/high
- Soil: soil type, pH, structure
- Winter hardiness: hardy/hardy with protection/not hardy, with the frost
  limit or climate the source assumes
- Pests and diseases: what to watch for, and practical prevention

## Crop Rotation

*(General crop notes only. A variety always uses its general crop's values.)*

- Plant family: botanical family name (for example Brassicaceae)
- Nutrient demand: low/medium/high
- Rotation break: X years between two crops of this family on the same bed
  (state the source wording if it was converted, for example "every 4 years"
  is a break of 3)

## Companion Planting

*(General crop notes only. A variety note says that it uses the general crop's
neighbours and records only a variety-specific source that contradicts them.)*

Good neighbours:
- Neighbour (crop or plant family): reason; evidence and source

Bad neighbours:
- Neighbour (crop or plant family): reason; evidence and source

Reasons: competition for space, light, water or nutrients; inhibits the other
plant; repels or lures away pests; improves the soil; shares pests or
diseases; other. Name each neighbour by its precise crop identity or plant
family, not by a broad group. Say whether a claim rests on trials or only on
gardening tradition. If sources state that no bad neighbours are known, write
that as a general statement instead of a list entry.

*(Remove the section if no source covers neighbours, and note the gap in
`Research Status`.)*

## Harvest & Use
- Harvest timing or harvest criterion
- Perennials: recurring harvest period (for example early May to mid-June) and
  years from planting to the first harvest
- Usual harvest unit: kg, pieces, or bunches; average piece or bunch weight
  when a source gives one
- Use

## Notes
- Care and special caveats that have no section above

## Comparison With General Crop Data

*(Only for variety notes. Remove this section for general crop notes.)*

Before writing a variety note, a matching general crop note must exist. If it is
missing, create and research the general crop note first.

Use short prose or a few bullets:
- Which variety values differ from the general crop?
- Which values were intentionally reused from the general crop because no
  variety-specific source was found?
- For reused general planning values, explicitly name the general value, the
  variety value, the reason, and that no contradicting variety-specific source
  was found.
- Check especially: growth duration, harvest window, yield, piece weight, seed
  requirement, spacing, sowing depth, germination, winter hardiness, and
  pests or diseases (for example a stated resistance).
- Plant family, nutrient demand, rotation break, and neighbours always come
  from the general crop. If a variety source contradicts them, document it as
  a source conflict, not as a variety value.
- Document every reuse or deviation. Do not silently treat the variety as equal
  to the general crop.

## Planning Value Derivations

*(Use only when a recommended or synced planning value is not directly copied as
a single value from one source. Remove this section if no derived values exist.)*

Use short prose or a few bullets:
- Value: X days/cm/kg/m²
- Source basis: which source gives which range or criterion?
- Derivation: how was the planning value calculated or selected?
- Reuse: if a general crop value was reused for a variety, say so explicitly.
- Field/form constraint: does the stored value need to be an integer or use a
  fixed unit?
- Safety buffer: if a seed safety buffer is used, document it separately from
  the source-backed base requirement.
- Uncertainty: which cultivation situation does the value fit, and where can it
  differ?

Use readable field labels such as "growth duration", "harvest window", "sowing
depth", or "seed requirement". Do not use technical API field names in this
section.

## Sources
- [Source 1](url)
- [Source 2](url)

Write source names in flowing text as direct Markdown links, for example
`[Source 1](url)`. Do not use footnote markers such as `[^source-1]`.

## Research Status
- Researched on: YYYY-MM-DD
- General crop note exists: yes/no/not applicable
- Sections not yet researched: for example germination, companion planting
- Open source conflicts: concrete conflicts between sources, if any
- Open mapping questions: unclear OpenFarmPlanner field mapping, if any
- Public-readiness: ready / needs review / blocked
