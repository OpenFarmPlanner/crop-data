# Crop Species Names: Italian, Portuguese And Dutch

Phase 1 reference for [issue #9](https://github.com/OpenFarmPlanner/crop-data/issues/9).
The [reference table](../data/crop-species-names-it-pt-nl.csv) contains one row
per existing crop identity and target language, with selected common names,
explicit search aliases, sources, candidate botanical names and exceptions.
It is research, not a record of database writes or authorization to make them.

## Coverage And Existing-language Completeness

The complete reference table covers **316 existing published crop identities**
(287 distinct scientific-name strings), audited again on 2026-11-16. Historical
French/Spanish research covered 202 species and is not a sufficient inventory
for this task. The original 2026-11-15 baseline had no it/pt/nl translations;
its first reviewed subset contained 606 entries. Continued country-specific
research now resolves all **948 it/pt/nl entries**, with **83 explicit search
aliases** and no unresolved rows.

| Language | Reference country | Reviewed names | Unresolved entries |
| --- | --- | ---: | ---: |
| it | Italy | 316 | 0 |
| pt | Portugal, pt-PT | 316 | 0 |
| nl | Netherlands, nl-NL | 316 | 0 |

`reviewed` includes the ten deliberate scientific display labels below. It
means the name/identity decision is documented; it does not mean every crop
has an established native vernacular, every possible synonym has been found,
or that the research table itself authorizes writes.

| Language | Crop identity | Deliberate scientific display label |
| --- | --- | --- |
| it | Einjähriger Beifuß | Artemisia annua |
| it | Purpur-Sonnenhut | Echinacea purpurea |
| it | Wilde Monarde | Monarda fistulosa |
| pt | Blauer Waldmeister | Asperula orientalis |
| pt | Erdbeerspinat | Blitum virgatum |
| pt | Erdkastanie | Bunium bulbocastanum |
| pt | Etagenzwiebel | Allium x proliferum |
| pt | Gelenkblume | Physostegia virginiana |
| pt | Surinamspinat | Talinum fruticosum |
| pt | Wilde Monarde | Monarda fistulosa |

The Italian entries are attested grower/nursery market labels. Portuguese
Bunium and Physostegia references omit a common name explicitly. For the other
rare Portuguese crops, exact-taxon and country searches did not establish an
unambiguous local preferred name. The table records the evidence and rejected
false matches. This is not a claim that no vernacular exists anywhere, and
none of these labels is an English fallback.

The completeness audit checks stored names and the language-specific list
response separately, following all pagination links:

| Language | Nonempty stored common names | Displayed in requested language | Missing/fallback labels |
| --- | ---: | ---: | ---: |
| de | 316/316 | 316/316 | 0 |
| en | 316/316 | 316/316 | 0 |
| fr | 316/316 | 316/316 | 0 |
| es | 316/316 | 316/316 | 0 |
| it | 316/316 | 316/316 | 0 |
| pt | 316/316 | 316/316 | 0 |
| nl | 316/316 | 316/316 | 0 |

No duplicate translation languages were observed. The existing de/en/fr/es
common names, aliases and regional maps are preserved. A name matching English
is not by itself a missing translation: established loanwords and trade-derived
crop labels need their own evidence. This is a coverage/fallback audit, not a
new linguistic review of every historical de/en/fr/es synonym.

The [family reference](plant-family-names.md) separately covers **16 families ×
seven languages**. It supplies the 80 formerly missing fr/es/it/pt/nl labels;
Portuguese Montiaceae is an explicit scientific-label exception. Public-library
descriptions remain a separate editorial inventory: the catalogue credential
cannot read them. Do not extend name-completeness claims to descriptions.

## Crop-form Decisions

**Zuckererbse is retained as the flat edible-pod crop**, consistent with the
existing French Pois mangetout and Spanish Tirabeque. The scientific name
Pisum sativum var. macrocarpum alone cannot settle this: the
[Naktuinbouw standard](https://www.naktuinbouw.nl/download?id=d3YxM1FhakZ1SmxsL3p3ejI3Qk5vT2FYeFBPTDhBPT0%3D)
cross-references both Sugar Pea Group (Peul) and Sugarsnap Group (Suikererwt).
[De Bolster](https://www.bolster.nl/peulen-en-sugar-snaps-oogsten/t22801)
explicitly distinguishes young flat pods from thicker round snaps.
The selected names are **Taccola** (alias Pisello mangiatutto), **Ervilha-torta**
and **Peul**, supported by
[Sativa's flat-pod crop](https://www.sativa.bio/it/gigante-svizzero-pisello-mangiatutto-prospecierara-er52)
and [Sementes Vivas Carouby](https://sementesvivas.bio/products/ervilha-carouby).
This resolves the translation interpretation; it does not rewrite taxonomy or
create a sugarsnap species. Round-snap aliases are not added.

Other explicit decisions in the CSV include the leaf versus seed use of
mustard, leaf versus flowering-shoot turnip greens, napus versus oleracea kale,
European medlar versus loquat, and qualified names for tomato/chicory use forms.
Portuguese Ragi avoids the ambiguous Pé-de-galo as its display name; the latter
is retained only as an attested search alias. Portuguese Feijão-mungo-verde
and Urad preserve the Vigna radiata / Vigna mungo distinction despite conflicting
unqualified Feijão-mungo usage in Portuguese sources. Generic botanical matches
never approve a different harvest form or narrower cultivar automatically.

Country evidence includes the
[Naktuinbouw standard names](https://www.naktuinbouw.nl/download?id=d3YxM1FhakZ1SmxsL3p3ejI3Qk5vT2FYeFBPTDhBPT0%3D),
[Italian Sativa catalogue](https://www.sativa.bio/pub/live-catalog/iteu-catalog-2024/index.html),
[Portugal INIAV crop inventory](https://www.iniav.pt/images/Recursos-Geneticos/Portuguese_Inventory_of_Food_and_other_Agricultural_crop_Landraces_A3size.pdf),
[DGADR leaf-celery distinction](https://www.dgadr.gov.pt/mediateca/send/8-protecao-e-producao-integradas/65-producao-integrada-em-horticolas-familia-das-apiaceas-aipo-cenoura-coentros-pastinaca-salsa)
and individual producer, botanical and dictionary entries linked per CSV row.

## How To Read The Reference Table

The CSV is UTF-8. `synonyms`, `sources` and `candidates` are JSON arrays inside
CSV cells, so commas within names and URLs are unambiguous. Its columns are:

| Column | Meaning |
| --- | --- |
| `german_name`, `scientific_name` | Existing public crop/use-form identity; not fields to rename |
| `language_code` | Only it, pt or nl; no separate pt-BR bundle |
| `common_name` | Selected display name; empty for an unresolved entry |
| `synonyms` | Explicitly reviewed aliases only; an empty list adds no aliases |
| `status` | `reviewed` research recommendation or `unresolved` exception |
| `sources` | Direct evidence URLs, or the documented botanical search for a missing exact match |
| `candidates` | Names found in a botanical reference; not approved aliases or fallback labels |
| `note` | Selection rationale or the identity/evidence question that still needs resolution |

`reviewed` does not mean the user has authorized a database update. When a row
is unresolved, both writable name fields stay empty. Candidate terms must never
be promoted automatically just to fill coverage. The table retains candidates
even when they are unsuitable: this makes false matches visible to the next
researcher rather than silently discarding the conflicting evidence.

## Sources And Review Method

Names are factual naming evidence, not copied source descriptions. The
[naming rules](rules/crop-species-naming.md) and the planner's
[taxonomy guidelines](https://github.com/OpenFarmPlanner/planner/blob/main/docs/crop-taxonomy-guidelines.md)
govern the selection. Scientific names and existing de/en/fr/es data stay intact.

1. The [EPPO Global Database](https://gd.eppo.int/) supplies multilingual
   botanical evidence. Each corresponding table row links directly to its
   taxon. The audit found a unique exact botanical match for 267 of the 287
   scientific-name strings. A synonym/accepted-name match or a genus-level
   result needs further identity review; it is not automatically accepted.
   EPPO's language label does not establish a reference country, preferred
   retail name, harvest form or appropriate search alias. Its ordering is not
   a preference ranking. Country and use-form evidence is reviewed separately;
   scientific-label exceptions remain explicit rather than becoming invented
   vernaculars.
2. The vegetable-seed list in Article 2 of Directive 2002/55/EC, consolidated
   2024-12-24, distinguishes crop groups in
   [Italian](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX%3A02002L0055-20241224),
   [Portuguese](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX%3A02002L0055-20241224)
   and [Dutch](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX%3A02002L0055-20241224).
   Its botanical/use-group pairs establish distinctions that species-level
   name lists cannot: chard versus beetroot, artichoke versus cardoon, bulb
   fennel, bush versus climbing beans and pickling versus ordinary cucumber.
   Group labels are naming evidence, not instructions to change taxonomy.
3. Fruit and nut terminology in Regulation 2023/2429, in
   [Italian](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX%3A32023R2429),
   [Portuguese](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX%3A32023R2429)
   and [Dutch](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX%3A32023R2429),
   supports fruit display names rather than automatically importing EPPO's
   tree names. Scientific identity is cross-checked with the linked taxon.
4. Country sources useful for continued review include Portugal's
   [DGAV technical questionnaires](https://www.dgav.pt/plantas/conteudo/sementes-plantas-e-variedades/direito-de-obtentor/questionario-tecnico-da-especie/),
   [DGAV national variety catalogue](https://www.dgav.pt/plantas/conteudo/sementes-plantas-e-variedades/catalogos-de-variedades/),
   [Sementes Vivas catalogue](https://www.sementesvivas.bio/img/cms/2022_CatalogoSemetesVivas_PT-WEB.pdf)
   and the Netherlands'
   [Skal herb categories](https://www.skal.nl/assets/publicaties/categorie-indeling-kruiden-2026.pdf).
   These are further country checks, not blanket evidence for every table row.
   A product title still needs a botanical and harvest-form match.

Wikipedia, Wikidata and unverified dictionary matches are not used to approve
these rows. No bulk share-alike crop list was imported.

## Naming Decisions And Open Questions

The canonical vocabulary follows Italy, Portugal and the Netherlands. Examples
include Portuguese Beringela, Pimento, Cebolinho and Coentros. Brazilian or
Belgian terms can become search aliases only after their exact crop identity
is verified. No regional display-name keys are introduced. Names start with a
capital letter; number follows natural crop usage (for example Brócolos and
Coentros). Original variety and trade names are never translated here.

The table documents questions per language. Recurring cases include:

- **Shared botanical name, different harvest form.** Beetroot/chard/sugar beet,
  leaf/seed mustard, leaf/root turnips and several tomato forms cannot inherit
  the same name merely because their scientific names match. Evidence for
  broad tomato does not approve a salad, cherry, beefsteak or sauce label.
- **Chicory and endive.** Forced Witloof, radicchio, puntarelle, sugarloaf and
  broad/wild chicory remain separate identities. EPPO's broad chicory names
  do not resolve their display names. Cichorium endivia has its own reviewed
  names, including Indivia, Chicória-endívia and Andijvie. Do not alias it to
  forced chicory on the basis of a false friend.
- **Fennel.** The directive's Funcho and Finocchio refer to the Azoricum bulb
  group in that context. They do not approve herb/seed fennel; the table uses
  separately reviewed labels for both forms.
- **Beans and peas.** Keep bush/climbing habit and green-pod/dry-seed use
  distinct. EPPO's ordinary bean or pea names do not establish every use form.
  The flat-pod Zuckererbse interpretation is documented above; round sugarsnaps
  are not silently included.
- **Pepper vocabulary.** Sweet Pimento/Peperone/Paprika does not establish
  Chili or Pfefferoni names. Preserve the long/pickling pepper identity and
  handle shared ambiguous words as search aliases only after review.
- **Potential duplicate mapping.** Rucola and Salatrauke share the same
  scientific name. Both entities are preserved, with attested
  cultivated-rocket labels for each current display name. This naming work does
  not assert that they are distinct taxa or merge them; the duplicate-identity
  question remains separate. Mibuna/mizuna and the existing
  tomato forms also remain intact even if a future taxonomy review changes them.
- **Fruit versus tree and breadth.** Do not substitute tree names for fruit
  by copying a botanical table. European medlar versus loquat needs country
  evidence. German Zwetschke versus the broader English plum label needs an
  identity review rather than automatic translation as generic plum. The
  reviewed table retains the documented use-form decisions.
- **Rare crops and broad genera.** Absence of an exact EPPO match or of a
  target-language name is an evidence gap, not permission to invent a common
  name, silently narrow a genus or choose a related species. These rows link
  the botanical search or matched taxon and explain what is missing.

## Adjacent Persisted Text

Audited separately on 2026-11-15. A species translation cannot update these
other entities.

| Entity | Observed coverage | Supported path and remaining work |
| --- | --- | --- |
| Plant-family display names | Complete seven-language reference for all 16 families; one intentional Portuguese scientific label | `GET /plant-families/` exposes the map. The translation-only admin action shipped in planner v1.171.0; see [family workflow](plant-family-names.md). No SQL or migration backfill. |
| Species-derived labels in the public library | Dependent on the linked species; no separate name backfill can be inferred | Verify after species readback that the requested language is selected rather than falling back. |
| Reusable library descriptions | Coverage unknown: catalogue credential receives HTTP 403 for public-library reads | Follow-up F2: inventory original-language and per-language descriptions through an authorized session. Application GET/PUT `/public-crops/<id>/translations/` is a separate editorial workflow, outside the catalogue-token surface. Translate reusable note content only after reviewing it; no guessed zero count or token workaround. |
| Original variety names and trade-name aliases | Not translated or inventoried by this species audit | Preserve original names. Add a trade name only with supplier evidence under the existing variety workflow; never mechanically translate it. |
| Pest/disease catalogue | Separate work | [Issue #8](https://github.com/OpenFarmPlanner/crop-data/issues/8) owns its multilingual content; do not duplicate that catalogue here. |

The audited families are Amaranthaceae, Amaryllidaceae, Apiaceae, Asteraceae,
Boraginaceae, Brassicaceae, Caprifoliaceae, Cucurbitaceae, Fabaceae, Lamiaceae,
Malvaceae, Montiaceae, Poaceae, Polygonaceae, Solanaceae and Tropaeolaceae.
The [family view](https://github.com/OpenFarmPlanner/planner/blob/main/backend/crops/views.py)
and [public-library translation action](https://github.com/OpenFarmPlanner/planner/blob/main/backend/farm/crops/views/public.py)
document the separate API surfaces. The family reference and supported API
address F1; the description inventory F2 remains separate outstanding work.

## Validation And Phase 2 Handoff

Validate the public table with Python 3.10+ (standard library only), without
credentials or network access:

```sh
python3 -I scripts/plan_species_translations.py
python3 -m unittest discover -s tests -v
```

For a private review plan, obtain a fresh complete published catalogue through
the crop-species GET API, following pagination. Save the flattened JSON list
under `sync-private/`; do not use seed snapshots, an old export, proposals or
the first page alone. Then, **after verifying the enabled languages in the
target deployment**, run for example:

```sh
python3 -I scripts/plan_species_translations.py \
  --snapshot sync-private/catalogue.json \
  --enabled-languages it pt nl \
  --out sync-private/species-translation-review.json
```

Supply only deployed languages if they ship separately. The command makes no
requests and writes only a private review artifact. Its flags record the
operator's deployment check; they do not discover API capabilities. The
[application language configuration](https://github.com/OpenFarmPlanner/planner/blob/main/backend/config/languages.py)
lists seven languages after planner#949, but that alone does not verify a
deployment. Use the [read-only version/release check](crop-species-api.md#writing-translations-synonyms-regional-names)
to inspect the language configuration and translation validator for the actual
deployed release. The generic public schema may omit species endpoints. An
OPTIONS probe was denied during research; fallback display output is not proof
of write support, and a test write is unnecessary.

The plan contains exact translation-only payloads and full private before-images.
It includes reviewed entries only, preserves existing target-language aliases
and regional maps, and omits unchanged entries and other languages. It stops
if the current identity set differs from the table or preferred names collide.
Resolve new, removed or changed identities before planning again.

Issue #9 explicitly requires comparison with latest values and a **separately
authorized write**. Before executing an approved plan, follow
[`PHASE2_SPECIES_PROMPT.md`](../PHASE2_SPECIES_PROMPT.md) and the
[API readback/search checklist](crop-species-api.md#italian-portuguese-and-dutch-backfill).
GET again before each PATCH and stop on concurrent edits. Re-read every changed
record, verify displayed language and all common-name/alias searches against
the original ID, confirm de/en/fr/es and identity fields are unchanged, and
confirm repeat execution plans no changes. Save operational checks privately.

Deployment evidence, approval of the exact diff, write results, readbacks and
live search checks belong in private Phase 2 records. Keep the public table's
research status separate from operational completion. Future unresolved rows
must remain visible and unwritable. Name completeness does not establish
coverage for public-library descriptions, varieties or pest/disease text.

Search behavior also has a separate application follow-up: the reviewed Italian
synonyms Cavolo di Milano and Spinacio di Giava, and Portuguese Tomate de carne,
can be omitted by capped autocomplete results despite being stored and indexed.
This is tracked in [planner #1159](https://github.com/OpenFarmPlanner/planner/issues/1159). See the
[reproduction and ranking explanation](crop-species-api.md#search-ranking-follow-up).
Do not resolve this by deleting the alias, changing the crop identity or
marking the affected search checks as passed.
