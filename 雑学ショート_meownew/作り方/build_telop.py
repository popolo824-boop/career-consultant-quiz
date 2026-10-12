import json,os,subprocess,sys
SP=os.path.dirname(os.path.abspath(__file__))
FONT=f"{SP}/fonts/MPLUS1p-Black.ttf"
W,H=1080,1920
CX=540; MAXW=700            # centered, half-width<=350 -> stays inside x 190..890 (safe x 60..890)
MY0,MY1=460,1395            # media area
MH=MY1-MY0
V={
"golf":dict(out="moon_golf_telop.mp4",title=["月面で人類が","最初にしたスポーツ"],scenes=[
 ("zatsu/golf/launch.jpg",None,0.35,"月面で、/人類が初めてやった/スポーツ、/何だと思いますか？","NASA"),
 ("zatsu/golf/shepard.jpg",None,0.45,"1971年、/アポロ14号。/アラン・シェパード|船長は、/月面を歩いた/5人目の人類です。","NASA"),
 ("zatsu/golf/tv.jpg","1500:1300:200:60",0.5,"答えは、/なんとゴルフ。/月面からの|テレビ中継で、/ボールを打ちました。","NASA"),
 ("zatsu/golf/club.jpg",None,0.5,"クラブは手作り。/6番アイアンの頭を、/サンプル採取用の|持ち手に取り付けたものです。","Kevin M. Gill（CC BY 2.0）"),
 ("zatsu/golf/balls.jpg","1200:1200:360:500",0.5,"本人は|「何マイルも飛んだ」と/言いましたが、/2021年の|画像解析では、/約22メートルと/約36メートルでした。","NASA"),
 ("zatsu/golf/shepard.jpg",None,0.45,"宇宙服で体が回らず、/片手で打ったそうです。/そのボールは、/今も月面に|残っています。","NASA")]),
"obama":dict(out="obama_telop.mp4",title=["オバマ元大統領の","人生初バイト"],scenes=[
 ("zatsu/img/obama.jpg",None,0.22,"オバマ元大統領の、/人生最初のバイト、/何だと思いますか？","Wikimedia Commons"),
 ("zatsu/img/store.jpg",None,0.5,"答えは、/アイスクリーム屋さん。/日本でいう、/サーティワンです。","Wikimedia Commons"),
 ("zatsu/img/hawaii.jpg",None,0.6,"場所は|ハワイのホノルル。/10代のころ、/カウンターで/アイスをすくっていました。","Wikimedia Commons"),
 ("zatsu/img/store.jpg","1200:1000:360:220",0.5,"本人いわく、/「カチカチのアイスを/何列もすくうのは、/手首にこたえる」。/2016年の、|本人の投稿です。","Wikimedia Commons"),
 ("zatsu/img/icecream.jpg","1000:780:330:470",0.5,"2010年に|来日したときは、/鎌倉の大仏で、/抹茶アイスを|食べています。","Wikimedia Commons"),
 ("zatsu/img/hawaii.jpg",None,0.6,"ちなみに「31」は、/1か月31日、/毎日ちがう味が選べる、/という意味です。","Wikimedia Commons")])}
