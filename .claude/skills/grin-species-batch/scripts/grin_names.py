"""GRIN accepted name, family and de/fr/es common names for each given taxon.
Usage: grin_names.py <grin-data-dir> "Genus species" ...
"""
import csv, sys, re, collections
csv.field_size_limit(10**9)
d = sys.argv[1]; qs = sys.argv[2:]
def rows(n): return csv.DictReader(open(f"{d}/{n}.txt", encoding="utf-8-sig"), delimiter="\t", quoting=csv.QUOTE_NONE)
taxa, cur, gen = {}, {}, {}
for r in rows("taxonomy_species"):
    t = r["taxonomy_species_id"]; taxa[t] = re.sub(r"<[^>]+>", "", r["name"]); cur[t] = r["current_taxonomy_species_id"]; gen[t] = r["taxonomy_genus_id"]
fam = {r["taxonomy_family_id"]: r["family_name"] for r in rows("taxonomy_family")}
gfam = {r["taxonomy_genus_id"]: fam.get(r["taxonomy_family_id"], "") for r in rows("taxonomy_genus")}
by = collections.defaultdict(list)
for t, n in taxa.items(): by[n.lower()].append(t)
L = {"German": "de", "English": "en", "French": "fr", "Spanish": "es"}
nm = collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows("taxonomy_common_name"):
    s = r["taxonomy_species_id"]; l = L.get(r["language_description"].split(" (")[0])
    if s != "\\N" and l: nm[cur.get(s, s)][l].append(r["name"])
for q in qs:
    ts = by.get(q.lower())
    if not ts: print(f"!! {q}: NOT FOUND"); continue
    t = cur[ts[0]]; acc = "" if t == ts[0] else f" (-> {taxa[t]})"
    print(f"{q}{acc} [{gfam.get(gen[t], '')}]")
    for l in ("de", "fr", "es"): print(f"   {l}: {', '.join(nm[t][l][:6])}")
