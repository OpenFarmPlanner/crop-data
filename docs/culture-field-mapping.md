# OpenFarmPlanner Culture Field Mapping

This document maps public research-note concepts to OpenFarmPlanner `Culture`
fields. It is intentionally implementation-oriented, but it must not contain
private project IDs or production IDs.

The field list follows the planner's crop model and crop-detail sections as of
planner v1.220.0 (planner docs `crop-detail.md`, `crop-companions.md`,
`germination.md`, `timing-windows.md`, `plant-health-catalogue.md`). Before a
Phase 2 sync, check the live schema (`GET /agent/openapi.json`) because fields
and enum values can change.

## Inheritance Between General Crop And Variety

A variety (`Sorte`) with a blank value uses its general crop's (`Kultur`)
value for almost every field below. Consequences for notes and sync:

- Research every value at the general crop level first.
- A variety note records a value only when it differs from the general crop
  and a variety-specific source supports it; an intentional reuse stays blank
  in the variety record and is documented in the note.
- **Species-invariant fields** (`crop_family`, `nutrient_demand`,
  `rotation_break_years`) cannot be overridden on a variety at all. They are
  general-crop facts only. A variety source that suggests a different value is
  a source conflict or an identity question, not a variety value.
- **Not inherited:** `seed_type` (variety only) and `specific_properties`
  (record-local).
- **Companions** (good and bad neighbours) belong to the general crop only; a
  variety uses its general crop's list.

## Identity And General Information

| Note concept | OpenFarmPlanner field | Level | Notes |
|---|---|---|---|
| Crop name | `name` | General and variety | General crop entries use an empty variety. |
| Variety name | `variety` | Variety | Leave empty for the general crop. |
| Botanical name | `botanical_name` | General; variety only if narrower | Free text, e.g. `Beta vulgaris var. flavescens`. A variety inherits it. |
| Seed type | `seed_type` | Variety only | `open_pollinated` or `f1_hybrid`. Only from a source that states it; never inferred from the variety name and never set on the general crop. Blank means unknown. |
| Life cycle | `life_cycle` | General | `annual`, `biennial`, `perennial`. Use the cultivation cycle (a biennial grown as an annual is still `biennial`; say so in the note). |
| Standing time | `standing_time_years` | General, perennials | Typical productive lifespan in whole years, at least 1. |
| Crop-specific properties | `specific_properties` | Record-local | Typed values defined per species profile (currently potato only: cooking type, maturity group). Set only when the species has a profile; see the planner's `x-crop-specific-properties` schema extension. Not inherited. |

## Crop Rotation

| Note concept | OpenFarmPlanner field | Level | Notes |
|---|---|---|---|
| Crop family | `crop_family` | General only (species-invariant) | The plant family's botanical name, e.g. `Brassicaceae`. Must match the planner's plant-family list; see [`plant-family-names.md`](plant-family-names.md). |
| Nutrient demand | `nutrient_demand` | General only (species-invariant) | `low`, `medium`, `high` (Schwach-, Mittel-, Starkzehrer). |
| Rotation break | `rotation_break_years` | General only (species-invariant) | Whole years **between** two crops of the same family on one bed. "Every 4 years" is a break of 3. Convert source wording explicitly and document the conversion. |

## Calendar Values

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Cultivation variants | `cultivation_types` | `direct_sowing`, `pre_cultivation`. |
| Growth duration | `growth_duration_days` | Use concrete variety values whenever possible; avoid falsely precise general values. |
| Harvest window | `harvest_duration_days` | Required for useful calendar planning on varieties whenever a plausible value can be documented. |
| Transplant duration | `propagation_duration_days` | Use whole days; document range-to-value decisions. |
| Recurring harvest window (perennials) | `annual_harvest_window` | One inclusive window as `MM-DD/MM-DD`, e.g. `05-01/06-20` for asparagus. Only for perennials harvested every year. |
| Years to first harvest (perennials) | `first_harvest_delay_years` | Whole calendar years after planting before the first harvest; `0` means the planting year. |

Sowing, propagation and planting periods ("sow March to May") map to the
planner's timing windows (`timing_windows`: kinds `pre_cultivation`,
`direct_sowing`, `planting`; units are thirds of a month or ISO weeks). They
are **project data**: the planner never publishes them to the crop library
because they depend on local climate. Keep them in the note as regional
guidance with the region named. Sync them only on explicit request, as a
project-specific choice, never as a general crop fact.

The planner has no harvest-period window for annual crops; the harvest start
follows from planting date plus growth duration.

## Germination

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Optimal germination temperature | `germination_temperature_optimal_min_c`, `germination_temperature_optimal_max_c` | °C. One source range, not a compromise between sources. |
| Minimum germination temperature | `germination_temperature_min_c` | °C. |
| Germination time | `germination_days_min`, `germination_days_max` | Whole days. A single value sets both. |
| Temperature requirement | `germination_temperature_requirement` | `none`, `cold_stratification` (Kaltkeimer), `frost_treatment` (Frostkeimer). Blank is unknown; `none` is an explicit statement and must be source-backed. |
| Light requirement | `germination_light_requirement` | `none`, `light` (Lichtkeimer), `dark` (Dunkelkeimer). Blank is unknown; `none` must be source-backed. |
| Stratification | `stratification_days_min/max`, `stratification_temperature_min_c/max_c` | Only with a cold or frost requirement. |
| Seed pretreatment | `germination_pretreatment` | Free text, e.g. soaking or scarifying. |

