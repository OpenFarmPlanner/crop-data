## Short Description
- Siberian kale (`Schnittkohl`, also `Sibirischer Kohl`, `Russischer Kohl`) is
  treated here as the leaf- and stem-harvested kale type of
  `Brassica napus` (Pabularia group), botanically `Brassica napus var. pabularia`.
- This note intentionally does not use the broad seed-supplier category
  `Grünkohl/Schnittkohl` as the crop identity. That category mixes two species:
  curly kale (`Grünkohl`, `Brassica oleracea var. sabellica`) and Siberian kale
  (`Schnittkohl`, `Brassica napus var. pabularia`). See `Notes` and
  `Planning Value Derivations`.
- Growth duration: strongly harvest-form dependent. Sources give roughly
  25-30 days for baby-leaf harvest, about 50-60 days for developed leaves from a
  spring sowing, and a much longer effective duration for overwintered crops.
  55 days is used as the general planning value for developed-leaf harvest
  (see `Planning Value Derivations`).

## Sowing & Planting

### Transplants
- Description: pre-cultivate for a set stand, especially for spring plantings
  and for autumn/winter crops where an even plant spacing is wanted.
- Sowing: spring sowing from about February under protection; autumn/overwinter
  sowing from about August to September.
- Outdoor planting: about 5-6 weeks after sowing, following the ReinSaat
  category guidance for this kale group.

### Direct Sowing
- Description: direct sow for cut-leaf, baby-leaf, or cut-and-come-again
  harvest.
- Sowing: from about March outdoors; late-summer sowings feed autumn and winter
  harvests.
- Sowing depth: 1-2 cm.

### Overwintering Crop
- Description: later sowings kept as smaller plants overwinter better in harsh
  sites; mulch protection helps. Harvest continues through winter in mild spells.
- Sowing: about August to September.
- Harvest: through winter into early spring, weather permitting.

- Spacing: no single general value. Cut-leaf and baby-leaf production uses close
  in-row spacing (around 10 cm) at about 50 cm row spacing; larger plants for
  repeated leaf picking use wider spacing.
- Site: sun to partial shade; moist, nutrient-rich, well-drained soil. High
  nutrient demand. Net cover against cabbage fly and caterpillars is useful.

## Harvest & Use
- Harvest young leaves and tender stems at several development stages: baby leaf
  for salads, larger leaves as a cooked vegetable.
- Suited to repeated cut-and-come-again harvest over a long window.

## Planning Value Derivations
- Crop identity: use `Schnittkohl` / `Siberian kale` (`Brassica napus var.
  pabularia`), not `Grünkohl/Schnittkohl`. The supplier category combines
  `Brassica oleracea` curly-kale varieties (for example `Rosco`,
  `Halbhoher grüner krauser`, `Nero di Toscana`, `Westlandse Winter`) with
  `Brassica napus` Siberian-kale varieties (`Winter Red`, `Russian Frills`).
  The narrower identity is chosen because the only variety currently maintained
  for this crop, `Winter Red`, is given by
  [ReinSaat](https://www.reinsaat.at/shop/DE/kohlgewaechse/gruenkohl_schnittkohl/winter_red/)
  as `Brassica napus ssp. napus var. pabularia`.
- Discarded category: `Grünkohl/Schnittkohl` is kept only as source context. If
  a curly-kale (`Brassica oleracea`) variety is added later, it needs its own
  general crop entry (`Grünkohl` / curly kale) rather than reusing this one.
- Growth duration: 55 days as an inferred planning value for developed-leaf
  harvest from a spring sowing. `Red Russian` type Siberian kale is given at
  "29 baby; 50 full size" days from direct seeding by
  [Johnny's Selected Seeds](https://www.johnnyseeds.com/vegetables/kale/red-russian-kale-seed-363.html),
  about 50-60 days to full size by
  [RHS](https://www.rhs.org.uk/plants/173056/brassica-napus-pabularia-group-red-russian/details)
  and [Gardener's Path](https://gardenerspath.com/plants/vegetables/grow-red-russian-kale/),
  with baby leaf around 25-30 days. 55 days is the whole-day midpoint of the
  developed-leaf range, documented as inferred, not a direct source value.
  Baby-leaf (about 30 days) and overwintered crops deviate strongly; the
  OpenFarmPlanner publish form nonetheless requires one mandatory value.
- Harvest window: 120 days as a planning value for a long cut-and-come-again
  winter harvest. The
  [ReinSaat category](https://www.reinsaat.at/shop/DE/kohlgewaechse/gruenkohl_schnittkohl/)
  gives a November-to-March harvest range for this kale group; 120 days is a
  conservative selection inside that range for repeated leaf picking.
- Yield: 1.5 kg/m² as a conservative planning value. This is borrowed from the
  curly-kale figures at
  [Open Organic Farm](https://openorganic.farm/plants/30) (organic average about
  1.40 kg/m², conventional close to 2 kg/m²), because no Siberian-kale-specific
  yield source was found. Kept in kg/m² (`per_sqm`) for table comparability;
  flagged as uncertain and species-transferred.
- Thousand kernel weight: 3-4 g for the supplier category; `Winter Red` seed is
  lighter at about 2.86 g.

## Sources
- [ReinSaat - Grünkohl/Schnittkohl category](https://www.reinsaat.at/shop/DE/kohlgewaechse/gruenkohl_schnittkohl/)
- [ReinSaat - Winter Red](https://www.reinsaat.at/shop/DE/kohlgewaechse/gruenkohl_schnittkohl/winter_red/)
- [RHS - Brassica napus (Pabularia Group) 'Red Russian'](https://www.rhs.org.uk/plants/173056/brassica-napus-pabularia-group-red-russian/details)
- [NC State Extension - Brassica napus Pabularia Group](https://plants.ces.ncsu.edu/plants/brassica-napus-pabularia-group/)
- [Gardener's Path - Red Russian kale](https://gardenerspath.com/plants/vegetables/grow-red-russian-kale/)
- [Open Organic Farm - Grünkohl](https://openorganic.farm/plants/30)

## Research Status
- Researched on: 2026-09-04
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: growth duration varies strongly by harvest form
  (baby leaf vs developed leaf vs overwintered); this is a harvest-logic
  spread, not a botanical conflict.
- Synced on 2026-09-04 to the live `Zwiebelzopf` project on `openfarmplanner.org`
  (records for the general crop and for `Winter Red`): `name` changed from
  `Grünkohl/Schnittkohl` to `Schnittkohl`, growth duration set to 55 days,
  German cultivation notes updated. A curly-kale (`Brassica oleracea`) variety
  is not planned under this crop; if added later it needs its own `Grünkohl`
  crop entry.
- Open mapping questions:
  - The `crop_display_language_code` (`de`) and the German/English
    `crop_species_translations` could not be written through the sync token;
    they appear to derive from the linked official crop species, which is not
    set. Needs the OpenFarmPlanner publish/crop-species step in the UI.
  - Yield (1.5 kg/m²) is species-transferred from curly kale and should be
    replaced when a Siberian-kale-specific source is found.
- Public-readiness: identity and calendar values researched and synced; yield
  and the crop-species link still need review.
