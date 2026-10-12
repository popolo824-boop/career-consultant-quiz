import json,sys,time,urllib.request,os
sys.path.insert(0,".")
from cs import search,UA
# args: outdir name=exact_title ...
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
meta=json.load(open(f"{out}/meta.json")) if os.path.exists(f"{out}/meta.json") else {}
for a in sys.argv[2:]:
    name,title=a.split("=",1)
    q,_,pre=title.partition("@")   # query@title-prefix
    r=[x for x in search(q,10) if x["title"].startswith(pre)]
    if not r: print("NOTFOUND",title); continue
    r=r[0]; url=r["thumb"]
    if r["w"]<=1920:
        import re as _re
        m=_re.match(r"(https://upload.wikimedia.org/wikipedia/commons)/(\w/\w\w)/([^?]+)",url)
        sz=max([x for x in (330,500,960,1280) if x<r["w"]] or [330])
        url=f"{m.group(1)}/thumb/{m.group(2)}/{m.group(3)}/{sz}px-{m.group(3)}"
    for i in range(5):
        try:
            data=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
            if data[:3]==b"\xff\xd8\xff" or data[:4]==b"\x89PNG": break
        except Exception as e: pass
        time.sleep(4*(i+1)); data=b""
    if not data: print("FAIL",title); continue
    ext=".png" if data[:4]==b"\x89PNG" else ".jpg"
    open(f"{out}/{name}{ext}","wb").write(data); meta[name]=r; print("OK",name,len(data),r["lic"],r["artist"][:40])
    time.sleep(2)
json.dump(meta,open(f"{out}/meta.json","w"),ensure_ascii=False,indent=1)
