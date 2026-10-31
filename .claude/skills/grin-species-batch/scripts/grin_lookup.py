"""Accepted status of each given name in GRIN (follows synonyms).
Usage: grin_lookup.py <grin-data-dir> "Genus species" ...
"""
import csv, sys, re, collections
csv.field_size_limit(10**9)
d = sys.argv[1]; qs = [q.lower() for q in sys.argv[2:]]
taxa, cur = {}, {}
for r in csv.DictReader(open(f"{d}/taxonomy_species.txt", encoding="utf-8-sig"), delimiter="\t", quoting=csv.QUOTE_NONE):
    taxa[r["taxonomy_species_id"]] = re.sub(r"<[^>]+>", "", r["name"]); cur[r["taxonomy_species_id"]] = r["current_taxonomy_species_id"]
de = collections.defaultdict(list)
for r in csv.DictReader(open(f"{d}/taxonomy_common_name.txt", encoding="utf-8-sig"), delimiter="\t", quoting=csv.QUOTE_NONE):
    if r["language_description"] in ("German", "English"): de[r["taxonomy_species_id"]].append(r["name"])
for q in qs:
    hits = [t for t, n in taxa.items() if n.lower() == q] or [t for t, n in taxa.items() if n.lower().startswith(q + " ")][:8]
    if not hits: print(f"{q}: -- not found"); continue
    for t in hits:
        acc = "ACCEPTED" if cur[t] == t else f"-> {taxa.get(cur[t])}"
        print(f"{taxa[t]}: {acc} | {', '.join(de[cur[t]][:6])}")
