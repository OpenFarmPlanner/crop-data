## Short Description
- Swiss chard (`Mangold`) is `Beta vulgaris` subsp. `vulgaris` (leaf/petiole
  group), grown either as leaf/cut chard (`Schnittmangold`, repeated
  cut-and-come-again leaf harvest) or as stalk chard (`Stielmangold`,
  grown for its thickened petioles, harvested later and less repeatedly).
  Both forms are covered by this note; see `Notes` for why they are not
  split into separate Kultur entries here.
- Medium nutrient demand (Mittelzehrer); needs a sheltered, sunny to partially
  shaded site with humus- and nutrient-rich soil, pH about 6.4-7.2.
- Growth duration: 63 days from direct sowing to the first cut as a general
  planning value (leaf chard about 8-10 weeks, stalk chard about 10-12 weeks
  in the sources); see `Planning Value Derivations`.
- Harvest window: 120 days, the cutting period of one planting (repeated
  cuts until frost).
- Propagation duration: not applicable; direct sown.
- Expected yield: 4.0 kg/m² for the cut/leaf-chard harvest form, as an
  uncertain general planning value (see `Planning Value Derivations`).

## Sowing & Planting

### Direct Sowing
- Description: direct sow outdoors; stalk chard (`Stielmangold`) is
  typically sown about 4 weeks earlier than leaf chard (`Blattmangold`/
  `Schnittmangold`) because it needs a longer season before its stalk
  harvest.
- Sowing: April to June.
- Sowing depth: about 2-3 cm (2.5 cm as a planning value); see `Planning
  Value Derivations`.

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
- Definitions: growth duration counts from direct sowing to the first cut;
  harvest window is the cutting period (repeated cuts), not a single harvest.
  Both are inferred planning values.
- Growth duration: 63 days (9 weeks). A search summary of garden sources
  ([Plantura](https://www.plantura.garden/gemuese/mangold/mangold-ernten),
  [Kiepenkerl](https://www.kiepenkerl.de/kulturanleitungen/mangold/),
  [meine-ernte](https://www.meine-ernte.de/pflanzen-a-z/gemuese/mangold/))
  gives 8-10 weeks (56-70 days) for leaf chard (some give 30-40 days for
  early small leaves) and 10-12 weeks (70-84 days) for stalk chard, with
  stalk harvest starting 50-60 days after sowing when stalks reach 20-25 cm.
  63 days is the middle of the leaf-chard range and is chosen because the
  general crop is used mainly as a cut crop. Stalk chard fits about 10-20 days
  later.
- Harvest window: 120 days. The chard season runs from mid-June until the
  first autumn frost, about mid-June to mid-October (about 120 days), and
  both forms regrow after cutting. Stalk chard is often harvested over a
  shorter period, and sowings in late June give a shorter window. Inferred
  from the season length; no source gives a per-planting day count.
- Propagation duration: left empty; chard is direct sown here. Pre-cultivation
  from mid-February (planting from mid-April) is possible but was not used as
  the general case.
- Field/form constraint: whole integer days.
- Yield: 4.0 kg/m², an uncertain general planning value for the leaf/cut
  chard harvest form. Source basis: no LfL/Hortipendium/KTBL commercial
  yield table was found (Hortipendium's "Mangold Erwerbsanbau" page gives
  spacing and seed-rate data but no yield); search-engine summaries of garden
  and small-scale cultivation sources give figures from about 3 kg/m² to
  5-6 kg/m² depending on variety and source. Derivation: 4.0 kg/m² is the
  rounded middle of the commonly cited 3-6 kg/m² range. This is documented as
  uncertain because it comes from search-engine summaries of garden sources
  rather than a single authoritative commercial-trial figure, and because
  stalk chard (`Stielmangold`) likely yields differently (heavier per-plant
  weight, lower density, less frequent harvest) but no separate figure was
  found to split the two forms.
- Sowing depth: 2.5 cm (2-3 cm range). Source basis:
  [Hortipendium - Mangold Erwerbsanbau](https://www.hortipendium.de/Mangold_Erwerbsanbau)
  gives "Saattiefe in mm: 20 - 30 mm" for commercial leaf-chard (Blattmangold)
  direct seeding. Derivation: the middle of the 20-30 mm range, converted to
  2.5 cm. This is a new, sourced value; the previous note left this field
  open.
- Nutrient demand: medium (Mittelzehrer). Source basis: [BUND Region
  Hannover - Stark-, Mittel- und Schwachzehrer im Gemüse- und
  Kräutergarten](https://bund-region-hannover.de/fileadmin/hannover/BUND_aktiv/Universum_Kleingarten/Publikationen_zum_Download/Handreichung_Stark-_Mittel-_und_Schwachzehrer.pdf)
  explicitly lists "Mangold" as a Mittelzehrer alongside Rote Bete, Spinat,
  and other Beta vulgaris/related crops. This revises the previous "moderate
  to high" wording to a decided "medium" classification; documented as a
  deliberate change, not a silent one.
- Thousand kernel weight: left open; not found in this research pass.

## Sources
- [Gartenberatung - Kultur- und Anzuchtdaten Mangold](https://www.gartenberatung.de/gemuese/blattgemuese/Kultur-Anzuchtdaten-Mangold.htm)
- [Plantura - Mangold anbauen](https://www.plantura.garden/gemuese/mangold/mangold-anbauen)
- [Kiepenkerl - Mangold Kulturanleitung](https://www.kiepenkerl.de/kulturanleitungen/mangold/)
- [Hortipendium - Mangold Erwerbsanbau](https://www.hortipendium.de/Mangold_Erwerbsanbau)
- [BUND Region Hannover - Stark-, Mittel- und Schwachzehrer im Gemüse- und Kräutergarten](https://bund-region-hannover.de/fileadmin/hannover/BUND_aktiv/Universum_Kleingarten/Publikationen_zum_Download/Handreichung_Stark-_Mittel-_und_Schwachzehrer.pdf)

## Research Status
- Researched on: 2026-09-18
- Calendar values researched on: 2026-09-21
- Yield, sowing depth and nutrient demand researched on: 2026-09-22
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: none found on the type split itself; sources agree
  leaf/cut and stalk chard differ in sowing timing and spacing.
- Open mapping questions: whether OpenFarmPlanner should model leaf/cut
  chard and stalk chard as separate Kultur entries is an open question,
  documented explicitly rather than silently decided; thousand kernel weight
  remains open. Growth duration, harvest window, and yield are inferred/
  derived values that mix both types or target the cut-chard case only.
- Public-readiness: needs review; type-split question is open; yield is an
  uncertain derived value; sowing depth and nutrient demand are now decided
  with sources.
