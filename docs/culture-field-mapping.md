# OpenFarmPlanner Culture Field Mapping

This document maps public research-note concepts to OpenFarmPlanner `Culture`
fields. It is intentionally implementation-oriented, but it must not contain
private project IDs or production IDs.

## Identity

| Note concept | OpenFarmPlanner field | Level | Notes |
|---|---|---|---|
| Crop name | `name` | General and variety | General crop entries use an empty variety. |
| Variety name | `variety` | Variety | Leave empty for the general crop. |
| Crop family | `crop_family` | Usually general | Reuse for varieties unless a source clearly contradicts it. |
| Nutrient demand | `nutrient_demand` | General, sometimes variety | `low`, `medium`, `high`. |

## Calendar Values

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Growth duration | `growth_duration_days` | Use concrete variety values whenever possible; avoid falsely precise general values. |
| Harvest window | `harvest_duration_days` | Required for useful calendar planning on varieties whenever a plausible value can be documented. |
| Transplant duration | `propagation_duration_days` | Use whole days; document range-to-value decisions. |
| Cultivation variants | `cultivation_types` | Examples: direct sowing, pre-cultivation. |

## Spacing And Seed

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Row spacing | `row_spacing_m` | Convert cm to meters for API sync. |
| In-row distance | `distance_within_row_m` | Convert cm to meters for API sync. |
| Sowing depth | `sowing_depth_m` | Convert cm to meters for API sync. |
| Thousand kernel weight | `thousand_kernel_weight_g` | Use source-backed values only. |
| Seed requirement | `seed_requirements` | Keep base requirement and safety buffer conceptually separate. |

## Yield

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Expected yield | `expected_yield` | Numeric value only. |
| Yield unit | `harvest_method` | Keep comparable within a crop whenever possible. |

Yield-unit rule:

- If the general crop uses kg/m², varieties should usually use kg/m².
- A source-backed head, piece, or per-plant value may be converted to kg/m²:
  `source weight × plants per m²`.
- Document source value, spacing or plant density, calculation, rounding, and
  uncertainty in `Planning Value Derivations`.
- If the per-plant value is not source-backed, do not convert it. Reuse a
  reliable general crop planning value instead and document the reuse.
- Keep another yield unit only when the crop's harvest logic genuinely requires
  it.

## Notes

| Note concept | OpenFarmPlanner field | Notes |
|---|---|---|
| Practical cultivation notes | `notes` | May include sources and derivations in readable language. |

Live notes should include useful cultivation guidance, source links, and short
derivations. They should not include private sync status, production IDs, API
jargon, token details, raw copied source fragments, delivery dates, prices, or
shop availability text.

## Open Questions

Document unclear mappings in the crop note's `Research Status`. Do not silently
invent field mappings when the OpenFarmPlanner model does not yet represent a
concept such as exact sowing-date windows, regional scheduling, or market form.
