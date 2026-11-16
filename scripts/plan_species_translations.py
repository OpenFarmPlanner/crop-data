#!/usr/bin/env python3
"""Validate public research and prepare a private translation diff; never call an API."""
from __future__ import annotations

import argparse
import copy
import csv
import json
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

LANGUAGES = ('it', 'pt', 'nl')
RESEARCH = Path(__file__).resolve().parents[1] / 'data/crop-species-names-it-pt-nl.csv'
FIELDS = {
    'german_name', 'scientific_name', 'language_code', 'common_name',
    'synonyms', 'status', 'sources', 'candidates', 'note',
}


def normalized(value: str) -> str:
    return unicodedata.normalize('NFC', ' '.join(value.split())).casefold()


def identity(german_name: str, scientific_name: str) -> tuple[str, str]:
    # A botanical name alone does not distinguish harvest/use forms.
    return normalized(german_name), normalized(scientific_name)


def string_list(value: object, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
        raise ValueError(f'{field} must be a list of nonempty strings')
    return value


def load_research(path: Path = RESEARCH) -> list[dict]:
    with path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        if set(reader.fieldnames or ()) != FIELDS:
            raise ValueError('Unexpected research columns')
        rows = list(reader)
    seen = set()
    languages_by_identity: dict[tuple[str, str], set[str]] = {}
    preferred = {}
    for row in rows:
        if any(not isinstance(row.get(f), str) for f in FIELDS):
            raise ValueError('Malformed research row')
        for f in ('german_name', 'scientific_name', 'note'):
            if not row[f].strip():
                raise ValueError(f'Missing {f}')
        key = identity(row['german_name'], row['scientific_name'])
        language = row['language_code']
        if language not in LANGUAGES or (key, language) in seen:
            raise ValueError('Unsupported language or duplicate research identity/language')
        seen.add((key, language))
        languages_by_identity.setdefault(key, set()).add(language)
        for f in ('synonyms', 'sources', 'candidates'):
            row[f] = string_list(json.loads(row[f]), f)
        if not row['sources'] or any(
            urlparse(source).scheme != 'https' or not urlparse(source).netloc
            for source in row['sources']
        ):
            raise ValueError('Every research row needs direct HTTPS evidence or a documented search')
        if row['status'] not in ('reviewed', 'unresolved'):
            raise ValueError('Unknown review status')
        if row['status'] == 'unresolved':
            if row['common_name'] or row['synonyms']:
                raise ValueError('Unresolved candidates must never be writable names or aliases')
        else:
            if not row['common_name'].strip():
                raise ValueError('Reviewed row lacks a common name')
            name_key = (language, normalized(row['common_name']))
            if name_key in preferred and preferred[name_key] != key:
                raise ValueError('A reviewed common name identifies multiple crop identities')
            preferred[name_key] = key
            aliases = [normalized(a) for a in row['synonyms']]
            if len(set(aliases)) != len(aliases) or normalized(row['common_name']) in aliases:
                raise ValueError('Duplicate reviewed aliases')
    if not rows or any(languages != set(LANGUAGES) for languages in languages_by_identity.values()):
        raise ValueError('Each identity must have a review or exception in all three languages')
    return rows


def coverage(rows: list[dict]) -> dict:
    return {
        'species': len({identity(r['german_name'], r['scientific_name']) for r in rows}),
        'languages': {
            language: dict(Counter(r['status'] for r in rows if r['language_code'] == language))
            for language in LANGUAGES
        },
    }


def build_plan(rows: list[dict], snapshot: list[dict], enabled_languages: list[str]) -> dict:
    enabled = set(enabled_languages)
    if not enabled or not enabled <= set(LANGUAGES):
        raise ValueError('Explicitly select only languages verified as enabled in the deployed API')
    if not isinstance(snapshot, list):
        raise ValueError('Snapshot must be the complete, pagination-flattened published catalogue list')
    live = {}
    ids = set()
    existing_names = {}
    for species in snapshot:
        if species.get('status') != 'published':
            raise ValueError('Snapshot must contain published species only')
        if not species.get('id') or species['id'] in ids:
            raise ValueError('Missing or duplicate live species ID')
        ids.add(species['id'])
        translations = species.get('translations', [])
        if len({t['language_code'] for t in translations}) != len(translations):
            raise ValueError('Duplicate live translation language')
        german = next((t['common_name'] for t in translations if t['language_code'] == 'de'), '')
        if not german.strip() or not species.get('scientific_name', '').strip():
            raise ValueError('Live identity lacks German or scientific name')
        key = identity(german, species['scientific_name'])
        if key in live:
            raise ValueError('Live catalogue contains duplicate German/scientific identities')
        live[key] = species
        for t in translations:
            if t['language_code'] in enabled and t.get('common_name'):
                existing_names.setdefault((t['language_code'], normalized(t['common_name'])), set()).add(key)
    research_keys = {identity(r['german_name'], r['scientific_name']) for r in rows}
    if research_keys != set(live):
        raise ValueError(
            f'Catalogue coverage changed: {len(set(live) - research_keys)} unresearched, '
            f'{len(research_keys - set(live))} missing or changed identities. Refresh research before planning.'
        )
    by_species: dict[tuple[str, str], list[dict]] = {}
    exceptions = []
    for row in rows:
        key = identity(row['german_name'], row['scientific_name'])
        if row['status'] != 'reviewed':
            exceptions.append({k: copy.deepcopy(row[k]) for k in (
                'german_name', 'scientific_name', 'language_code', 'sources', 'note',
            )})
            continue
        if row['language_code'] not in enabled:
            continue
        if existing_names.get((row['language_code'], normalized(row['common_name'])), set()) - {key}:
            raise ValueError('Reviewed common name collides with another live crop in the same language')
        by_species.setdefault(key, []).append(row)
    patches = []
    unchanged = 0
    for key, research in by_species.items():
        species = live[key]
        translations = {t['language_code']: t for t in species['translations']}
        changes = []
        for row in research:
            language = row['language_code']
            before = translations.get(language)
            aliases = string_list(copy.deepcopy(before.get('synonyms', [])) if before else [], 'live synonyms')
            alias_keys = {normalized(a) for a in aliases}
            for alias in row['synonyms']:
                if normalized(alias) not in alias_keys:
                    aliases.append(alias)
                    alias_keys.add(normalized(alias))
            regions = copy.deepcopy(before.get('regional_names', {})) if before else {}
            if not isinstance(regions, dict):
                raise ValueError('Live regional_names must be an object')
            after = {
                'language_code': language, 'common_name': row['common_name'],
                'synonyms': aliases, 'regional_names': regions,
            }
            if before and all(before.get(k) == v for k, v in after.items()):
                unchanged += 1
                continue
            changes.append(after)
        if changes:
            patches.append({
                'id': species['id'],
                'german_name': next(t['common_name'] for t in species['translations'] if t['language_code'] == 'de'),
                'scientific_name': species['scientific_name'],
                # Private review/optimistic precondition: a writer must GET again
                # and compare this immediately before any authorized PATCH.
                'before': copy.deepcopy(species),
                'patch': {'translations': changes},
            })
    return {
        'mode': 'review-only',
        'enabled_languages': sorted(enabled),
        'coverage': coverage(rows),
        'unchanged_translations': unchanged,
        'patches': patches,
        'unresolved': exceptions,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--research', type=Path, default=RESEARCH)
    parser.add_argument('--snapshot', type=Path, help='Private, fresh complete published catalogue JSON list')
    parser.add_argument('--enabled-languages', nargs='+', choices=LANGUAGES)
    parser.add_argument('--out', type=Path, help='Private output path, normally under sync-private/')
    args = parser.parse_args()
    try:
        rows = load_research(args.research)
        if args.snapshot is None:
            if args.out or args.enabled_languages:
                parser.error('--out and --enabled-languages require --snapshot')
            print(json.dumps(coverage(rows), ensure_ascii=False, indent=2))
            return
        if not args.out or not args.enabled_languages:
            parser.error('--snapshot requires --out and --enabled-languages')
        # Keep operational IDs and before-images out of the public tree.
        private_root = Path(__file__).resolve().parents[1] / 'sync-private'
        if not args.out.resolve().is_relative_to(private_root.resolve()):
            raise ValueError('Plan output must be inside the git-ignored sync-private directory')
        if args.out.resolve() in (args.snapshot.resolve(), args.research.resolve()):
            raise ValueError('Output must not overwrite an input')
        plan = build_plan(rows, json.loads(args.snapshot.read_text(encoding='utf-8')), args.enabled_languages)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({
            **plan['coverage'], 'species_to_patch': len(plan['patches']),
            'translations_to_patch': sum(len(p['patch']['translations']) for p in plan['patches']),
            'unchanged_translations': plan['unchanged_translations'],
            'mode': plan['mode'],
        }, indent=2))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f'Cannot prepare plan: {error}\n')


if __name__ == '__main__':
    main()
