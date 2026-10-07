import re,json,subprocess,urllib.parse,sys
def get(u):
    return subprocess.run(["curl","-sS","-L","-m","40","-A","Mozilla/5.0","-H","Accept-Language: ja","-b","CONSENT=YES+1",u],capture_output=True,text=True).stdout
def initial(h):
    m=re.search(r'var ytInitialData = (\{.*?\});</script>',h,re.S)
    return json.loads(m.group(1)) if m else {}
def walk(o,key,out):
    if isinstance(o,dict):
        if key in o: out.append(o[key])
        for v in o.values(): walk(v,key,out)
    elif isinstance(o,list):
        for v in o: walk(v,key,out)
def search(q,sp=""):
    h=get("https://www.youtube.com/results?search_query="+urllib.parse.quote(q)+(("&sp="+sp) if sp else ""))
    d=initial(h); vids=[];chs=[]
    walk(d,'videoRenderer',vids); walk(d,'channelRenderer',chs)
    return vids,chs
def txt(x):
    if not x: return ''
    return x.get('simpleText') or ''.join(r.get('text','') for r in x.get('runs',[]))
if __name__=="__main__":
    seen={}
    for q in sys.argv[1:]:
        for sp in ("EgIQAg%3D%3D",""):  # channels filter, then all
            vids,chs=search(q,sp)
            for c in chs:
                h=c.get('navigationEndpoint',{}).get('browseEndpoint',{}).get('canonicalBaseUrl','')
                seen.setdefault(h,(txt(c.get('title')),txt(c.get('videoCountText')) or txt(c.get('subscriberCountText')),txt(c.get('subscriberCountText')),q))
            for v in vids:
                h=v.get('ownerText',{}).get('runs',[{}])[0].get('navigationEndpoint',{}).get('browseEndpoint',{}).get('canonicalBaseUrl','')
                if h and h not in seen: seen[h]=(txt(v.get('ownerText')),'',' (video hit)',q)
    for k,v in seen.items(): print(k,v)
