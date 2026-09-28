## Short Description
- Corn salad / lamb's lettuce (`Feldsalat`) is `Valerianella locusta`, a
  small, frost-tolerant leaf crop grown only in autumn and winter because it
  is a long-day plant and bolts quickly if sown in summer.
- Low nutrient demand (Schwachzehrer); prefers calcareous, loamy soil;
  undemanding overall.
- Growth duration: about 10-12 weeks from sowing to harvest as a general
  planning value; see `Planning Value Derivations`.
- Harvest window: 60 days per sowing (inferred). No propagation; direct sown.
- Expected yield: 1.0 kg/m² as an uncertain general planning value (see
  `Planning Value Derivations`).
- Botanical family: `Caprifoliaceae` (honeysuckle family), subfamily
  Valerianoideae, under current (APG-based) taxonomy; see `Notes`.

## Sowing & Planting

### Direct Sowing
- Description: direct sow into the final position; usually not transplanted.
- Sowing: mid-August onward for autumn/winter harvest; about mid-September
  for a spring harvest. As a long-day plant it is not sown in summer.
- Sowing depth: 1-2 cm.

- Spacing: about 10-15 cm between rows in the open field (closer, about
  8-10 cm, under glass); within the row, about 1-2 cm (see `Planning Value
  Derivations`), depending on intended leaf size.
- Site: sunny; calcareous, loamy soil is sufficient; undemanding otherwise.

## Harvest & Use
- Harvest whole rosettes once filled; frost-tolerant varieties can be
  harvested through winter and into early spring in mild spells.

## Notes
- Germination is slow and temperature-dependent; one source gives about
  18-22 days at 18-20 °C soil temperature, notably longer than many other
  leafy salad crops.
- Frost tolerance varies by variety; document variety-specific hardiness in
  variety notes rather than assuming uniform hardiness for the crop.
