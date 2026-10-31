---
name: phase2-species-sync
description: Write names that this repository's approved notes already establish (synonyms, regional names for Austria/Switzerland, fr/es translations, a missing species proposal) into OpenFarmPlanner's official crop species library with the admin crop-library token (Phase 2, admin only). Use when the user explicitly asks to update the official crop species / Kulturarten for researched crops. Not for importing a crop list (import-crop-species-list), not for GRIN batches (grin-species-batch), not for project Cultures (phase2-culture-sync).
argument-hint: "[crop species names]"
---

# Phase 2: sync approved names into the official crop species library

Follow [`PHASE2_SPECIES_PROMPT.md`](../../../PHASE2_SPECIES_PROMPT.md) step by
step; it holds the rules, the sync sequence and when to stop and ask. Also
read [`docs/crop-species-api.md`](../../../docs/crop-species-api.md) and
[`docs/rules/crop-species-naming.md`](../../../docs/rules/crop-species-naming.md).

On top of the prompt:

- Only on explicit request. Show the user the full diff per species (language,
  common name, synonyms, regional names, scientific name: live vs. new) and
  wait for an explicit OK before any PATCH or POST.
- Always include the English translation, and check Austrian and Swiss
  regional names explicitly; if none exists, say so in the summary instead of
  leaving the field silently empty.
- The import skill's helpers can do the API work:
  `.claude/skills/import-crop-species-list/scripts/apply_species_plan.py`
  (new species, synonym merges, `--restore` after approval) and
  `apply_scientific_names.py` (scientific names). Both are dry runs by default.
- New species arrive as `proposed`; a moderator approves them in the UI.
  Read the records back after approval.
- Logs and pre-write snapshots go to `sync-private/`, never to git.
