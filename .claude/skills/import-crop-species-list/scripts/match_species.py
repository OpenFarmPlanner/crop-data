"""List the distinct crop names of a crop list and the species each already matches.

Usage: python3 -I match_species.py <file.xlsx|file.csv|file.txt|-> --env <env> --out <dir>
       [--name-col Name] [--variety-col Sorte]

Reads xlsx without third-party packages (first worksheet only). A .txt file or
`-` (stdin) is a plain list typed by the user: one crop per line, optionally
followed by varieties after ":" or ";" (comma-separated), e.g.
`Spinat: Malabarspinat, Butterflay`. Bullet markers are ignored.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ofp_species import fetch_all_species, load_env, name_index, norm  # noqa: E402

NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def read_xlsx(path: Path) -> list[list[str]]:
    with zipfile.ZipFile(path) as zf:
        shared = []
        if 'xl/sharedStrings.xml' in zf.namelist():
            root = ElementTree.fromstring(zf.read('xl/sharedStrings.xml'))
            shared = [''.join(t.text or '' for t in si.iter(f"{{{NS['m']}}}t")) for si in root.findall('m:si', NS)]
        sheet = sorted(n for n in zf.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n))[0]
        root = ElementTree.fromstring(zf.read(sheet))
    rows = []
    for row in root.iter(f"{{{NS['m']}}}row"):
        cells: dict[int, str] = {}
        for c in row.findall('m:c', NS):
            col = 0
            for ch in re.match(r'[A-Z]+', c.get('r')).group():
                col = col * 26 + ord(ch) - 64
            v = c.find('m:v', NS)
            if c.get('t') == 's' and v is not None:
                val = shared[int(v.text)]
            elif c.get('t') == 'inlineStr':
                val = ''.join(t.text or '' for t in c.iter(f"{{{NS['m']}}}t"))
            else:
                val = v.text if v is not None else ''
            cells[col - 1] = val or ''
        rows.append([cells.get(i, '') for i in range(max(cells, default=-1) + 1)])
    return rows


def read_plain_list(text: str) -> list[list[str]]:
    """Turn a typed list into rows of [Name, Sorte] (one row per variety)."""
    rows = [['Name', 'Sorte']]
    for line in text.splitlines():
        line = re.sub(r'^\s*(?:[-*•]|\d+[.)])\s*', '', line).strip()
        if not line:
            continue
        name, rest = (re.split(r'[:;\t]', line, maxsplit=1) + [''])[:2]
        varieties = [v.strip() for v in rest.split(',') if v.strip()]
        rows += [[name.strip(), v] for v in varieties] or [[name.strip(), '']]
    return rows


def read_rows(path: Path) -> list[list[str]]:
    if str(path) == '-':
        return read_plain_list(sys.stdin.read())
    if path.suffix.lower() in ('.txt', '.md'):
        return read_plain_list(path.read_text(encoding='utf-8'))
    if path.suffix.lower() in ('.xlsx', '.xlsm'):
        return read_xlsx(path)
    text = path.read_text(encoding='utf-8-sig')
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=',;\t')
    except csv.Error:  # a single column has no delimiter to detect
        dialect = csv.excel
    return list(csv.reader(text.splitlines(), dialect=dialect))


NAME_COLUMNS = ['Name', 'Kultur', 'Kulturart', 'Crop', 'Crop name', 'Gemüse', 'Pflanze']
VARIETY_COLUMNS = ['Sorte', 'Sorten', 'Variety', 'Varieties', 'Sortenname']


def find_column(header: list[str], candidates: list[str]) -> int | None:
    for name in candidates:
        if name.lower() in header:
            return header.index(name.lower())
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('file', type=Path)
    ap.add_argument('--env', required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--name-col', default='Name')
    ap.add_argument('--variety-col', default='Sorte')
    args = ap.parse_args()

    rows = read_rows(args.file)
    header = [h.strip().lower() for h in rows[0]]
    ni = find_column(header, [args.name_col, *NAME_COLUMNS])
    if ni is None:
        ni, rows = 0, [[''], *rows]  # no known header: first column, every row is data
        print('No name column found; using the first column without a header row.', file=sys.stderr)
    vi = find_column(header, [args.variety_col, *VARIETY_COLUMNS])
    groups: dict[str, list[str]] = {}
    for row in rows[1:]:
        name = (row[ni] if ni < len(row) else '').strip()
        if not name:
            continue
        variety = (row[vi] if vi is not None and vi < len(row) else '').strip()
        groups.setdefault(name, []).append(variety)

    api, token = load_env(args.env)
    species = fetch_all_species(api, token)
    index = name_index(species)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / 'species-snapshot.json').write_text(json.dumps(species, ensure_ascii=False, indent=1))

    lines = ['status\tname\trows\tmatches\tvarieties']
    for name in sorted(groups, key=norm):
        hits = sorted(index.get(norm(name), ()))
        varieties = sorted({v for v in groups[name] if v})
        lines.append(f"{'MATCH' if hits else 'NONE'}\t{name}\t{len(groups[name])}\t{'; '.join(hits)}\t{'; '.join(varieties)}")
    (args.out / 'name-match.tsv').write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    matched = sum(1 for line in lines[1:] if line.startswith('MATCH'))
    print(f'\n{len(groups)} names, {matched} match, {len(groups) - matched} without a species; {len(species)} species loaded', file=sys.stderr)


if __name__ == '__main__':
    main()
