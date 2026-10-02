# Phase 2 Prompt: Official Crop Species Sync

Use this prompt when approved research in this repository should be written
into OpenFarmPlanner's **official crop species library** (names, synonyms,
regional names, or a new species proposal) — not into a private project's
Culture records. See [`docs/crop-species-api.md`](docs/crop-species-api.md)
for the full API reference this prompt relies on.

This is a separate, admin-only credential and a narrower surface than
`PHASE2_PROMPT.md`'s Culture sync. Do not run this prompt as a routine part
of a Culture sync; run it only when the user explicitly asks for a species
library update.

## Goal

For one or more crop identities named by the user, bring the live official
crop species records up to date with what this repository's approved public
notes already establish — and nothing beyond that. This prompt proposes and
edits species metadata; it does not decide taxonomy on its own authority.

## Rules

- Never invent a synonym, regional name, or new species that is not already
  documented and approved in this repository's public notes
  (`notes/*.md`, `docs/crop-species-linking.md`). If the live library is
  missing something the notes already establish, sync it. If the notes
  themselves are unclear or incomplete, stop and research/document that
  first — do not fill the gap by guessing through the API.
- Apply the planner repo's
  [`docs/crop-taxonomy-guidelines.md`](https://github.com/OpenFarmPlanner/planner/blob/main/docs/crop-taxonomy-guidelines.md)
  rule set for every decision: alias (synonym vs. regional name) vs. own
  species vs. variety. Quote the specific rule you are applying when the
  call is not obvious.
- Before proposing a new species, search (`GET /crop-species/?q=`) to confirm
  it does not already exist under a different spelling, synonym, or regional
  name. A duplicate proposal is rejected by the API — treat that rejection as
  a signal to re-check identity, not as an error to retry past.
- Never touch anything outside this token's surface: no `approve`, `reject`,
  `destroy` calls, and no attempt to set a Culture's `crop_species` link
  (that stays UI-only, unrelated to this token — see
  `docs/crop-species-linking.md`).
- Never write a region outside `austria`/`switzerland` into `regional_names`,
  and never put an ambiguous term there — an ambiguous regional term (names
  different crops in different regions) is a `synonyms` entry on every
  species it can mean, never a displayed regional name. This mirrors the
  planner's own "Peperoni" example in `crop-taxonomy-guidelines.md`.
- A proposal this creates (`status: "proposed"`) is not done when the API
  call succeeds — it still needs a human moderator to approve it in the
  OpenFarmPlanner UI. Say so explicitly in the summary; do not imply the
  change is live.
- Never log the token value itself anywhere, including in `sync-private/`.

## Recommended Sync Sequence

1. Source `.openfarmplanner.env` for the target environment; confirm
   `OFP_CROP_LIBRARY_TOKEN` is set (not just `OFP_TOKEN` — that is the other,
   Culture-scoped token and will not authenticate against `/crop-species/`).
2. For each crop identity in scope, re-read its public note(s) and
   `crop-species-linking.md` entry to restate what this sync is about to do
   and why, before calling the API.
3. `GET /crop-species/?q=<name>` to find the current live record, if any.
4. Compare the live record's `translations` (`common_name`, `synonyms`,
   `regional_names`) against the note. Build a minimal PATCH (existing
   species) or POST (missing species) with only the fields that need to
   change.
5. PATCH/POST, then `GET` the record back and diff every field you intended
   to change.
6. Write a short result log to `sync-private/` (never to git): what changed,
   the species id, and whether a proposal is now pending human approval.
7. Report a summary to the user: what was written, what is still pending
   moderator approval, and any identity questions this surfaced that the
   taxonomy guidelines did not resolve.

## When To Stop And Ask

- The note and the live library disagree on canonical spelling or botanical
  identity in a way `crop-taxonomy-guidelines.md` does not clearly resolve.
- The target species does not exist yet and creating it would be a judgment
  call beyond what the note documents (e.g. deciding it is a new species
  rather than a variety).
- The API response suggests a duplicate the search step did not catch.
