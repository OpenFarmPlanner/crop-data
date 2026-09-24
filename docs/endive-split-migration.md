# Migration Note: Splitting "Endiviensalat" Into Escariol And Frisée

Prepared for a later Phase 2 sync. This document contains no project names,
production IDs, or API details. Nothing has been written to any live project.

## Why

`Endiviensalat` (*Cichorium endivia*) covers two botanical varieties with
different cultivation. Under the "lowest cultivation level" naming rule they
are separate Kulturen:

| | Escariol | Frisée |
|---|---|---|
| Synonym (DE) | Glatte Endivie | Krause Endivie |
| English name | Escarole | Frisée (synonym: Curly endive) |
| Botanical name | *Cichorium endivia* var. *latifolium* | *Cichorium endivia* var. *crispum* |
| Note | [escarole.md](../notes/escarole.md) | [frisee.md](../notes/frisee.md) |

"Endive" alone is not used as a name or synonym: in US English it usually
means chicory (*Cichorium intybus*). `Endiviensalat` should be kept only as a
synonym/alias of both Kulturen, the same mechanism as `Peperoni`.

## Naming And Rank Uncertainty

- The accepted botanical rank differs between sources. EPPO and WFO list
  var. *crispum*; the accepted status of var. *latifolium* could not be
  verified (the Plants of the World Online page returned an error), and one
  source treats the two as cultivar groups. The split rests on cultivation
  differences, not on the botanical rank.

## Existing Records That Hang On "Endiviensalat"

Checked read-only on 2026-09-24 in both available projects.

| Project | Records |
|---|---|
| Research project | general `Endiviensalat` (growth 75 d, harvest window 21 d) and variety `Anconi` (75 d / 21 d) |
| Sync project for the farm crop library | none |

## Variety Assignment

| Variety | Type | Confidence | Basis |
|---|---|---|---|
| Anconi | Escariol (smooth) | high | Breeder pages titled "glattblättrig" / "Smooth endive". Those pages could only be read through search excerpts (HTTP 403), and ReinSaat does not list the variety. |

No other variety is attached. Named candidates for a later Frisée variety
(from ReinSaat and Sativa, not researched as varieties): Capriccio, Très fine
maraîchère, Wallonne, Grosse Pancalière. Diva, Nuance and Géante maraîchère
are smooth types. Bubikopf 2 and Roxane are only described, so their type is
not confirmed.

No variety is unassignable at present.

## Value Comparison (General Crop Level)

Values were researched independently for each type. The former mixed note was
not used as a source.

| Field | Former mixed note | Escariol | Frisée |
|---|---|---|---|
| Growth duration (from transplanting) | 75 d | 70 d | 49 d |
| Harvest window | 21 d | 21 d (inferred) | 14 d (inferred) |
| Propagation duration | 25 d | 25 d | 28 d |
| Row / in-row spacing | 30 × 25-30 cm | 35 × 30 cm | 30 × 30 cm |
| Sowing depth | 1 cm | 1 cm | 1 cm |
| Yield | open | 6 kg/m² | 3.5 kg/m² |
| Thousand kernel weight | open | 1.5 g | 1.5 g |
| Nutrient demand | medium | medium | medium |

Yield, nitrogen level and planting density are where sourced differences
exist (fertilization-regulation table: 600 dt/ha and 190 kg N/ha for smooth
types versus 350 dt/ha and 150 kg N/ha for curly types).

## Variety Values Stay Independent

`Anconi` was rewritten against the Escariol general note with an explicit
value-by-value comparison. Every value is either variety-sourced or an
explicitly documented reuse of the Escariol value. Its growth duration changes
from 75 to 70 days because it now follows the Escariol note.

## Recommended Phase 2 Handling

1. Rename the existing general `Endiviensalat` record to `Escariol` and update
   its values from `escarole.md`. Rename the variety record `Anconi` to the
   crop name `Escariol` in the same step, so the group stays intact (the link
   between general and variety records may be empty, in which case they are
   grouped only by matching names). Then update the `Anconi` values from
   `escarole-anconi.md`.
2. Create `Frisée` as a new general record from `frisee.md`, with no variety.
3. Add `Endiviensalat` as a synonym/alias on both Kulturen. Display language
   and localized crop-species names cannot be set through the sync token and
   need the OpenFarmPlanner UI.
4. Link both records to an official crop species in the UI (see
   [crop-species-linking.md](crop-species-linking.md), which has no entries
   for the two Kulturen yet).

Rename-plus-update was chosen over replacement because it keeps existing record
history and needs one step less. A replacement (delete and recreate) would be
equivalent in outcome.

## Open Points For A Decision

1. **Rename or replace** the existing `Endiviensalat` (recommendation above).
2. **Frost hardiness:** sources contradict each other on which type is hardier
   (one source says Frisée, two say Escariol). No frost value was set for
   either note.
3. **Harvest windows** (21 d and 14 d) are inferred; no source gives one.
4. **Yield gap:** Escariol 6 kg/m² comes from a fertilization-regulation
   yield level, while an Austrian guideline without type gives 3-4 kg/m². The
   6 kg/m² may be high for a garden crop.
5. **Sowing depth** varies in sources (0.5-1 cm commercial, 2-3 cm garden).
6. **Source gaps:** no LfL Bayern, Bio Austria, LWG or DLR sheet on either type
   could be read; values rest on ReinSaat, the fertilization-regulation table,
   Hortipendium and seed companies.
7. **Named Frisée variety:** none is in the data yet. Add one (candidates
   above) if a curly variety should be grown.
8. **`crop-species-linking.md`** needs entries for both Kulturen.
9. The old mixed note [endive.md](../notes/endive.md) is kept, marked
   superseded. Delete it once the migration is done.
