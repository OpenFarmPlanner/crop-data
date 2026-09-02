# Phase 2 Prompt: Private OpenFarmPlanner Sync

Use this prompt when approved public crop notes should be copied into a private
OpenFarmPlanner project. The prompt may be run from this repository, but all
private operational state must stay outside git. Do not store tokens, project
IDs, production IDs, or sync reports in this public repository.

## Goal

Read approved notes from this repository and write selected values into the
token-bound OpenFarmPlanner project's private crop library.

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
3. Read the API schema.
4. Read the target live crop record, if it already exists.
5. Build a minimal patch that changes only approved fields.
6. Check live notes for forbidden private or technical patterns.
7. Write the patch.
8. Read the record back and verify the changed fields.
9. Record the sync result in a private sync log, not in this public repository.
10. Only update public notes after syncing when the update improves reusable
    crop knowledge rather than documenting private operational state.
