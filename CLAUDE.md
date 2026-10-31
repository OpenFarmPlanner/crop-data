# OpenFarmPlanner Crop Data

## Purpose

This public repository is the primary workspace for researching and documenting
reusable crop data for OpenFarmPlanner. It is not a live database and must not
contain private OpenFarmPlanner project details.

## Public-First Rule

Everything committed here must be safe for a public repository:

- no API tokens or secrets
- no private project names or project IDs
- no production IDs
- no private live-sync reports
- no personal operational notes

Keep private sync work in an ignored local directory or a separate private
repository.

## Two-Phase Workflow

- Phase 1: research, source review, and public notes in this repository.
- Phase 2: optional private sync into an OpenFarmPlanner project using
  `PHASE2_PROMPT.md` or project-specific tooling outside this public repo.
  This includes an optional, admin-only sub-flow for writing official crop
  species metadata (synonyms, regional names, proposals) directly — see
  `docs/crop-species-api.md`. It uses a separate credential from the
  Culture sync token and is never part of the default Phase 2 flow unless
  explicitly requested.

Do not write to a live API during Phase 1.

Do not create a parallel private research note when the information is reusable.
Research improvements belong here first. Private files are only for credentials,
temporary sync logs, project-specific IDs, or information that cannot be made
public safely.

## Language

All public content is English by default:

- documentation
- templates
- crop notes
- examples
- commit messages

Localized crop names may be included in parentheses when helpful.

## Copyright And Source Style

Do not copy source text verbatim or preserve promotional source wording. Facts,
numbers, and variety characteristics must be paraphrased in plain, neutral
language.

When a source is mentioned in flowing text, write the source name as a direct
Markdown link, for example:
`[ReinSaat](https://example.org/source)`.

Do not use footnote markers for source references. Avoid bare source names when
the reader may not know whether the name refers to a person, company, or
publication.

## Explicit, Not Silent

Source conflicts, identity questions, duplicate suspects, and mapping questions
must always be documented explicitly in the note. Do not make a silent choice
when the correct source, crop identity, or OpenFarmPlanner field is unclear.

## Use Precise Crop Identities

Do not use broad supplier or shop categories as crop identities when they mix
multiple botanical groups, harvest forms, or crop-calendar logic. Slash names
such as "Asian leaf vegetables/mustard cabbage" may be useful source context,
but they must not silently become the OpenFarmPlanner crop name when a more
specific crop identity is supported by the sources.

Prefer the narrowest reusable crop identity that fits the botanical evidence
and the intended harvest logic. Document the discarded broad category and the
reason it was not used when the source could otherwise be misread as the crop
name.

## Task Guides

Read only the guide for the task at hand. Each guide adds rules on top of this
file.

| Task | Read first | Skill |
| --- | --- | --- |
| Research or edit a general crop or variety note (Phase 1) | [`docs/rules/crop-research.md`](docs/rules/crop-research.md), [`templates/crop-note.md`](templates/crop-note.md) | `research-crop-note` |
| Name, translate, or import official crop species | [`docs/rules/crop-species-naming.md`](docs/rules/crop-species-naming.md) | `import-crop-species-list` (crop lists), `grin-species-batch` (GRIN) |
| Sync approved notes into a project's Cultures (Phase 2) | [`PHASE2_PROMPT.md`](PHASE2_PROMPT.md), [`docs/private-sync.md`](docs/private-sync.md), [`docs/culture-field-mapping.md`](docs/culture-field-mapping.md) | `phase2-culture-sync` |
| Write official crop species metadata (Phase 2, admin only) | [`PHASE2_SPECIES_PROMPT.md`](PHASE2_SPECIES_PROMPT.md), [`docs/crop-species-api.md`](docs/crop-species-api.md), [`docs/rules/crop-species-naming.md`](docs/rules/crop-species-naming.md) | `phase2-species-sync` |

## Commits

Use English commit messages. Keep commits focused by crop, research session, or
workflow change.
