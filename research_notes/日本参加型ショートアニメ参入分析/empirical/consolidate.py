import json,re,statistics as st,collections,csv
E="/home/user/career-consultant-quiz/research_notes/日本参加型ショートアニメ参入分析/empirical/"
C=json.load(open(E+"channels_2026-10-07.json"))
import glob
D={}
for f in sorted(glob.glob(E+"video_dates_w*.json")): D.update(json.load(open(f)))
json.dump(D,open(E+"video_dates_merged_2026-10-07.json","w"),ensure_ascii=False,indent=0)
print("dated videos",len(D),"ok",sum(1 for x in D.values() if x.get("ok")))
PART=re.compile(r'指を置|指をおい|指おいて|指おく|指を置く|指置|指を動か|指動かす|指を動|指でつまん|THUMB|Thumb|thumb|finger|Finger|FINGER|指を離|タップ|スワイプ|友達に送|YES|Yes|参加型|ピッタリ|ぴったり|止めると|止められたら|選んで|どっち|2択|指でなで|指でなぞ|指を使|手を使|手を動か|手をかざ|指遊び|指で止め|指で守|指でブロック|⭕|親指|遊べる|指で遊|指☝|遊ぶアニメ|画面を|画面に|長押し|一緒に指|指を一緒',re.I)
def n(s):
    if s is None: return None
    m=re.search(r'([\d.,]+)\s*(億|万|千)?',str(s)); 
    if not m: return None
    return float(m.group(1).replace(',',''))*{'億':1e8,'万':1e4,'千':1e3,None:1}[m.group(2)]
# per-channel participatory video dates (from D), keyed by cid
bycid=collections.defaultdict(list)
for v,x in D.items():
    if x.get('ok') and x.get('cid'): bycid[x['cid']].append(dict(vid=v,**x))
rows=[]
for h,a in C.items():
    if 'err' in a or not a.get('cid'): rows.append(dict(handle=h,err=a.get('err','nocid'))); continue
    s=a['stats']; cid=a['cid']
    pv=[x for x in bycid.get(cid,[]) if PART.search(x['title'])]
    pdates=sorted(x['date'] for x in pv if x.get('date'))
    yrs=collections.Counter(d[:4] for d in pdates)
    rss=a.get('rss',[])
    rows.append(dict(handle=h,title=a.get('title'),subs=a.get('subs'),subs_n=n(a.get('subs')),joined=a.get('joined'),total_views=a.get('total_views'),videos=a.get('videos'),country=a.get('country'),
        shorts_n=s['n'],median=s['median'],max=s['max'],n_part48=s['n_part'],part_median=s['part_median'],part_max=s['part_max'],nonpart_median=s['nonpart_median'],
        rss_first=s.get('rss_first'),rss_last=s.get('rss_last'),per_week=s.get('per_week'),
        part_dated_n=len(pv),part_first=pdates[0] if pdates else None,part_last=pdates[-1] if pdates else None,part_by_year=dict(sorted(yrs.items())),
        part_top=sorted([(n(x['views']),x['date'],x['title'][:40]) for x in pv if x.get('views')],key=lambda t:-(t[0] or 0))[:3]))
json.dump(rows,open(E+"summary_2026-10-07.json","w"),ensure_ascii=False,indent=1)
with open(E+"summary_2026-10-07.csv","w",newline='') as f:
    w=csv.writer(f); keys=[k for k in rows[0].keys() if k not in('part_top','err')]; w.writerow(keys)
    for r in rows: w.writerow([json.dumps(r.get(k),ensure_ascii=False) if isinstance(r.get(k),(dict,list)) else r.get(k) for k in keys])
for r in sorted(rows,key=lambda r:-(r.get('subs_n') or 0)):
    if 'err' in r: print(r['handle'],'ERR'); continue
    print(f"{r['handle'][:28]:28} | {r['title'] and r['title'][:22]!s:22} | subs {r['subs_n']!s:10} | joined {r['joined']} | vids {r['videos']} | 48med {r['median']} max {r['max']} | part48 {r['n_part48']} pmed {r['part_median']} pmax {r['part_max']} npmed {r['nonpart_median']} | /wk {r['per_week']} last {r['rss_last']} | dated {r['part_dated_n']} {r['part_first']}..{r['part_last']} {r['part_by_year']}")
