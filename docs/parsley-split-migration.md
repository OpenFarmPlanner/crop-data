# Migration Note: Splitting "Petersilie, Blatt" Into Three Parsley Kulturen

Prepared for a later Phase 2 sync. It contains no project names, production
IDs, or API details. Nothing has been written to any live project.

## Why

`Petersilie` (*Petroselinum crispum*) covers botanical varieties with different
cultivation. Under the "lowest cultivation level" naming rule they become three
Kulturen with a symmetric naming scheme:

| | Krause Petersilie | Glatte Petersilie | Wurzelpetersilie |
|---|---|---|---|
| Botanical name (as specified) | *Petroselinum crispum* var. *crispum* | *Petroselinum crispum* var. *neapolitanum* | *Petroselinum crispum* var. *tuberosum* |
| English name | Curly parsley | Flat-leaf parsley | Parsley root |
| Synonyms (DE) | none | Blattpetersilie (glatt), Italienische Petersilie | none |
| Synonyms (EN) | none | Italian parsley | Hamburg parsley |
| Note | [curly-parsley.md](../notes/curly-parsley.md) | [flat-leaf-parsley.md](../notes/flat-leaf-parsley.md) | [parsley-root.md](../notes/parsley-root.md) |

The bare words `Petersilie` and `Parsley` are not used as a name of any Kultur.

## Botanical Rank Conflict (Decision Needed)

The specified ranks are not confirmed everywhere.

- Rhineland-Palatinate trial tables use var. *crispum* and var. *neapolitanum*,
  and commercial sources use var. *neapolitanum*.
- A Plants of the World Online search summary lists *Petroselinum crispum* subsp.
  *crispum* and treats var. *neapolitanum* as not valid. The page itself could
  not be opened (HTTP 403), so this is unverified.
- For the root type, the sources read use subsp. *tuberosum*, while other
  sources use var. or convar.; no taxonomic database was checked.

The notes use the specified var. names and record the conflict. The split rests
on cultivation differences, not on the botanical rank.

## Existing Records That Hang On The Old Kultur

Checked read-only on 2026-09-25.

| Project | Records |
|---|---|
| Research project | general `Petersilie, Blatt` (90 d, harvest window 105 d, yield 2.4 kg/m²) and the four varieties Afrodite, Felicia, Gigante d'Italia, Mooskrause |
| Sync project for the farm crop library | none |

The variety records are not linked to the general record; they are grouped only
by the matching crop name. A rename therefore has to be done for every record
individually.

`Wurzelpetersilie` does not exist yet, neither as a note nor as a record, and is
created new.

## Variety Assignment

| Variety | Kultur | Confidence | Basis |
|---|---|---|---|
| Mooskrause | Krause Petersilie | high | Described as heavily curled; the type is in the name and in retailer titles. |
| Gigante d'Italia | Glatte Petersilie | high | Listed as var. *neapolitanum* with large flat leaves. |
| Felicia | Glatte Petersilie | high | Two seed suppliers list it as smooth. |
| Afrodite | **not assigned** | low to medium | The supplier pages that could be opened describe dark green, aromatic foliage without naming the leaf shape. Retailer titles and search summaries call it curly ("Mooskrause", "Krause Petersilie"), but the breeder text itself was not read. |

Afrodite is listed separately instead of guessed. Its note keeps the old file
name until the type is decided.

Candidates for later varieties (ReinSaat parsley page, via retailer): Grüne
Perle (curly), Einfache Schnitt 3 (smooth). The ReinSaat page itself returned an
error, so the list is unverified.

## Value Comparison (General Crop Level)

Values were researched independently. The former mixed note was not used as a
source.

