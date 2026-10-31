"""Scientific-name candidates for existing crop species, scored by name matches.
Usage: grin_sci_candidates.py <grin-data-dir> <species-snapshot.json> <out-dir>  -> sci-candidates.json (+ TSV on stdout)
"""
import csv, sys, json, collections, unicodedata, re
csv.field_size_limit(10**9)
grin, snap, out = sys.argv[1:4]
def rows(name):
    with open(f"{grin}/{name}.txt", encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
taxa, cur = {}, {}
for r in rows("taxonomy_species"):
    cur[r["taxonomy_species_id"]] = r["current_taxonomy_species_id"]
    taxa[r["taxonomy_species_id"]] = re.sub(r"<[^>]+>", "", r["name"])
by_sci = {norm(n): t for t, n in taxa.items()}
LANG = {"German": "de", "English": "en", "French": "fr", "Spanish": "es"}
idx = collections.defaultdict(set)
for r in rows("taxonomy_common_name"):
    sid = r["taxonomy_species_id"]
    if sid == "\\N": continue
    lang = LANG.get(r["language_description"].split(" (")[0])
    if lang: idx[(lang, norm(r["name"]))].add(cur.get(sid, sid))
sp = [s for s in json.load(open(snap)) if s["status"] == "published"]
res = []
for s in sp:
    row = {"id": s["id"], "name": s["name"], "current": s["scientific_name"]}
    if s["scientific_name"]:
        t = by_sci.get(norm(s["scientific_name"]))
        row["check"] = "not in GRIN" if not t else ("ok" if cur[t] == t else f"synonym of {taxa[cur[t]]}")
    score = collections.Counter()
    for tr in s["translations"]:
        w_common = 3 if tr["language_code"] == "de" else 2
        for i, n in enumerate([tr["common_name"], *tr["synonyms"]]):
            for t in idx.get((tr["language_code"], norm(n)), ()):
                score[t] += w_common if i == 0 else 1
    row["candidates"] = [(taxa[t], v) for t, v in score.most_common(5)]
    res.append(row)
json.dump(res, open(f"{out}/sci-candidates.json", "w"), ensure_ascii=False, indent=1)
for r in res:
    print(f'{r["id"]}\t{r["name"]}\t{r["current"]}\t{r.get("check","")}\t' + "; ".join(f"{n} ({v})" for n, v in r["candidates"]))
