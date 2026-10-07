# 日本語圏YouTubeショートの「参加型ショートアニメ」チャンネル網羅調査（規模・成長・投稿頻度の実データ、2026-10-07取得）

**取得方法と注記（全数値は2026-10-07にYouTube公開ページから直接取得）**
- 検索: YouTube検索結果ページ（`results?search_query=`）を日本語/英語の計100語で取得し、`videoRenderer`/`channelRenderer`/`shortsLockupViewModel`から動画・チャンネルを抽出。ショート動画→チャンネルの紐付けはoEmbed API、投稿日・正確な再生数は`youtubei/v1/next`（視聴ページ相当。watch/shortsページ本体はbot検出で不可）で取得。
- チャンネル指標: `/about`（登録者数・総再生数・登録日・動画本数・国）、`/shorts`タブ先頭48本（タイトル・概算再生数。YouTube表示の丸め値「64万」等）、RSSフィード（直近15本の投稿日→週あたり投稿本数）。
- 「参加型」判定はタイトル正規表現（指を置|指を動か|THUMB|つまんで|タップ|止めると|どっち|YES|目を閉じ 等）。誤検出（例: 「指を切る」）を目視で除外して本文に記載。
- **Social Blade・ユーチュラ・hypeauditorは403、playboard/vidIQは429、Wayback MachineはプロキシのEgress policyで遮断**→ 登録者推移の時系列は取得不可（Gapsに記載）。代替として「開設日→現在の登録者数」「参加型回と通常回の再生数差」「投稿日付き参加型動画の四半期別件数」を使用。
- 元データ・集計スクリプト: `empirical/`（`search_raw*_2026-10-07.json`=検索ヒット3,575件、`oembed*_2026-10-07.json`=617本の動画→チャンネル解決、`channels_2026-10-07.json`=163チャンネルの詳細、`video_dates_merged_2026-10-07.json`=914本の投稿日・再生数、`dated_participatory_videos_2026-10-07.json`=型分類済み、`summary_2026-10-07.json/.csv`・`summary_table.txt`=チャンネル集計、`formats_summary_2026-10-07.txt`=型別時系列、スクリプト `yt.py ch2.py vdates.py consolidate.py formats.py`）。

## Q1. どのチャンネルが、どの型を、オリジナル／二次創作のどちらでやっているか（網羅インベントリ）

### Takeaway
日本語圏で「参加型ショートアニメ」を**継続シリーズ**として回しているアニメ/手描き系チャンネルは約15（カッキー、もやりつ、なで肩、タカノメ、そろ谷、Plott系3ch、慎本真、Bee Domina、omi_irotoridori、リンクの作業場、ミリプロ等）、**単発〜数本**で試したチャンネルは100以上確認できた。型は「リズムに合わせて指を動かす（THUMB DANCE）」が2025年8月以降に圧倒的多数（日付判明分284本）、次いで「右左どっち/2択」（170本、2022年〜Plott系が主導）、「指を置いて/ここに指」（116本、ただし再生数中央値は5千回と低い）、「ピッタリ止めると（タップ停止）」（87本、2022–23年に一巡したあと2025年に再燃）。キャラは**二次創作が多数派**（ボカロ、呪術廻戦、鬼滅、ヒロアカ、ポケモン、原神/鳴潮等のゲーム、ホロライブ）で、オリジナルキャラで大きく当てているのはPlott（カレコレ/フラグちゃん/ブラックチャンネル）、そろ谷、お文具、へっぽこアニメ、虹深ぬふ、ララァ、マイ部アニメ、杰克大魔王（中国語圏）に限られる。

