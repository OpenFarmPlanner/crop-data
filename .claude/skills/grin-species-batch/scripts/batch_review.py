"""Review table for a batch plan; lists names not found in GRIN for that taxon.
Usage: batch_review.py <grin-data-dir> <batch-plan.json> <out.md>
"""
import csv, sys, re, json, collections, unicodedata
csv.field_size_limit(10**9)
d, planf, out = sys.argv[1:4]
def rows(n): return csv.DictReader(open(f"{d}/{n}.txt", encoding="utf-8-sig"), delimiter="\t", quoting=csv.QUOTE_NONE)
def norm(s): return re.sub(r"[^a-z]+", " ", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()).strip()
taxa, cur = {}, {}
for r in rows("taxonomy_species"): taxa[r["taxonomy_species_id"]] = re.sub(r"<[^>]+>", "", r["name"]).lower(); cur[r["taxonomy_species_id"]] = r["current_taxonomy_species_id"]
L = {"German": "de", "English": "en", "French": "fr", "Spanish": "es"}
nm = collections.defaultdict(set)
for r in rows("taxonomy_common_name"):
    s = r["taxonomy_species_id"]; l = L.get(r["language_description"].split(" (")[0])
    if s != "\\N" and l:
        t = cur.get(s, s); nm[(taxa[t], l)].add(norm(r["name"]))
        # names on infraspecific taxa count for the species too
        nm[(" ".join(taxa[t].split()[:2]), l)].add(norm(r["name"]))
plan = json.load(open(planf))["new"]
lines = ["| de | en | fr | es | Scientific name | Family | Not found in GRIN | Note |", "|---|---|---|---|---|---|---|---|"]
for e in plan:
    b = e["body"]; sci = b["scientific_name"].lower(); miss = []
    tr = {t["language_code"]: t for t in b["translations"]}
    for l in ("de", "en", "fr", "es"):
        got = nm.get((sci, l), set()) | nm.get((" ".join(sci.split()[:2]), l), set())
        m = [n for n in [tr[l]["common_name"], *tr[l]["synonyms"]] if norm(n) not in got]
        if m: miss.append(f"{l}: " + ", ".join(m))
    cell = lambda l: f"**{tr[l]['common_name']}**" + (f" ({', '.join(tr[l]['synonyms'])})" if tr[l]['synonyms'] else "")
    lines.append(f"| {cell('de')} | {cell('en')} | {cell('fr')} | {cell('es')} | *{b['scientific_name']}* | {b['family']} | {'; '.join(miss)} | {e.get('flag','')} |")
open(out, "w").write("\n".join(lines) + "\n")
print(sum(1 for e in plan), "rows written")
