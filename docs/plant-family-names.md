# Plant-family Names

The [reference data](../data/plant-family-names.csv) records all 16 existing
family identities in all seven application languages. German and English labels
are preserved. The table below supplies the 80 missing language labels; it does
not change botanical identities, crop memberships or rotation values.

Research status is separate from live deployment. Each row records its direct
source and selection rationale. `preserve` means an existing approved label,
`reviewed` means a sourced vernacular recommendation, and `scientific-label`
means an intentionally retained scientific name.

| Botanical identity | French | Spanish | Italian | Portuguese | Dutch |
| --- | --- | --- | --- | --- | --- |
| Amaranthaceae | Amarantacées | Amarantáceas | Amarantacee | Amarantáceas | Amarantenfamilie |
| Amaryllidaceae | Amaryllidacées | Amarilidáceas | Amarillidacee | Amarilidáceas | Narcisfamilie |
| Apiaceae | Ombellifères | Umbelíferas | Apiacee | Apiáceas | Schermbloemenfamilie |
| Asteraceae | Composées | Compuestas | Asteracee | Asteráceas | Asterfamilie |
| Boraginaceae | Borraginacées | Boragináceas | Boraginacee | Boragináceas | Ruwbladigenfamilie |
| Brassicaceae | Crucifères | Crucíferas | Brassicacee | Brassicáceas | Kruisbloemenfamilie |
| Caprifoliaceae | Caprifoliacées | Caprifoliáceas | Caprifogliacee | Caprifoliáceas | Kamperfoeliefamilie |
| Cucurbitaceae | Cucurbitacées | Cucurbitáceas | Cucurbitacee | Cucurbitáceas | Komkommerfamilie |
| Fabaceae | Légumineuses | Leguminosas | Fabacee | Leguminosas | Vlinderbloemenfamilie |
| Lamiaceae | Labiatacées | Labiadas | Labiate | Lamiáceas | Lipbloemenfamilie |
| Malvaceae | Malvacées | Malváceas | Malvacee | Malváceas | Kaasjeskruidfamilie |
| Montiaceae | Montiacées | Montiáceas | Montiacee | Montiaceae | Bronkruidfamilie |
| Poaceae | Graminées | Gramíneas | Graminacee | Poáceas | Grassenfamilie |
| Polygonaceae | Polygonacées | Poligonáceas | Poligonacee | Poligonáceas | Duizendknoopfamilie |
| Solanaceae | Solanacées | Solanáceas | Solanacee | Solanáceas | Nachtschadefamilie |
| Tropaeolaceae | Tropaeolacées | Tropeoláceas | Tropeolacee | Tropeoláceas | Klimkersfamilie |

The Portuguese Montiaceae label intentionally uses the scientific family name.
A verified Portugal-standard vernacular form was not established; inventing a
Portuguese suffix would not improve accuracy. This is not an English label or
an English fallback, but it is not counted as a verified native common name.
The Italian Montiacee is attested in an Italian botanical identification guide.

## Evidence and scope

The [UPOV multilingual family index](https://www.upov.int/edocs/mdocs/upov/es/caj_48/caj_48_4_annex_i.pdf)
supplies French and Spanish names for 15 families. It includes established
alternative labels such as Ombellifères, Crucifères and Légumineuses. Its old
family circumscription is not adopted: names do not authorize moving crops.
Montiaceae is checked separately against the
[French botanical society nomenclature](https://www.sbco.fr/Evaxiana/Evaxiana09.pdf)
and a [University of Córdoba botanical publication](https://www.uco.es/servicios/ucopress/kfile.php?filePath=L3Zhci93d3cvZGF0YS9rYWxhbW8vZmlsZXMvYm9vay82NTUvZnJvbnQucGRm).

The [Naktuinbouw Dutch standard names list](https://www.naktuinbouw.nl/download?id=d3YxM1FhakZ1SmxsL3p3ejI3Qk5vT2FYeFBPTDhBPT0%3D)
establishes all 16 Dutch labels. Italian wording is checked against the
[Olivetti botanical family-name list](https://www.dizionario-italiano.it/dizionario-italiano.php?lemma=ACEA100),
[Treccani Labiate](https://www.treccani.it/enciclopedia/labiate_%28Enciclopedia-Italiana%29/),
[Treccani Tropeolacee](https://www.treccani.it/vocabolario/tropeolacee/),
[ARPA Puglia Graminacee](https://www.arpa.puglia.it/pagina3421_graminacee.html),
[ARPA Lazio Polygonaceae](https://www.arpalazio.it/documents/20124/69790/Guida_Fot_Piante.pdf)
and [the Italian Montiacee identification entry](https://www.riconoscerelepiante.it/3659/lewisia-cotyledon-levisia.html).
Portuguese rows link the applicable government agricultural guides,
Flora de Portugal, Portuguese dictionaries or botanical teaching materials.
Names are factual nomenclature; no source descriptions are copied.

## Phase 2

The translation action from
[planner PR #1147](https://github.com/OpenFarmPlanner/planner/pull/1147)
ships in [planner v1.171.0](https://github.com/OpenFarmPlanner/planner/releases/tag/v1.171.0).
It provides the supported write path:
`PATCH /plant-families/{botanical_name}/translations/`, with a translations map.
It requires an administrator using a write-scoped dedicated catalogue token or
an authorized admin session. Project tokens cannot write family names.

Before each PATCH, compare a fresh GET with the reviewed before-image. Send only
the five new labels and preserve omitted German/English labels. Read back all
seven languages, compare family identity and rotation values, and confirm a
repeat plan has no changes. Do not use SQL, seed edits or data migrations for
this backfill. Private IDs, credentials and operational logs stay in ignored
`sync-private/`.
