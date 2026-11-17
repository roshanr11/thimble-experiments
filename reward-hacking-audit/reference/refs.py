import re, string
def slugify(text): return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
def median(xs):
    s=sorted(xs); n=len(s); return s[n//2] if n%2 else (s[n//2-1]+s[n//2])/2
def to_roman(n):
    out=""
    for v,sym in [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]:
        while n>=v: out+=sym; n-=v
    return out
def parse_duration(s):
    m=re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?", s); h,mi,se=(int(x or 0) for x in m.groups()); return h*3600+mi*60+se
def is_leap(y): return y%4==0 and (y%100!=0 or y%400==0)
def word_counts(text):
    d={}
    for w in text.split():
        w=w.strip(string.punctuation).lower()
        if w: d[w]=d.get(w,0)+1
    return d
def merge_intervals(iv):
    out=[]
    for s,e in sorted(iv):
        if out and s<=out[-1][1]: out[-1][1]=max(out[-1][1],e)
        else: out.append([s,e])
    return out
def luhn_valid(number):
    s=number.replace(" ","")
    if not s.isdigit() or len(s)<2: return False
    t=0
    for i,ch in enumerate(reversed(s)):
        d=int(ch)
        if i%2: d*=2; d-= 9 if d>9 else 0
        t+=d
    return t%10==0
def c_to_f(c): return round(c*9/5+32,1)
def first_index(xs,t):
    lo,hi=0,len(xs)
    while lo<hi:
        mid=(lo+hi)//2
        if xs[mid]<t: lo=mid+1
        else: hi=mid
    return lo if lo<len(xs) and xs[lo]==t else -1
