"""Match all in-scope GRIN taxa against the crop-species snapshot.
Usage: grin_match.py <grin-data-dir> <species-snapshot.json> <out-dir>  -> grin-match.tsv, ours-not-in-grin.txt
"""
import csv, sys, json, collections, unicodedata, re
csv.field_size_limit(10**9)
grin, snap, out = sys.argv[1], sys.argv[2], sys.argv[3]
def rows(name):
    with open(f"{grin}/{name}.txt", encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
def strip_html(s): return re.sub(r"<[^>]+>", "", s or "")
SCOPE = {("FOOD", None), ("ADDITIVE", "flavoring"), ("ENVIRON", "soil improver")}
taxa, cur = {}, {}
for r in rows("taxonomy_species"):
    tid = r["taxonomy_species_id"]; cur[tid] = r["current_taxonomy_species_id"]
    taxa[tid] = strip_html(r["name"])
uses = collections.defaultdict(set); other = collections.defaultdict(set)
for r in rows("taxonomy_use"):
    t = cur.get(r["taxonomy_species_id"], r["taxonomy_species_id"])
    code, typ = r["economic_usage_code"], r["usage_type"]
    if ("FOOD", None) in SCOPE and code == "FOOD" or (code, typ) in SCOPE:
        uses[t].add(typ if code == "FOOD" else f"{code.lower()}:{typ}")
    else:
        other[t].add(f"{code.lower()}:{typ}" if typ != "\\N" else code.lower())
LANG = {"German": "de", "English": "en", "French": "fr", "Spanish": "es"}
names = collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows("taxonomy_common_name"):
    sid = r["taxonomy_species_id"]
    if sid == "\\N": continue
    t = cur.get(sid, sid); lang = r["language_description"].split(" (")[0]
    if lang in LANG and r["name"] not in names[t][LANG[lang]]:
        names[t][LANG[lang]].append(r["name"])
# our species
sp = json.load(open(snap)); sp = [s for s in sp if s["status"] != "rejected"]
sci_idx = {}; name_idx = collections.defaultdict(set)
by_name = {norm(t): tid for tid, t in taxa.items()}
for s in sp:
    if s["scientific_name"]:
        n = norm(s["scientific_name"]); tid = by_name.get(n)
        sci_idx.setdefault(cur.get(tid, n) if tid else n, set()).add(s["name"])
    for tr in s["translations"]:
        for n in [tr["common_name"], *tr["synonyms"], *tr["regional_names"].values()]:
            name_idx[(tr["language_code"], norm(n))].add(s["name"])
res = []; matched_species = set()
for t in uses:
    if cur.get(t) != t: continue
    m_sci = sci_idx.get(t, set())
    m_name = set()
    for lang, ns in names[t].items():
        for n in ns: m_name |= name_idx.get((lang, norm(n)), set())
    status = "SCI" if m_sci else ("NAME" if m_name else "NEW")
    matched_species |= m_sci | m_name
    res.append(dict(grin_id=t, scientific=taxa[t], status=status, uses=";".join(sorted(uses[t])),
        de=" | ".join(names[t]["de"]), en=" | ".join(names[t]["en"][:6]), fr=" | ".join(names[t]["fr"][:4]),
        es=" | ".join(names[t]["es"][:4]), matched=" | ".join(sorted(m_sci | m_name)),
        other_uses=";".join(sorted(other[t]))))
res.sort(key=lambda r: (r["status"], r["scientific"]))
with open(f"{out}/grin-match.tsv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(res[0]), delimiter="\t"); w.writeheader(); w.writerows(res)
unmatched = [s["name"] for s in sp if s["name"] not in matched_species]
open(f"{out}/ours-not-in-grin.txt", "w").write("\n".join(sorted(unmatched)) + "\n")
c = collections.Counter(r["status"] for r in res); print("GRIN taxa in scope:", len(res), dict(c))
new = [r for r in res if r["status"] == "NEW"]
print("NEW with de name:", sum(1 for r in new if r["de"]), " with en:", sum(1 for r in new if r["en"]),
      " with fr:", sum(1 for r in new if r["fr"]), " with es:", sum(1 for r in new if r["es"]))
uc = collections.Counter(u for r in new for u in r["uses"].split(";")); print("NEW by use:", uc.most_common(12))
rank = collections.Counter(("infra" if (" var. " in r["scientific"] or " subsp. " in r["scientific"] or " f. " in r["scientific"]) else "species") for r in new)
print("NEW rank:", dict(rank))
print("our species not matched to any GRIN taxon in scope:", len(unmatched))
