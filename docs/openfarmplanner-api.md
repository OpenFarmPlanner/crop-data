# OpenFarmPlanner API Notes (Phase 2 Sync)

Generic, host-neutral notes on the OpenFarmPlanner API as used for private
Culture sync. No hostnames, tokens, project names, or production IDs belong in
this file. Keep the environment-specific mapping (which token points at which
project) in an ignored local file such as `sync-private/target-notes.md`.

## Auth

- API token in `Authorization: Bearer <token>`.
- Load tokens from a local, git-ignored `.openfarmplanner.env`. The file takes
  one argument selecting the environment and exports `OFP_API` and `OFP_TOKEN`.

## Base Path

- The API base already includes the API prefix (`.../api`). Build requests as
  `"$OFP_API/cultures/..."`.

## Culture Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/cultures/` | List. Paginated: `count`, `next`, `previous`, `results`. |
| GET | `/cultures/?search=<term>` | Filter by crop/variety name. |
| GET | `/cultures/<id>/` | Read one record. |
| PATCH | `/cultures/<id>/` | Partial update. Send only changed fields. |

Trailing slash is required (a missing slash returns `301`).

## Record Model Notes

- A general crop record has an empty `variety`. Variety records repeat the crop
  `name` and add `variety`.
- `general_crop` (FK) may be `null` even when a general record exists; in that
  case general and variety records are grouped only by matching
  `name` / `name_normalized`. **Rename the general record and every variety
  together** so the group stays intact.
- Spacing exists twice: centimetre fields (`row_spacing_cm`,
  `distance_within_row_cm`, `sowing_depth_cm`) and metre fields
  (`row_spacing_m`, ...). Keep them consistent when patching.
- `seed_requirements` is a nested structure mirrored by the flat
  `seed_rate_*` / `sowing_calculation_safety_percent_*` fields.

## Fields Writable via an API Token

Confirmed writable by PATCH: `name`, `crop_display_name`,
`growth_duration_days`, `harvest_duration_days`, `propagation_duration_days`,
`expected_yield`, `harvest_method`, `nutrient_demand`, `notes`, spacing and
sowing-depth fields, `thousand_kernel_weight_g`, seed-rate fields.

## Fields Silently Ignored via an API Token

PATCH returns `200` but the value does not change:

- `crop_display_language_code`
- `crop_species_translations`

These appear to derive from the linked official crop species
(`crop_species`, often `null`) and the Studio publish flow. Setting the display
language and the localized crop-species names needs the OpenFarmPlanner UI
publish / crop-species step, not the sync token.

## Endpoints Blocked for API Tokens

- `GET /` -> `403` `"This endpoint is not available for API tokens."`
- `OPTIONS` metadata -> `"The action 'metadata' is not available for API tokens."`
- No `/token`, `/me`, `/schema`, or OpenAPI document is exposed to tokens.

## Recommended Sync Sequence

1. Source the local env file for the correct environment.
2. `GET /cultures/?search=` to find the record ids.
3. `GET /cultures/<id>/` for each target and save the pre-change state to
   `sync-private/`.
4. Build a minimal PATCH body with only approved, changed fields.
5. Check `notes` for forbidden private or shop text.
6. PATCH, then `GET` again and diff the verified fields.
7. Write the readback and a short log to `sync-private/` (never to git).
