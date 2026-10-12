import json,subprocess,sys,os
SP=os.path.dirname(os.path.abspath(__file__))
src=open(SP+"/build_telop.py").read()
ns={}; exec(src[src.index("V={"):src.index("def esc")],ns); V=ns["V"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
INFO={
"tug":dict(file="雑学_綱引きはオリンピック競技",head="綱引きは昔オリンピック競技だった",neta="1900年から1920年まで、綱引きはオリンピックの競技種目だった",
 why=["身近な遊びが五輪種目だったという意外さ。","1908年のブーツ抗議という、オチになる実話がある。","当時の写真がパブリックドメインで残っている。"],
 src=["綱引きは1900年パリ大会から1920年アントワープ大会まで実施(1906年の中間大会でも実施)。","1908年ロンドン大会は、シティ・オブ・ロンドン警察が金、リバプール警察が銀、ロンドン警視庁K分署が銅(英国の警察チームが独占)。※銀と銅を逆に書く資料も1つある。動画では「金・銀・銅を警察チームが独占」とだけ言っている。","リバプール警察は勤務用のブーツで出場し、アメリカが抗議。抗議は退けられ、アメリカは棄権した。",
  "[Wikipedia: Tug of war at the 1908 Summer Olympics](https://en.wikipedia.org/wiki/Tug_of_war_at_the_1908_Summer_Olympics)","[Topend Sports: Tug-of-War at the Olympics](https://www.topendsports.com/events/discontinued/tugofwar.htm)","[Mental Floss: Tug of War Used to Be an Olympic Sport](https://www.mentalfloss.com/article/55107/tug-war-used-be-olympic-sport)","[Liverpool City Police: Sporting achievements](https://www.liverpoolcitypolice.co.uk/articles/sport/)"],
 note=["最後の場面の写真(1912年の英国チーム)は、話の流れのイメージとして使っている。1908年の写真ではない。","4・5場面目は1904年セントルイス大会の写真を切り抜いたもの。1908年の写真ではない(イメージ)。"]),
"gorilla":dict(file="雑学_ゴリラの学名",head="ゴリラの学名はゴリラ・ゴリラ・ゴリラ",neta="ゴリラの学名はゴリラ・ゴリラ・ゴリラ",
 why=["言葉の響きだけで笑える。","学名の仕組み(属・種・亜種)という、ちゃんとした理由がある。","CC0(自由に使える)の写真がそろう。"],
 src=["ニシローランドゴリラの学名は Gorilla gorilla gorilla(属・種・亜種)。","[Wikipedia: Gorilla](https://en.wikipedia.org/wiki/Gorilla)","[National Geographic: Western lowland gorilla](https://www.nationalgeographic.com/animals/mammals/facts/western-lowland-gorilla)","[U.S. Fish & Wildlife Service: Western lowland gorilla](https://www.fws.gov/species/western-lowland-gorilla-gorilla-gorilla-gorilla)",
  "「動物では同じ語のくり返しが認められ、植物では禁止」は、動物命名規約と植物命名規約の違いによるもの。この点は今回の検索結果では確認しておらず、私の知識に基づく。公開前に確認するのが安全。"],
 note=["写真はすべて CC0 で、クレジット表記は必須ではないが、動画内に撮影者名を表示している。"]),
"gogh":dict(file="雑学_ゴッホの売れた絵",head="ゴッホが生前に売れた絵は1枚だけ?",neta="ゴッホが生きている間に売れた自身の絵はたったの一枚だけ",
 why=["今は超高額で売れる画家なのに、という大きなギャップ。","売れた絵(赤い葡萄畑)と、買った人がはっきり分かっている。","ゴッホの絵はパブリックドメインで使える。"],
 src=["《赤い葡萄畑》は1890年のブリュッセルの展覧会で、画家アンナ・ボックが400フランで購入(弟テオの帳簿に記録)。","アンナ・ボックは1906年に1万フランで売却。","ゴッホは1890年7月に死去。","「売れたのは1枚だけ」は、確かな記録が残るのが1枚という意味。ほかにも売れた可能性を示す資料があり、The Art Newspaper は「1枚だけではなかった」と論じている。動画でもそう説明している。",
  "[Wikipedia: The Red Vineyard](https://en.wikipedia.org/wiki/The_Red_Vineyard)","[Van Gogh Letters: letter 855](https://vangoghletters.org/vg/letters/let855/letter.html)","[The Art Newspaper: Why did Van Gogh fail to sell his work?](https://theartnewspaper.com/2022/06/03/why-did-van-gogh-fail-to-sell-his-work)","[Artprice](https://news.artprice.com/de/13016/what-is-the-only-painting-sold-during-van-gogh-s-lifetime-and-why-is-it-so-important)"],
 note=[]),
}
INFO.update({
"mike":dict(file="雑学_三毛猫はほぼメス",head="三毛猫のほとんどはメス",neta="三毛猫の99％はメス",
 why=["身近な猫の話で、理由(遺伝)まで説明できる。","オスがとても珍しい、という続きがある。","パブリックドメインの三毛猫の写真がある。"],
 src=["毛色(オレンジと黒)を決める遺伝子はX染色体にあり、両方を持てるのはX染色体が2本のメス。オスの三毛猫はXXYなどの珍しいケース。",
  "[Wikipedia: Calico cat](https://en.wikipedia.org/wiki/Calico_cat)","[PangoVet: Are calico cats always female?](https://info.pangovet.com/pet-health-wellness/cats/are-calico-cats-always-female)",
  "「オスは約3000匹に1匹」という数字は多くのサイトにあるが、元になった研究は見つけていない。動画では「数千匹に1匹とも言われる」とした。"],
 note=["写真はすべて同じ1匹の猫(パブリックドメイン)。"]),
"otter":dict(file="雑学_ラッコのポケット",head="ラッコの脇にはポケットがある",neta="ラッコは気に入った石を使い続け、使わない時は脇のポケットにしまう",
 why=["かわいい動物の、意外な体のしくみ。","道具(石)を使う話につながる。","国立公園局(パブリックドメイン)などの写真がある。"],
 src=["ラッコの前足の下にはたるんだ皮があり、ポケットのように食べ物や石をしまう。石は胸の上に置いて貝を割るのに使う。",
  "[The Ethogram: Otter Pockets](https://theethogram.com/2019/11/24/sunday-sketch-otter-pockets/)","[ZME Science: Sea otters' favorite rock](https://zmescience.com/ecology/animals-ecology/sea-otters-favorite-rock)","[BBC Wildlife](https://www.discoverwildlife.com/animal-facts/tv/sea-otter-spy-camera-bbc)",
  "「お気に入りの石を何年も使う」は資料によって強さが違い、BBC Wildlife は「使いやすい石を持ち続けるだけ」とも説明している。動画では「使いやすい石を使い続けることもある」とした。"],
 note=[]),
"seahorse":dict(file="雑学_タツノオトシゴはオスが出産",head="タツノオトシゴはオスが出産する",neta="タツノオトシゴはオスが卵を産む",
 why=["「オスが出産」という強い意外さ。","NOAA(米国海洋大気庁)の公式ページで確認できる。","CC0の写真がある。"],
 src=["メスがオスの育児嚢に卵を移し、そこで受精。オスが子を育てて産む。シードラゴン(リーフィーシードラゴンなど)も同じくオスが子を育てる。",
  "[NOAA: Are seahorses fish?(男性の妊娠について)](https://oceanservice.noaa.gov/facts/seahorse.html)","[Science News: Pregnant—and Still Macho](https://www.sciencenews.org/article/pregnant-and-still-macho)",
  "ネタ元の「オスが卵を産む」は正確ではないため、「メスが卵を入れ、オスが出産する」と直した。"],
 note=["5場面目の写真はタツノオトシゴの仲間のシードラゴン(ウィーディーシードラゴン)。"]),
"boycott":dict(file="雑学_ボイコットは人の名前",head="ボイコットは人の名前",neta="ボイコットという言葉はボイコットされた人の名前",
 why=["よく使う言葉の由来という意外さ。","1880年の出来事として、はっきり記録がある。","当時の風刺画・版画がパブリックドメイン。"],
 src=["チャールズ・ボイコットはアイルランド・メイヨー州でアーン卿の土地の管理人。1880年、土地同盟の呼びかけで、地元の人々が働くのをやめ、店も取引を断った。収穫のために、兵士に守られた作業隊が送られた。",
  "[Wikipedia: Charles Boycott](https://en.wikipedia.org/wiki/Charles_Boycott)","[World Wide Words: Boycott](https://worldwidewords.org/qa-boy1.html)","[Amusing Planet: The Man Who Became a Verb](https://www.amusingplanet.com/2023/01/charles-boycott-man-who-became-verb.html)"],
 note=[]),
"kame":dict(file="雑学_カメハメハの名前の意味",head="カメハメハの名前の意味",neta="カメハメハ大王のカメハメハは「孤独な人」という意味",
 why=["名前の響きと意味のギャップ。","命を狙われて育った、という物語がある。","肖像画や銅像の写真が自由に使える。"],
 src=["カメハメハの意味は「とても孤独な者」または「選び分けられた者」。生まれてすぐ殺すよう命じられたが、ひそかに育てられ、成人してこの名を名乗った(ブリタニカ)。",
  "[Britannica: Kamehameha I](https://www.britannica.com/biography/Kamehameha-I)","[Country Reports: King Kamehameha I](https://countryreports.org/articles/king-kamehameha-i)",
  "6月11日のカメハメハ・デーはハワイ州の祝日。","名前の語源そのものは、資料によって説明が違う。"],
 note=[]),
})
AUDIO="""## 音声
- ナレーションのみ。BGMは入れていない(投稿するときに、YouTubeの音源から選ぶ)。
- ナレーション: オープンソースの音声合成 Kokoro(Apache License 2.0。商用利用可)の女性の声 jf_alpha。速さ 1.3倍。音量は約 -14 LUFS。
- 字幕は、ナレーションの区切りごとに切り替わる。
"""
LAYOUT="""## 画面の作り
- 上に固定の大きなタイトル(1行目は黄、2行目は赤)、まん中に写真、写真の下に、ナレーションに合わせて切り替わる黄色の字幕。背景は黒。
- 文字: M PLUS 1p Black(SIL Open Font License。商用利用可)。
- 下 480px には文字を置いていない。字幕とクレジットは、右下のボタンにかからないよう中央から左右 350px 以内。
"""
def write(key,outdir):
    cfg=V[key]; I=INFO[key]; meta=json.load(open(f"{SP}/next/{key}/meta.json"))
    t=0; rows=[]
    for i,(img,pre,fy,narr,cr) in enumerate(cfg["scenes"]):
        d=round(dur(f"{SP}/telop_k/{key}/n{i}.wav")+0.25,2)
        caps=" → ".join(c.replace("|"," ").replace("、","").replace("。","") for c in narr.split("/"))
        rows.append(f"| {t:.1f}〜{t+d:.1f} | {narr.replace('/','').replace('|','')} | {caps} | {cr} |"); t+=d
    used={sc[0].split("/")[-1].rsplit(".",1)[0] for sc in cfg["scenes"]}
    cred="\n".join(f"| [{m['title'].replace('File:','')}]({m['page']}) | {m['lic']} | {m['artist'] or '不明'} |" for k,m in meta.items() if k in used)
    md=f"""# 雑学ショート「{I['head']}」台本とクレジット

- 動画: `{I['file']}.mp4`(縦1080×1920、約{t:.1f}秒、ナレーションと字幕入り・BGMなし)
- ネタ元: https://hq-improve.com/zatsugaku/ 「{I['neta']}」

## 選んだ理由
"""+"".join(f"- {w}\n" for w in I["why"])+f"""
## タイトル(画面上部に固定)
- 1行目(黄): {cfg['title'][0]}
- 2行目(赤): {cfg['title'][1]}

## 台本
| 秒 | ナレーション | 字幕の切り替わり | 写真クレジット |
|---|---|---|---|
"""+"\n".join(rows)+"\n\n"+LAYOUT+"\n"+AUDIO+"\n## 事実の出典\n"+"".join(f"- {x}\n" for x in I["src"])+f"""
## 写真クレジット(すべてWikimedia Commons)
| ファイル | ライセンス | 作者 |
|---|---|---|
{cred}
"""+("\n## 注意\n"+"".join(f"- {x}\n" for x in I["note"]) if I["note"] else "")
    open(f"{outdir}/{I['file']}_台本とクレジット.md","w").write(md); print(I["file"],t)
for k in sys.argv[1:]: write(k,os.path.join(SP,"..","台本とクレジット"))
