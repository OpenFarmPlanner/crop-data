---
name: phase2-culture-sync
description: Copy approved public crop and variety notes from this repository into a private OpenFarmPlanner project's Culture records (Phase 2 sync) - growth duration, harvest window, spacing, yield, seed weight, live notes. Use when the user asks to sync, push, or "live schalten" researched crops into their project ("in mein Projekt übernehmen", "Phase 2", "sync to OpenFarmPlanner"). Not for official crop species names (use phase2-species-sync or import-crop-species-list) and not for research.
argument-hint: "[crop or variety names]"
---

# Phase 2: sync approved notes into project Cultures

Follow [`PHASE2_PROMPT.md`](../../../PHASE2_PROMPT.md) step by step; it holds
the rules and the sync sequence. Also read
[`docs/openfarmplanner-api.md`](../../../docs/openfarmplanner-api.md),
[`docs/culture-field-mapping.md`](../../../docs/culture-field-mapping.md) and
[`docs/private-sync.md`](../../../docs/private-sync.md), and the "Live Notes
With Sources" and "Respect Field And Form Constraints" sections of
[`docs/rules/crop-research.md`](../../../docs/rules/crop-research.md).

On top of the prompt:

- Only on explicit request. Before any write, show the user the full diff per
  record (field, live value, new value, source note) and wait for an explicit
  OK. Approval for one batch does not cover the next.
- The target project and environment come from the local, git-ignored
  `.openfarmplanner.env` and the user; never write them into public files.
- If the auto-mode classifier blocks a write, do not retry; hand the exact
  command to the user.
- Logs, pre-write snapshots and read-backs go to `sync-private/`. Public notes
  get no sync reports (no project names, field names with before/after values,
  or sync dates); update a note only when the sync taught something reusable
  about the crop.