V.update({
"tug":dict(out="tug_telop.mp4",title=["綱引きは昔","オリンピック競技"],scenes=[
 ("next/tug/greek.jpg",None,0.5,"綱引きが、/オリンピックの|正式な種目だったって、/知っていますか？","Jessie Tarbox Beals（パブリックドメイン）"),
 ("next/tug/nyac.jpg",None,0.5,"1900年の|パリ大会から、/1920年の|アントワープ大会まで、/正式な種目でした。","Jessie Tarbox Beals（パブリックドメイン）"),
 ("next/tug/col.jpg",None,0.45,"1908年の|ロンドン大会では、/金・銀・銅を、/イギリスの|警察チームが独占。","Wikimedia Commons（パブリックドメイン）"),
 ("next/tug/nyac.jpg","1100:800:0:560",0.5,"このとき、/アメリカは、/「相手のブーツが|ずるい」と抗議しました。","Jessie Tarbox Beals（パブリックドメイン）"),
 ("next/tug/greek.jpg","1100:800:760:520",0.5,"リバプール警察が、/仕事用のブーツのまま|出ていたからです。/でも抗議は認められず、/アメリカは|棄権しました。","Jessie Tarbox Beals（パブリックドメイン）"),
 ("next/tug/gb1912.jpg",None,0.5,"そして綱引きは、/1920年を最後に、/オリンピックから|消えました。","Wikimedia Commons（パブリックドメイン）")]),
"gorilla":dict(out="gorilla_telop.mp4",title=["ゴリラの学名","まさかの3連続"],scenes=[
 ("next/gorilla/watch.jpg",None,0.45,"ゴリラの学名、/知っていますか？","TheLeftCoast（CC0）"),
 ("next/gorilla/bronx.jpg",None,0.35,"ニシローランドゴリラの|学名は、/ゴリラ・ゴリラ・ゴリラ。","Ryan Schwark（CC0）"),
 ("next/gorilla/figs.jpg",None,0.45,"最初のゴリラが「属」、/次のゴリラが「種」、/最後のゴリラが|「亜種」の名前です。","TheLeftCoast（CC0）"),
 ("next/gorilla/hannover.jpg",None,0.45,"つまり、/ゴリラの仲間の、/ゴリラという種の、/ゴリラという亜種、/という意味なんです。","XenonX3（CC0）"),
 ("next/gorilla/family.jpg",None,0.5,"同じ言葉をくり返す学名は、/動物では|認められています。","TheLeftCoast（CC0）"),
 ("next/gorilla/watch.jpg",None,0.4,"でも植物では禁止。/だから植物には、/こういう学名はありません。","TheLeftCoast（CC0）")]),
"gogh":dict(out="gogh_telop.mp4",title=["ゴッホの絵","生前に売れたのは…"],scenes=[
 ("next/gogh/self.jpg",None,0.35,"ゴッホが、/生きている間に|売れた絵、/何枚だと思いますか？","Wikimedia Commons（パブリックドメイン）"),
 ("next/gogh/vine.jpg",None,0.5,"確かな記録が|残っているのは、/たった1枚。/この「赤い葡萄畑」です。","Wikimedia Commons（パブリックドメイン）"),
 ("next/gogh/boch.jpg",None,0.3,"1890年、/画家のアンナ・ボックが、/400フランで|買いました。","Wikimedia Commons（パブリックドメイン）"),
 ("next/gogh/ear.jpg",None,0.35,"そしてゴッホは、/その年の7月に|亡くなります。","Wikimedia Commons（パブリックドメイン）"),
 ("next/gogh/vine.jpg",None,0.5,"アンナは1906年、/この絵を|1万フランで売りました。/買った値段の、25倍です。","Wikimedia Commons（パブリックドメイン）"),
 ("next/gogh/self.jpg",None,0.35,"ただ、ほかにも/売れた絵があったという|説もあり、/今も研究が続いています。","Wikimedia Commons（パブリックドメイン）")]),
})
V.update({
"mike":dict(out="mike_telop.mp4",title=["三毛猫のほとんどは","メスだった"],scenes=[
 ("next/mike/c8.jpg",None,0.4,"三毛猫って、/ほとんどがメスなのを|知っていますか？","Wikimedia Commons（パブリックドメイン）"),
 ("next/mike/c0.jpg",None,0.35,"毛の色を決める遺伝子の|一部は、/X染色体に|乗っています。","Wikimedia Commons（パブリックドメイン）"),
 ("next/mike/c1.jpg",None,0.4,"オレンジと黒の両方を|持てるのは、/X染色体を|2本持つメスだけ。/だから三毛になるのは、|ほぼメスなんです。","Wikimedia Commons（パブリックドメイン）"),
 ("next/mike/c4.jpg",None,0.4,"オスの三毛猫は、/X染色体が|1本多いなどの、/とても珍しいケースです。","Wikimedia Commons（パブリックドメイン）"),
 ("next/mike/c8.jpg",None,0.6,"数千匹に1匹とも|言われています。","Wikimedia Commons（パブリックドメイン）"),
 ("next/mike/c0.jpg",None,0.5,"もしオスの三毛猫に|会えたら、/それはかなり|珍しい出会いです。","Wikimedia Commons（パブリックドメイン）")]),
"otter":dict(out="otter_telop.mp4",title=["ラッコの脇には","ポケットがある"],scenes=[
 ("next/otter/mb13.jpg",None,0.45,"ラッコの脇の下には、/ポケットがあるのを|知っていますか？","Mike Baird（CC BY 2.0）"),
 ("next/otter/nurse.jpg",None,0.5,"前足の下の、|たるんだ皮が、/ポケットのように|なっているんです。","Mike Baird（CC BY 2.0）"),
 ("next/otter/nps2.jpg",None,0.5,"ここに、/とった食べ物を|しまっておきます。","National Park Service（パブリックドメイン）"),
 ("next/otter/ak.jpg",None,0.5,"さらに、/貝を割るための石も|入れておきます。","RndmCrs（CC0）"),
 ("next/otter/nps1.jpg",None,0.5,"おなかの上に石を置き、/貝を打ちつけて|割るんです。","National Park Service（パブリックドメイン）"),
 ("next/otter/mb13.jpg",None,0.55,"使いやすい石は、/手放さずに|使い続けることも|あるそうです。","Mike Baird（CC BY 2.0）")]),
"seahorse":dict(out="seahorse_telop.mp4",title=["タツノオトシゴは","オスが出産する"],scenes=[
 ("next/seahorse/pac.jpg",None,0.4,"タツノオトシゴは、/オスが出産するって|知っていますか？","HeavyMetalChicken（CC0）"),
 ("next/seahorse/fmib.jpg",None,0.5,"メスが、/オスのおなかの袋に|卵を入れます。","Theodore Edward Cantor（パブリックドメイン）"),
 ("next/seahorse/pac.jpg",None,0.6,"卵は袋の中で受精し、/オスが袋の中で|育てます。","HeavyMetalChicken（CC0）"),
 ("next/seahorse/kny.jpg",None,0.5,"そして子どもが育つと、/オスがおなかから|産み出すんです。","iNaturalist（CC0）"),
 ("next/seahorse/rg.jpg",None,0.5,"仲間のシードラゴンも、/オスが子どもを|育てます。","Romain Guy（CC0）"),
 ("next/seahorse/pac.jpg",None,0.3,"オスが妊娠する、/動物の中でも|とても珍しい仕組みです。","HeavyMetalChicken（CC0）")]),
"boycott":dict(out="boycott_telop.mp4",title=["ボイコットは","実は人の名前"],scenes=[
 ("next/boycott/vf.jpg",None,0.3,"ボイコットという言葉、/実は人の名前|なんです。","Leslie Ward（パブリックドメイン）"),
 ("next/boycott/lw.jpg",None,0.25,"チャールズ・ボイコット。/1880年、アイルランドで|土地の管理人を|していました。","Leslie Ward（CC0）"),
 ("next/boycott/vf.jpg",None,0.5,"小作人を|追い出そうとしたため、/地元の人たちは、/彼のために働くのを|やめました。","Leslie Ward（パブリックドメイン）"),
 ("next/boycott/wollen.jpg",None,0.5,"店も、/彼に物を売らなくなり、/収穫には、|兵士に守られた人たちが|送り込まれたほどです。","William Barnes Wollen（パブリックドメイン）"),
 ("next/boycott/wollen.jpg","900:900:500:200",0.5,"こうして、/みんなで関わりを断つことを、/「ボイコット」と|呼ぶようになったんです。","William Barnes Wollen（パブリックドメイン）"),
 ("next/boycott/lw.jpg",None,0.6,"人の名前が、/そのまま言葉に|なった例です。","Leslie Ward（CC0）")]),
"kame":dict(out="kame_telop.mp4",title=["カメハメハの","名前の意味"],scenes=[
 ("next/kame/cap.jpg",None,0.3,"カメハメハ大王の名前、/どんな意味か|知っていますか？","U.S. Capitol（パブリックドメイン）"),
 ("next/kame/choris.jpg",None,0.4,"ハワイの島々を、/初めて一つの王国に|まとめた王様です。","Louis Choris（CC0）"),
 ("next/kame/veel.jpg",None,0.45,"名前の意味は、/「とても孤独な者」、/または|「選び分けられた者」。","D. Veelward（パブリックドメイン）"),
 ("next/kame/kohala.jpg",None,0.35,"生まれてすぐ|命を狙われ、/ひそかに育てられたと|伝えられています。","Wmpearl（CC0）"),
 ("next/kame/cap.jpg",None,0.6,"大人になってから、/この名前を|名乗ったそうです。","U.S. Capitol（パブリックドメイン）"),
 ("next/kame/cap.jpg",None,0.25,"6月11日は、/ハワイでは|「カメハメハ・デー」という|祝日です。","U.S. Capitol（パブリックドメイン）")]),
})
READ={"X染色体":"エックス染色体","小作人":"こさくにん","柄に":"えに"}
def yomi(t):
    for k,v in READ.items(): t=t.replace(k,v)
    return t
