"""Dry-run or apply scientific names on existing crop species.

Plan format: {"<species id>": {"name": "<species name>", "scientific_name": "<new>", "replace": false, "flag": "..."}}
Only empty live values are filled unless the entry sets "replace": true.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ofp_species import fetch_all_species, load_env, request  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('plan', type=Path)
    ap.add_argument('--env', required=True)
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    plan = json.loads(args.plan.read_text())
    api, token = load_env(args.env)
    live = {str(s['id']): s for s in fetch_all_species(api, token)}

    changes = {}
    for sid, entry in plan.items():
        sp = live.get(sid)
        if sp is None or sp['name'] != entry['name']:
            raise SystemExit(f"Species {sid} {entry['name']!r} not found or renamed (live: {sp and sp['name']!r})")
        old, new = sp['scientific_name'], entry['scientific_name']
        if old == new:
            continue
        if old and not entry.get('replace'):
            print(f"SKIP {entry['name']}: live {old!r} kept (plan {new!r} without replace)")
            continue
        changes[sid] = new
        flag = f"  [{entry['flag']}]" if entry.get('flag') else ''
        print(f"{entry['name']}: {old!r} -> {new!r}{flag}")
    print(f'\n{len(changes)} change(s)')

    if not args.apply:
        print('Dry run only. Re-run with --apply after the user approved this diff.')
        return

    with args.plan.with_name('apply-log.jsonl').open('a', encoding='utf-8') as log:
        for sid, new in changes.items():
            status, payload = request(api, token, 'PATCH', f'/crop-species/{sid}/', {'scientific_name': new})
            _, after = request(api, token, 'GET', f'/crop-species/{sid}/')
            ok = isinstance(after, dict) and after.get('scientific_name') == new
            log.write(json.dumps({'time': time.strftime('%Y-%m-%dT%H:%M:%S'), 'action': 'PATCH_SCIENTIFIC_NAME',
                                  'id': sid, 'name': plan[sid]['name'], 'value': new, 'status': status,
                                  'readback_ok': ok, 'response': payload}, ensure_ascii=False) + '\n')
            print(f"PATCH {plan[sid]['name']}: {status}{'' if ok else '  READBACK MISMATCH'}")


if __name__ == '__main__':
    main()
