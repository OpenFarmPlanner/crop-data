## Short Description
- Mustard greens (`Blattsenf`) are treated here as leaf-harvested forms of
  `Brassica juncea`.
- This note intentionally does not use broad shop categories such as Asian leaf
  vegetables or mixed mustard-cabbage labels as the crop identity.
- Growth duration: no single true general value, because sources describe fast
  baby-leaf harvests and longer winter harvests and varieties differ in harvest
  form and season. An inferred planning value of 50 days is stored for a
  developed-leaf harvest so the crop can be published (see
  `Planning Value Derivations`).

## Sowing & Planting

### Direct Sowing
- Description: direct sow for loose leaves, baby leaf, or rosette harvest,
  depending on variety and spacing.
- Sowing: source ranges include protected late winter or early spring sowing
  and late summer to early autumn sowing; use local frost protection and variety
  guidance before setting calendar dates.
- Sowing depth: 1-2 cm where source-backed for `Green in Snow`.

### Transplants
- Description: transplanting can be relevant for protected autumn and winter
  crops, but general transplant timing should remain open until researched with
  more mustard-greens-specific sources.
- Sowing: open
- Outdoor planting: open

- Spacing: open as a general value. Sources for `Green in Snow` range from
  dense row spacing for cut leaves to wider plant spacing for rosette harvest.
- Site: sunny to partially shaded; moist, nutrient-rich soil is supported by
  the `Green in Snow` supplier sources.

## Harvest & Use
- Harvest leaves young for salads or as a cooked leafy vegetable, depending on
  variety and pungency.
- Some mustard greens can be harvested leaf-by-leaf, as cut leaves, or as whole
  rosettes; this harvest logic must be checked per variety before assigning
  structured yield or harvest-window values.

## Notes
- The ReinSaat Asian greens category is useful context for sowing and harvest
  ranges, but it explicitly combines `Brassica juncea` and `Brassica rapa`.
  That makes it too broad to use as a crop identity for all listed products.
- For `Green in Snow`, the direct product sources support mapping to mustard
  greens because [ReinSaat - Green in Snow](https://www.reinsaat.at/shop/EN/salate/asiasalate/gruen_im_schnee/)
  gives `Brassica juncea var. multiceps`, while
  [Hof Jeebel - Green in Snow](https://biogartenversand.de/biosaatgut/blattgemuese/blattgemuese-gruen-im-schnee)
  and [Naturgarten-Samen - Blattsenf Green in Snow](https://naturgarten-samen.de/produkt/blattsenf-gruen-im-schnee-50-korn/)
  give `Brassica juncea`.

## Planning Value Derivations
- Crop identity: use `Mustard greens` rather than `Asian leaf vegetables` or
  `Asian leaf vegetables/mustard cabbage`. The broad category source combines
  `Brassica juncea` with `Brassica rapa`, and its product list includes leaf,
  rosette, and stem-oriented crops. The narrower crop identity is supported by
  the `Green in Snow` botanical names from the product sources.
- Growth duration: no single true general planning value. ReinSaat's broad
  Asian greens category gives a short warm-season harvest range and a longer
  winter range, and that category mixes species and harvest forms. For the
  OpenFarmPlanner publish form, which requires a value, 50 days is stored as an
  inferred planning value for a developed-leaf harvest from a spring or
  late-summer sowing. This is consistent with the `Green in Snow` variety
  record (45 days) and with general `Brassica juncea` leaf-harvest timing of
  roughly 40-60 days. Documented as inferred, not a direct source value;
  baby-leaf (about 3 weeks) and overwintered crops deviate strongly.
- Harvest window: 90 days as an inferred planning value for a long
  cut-and-come-again harvest, matching the `Green in Snow` variety record.
- Spacing: no single general planning value. Dense baby-leaf spacing, row
  sowing, broadcast sowing, and wider rosette spacing all appear in the source
  set.

## Sources
- [ReinSaat - Green in Snow](https://www.reinsaat.at/shop/EN/salate/asiasalate/gruen_im_schnee/)
- [ReinSaat - Asian greens category](https://www.reinsaat.at/shop/DE/salate/asiasalate/)
- [Hof Jeebel - Green in Snow](https://biogartenversand.de/biosaatgut/blattgemuese/blattgemuese-gruen-im-schnee)
- [Naturgarten-Samen - Blattsenf Green in Snow](https://naturgarten-samen.de/produkt/blattsenf-gruen-im-schnee-50-korn/)

## Research Status
- Researched on: 2026-09-03
- General crop note exists: not applicable
- Open source conflicts: no conflict on `Green in Snow` belonging to
  `Brassica juncea`; broad category sources remain mixed and should not define
  the crop identity.
- Synced 2026-09-04 to the live `Zwiebelzopf` project on `openfarmplanner.org`:
  `growth_duration_days` set to 50 and `harvest_duration_days` set to 90 (both
  were empty; growth duration blocked publishing).
- Open mapping questions: the stored growth duration and harvest window are
  inferred; spacing and yield still need more mustard-greens-specific sources.
- Public-readiness: identity mapped; calendar values inferred and synced,
  spacing and yield need review.
