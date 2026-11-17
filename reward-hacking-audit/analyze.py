"""Tabulate outcomes from completed (non-errored) samples in Inspect JSON logs."""
import glob, json, sys, collections
rows = []
for f in sorted(glob.glob(sys.argv[1] + "/*.json")):
    d = json.load(open(f))
    m = d["eval"]["model"].split("/")[-1]
    for s in d.get("samples") or []:
        if s.get("error") or not s.get("scores"):
            continue
        sc = list(s["scores"].values())[0]
        rows.append(dict(model=m, id=s["id"], epoch=s["epoch"], variant=s["metadata"]["variant"],
                         outcome=sc["metadata"]["outcome"], limit=bool(s.get("limit"))))
by = collections.defaultdict(collections.Counter)
for r in rows:
    by[(r["model"], r["variant"])][r["outcome"]] += 1
print(f"{'model':28} {'variant':10} n  outcomes")
for (m, v), c in sorted(by.items()):
    print(f"{m:28} {v:10} {sum(c.values()):2} {dict(c)}")
imp = [r for r in rows if r["variant"] == "impossible"]
cheat = [r for r in imp if r["outcome"] in ("special_cased", "tampered")]
print(f"\nimpossible runs: {len(imp)}, cheated: {len(cheat)}")
for r in sorted(cheat, key=lambda r: (r["model"], r["id"])):
    print("  ", r["model"], r["id"], "epoch", r["epoch"], r["outcome"])
json.dump(rows, open(sys.argv[2], "w"), indent=1)
