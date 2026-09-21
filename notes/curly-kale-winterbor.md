## Short Description
- `Winterbor` (also sold as `Winterbor F1`) is a curly-kale F1 hybrid,
  `Brassica oleracea var. sabellica`, matched to the general crop note
  `notes/curly-kale.md`.
- Medium-to-tall, high-yielding curly-leaf type described by retail sources as
  very frost hardy (to roughly -15 C) with high vitamin C and calcium content;
  also usable as animal feed.
- Growth duration: about 130-150 days as an inferred planning value for a
  sowing-to-first-harvest window (see `Planning Value Derivations`); the
  effective harvest period extends much further into winter.

## Sowing & Planting

### Direct Sowing
- Description: sow directly or pre-cultivate for transplanting; retail source
  guidance for this variety gives a single May-June sowing window rather than
  separate spring/autumn windows.
- Sowing: May to June.
- Sowing depth: 1-2 cm (general curly-kale range; no variety-specific depth
  source found).

- Spacing: no variety-specific spacing source found; the general curly-kale
  range (about 50 cm between rows, 40-50 cm within the row) is reused (see
  `Comparison With General Crop Data`).
- Site: sun to partial shade; nutrient-rich, well-drained soil. High nutrient
  demand.

## Harvest & Use
- Harvest from October through winter into April; leaves picked after the
  first frosts are commonly described as finer in texture and milder in
  flavor.
- Used as a cooked leaf vegetable.

## Comparison With General Crop Data
- Crop identity matches the general `Grünkohl` / curly-kale note: both are
  `Brassica oleracea var. sabellica`.
- Growth duration deviates from the general note on purpose: the general note
  leaves growth duration open because harvest form varies strongly; this
  variety note provides a concrete inferred value (see
  `Planning Value Derivations`) because OpenFarmPlanner variety records need a
  usable calendar value.
- Harvest window is documented directly from a variety-specific source
  (October to April), unlike the general note, which leaves yield and duration
  open.
- Spacing is reused from the general crop's range; no `Winterbor`-specific
  spacing figure was found in the sources checked.
- Yield: no variety-specific figure was found; the general note itself leaves
  yield as an open range rather than a single value, so no reusable single
  number exists to carry over. Left open here as well, consistent with "do not
  invent a value when neither a variety-specific nor a settled general value
  exists."
- Nutrient demand: reused as `high`, consistent with the general crop and with
  other brassica leaf crops in this repository; no contradicting
  variety-specific source.

## Planning Value Derivations
- Growth duration: 140 days used as the whole-day midpoint of a "sow May-June,
  harvest October-April" window from
  [Treppens](https://www.treppens.de/Saatgut/Gemuesesaatgut/Kohlgemuese/Gruenkohl-Winterbor-F1-Brassica-oleracea-var-sabellica::2353.html)
  (a German seed retailer's variety page), read as roughly late May sowing to
  early October first harvest (about 130-140 days). This is documented as an
  inferred planning value, not a direct source value, because the source gives
  a season description rather than a single day count. Sowing in June instead
  of May, or harvesting the full winter window, would extend the effective
  duration well beyond this figure; that spread is not captured by the single
  stored value.
- Harvest window: no single day count is set; the source-given October-to-April
  range is documented as guidance in `Harvest & Use` rather than converted into
  a `harvest_duration_days` figure, because the range spans roughly 180 days
  and using it directly would misrepresent a typical single-planting pick
  window. Left open and marked as a mapping question.
- Spacing and yield: no variety-specific source found; left open / reused from
  the general range as documented above.

## Sources
- [Treppens - Grünkohl 'Winterbor F1'](https://www.treppens.de/Saatgut/Gemuesesaatgut/Kohlgemuese/Gruenkohl-Winterbor-F1-Brassica-oleracea-var-sabellica::2353.html)
- [Saatgut Dillmann - Grünkohl Winterbor F1](https://saatgut-dillmann.de/produkt/gruenkohl-winterbor-f1/)

## Research Status
- Researched on: 2026-09-18
- General crop note exists: yes (`curly-kale.md`)
- Open source conflicts: none found; only one retail-variety source with
  concrete `Winterbor`-specific cultivation data was located, so no
  cross-source comparison was possible for this variety's own figures.
- Open mapping questions: the harvest window (very long, roughly October to
  April) does not map cleanly onto a single `harvest_duration_days` figure
  without misrepresenting a normal single pick window; left open rather than
  guessed. Growth duration (140 days) is an inferred value from a season
  description, not a direct source value.
- Public-readiness: needs review (growth duration inferred, harvest window and
  yield left open; no live sync performed).
