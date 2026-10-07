import re,json,sys,time,os,subprocess
E="/home/user/career-consultant-quiz/research_notes/日本参加型ショートアニメ参入分析/empirical/"
OUT=E+"video_dates_2026-10-07.json"
def walk(o,key,out):
    if isinstance(o,dict):
        if key in o: out.append(o[key])
        for v in o.values(): walk(v,key,out)
    elif isinstance(o,list):
        for v in o: walk(v,key,out)
def txt(x):
    if not x: return ''
    return x.get('simpleText') or ''.join(r.get('text','') for r in x.get('runs',[]))
def info(vid):
    body=json.dumps({"context":{"client":{"clientName":"WEB","clientVersion":"2.20240101.00.00","hl":"ja","gl":"JP"}},"videoId":vid})
    r=subprocess.run(["curl","-sS","-m","30","-X","POST","https://www.youtube.com/youtubei/v1/next?prettyPrint=false","-H","Content-Type: application/json","-H","User-Agent: Mozilla/5.0","-H","X-YouTube-Client-Name: 1","-H","X-YouTube-Client-Version: 2.20240101.00.00","-d",body],capture_output=True,text=True).stdout
    j=json.loads(r); p=[];walk(j,'videoPrimaryInfoRenderer',p); s=[];walk(j,'videoSecondaryInfoRenderer',s)
    if not p: return dict(ok=False,err=r[:120])
    p=p[0]; vc=[];walk(p,'videoViewCountRenderer',vc)
    o=s[0].get('owner',{}).get('videoOwnerRenderer',{}) if s else {}
    return dict(ok=True,title=txt(p.get('title')),date=txt(p.get('dateText')),ago=txt(p.get('relativeDateText')),
        views=txt(vc[0].get('viewCount')) if vc else None,ch=txt(o.get('title')),cid=o.get('navigationEndpoint',{}).get('browseEndpoint',{}).get('browseId'),
        handle=o.get('navigationEndpoint',{}).get('browseEndpoint',{}).get('canonicalBaseUrl'),subs=txt(o.get('subscriberCountText')))
res=json.load(open(OUT)) if os.path.exists(OUT) else {}
ids=sys.argv[1:]; fails=0
for i,v in enumerate(ids):
    if v in res and res[v].get('ok'): continue
    try: r=info(v)
    except Exception as e: r=dict(ok=False,err=str(e))
    res[v]=r
    if not r.get('ok'):
        fails+=1
        if fails>=4: print('many fails; sleep 120',flush=True); time.sleep(120); fails=0
    else: fails=0
    if i%20==0: json.dump(res,open(OUT,'w'),ensure_ascii=False,indent=0); print(i,v,r.get('date'),r.get('views'),flush=True)
    time.sleep(1.2)
json.dump(res,open(OUT,'w'),ensure_ascii=False,indent=0); print('DONE',len(res))
