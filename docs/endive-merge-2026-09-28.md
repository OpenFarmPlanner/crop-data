# Migration Note: Merging Glatte Endivie And Krause Endivie Back Into Endivie

Prepared for a later Phase 2 sync. This document contains no project names,
production IDs, or API details. Nothing has been written to any live project
during this research pass.

Supersedes [endive-split-migration.md](endive-split-migration.md) (now marked
superseded at its top), which documented the original 2026-09-24 split this
note reverses.

## Why

On 2026-09-24, `Endiviensalat` was split into two Kulturen, `Glatte Endivie`
(Eskariol/Escariol) and `Krause Endivie` (Frisée), under the "lowest
cultivation level" naming rule, based on apparently different growth
duration, harvest window, spacing, yield and nitrogen demand values per leaf
type. That split was already synced live (see private sync logs, not part of
this public repository).

On 2026-09-28, this was reconsidered. Further research (below) found that
most of the differences behind the split were an artifact of picking
different source ranges per leaf type, not an independently confirmed
botanical or cultivation difference. The merge is a deliberate, documented
decision, made after the counter-research below, not a silent reversal.

## Value Comparison (from the 2026-09-24 split)

| Field | Glatte Endivie (smooth) | Krause Endivie (curly) | Merged (averaged) |
|---|---|---|---|
| Growth duration (from transplanting) | 70 d | 49 d | 60 d |
| Harvest window | 21 d (inferred) | 14 d (inferred) | 18 d |
| Propagation duration | 25 d | 28 d | 27 d |
| Row / in-row spacing | 35 x 30 cm | 30 x 30 cm | 33 x 30 cm |
| Sowing depth | 1 cm | 1 cm | 1 cm (unchanged) |
| Sowing window | 2026-06-01 to 2026-07-20 | 2026-05-01 to 2026-07-15 | 2026-05-16 to 2026-07-17 |
| Yield | 6 kg/m² | 3.5 kg/m² | 4.75 kg/m² |
| Thousand kernel weight | 1.5 g | 1.5 g | 1.5 g (unchanged) |
| Nutrient demand | medium | medium | medium (unchanged) |

## Counter-Research (2026-09-28)

Sources newly consulted, not part of the original 2026-09-24 split research:

