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
- Growth duration: about 80 days from transplanting to first ripe pods; the
  harvest window is about 100 days and the propagation duration about 84
  days (sowing to transplanting). These are representative planning values
  for a mid-season garden chili, not exact source values; pod size/shape and
  earliness vary strongly between chili types (see `Planning Value
  Derivations`).

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

- Sowing depth: 0.5-1.5 cm depending on seed size; a minimum of 0.5 cm for
  light/dark germinators and up to 1-1.5 cm for larger seed
  ([garteln.info - Chili](https://garteln.info/stammdaten.php?pflanze=Chili),
  [chili-balkon.de - Aussaat](https://www.chili-balkon.de/anzucht/aussaat.htm)).
  See `Planning Value Derivations` for the chosen planning value.
- Spacing: sources disagree - 30-40 cm between plants in one source vs.
  40-50 cm in another
  ([magicgardenseeds.de - Chili-Aussaat](https://www.magicgardenseeds.de/Chili-Aussaat)).
  This is documented as an open source conflict rather than silently picking
  one value; see `Planning Value Derivations` for how a planning value was
  still derived.
- Row spacing: also conflicting - [garteln.info](https://garteln.info/stammdaten.php?pflanze=Chili)
  gives a minimum of 30 cm between rows, while a commercial growing guide
  recommends 70-80 cm between rows for high yield
  ([Wikifarmer - Growing peppers for profit](https://wikifarmer.com/library/en/article/growing-peppers-for-profit-pepper-and-chilies-farming)).
  Documented as an open conflict; see `Planning Value Derivations`.
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
  relying on this general note's single representative values.

## Planning Value Derivations
- Spacing: sources give 30-40 cm and 40-50 cm between plants for chili in
  general garden guidance; no single authoritative figure was found. A
  cautious mid-range planning value of about 40 cm within the row was chosen
  for live sync (matching the live `distance_within_row_m` value); the
  conflict is documented explicitly instead of silently resolved.
- Row spacing: 0.5 m (50 cm). Source basis: [garteln.info](https://garteln.info/stammdaten.php?pflanze=Chili)
  gives a minimum of 30 cm between rows (a garden-minimum, compact-plant
  figure), while [Wikifarmer](https://wikifarmer.com/library/en/article/growing-peppers-for-profit-pepper-and-chilies-farming)
  recommends 70-80 cm between rows specifically for high yield in commercial
  growing. Derivation: 50 cm is a documented cautious midpoint between the
  garden minimum and the high-yield commercial figure, not a direct source
  value; it also sits close to `Pfefferoni`'s live row spacing (0.60 m) for
  the same botanical species. Uncertainty: compact or container-grown chili
  can be planted closer (30 cm); wide-spreading types grown for maximum
  yield benefit from the wider 70-80 cm figure.
- Sowing depth: 1 cm. Source basis: 0.5-1 cm for light/dark-germinating seed
  ([garteln.info](https://garteln.info/stammdaten.php?pflanze=Chili)) and
  1-1.5 cm for larger seed, 0.5-1 cm for small seed
  ([chili-balkon.de](https://www.chili-balkon.de/anzucht/aussaat.htm)).
  Derivation: 1 cm sits within both ranges and is used as a single planning
  value for typical chili seed size.
- Nutrient demand: high (Starkzehrer). Source basis: [Plantura - Starkzehrer, Mittelzehrer und Schwachzehrer](https://www.plantura.garden/gemuese/gemuese-anbauen/starkzehrer-mittelzehrer-und-schwachzehrer)
  explicitly groups "Paprika und Chili" together among high-demand
  vegetables, consistent with this note's existing nutrient-rich-soil
  guidance.
- Yield: left open. No reliable chili/hot-pepper-specific kg/m² or kg/plant
  source was found. The only area-based figure found for a "special form"
  paprika trial that includes one hot-spice entry (`Chili` (Austro)) is an
  aggregate 6 kg/m² for the whole 1997 LVG Heidelberg trial, not broken out
  per variety, so it is not usable as a `Chili`-specific figure
  ([hortigate - Erträge von 6 kg je m²](https://www.hortigate.de/publikation/47661/Ertr%C3%A4ge-von-6-kg-je-m%C2%B2-machen-den-Anbau-von-Paprikasonderformen-im-Freiland-attraktiv/)).
  A commercial polytunnel blog post claims 25 kg/m² for chili without stating
  methodology, plant density, or cultivation period; this figure is judged
  implausible relative to the sweet-pepper figures above and is not used
  ([krosagro - Anbau von Chili im Folientunnel](https://krosagro.com/de/anabu-under-abdeckung/anbau-von-chili-im-folientunnel/)).
  The general `Paprika` note's 5.5 kg/m² value is not reused here either,
  because chili pod types (slim, cayenne-shaped) have much lower individual
  fruit mass than blocky or Spitzpaprika-shaped sweet pepper, and no source
  quantifies whether higher fruit count compensates for this. Left open and
  documented as an explicit research gap rather than guessed.
- Growth duration (from transplanting to first harvest): 80 days.
  Source basis: [Kiepenkerl - Paprika](https://www.kiepenkerl.de/kulturanleitungen/paprika/)
  gives about six weeks from planting out to first harvest for pepper in
  general; the general `Paprika` and `Pfefferoni` values are 70 and 75 days.
  Chili pods usually need to reach full color and are slower than sweet
  pepper, so 80 days was chosen as an inferred value slightly above the
  `Pfefferoni` figure. Not a direct source value.
- Harvest window: 100 days. Sources describe harvest from summer into late
  autumn ("summer to late autumn"); roughly mid-July to end of October is
  about 100 days. Inferred from that calendar wording; fits plants in a
  tunnel or warm site, shorter outdoors in cool years.
- Propagation duration: 84 days (12 weeks). Chili is sown earliest of the
  pepper crops (mid-January to March per the sources above) and needs a long
  warm pre-cultivation; [Kiepenkerl - Paprika](https://www.kiepenkerl.de/kulturanleitungen/paprika/)
  quotes 6-8 weeks for pepper from a mid-February sowing, and a mid-January
  to mid-May calendar implies up to about 17 weeks. 84 days matches the live
  `Pfefferoni` value and sits between these bounds. Re-verified 2026-09-21:
  [LWG Bayern](https://www.lwg.bayern.de/gartenakademie/gartendokumente/gemueseblog/371108/index.php)
  gives about 3 months from a February sowing to May planting (about 85-90
  days), consistent with 84 days; the sweet-pepper value of 70 days
  (`pepper-paprika.md`) differs only because sweet pepper is sown later.
- Field/form constraint: whole integer days. Rounding: none needed beyond
  converting weeks to days.
- Uncertainty: types such as small-podded or very early chilies can be
  harvested 2-3 weeks earlier; variety notes should override these values
  with variety-specific figures where available.

## Sources
- [SRF Kassensturz - Peperoni, Paprika, Peperoncini und Chili](https://www.srf.ch/sendungen/kassensturz-espresso/services/espresso-aha/schlauer-i-d-wuche-peperoni-paprika-peperoncini-und-chili-was-ist-was)
- [magicgardenseeds.de - Chili-Aussaat](https://www.magicgardenseeds.de/Chili-Aussaat)
- [bloomify.de - Cayenne-Chilis pflanzen und pflegen](https://wissen.bloomify.de/wissen/pflanzen/chili)
- [Neudorff - Chili anpflanzen (Capsicum annuum)](https://www.neudorff.at/magazin/chili-anpflanzen-capsicum-annuum)
- [garteln.info - Chili Stammdaten](https://garteln.info/stammdaten.php?pflanze=Chili)
- [chili-balkon.de - Aussaat von Chili und Paprika](https://www.chili-balkon.de/anzucht/aussaat.htm)
- [Wikifarmer - Growing peppers for profit: pepper and chilies farming](https://wikifarmer.com/library/en/article/growing-peppers-for-profit-pepper-and-chilies-farming)
- [Plantura - Starkzehrer, Mittelzehrer und Schwachzehrer](https://www.plantura.garden/gemuese/gemuese-anbauen/starkzehrer-mittelzehrer-und-schwachzehrer)
- [hortigate - Erträge von 6 kg je m² machen den Anbau von Paprikasonderformen im Freiland attraktiv](https://www.hortigate.de/publikation/47661/Ertr%C3%A4ge-von-6-kg-je-m%C2%B2-machen-den-Anbau-von-Paprikasonderformen-im-Freiland-attraktiv/)
- [krosagro - Anbau von Chili im Folientunnel](https://krosagro.com/de/anabu-under-abdeckung/anbau-von-chili-im-folientunnel/)

## Research Status
- Researched on: 2026-09-18
- General crop note exists: not applicable (this is the general crop note)
- Open source conflicts: between-plant spacing given as 30-40 cm in one
  source and 40-50 cm in another; row spacing given as a 30 cm minimum in one
  source and 70-80 cm recommended for high yield in another. Not silently
  resolved, see `Planning Value Derivations`.
- Open mapping questions: same official OpenFarmPlanner crop-species question
  as documented in the Pfefferoni general crop note - whether `Chili` should
  link to a shared `Paprika` (`Capsicum annuum`) crop species or its own.
  Not re-decided here; follow the recommendation already documented in
  `notes/pepper-pfefferoni.md`. Growth duration, harvest window and propagation
  duration are set as representative planning values (see above). Yield is
  left open; no reliable chili-specific kg/m² source was found (see
  `Planning Value Derivations`).
- Calendar values researched on: 2026-09-21
- Calendar values re-verified on: 2026-09-21
- Yield and spacing values researched on: 2026-09-22
- Public-readiness: needs review (spacing conflicts open; yield left open;
  calendar values inferred; identity/crop-species link is a known open
  question shared with `Pfefferoni`).