A light germinator must have a consistent sowing depth: if sources call a crop
a light germinator, a deep sowing depth is a source conflict to document.

## Site And Plant Health

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Light | `light_requirement` | List of `full_sun`, `partial_shade`, `shade`; all that the sources call suitable. |
| Water need | `water_requirement` | `low`, `medium`, `high`. |
| Winter hardiness | `winter_hardiness` | `hardy`, `with_protection`, `not_hardy`. Name the climate or frost limit the source assumes. |
| Pests and diseases (prose) | `pests_diseases` | Plain free text: what to watch for and practical prevention. |
| Pests and diseases (structured) | `plant_health` | Selections from the planner's plant-health catalogue, by catalogue UUID. **Do not fill from crop notes yet.** The catalogue is researched separately (crop-data issue #8). Until then, record pests and diseases as prose only. |

## Spacing And Seed

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Row spacing | `row_spacing_m` | Metres. The API also accepts `row_spacing_cm`. |
| In-row distance | `distance_within_row_m` | Metres. |
| Sowing depth | `sowing_depth_m`, `sowing_depth_max_m` | A range: lower and upper bound in metres. A single depth sets both. Keep the source range instead of collapsing it to one value. |
| Canopy diameter | `estimated_canopy_diameter_m` | Optional, for individually placed plants (perennials, large fruiting crops). Metres. |
| Thousand kernel weight | `thousand_kernel_weight_g` | Use source-backed values only. |
| Seed rate, direct sowing | `seed_rate_direct_value`, `seed_rate_direct_unit` | Units: `g_per_m2`, `g_per_lfm`, `seeds_per_m2`, `seeds_per_lfm`, `seeds_per_plant` (`lfm` = running metre of row). |
| Seed rate, transplants | `seed_rate_pre_cultivation_value`, `seed_rate_pre_cultivation_unit` | Same units; `seeds_per_plant` must be an integer. |
| Seed safety buffer | `sowing_calculation_safety_percent_direct`, `sowing_calculation_safety_percent_pre_cultivation` | Keep the buffer separate from the source-backed base requirement. |

## Yield

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Expected yield | `expected_yield` | Numeric value only. |
| Yield unit | `harvest_method` | `per_sqm` or `per_plant`. Keep comparable within a crop whenever possible. |
| Default harvest unit | `default_harvest_unit` | `kg`, `g`, `piece`, `bunch`: how harvests of this crop are usually recorded. |
| Piece weight | `average_harvest_piece_weight_g` | Average weight of one harvested piece (head, fruit, root) in grams. |
| Bunch weight | `average_harvest_bunch_weight_g` | Average weight of one bunch in grams. |

Yield-unit rule:

- If the general crop uses kg/m², varieties should usually use kg/m².
- A source-backed head, piece, or per-plant value may be converted to kg/m²:
  `source weight × plants per m²`. Store the source-backed piece weight in
  `average_harvest_piece_weight_g` as well.
- Document source value, spacing or plant density, calculation, rounding, and
  uncertainty in `Planning Value Derivations`.
- If the per-plant value is not source-backed, do not convert it. Reuse a
  reliable general crop planning value instead and document the reuse.
- Keep another yield unit only when the crop's harvest logic genuinely requires
  it.

## Companion Planting (Good And Bad Neighbours)

Neighbours are not `Culture` fields. They are separate relations
(`/crop-companions/`) on the **general crop**, and a pair between two crops
reads the same from both sides.

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Neighbour | `companion_crop` or `companion_family` | Another general crop, or a whole plant family by botanical name. Free text (`companion_text`) is only a fallback and is never published to the crop library. |
| Good or bad | `kind` | `good` or `bad`. |
| Reason | `reason` | `competition`, `allelopathy`, `pest_control`, `soil`, `shared_pests_diseases`, `other`. |
| Note | `notes` | Short note with the source, at most 500 characters per language. |

The crop library publishes a neighbour only when it is a crop species or a
plant family. Name neighbours in notes by their precise crop identity (the
official crop species name) or by plant family, never by broad groups such as
"herbs" or "cabbages". Shared pests and diseases usually follow the plant
family, so a `shared_pests_diseases` relation should normally name the family.

## Notes

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Practical cultivation notes | `notes` | May include sources and derivations in readable language. |

Live notes should include useful cultivation guidance, source links, and short
derivations. They should not include private sync status, production IDs, API
jargon, token details, raw copied source fragments, delivery dates, prices, or
shop availability text. Content that has its own field (germination, site,
pests and diseases, neighbours) goes into that field, not into `notes`.

## Out Of Scope For Public Notes

These fields are project or display data. Do not research or sync them from
this repository: `tags`, `display_color`, supplier and seed-package data,
task templates, `library_pinned_fields`, and the deprecated
`cultivation_type`, `germination_types`, `seed_rate_value`/`seed_rate_unit`.

## Open Questions

Document unclear mappings in the crop note's `Research Status`. Do not silently
invent field mappings when the OpenFarmPlanner model does not represent a
concept, such as sowing windows relative to the last frost date (planned
upstream), regional scheduling, or market form.
