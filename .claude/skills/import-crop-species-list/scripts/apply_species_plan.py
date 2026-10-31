"""Dry-run or apply a crop-species plan (new species + synonym patches).

Usage: python3 -I apply_species_plan.py <plan.json> --env <env> [--apply]

Plan format: {"new": [{"body": <POST body>, ...}], "patch": {"<species name>": {"<lang>": [synonyms to add]}}}
Without --apply nothing is written; the script prints collisions and the diff.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ofp_species import LANGUAGES, fetch_all_species, load_env, name_index, norm, request  # noqa: E402


def collisions(plan: dict, index: dict[str, set[str]]) -> list[str]:
    found = []
    for entry in plan.get('new', []):
        body = entry['body']
        langs = {t['language_code'] for t in body['translations'] if t.get('common_name')}
        if missing := [code for code in LANGUAGES if code not in langs]:
            found.append(f"{body['name']}: missing languages {missing}")
        for tr in body['translations']:
            hit = index.get(norm(tr['common_name']))
            if hit:
                found.append(f"COMMON NAME {body['name']} [{tr['language_code']}] '{tr['common_name']}' already on {sorted(hit)}")
            for syn in tr['synonyms']:
                if hit := index.get(norm(syn)):
                    found.append(f"shared synonym {body['name']} [{tr['language_code']}] '{syn}' also on {sorted(hit)}")
    return found


def patched_translations(species: dict, additions: dict[str, list[str]]) -> list[dict]:
    """Full translation entries for the patched languages, with merged synonyms (nothing removed)."""
    by_lang = {t['language_code']: t for t in species['translations']}
    result = []
    for lang, extra in additions.items():
        current = by_lang.get(lang)
        if current is None:
            raise SystemExit(f"{species['name']}: no {lang} translation to patch")
        known = {norm(s) for s in current['synonyms']} | {norm(current['common_name'])}
        merged = current['synonyms'] + [s for s in extra if norm(s) not in known]
        if merged != current['synonyms']:
            result.append({
                'language_code': lang,
                'common_name': current['common_name'],
                'synonyms': merged,
                'regional_names': current.get('regional_names') or {},
            })
    return result


def restore(args: argparse.Namespace, plan: dict, api: str, token: str) -> None:
    """Re-add planned synonyms and regional names to species created by --apply.

    The UI approval dialog sends only de/en common names, and the API replaces
    a sent language wholesale, so approval clears de/en synonyms and regional
    names. Species ids come from the POST responses in apply-log.jsonl because
    approval also renames the record. Live common names (possibly edited by
    the moderator) are kept; nothing is removed.
    """
    log_path = args.plan.with_name('apply-log.jsonl')
    ids = {}
    for line in log_path.read_text(encoding='utf-8').splitlines():
        item = json.loads(line)
        if item['action'] == 'POST' and item['status'] in (200, 201):
            ids[item['name']] = item['response']['id']
    for entry in plan.get('new', []):
        name = entry['body']['name']
        if name not in ids:
            print(f'{name}: no POST in {log_path.name}, skipped')
            continue
        _, live = request(api, token, 'GET', f'/crop-species/{ids[name]}/?include_proposed=true')
        if live.get('status') != 'published':
            print(f"{name}: still {live.get('status')}, skipped")
            continue
        live_by_lang = {t['language_code']: t for t in live['translations']}
        changes = []
        for planned in entry['body']['translations']:
            current = live_by_lang.get(planned['language_code'])
            if current is None:
                changes.append(planned)
                continue
            known = {norm(s) for s in current['synonyms']}
            synonyms = current['synonyms'] + [s for s in planned['synonyms'] if norm(s) not in known]
            regional = {**planned.get('regional_names', {}), **(current.get('regional_names') or {})}
            if synonyms != current['synonyms'] or regional != (current.get('regional_names') or {}):
                changes.append({'language_code': current['language_code'], 'common_name': current['common_name'],
                                'synonyms': synonyms, 'regional_names': regional})
        if not changes:
            print(f'{name}: complete')
            continue
        for tr in changes:
            print(f"{name} [{tr['language_code']}]: -> {tr['synonyms']} {tr.get('regional_names') or ''}")
        if args.apply:
            status, payload = request(api, token, 'PATCH', f"/crop-species/{ids[name]}/", {'translations': changes})
            print(f'  PATCH {status}')
            with log_path.open('a', encoding='utf-8') as log:
                log.write(json.dumps({'time': time.strftime('%Y-%m-%dT%H:%M:%S'), 'action': 'RESTORE', 'name': name,
                                      'status': status, 'response': payload}, ensure_ascii=False) + '\n')
    if not args.apply:
        print('\nDry run only. Add --apply to write.')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('plan', type=Path)
    ap.add_argument('--env', required=True)
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--restore', action='store_true',
                    help='after moderator approval: put back planned synonyms/regional names the approval dropped')
    args = ap.parse_args()

    plan = json.loads(args.plan.read_text())
    api, token = load_env(args.env)
    if args.restore:
        restore(args, plan, api, token)
        return
    species = fetch_all_species(api, token)
    by_name = {s['name']: s for s in species}
    index = name_index(species)

    print('== Collisions ==')
    issues = collisions(plan, index)
    print('\n'.join(issues) or 'none')
    if args.apply and any(i.startswith('COMMON NAME') or 'missing languages' in i for i in issues):
        raise SystemExit('Resolve common-name collisions and missing languages before --apply.')

    print(f"\n== New species ({len(plan.get('new', []))}) ==")
    for entry in plan.get('new', []):
        print(json.dumps(entry['body'], ensure_ascii=False))

    patches = {}
    print(f"\n== Synonym patches ({len(plan.get('patch', {}))}) ==")
    for name, additions in plan.get('patch', {}).items():
        if name not in by_name:
            raise SystemExit(f'Species to patch not found: {name}')
        translations = patched_translations(by_name[name], additions)
        if translations:
            patches[name] = translations
            for tr in translations:
                old = next(t['synonyms'] for t in by_name[name]['translations'] if t['language_code'] == tr['language_code'])
                print(f"{name} [{tr['language_code']}]: {old} -> {tr['synonyms']}")
        else:
            print(f'{name}: already up to date')

    if not args.apply:
        print('\nDry run only. Re-run with --apply after the user approved this diff.')
        return

    log = args.plan.with_name('apply-log.jsonl').open('a', encoding='utf-8')

    def record(action: str, name: str, status: int, payload: object) -> None:
        log.write(json.dumps({'time': time.strftime('%Y-%m-%dT%H:%M:%S'), 'action': action, 'name': name,
                              'status': status, 'response': payload}, ensure_ascii=False) + '\n')
        log.flush()
        print(f'{action} {name}: {status}')

    for entry in plan.get('new', []):
        status, payload = request(api, token, 'POST', '/crop-species/', entry['body'])
        record('POST', entry['body']['name'], status, payload)
    for name, translations in patches.items():
        sid = by_name[name]['id']
        status, payload = request(api, token, 'PATCH', f'/crop-species/{sid}/', {'translations': translations})
        record('PATCH', name, status, payload)
        _, after = request(api, token, 'GET', f'/crop-species/{sid}/')
        for tr in translations:
            live = next((t for t in after['translations'] if t['language_code'] == tr['language_code']), {})
            if live.get('synonyms') != tr['synonyms']:
                print(f"  READBACK MISMATCH {name} [{tr['language_code']}]: {live.get('synonyms')}")


if __name__ == '__main__':
    main()
