# YouTubeショート(Shorts)フィードのアルゴリズムの仕組みと2025〜2026年の変更点

確度ラベル: [公式]=YouTubeヘルプ/公式幹部発言の直接確認, [公式(二次経由)]=公式発言を報じた記事で確認(原文未取得), [二次]=第三者記事, [推測]=調査者の推論。取得日: 2026-10-06。調査は検索数回に限定した簡易調査で、Creator Insider動画の原文・Studioヘルプの「Viewed vs swiped away」原文は未取得。

## 1. 「視聴 vs スワイプ(Viewed vs Swiped away)」指標

### Takeaway
2023年8月にShorts製品責任者Todd ShermanがCreator Insiderで説明し、Analyticsに「視聴された割合 vs スワイプされた割合」が追加された。「何%以上が良い」という公式の目安数値は確認できず、「Viewedの方がSwipedより高いのが理想」という解説は二次情報(俗説寄り)。

### Cited Findings
- 2023年8月、Shorts製品リードのTodd Shermanは「viewは視聴の意図をエンコードし、クリエイターが意味のある閾値と感じられるものにしたい」と述べた。AnalyticsにShortが「視聴」vs「スワイプで離脱」された割合を示す新指標が追加された [公式(二次経由), 2023-08-28] — [SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/) / [TechCrunch 2023-08-25](https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/)(後者は検索結果での確認のみ、本文未取得)
- Shermanの説明(検索スニペット経由): フィードではまず動画が再生され(再生開始)、視聴者が見続ける(retention)かスワイプで離れるかが、Analytics上の「viewed vs swiped away」 [公式(二次経由)] — [SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)
- 「Viewedの割合がSwiped awayより高いのが理想」「最初の約2秒でスワイプを防ぐのが鍵」という解説 [二次/俗説] — [vidIQ](https://vidiq.com/blog/post/youtube-shorts-algorithm/), [1of10](https://1of10.com/blog/youtube-shorts-analytics/)。公式の閾値(例: 70%など)は今回の調査で見つからず。
- 「swipe-away rateはShorts版CTR」という例え [二次] — 上記二次記事群(検索結果要約のみ)

### Inferences
- 2025-03-31以降は再生開始で「再生数」に加算されるため、Viewed vs Swipedは「再生数が増えても質が見えにくい」問題を補う指標として重要度が上がったと推測できる(二次記事の論旨と同じ)[推測]。

### Gaps
- Studio上の正確な表示位置・文言(概要タブ/エンゲージメントタブのどこか)の公式ヘルプ原文は未取得(support.google.comの該当記事をcurlで取得できず)。
- 公式の目安数値は未確認。ネット上の「70%以上が良い」等は出典未確認のため記載せず。

## 2. 2025-03-31のShorts再生数カウント変更とエンゲージビュー、YPPとの関係

### Takeaway
2025-03-31から、Shortsの「再生数」は再生開始・リプレイ開始ごとにカウント(最低視聴時間なし)。従来の指標は「エンゲージビュー(Engaged views)」に改名されAnalyticsに残り、YPP資格とShorts広告収益分配は引き続きエンゲージビュー基準で、資格・収益は変わらない。

### Cited Findings
- 「2025/3/31から、Shorts再生数は、Shortが再生またはリプレイを開始した回数をカウントし、最低視聴時間の要件なし。複数プラットフォームで投稿するクリエイターにとってより完全な状況把握ができる」 [公式] — [YouTubeヘルプ answer/10059070 (curl取得)](https://support.google.com/youtube/answer/10059070?hl=en)
- 既存の指標を「Engaged views」と改名し、YouTube Analyticsに残す。視聴者が見続けた数を示し、Shorts間の比較に使える [公式] — 同上
- YPP資格とShorts広告収益分配は「Engaged Shorts views」基準で、資格・収益に直接の影響はない [公式] — 同上
- Shorts経由のYPP条件: 登録者1,000人+直近90日で1,000万の有効な公開Shorts視聴 [公式] — 同上
- 発表は2025-03-26(TeamYouTubeのコミュニティ投稿)、3/31実施 [公式(二次経由)] — [PPC Land](https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/)
- 旧来は「数秒以上再生」で再生数カウントだったが、秒数の閾値は非公開 [二次] — 検索結果(MobileSyrup等)要約
- 通常のYPP(長尺中心)条件は登録者1,000人+公開動画の総再生4,000時間、または有効Shorts視聴1,000万/90日 [一般に知られた公式条件。今回は10059070のShorts側のみ直接確認]。また下位の早期アクセス枠(登録者500人など)は今回未確認。

### Inferences
- 再生数が増えて見えても収益指標は変わらないので、「再生数が急増した=アルゴリズムが好意的」とは読めない。分析にはEngaged viewsとViewed vs Swipedを使うべき [推測]。

### Gaps
- 2025〜2026年のYPP条件の追加変更(日本向け含む)は今回未確認。

## 3. 視聴維持率、ループ、3分化、平均視聴率100%超

### Takeaway
平均視聴率(Average percentage viewed)はエンゲージビューとその視聴時間から計算され、リプレイ・ループで100%を超え得る。Shortsの最大尺は2024-10-15に3分へ。ループが推薦で強い正シグナルという主張は二次情報で、公式の確認はない。

### Cited Findings
- 平均視聴率/平均視聴時間は「エンゲージビューとそれに対応する視聴時間から計算」 [公式] — [YouTubeヘルプ answer/9314415 (curl取得)](https://support.google.com/youtube/answer/9314415?hl=en)
- 平均視聴率は、全体または一部のリプレイにより100%を超え得る、エンゲージビューに対する計算なので繰り返し視聴で動画尺を超える [二次(検索要約; 公式ヘルプ記述に近い)] — [1of10](https://1of10.com/blog/youtube-shorts-analytics/) / [Creator Essentials](https://www.creatoressentials.com/glossary/shorts-views/)
- 2024-10-15からShortsは正方形以下の縦長/正方形で最大3分 [二次/一般報道] — [Organisator](https://www.organisator.ch/en/?p=30477) ほか(公式ブログURLはcurlで取得できず未確認)
- ループが推薦の最強シグナルの一つという主張 [二次/推測] — [vidIQ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/) 等。公式確認なし。
- 「満足度アンケートなど視聴後行動が視聴完了率より重視される」「スワイプ離脱率が最初のフィルタ」 [二次; 運営は公式確認していないと記事自体が注記] — [TunePocket](https://www.tunepocket.com/youtube-shorts-algorithm-update-focus-on-freshness-and-search/), [AIR Media-Tech](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views)

### Inferences
- 3分Shortsでは、短い尺のShortより完走ハードルが高く、100%超えは短尺(〜15秒)ループ向きの現象になる [推測]。

### Gaps
- 3分化の公式ブログ・Creator Insider原文、およびループ回数の扱い(再生数にいくつ数えるか、レコメンドへの寄与)は未確認。

## 4. 新規動画の初期テスト配信、波状拡散、寿命

### Takeaway
Todd Shermanは、新しいShortは少数の「シード(種)」視聴者に出して反応を見て拡大する旨を説明(公式発言を二次経由で確認)。「バッチ」「波」という公式表現、および配信が終わる時間・日数の公式数値は確認できず。

### Cited Findings
- 新しいShortは最初に少数の対象視聴者に出され、反応が良ければ広い視聴者に拡大 [公式(二次経由)] — [SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/) と検索結果要約(onlinemarketing.de)
- Shermanは初期の数百〜数千程度の再生は「視聴者を探す実験的配信」で、その後落ちることがあると説明 [公式(二次経由)] — [SEJ 2023-08-28](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)
- 「The audience is the algorithm」という方針発言 [公式(二次経由)] — 同上
- 2025年9月ごろから、Shortsは公開後28〜30日を過ぎるとインプレッションが急減する(「flattening」)という主張 [二次; 公式確認なし] — [TunePocket](https://www.tunepocket.com/youtube-shorts-algorithm-update-focus-on-freshness-and-search/), [AIR](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views)

### Inferences
- 初期テスト→拡大という構造は公式発言と整合するが、再配信の周期(再浮上)の根拠は公式にはなく、制作者の観察から語られている [推測]。

### Gaps
- 何時間・何日で配信が終わるか: 公式の数値なし。二次の28〜30日説はベンダー記事のみで独立検証なし。
- 「バッチ配信」という公式言及は発見できず。

## 5. ショートからの登録者転換、長尺への流入、フィードの性質

### Takeaway
ShortsからYouTubeの登録は多いが、Shorts視聴者が同チャンネルの長尺を見る割合は低いという報告が二次情報で多い。公式のコメントは今回確認できていない。「ショートが非登録者向け中心」の公式確認も未取得。

### Cited Findings
- Shorts視聴者と長尺視聴者の重なりが約10%と低い場合がある、新規Shorts登録者の15〜25%が長尺も見る、という主張 [二次/出典不明確] — [Subscribr](https://subscribr.ai/p/youtube-shorts-hurting-long-form-views), [AIR Media-Tech 18,000チャンネル分析](https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels)
- Rene Ritchie(YouTube Creator Liaison)の「ShortsはLong-formを損なわない」発言は、複数サイトで文言が異なり原文URLなし [確度低] — 同Subscribr記事
- 2022年にYouTubeはShortsが長尺への入り口になると説明(月間ログインユーザー15億) [公式(二次経由)] — [TechCrunch 2022-06-15](https://techcrunch.com/2022/06/15/youtube-shorts-tops-1-5b-logged-in-users-monthly-users-touted-as-feeder-to-long-form-content)
- 2025年後半にShortsと長尺の推薦が完全に分離したという主張 [二次; 公式確認なし] — [TunePocket](https://www.tunepocket.com/youtube-shorts-algorithm-update-focus-on-freshness-and-search/)

### Inferences
- Shortsフィードは「次々と新しい動画を提示する」構造上、登録者より非登録者への露出が大部分になる可能性が高い。ただし登録者比率の公式データは未確認 [推測]。

### Gaps
- 公式の「Shortsフィードは非登録者中心」説明、Shortsからの登録者転換率の公式数値は未取得。
- vidIQ「Why some Shorts don't attract long-form viewers」記事はcurl取得で本文が取れず中身未確認。

## 6. Shortsフィードの関連シグナル(いいね・コメント・共有・保存・リミックス・サウンド)

### Takeaway
今回、公式にシグナル一覧を確認できたものはない。二次情報は、スワイプ離脱率・視聴継続・ループ・いいね/コメント/共有・満足度アンケートを挙げるが、重みは推測。

### Cited Findings
- 視聴継続とスワイプ離脱が基本指標 [公式(二次経由)] — [SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)
- 満足度アンケートなど視聴後行動のほうが完走率より重い、という主張 [二次/推測] — [AIR](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views)
- リミックス関連: 2025年9月「Extend with AI」、2026年3月「Reimagine」、2026年5月にモデルがGemini Omniに、リミックスにデジタル透かしとソースリンク追加、との記載 [二次(AIR; 公式Update名を挙げるが原文未確認)] — [AIR](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views)

### Gaps
- 保存・サウンド(音源)の推薦への寄与は公式にも二次にも確かな根拠を確認できず。

## 7. 2025〜2026年のShorts関連の機能・アルゴリズム変更

### Takeaway
機能面の変更は多いが、今回の主な情報源は一つの二次記事(AIR Media-Tech)で、一部は疑わしい(下記)ため、公式ブログでの個別確認が必要。

### Cited Findings(全て [二次] — [AIR Media-Tech 2026](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views))
- 2025年4月: 音楽への自動同期、写真背景、写真ステッカー
- 2025年5月: Shorts内でGoogle Lensテスト
- 2025年9月: Extend with AI(リミックス)、自動翻訳(音声・タイトル・字幕)を12月に展開予告
- 2025年12月: Shorts on TV、自動翻訳が稼働
- 2026年3月: Reimagine。2026年5月: Gemini Omniに置換、透かし追加
- 2026年7月: Shortsプレーヤー再設計(クリア画面、2倍速、タップでミュート、YPPメンバーにカスタムサムネイル)。「ハートアイコンが高評価に代わり、低評価ボタン廃止」という記載は要注意で、他で確認できず信頼しないこと [未検証]
- 2026年9月: Shortsシリーズ機能、Geminiの会話型編集、1日2,000億回再生到達
- アルゴリズム: 約30日以降の露出減、Shorts推薦のロングフォーム分離、検索結果でShorts枠が拡大 [二次; 運営未確認と記事自体が注記] — [TunePocket](https://www.tunepocket.com/youtube-shorts-algorithm-update-focus-on-freshness-and-search/)
- 2025-03-31の再生数定義変更 [公式] — 上記#2

### Inferences
- 機能面(AIリミックス・翻訳)の追加は、Shortsの拡散に「リミックス/翻訳による再利用」を組み込む方向。推薦への影響は未確認 [推測]。

### Gaps
- 日本向け固有の変更(例: 日本のYPP/ショート収益化、日本語自動翻訳)は未調査/未確認。
- 2026年の各機能の公式ブログ原文は未取得。AIRの日付・内容は一次確認が必要。
- Rene Ritchie/Creator Insiderの2025〜2026年のShorts関連発言の原文は未取得。
