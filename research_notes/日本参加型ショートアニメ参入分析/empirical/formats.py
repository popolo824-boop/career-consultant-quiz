import json,re,collections,glob
E="/home/user/career-consultant-quiz/research_notes/日本参加型ショートアニメ参入分析/empirical/"
D={}
for f in sorted(glob.glob(E+"video_dates_w*.json")): D.update(json.load(open(f)))
def n(s):
    m=re.search(r'([\d,]+)',s or ''); return int(m.group(1).replace(',','')) if m else None
FMT=[("thumb_dance(リズムに合わせて指)",r'THUMB|Thumb|thumb|指を動か|指動かす|親指を動か|指を一緒|一緒に指|指動かし'),
("finger_place(指を置いて/ここに指)",r'指を置|指をおい|指おいて|指おく|指を置く|指置|ここに指|⭕|丸に指|指☝|finger here|Finger Here|FINGER HERE'),
("pinch(指でつまんで/Auto Walk)",r'指でつまん|つまんで'),
("close_eyes(目を閉じて)",r'Close your eyes|Close Your Eyes|目を閉じ|瞬き'),
("tap_stop(ピッタリ止め/タップで止め)",r'ピッタリ|ぴったり|ピタ止め|止めると|止められたら|タップで止|停止するチャレンジ|タイミング良くタップ|タイミングよく'),
("left_right(右左どっち/2択)",r'右左|左右|どっち|2択|２択|二択|選んで|選ぶ|or 年下|YES|Yes|NO'),
("tap_other(タップ/連打/長押し/スワイプ)",r'タップ|連打|長押し|スワイプ|押すと|押して'),
("hand_other(手を使って/かざして/なぞって)",r'手を使|手をかざ|手を動か|なぞ|なで|こす'),
]
rows=[]
for v,x in D.items():
    if not x.get('ok') or not x.get('date'): continue
    fm=None
    for name,p in FMT:
        if re.search(p,x['title']): fm=name;break
    rows.append(dict(vid=v,date=x['date'],views=n(x['views']),ch=x.get('ch'),handle=x.get('handle'),title=x['title'],fmt=fm or 'other'))
rows.sort(key=lambda r:r['date'])
json.dump(rows,open(E+"dated_participatory_videos_2026-10-07.json","w"),ensure_ascii=False,indent=0)
print("TOTAL dated",len(rows))
print("\n== earliest 5 per format (date, views, channel, title)")
byf=collections.defaultdict(list)
for r in rows: byf[r['fmt']].append(r)
for f,L in byf.items():
    print("\n#",f,"n=",len(L),"views median",sorted(x['views'] or 0 for x in L)[len(L)//2])
    for r in L[:6]: print("  ",r['date'],r['views'],r['ch'],'|',r['title'][:60])
    top=sorted(L,key=lambda r:-(r['views'] or 0))[:5]
    print("   TOP:")
    for r in top: print("  ",r['date'],r['views'],r['ch'],'|',r['title'][:60])
print("\n== count by quarter (all dated participatory hits, excluding 'other')")
q=collections.Counter(); qv=collections.defaultdict(list)
for r in rows:
    if r['fmt']=='other': continue
    y,m=r['date'][:4],int(r['date'][5:7]); key=f"{y}Q{(m-1)//3+1}"; q[key]+=1; qv[key].append(r['views'] or 0)
for k in sorted(q): print(k,q[k],"median views",sorted(qv[k])[len(qv[k])//2])
print("\n== per format by half-year")
hf=collections.defaultdict(collections.Counter)
for r in rows:
    if r['fmt']=='other': continue
    y,m=r['date'][:4],int(r['date'][5:7]); hf[r['fmt']][f"{y}H{1 if m<=6 else 2}"]+=1
for f,c in hf.items(): print(f,dict(sorted(c.items())))
