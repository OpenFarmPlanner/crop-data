# OpenFarmPlanner Crop Species API Notes (Phase 2 Sync)

Generic, host-neutral notes on the OpenFarmPlanner **crop species** API — the
official, shared taxonomy ("Kulturart") behind the public crop library. This
is a separate surface from [`openfarmplanner-api.md`](openfarmplanner-api.md)
(private project `Culture` records): different auth token, different
endpoint, different data. No hostnames, tokens, or production IDs belong in
this file.

## Why This Exists

Until this was added, synonyms, regional names (AT/CH display names), and new
species proposals could only be written through the OpenFarmPlanner UI by a
moderator — see the "cannot be set through the sync API token" note in
[`crop-species-linking.md`](crop-species-linking.md). This API closes that
gap for species *metadata*. It does **not** close the Culture-to-species
*linking* gap — that is still manual in the UI; see the next section.

## Auth

- Separate token type from the Culture sync token: `Authorization: Bearer
  <token>`, prefix `ofp_clt_` (vs. `ofp_pat_` for the Culture token).
- Load from the same local, git-ignored `.openfarmplanner.env` file as the
  Culture token, under a distinct variable: `OFP_CROP_LIBRARY_TOKEN`. Export
  both `OFP_API` (shared) and `OFP_CROP_LIBRARY_TOKEN` for the chosen
  environment.
- This token is **not project-bound** — it authenticates as whichever admin
  account created it, platform-wide. Never add it to a prompt or log
  alongside a project name; keep the two kinds of token mentally separate.
