---
name: grin-species-batch
description: Extend the official OpenFarmPlanner crop-species list towards worldwide coverage with the next batch of crops from GRIN Taxonomy (USDA, CC0) - names only in de/en/fr/es plus scientific name and family - or fill scientific names on existing species from GRIN. Use when the user says "mach mit GRIN weiter", "nächstes GRIN-Paket", "next GRIN batch", or asks to add more worldwide crops to the suggestion list. Not for customer crop lists (use import-crop-species-list) and not for crop research notes.
argument-hint: "[focus, e.g. 'vegetables and pulses' or 'tropical fruit']"
---

# Next GRIN batch for the crop-species list

Names only: no planning values, no research notes. Live writes only after the
user's explicit OK on the review table.

Read first: [`docs/rules/crop-species-naming.md`](../../../docs/rules/crop-species-naming.md)
(naming, German canonical name, GRIN scope, scientific names) and the
planner's `docs/crop-taxonomy-guidelines.md` (species vs. alias vs. variety).

## Private state

Progress, decisions and open questions of the running import live in a
git-ignored status file: `sync-private/grin-import-*/STATUS.md`. Read it
first; update it at the end of every batch. Plans, logs, snapshots and the
GRIN download stay in that directory.

## Steps

1. **GRIN data.** Extract the saved export (or download a fresh one from
   `https://npgsweb.ars-grin.gov/gringlobal/uploads/documents/taxonomy_data.cab`
   into its own directory):

       cabextract -q -d <tmp>/grin/data sync-private/grin-import-*/download/taxonomy_data.cab

2. **Fresh snapshot** of the live library including proposals (read only), with
   the import skill's matcher and the environment named in `STATUS.md`:

       python3 -I .claude/skills/import-crop-species-list/scripts/match_species.py <dir>/input/probe.txt --env <env> --out <dir>

3. **Rank candidates** not yet in the library:

       python3 -I .claude/skills/grin-species-batch/scripts/grin_rank.py <tmp>/grin/data <dir>/species-snapshot.json <dir> [--uses vegetable,pulse,cereal,...]

   Pick about 50 by the batch focus and judgment, not only by score: drop
   wild-gathered plants and weeds, skip taxa that fall inside an existing
   species covering several botanical species (`Chili`, `Kürbis`, `Minze` ...),
   and split a taxon only where use form or harvest logic differ.

4. **Names and family** for the picks:

       python3 -I .claude/skills/grin-species-batch/scripts/grin_names.py <tmp>/grin/data "Genus species" ...

   Choose names per the naming rules: German canonical (used name, loanword,
   else scientific name), usual name in France and Spain, Peperoni rule for
   names that mean different crops, no racist or offensive GRIN names. Check
   doubtful common names with a quick source search.

5. **Write `batchN-plan.py`** in the private directory (format of the import
   skill: `{"new": [{"body": ..., "flag": ...}], "patch": {}}`), using an earlier
   batch plan as template. Then dry-run the collision check and build the
   review table:

       python3 -I batchN-plan.py > batchN-plan.json
       python3 -I .claude/skills/import-crop-species-list/scripts/apply_species_plan.py batchN-plan.json --env <env>
       python3 -I .claude/skills/grin-species-batch/scripts/batch_review.py <tmp>/grin/data batchN-plan.json batchN-review.md

   Resolve every `COMMON NAME` collision; shared synonyms are fine.

6. **Show the user** the table grouped by crop group (de/en/fr/es/scientific
   name), the decisions (Peperoni cases, uncertain names, skipped taxa, AT/CH
   check) and wait for an explicit OK.

7. **Apply**, then read back every proposal against the plan:

       python3 -I .claude/skills/import-crop-species-list/scripts/apply_species_plan.py batchN-plan.json --env <env> --apply

8. **After the user approved the proposals** in the moderation UI, read them
   back again; if synonyms were dropped, run the import skill's `--restore`.
   Update `STATUS.md`.

## Scientific names on existing species

`grin_sci_candidates.py` scores GRIN taxa for each existing species; write the
chosen values into a plan `{"<id>": {"name", "scientific_name", "flag", "replace"}}`
and apply it with
`.claude/skills/import-crop-species-list/scripts/apply_scientific_names.py`
(dry run by default, fills empty values only unless `replace` is set).

Other helpers: `grin_lookup.py` (accepted status of a name),
`grin_match.py` (full match table), `grin_stats.py` (usage and language
counts).
