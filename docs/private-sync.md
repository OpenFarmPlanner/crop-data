# Private Sync Guide

This repository can be used as the public source for crop research while still
supporting private OpenFarmPlanner sync work.

## Local Setup

Create a local `.openfarmplanner.env` file when API access is needed. The file
is ignored by git and must never be committed.

Use `sync-private/` for temporary logs, API readbacks, diffs, or project-specific
notes. This directory is ignored by git.

## What To Commit

Commit:

- source-backed crop facts
- planning-value derivations
- source conflicts
- mapping questions that are generally useful
- template or workflow improvements

Do not commit:

- API tokens
- private project names
- production IDs
- token scopes
- raw API responses from private projects
- live sync logs

## After A Live Sync

If the sync revealed a reusable issue, such as a missing derivation rule or a
better source, update the public note or documentation. If the sync only
produced project-specific operational details, keep it in `sync-private/`.
