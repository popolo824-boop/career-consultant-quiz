import re,json,sys,time,os,statistics as st
from yt import get,initial,walk,txt
E="/home/user/career-consultant-quiz/research_notes/日本参加型ショートアニメ参入分析/empirical/"
OUT=E+"channels_2026-10-07.json"
PART=re.compile(r'指を置|指をおい|指おいて|指おく|指を置く|指置|指を動か|指動かす|指を動|指でつまん|THUMB|Thumb|thumb|finger|Finger|指を離|タップ|スワイプ|友達に送|YES|参加型|一時停止|止めると|止められたら|選んで|どっち|指でなで|指でこす|指を使|手を使|手を動か|手をかざ|指遊び|指で止め|指で守|指でブロック|⭕に指|親指|遊べる|指で遊|指☝|遊ぶアニメ|指で|画面を|画面に|長押し|指を',re.I)
def views(s):
    m=re.search(r'([\d.,]+)\s*(億|万|千)?\s*回視聴',s or '')
    if not m: return None
    n=float(m.group(1).replace(',',''));u=m.group(2)
    return n*{'億':1e8,'万':1e4,'千':1e3,None:1}[u]
def about(h):
    d=initial(get("https://www.youtube.com/"+h+"/about")); o=[];walk(d,'aboutChannelViewModel',o)
    if not o: return {}
    a=o[0]
    return dict(subs=a.get('subscriberCountText'),total_views=a.get('viewCountText'),joined=a.get('joinedDateText',{}).get('content'),
        videos=a.get('videoCountText'),country=a.get('country'),cid=a.get('channelId'),title=None,desc=(a.get('description') or '')[:400])
def shorts(h):
    p=get("https://www.youtube.com/"+h+"/shorts"); d=initial(p)
    items=[];walk(d,'shortsLockupViewModel',items);rows=[]
    title=re.search(r'<title>([^<]*)</title>',p)
    for it in items:
        v=it.get('onTap',{}).get('innertubeCommand',{}).get('reelWatchEndpoint',{}).get('videoId') or it.get('entityId','').replace('shorts-shelf-item-','')
        m=it.get('overlayMetadata',{});t=m.get('primaryText',{}).get('content','')
        rows.append(dict(vid=v,title=t,views=views(m.get('secondaryText',{}).get('content')),part=bool(PART.search(t))))
    return (title.group(1).replace(' - YouTube','') if title else None),rows[:48]
def rss(cid):
    x=get("https://www.youtube.com/feeds/videos.xml?channel_id="+cid)
    rows=[]
    for e in re.findall(r'<entry>(.*?)</entry>',x,re.S):
        try: rows.append(dict(id=re.search(r'<yt:videoId>([^<]+)',e).group(1),date=re.search(r'<published>([^<]+)',e).group(1)[:10],
          title=re.search(r'<title>([^<]*)',e).group(1),views=int(re.search(r'<media:statistics views="(\d+)"',e).group(1))))
        except Exception: pass
    return rows
res=json.load(open(OUT)) if os.path.exists(OUT) else {}
for h in sys.argv[1:]:
    if h in res and 'err' not in res[h]: continue
    try:
        a=about(h); t,rows=shorts(h); a['title']=t; a['shorts']=rows
        a['rss']=rss(a['cid']) if a.get('cid') else []
        v=[r['views'] for r in rows if r['views']]; pv=[r['views'] for r in rows if r['views'] and r['part']]; nv=[r['views'] for r in rows if r['views'] and not r['part']]
        a['stats']=dict(n=len(v),median=st.median(v) if v else None,max=max(v) if v else None,n_part=len(pv),part_median=st.median(pv) if pv else None,part_max=max(pv) if pv else None,nonpart_median=st.median(nv) if nv else None)
        if len(a['rss'])>=2:
            ds=sorted(r['date'] for r in a['rss']); from datetime import date
            d0=date.fromisoformat(ds[0]);d1=date.fromisoformat(ds[-1]);span=(d1-d0).days or 1
            a['stats'].update(rss_n=len(ds),rss_first=ds[0],rss_last=ds[-1],per_week=round(len(ds)/span*7,2))
        res[h]=a; print(h,a.get('subs'),a.get('joined'),a['stats'],flush=True)
    except Exception as e:
        res[h]=dict(err=str(e)); print(h,"ERR",e,flush=True)
    json.dump(res,open(OUT,'w'),ensure_ascii=False,indent=0); time.sleep(2)
