"""Shared helpers for the crop-species import scripts (stdlib only)."""
from __future__ import annotations

import json
import re
import subprocess
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
ENV_FILE = REPO_ROOT / '.openfarmplanner.env'
LANGUAGES = ('de', 'en', 'fr', 'es')


def load_env(env: str) -> tuple[str, str]:
    """Source the git-ignored env file for one environment and return API base and crop-library token."""
    out = subprocess.run(
        ['bash', '-c', f'source "{ENV_FILE}" "$1" >/dev/null && printf "%s\\n%s" "$OFP_API" "$OFP_CROP_LIBRARY_TOKEN"', '_', env],
        capture_output=True, text=True, check=True,
    ).stdout.split('\n')
    api, token = (out + ['', ''])[:2]
    if not api or not token:
        raise SystemExit(f'No OFP_API / OFP_CROP_LIBRARY_TOKEN for env {env!r} in {ENV_FILE}')
    return api.rstrip('/'), token


def request(api: str, token: str, method: str, path: str, body: dict | None = None) -> tuple[int, object]:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        path if path.startswith('http') else f'{api}{path}',
        data=data, method=method,
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'Accept': 'application/json',
                 'User-Agent': 'openfarmplanner-crop-data/import-crop-species-list'},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read() or b'null')
    except urllib.error.HTTPError as err:
        raw = err.read()
        try:
            return err.code, json.loads(raw)
        except ValueError:
            return err.code, raw.decode(errors='replace')


def fetch_all_species(api: str, token: str) -> list[dict]:
    url, items = '/crop-species/?include_proposed=true&page_size=500', []
    while url:
        status, page = request(api, token, 'GET', url)
        if status != 200:
            raise SystemExit(f'GET crop-species failed: {status} {page}')
        if isinstance(page, list):
            return page
        items += page['results']
        url = page.get('next')
    return items


def norm(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', str(text)).strip().lower())


def name_index(species: list[dict]) -> dict[str, set[str]]:
    """Map every normalized common name, synonym and regional name to 'Species (lang, status)' labels."""
    index: dict[str, set[str]] = {}
    for sp in species:
        for tr in sp['translations']:
            names = [tr['common_name'], *tr['synonyms'], *tr.get('regional_names', {}).values()]
            for name in names:
                if name:
                    index.setdefault(norm(name), set()).add(f"{sp['name']} ({tr['language_code']}, {sp['status']})")
    return index