- Only a platform admin can create this token, through a browser session (not
  via any token) — see the OpenFarmPlanner repo's
  [`docs/crop-library-api-tokens.md`](https://github.com/OpenFarmPlanner/planner/blob/main/docs/crop-library-api-tokens.md)
  for how to request one. This repo only consumes it once issued.

## Base Path

`"$OFP_API/crop-species/"` (same `$OFP_API` as the Culture token, since the
API prefix is identical — only the path segment and the bearer token differ).

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/crop-species/` | List published species. Paginated. |
| GET | `/crop-species/?q=<term>` | Typo-tolerant name/synonym search. |
| GET | `/crop-species/?include_proposed=true` | Also list proposals pending moderator review (requires the bound account to be a moderator). |
| GET | `/crop-species/<id>/` | Read one species, with all its language translations. |
| POST | `/crop-species/` | Propose a new species. Becomes `status: "proposed"`, awaiting human review. |
| PATCH | `/crop-species/<id>/` | Edit a species' `name`/`scientific_name`/`family`/`categories`, or any entry in its `translations` list (requires the bound account to be a moderator). |

## Writing Translations, Synonyms, Regional Names

`translations` is a list; each entry is one language:

```json
{
  "translations": [
    {
      "language_code": "de",
      "common_name": "Tomate",
      "synonyms": ["Paradeiser"],
      "regional_names": {"austria": "Paradeiser"}
    }
  ]
}
```

- `synonyms`: pure search aliases, never displayed to users.
- `regional_names`: keys restricted to `austria`/`switzerland`; these *are*
  displayed to projects in that region instead of the canonical name.
- Sending a `translations` entry **upserts** that language only — languages
  you omit stay untouched. There is no way to delete a translation through
  this API; that stays a moderator UI action.
- Within a language you do send, `synonyms` and `regional_names` are
  **replaced**, not merged: an omitted field is cleared. Always `GET` the
  species first and send the complete lists for that language, or existing
  aliases are lost.
- An entry without `common_name` is skipped silently, so a synonyms-only
  update must still repeat the current `common_name`. Read the record back
  after every write.
- The planner's `SUPPORTED_LANGUAGE_CODES` includes `de`, `en`, `fr`, `es`,
  `it`, `pt` and `nl` after planner#949. This is a source-code contract, not
  proof that a particular deployment supports a language. Verify deployment
  support before writing each new language; a closed application issue or a
  fallback display label is insufficient evidence. Do not probe with writes.
  `de` remains canonical. `it` uses Italy, `pt` uses Portugal (pt-PT), and
  `nl` uses the Netherlands as reference countries. This does not change
  mandatory-translation or fallback policies.
- A read-only deployment check can use unauthenticated `GET /version/` (omit the catalogue token, which is intentionally restricted to catalogue endpoints), then inspect
  `backend/config/languages.py` and the crop-species translation validator in
  `backend/crops/serializers.py` at that exact release tag. Confirm both that
  the language is listed and that the validator uses that supported-language
  configuration. Keep the observed deployment version and evidence in the
  private review log. A generic schema may omit the crop-species endpoints;
  its absence is not proof that the endpoint or language is unsupported.
- New `fr`/`es`/`it`/`pt`/`nl` entries use `common_name`, `synonyms` and
  `regional_names: {}`. Never introduce regional display keys for Brazil,
  Belgium or Italy. When updating an existing entry, preserve its approved
  aliases and regional names: never clear a live list merely because a new
  research row has no aliases.
- Before deciding synonym vs. regional name vs. "this needs a new species",
  follow the planner repo's
  [`docs/crop-taxonomy-guidelines.md`](https://github.com/OpenFarmPlanner/planner/blob/main/docs/crop-taxonomy-guidelines.md)
  rules — alias vs. own-species vs. variety, and the AT/CH regional-name
  rules. Do not invent a different rule set here.

## Explicitly Not Reachable With This Token

- `POST /crop-species/<id>/approve/`, `POST /crop-species/<id>/reject/` —
  publishing or rejecting a proposal stays a human moderator action in the
  UI, even when this token's bound account is itself a moderator.
- `DELETE /crop-species/<id>/` — species deletion stays UI-only.
- Any Culture endpoint (`/cultures/...`). This token cannot read or write
  private project data at all — it is a different credential for a different
  surface. Use `openfarmplanner-api.md`'s token for Culture records.
- **The Culture-to-species link itself** (`crop_species` field on a Culture).
  That still has no writable endpoint anywhere — see
  [`crop-species-linking.md`](crop-species-linking.md), which is unchanged by
  this API.

## Recommended Sync Sequence

1. Source the local env file for the correct environment (both tokens).
2. `GET /crop-species/?q=<name>` to check whether a species already exists
   before proposing one — a duplicate proposal is rejected by the API with a
   `"already exists or has already been proposed"` error.
3. Build a minimal PATCH/POST body with only the approved, changed fields.
4. Check the request against `crop-taxonomy-guidelines.md`'s alias/species/
   variety rule before writing a synonym or regional name.
5. PATCH or POST, then `GET` the record back and diff the verified fields.
6. Write the readback and a short log to `sync-private/` (never to git).
7. A proposal this created (`status: "proposed"`) still needs a human
   moderator to `approve`/`reject` it in the UI — note that as an open item
   rather than treating the proposal as done.

## Italian, Portuguese And Dutch Backfill

The [research and coverage notes](crop-species-names-it-pt-nl.md) and
[per-language reference table](../data/crop-species-names-it-pt-nl.csv) are the
Phase 1 basis. `reviewed` means a research recommendation, not live-write
authorization. Unresolved rows and their botanical candidates are excluded.

The [offline planner](../scripts/plan_species_translations.py) validates the
table and compares it with a complete, fresh published-catalogue snapshot. It
has no API access or live-write capability. Its private plan contains full before-images
and exact translation-only PATCH bodies; each existing target-language alias
and regional-name map is preserved. Unchanged translations produce no patch.
It refuses changes in catalogue coverage and identity rather than quietly
reusing the historical snapshot. See the research notes for usage.

Before a separately authorized sync, refresh the catalogue, verify enabled
languages from deployment evidence, regenerate the diff and review every
changed language. Immediately before each PATCH, GET the record and compare
with the plan's before-image. If anything changed, regenerate and review the
diff; do not send a stale replacement list. Do not POST, rename identities or
change scientific names for this backfill.

After every authorized PATCH, GET the same ID and compare all intended fields,
as well as omitted-language translations, identity and scientific name with
the before-image. Check `display_name` **and** `display_language_code` in each
written request language to detect fallback. Search each new common name and
alias with `?q=` and verify that the original species ID appears (follow
pagination, and allow shared synonyms to return multiple crops). Record these
checks privately. Replanning against the verified snapshot must yield no
remaining patches for those entries.

### Search Ranking Follow-up

A successful translation readback does not guarantee that autocomplete returns
every exact synonym. The
[species search service](https://github.com/OpenFarmPlanner/planner/blob/main/backend/crops/services.py)
sorts by match source before exactness: displayed-name matches precede synonym
matches, including when the displayed-name match is only partial. The
[list endpoint](https://github.com/OpenFarmPlanner/planner/blob/main/backend/crops/views.py)
caps results at 20 and returns no next page for that ranked search, even with
`page_size=500`.

Tracked in [planner #1159](https://github.com/OpenFarmPlanner/planner/issues/1159).
Reproducible examples with the reviewed names:

- `GET /crop-species/?language=it&q=Cavolo%20verza` returns the Savoy cabbage
  identity under its Italian common name.
- `GET /crop-species/?language=it&q=Cavolo%20di%20Milano` can omit that same
  identity: other displayed-name token matches occupy the capped result set
  before the exact synonym is reached.
- The stored synonym is returned for the same query with `language=en`,
  confirming that it is indexed rather than missing from the translation.
- The same failure occurs for Italian `Spinacio di Giava` (current name
  `Spinacio di Suriname`) and Portuguese `Tomate de carne` (current name
  `Tomate carnudo`). Their exact synonyms are stored; changing only the
  request language to English returns the expected identity.

Application follow-up: review exact-synonym versus partial-display-name ranking
and add a regression check for this capped-result case. This belongs to the
planner search implementation, independently of the catalogue translation
payload. Keep the approved synonym intact. Record such a search check as an
explicit failed verification with a reproducible query; do not count it as
passed just because readback, another request language or an empty repeat plan
succeeds.

## Adjacent Persisted Text

- `GET /plant-families/` returns family names and their translation map. The
  translation-only admin action shipped in planner v1.171.0:
  `PATCH /plant-families/{botanical_name}/translations/`, with a translation map.
  The [family research and API workflow](plant-family-names.md) documents its
  supported authentication, validation and preservation rules. Verify the
  target deployment before using it. A species PATCH
  can change its family association, not translate the family name.
- Public-library descriptions belong to `PublicCropTranslation`, independently
  of species names. The application's session-authorized
  `/public-crops/<id>/translations/` GET/PUT workflow handles editorial text;
  it is not a crop-library-token surface. Variety trade names require sourced
  trade-name evidence and their own authorized workflow. Do not translate
  original variety names as common names or descriptions.
- Track unsupported work explicitly using the
  [adjacent-text audit](crop-species-names-it-pt-nl.md#adjacent-persisted-text).
  Do not use SQL or seed/migration edits to bypass unavailable API capabilities.
