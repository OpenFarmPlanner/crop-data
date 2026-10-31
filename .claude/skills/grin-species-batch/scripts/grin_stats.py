"""Usage codes, food usage types and common-name languages in the GRIN export.
Usage: grin_stats.py <grin-data-dir>
"""
import csv, sys, collections
csv.field_size_limit(10**9)
d = sys.argv[1]
def rows(name):
    with open(f"{d}/{name}.txt", encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
use = collections.Counter(); ut = collections.Counter(); sp_by_code = collections.defaultdict(set)
for r in rows("taxonomy_use"):
    use[r["economic_usage_code"]] += 1
    sp_by_code[r["economic_usage_code"]].add(r["taxonomy_species_id"])
    if r["economic_usage_code"] == "FOOD": ut[r["usage_type"]] += 1
print("usage codes (rows, species):")
for k, v in use.most_common(): print(f"  {k}: {v} / {len(sp_by_code[k])}")
print("FOOD usage types:"); 
for k, v in ut.most_common(40): print(f"  {k}: {v}")
allsp = set().union(*sp_by_code.values())
print("species with any use:", len(allsp))
lang = collections.Counter(); food = sp_by_code.get("FOOD", set()); langfood = collections.Counter()
for r in rows("taxonomy_common_name"):
    lang[r["language_description"]] += 1
    if r["taxonomy_species_id"] in food: langfood[r["language_description"]] += 1
print("languages (all / FOOD species):")
for k, v in lang.most_common(25): print(f"  {k}: {v} / {langfood[k]}")
