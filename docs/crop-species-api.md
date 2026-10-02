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
