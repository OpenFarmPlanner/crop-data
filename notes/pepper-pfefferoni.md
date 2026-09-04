## Short Description
- `Pfefferoni` (also `Peperoni`, in this project the crop covering pointed
  mild-to-hot peppers) is `Capsicum annuum` - the same botanical species as
  sweet pepper (`Paprika`) and most garden chilies.
- `Pfefferoni`, `Peperoni`, `Paprika`, `Peperoncini`, `Chili` are largely
  regional/culinary names, not botanical ranks. The split between them is
  capsaicin content and fruit shape, bred within one species
  ([SRF Kassensturz](https://www.srf.ch/sendungen/kassensturz-espresso/services/espresso-aha/schlauer-i-d-wuche-peperoni-paprika-peperoncini-und-chili-was-ist-was),
  [capsup.at](https://www.capsup.at/blogs/news/paprika-chili-pfefferoni-pepperoni-peperoncini-hot-peppers-verschiedene-worter-mit-der-selben-bedeutung)).
- Very hot chilies from other species do exist - `Capsicum chinense`
  (Habanero), `C. baccatum` (Ají), `C. frutescens` (Tabasco) - but the
  project's `Pfefferoni` and its variety `Milder Spiral` are `C. annuum`.

## Identity And Official Crop Species (Mapping Question)

The OpenFarmPlanner publish dialog offers no official crop species for
`Pfefferoni`; it only offers to suggest it as a new one. This is a mapping
question, documented here rather than decided silently.

- `Pfefferoni` is **not** a distinct botanical subspecies. It is a use/shape
  group inside `Capsicum annuum`.
- Crop-calendar logic (long early pre-cultivation, warmth requirement, growth
  duration, spacing, high nutrient demand) is essentially the same as for sweet
  pepper. The live records reflect this: `Pfefferoni` growth 75 days, harvest
  window 90 days, propagation 84 days, spacing 0.60 x 0.45 m, yield ~4 kg/m².

Recommended handling:

1. Prefer one official crop species **`Paprika` (`Capsicum annuum`)** that
   covers sweet pepper, `Pfefferoni`, and `C. annuum` chilies. Keep the
   project crop's display name `Pfefferoni` and link it to that species.
2. Do **not** create a separate official `Pfefferoni` species purely on the
   hot/sweet distinction - the planning values do not diverge enough to justify
   a parallel crop calendar.
3. If a genuinely different species is grown later (Habanero etc.), that needs
   its own crop identity because germination and season length differ.

The crop-species link cannot be set through the sync API token (it is ignored
on PATCH); this step has to be done in the OpenFarmPlanner UI.

## Planning Value Derivations
- No structured values are set from this note. The live `Pfefferoni` records
  already carry a complete field set; only the official crop-species link is
  open.

## Sources
- [SRF Kassensturz - Peperoni, Paprika, Peperoncini und Chili](https://www.srf.ch/sendungen/kassensturz-espresso/services/espresso-aha/schlauer-i-d-wuche-peperoni-paprika-peperoncini-und-chili-was-ist-was)
- [capsup.at - Paprika, Chili, Pfefferoni ... verschiedene Wörter](https://www.capsup.at/blogs/news/paprika-chili-pfefferoni-pepperoni-peperoncini-hot-peppers-verschiedene-worter-mit-der-selben-bedeutung)
- [Wikipedia - Liste der Paprika- und Chilisorten](https://de.wikipedia.org/wiki/Liste_der_Paprika-_und_Chilisorten)

## Research Status
- Researched on: 2026-09-04
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: none botanical; the naming is regional.
- Open mapping questions: which official OpenFarmPlanner crop species
  `Pfefferoni` should link to. Recommendation: a single `Paprika`
  (`Capsicum annuum`) species. Needs a UI decision; not syncable via token.
- Public-readiness: identity clarified; the structured record is already
  complete, only the crop-species link is open.
