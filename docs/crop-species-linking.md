# Official Crop Species Linking

Before an OpenFarmPlanner culture can be published, it must be linked to an
official public crop species ("offizielle Kulturart"). The general data of that
culture is then published under the species.

The crop-species **link** (which species a Culture points at) still **cannot
be set through any API token** (a PATCH to `crop_species` is silently
ignored) — it has to be chosen in the OpenFarmPlanner UI publish dialog. This
document is the reference for that manual step: it maps each crop identity
used in the notes to a recommended official crop species and its botanical
name.

The species records themselves (name, synonyms, regional names, new
proposals) *can* now be written directly through a separate admin token —
see [`crop-species-api.md`](crop-species-api.md). That closes the "propose or
correct a species" half of this workflow; the "point this Culture at that
species" half below is still manual.

It contains no tokens, project identifiers, or production IDs.

## How to read the table

- **Recommended species (de / en)**: the name the official crop species should
  have, or the existing one to pick.
- **Botanical name**: the accepted scientific name for the crop identity.
- **Notes**: identity or splitting questions, and whether a new official
  species likely needs to be suggested.

## Brassicas

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Weißkraut | Weißkraut / White cabbage | *Brassica oleracea* var. *capitata* f. *alba* | Storage/kraut type carries the general calendar; see `notes/white-cabbage.md`. |
| Wirsing | Wirsing / Savoy cabbage | *Brassica oleracea* var. *sabauda* | See `notes/savoy-cabbage.md`. |
| Schnittkohl | Schnittkohl / Siberian kale | *Brassica napus* var. *pabularia* | Split out of the ReinSaat "Grünkohl/Schnittkohl" category; curly kale (*B. oleracea*) would be a separate species. See `notes/siberian-kale.md`. |
| Blattsenf | Blattsenf / Mustard greens | *Brassica juncea* | Not the mixed "Asian greens" category (that also holds *B. rapa*). See `notes/mustard-greens.md`. |
| Radieschen | Radieschen / Radish | *Raphanus sativus* var. *sativus* | Same species as Rettich but a distinct crop calendar (~30 d); keep separate. |
| Rettich | Rettich / Daikon & winter radish | *Raphanus sativus* var. *longipinnatus* (daikon), var. *niger* (black) | Same species as Radieschen; longer calendar (~50-70 d). |
| Winterkresse | Winterkresse / Land cress | *Barbarea verna* | Sometimes sold as *Barbarea vulgaris*; confirm against the seed source before linking. |
| Kohlröschen | Kohlröschen / (no canonical English name decided yet) | *Brassica oleracea* (hybrid; no separate varietal epithet found) | Bred hybrid of Brussels sprouts and kale; kept as its own species, distinct from both `Rosenkohl` and `Grünkohl`, confirmed by the user on 2026-10-02. No existing live species found under this or related names (`Kalette`, `Pettikohl`, `Wilder Rosenkohl`); new species proposal pending moderator approval. See `notes/flowersprout.md`. |

## Chicory / lettuce (Asteraceae)

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Kopfsalat | Kopfsalat / Butterhead lettuce | *Lactuca sativa* var. *capitata* | Removed the former "Salat" entry (2026-10-02): too general a crop identity, mixing head, cut, and romaine types with different calendar logic under one species, and the live library already carries `Eisbergsalat`/`Iceberg lettuce` and `Römersalat`/`Romaine lettuce` as separate species (confirmed by a 2026-10-02 `q=Salat`/`q=Kopfsalat` search), so a shared generic species contradicts the "narrowest reusable crop identity" rule. `Kopfsalat` here means the butterhead type specifically, matching that existing split. See `notes/head-lettuce.md`; note that note's own "Short Description" still describes head lettuce as covering butterhead, iceberg, and batavia together and has not yet been split to match — flagged as an open point, not resolved here. |
| Radicchio | Radicchio / Red chicory | *Cichorium intybus* var. *foliosum* | Heading red chicory. See `notes/radicchio.md`. |
| Puntarelle | Puntarelle / Catalogna chicory | *Cichorium intybus* var. *foliosum* | Same botanical variety as Radicchio, but the harvest form (flower shoots) and calendar differ enough to justify a separate official species rather than one shared "leaf chicory". Flag for the OpenFarmPlanner maintainers. See `notes/puntarelle.md`. |
| Strohblume | Strohblume / Strawflower | *Xerochrysum bracteatum* (syn. *Helichrysum bracteatum*) | Ornamental cut flower; yield stays open. See `notes/strawflower.md`. |

