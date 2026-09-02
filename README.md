# OpenFarmPlanner Crop Data

Primary public research workspace for reusable OpenFarmPlanner crop data.

This repository is the source of truth for crop-data improvements that should
be reusable by the OpenFarmPlanner community. It documents crop facts, sources,
planning-value derivations, and open questions before data is copied into an
OpenFarmPlanner instance.

It is intentionally source-focused: no private project IDs, no API tokens, no
live sync logs, and no environment-specific production history belong here.

## Repository Layout

- `templates/crop-note.md` - canonical template for crop and variety notes.
- `notes/` - public crop research notes in English.
- `examples/` - completed example notes that demonstrate the expected style.
- `docs/culture-field-mapping.md` - mapping between note concepts and
  OpenFarmPlanner Culture fields.
- `PHASE2_PROMPT.md` - optional prompt for copying approved notes into a private
  OpenFarmPlanner project. Keep live credentials and sync logs outside this
  public repository.

## Workflow

1. Research the general crop first.
2. Research each variety independently.
3. Compare variety values against the general crop values explicitly.
4. Document source conflicts and unclear field mappings instead of deciding
   silently.
5. Commit reusable research changes here first.
6. Only copy data into a live OpenFarmPlanner project in a separate private
   sync step.

## Private Sync Without A Private Research Repo

This public repository is intended to replace the old private research repo for
ongoing crop-data work. Keep private operational state local and ignored:

- create `.openfarmplanner.env` locally when you need API access
- write temporary sync logs under `sync-private/`
- do not commit production IDs, project names, token scopes, or private sync
  reports
- after a sync, update public notes only when the change improves reusable crop
  knowledge

## Data Principles

- Prefer reputable horticultural, agricultural, breeding, or seed-supplier
  sources.
- Paraphrase source text. Do not copy marketing copy or long passages.
- Link sources directly in the text and in the source list.
- Document derived values: source basis, calculation, rounding, and uncertainty.
- Keep yield units consistent within one crop whenever possible.
- Do not put private project names, production IDs, token scopes, or sync logs
  into public notes.

## Language

All public repository content is written in English. Localized crop names may be
mentioned when useful, but the note itself should remain readable to an English
speaker.

## Private Sync Work

If you use this repository to maintain a private OpenFarmPlanner project, keep
the following outside git or in a private companion repository:

- `.openfarmplanner.env`
- live API tokens
- project names and IDs
- production IDs
- sync reports
- private correction logs

The `.gitignore` already excludes common private sync locations.

## Historical Private Repository

Older project-specific sync history may exist in a private repository. That
history is not required for new public research work and should not be copied
here unless it has been reviewed, translated to English, and stripped of private
operational details.

## License

This repository is licensed under the GNU Affero General Public License v3.0.
See [`LICENSE`](LICENSE) for the full license text.
