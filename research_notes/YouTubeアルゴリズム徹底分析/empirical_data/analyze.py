import json,statistics as st,math,datetime as dt
from collections import defaultdict
d=json.load(open('raw_watch.json')); lst=json.load(open('listing.json'))
by=defaultdict(list)
for v,r in d.items():
    if r.get('date'): by[r['ch']].append(r)
def rank(x):
    s=sorted(range(len(x)),key=lambda i:x[i]);r=[0]*len(x);i=0
    while i<len(x):
        j=i
        while j+1<len(x) and x[s[j+1]]==x[s[i]]: j+=1
        for k in range(i,j+1): r[s[k]]=(i+j)/2+1
        i=j+1
    return r
def sp(a,b):
    if len(a)<5: return None
    ra,rb=rank(a),rank(b);ma,mb=st.mean(ra),st.mean(rb)
    n=sum((x-ma)*(y-mb) for x,y in zip(ra,rb));de=math.sqrt(sum((x-ma)**2 for x in ra)*sum((y-mb)**2 for y in rb))
    return n/de if de else None
def D(s): return dt.datetime.fromisoformat(s[:10]) if s else None
out={}
pool=[]
for h,rows in by.items():
    rows=[dict(r,dd=D(r['date'])) for r in rows]; rows.sort(key=lambda r:r['dd'])
    n=len(rows); vs=[r['views'] for r in rows]; med=st.median(vs)
    span=(rows[-1]['dd']-rows[0]['dd']).days or 1
    age=[(dt.datetime(2026,10,7)-r['dd']).days for r in rows]
    idx=list(range(n))
    half=n//2
    L=[r['len'] for r in rows]
    gaps=[None]+[(rows[i]['dd']-rows[i-1]['dd']).days for i in range(1,n)]
    gv=[(g,r['views']) for g,r in zip(gaps,rows) if g is not None]
    rr=dict(n=n,first=rows[0]['date'],last=rows[-1]['date'],span_days=span,per_week=round((n-1)/span*7,2) if span else None,
      median=med,mean=int(st.mean(vs)),max=max(vs),min=min(vs),
      first5=vs[:5],last5=vs[-5:],first5_med=st.median(vs[:5]),last5_med=st.median(vs[-5:]),
      firsthalf_med=st.median(vs[:half]),secondhalf_med=st.median(vs[half:]),
      rho_time_views=sp(idx,vs), rho_len_views=sp(L,vs),len_min=min(L),len_med=st.median(L),len_max=max(L),
      rho_gap_views=sp([g for g,_ in gv],[v for _,v in gv]),
      top3=[(r['views'],r['len'],r['date'],r['title'][:30]) for r in sorted(rows,key=lambda r:-r['views'])[:3]],
      top10share=round(sum(sorted(vs)[-max(1,n//10):])/sum(vs),2))
    out[h]=rr
    for r in rows: pool.append((h,r['views']/med,r['len'],r['views']))
for h,r in out.items(): print(h,json.dumps(r,ensure_ascii=False,default=str))
rho=sp([p[2] for p in pool],[p[1] for p in pool]); print('POOLED len vs views/chmedian rho',rho,len(pool))
# length buckets pooled normalized
b=defaultdict(list)
for h,x,L,v in pool: b['<=15' if L<=15 else '16-30' if L<=30 else '31-45' if L<=45 else '46+'].append(x)
for k,v in b.items(): print(k,len(v),round(st.median(v),2))
json.dump(out,open('summary.json','w'),ensure_ascii=False,default=str)
