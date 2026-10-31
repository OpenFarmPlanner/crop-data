# Crop Species Naming Rules

Read this before naming, translating, or importing official crop species
(the suggestion list), including species imports from crop lists or from GRIN.
The always-on rules in [`CLAUDE.md`](../../CLAUDE.md) apply as well; the
reviewed fr/es names live in
[`docs/crop-species-names-fr-es.md`](../crop-species-names-fr-es.md).

## Crop Species Names In Other Languages

When researching names of official crop species for a language other than
German (for example `fr` or `es`), keep the identity of the German record and
apply the planner's
[crop taxonomy guidelines](https://github.com/OpenFarmPlanner/planner/blob/main/docs/crop-taxonomy-guidelines.md)
to that language:

- Keep the specificity of the German name. Never map a specific species to an
  umbrella term (`Buschbohne` is `Haricot nain` / `Judía enana`, not `Haricot`
  / `Judía`).
- The common name is the usual name in the reference country (France for
  `fr`, Spain for `es`). Variants from other countries (Belgium, Switzerland,
  Canada, Latin America) are synonyms only.
- Do not set `regional_names` for these languages; the only keys are
  `austria` and `switzerland`.
- A term that names different crops in different countries, or different crops
  within the reference country, is a synonym on every species it can mean and
  never a common name (the "Peperoni" rule).
- Do not add bare umbrella words (`Pois`, `Haricot`, `Col`, `Chou`) as
  synonyms; they would match many species.
- If the German record itself is broad or unclear, translate it with the same
  breadth and document the open identity question instead of narrowing it.

Source order for names:

1. Official multilingual references by scientific name, such as
   [UPOV GENIE](https://www.upov.int/genie/en/), CPVO technical protocols, and
   [GRIN Taxonomy](https://npgsweb.ars-grin.gov/gringlobal/taxon/taxonomysearch)
   (USDA, CC0).
2. Seed catalogues and agricultural statistics from the reference country.
3. Dictionaries, counted only when the definition names the crop meant.

Wikipedia and Wikidata are cross-checks only, never the sole source. Spot-check
automatic text matches against catalogues; a name inside an unrelated product
(for example `tomate cerise` for cherries) is not evidence.

GRIN Taxonomy lists many German "book names" coined in botanical literature
(for example `nickender Lauch`). Such a name is evidence that the name exists,
not that it is in use.

The reviewed result lives in
[`docs/crop-species-names-fr-es.md`](../crop-species-names-fr-es.md). Rows
with an open flag are not written in Phase 2 until the flag is resolved.

## Crops Without An Established German Name

OpenFarmPlanner is meant to cover crops grown worldwide, and many of them have
no German name in practical use. Choose the German canonical name in this
order:

1. A German name actually used in seed catalogues, trade, or standard German
   horticultural references (`Ackerbohne`, `Feijoa`).
2. A loanword that German uses for the traded crop (`Okra`, `Moringa`,
   `Yacon`, `Oca`, `Pak Choi`).
3. Otherwise the scientific name (`Piper auritum`).

Do not use an English trade name as the German canonical name; English names
are often regional and ambiguous, and they belong in the `en` translation.
Names from other languages that German speakers may search for (`Hoja Santa`)
and book names that are not in practical use become German synonyms, never
the canonical name.

## Worldwide Crop Coverage From GRIN

The list of crop species is extended from
[GRIN Taxonomy](https://www.gbif.org/dataset/66dd0960-2d7d-46ee-a491-87b9adcfe7b1)
(USDA ARS, National Plant Germplasm System, published under CC0). Do not use
Growstuff or other CC-BY-SA crop lists as a bulk source: share-alike is not
compatible with the CC-BY-4.0 crop library.

- Scope: taxa with a food use, flavoring herbs and spices, and soil improvers
  (green manure), cultivated somewhere and not flagged only as weeds.
  Perennial trees and palms are included. Ornamentals and cut flowers are out
  of scope for now.
- A GRIN taxon is not automatically an OpenFarmPlanner crop species. Create
  new species at species rank; split by subspecies, variety, or cultivar group
  only where harvest form or crop management differ, following the planner's
  crop taxonomy guidelines.
- Only names are imported: no planning values, no research notes.
- Use GRIN to fill `scientific_name` on existing species too.
- Downloads, match tables, and plans stay in `sync-private/`; only the
  resulting species names are public.

## Scientific Names

Every crop species should carry a `scientific_name`.

- Use the GRIN accepted name without author (`Brassica oleracea var. italica`,
  `Fragaria x ananassa`).
- Use species rank unless an infraspecific name separates the crop from
  another crop of the same species (`Brassica oleracea var. capitata` for
  head cabbage, but `Daucus carota` and `Beta vulgaris` where the
  infraspecific name only separates the crop from its wild form).
- Several crop species may share one scientific name when they are different
  use forms of the same plant (`Mangold`, `Rote Rübe`).
- A crop species that covers several botanical species uses the genus with
  `spp.` (`Capsicum spp.` for `Chili`). Prefer a narrower rank when GRIN has
  one that fits (`Rubus subg. Rubus` for cultivated blackberries).
- If the crop identity is unclear, leave the field empty and document the
  identity question instead of picking one species.
