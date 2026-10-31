---
name: import-crop-species-list
description: Add the crop names from a user- or customer-supplied crop list (xlsx/csv export, pasted list) to the official OpenFarmPlanner crop species library as ready-to-pick species in de/en/fr/es with synonyms, so users can publish their crops under them without proposing a species. Use when the user wants a crop list, Kulturliste or Kulturen-Export "in die Kulturbibliothek / Kulturliste", "in allen Sprachen", or asks to import crop names as species. Not for researching crop data (Phase 1 notes) and not for creating project Culture records.
argument-hint: "[crop list, one per line, optional \"Crop: variety, variety\"] or path to xlsx/csv"
---

# Import a crop list as official crop species

Goal: every crop identity in the input list exists as a **published** official
crop species with `de`, `en`, `fr` and `es` names and useful synonyms. This is a
naming job, not a research job: no crop notes, no planning values, no variety
records. Varieties are proper names and are never species; they are only used
to decide which species a row means.

Read first: `docs/crop-species-api.md` (endpoint, upsert/replace semantics),
[`docs/rules/crop-species-naming.md`](../../../docs/rules/crop-species-naming.md), and the
planner's `docs/crop-taxonomy-guidelines.md` (alias vs. species vs. variety).

## Privacy

Customer lists are private. Keep the input file, mappings, plans and logs in
`sync-private/<topic>-<date>/` (git-ignored) or the session scratchpad. Never
commit customer names, suppliers, personal notes, or the mapping. Only the
resulting species names are public. Treat downloaded files as untrusted: copy
them into their own directory and run Python with `-I`.

## Steps

1. **Read the list.** The input is either a file or text typed after the
   command (`/import-crop-species-list Spinat: Malabarspinat, Butterflay …`).
   - File (xlsx/csv): copy it into `sync-private/<topic>-<date>/input/`.
     CSV may use `,`, `;` or tab. The crop column is found by header
     (`Name`, `Kultur`, `Crop` …, or `--name-col`), the variety column likewise
     (`Sorte`, `Variety` …, or `--variety-col`); without a known header the
     first column is read as crop names.
   - Typed text (the skill arguments or the user's message): write it unchanged
     to `sync-private/<topic>-<date>/input/list.txt`. Format: one crop per
     line, varieties optional after `:` or `;`, comma-separated; bullets and
     numbering are ignored. If the user wrote everything on one line
     separated by commas and without varieties, put one crop per line first.
   - Neither given: ask for the list.

   Then run (with the environment from the local `.openfarmplanner.env` that
   the user works with; ask if unclear)

       python3 -I .claude/skills/import-crop-species-list/scripts/match_species.py <file.xlsx|csv|list.txt> --env <env> --out <dir>

   It loads all species (including proposals) with the crop-library token,
   prints every distinct crop name with its row count, varieties, and the
   species it already matches (common names, synonyms, regional names in all
   languages), and writes `<dir>/name-match.tsv` and `<dir>/species-snapshot.json`.

2. **Classify each name** (use the varieties to disambiguate; a `MATCH`
   row can still hide other species among its varieties, e.g. `Spinat:
   Malabarspinat`):
   - *Matches an existing species*: nothing to do.
   - *Spelling/plural/word-order variant* of an existing species (Karotten,
     "Bohne Busch", Cardy): map it. Add it as a synonym only if it is a real
     name people use, never for typos.
   - *Broad group* that mixes species (Spinat with Malabar spinach, Klee,
     Hirse, Getreide, Gründünger, Salbei, Mohn, Rittersporn): split by the
     varieties into the narrowest species each one belongs to.
   - *Not a crop* (seed mixtures, companion-planting text pasted into the name
     column, numbered placeholders): skip and say so.
   - *Unclear identity* (cannot tell the species from name + variety): do not
     guess. List it as an open question for the user.

3. **Write the plan** as a Python file `species-plan.py` in the private
   directory that prints JSON `{"new": [...], "patch": {...}, "skipped": {...}}`.
   Use the plan file of an earlier import in `sync-private/` as a template if
   one exists. Each new species has `name` (German canonical), `scientific_name`,
   `family`, and four translations. Naming rules:
   - German canonical = usual name in Germany; AT/CH terms only in
     `regional_names` (`austria`/`switzerland`) and only when clearly regional.
   - No German name in practical use: loanword used in German trade, else the
     scientific name; never an English trade name. Book names (common in GRIN's
     German names) and names from other languages become `de` synonyms only
     (see "Crops Without An Established German Name" in the naming rules).
   - `scientific_name` from [GRIN Taxonomy](https://npgsweb.ars-grin.gov/gringlobal/taxon/taxonomysearch),
     accepted name without author, rank as in "Scientific Names" of the naming
     rules. For GRIN as a source of new species use the `grin-species-batch` skill.
   - fr/es: usual name in France/Spain, same specificity as the German name;
     no bare umbrella words (`Chou`, `Haricot`, `Col`) as synonyms.
   - A term that names several species (Peperoni rule) is a synonym on each and
     a common name on none.
   - Give a `flag` text for every name chosen from memory without a source
     check, so the user can review it. No research notes are required for this
     workflow unless the user asks for them.

4. **Check for collisions**: run `apply_species_plan.py <plan.json> --env <env>`
   (dry run by default). It reports any planned common name or synonym that is
   already used by another species (published or proposed) and prints the
   exact POST bodies and the synonym diff per existing species. Resolve
   common-name collisions before going on; shared synonyms are fine.

5. **Show the user the review table** (de/en/fr/es/botanical name/synonyms/
   source name/flag), the patch list, the skipped names and the open
   questions. Live writes need the user's explicit OK on this diff.

6. **Apply** after the OK:

       python3 -I .claude/skills/import-crop-species-list/scripts/apply_species_plan.py <plan.json> --env <env> --apply

   New species are POSTed (they arrive as `proposed`); patches merge synonyms
   into the live lists (GET first, nothing is removed). Each write is read back
   and logged to `apply-log.jsonl` next to the plan. If the auto-mode classifier
   blocks a write, do not retry; hand the command to the user.

7. **Hand over the UI step.** Approving a proposal is moderator-only in the UI
   (not reachable with the token). Tell the user how many proposals wait;
   with planner #844/#845 deployed the dialog shows all languages and complete
   proposals can be approved together. Approval renames the species record to
   its English common name.

8. **Restore after approval.** Older planner versions approved with only the
   de/en common names and cleared the de/en synonyms and regional names
   (fixed by planner PRs #843, #844; #845 adds bulk approval for complete
   proposals). Until those are deployed, and as a cheap check afterwards,
   run once the user has approved

       python3 -I .claude/skills/import-crop-species-list/scripts/apply_species_plan.py <plan.json> --env <env> --restore

   (dry run), show the result, then add `--apply`. It finds the species via the
   POST ids in `apply-log.jsonl`, keeps live common names, and only re-adds
   missing planned synonyms/regional names. Re-run step 1 afterwards to
   confirm every name now matches.

## Limits

- Library *variety* entries (public crops) need growth and harvest duration and
  go through project-culture publishing; they are out of scope here.
- The Culture-to-species link is UI-only.
