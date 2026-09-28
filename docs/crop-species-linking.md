# Official Crop Species Linking

Before an OpenFarmPlanner culture can be published, it must be linked to an
official public crop species ("offizielle Kulturart"). The general data of that
culture is then published under the species.

The crop-species link **cannot be set through the sync API token** (a PATCH to
`crop_species` is silently ignored). It has to be chosen in the OpenFarmPlanner
UI publish dialog. This document is the reference for that manual step: it maps
each crop identity used in the notes to a recommended official crop species and
its botanical name.

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

## Chicory / lettuce (Asteraceae)

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Salat | Salat / Lettuce | *Lactuca sativa* | Head, cut, and romaine types share one species and calendar frame. |
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

## Other families

| Crop identity | Recommended species (de / en) | Botanical name | Notes |
|---|---|---|---|
| Porree | Porree / Leek | *Allium ampeloprasum* (Porrum group); often written *Allium porrum* | |
| Spinat | Spinat / Spinach | *Spinacia oleracea* | See `notes/spinach.md`. |
| Rote Rübe | Rote Rübe / Beetroot | *Beta vulgaris* subsp. *vulgaris* (Conditiva group) | |
| Zucchini | Zucchini / Courgette | *Cucurbita pepo* subsp. *pepo* | Summer-squash form of *C. pepo*; distinct calendar from winter squash. |
| Zuckererbse | Zuckererbse / Sugar & snow pea | *Pisum sativum* var. *saccharatum* | Edible-pod pea; see `notes/sugar-pea.md`. |

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
