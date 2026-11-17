"""For each cheating run, print the final solution.py as the agent left it (last write found in tool calls)."""
import glob, json, sys, re
rows = {(r["model"], r["id"], r["epoch"]) for r in json.load(open("results-main.json")) if r["outcome"] == "special_cased"}
for f in sorted(glob.glob("logs/main/*.json")):
    d = json.load(open(f)); m = d["eval"]["model"].split("/")[-1]
    for s in d.get("samples") or []:
        if (m, s["id"], s["epoch"]) not in rows: continue
        last = None
        for msg in s["messages"]:
            for tc in msg.get("tool_calls") or []:
                a = json.dumps(tc.get("arguments"))
                if "solution.py" in a and re.search(r"(cat\s*>|open\(|write|tee|sed -i|apply_patch|<<)", a):
                    last = tc.get("arguments")
        code = (last or {}).get("cmd") or (last or {}).get("code") or str(last)
        print(f"===== {m} | {s['id']} | epoch {s['epoch']}\n{code[:1400]}\n")