### Cited Findings
**A. 継続シリーズ化している日本語チャンネル（型／キャラ／規模）**
- カッキー創作チャンネル（@Kakki）: 登録129万人、2015/01/03開設、907本、総再生14.0億回、国=日本。型=リズムに合わせて指を動かす／指を置いて遊ぶ／タイミング良くタップ停止／どっち2択。キャラ=二次創作（初音ミク・重音テト等ボカロ、ポケポケ、鳴潮、アークナイツ、ソニック、東方）。日付判明の参加型33本（2025/09〜2026/09）、初回は2025/09/02「リズムに合わせて指を動かして遊ぶアニメ【ポケポケ】」646万回 — [YouTube @Kakki](https://www.youtube.com/@Kakki/shorts); 投稿日・再生数は [empirical/video_dates_merged_2026-10-07.json](empirical/video_dates_merged_2026-10-07.json)
- もやりつの手描きアニメ部屋（@MOYARITSU）: 97.9万人、2010/06開設、332本。型=THUMB DANCE系（2025/10/15〜12/30に10本）→「指でつまんでみてね！(Auto Walk Mode ACTIVATED)」パート1〜4（2026/01/01〜01/09、120万〜706万回）。キャラ=呪術廻戦二次創作。2026/01中旬以降は参加型を出していない（直近48本中2本のみ） — [YouTube @MOYARITSU](https://www.youtube.com/@MOYARITSU/shorts)
- なで肩（@nadegataaaa）: 13.1万人、2023/07開設、88本。型=THUMB DANCE CHALLENGE Part1〜15（2025/08/24〜2026/07/03）＋「指でつまんでみてね！」2本＋「Close your eyes to the rhythm」1本。キャラ=僕のヒーローアカデミア二次創作（手描き） — [YouTube @nadegataaaa](https://www.youtube.com/@nadegataaaa/shorts)
- タカノメ（@タカノメ_illust）: 7.15万人、2021/10開設、91本。型=「指を動かすやつ○○Ver」25本（2025/10/18〜2026/01/17）。キャラ=鬼滅の刃（柱・鬼ごとに1本ずつ）、おそ松さん、呪術廻戦、フリーレン。RSS最終投稿2026/01/25で以後停止 — [YouTube @タカノメ_illust](https://www.youtube.com/@%E3%82%BF%E3%82%AB%E3%83%8E%E3%83%A1_illust/shorts)
- そろ谷のアニメっち（@sorotani）: 127万人、2021/06開設、537本。型=「リズムに合わせて(親)指を動かすやつ」3〜6（2025/12/05・2026/01/04・04/07・09/11、306万〜1,076万回）。キャラ=オリジナル — [YouTube @sorotani](https://www.youtube.com/@sorotani/shorts)
- 混血のカレコレ（@karekoreya、Plott）: 307万人、2019/09開設、3,565本、週10.5本。型=タップでぴったり止める（2022/06/09 215万、2022/08/09、2023/04/28、2025/05/06）、右左どっち（2024/02/29〜、最大1,164万回「右左どっちでメイクする」2024/03/26）、Yes or Noチャレンジ（2024/07/16 235万）、THUMB DANCE（2025/10/17 420万）。キャラ=オリジナル — [YouTube @karekoreya](https://www.youtube.com/@karekoreya/shorts)
- 全力回避フラグちゃん!（@flag__chan、Plott）: 248万人、週21本。「右左どっち？」2023/05/22が3,793万回（本調査で最大の日本語参加型ショート）、「右左どっち？2」2023/07/31 791万回、「右左どっちでメイクする？」2025/08/18 292万回。キャラ=オリジナル — [YouTube @flag__chan](https://www.youtube.com/@flag__chan/shorts)
- ブラックチャンネル（@black_orechan、Plott）: 130万人。「【画面をタップ！】今日の運勢は？」2022/07/22 8.7万、「タップしてピッタリ止めると」25万、「右左どっち？でイタズラされた結果」354万、「指ハート③」151万。オリジナル — [YouTube @black_orechan](https://www.youtube.com/@black_orechan/shorts)
- テイコウペンギン（@teipen.official、Plott）: 213万人。「ここに指を置いてくれないか」2024/10/03 99万回（直近48本中央値3.6万の約27倍）。オリジナル — [YouTube @teipen.official](https://www.youtube.com/@teipen.official/shorts)
- SS manga diary-慎本 真-（@ssmangadiary）: 98.7万人、2020/01開設。型=「YES??NO??イラストチャレンジ」16本（2025/04〜2026/10、直近48本中11本、参加型中央値18万 vs 通常10万）。右左どっち系の前身「右？左？どっち？選んだ設定だけでイラスト描いてみたw8」2022/10/26 358万。キャラ=オリジナル（イラスト） — [YouTube @ssmangadiary](https://www.youtube.com/@ssmangadiary/shorts)
- ミリプロ（@Mil_Pro、VTuber事務所）: 47.3万人。「【マイクラ】安全な床を選んで生き残れ！」3本（100万〜203万）、「タップするたびに成長したら…」2025/12/10 274万、「右左どっち？」106万。キャラ=所属VTuberのアニメ化 — [YouTube @Mil_Pro](https://www.youtube.com/@Mil_Pro/shorts)
- Bee Domina（@BeeDomina）: 1,050人、2021/02開設、30本。直近48本中24本が「リズムに合わせて指を動かしてね♪○○編」（2025/12〜2026/10、中央値1.3万・最大2.3万、通常回中央値2,540）。ボカロ二次創作。小規模だが参加型でチャンネルを回している例 — [YouTube @BeeDomina](https://www.youtube.com/@BeeDomina/shorts)
- omi_irotoridori（@omi_irotoridori）: 242人、2025/03開設、137本。直近48本中38本が参加型（「指を置いてね☝🏻」ジブリ二次創作、「タップで止めてね！」サンリオ/自作キャラ「おろろ」）。再生数中央値26回、最大3,526回 — [YouTube @omi_irotoridori](https://www.youtube.com/@omi_irotoridori/shorts)
- リンクの作業場（@linku_no_sagyouba）: 1,000人、2025/09開設。THUMB DANCE CHALLENGE Part1〜7（BLEACH二次創作、2026/07〜10、1,305〜2.4万回）＋Close your eyes — [YouTube @linku_no_sagyouba](https://www.youtube.com/@linku_no_sagyouba/shorts)
- アマタのアニメ（@AnimationOfAmata）: 2,260人、2013/12開設。「リズムに合わせて親指を動かしてください」ver1〜5（2026/07〜09、1,616〜4,828回）。オリジナル — [YouTube @AnimationOfAmata](https://www.youtube.com/@AnimationOfAmata/shorts)
- yuusuube（@yuusuube）: 4万人、2020/05開設、278本。「○○でピッタリ止めると…⁉」44本（2022/06/03〜2023/07/07、鬼滅・スパイファミリー二次創作、最大204万）。RSS最終投稿2023/07/08で停止 — [YouTube @yuusuube](https://www.youtube.com/@yuusuube/shorts)
- ナカチコChannel（@nakachiko_ch）: 9,690人。「手を動かして見てね」7本（2022/10〜11、カラフルピーチ/呪術廻戦/カレコレ二次創作、6,762〜6.6万回）。最終投稿2023/04/15で停止 — [YouTube @nakachiko_ch](https://www.youtube.com/@nakachiko_ch/shorts)
- お文具のアニメ（@imoko_iimo）: 111万人、2020/01開設、755本。参加型は長尺（1〜3分）の「指をつかって見る動画」1〜7（6年前、35万〜260万回）、「指を置いて見るアニメ」（5年前、114万）、「手を使って見る動画」（2024/02、343万）、「手をかざして見る動画 #視聴者参加型」218万。直近48本のショートには参加型なし。オリジナル — [YouTube @imoko_iimo](https://www.youtube.com/@imoko_iimo)
- みっちーのアニメ（@piyorigo）: 32.8万人、2008/02開設。「リズムに合わせて指を動かしてね！THUMB DANCE CHALLENGE!!」16万、「画面タップで3月のラッキーキャラを決めよう！」4.7万、「どっちが正しい？」12万（2026/02〜07に3本）。オリジナル — [YouTube @piyorigo](https://www.youtube.com/@piyorigo/shorts)
- おゆびちゃん（@oyubi）: 242人、2021/02開設、11本、最終投稿2021/08/16（停止） — [YouTube @oyubi](https://www.youtube.com/@oyubi)

**B. 1〜4本の単発投稿で参加型を試したアニメ/イラスト系チャンネル（主なもの、再生数は当該回）**
- 虹深°ぬふ（@NijipukaNuhu、42.1万、オリジナル）: THUMB DANCE 857万（2025/09）、右と左どっち 127万（2026/09） — [YouTube](https://www.youtube.com/@NijipukaNuhu/shorts)
- ララァ（@laraa4467、81.1万、オリジナル・アナログ絵）: どっちが好き？325万、2択で仕事選んでも怒らない彼女 236万 — [YouTube](https://www.youtube.com/@laraa4467/shorts)
- マイ部アニメ（@maibuanime、92.3万、オリジナル）: リズムに合わせて指を動かそう 2026/02/27 510万、右左どっち？海洋生物Ver 637万 — [YouTube](https://www.youtube.com/@maibuanime/shorts)
- へっぽこアニメ（@heppoko_anime、10.9万、2024/07開設、オリジナル）: 「リズムに合わせて指動かすやつ」1・2（2026/02〜03、16万・13万、通常回中央値7.4万） — [YouTube](https://www.youtube.com/@heppoko_anime/shorts)
- 魔法少女アルト（@alto_magical、14万、オリジナル）: THUMB DANCE ①620万（通常回中央値9.3万の約67倍）、②51万、③20万（2025/08〜09） — [YouTube](https://www.youtube.com/@alto_magical/shorts)
- zakkuri24（@zakkuri24CH、27.2万、原神二次創作）: THUMB DANCE CHALLENGE! GENSHIN 2025/08/16 993万（日本語圏で日付判明の最古THUMB DANCE）、胡桃＆七七編 83万、指でつまんでみてね 2026/01/04 178万 — [YouTube](https://www.youtube.com/@zakkuri24CH/shorts)
- Rse143（@Rse-143、10万、2025/03開設、鬼滅二次創作・英語題）: Thumb dance with akaza 1,365万、giyu 1,147万、sanemi 35万 — [YouTube](https://www.youtube.com/@Rse-143/shorts)
- ハンドレッドノート（@HundredNote-Official、46.9万、週26本、オリジナル）: 一緒に指を動かして！204万・114万、ピッタリ止めると 6.1万、究極の2択 30万 — [YouTube](https://www.youtube.com/@HundredNote-Official/shorts)
- ヒロたま!ヒロくん（@hirotama-hirokun、32.4万）: THUMB DANCE 218万（通常82万） — [YouTube](https://www.youtube.com/@hirotama-hirokun/shorts)
- 鷲羽アスカ（@WashuAsuka、13万、VTuber手描き）: MIKU×Close your eyes to the rhythm 2025/12/07 1,327万（通常回中央値2万）、直近48本中11本が参加型（中央値95万） — [YouTube](https://www.youtube.com/@WashuAsuka/shorts)
- クロム（@crcat-H、6万、ブルアカ二次創作）: Close your eyes to the rhythm 168万・90万・79万（2025/12） — [YouTube](https://www.youtube.com/@crcat-H/shorts)
- 斎木こまり（@saikikomari_np、7万、VTuberイラスト）: 直近48本中20本が参加型（中央値33万 vs 通常12万）、Close your eyes 67万 — [YouTube](https://www.youtube.com/@saikikomari_np/shorts)
- えーてぃーあい ちゃんねる（@AnimeThemedItemsChannel、184万、ねんどろいどコマ撮り・鬼滅）: リズムに合わせて指を動かそう その4 270万、その8 127万 — [YouTube](https://www.youtube.com/@AnimeThemedItemsChannel/shorts)
- アニメーにょン（ボカロ手描き）: 指動かすやつにがんばってテトが合わせるアニメーション 156万 — [oembed3](empirical/oembed3_2026-10-07.json)
- ゆめう ゆいの創作部屋（2.79万）: リズムに合わせて指動かすやつ描いてみた 236万、テトバージョン 99万（2025/09） — [YouTube](https://www.youtube.com/@%E3%82%86%E3%82%81%E3%81%86%E3%82%86%E3%81%84/shorts)
- びふぉあ（@bihuloa1、2.45万）: 指を動かすアニメ描いてみた 161万・83万（2025/09〜12、通常4.4万） — [YouTube](https://www.youtube.com/@bihuloa1/shorts)
- 透々ルチカ（@SukitouLuccica、3万）: THUMB DANCE 169万・85万（通常1万） — [YouTube](https://www.youtube.com/@SukitouLuccica/shorts)
- HARUHO（@haruho0、1.22万、オリジナル）: THUMB DANCE 42万、他5本は1.3〜3.7万（2025/09〜10） — [YouTube](https://www.youtube.com/@haruho0/shorts)
- こみレイン（@komileinch、1,960人）: THUMB DANCE 19万・12万（2025/09〜10、通常1,461）、最終投稿2026/01/15 — [YouTube](https://www.youtube.com/@komileinch/shorts)
- いずもゆう（@12m0channel、5,060人）: THUMB DANCE 26万（通常中央値659） — [YouTube](https://www.youtube.com/@12m0channel/shorts)
- ギャルすぎ！（@toogal_moregal_mottogal、45.5万、YouTubeアニメ）: THUMB DANCE 19万（2025/12） — [YouTube](https://www.youtube.com/@toogal_moregal_mottogal/shorts)
- 運命の巻戻士 公式（@MAKIMODOSI、56.8万）: THUMB DANCE 66万（2025/09） — [YouTube](https://www.youtube.com/@MAKIMODOSI/shorts)
- 女子力高めな獅子原くん（@shishiharakun、118万、GANMA）: 右左どっち？249万、2人で指ハート 755万 — [YouTube](https://www.youtube.com/@shishiharakun/shorts)
- ちぐさくん【AMPTAK】（@Tigusakun、132万、オリジナル）: 究極の2択…君ならどっちを選ぶ？【2】603万・【3】378万、右左どっち⁉181万（2024/03〜2026/08に7本） — [YouTube](https://www.youtube.com/@Tigusakun/shorts)
- 右左どっち系をやったその他: まぜ太 265万、罪人転校生 242万（2025/05）、ゆずざくろ「デスゲームで右左どっちするやつ」113万（2026/08）、ゴウキブック 58万（2022/08）、ボンバーにゃん 16万（2026/06〜07に4本）、いれいす 23万・56万、莉犬くん 100万・90万、すとぷり 115万、すにすて 11万、AMPTAKxCOLORS 160万・110万・98万、プリズマジカ 2万 — [dated list](empirical/dated_participatory_videos_2026-10-07.json)
- 指を置いて系をやったその他（多くが数百〜数万回）: やしゅし「指おいてね🐰」255万（2025/12、通常1.1万）、hololive公式「ここに指を置いてね」276万（ロボ子さん）、トキイチ 15万（2021/10）、ぽぱい（ポーランドボール）22万、めい「ここに指を置いてね！恋愛フラグver」22万、カブウサギ「指を置くとくっつくよ！」2.4万、モンキーランド「⭕️に指を置いてね☝️」4本（2.5〜8.5万、2023/08〜2024/02、最終投稿2024/04）、みかん 4,553、ほけまる 2,781、せいのすけ 2,882 — [dated list](empirical/dated_participatory_videos_2026-10-07.json)

**C. 公式・企業・VTuberの参加型（アニメチャンネルではないが同型）**
- ポケモン公式（@PokemonCoJp、407万）: 「【公式】『ポケポケ』リズムに合わせて指を動かそう！」2026/02/26・03/11 44万・68万、「ポケポケ1周年記念」50万 — [YouTube](https://www.youtube.com/@PokemonCoJp/shorts)
- Google Play Japan公式: 「【アニメ】リズムに合わせて指を動かそう！#パイモン」850回 — [search_raw](empirical/search_raw_2026-10-07.json)
- ねこいちさん【第一三共ヘルスケア】（@neko_ichi_san、3,470人）: 「タイミングに合わせて指を動かしてにゃ」等4本（5,984〜5万） — [YouTube](https://www.youtube.com/@neko_ichi_san/shorts)
- アミューズ公式【ショートアニメ】（@amuseshort、2,920人）: ぽてうさろっぴー「Thumb Dance Challenge」3,310回 — [YouTube](https://www.youtube.com/@amuseshort/shorts)
- VTuber個人勢・事務所（シクフォニ 79万・64万、雨乃こさめ 24万・20万・18万、椎名唯華 54万、博衣こより 24万、293Project 74万・62万、エビフライ 75万、CO-DA 83万、こみレイン、一色イズ、菱垣ゆり、VEE、Mixstgirls等）がTHUMB DANCE／指でつまんで／Close your eyesを1〜3本ずつ投稿 — [oembed](empirical/oembed_2026-10-07.json)

**D. 日本語圏外の参照点（起源・比較用）**
- 杰克大魔王㊣（@HandsomeJack-theBigDevil、1,090万人、2023/08開設、241本、英語題・中国語圏）: THUMB DANCE CHALLENGE! Part4 2025/08/22 2,980万、Part8 2025/09/12 2,084万、Part11 2025/11/03 2,709万。直近48本中参加型4本の中央値326万 vs 通常193万 — [YouTube](https://www.youtube.com/@HandsomeJack-theBigDevil/shorts)
- Filmora（Wondershare）の解説記事: 「親指ダンスチャレンジは2024年から2025年にかけてTikTokを中心に爆発的な人気」「杰克大魔王のTHUMB DANCE CHALLENGE動画は2480万回以上の再生数を記録」 — [filmora.wondershare.jp](https://filmora.wondershare.jp/video-editing-tips/how-to-make-thumb-dance-challenge-video.html)
- 「Put Your Finger Here」の起源は2011年4月のSkittlesのインタラクティブCM、2012年Redditで拡散 — [Know Your Meme](https://knowyourmeme.com/sensitive/memes/put-your-finger-here)
- 英語圏アニメーションメームの規模: Zane Little「Put Finger Here #flipnote」2024/02/23 3,491万、Nutshell Animations「PLACE FINGER HERE」2024/02/10 2,954万・2024/07/21 3,330万、Gigaverse「Put Your Finger Here ❤️」698万、Rse143（鬼滅）1,365万 — [dated list](empirical/dated_participatory_videos_2026-10-07.json)

### Inferences
- 日本語圏の「リズムに合わせて指を動かす」型は、2025/08中旬（zakkuri24 08/16、杰克大魔王 Part4 08/22、なで肩 08/24）に同時多発し、2025/09にカッキー・もやりつが参入して10〜12月にピーク化したと推定される（日付判明分の四半期件数: 2025Q3=87→2025Q4=190→2026Q1=108→Q2=61→Q3=97）。検索結果は近時に偏るため絶対数は参考値。
- 「オリジナルキャラ×参加型」で継続的に100万回超を出せているのはPlott（週10〜21本の量産体制）、そろ谷、お文具（長尺）、マイ部アニメ程度で、個人のオリジナル勢（HARUHO、アマタ、omi、Bee Domina）は1〜数万回に留まる傾向。二次創作勢（なで肩・タカノメ・もやりつ・Rse143）は人気IPのファン流入で初回から数百万回に達している。
- 「指を置いて」型は投稿数は多い（116本）が中央値5,167回と最も当たりにくい。一方「指でつまんで（Auto Walk）」は11本すべて2026/01で中央値75万（もやりつ・zakkuri24・なで肩が主）。

### Gaps
- 検索ベースの発見のため、タイトルに参加型キーワードを含まない参加型動画（例: 題名が「○○編」のみ）は漏れている。カレコレ・フラグちゃんの直近48本の正規表現検出が0本なのはタイトルに「#Plottアニメ」等しか含まないため。
- 国の判定は/aboutの「国」欄とタイトル言語で行い、Rse143（英語題だが日本語ハッシュタグなし、国=不明）など境界例あり。
- @starpola（すたぽら公式）、@mekuru1koma、@ataroooo、@Gigaverseはaboutページ取得に失敗。

## Q2. 各チャンネルの登録者数、直近48本の再生数（中央値・最大）、参加型回と通常回の比較

### Takeaway
直近48本（ショートタブ）で見ると、参加型回が通常回を大きく上回るのは「二次創作×THUMB DANCE」のなで肩（344万 vs 29万、約12倍）、タカノメ（181万 vs 9.1万、約20倍）、もやりつ（434万 vs 125万）、魔法少女アルト（620万 vs 9.3万）、鷲羽アスカ（95万 vs 2万）で、一方カッキーは直近48本では参加型64万 vs 通常105万と**参加型が通常回を下回る**（2026年春以降の参加型回が数十万回台に落ちているため）。

### Cited Findings
（形式: 登録者 / 直近48本 中央値→最大 / 参加型本数: 参加型中央値→最大 / 通常回中央値。全て2026-10-07、出典は各チャンネル/shortsページと [summary_table.txt](empirical/summary_table.txt)）
- @Kakki カッキー: 129万 / 89万→2,986万 / 17本: 64万→2,235万 / 105万 — [YouTube](https://www.youtube.com/@Kakki/shorts)。日付付きデータでは2025/09〜11の参加型が500万〜3,145万（例: リンレン＆ミク編 2025/10/22 3,145万、ミクテト編 10/03 2,870万、ツーショット編 10/29 2,645万、千咲編【鳴潮】11/19 2,468万）、2026/02以降は鳴潮・NIKKE・リバース1999等のゲームキャラ編が28万〜158万に低下、2026/09/30「鳴潮 心 編」3.0万。非参加型でも「リズムに合わせて単語を言ってみようチャレンジ♪ゾンビボーカロイド編」2026/01/07 2,986万、「荷物検査する空港」2026/02/06 2,390万 — [video_dates](empirical/video_dates_merged_2026-10-07.json)
- @sorotani そろ谷: 127万 / 188万→2,076万 / 1本: 306万 / 179万。参加型4本=765万・1,015万・1,076万・306万。通常回最大2,076万（「雨で濡れないように横揺れダンスで助けるヤツ」） — [YouTube](https://www.youtube.com/@sorotani/shorts)
- @MOYARITSU もやりつ: 97.9万 / 134万→1,457万 / 2本: 434万→706万 / 125万。参加型14本（2025/10〜2026/01）: 63万〜2,445万（虎杖＆脹相編 2025/11/06 2,445万、パート12 12/30 1,334万）。非参加型最大「脹相の目覚まし時計part２」2026/05/05 1,457万 — [YouTube](https://www.youtube.com/@MOYARITSU/shorts)
- @imoko_iimo お文具: 111万 / 38万→83万 / 0本 / 38万（直近ショートに参加型なし。参加型長尺は35万〜343万） — [YouTube](https://www.youtube.com/@imoko_iimo)
- @piyorigo みっちー: 32.8万 / 8.1万→130万 / 1本: 12万 / 8.0万 — [YouTube](https://www.youtube.com/@piyorigo/shorts)
- @oyubi おゆびちゃん: 242人 / ショート2本 2,644→3,089 — [YouTube](https://www.youtube.com/@oyubi)
- @nadegataaaa なで肩: 13.1万 / 46.5万→1,480万 / 20本: 344万→1,480万 / 29万。Part1 725万（2025/08/24）→Part3 1,023万→Part4 1,186万→Part7 1,146万・1,481万（2025/10/28・11/14）→Part10 214万（12/10）→Part11 154万（2026/02/07）→Part15 51万（2026/07/03） — [YouTube](https://www.youtube.com/@nadegataaaa/shorts)
- @タカノメ_illust: 7.15万 / 49.5万→696万 / 25本: 181万→696万 / 9.1万。鬼滅Ver2 2025/10/26 650万、Ver4 11/10 697万、以後キャラ別Ver 61万〜369万、2026/01/14 15万・01/17フリーレン 17.5万で停止 — [YouTube](https://www.youtube.com/@%E3%82%BF%E3%82%AB%E3%83%8E%E3%83%A1_illust/shorts)
- @karekoreya カレコレ: 307万 / 138万→388万 / （直近48本に参加型タイトルなし）。過去参加型12本は104万〜1,164万 — [YouTube](https://www.youtube.com/@karekoreya/shorts)
- @flag__chan フラグちゃん: 248万 / 75万→270万。右左どっち？3,793万（2023/05）は直近中央値の約50倍 — [YouTube](https://www.youtube.com/@flag__chan/shorts)
- @ssmangadiary 慎本真: 98.7万 / 10万→360万 / 11本: 18万→48万 / 10万 — [YouTube](https://www.youtube.com/@ssmangadiary/shorts)
- @Mil_Pro ミリプロ: 47.3万 / 82万→388万 / 3本: 181万→203万 / 80万 — [YouTube](https://www.youtube.com/@Mil_Pro/shorts)
- @alto_magical 魔法少女アルト: 14万 / 9.5万→620万 / 3本: 51万→620万 / 9.3万 — [YouTube](https://www.youtube.com/@alto_magical/shorts)
- @NijipukaNuhu 虹深ぬふ: 42.1万 / 215万→1,136万 / 2本: 492万→857万 / 215万 — [YouTube](https://www.youtube.com/@NijipukaNuhu/shorts)
- @laraa4467 ララァ: 81.1万 / 219万→652万 / 2本: 281万→325万 / 210万 — [YouTube](https://www.youtube.com/@laraa4467/shorts)
- @maibuanime マイ部アニメ: 92.3万 / 517万→3,172万 / （参加型2本: 510万・637万は中央値と同程度） — [YouTube](https://www.youtube.com/@maibuanime/shorts)
- @heppoko_anime へっぽこ: 10.9万 / 7.9万→116万 / 2本: 14.5万→16万 / 7.4万 — [YouTube](https://www.youtube.com/@heppoko_anime/shorts)
- @hirotama-hirokun: 32.4万 / 82万→370万 / 1本: 218万 / 82万 — [YouTube](https://www.youtube.com/@hirotama-hirokun/shorts)
- @HundredNote-Official: 46.9万 / 16.5万→117万 / 2本: 18万→30万 / 16.5万 — [YouTube](https://www.youtube.com/@HundredNote-Official/shorts)
- @WashuAsuka 鷲羽アスカ: 13万 / 9万→2,451万 / 11本: 95万→1,327万 / 2万 — [YouTube](https://www.youtube.com/@WashuAsuka/shorts)
- @saikikomari_np 斎木こまり: 7万 / 17万→94万 / 20本: 33万→87万 / 12万 — [YouTube](https://www.youtube.com/@saikikomari_np/shorts)
- @Rse-143: 10万 / 22.5万→1,309万 / 1本: 35万 / 22万（過去Thumb dance 1,365万・1,147万） — [YouTube](https://www.youtube.com/@Rse-143/shorts)
- @zakkuri24CH: 27.2万 / 28.5万→178万（過去THUMB DANCE 993万） — [YouTube](https://www.youtube.com/@zakkuri24CH/shorts)
- @Akubi.demonspade あくび・でもんすぺーど（VTuber）: 52.7万 / 90万→412万 / 3本: 132万→152万 / 89万 — [YouTube](https://www.youtube.com/@Akubi.demonspade/shorts)
- @Amayo_liz 雨夜リズ（ミリプロ）: 22.6万 / 34.5万→235万 / 2本（右左どっち歌ってみた）: 107万→167万 / 30.5万 — [YouTube](https://www.youtube.com/@Amayo_liz/shorts)
- 小規模勢: @BeeDomina 1,050人 / 1.2万→8万 / 24本: 1.3万→2.3万 / 2,540; @omi_irotoridori 242人 / 24→3,526 / 38本: 26→3,526 / 24; @linku_no_sagyouba 1,000人 / 1,886→2.4万 / 9本: 4,196→2.4万 / 1,524; @AnimationOfAmata 2,260人 / 2,158→44万 / 5本: 3,091→4,828 / 2,078; @haruho0 1.22万 / 1.6万→230万 / 6本: 2.25万→42万 / 1.35万; @ritatictic 5.41万 / 1.6万→3.1万 / 6本: 1.95万→2.1万 / 1.55万 — [summary_table.txt](empirical/summary_table.txt)
- 全163チャンネルの一覧（登録者・開設日・本数・48本中央値/最大・参加型/通常回・週本数・最終投稿・参加型初出/最終・年別本数）は [summary_table.txt](empirical/summary_table.txt) / [summary_2026-10-07.csv](empirical/summary_2026-10-07.csv)

### Inferences
- 「参加型／通常の倍率」は、通常回の中央値が低いチャンネル（タカノメ9万、アルト9万、鷲羽アスカ2万、こみレイン1,461）ほど大きく、参加型は**既存ファン数に依存しない外部流入（おすすめ・ショートフィード）を獲得しやすい**フォーマットであることを示唆する。
- 逆に通常回が既に100万超の大手（カッキー、そろ谷、マイ部、ララァ）では参加型は上振れ要因にはなるが、2026年以降は必ずしも通常回を上回らない。
- 「48本中央値」はショートタブ表示の丸め値（例: 64万）に基づくため、±1桁目の精度しかない。

### Gaps
- 直近48本に参加型タイトルが含まれないチャンネル（カレコレ等）では参加型/通常の同時期比較ができない。
- ショートタブは新しい順のため、過去に参加型シリーズを終えたチャンネル（タカノメ以外）では参加型回が48本に含まれないケースがある。

## Q3. 投稿頻度（週本数）、開設時期、参加型の開始時期、登録者の伸び

### Takeaway
参加型で当たった個人勢は週0.4〜2.2本の低頻度（カッキー0.6本/週、なで肩0.42、もやりつ1.0、タカノメ2.2、そろ谷3.2）で、Plott系・事務所系は週10〜26本。参加型の開始時期は、タップ停止型=2022年6月（カレコレ・yuusuube）、右左どっち=2022年〜2023/05（Plottで3,793万）、THUMB DANCE=2025年8月（日本語圏）、Close your eyes=2025年12月、指でつまんで=2026年1月。**登録者の時系列（Social Blade等）は全て取得不可**で、開設日と現登録者数から長期の平均増加しか推定できない。

### Cited Findings
- 投稿頻度（RSS直近15本の投稿日から算出、2026-10-07）: カッキー 0.6本/週（2026/04/13〜10/04）、そろ谷 3.18、もやりつ 1.0、お文具 1.67、みっちー 2.62、なで肩 0.42（2025/10/28〜2026/07/03）、タカノメ 2.19（2025/12/08〜2026/01/25で停止）、カレコレ 10.5、フラグちゃん 21.0、テイコウペンギン 21.0、ブラックチャンネル 6.18、ハンドレッドノート 26.25、ミリプロ 8.75、慎本真 2.14、Bee Domina 1.03、omi_irotoridori 1.42、リンクの作業場 3.09、鷲羽アスカ 7.0、杰克大魔王 1.52 — [summary_table.txt](empirical/summary_table.txt)
- 開設日と現登録者数（/about）: カッキー 2015/01/03→129万（総再生14.0億）、そろ谷 2021/06/12→127万、もやりつ 2010/06/15→97.9万、お文具 2020/01/14→111万、みっちー 2008/02/21→32.8万、なで肩 2023/07/19→13.1万、タカノメ 2021/10/02→7.15万、Rse143 2025/03/31→10万、へっぽこアニメ 2024/07/31→10.9万、鷲羽アスカ 2024/02→13万、雨夜リズ 2025/02/04→22.6万、杰克大魔王 2023/08/09→1,090万、マイ部アニメ 2023/07/18→92.3万 — [channels_2026-10-07.json](empirical/channels_2026-10-07.json)
- 型ごとの日本語圏での初出（日付判明分）: 
  - タップでピッタリ止める: スプラクリップ 2022/03/22（298万、ゲーム）、yuusuube 2022/06/03、混血のカレコレ 2022/06/09（215万）、やむ 2022/06/11 — [formats_summary](empirical/formats_summary_2026-10-07.txt)
  - 右左どっち/2択: SION 2022/02/23（164万、呪術廻戦）、ゴウキブック 2022/08/09、慎本真 2022/10/26（358万）、フラグちゃん 2023/05/22（3,793万） — 同上
  - 指を置いて: トキイチ 2021/10/16（15.8万）、さやままや 2021/12/26、英語圏 ella.youtube 2022/08/15（196万） — 同上
  - 手を動かして見てね: ナカチコ 2022/10/15〜 — 同上
  - THUMB DANCE（リズムに合わせて指）: zakkuri24 2025/08/16（993万）、杰克大魔王 Part4 2025/08/22、なで肩 2025/08/24、カッキー 2025/09/02、もやりつ 2025/10/15、タカノメ 2025/10/18、そろ谷 2025/12/05 — 同上
  - Close your eyes to the rhythm: fee_macaron 2025/10/22、鷲羽アスカ 2025/12/07（1,327万）、SpaceBirbLizzy 2025/12/08、クロム 2025/12/16 — 同上
  - 指でつまんでみてね（Auto Walk Mode）: もやりつ 2026/01/01〜01/09、zakkuri24 2026/01/04、なで肩 2026/02/28 — 同上
- 四半期別の参加型投稿件数（日付判明914本中、型分類「other」除く）と再生数中央値: 2022Q3 21本/17万、2023Q1 16本/13万、2024Q1 22本/161万、2025Q2 25本/3.4万、2025Q3 87本/14万、**2025Q4 190本/25万**、2026Q1 108本/6.2万、2026Q2 61本/1.1万、2026Q3 97本/1.1万、2026Q4(10/07まで) 21本/1.3万 — [formats_summary](empirical/formats_summary_2026-10-07.txt)
- 型別の半期件数: THUMB DANCE 2025H2=181→2026H1=71→2026H2=44；右左どっち 2024H1=17、2025H2=40、2026H1=34、2026H2=37；指を置いて 2024H2=14、2025H2=18、2026H1=21、2026H2=26；ピッタリ止め 2022H2=24→2023H2=1→2025H2=16→2026H2=4 — 同上
- カッキーの参加型推移（投稿日・再生数）: 2025/09/02 647万 → 09/27 1,956万 → 10/03 2,870万 → 10/22 3,145万 → 11/19 2,468万 → 12/18 58万（スノウブレイク編）→ 12/26 2,235万（指を置いて遊ぶ）→ 2026/01/22 1,779万（アークナイツ）→ 02/05 41万 → 03/19 158万 → 04/01 1,494万（ソニック）→ 04/13 64万 → 09/30 3.0万 — [video_dates](empirical/video_dates_merged_2026-10-07.json)
- なで肩の参加型推移: 2025/08/24 725万 → 09/09 1,023万 → 09/20 1,186万 → 10/28 1,146万 → 11/14 1,481万 → 11/24 378万 → 12/10 214万 → 2026/02/07 154万 → 03/21 102万 → 04/07 79万 → 07/03 51万（参加型開始前の通常回は12万〜131万） — 同上
- タカノメの参加型推移: 2025/10/18 61万 → 10/26 650万 → 11/10 697万 → 11/15〜12/28 61万〜369万 → 2026/01/01 371万 → 01/14 15万 → 01/17 17.5万（以後投稿なし。参加型前の通常回は4.6万〜14万、例外370万1本） — 同上
- Filmora記事: 親指ダンスチャレンジは「2024年から2025年にかけてTikTokを中心に爆発的な人気」 — [filmora.wondershare.jp](https://filmora.wondershare.jp/video-editing-tips/how-to-make-thumb-dance-challenge-video.html)

### Inferences
- 日付付きデータの件数推移から、THUMB DANCE型のブームは2025年10〜12月がピークで、2026年に入って件数・中央値ともに減衰している（2026Q2〜Q3の中央値1.1万は、小規模チャンネルの後追い参入が増え、ヒット率が下がったことを示す）。
- 開設日から見ると、なで肩（2023/07開設→13.1万）、Rse143（2025/03開設→10万）、鷲羽アスカ（2024/02→13万）は参加型ヒット後1年前後で10万超に到達しており、参加型1本の数百万〜1,000万回が登録者数万人規模の押し上げに繋がった可能性が高い（ただし推移データがないため因果は未確認）。
- カッキーは2025年末〜2026年初に参加型（指を動かす／指を置く）から「リズムに合わせて○○」系の非接触リズム演出（単語を言う、荷物検査、ランニング）へ軸を移しており、参加型は2026年春以降ゲームコラボ案件（鳴潮・NIKKE・アークナイツ・リバース1999・NTE等、概要欄に「中国のお仕事のご相談」）を中心に続いている。

### Gaps
- **登録者の時系列推移は未取得**: socialblade.com（403）、yutura.net（403、検索結果にはカッキーのチャートページ https://yutura.net/channel/59907/chart/ が存在）、hypeauditor（403）、playboard（429）、vidIQ（429）、Wayback Machine（Egress policyで遮断）。報告書作成者はこれらを別環境で参照できる可能性あり。
- RSSは直近15本のみのため、週本数は直近1〜6か月の値。長期の投稿頻度は「動画本数÷経過年数」で概算可能（例: カッキー 907本/11.8年≈1.5本/週）。
- 参加型の「初回」は検索ヒット＋直近48本の範囲に限るため、チャンネル内の真の初回より遅い可能性がある（特にPlott系）。

## Q4. 参加型を数本出して止めたチャンネル（失敗・停止例）と、その後の投稿状況

### Takeaway
停止・失敗例は3パターン確認できた: (a) ブームが去って**シリーズ終了したがチャンネルは継続**（タカノメ: 2026/01で参加型もチャンネル投稿も停止、もやりつ: 2026/01で参加型終了・通常回継続、なで肩: 間隔が空き2026/07が最終、yuusuube: 2023/07でチャンネル自体停止）、(b) **数本試して再生数が伸びず通常回に戻った**（HARUHO、ritatictic、ナカチコ、モンキーランド、Mixstgirls、VEE）、(c) **参加型を主軸にしているが再生数が付かない小規模チャンネル**（omi_irotoridori 中央値26回、Bee Domina 中央値1.3万、アマタ 2〜5千、リンクの作業場 1〜2万）。

### Cited Findings
- タカノメ（@タカノメ_illust）: 「指を動かすやつ」25本（2025/10/18〜2026/01/17）。2026/01/14 15万・01/17 17.5万と急落した直後、RSS最終投稿が2026/01/25で、以後8か月以上投稿なし（登録7.15万、91本） — [YouTube](https://www.youtube.com/@%E3%82%BF%E3%82%AB%E3%83%8E%E3%83%A1_illust/shorts)
- もやりつ（@MOYARITSU）: 参加型は2025/10/15〜2026/01/09の14本で終了。以後は通常回（脹相ネタ・ダンスミーム等）を週1本ペースで継続し、2026/05/05に1,457万回（非参加型）を記録。直近は2026/09/25 7.5万、09/28 4.5万 — [YouTube](https://www.youtube.com/@MOYARITSU/shorts)
- なで肩（@nadegataaaa）: THUMB DANCE Part15 2026/07/03（51万）が最終投稿。Part1〜7（2025/08〜11）は725万〜1,481万だったが、Part8以降は378万→214万→154万→88万→102万→79万→51万と単調減少 — [YouTube](https://www.youtube.com/@nadegataaaa/shorts)
- yuusuube（@yuusuube、4万人）: 「○○でピッタリ止めると…⁉」を2022/06〜2023/07に44本投稿（最大204万、2023年は5〜125万）。2023/07/08が最終投稿でチャンネル停止 — [YouTube](https://www.youtube.com/@yuusuube/shorts)
- ナカチコChannel（@nakachiko_ch、9,690人）: 「手を動かして見てね」7本（2022/10〜11、6,762〜6.6万回）。最終投稿2023/04/15 — [YouTube](https://www.youtube.com/@nakachiko_ch/shorts)
- モンキーランド（@monkeyrand-youtube、3.11万人）: 「⭕️に指を置いてね☝️」4本（2.5〜8.5万回、通常回中央値3.3万と同水準）。最終投稿2024/04/02 — [YouTube](https://www.youtube.com/@monkeyrand-youtube/shorts)
- HARUHO（@haruho0、1.22万人）: 2025/09〜10にTHUMB DANCE等6本。1本42万、残り1.3万〜3.7万（通常回中央値1.35万）。以後は通常回に戻り、週0.34本、最終2026/08/11 — [YouTube](https://www.youtube.com/@haruho0/shorts)
- りいたの遊びば（@ritatictic、5.41万人）: 「どっちを選ぶ？」等6本（2026/01〜04、1,510〜2.1万、通常回1.55万）。以後通常回、最終2026/08/30 — [YouTube](https://www.youtube.com/@ritatictic/shorts)
- アオ。（@Ao-0405、1,290人）: 「指を置いてみて！！」2本（2024/08、33万・10万、通常回中央値2,923）がヒットしたが登録者は1,290人に留まり、最終投稿2025/03/16 — [YouTube](https://www.youtube.com/@Ao-0405/shorts)
- トキイチ（@トキイチ-l6b、6,140人）: 「ここに指をおいてみて！！」2021/10/16 15万（通常7,323）。最終投稿2022/08/23 — [YouTube](https://www.youtube.com/@%E3%83%88%E3%82%AD%E3%82%A4%E3%83%81-l6b/shorts)
- おゆびちゃん（@oyubi、242人）: 2021/02開設、11本、最終投稿2021/08/16 — [YouTube](https://www.youtube.com/@oyubi)
- himarian（@himarian-0606、137人）: 2025/09開設、4本中「リズムに合わせて指を動かしてね！」6.1万回、最終投稿2025/10/02 — [YouTube](https://www.youtube.com/@himarian-0606/shorts)
- Anime JAPAN 3D @TKG（@anime.japan.3d_TKG、221人）: 2025/10開設、THUMB DANCE 2本（1.9万・6,752）、最終投稿2025/12/16 — [YouTube](https://www.youtube.com/@anime.japan.3d_TKG/shorts)
- こみレイン（@komileinch、1,960人）: THUMB DANCE 19万・12万（通常1,461）、最終投稿2026/01/15 — [YouTube](https://www.youtube.com/@komileinch/shorts)
- Aiko Makes Art（@AikoMakesArt、8,720人）: 2025/12開設、37本全てClose your eyes系（中央値9万、最大470万）、最終投稿2026/02/19で停止 — [YouTube](https://www.youtube.com/@AikoMakesArt/shorts)
- omi_irotoridori（@omi_irotoridori、242人）: 2025/03開設、137本、週1.42本で2026/09/29まで継続投稿しているが、参加型38本の再生数中央値26回・最大3,526回 — [YouTube](https://www.youtube.com/@omi_irotoridori/shorts)
- Bee Domina（@BeeDomina、1,050人）: 2025/12〜2026/10に参加型24本（中央値1.3万、最大2.3万）、継続中 — [YouTube](https://www.youtube.com/@BeeDomina/shorts)
- Mixstgirls（@Mixstgirls、17.7万）: 「指でつまんでみてね」4本（2026/01〜04、7,191〜1.4万、通常9,241）で通常回と差なし — [YouTube](https://www.youtube.com/@Mixstgirls/shorts)
- VEE official（@VEE_official、1.58万）: THUMB DANCE 3本（4,262〜2.6万、通常3,506）、最終投稿2026/07/14 — [YouTube](https://www.youtube.com/@VEE_official/shorts)
- 【公式】めぐる株式会社（@meguru-youtube、474人）: 「【ショートゲーム】リズムに合わせて指を動かすと...」9本（2025/08〜2026/02、中央値1万・最大10万）、最終投稿2026/04/17 — [YouTube](https://www.youtube.com/@meguru-youtube/shorts)

### Inferences
- 二次創作×THUMB DANCEのシリーズ（なで肩・タカノメ・もやりつ）は、いずれも開始から3〜5か月で再生数が1/10以下に落ち、4〜5か月目でシリーズ終了している。ブーム型フォーマットの寿命は概ね1四半期と推定される。
- 「指を置いて」型をオリジナルキャラで小規模チャンネルが行った場合（omi、ほけまる、みかん、せいのすけ等）の到達は数十〜数千回で、フォーマット自体に拡散力はない。一方、同型でも人気IP（hololive 276万、やしゅし 255万、テイコウペンギン 99万）や既存ファンがいれば伸びる。
- 参加型でヒットしても登録者に転換しない例（アオ。33万回→1,290人、こみレイン19万→1,960人、いずもゆう26万→5,060人）が多く、単発ヒットは登録者獲得に直結しにくい。

### Gaps
- 停止の理由（制作負荷、収益、権利）は本人の発信を確認できておらず、数値からの推測。
- 「失敗」例はタイトルに型キーワードを含むものに限られ、キーワードなしで試して消した動画（削除済み）は検出不能。oEmbedで作者が取れなかった動画（例: 鳴潮「指を置いて遊ぶアニメ!千咲編」7,035回、ゼンゼロ手描き等）は削除・非公開化の可能性がある。