## Solanaceae

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Pfefferoni | Paprika / Pepper | *Capsicum annuum* | Recommend a single official *Capsicum annuum* species covering sweet pepper, Pfefferoni, and *C. annuum* chilies. Do not create a separate "Pfefferoni" species. See `notes/pepper-pfefferoni.md`. |

## Apiaceae

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Stangensellerie | Stangensellerie / Celery | *Apium graveolens* var. *dulce* | Distinct from celeriac (var. *rapaceum*). |
| Koriander | Koriander / Coriander | *Coriandrum sativum* | Linked here as the leaf crop; the seed-spice use shares the species. See `notes/coriander.md`. |
| Krause Petersilie | Krause Petersilie / Curly parsley | *Petroselinum crispum* var. *crispum* | Already an official, published species. Kept separate from Glatte Petersilie; see the 2026-10-02 decision below. |
| Glatte Petersilie | Glatte Petersilie / Flat-leaf parsley | *Petroselinum crispum* var. *neapolitanum* | Separate official species from Krause Petersilie, not a shared "Petersilie" species. This reverses the shared-species plan in `../docs/parsley-split-migration.md`'s "Synonym Handling" section; split confirmed by the user on 2026-10-02 after the live library turned out to already carry Krause Petersilie as its own species. See `notes/flat-leaf-parsley.md`. |

## Other families

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Porree | Porree / Leek | *Allium ampeloprasum* (Porrum group); often written *Allium porrum* | |
| Spinat | Spinat / Spinach | *Spinacia oleracea* | See `notes/spinach.md`. |
| Rote Rübe | Rote Rübe / Beetroot | *Beta vulgaris* subsp. *vulgaris* (Conditiva group) | |
| Zucchini | Zucchini / Courgette | *Cucurbita pepo* subsp. *pepo* | Summer-squash form of *C. pepo*; distinct calendar from winter squash. |
| Zuckererbse | Zuckererbse / Sugar & snow pea | *Pisum sativum* var. *saccharatum* | Edible-pod pea; see `notes/sugar-pea.md`. |

## Green manure and cut flowers

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Gelbsenf | Gelbsenf / White mustard | *Sinapis alba* | Renamed from `Senf` on 2026-10-20 (no crop was linked). `Senf` is an umbrella over *Sinapis alba*, *Brassica juncea* and *B. nigra*; the record sits among the library's green manures, so it was fixed as Gelbsenf. `Senf` is now a de synonym here and on `Blattsenf` (*B. juncea*); en changed from `Mustard` to `White mustard`. Seed mustard of other species would be a separate species. |
| Bischofskraut | Bischofskraut / Ammi | *Ammi majus* | The German name is used for both *Ammi majus* and *A. visnaga*. Fixed on 2026-10-20 as *Ammi majus*, the cut-flower species, because the record sits among the library's cut flowers; the botanical name is set on the live species. *A. visnaga* (Khella) would be a separate species if needed. |

## Already linked

These general crops already have an official crop species and need no action:
Aubergine, Blattsenf, Borretsch, Buchweizen, Buschbohne, Chinakohl, Gurke,
Karfiol, Karotte, Kidneybohne, Knollenfenchel, Kohlrabi, Kürbis, Majoran,
Pastinake, Tomate, Zuckermais.

## Open questions for the OpenFarmPlanner maintainers

- Whether Puntarelle and Radicchio should be one official "leaf chicory"
  species or two. This note recommends two, because the harvest form and crop
  calendar differ.
- Whether Radieschen and Rettich should be one *Raphanus sativus* species with
  groups, or two. This note recommends two crop identities because the
  calendars differ substantially.
- The correct species for Winterkresse (*Barbarea verna* vs *Barbarea
  vulgaris*).