def esc(s): return s.replace("\\","\\\\").replace(":","\\:").replace("'","\u2019").replace("%","\\%")
def tw(s,fs): return sum(fs*(0.6 if ord(c)<128 else 1.0) for c in s)
def fit(s,fs,maxw=MAXW): return min(fs,int(fs*maxw/max(1,tw(s,fs))))
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def chunks(marked,words):
    parts=marked.split("/"); plain=marked.replace("/","").replace("|","")
    bounds=[];p=0
    for c in parts:
        n=len(c.replace("|","")); bounds.append((p,p+n)); p+=n
    starts=[None]*len(parts); pos=0
    for a,b,w in words:
        k=plain.find(w,pos)
        if k<0: continue
        pos=k+len(w)
        ci=next(x for x,(u,v) in enumerate(bounds) if u<=k<v)
        if starts[ci] is None: starts[ci]=a
    for x in range(len(starts)):
        if starts[x] is None: starts[x]=starts[x-1] if x else 0
    return [[starts[x],[ "".join(ch for ch in l if ch not in "、。") for l in parts[x].split("|")]] for x in range(len(parts))]
def build(key):
    cfg=V[key]; D=f"telop_k/{key}"; os.makedirs(D,exist_ok=True)
    jobs=[[f"{D}/n{i}",[yomi(p.replace("|","")) for p in sc[3].split("/")]] for i,sc in enumerate(cfg["scenes"])]
    json.dump(jobs,open(f"{D}/jobs.json","w"),ensure_ascii=False)
    subprocess.run(["python3","tts_kokoro.py",f"{D}/jobs.json"],check=True)
    clips=[]; alist=[]; T=0
    for i,(img,pre,fy,narr,cr) in enumerate(cfg["scenes"]):
        base=f"{D}/n{i}"
        starts=json.load(open(base+".json")); ad=dur(base+".wav")
        d=round(ad+0.25,2); LEAD=0.0
        caps=[[st,["".join(ch for ch in l if ch not in "、。") for l in part.split("|")]] for st,part in zip(starts,narr.split("/"))]
        # source size after precrop
        iw,ih=(map(int,pre.split(":")[:2]) if pre else map(int,subprocess.check_output(["ffprobe","-v","error","-show_entries","stream=width,height","-of","csv=p=0",img],text=True).strip().split(",")))
        s=max(W/iw,MH/ih)*1.10; sw=int(iw*s)//2*2; sh=int(ih*s)//2*2
        x0=(sw-W)/2; y0=max(0,min(sh-MH,(sh-MH)*fy*2 if fy<0.5 else (sh-MH)*fy))
        y0=max(0,min(sh-MH,sh*fy-MH/2))
        px=min(x0,40)
        f=[f"color=black:s={W}x{H}:d={d}:r=30[bg]",
           (f"[0:v]crop={pre}," if pre else "[0:v]")+f"scale={sw}:{sh},setsar=1,crop={W}:{MH}:'{x0}-{px}+{2*px}*t/{d}':{y0}[m]",
           f"[bg][m]overlay=0:{MY0}:shortest=1[v0]"]
        dr=[]
        t1,t2=cfg["title"]; fs=min(fit(t1,130,980),fit(t2,130,980))
        for j,(t,col) in enumerate([(t1,"0xFFE100"),(t2,"0xFF4A1C")]):
            dr.append(f"drawtext=fontfile={FONT}:text='{esc(t)}':fontsize={fs}:fontcolor={col}:borderw=9:bordercolor=black:shadowcolor=black@0.8:shadowx=0:shadowy=6:x={CX}-text_w/2:y={190+j*int(fs*1.18)}")
        for c,(st,txt) in enumerate(caps):
            a=LEAD+st-0.05; b=(LEAD+caps[c+1][0]-0.05) if c+1<len(caps) else d
            cfs=min(fit(l,86) for l in txt); lh=int(cfs*1.15)
            for li,l in enumerate(txt):
                yy=MY1-40-cfs-(len(txt)-1-li)*lh
                dr.append(f"drawtext=fontfile={FONT}:text='{esc(l)}':fontsize={cfs}:fontcolor=0xFFF000:borderw=9:bordercolor=black:x={CX}-text_w/2:y={yy}:enable='between(t,{a:.2f},{b:.2f})'")
        dr.append(f"drawtext=fontfile={FONT}:text='{esc('写真：'+cr)}':fontsize=30:fontcolor=0xBBBBBB:x={CX}-text_w/2:y={MY1+8}")
        fc=";".join(f)+";[v0]"+",".join(dr)+f",fade=t=in:st=0:d=0.2,fade=t=out:st={d-0.2}:d=0.2,format=yuv420p[v]"
        out=f"{D}/s{i}.mp4"
        r=subprocess.run(["ffmpeg","-y","-loglevel","error","-loop","1","-t",str(d),"-i",img,"-filter_complex",fc,"-map","[v]","-r","30","-c:v","libx264","-profile:v","main","-level","4.0","-preset","medium","-crf","20","-t",str(d),out],capture_output=True,text=True)
        if r.returncode: print(r.stderr[-800:]); sys.exit(1)
        clips.append(out); alist.append((base+".wav",T+LEAD)); T+=d
        print(key,i,d,[c[1] for c in caps])
    open(f"{D}/list.txt","w").write("".join(f"file '{os.path.basename(c)}'\n" for c in clips))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{D}/list.txt","-c","copy",f"{D}/v.mp4"],check=True)
    ins=[];fl=[]
    for i,(m,t) in enumerate(alist):
        ins+=["-i",m]; ms=int(t*1000); fl.append(f"[{i+1}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{i}]")
    fl.append("".join(f"[a{i}]" for i in range(len(alist)))+f"amix=inputs={len(alist)}:normalize=0,apad=whole_dur={T},atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    r=subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{D}/v.mp4"]+ins+["-filter_complex",";".join(fl),"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart",cfg["out"]],capture_output=True,text=True)
    print(r.returncode,r.stderr[-500:],cfg["out"],T)
for k in sys.argv[1:]: build(k)