- Botanical family, resolved explicitly: [Hortipendium - Feldsalat
  Erwerbsanbau](https://hortipendium.de/Feldsalat_Erwerbsanbau) states corn
  salad belongs to the "Familie der Geißblattgewächse (Caprifoliaceae) sowie
  der Unterfamilie der Baldriangewächse (Valerianoideae)" — the honeysuckle
  family (Caprifoliaceae), subfamily Valerianoideae. This matches this note's
  existing `crop_family` value of `Caprifoliaceae`. The older family name
  Valerianaceae (valerian family) is still common in general and older
  literature, but current (APG III/IV-based) taxonomy treats Valerianaceae as
  merged into Caprifoliaceae as the subfamily Valerianoideae, rather than as
  a separate family. Caprifoliaceae is therefore kept as the current,
  source-confirmed value; Valerianaceae is documented here as the older/
  alternative name for the reader's benefit, not as a competing current
  classification.

## Planning Value Derivations
- Growth duration: 80 days as an inferred general planning value. One source
  gives a total culture duration of about 12 weeks (84 days) for the
  variety-level product `Vit`
  ([ReinSaat](https://www.reinsaat.at/shop/EN/salate/feldsalat/vit/)); this
  is treated as a reasonable general-crop proxy in the absence of a
  dedicated general-crop day count, rounded down slightly to 80 days as a
  whole-day mid-season value. Documented as inferred, not a direct general
  crop source figure.
- Harvest window: 60 days, counted from the start of harvest of one sowing.
  Sources describe harvest from September or October through March for hardy
  varieties ([ReinSaat](https://www.reinsaat.at/shop/EN/salate/feldsalat/vit/)
  chart: October to March; August sowings harvested September to October in
  a search summary of [Plantura](https://www.plantura.garden/gemuese/feldsalat/feldsalat-anbauen)),
  i.e. anything from about 4 weeks (early sowings, quality declines) to about
  4 months (hardy variety sown in September). 60 days was inferred as a
  compromise; the hardy variety `Vit` uses a longer value in
  `corn-salad-vit.md`. Direct sowing, so no propagation duration.
- Growth duration situation: the 80-day value fits an autumn sowing in
  September; summer-to-early-autumn sowings can be ready after about 8 weeks
  (56 days), winter sowings take up to 18 weeks (126 days) per the Plantura
  search summary.
- Field/form constraint: whole integer days.
- Yield: 1.0 kg/m², an uncertain general planning value. Source basis: no
  authoritative commercial (Hortipendium/LfL/KTBL) yield figure was found;
  [Hortipendium - Feldsalat Erwerbsanbau](https://hortipendium.de/Feldsalat_Erwerbsanbau)
  gives spacing and seed-rate data but no yield. Search-engine summaries of
  protected-cultivation trial reports give marketable yields of about
  0.77-1.7 kg/m²: an [Öko-Landbau NRW greenhouse trial](https://www.oekolandbau.nrw.de/sites/default/files/2017-05/35_Feldsalat_Glashaus_Dezember_GM_00.pdf)
  reports about 1.7 kg/m² for a mid-December harvest; a glasshouse
  preliminary-crop trial reports 1.4 kg/m²; an [LVG Baden-Württemberg cold
  film-house spring trial](https://lvg.landwirtschaft-bw.de/site/pbs-bw-mlr-root/get/documents_E-64008075/MLR.LEL/PB5Documents/lvg/pdf/2/2008%20Gute%20Ertr%C3%A4ge%20im%20Feldsalatanbau%20im%20Fr%C3%BChjahr.pdf?attachment=true)
  reports 1.0-1.1 kg/m² for its best varieties; other autumn variety trials
  report 0.77-1.0+ kg/m². Derivation: 1.0 kg/m² was chosen as a conservative
  mid-low value from this range. This is an uncertain planning value: the
  underlying trials are mostly greenhouse/cold-frame protected cultivation,
  not open-field, so an open-field figure could be lower; no separate
  open-field figure was found.
- Thousand kernel weight: left open at the general level; the
  variety-specific figure for `Vit` (1.83 g) is documented in
  `corn-salad-vit.md` rather than generalized here, since no other variety
  was reviewed for comparison.
- Distance within the row: 1.5 cm. Source basis: [Hortipendium - Feldsalat
  Erwerbsanbau](https://hortipendium.de/Feldsalat_Erwerbsanbau) gives an
  in-row plant density of 50-100 plants per linear meter of row for field
  cultivation (higher densities give a shorter harvest window). Derivation:
  spacing = 1 m / plants per meter, giving about 1-2 cm; 1.5 cm is the
  rounded middle. This is a new, sourced value; the previous note left this
  field open.
- Nutrient demand: low (Schwachzehrer). Source basis: [BUND Region Hannover -
  Stark-, Mittel- und Schwachzehrer im Gemüse- und Kräutergarten](https://bund-region-hannover.de/fileadmin/hannover/BUND_aktiv/Universum_Kleingarten/Publikationen_zum_Download/Handreichung_Stark-_Mittel-_und_Schwachzehrer.pdf)
  explicitly lists "Feldsalat" as a Schwachzehrer, stating it needs no
  fertilization and is typically sown onto compost beds only in a later
  season. This revises the previous "low to moderate" wording to a decided
  "low" classification; documented as a deliberate change, not a silent one.

## Sources
- [Hortipendium - Feldsalat](https://hortipendium.de/Feldsalat)
- [Bio-Gärtner - Feldsalat](https://www.bio-gaertner.de/Pflanzen/Feldsalat)
- [ReinSaat - Vit](https://www.reinsaat.at/shop/EN/salate/feldsalat/vit/)
  (used here only for the general growth-duration proxy; treated as
  variety-sourced elsewhere)
- [Hortipendium - Feldsalat Erwerbsanbau](https://hortipendium.de/Feldsalat_Erwerbsanbau)
- [Öko-Landbau NRW - Feldsalat Glashaus Dezember](https://www.oekolandbau.nrw.de/sites/default/files/2017-05/35_Feldsalat_Glashaus_Dezember_GM_00.pdf)
- [LVG Baden-Württemberg - Gute Erträge im Feldsalatanbau im Frühjahr](https://lvg.landwirtschaft-bw.de/site/pbs-bw-mlr-root/get/documents_E-64008075/MLR.LEL/PB5Documents/lvg/pdf/2/2008%20Gute%20Ertr%C3%A4ge%20im%20Feldsalatanbau%20im%20Fr%C3%BChjahr.pdf?attachment=true)
- [BUND Region Hannover - Stark-, Mittel- und Schwachzehrer im Gemüse- und Kräutergarten](https://bund-region-hannover.de/fileadmin/hannover/BUND_aktiv/Universum_Kleingarten/Publikationen_zum_Download/Handreichung_Stark-_Mittel-_und_Schwachzehrer.pdf)

## Research Status
- Researched on: 2026-09-18
- Calendar values researched on: 2026-09-21
- Yield, spacing, nutrient demand and family researched on: 2026-09-22
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: none found; sources agree corn salad is a long-day
  plant restricted to autumn/winter/early-spring cultivation.
- Open mapping questions: the growth-duration value is inferred from a
  variety-level source in the absence of a dedicated general-crop figure;
  this should be reconsidered if a better general source is found. Yield
  (1.0 kg/m²) is an uncertain planning value derived mostly from
  protected-cultivation trials, not a direct open-field source figure.
  Thousand kernel weight is open at the general level.
- Public-readiness: needs review; growth duration and harvest window
  inferred; yield is an uncertain derived value; seed weight open at the
  general level; nutrient demand and botanical family are now decided with
  sources.
