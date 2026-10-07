import re,json,time
from yt import get
CH=["@sorotani","@ikuze_1111","@fuziko-fuziko","@kyomuo","@kawisouni","@hajimemashite","@takatume_ncj","@kenozakaanime"]
out={}
for h in CH:
    p=get("https://www.youtube.com/"+h+"/shorts")
    cid=re.findall(r'channel_id=(UC[\w-]+)',p)[:1]
    x=get("https://www.youtube.com/feeds/videos.xml?channel_id="+cid[0])
    ents=re.findall(r'<entry>(.*?)</entry>',x,re.S); rows=[]
    for e in ents:
        rows.append(dict(id=re.search(r'<yt:videoId>([^<]+)',e).group(1),date=re.search(r'<published>([^<]+)',e).group(1),
          title=re.search(r'<title>([^<]*)',e).group(1),views=int(re.search(r'<media:statistics views="(\d+)"',e).group(1))))
    out[h]=dict(cid=cid[0],rows=rows); print(h,len(rows)); time.sleep(3)
json.dump(out,open('rss.json','w'),ensure_ascii=False)
