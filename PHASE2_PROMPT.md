# Phase 2 Prompt: Private OpenFarmPlanner Sync

Use this prompt when approved public crop notes should be copied into a private
OpenFarmPlanner project. The prompt may be run from this repository, but all
private operational state must stay outside git. Do not store tokens, project
IDs, production IDs, or sync reports in this public repository.

## Goal

Read approved notes from this repository and write selected values into the
token-bound OpenFarmPlanner project's private crop library.

This covers private Culture records (`openfarmplanner-api.md`). Writing
official crop species metadata (synonyms, regional names, new species
proposals) is a separate, admin-only credential and workflow — see
`crop-species-api.md` — and is not part of the default Culture sync flow
below unless explicitly requested.

## Rules

- Confirm the token-bound project context before writing.
- Write only private project `Culture` records unless the user explicitly uses
  the OpenFarmPlanner UI or a separately authorized public moderation workflow.
- Do not write to the public crop library with a general project sync token.
- General crop data and variety data are independent. Write the general crop
  entry with an empty variety and write variety entries separately.
- Before syncing a variety, verify that a matching general crop note and general
  live crop entry exist.
- If a variety reuses a general crop planning value, the note must explicitly
  document the reuse and the reason.
- Keep yield units consistent within one crop whenever possible.
- If a source-backed per-plant/head value is converted to kg/m², document the
  source value, spacing or plant density, calculation, rounding, and uncertainty.
- If a value is not source-backed, do not convert it into a falsely precise
  value. Reuse a reliable general planning value or leave the field open.
- Respect the strictest known API, UI, and data-model constraints.
- Never put private sync bookkeeping, production IDs, API jargon, tokens,
  delivery dates, prices, or copied shop fragments into live-visible notes.
- Write plant family, nutrient demand, and rotation break on the general crop
  only; a linked variety cannot hold its own value.
- Map germination, site, winter hardiness, and pests-and-diseases text to
  their own fields (see `docs/culture-field-mapping.md`) instead of the live
  notes. Do not repeat the same content in both.
- Do not write structured plant-health selections (`plant_health`) until the
  plant-health catalogue is researched and approved.
- Sowing and planting windows are project data. Write them only when the user
  explicitly asks for this project, never as a general default.
- Good and bad neighbours cannot be written with a project token. Prepare
  them for the user to enter in the OpenFarmPlanner UI (see Companions below).
- The first sync of a field that is not yet on the confirmed-writable list in
  `docs/openfarmplanner-api.md` needs a readback check of that field.

## Companions

For each general crop with approved neighbours, give the user a short list
to enter in the crop's companion editor or through the UI spreadsheet import:

- neighbour: an existing general crop of the project or a plant family
- good or bad
- reason (competition, inhibits the other plant, repels or lures pests,
  improves the soil, shares pests or diseases, other)
- a short note with the source, at most 500 characters

Read `/crop-companions/?crop=<id>` first and list only relations that are
missing or differ. Flag a neighbour that has no general crop in the project
instead of turning it into free text silently.

## Live Notes

Live-visible notes may include:

- practical cultivation guidance
- source links
- concise derivations of planning values
- relevant caveats and additional information

Live-visible notes must not include:

- private research status
- production IDs
- token scopes
- API field names
- raw copied source fragments
- delivery dates, prices, or shop availability text

## Recommended Sync Sequence

1. Load private environment variables from an ignored local file.
2. Read token context from the OpenFarmPlanner API.
3. Read the API schema (`/agent/openapi.json`, if the token can read it) for
   current field names, enums, and bounds.
4. Read the target live crop record, if it already exists.
5. Build a minimal patch that changes only approved fields.
6. Check live notes for forbidden private or technical patterns.
7. Write the patch.
8. Read the record back and verify the changed fields.
   Then hand the user the companion list for UI entry, if any.
9. Record the sync result in a private sync log, not in this public repository.
10. Only update public notes after syncing when the update improves reusable
    crop knowledge rather than documenting private operational state.