- [gemueseliebe.de - Endivien](https://gemueseliebe.de/wp-content/uploads/2025/04/Endivie.pdf)
  (German production guide): describes Frisée and Escariol as one crop with
  one shared sowing window, spacing (30x30 cm) and protocol; distinguishes
  them only by leaf shape ("gekräuselt und geschlitzt - Sorte Frisée - oder
  weitgehend glatt, Escariol").
- [BioCérès - La chicorée frisée et scarole](https://www.bioceres.be/fiche/la-chicoree-frisee-et-scarole)
  (Belgian organic guide): one shared cycle length ("3 à 4 mois") for both
  types; distinguishes them only qualitatively (frisée trickier to grow,
  higher necrosis risk, better winter adaptation), not by yield or duration.
- [Auxine - Scarole fiche culture](https://www.auxine-shop.fr/scarole-fiche-culture/)
  (French guide): "récolte environ 3 à 4 mois après le semis" for scarole,
  matching the BioCérès figure for both types.
- [chefsimon.com - Proportions et grammages des légumes](https://chefsimon.com/articles/pratique-proportions-et-grammages-des-legumes):
  gives one combined average serving weight for "chicorée frisée ou scarole"
  (~480 g/head), no per-type distinction.
- [pflanzjahr.de - Friséesalat anbauen](https://pflanzjahr.de/friseesalat-anbauen/)
  (independent of the sources used in the original split, curly-type only):
  yield 2-3 kg/m², below even the split's 3.5 kg/m² curly-type figure,
  supporting that curly types yield somewhat less, but with no comparable
  independent smooth-type figure to confirm the 6 kg/m² gap.
- The [LKSH DüV Annex 4 Table 4](https://www.lksh.de/fileadmin/PDFs/Landwirtschaft/Duengung/Stickstoffbedarfswertefuer_Gemuesekulturen_und_Erdbeeren.pdf)
  PDF used in the original split was re-verified directly (table extracted
  with `pdftotext`): it does list smooth-leaved endive at 600 dt/ha / 190 kg
  N/ha and Frisée at 350 dt/ha / 150 kg N/ha, confirmed accurate. This
  remains the only source found with a clear, type-attributed structured
  difference. It is a German fertilization-regulation compliance table (sets
  legal nitrogen-application limits per an assumed yield level), not a
  measured yield trial, which may explain why it is not corroborated by
  production guides describing typical head size or garden yield.

## Conclusion

- Growth duration, harvest window, propagation duration and spacing: treated
  as source-range noise rather than a confirmed leaf-type difference, because
  independent production guides (French, Belgian, German) describe a single
  shared cycle and protocol for both leaf types. Merged by averaging the two
  split-era values (see table above and the rounding method in `endive.md`).
- Yield and nitrogen demand: the only figure with a real named-by-type
  source (DüV table), but not corroborated elsewhere. Rather than picking one
  side, the merged general note documents both original figures, the
  DüV source, the lack of corroboration, and uses the arithmetic mean
  (4.75 kg/m²) as an explicit planning compromise, not a resolved fact. See
  `endive.md`, "Differences By Leaf Type".
- Qualitative, sourced differences (frost-tolerance conflict, taste, storage,
  blanching effort) are kept in `endive.md` under "Differences By Leaf Type"
  as informational text, not structured per-type values, so they are not lost
  by the merge.

## Files Changed

- `notes/endive.md`: rewritten as the single merged general crop note for
  Kultur `Endivie` (previously the pre-split general note, marked
  superseded since 2026-09-24; un-superseded and rewritten here).
- `notes/escarole.md`: removed (content merged into `endive.md`; the
  2026-09-24 sourced values remain visible in git history).
- `notes/frisee.md`: removed (content merged into `endive.md`; the
  2026-09-24 sourced values remain visible in git history).
- `notes/escarole-anconi.md` renamed to `notes/endive-anconi.md`: updated to
  compare against the merged `endive.md` general note instead of the removed
  `escarole.md`.
- `docs/endive-split-migration.md`: marked superseded, kept for the original
  split's sourced reasoning and history.

## Recommended Phase 2 Handling

The 2026-09-24 split was already synced live (private records `Glatte
Endivie` and `Krause Endivie`, plus `Anconi` linked to `Glatte Endivie`; see
private sync logs, not part of this repository). Reversing the public notes
does not change the live project. A later Phase 2 sync needs to, in a
project-specific sync session with explicit user approval per record:

1. Rename the `Glatte Endivie` general record back to `Endivie` and update
   its values from `endive.md` (merged/averaged values).
2. Update `Anconi`'s values from the rewritten `endive-anconi.md`.
3. Decide what happens to the `Krause Endivie` general record: either delete
   it (no varieties are attached to it) after confirming no planning data
   depends on it, or leave it as a duplicate to avoid a destructive live
   action without explicit approval. This needs an explicit user decision at
   sync time, not a default.
4. Update synonyms in the UI to the merged alias list: `Eskariol`,
   `Escariol`, `Frisée`, `Friséesalat`, `Endiviensalat`, `Winterendivie`,
   `Endivie glatt`, `Endivie krause`, `Curly endive`.
5. Re-check crop-species linking (`docs/crop-species-linking.md`) once the
   merged record exists; the official species `Endivie` (English "Endive")
   already exists in the library per the original split note and should now
   match the Kultur name directly.

No live API write was made during this research/merge pass.

## Open Points For A Decision

1. The yield/nitrogen-demand averaging (4.75 kg/m²) is a compromise, not a
   resolved fact; if a corroborating trial or extension source for either
   figure turns up, the general value should be revisited.
2. Frost hardiness remains genuinely disputed between sources; no value is
   set, by design.
3. The averaged sowing window (2026-05-16 to 2026-07-17) is a date-midpoint
   simplification; it should be checked against field experience.
4. Whether to keep or delete the live `Krause Endivie` record needs an
   explicit decision during the Phase 2 sync session (see above), not a
   default here.