| Field | Former mixed note | Krause Petersilie | Glatte Petersilie | Wurzelpetersilie |
|---|---|---|---|---|
| Growth duration | 90 d to first cut | 90 d to first cut | 85 d to first cut | 180 d |
| Harvest window | 105 d (cutting period) | 84 d (inferred) | 70 d (inferred) | 60 d (inferred) |
| Propagation | none | optional pot culture only | 45 d | none (direct sown) |
| Yield | 2.4 kg/m² (first cut) | 5.6 kg/m² per three-cut cycle | 6 kg/m² per season | 4.0 kg/m² |
| Spacing (row x in-row) | see old note | 25 x 3 cm | 25 x 3 cm | 30 x 3 cm |
| Sowing depth | see old note | 1.5 cm | 1.5 cm | 1 cm |

Sourced differences between the two leaf types are small: cuts after about
6 weeks (curly) against about 5 weeks (flat), about a week longer crop duration
for curly, less bolting for curly. Frost, leaf mass and aroma differences rest on
one garden source or a search snippet. Spacing, depth, yield and nutrient demand
are not separated by type in the sources, which is recorded as a finding.

The yield basis changed: the old value was one first cut, the new values cover
a whole cutting cycle. Yield is therefore not comparable with the old record.

## Synonym Handling

`Petersilie` and `Parsley` are deliberately not added as search synonyms.
Synonyms belong to the official crop species, not to the private records, and
they also feed exact-identity checks (duplicate detection when proposing a
species, and the "is this name known" lookup), so they are not search-only. The
official library already has the species `Petersilie` (English "Parsley") and a
separate species `Wurzelpetersilie` (English "Parsley root"), so `Wurzelpetersilie`
already has an official counterpart. Both leaf Kulturen would link to the single
leaf species `Petersilie`. Synonyms cannot be set with a sync token and need the
UI.

## Recommended Phase 2 Handling

Because the records are not linked, each one is renamed on its own.

1. Rename the existing general record to `Krause Petersilie` and update its
   values from `curly-parsley.md`. Rename the variety `Mooskrause` to the crop
   name `Krause Petersilie` and update it from `curly-parsley-mooskrause.md`.
2. Create `Glatte Petersilie` as a new general record from
   `flat-leaf-parsley.md`. Rename the varieties `Felicia` and `Gigante d'Italia`
   to the crop name `Glatte Petersilie` and update them from their notes.
3. Create `Wurzelpetersilie` as a new general record from `parsley-root.md`.
4. `Afrodite` stays on the old crop name until its type is decided, then it is
   renamed to the matching Kultur.
5. Set synonyms and the link to the official species in the UI.
6. Delete the old note [leaf-parsley.md](../notes/leaf-parsley.md) once the
   migration is done; until then it is marked superseded.

## Open Points For A Decision

1. **Afrodite:** curly (probable) or open until the breeder text is read.
2. **Which existing record becomes which:** the plan above renames the old
   general record to the curly Kultur. The alternative is to rename it to the
   flat-leaf Kultur, which changes which record keeps its history.
3. **Botanical rank** of the three types (see above).
4. **Yield basis:** per cutting cycle or per season, and whether 5.6 and 6
   kg/m² are realistic for a garden.
5. **Root parsley yield:** 4.0 kg/m² against garden figures of 1 to 1.6 kg/m²
   (the latter from a snippet only), and a very tight 30 x 3 cm spacing.
6. **Source gaps:** LfL Bayern, Bio Austria, KTBL and Agroscope pages could not
   be read for any of the three; the ReinSaat parsley page returned an error.
7. **Frost hardiness** differs between the leaf types only per one source.
8. **Felicia duration:** the old note read a Rhineland-Palatinate table as
   90 days for Felicia; the new flat-leaf note says that table uses a curly
   reference. The variety now reuses the general 85 days, so 90 versus 85 days
   is unresolved.
9. **Gigante d'Italia overwintering:** a group-level table rates the Gigante
   type as bolting early and not suited to overwintering, unlike the general
   flat-leaf note.
10. **`crop-species-linking.md`** has no entries for the three Kulturen yet.
