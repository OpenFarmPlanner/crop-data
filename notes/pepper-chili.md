## Short Description
- `Chili` is `Capsicum annuum`, the same botanical species as sweet pepper
  (`Paprika`) and pointed mild-to-hot peppers (`Pfefferoni`/`Peperoni`). The
  split between these project Kulturen is culinary/regional naming and
  capsaicin content, not a botanical rank; see the
  [Pfefferoni general crop note](pepper-pfefferoni.md) for the full identity
  discussion, which already covers this and is not repeated here.
- In this project, `Chili` covers the hot, typically slim/cayenne-shaped
  `C. annuum` types grown mainly for pungency, distinct from the sweet,
  blocky-to-elongated `Paprika` group and the pointed, mild-to-hot
  `Pfefferoni` group
  ([SRF Kassensturz](https://www.srf.ch/sendungen/kassensturz-espresso/services/espresso-aha/schlauer-i-d-wuche-peperoni-paprika-peperoncini-und-chili-was-ist-was)).
  Very hot chilies from other species (`C. chinense` Habanero, `C. baccatum`
  Ají, `C. frutescens` Tabasco) exist but are out of scope here unless grown;
  see the Pfefferoni note's identity section for that caveat.
- Warm-season, frost-sensitive fruiting crop with a long pre-cultivation phase
  and high nutrient demand, like `Paprika` and `Pfefferoni`
  ([bloomify.de - Cayenne-Chilis](https://wissen.bloomify.de/wissen/pflanzen/chili)).
- Growth duration and harvest window are left open at the general-crop level
  (see below); sources give only qualitative timing, and pod size/shape vary
  strongly between chili types (short cayenne pods vs. small thin pods vs.
  bushier ornamental-leaning types), which would make a single precise value
  falsely precise.

## Sowing & Planting

### Transplants
- Description: pre-cultivate early and warm; germination needs at least 20°C,
  optimally 25-27°C
  ([magicgardenseeds.de - Chili-Aussaat](https://www.magicgardenseeds.de/Chili-Aussaat),
  [bloomify.de - Cayenne-Chilis](https://wissen.bloomify.de/wissen/pflanzen/chili)).
- Sowing: mid-January to March, ideally February
  ([magicgardenseeds.de - Chili-Aussaat](https://www.magicgardenseeds.de/Chili-Aussaat)).
- Outdoor / tunnel planting: only after the "Ice Saints" (mid-May) once frost
  risk has passed
  ([Neudorff - Chili anpflanzen](https://www.neudorff.at/magazin/chili-anpflanzen-capsicum-annuum)).

- Spacing: sources disagree - 30-40 cm between plants in one source vs.
  40-50 cm in another
  ([magicgardenseeds.de - Chili-Aussaat](https://www.magicgardenseeds.de/Chili-Aussaat)).
  This is documented as an open source conflict rather than silently picking
  one value; see `Planning Value Derivations` for how a planning value was
  still derived.
- Site: full sun, warm, wind-sheltered; nutrient-rich, well-drained soil,
  matching the general warmth/nutrient needs of `Paprika` and `Pfefferoni`.

## Harvest & Use
- Harvest from summer into late autumn as pods ripen; pungency and color
  intensify with ripeness, so pods can be picked green (milder, less typical
  color) or left to fully ripen (usually red) for maximum heat and flavor
  ([bloomify.de - Cayenne-Chilis](https://wissen.bloomify.de/wissen/pflanzen/chili)).
- Used fresh, dried, or preserved; exact use depends on the specific chili
  type grown, which is not further split in this general note.

## Notes
- Crop rotation: avoid growing after other Solanaceae (including `Paprika`,
  `Pfefferoni`, tomato, potato, eggplant) on the same spot for several years.
- Because "Chili" spans multiple fruit shapes and heat levels within
  `C. annuum`, variety notes should document the specific type (e.g.
  cayenne-style) and its concrete growth duration/harvest window rather than
  relying on this general note's open values.

## Planning Value Derivations
- Spacing: sources give 30-40 cm and 40-50 cm between plants for chili in
  general garden guidance; no single authoritative figure was found. A
  cautious mid-range planning value of about 40 cm within the row could be
  used for live sync, but this note leaves the exact stored value to be
  decided at sync time rather than asserting a false precision; the conflict
  is documented explicitly instead of silently resolved.
- Growth duration / harvest window: sources describe timing only in relative
  terms ("summer to late autumn" harvest, sowing "mid-January to March").
  No day-count planning value is derived here because chili types within
  `C. annuum` vary enough (pod size, plant vigor) that a single number would
  be falsely precise at the general-crop level; this is intentionally left
  open per the "Model Calendar Values Deliberately" rule.

## Sources
- [SRF Kassensturz - Peperoni, Paprika, Peperoncini und Chili](https://www.srf.ch/sendungen/kassensturz-espresso/services/espresso-aha/schlauer-i-d-wuche-peperoni-paprika-peperoncini-und-chili-was-ist-was)
- [magicgardenseeds.de - Chili-Aussaat](https://www.magicgardenseeds.de/Chili-Aussaat)
- [bloomify.de - Cayenne-Chilis pflanzen und pflegen](https://wissen.bloomify.de/wissen/pflanzen/chili)
- [Neudorff - Chili anpflanzen (Capsicum annuum)](https://www.neudorff.at/magazin/chili-anpflanzen-capsicum-annuum)

## Research Status
- Researched on: 2026-09-18
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: between-plant spacing given as 30-40 cm in one
  source and 40-50 cm in another; not silently resolved, see `Planning Value
  Derivations`.
- Open mapping questions: same official OpenFarmPlanner crop-species question
  as documented in the Pfefferoni general crop note - whether `Chili` should
  link to a shared `Paprika` (`Capsicum annuum`) crop species or its own.
  Not re-decided here; follow the recommendation already documented in
  `notes/pepper-pfefferoni.md`. Growth duration and harvest window are left
  open rather than mapped to a specific number.
- Public-readiness: needs review (spacing conflict and calendar values open;
  identity/crop-species link is a known open question shared with
  `Pfefferoni`).
