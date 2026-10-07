import re,json,time,os
from yt import get,initial,walk
CH=["@sorotani","@ikuze_1111","@fuziko-fuziko","@kyomuo","@kawisouni","@hajimemashite","@takatume_ncj","@kenozakaanime"]
OUT='raw_watch.json'
res=json.load(open(OUT)) if os.path.exists(OUT) else {}
def listing(h):
    p=get("https://www.youtube.com/"+h+"/shorts"); d=initial(p)
    items=[];walk(d,'shortsLockupViewModel',items); out=[]
    for it in items:
        v=it.get('onTap',{}).get('innertubeCommand',{}).get('reelWatchEndpoint',{}).get('videoId') or it.get('entityId','').replace('shorts-shelf-item-','')
        m=it.get('overlayMetadata',{})
        out.append((v,m.get('primaryText',{}).get('content',''),m.get('secondaryText',{}).get('content','')))
    return out[:48]
def watch(v):
    h=get("https://www.youtube.com/watch?v="+v)
    pr=re.search(r'var ytInitialPlayerResponse = (\{.*?\});(?:var|</script>)',h,re.S)
    if not pr: return None
    j=json.loads(pr.group(1))
    if 'videoDetails' not in j: return None
    vd=j['videoDetails']; mf=j.get('microformat',{}).get('playerMicroformatRenderer',{})
    return dict(id=v,title=vd['title'],views=int(vd['viewCount']),len=int(vd['lengthSeconds']),date=mf.get('publishDate'))
lst=json.load(open('listing.json'))
print('listing saved',flush=True)
fails=0
for h in CH:
    for v,t,s in lst[h]:
        if v in res: continue
        r=None
        for k in range(3):
            r=watch(v)
            if r: break
            time.sleep(20)
        if not r:
            fails+=1
            if fails>=3:
                print('blocked; waiting 300s',flush=True); time.sleep(300); fails=0
            continue
        fails=0; r['ch']=h; res[v]=r
        json.dump(res,open(OUT,'w'),ensure_ascii=False)
        time.sleep(2.5)
    print('done',h,flush=True)
print('ALLDONE',flush=True)
