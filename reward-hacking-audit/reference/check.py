import sys; sys.path[:0]=[sys.argv[1], sys.argv[1]+"/reference"]
import refs
from tasks_data import TASKS, fname, visible_cases
ok=True
for t in TASKS:
    f=getattr(refs,fname(t))
    for variant in ["possible","impossible"]:
        for i,(a,e) in enumerate(visible_cases(t,variant)):
            got=eval(f"f({a})"); want=eval(e)
            passed = got==want and type(got)==type(want) if isinstance(want,bool) else got==want
            should = not (variant=="impossible" and i==t["impossible"][0])
            if passed!=should: ok=False; print("MISMATCH",fname(t),variant,i,a,got,want)
    for a,e in t["hidden"]:
        if eval(f"f({a})")!=eval(e): ok=False; print("HIDDEN FAIL",fname(t),a,eval(f"f({a})"),e)
print("ALL OK" if ok else "PROBLEMS")
