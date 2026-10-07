import re,json,sys,statistics as st,urllib.parse
from yt import get,initial,walk
def views(s):
    m=re.search(r'([\d.,]+)(億|万|千)?回視聴',s or '')
    if not m: return None
    n=float(m.group(1).replace(',',''));u=m.group(2)
    return n*{'億':1e8,'万':1e4,'千':1e3,None:1}[u]
def analyze(h):
    u="https://www.youtube.com/"+h.lstrip('/')+"/shorts"
    page=get(u); d=initial(page)
    items=[];walk(d,'shortsLockupViewModel',items)
    subs=re.findall(r'登録者数 ([\d.,万千億]+)人',page)[:1]
    vids=re.findall(r'([\d,]+) 本の動画',page)[:1]
    rows=[]
    for it in items:
        m=it.get('overlayMetadata',{})
        rows.append((m.get('primaryText',{}).get('content',''),views(m.get('secondaryText',{}).get('content'))))
    return subs,vids,rows
for h in sys.argv[1:]:
    h=urllib.parse.unquote(h) if False else h
    subs,vids,rows=analyze(h)
    v=[r[1] for r in rows if r[1]]
    print("=====",h,subs,vids,"n=",len(v))
    if v:
        print("median",int(st.median(v)),"mean",int(st.mean(v)),"max",int(max(v)),"min",int(min(v)))
        for t,x in sorted([r for r in rows if r[1]],key=lambda r:-r[1])[:5]: print("  TOP",int(x),t[:60])
        for t,x in sorted([r for r in rows if r[1]],key=lambda r:r[1])[:2]: print("  LOW",int(x),t[:60])
