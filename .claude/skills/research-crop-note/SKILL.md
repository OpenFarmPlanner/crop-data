---
name: research-crop-note
description: Research or update a public crop note or variety note in notes/ (Phase 1) for OpenFarmPlanner - general crop facts, variety values, sowing, spacing, growth duration, harvest window, yield, sources. Use when the user asks to research a crop or a variety ("recherchiere Sorte X", "neue Kultur", "Kulturnotiz"), to fill or check planning values, or to compare a variety with its general crop. Not for naming or importing official crop species (use import-crop-species-list or grin-species-batch) and not for writing to a live API.
argument-hint: "[crop or variety name]"
---

# Research a crop or variety note

Phase 1 only: research and public notes in this repository. Never write to a
live API in this skill.

Read first:

- [`docs/rules/crop-research.md`](../../../docs/rules/crop-research.md): rules
  for variety comparison, general crop data, planning values, yield units,
  calendar values, field constraints, live notes.
- [`templates/crop-note.md`](../../../templates/crop-note.md): note structure.
- [`docs/culture-field-mapping.md`](../../../docs/culture-field-mapping.md):
  which OpenFarmPlanner field a value maps to.

## Steps

1. **Fix the crop identity.** Find the existing general crop note in `notes/`
   (`<crop>.md`) and the variety note (`<crop>-<variety>.md`), if any. Use the
   narrowest reusable crop identity (see "Use Precise Crop Identities" in
   `CLAUDE.md`). If the identity is unclear, stop and document it as an
   identity question instead of creating a note.
2. **General crop first.** If the general crop note is missing or thin,
   research it before the variety: reliable facts, source ranges, open
   uncertainties. Leave a structured value open when varieties or crop cycles
   differ too much for one value, and say why.
3. **Research the variety independently** from variety-specific sources
   (breeder, seed suppliers, trials). Do not copy general values silently.
4. **Compare explicitly** in `Comparison With General Crop Data`: each value
   is either a sourced deviation or an intentional reuse of the general
   value, written out as such.
5. **Derive planning values** only with source basis, calculation, rounding
   and uncertainty in `Planning Value Derivations`. Respect integer-only
   fields; keep yield units consistent within the crop.
6. **Sources:** paraphrase, never copy promotional text; link each source
   name directly in Markdown, no footnotes; no prices or availability text.
7. **Research Status:** list what is verified, what was reused, and every open
   research, identity, or mapping question.
8. **Public-first check** before committing: no tokens, project names,
   production IDs, or sync logs. Commit in English, one focused commit per
   crop or research session.

A live sync of the finished note is a separate step (Phase 2,
[`PHASE2_PROMPT.md`](../../../PHASE2_PROMPT.md)) and only on explicit request.
