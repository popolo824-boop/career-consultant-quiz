import json,sys,time,urllib.request,urllib.parse,re
UA={"User-Agent":"trivia-shorts-research/1.0 (popolo824 project)"}
def api(p):
    url="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p)
    for i in range(5):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30).read()
            return json.loads(r)
        except Exception as e:
            time.sleep(3*(i+1))
    return {}
def search(q,n=8):
    d=api({"action":"query","format":"json","generator":"search","gsrsearch":q,"gsrnamespace":6,"gsrlimit":n,
           "prop":"imageinfo","iiprop":"url|size|extmetadata","iiurlwidth":1920})
    out=[]
    for p in sorted(d.get("query",{}).get("pages",{}).values(),key=lambda x:x.get("index",0)):
        ii=p["imageinfo"][0]; m=ii.get("extmetadata",{})
        g=lambda k:re.sub("<[^>]+>","",m.get(k,{}).get("value",""))[:80]
        out.append(dict(title=p["title"],w=ii["width"],h=ii["height"],lic=g("LicenseShortName"),artist=g("Artist"),date=g("DateTimeOriginal"),thumb=ii.get("thumburl"),page=ii.get("descriptionurl")))
    return out
if __name__=="__main__":
  for q in sys.argv[1:]:
    print("##",q)
    for r in search(q): print(json.dumps(r,ensure_ascii=False))
    time.sleep(2)
