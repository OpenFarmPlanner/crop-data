## Short Description
- Swiss chard (`Mangold`) is `Beta vulgaris` subsp. `vulgaris` (leaf/petiole
  group), grown either as leaf/cut chard (`Schnittmangold`, repeated
  cut-and-come-again leaf harvest) or as stalk chard (`Stielmangold`,
  grown for its thickened petioles, harvested later and less repeatedly).
  Both forms are covered by this note; see `Notes` for why they are not
  split into separate Kultur entries here.
- Moderate to high nutrient demand; needs a sheltered, sunny to partially
  shaded site with humus- and nutrient-rich soil, pH about 6.4-7.2.
- Growth duration: left open as a general value because it differs strongly
  between the cut-leaf and stalk forms and their harvest logic. See
  `Planning Value Derivations`.

## Sowing & Planting

### Direct Sowing
- Description: direct sow outdoors; stalk chard (`Stielmangold`) is
  typically sown about 4 weeks earlier than leaf chard (`Blattmangold`/
  `Schnittmangold`) because it needs a longer season before its stalk
  harvest.
- Sowing: April to June.
- Sowing depth: not reviewed in this research pass; left open.

- Spacing: leaf/cut chard about 25-35 cm between rows x 35 cm within the
  row; stalk chard wider, about 45 x 35 cm, up to a maximum of about 8
  plants/m². For broad leaves and thick stalks generally, at least 40 cm
  spacing is recommended.
- Site: sun to partial shade, sheltered; humus- and nutrient-rich soil, pH
  about 6.4-7.2.

## Harvest & Use
- Leaf/cut chard is harvested repeatedly by cutting outer leaves or a third
  of the leaf mass, leaving the heart to regrow. Stalk chard is harvested
  later, typically as whole mature stalks with attached leaves.

## Notes
- Germination takes about 4-10 days at 14-18 °C soil temperature.
- The leaf/cut vs. stalk distinction is treated here as an internal type
  note rather than a Kultur split, matching how the task's assigned crop
  name `Mangold` is used; this must be revisited explicitly if
  OpenFarmPlanner needs separate calendar values per type, since a single
  general growth-duration or harvest-window figure would otherwise be
  falsely precise.

## Planning Value Derivations
- Growth duration: left open as a single general value; leaf/cut chard is
  harvested repeatedly over an extended period starting relatively early,
  while stalk chard needs a longer, single-harvest-oriented season. No
  general source reviewed here separates these into distinct day counts.
- Harvest window: left open for the same reason; leaf/cut chard has a long,
  repeated harvest window in principle, while stalk chard's harvest window
  is comparatively short and concentrated.
- Yield: left open; no general source reviewed here gives a reliable kg/m²
  figure.
- Thousand kernel weight: left open; not reviewed in this research pass.

## Sources
- [Gartenberatung - Kultur- und Anzuchtdaten Mangold](https://www.gartenberatung.de/gemuese/blattgemuese/Kultur-Anzuchtdaten-Mangold.htm)
- [Plantura - Mangold anbauen](https://www.plantura.garden/gemuese/mangold/mangold-anbauen)
- [Kiepenkerl - Mangold Kulturanleitung](https://www.kiepenkerl.de/kulturanleitungen/mangold/)

## Research Status
- Researched on: 2026-09-18
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: none found on the type split itself; sources agree
  leaf/cut and stalk chard differ in sowing timing and spacing.
- Open mapping questions: whether OpenFarmPlanner should model leaf/cut
  chard and stalk chard as separate Kultur entries is an open question,
  documented explicitly rather than silently decided; sowing depth, growth
  duration, harvest window, yield, and thousand kernel weight are all open.
- Public-readiness: needs review; type-split question and calendar/yield
  values are open.
