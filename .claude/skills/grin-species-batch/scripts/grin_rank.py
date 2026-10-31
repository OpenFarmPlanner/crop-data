"""Rank GRIN crop candidates that are not yet in the crop-species library.

Usage: grin_rank.py <grin-data-dir> <species-snapshot.json> <out-dir> [--uses vegetable,pulse,...]
Writes <out-dir>/candidates.tsv. Column `ours`: EXACT = same scientific name in
the library, SAME_SPECIES = same binomial, empty = not yet in the library.
Score = number of countries where GRIN lists the taxon as cultivated + 2 x
number of common-name languages. The GRIN weed flag is reported, not filtered:
it also marks major crops such as rice and taro.
"""
import argparse, collections, csv, json, re

USES = {"vegetable", "pulse", "cereal", "pseudocereal", "seeds", "starch", "fruit", "nut", "oil/fat",
        "sugar", "beverage base", "gum/mucilage", "additive:flavoring", "environ:soil improver"}

ap = argparse.ArgumentParser()
ap.add_argument("grin"); ap.add_argument("snapshot"); ap.add_argument("out")
ap.add_argument("--uses", default=",".join(sorted(USES)))
args = ap.parse_args()
wanted = set(args.uses.split(","))
csv.field_size_limit(10**9)

def rows(n):
    with open(f"{args.grin}/{n}.txt", encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)

taxa, cur, genus_of = {}, {}, {}
for r in rows("taxonomy_species"):
    t = r["taxonomy_species_id"]; cur[t] = r["current_taxonomy_species_id"]
    taxa[t] = re.sub(r"<[^>]+>", "", r["name"]); genus_of[t] = r["taxonomy_genus_id"]
fam_name = {r["taxonomy_family_id"]: r["family_name"] for r in rows("taxonomy_family")}
gen_fam = {r["taxonomy_genus_id"]: fam_name.get(r["taxonomy_family_id"], "") for r in rows("taxonomy_genus")}
uses, other = collections.defaultdict(set), collections.defaultdict(set)
for r in rows("taxonomy_use"):
    t = cur.get(r["taxonomy_species_id"], r["taxonomy_species_id"]); c, ty = r["economic_usage_code"], r["usage_type"]
    if c == "FOOD": uses[t].add(ty)
    elif c == "ADDITIVE" and ty == "flavoring": uses[t].add("additive:flavoring")
    elif c == "ENVIRON" and ty == "soil improver": uses[t].add("environ:soil improver")
    else: other[t].add(c.lower())
cult = collections.Counter()
for r in rows("taxonomy_geography_map"):
    if r["geography_status_code"] == "c": cult[cur.get(r["taxonomy_species_id"], r["taxonomy_species_id"])] += 1
LANG = {"German": "de", "English": "en", "French": "fr", "Spanish": "es"}
names = collections.defaultdict(lambda: collections.defaultdict(list)); nlang = collections.defaultdict(set)
for r in rows("taxonomy_common_name"):
    s = r["taxonomy_species_id"]
    if s == "\\N": continue
    t = cur.get(s, s); nlang[t].add(r["language_description"])
    l = LANG.get(r["language_description"].split(" (")[0])
    if l and r["name"] not in names[t][l]: names[t][l].append(r["name"])
sp = [s for s in json.load(open(args.snapshot)) if s["status"] != "rejected"]
ours_sci = {s["scientific_name"].lower() for s in sp if s["scientific_name"]}
ours_binom = {" ".join(n.split()[:2]) for n in ours_sci}
res = []
for t, u in uses.items():
    if cur.get(t) != t or not (u & wanted) or not cult[t]: continue
    sci = taxa[t]
    res.append(dict(grin_id=t, scientific=sci, family=gen_fam.get(genus_of[t], ""), uses=";".join(sorted(u)),
        cult_countries=cult[t], name_langs=len(nlang[t]), score=cult[t] + 2 * len(nlang[t]), weed="weed" in other[t],
        ours="EXACT" if sci.lower() in ours_sci else ("SAME_SPECIES" if " ".join(sci.lower().split()[:2]) in ours_binom else ""),
        de=" | ".join(names[t]["de"]), en=" | ".join(names[t]["en"][:5]), fr=" | ".join(names[t]["fr"][:4]), es=" | ".join(names[t]["es"][:4])))
res.sort(key=lambda r: -r["score"])
with open(f"{args.out}/candidates.tsv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(res[0]), delimiter="\t"); w.writeheader(); w.writerows(res)
print(len(res), dict(collections.Counter(r["ours"] or "NEW" for r in res)))
for r in [r for r in res if not r["ours"]][:60]:
    print(f'{r["score"]:>3} {r["scientific"]} [{r["family"]}] {r["uses"]} | de: {r["de"][:45]} | en: {r["en"][:50]}')
