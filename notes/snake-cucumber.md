## Short Description
- `Schlangengurke` (slicing/snake cucumber) is `Cucumis sativus`. It covers the
  long, slender, mild-tasting slicing cucumbers grown for fresh eating, as
  opposed to the small-fruited `Einlegegurke` (pickling cucumber) grown for
  once-over or multi-pick preserving harvest - see `notes/pickling-cucumber.md`
  for that separate Kultur and the identity note there.
- `Gurke` alone is a genus-level umbrella term used loosely in shops and
  everyday German; it is not used here as a Kultur name. In this project it
  may appear only as a generic alias pointing to either `Schlangengurke` or
  `Einlegegurke`, never as the crop identity itself.
- Warm-season, frost-sensitive fruiting crop; needs warm soil, high water and
  nutrient supply, and shelter from wind
  ([LWG Veitshöchheim - Gurkenanbau im Freiland](https://www.lwg.bayern.de/gartenakademie/gartendokumente/infoschriften/064405/index.php)).
- Growth duration: 50 days from planting out to first harvest; harvest
  window 60 days; propagation duration 21 days. These are planning values for
  transplanted open-field cultivation (see `Planning Value Derivations`).

## Sowing & Planting

### Transplants
- Description: pre-cultivate in pots from mid-March, 2 seeds per pot about
  2 cm deep in loose, nutrient-rich soil; keep warm (germination needs at
  least 14 °C, ideally 20-25 °C)
  ([Lubera - Gurken säen](https://www.lubera.com/de/gartenbuch/gurken-saeen-gurkensamen-ins-freiland-aussaeen-und-vorziehen-p5414)).
- Sowing: mid-March onward for transplants.
- Outdoor planting: after the "Ice Saints" (mid-to-late May), once frost risk
  has passed
  ([Lubera](https://www.lubera.com/de/gartenbuch/gurken-saeen-gurkensamen-ins-freiland-aussaeen-und-vorziehen-p5414),
  [LWG Veitshöchheim](https://www.lwg.bayern.de/gartenakademie/gartendokumente/infoschriften/064405/index.php)).

### Direct Sowing
- Description: sow directly into warm soil after frost risk has passed;
  commercial growers often use perforated mulch film to warm the soil.
- Sowing: mid-May onward
  ([Lubera](https://www.lubera.com/de/gartenbuch/gurken-saeen-gurkensamen-ins-freiland-aussaeen-und-vorziehen-p5414)).
- Sowing depth: about 2-3 cm
  ([Lubera](https://www.lubera.com/de/gartenbuch/gurken-saeen-gurkensamen-ins-freiland-aussaeen-und-vorziehen-p5414)).

- Spacing: sources give a range depending on training method - trellised,
  upright-trained plants need about 50-100 cm within the row; ground-trailing
  plants need about 40-50 cm within the row and 100-130 cm between rows. A
  commercial LfL Bayern source gives roughly 1.40 m row spacing with plants
  every 30-40 cm
  ([LWG Veitshöchheim](https://www.lwg.bayern.de/gartenakademie/gartendokumente/infoschriften/064405/index.php),
  [Lubera](https://www.lubera.com/de/gartenbuch/gurken-saeen-gurkensamen-ins-freiland-aussaeen-und-vorziehen-p5414)).
  This is documented as an open source conflict rather than a single silently
  chosen figure; see `Planning Value Derivations`. As a general planning
  value (needed for the structured record), 100 cm between rows and 35 cm
  within the row is used, based on two independent variety-level ReinSaat
  sources (`Tanja` and `Arola`) that both converge on 100 x 30-40 cm outdoors;
  see `Planning Value Derivations`.
- Site: full sun, warm, wind-sheltered; nutrient-rich, well-drained,
  consistently moist soil; cucumbers do not tolerate peat moss or chlorinated
  water in the irrigation.

## Harvest & Use
- Harvest continuously through summer into early autumn once fruits reach
  usable length; frequent picking encourages further fruit set.
- Used fresh, mainly for salads; commercial peak yields under intensive
  cultivation (fleece, drip irrigation) can exceed 1,000 dt/ha, with about
  450 dt/ha considered a secured yield under irrigation
  ([LWG Veitshöchheim](https://www.lwg.bayern.de/gartenakademie/gartendokumente/infoschriften/064405/index.php)).
  This hectare-scale figure (4.5-10+ kg/m²) reflects intensive trellised
  commercial cultivation and is not used directly as the garden planning
  value; see `Planning Value Derivations` for the garden-scale figure used
  instead.

## Notes
- Crop rotation: avoid growing cucumbers after other Cucurbitaceae (pumpkin,
  squash, zucchini, melon) on the same spot for several years.
- Both mixed-flowering (male and female flowers on the same plant) and
  all-female (gynoecious/parthenocarpic) varieties exist; flowering type
  affects whether pollination is needed and is documented per variety.

## Planning Value Derivations
- Spacing: sources disagree by training method and growing scale - garden
  guidance gives 40-130 cm depending on trellised vs. ground cultivation;
  commercial guidance gives about 30-40 cm within the row on 1.40 m rows. No
  single authoritative general-crop figure is derived from the general garden
  sources alone; the conflict is documented instead of silently resolved.
  Re-checked 2026-09-22: since a structured general-crop value is needed and
  two independent variety-specific ReinSaat sources
  ([Tanja](https://www.reinsaat.at/shop/EN/gurken/salatgurken/tanja/),
  [Arola](https://www.reinsaat.at/shop/DE/gurken/salatgurken/arola/)) both
  give 100 x 30-40 cm for outdoor cultivation, this convergence (not an
  invented figure) is used as the general planning value: 100 cm between
  rows, 35 cm within the row (midpoint of 30-40 cm). The wider garden/
  commercial conflict range above remains documented as an open uncertainty
  for other training methods (upright-trellised vs. ground-trailing).
  Variety notes use the more specific spacing given by their own source where
  available.
- Yield: 2.0 kg/m² (`per_sqm`), used as a garden planning value. Source basis:
  a garden-yield reference table on
  [forum.garten-pur.de](https://forum.garten-pur.de/index.php?topic=28046.0)
  gives "Gurken (Schälgurken) 1,6-2,4" kg/m²; `Schälgurke` (peeling/slicing
  cucumber) is the closest garden-yield category to `Schlangengurke` in that
  table. The midpoint, 2.0 kg/m², is used. This sits well below the
  commercial intensive-cultivation figures above (4.5-10+ kg/m²), which use
  trellising, fleece and drip irrigation not assumed for the garden planning
  value. Uncertainty: moderate, since the forum table is a secondary
  aggregation rather than a primary institutional source, and open-field vs.
  greenhouse cultivation can shift yield substantially.
- Thousand kernel weight: about 25 g, inferred as a general planning value
  from two variety-specific figures: `Tanja` gives 15-30 g and `Arola` gives
  27.55 g (see variety notes); the midpoint of the combined range is used.
  This is an inferred general-crop value derived from variety data, not a
  direct general-crop source measurement, and is documented as such rather
  than presented as source-backed for the general crop itself.
- Definition: growth duration is measured from planting out (transplant) to
  the first harvest, not from sowing. Direct-sown plants need roughly 10-14
  days longer from sowing because of germination and early growth
  ([Sperli](https://www.sperli.de/anbauexperte/kulturanleitung-gurken/) gives 10-14 days germination).
- Propagation duration: 21 days. [Sperli](https://www.sperli.de/anbauexperte/kulturanleitung-gurken/) advises sowing 2-3 weeks before
  the planting date and [grove.eco](https://www.grove.eco/pflanzen/cucumis-sativus/) gives about 25 days; 21 days is used.
- Growth duration: 50 days. Inferred from sources that describe timing only as
  a "culture time of 60 days" up to first harvest ([grove.eco](https://www.grove.eco/pflanzen/cucumis-sativus/)) and a
  harvest season from July ([Sperli](https://www.sperli.de/anbauexperte/kulturanleitung-gurken/)); a planting in mid-to-late May with
  first fruit in early to mid July gives about 45-55 days. 50 days is used
  as a mid-season open-field planning value; greenhouse cultivation starts
  earlier but has similar plant-age timing. Uncertainty: about +/- 10 days
  with weather and variety.
- Harvest window: 60 days. Inferred: sources describe continuous harvest from
  late June/July to mid October under favorable conditions
  ([grove.eco](https://www.grove.eco/pflanzen/cucumis-sativus/)), but a single planting of an open-field slicing cucumber
  usually declines earlier because of mildew and cooler nights; 60 days is a
  conservative planning value, and healthy protected crops can crop for
  90-100 days.

## Sources
- [LWG Veitshöchheim - Infoschrift Gurkenanbau im Freiland](https://www.lwg.bayern.de/gartenakademie/gartendokumente/infoschriften/064405/index.php)
- [Lubera - Gurken säen: Gurkensamen ins Freiland aussäen und Vorziehen](https://www.lubera.com/de/gartenbuch/gurken-saeen-gurkensamen-ins-freiland-aussaeen-und-vorziehen-p5414)
- [ReinSaat - Schlangengurken](https://www.reinsaat.at/shop/DE/gurken/schlangengurken/)
- [grove.eco - Gurke](https://www.grove.eco/pflanzen/cucumis-sativus/)
- [Sperli - Kulturanleitung Gurken](https://www.sperli.de/anbauexperte/kulturanleitung-gurken/)
- [forum.garten-pur.de - übliche Ertragsmengen im Hausgarten/Kleingarten](https://forum.garten-pur.de/index.php?topic=28046.0)

## Research Status
- Researched on: 2026-09-18
- Calendar values researched on: 2026-09-21
- Yield and spacing values researched on: 2026-09-22
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: within-row/between-row spacing differs by training
  method (trellised vs. ground) and by garden vs. commercial source; not
  silently resolved, see `Planning Value Derivations`. A structured general
  planning value (100 x 35 cm) is now set from converging variety-level
  sources, without erasing the documented wider-range conflict.
- Open mapping questions: `Gurke` is used only as a generic alias in prose,
  never as a Kultur name; `Schlangengurke` and `Einlegegurke` are kept as
  separate Kulturen because their harvest logic differs (continuous slicing
  harvest vs. once-over/multi-pick pickling harvest). Calendar values are
  defined from planting out for the transplant variant; `Einlegegurke` is
  direct sown and uses sowing-based values (see `pickling-cucumber.md`).
- Public-readiness: needs review; wider spacing conflict remains open (a
  planning-value compromise is now set); calendar values, yield, spacing and
  thousand kernel weight are documented planning values above.
