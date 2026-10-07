# YouTubeショート配信の実証データと俗説の検証 (as of 2026-10-07)

注記: 日付は取得日 2026-10-06〜07(UTC)。「根拠の格付け」は 公式 / 実データ / 二次情報 / 根拠なし の4段階。実データでも相関であり因果ではない。自前集計の元データは同ディレクトリの `empirical_data/` に保存(後述)。

## Q1. 俗説・通説ごとの根拠の評価

### Takeaway
公式に確認できるのは「ハッシュタグ#shortsは不要」「投稿数への直接ペナルティは無い(ただし低品質を量産するより良い1本)」「Shortsの再生数は開始・リプレイでカウント(2025-03-31〜)」「表示は視聴者の反応(視聴時間・リプレイ・いいね等)重視」程度。時間帯・長さ・VVSA 70%・固定コメント・ループ・フックは、実データがあっても標本が偏る、または二次情報・根拠なしのものが大半。

### Cited Findings

#### 1. 投稿時間帯 — 格付け: 実データ(大規模・ただし指標が再生数ではなくエンゲージメント中央値)、効果は小さいと発信元自身が述べる
- Buffer(2026-07-24公開、約180万本のShorts+長尺、時間帯別のエンゲージメント中央値)は、Shortsは金曜が最良で16時・18時・19時が上位3枠、長尺は日曜10時と報告。2025年分析から変化し、Shortsと長尺でピーク時間が大きく異なる — [Buffer](https://buffer.com/resources/best-time-to-post-on-youtube/)
- 同記事は「万能薬ではない」とし、Shortsは「数日〜数週間にわたり推薦エンジンに再浮上し続けるため、初回公開時刻はmake-or-breakではない」と説明(Buffer側の解釈で、YouTube公式の説明ではない) — [Buffer](https://buffer.com/resources/best-time-to-post-on-youtube/)
- YouTube側(Todd Sherman, 2023-08)のインタビュー記事に具体的な投稿時間帯のガイダンスは無い — [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)
- 自前集計: sorotani(約2.3本/週、毎回ほぼ同時刻の10:00 UTC投稿)では時間帯のばらつきが無く検証不能。

#### 2. ハッシュタグ #shorts は必要か — 格付け: 公式(不要寄り)+二次情報
- Todd Sherman: ハッシュタグは必須ではないが、イベント・トレンド・ニッチ話題には文脈的に有用 — [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)
- Shorts判定は縦型(9:16)・3分以内で自動、という二次情報あり(検索要約。YouTube一次ページは未確認) — [Schedulala等の検索結果](https://schedulala.com/blog/youtube-shorts-hashtags-best-practices-guide)
- Metricool(79.9万本・7.1万アカウント、2025→2026比較): ハッシュタグ付き投稿は再生数が約10%少なく、エンゲージメントは約9%高い(相関) — [Metricool](https://metricool.com/youtube-trends/)
- 日本の調査対象: sorotani・fuziko・kyomuo(=ほぼ【アニメ】#shortsを付与)と、付けない/別タグのchは混在するが、チャンネル規模が違い比較不能(後述の自前データ参照)。

#### 3. 投稿頻度が高いほど良いか — 格付け: 公式(ペナルティ無し)+実データ(相関、結果が割れる)
- Todd Sherman: 投稿を増やすことへのアルゴリズム上のペナルティは無い。ただし「低品質な動画を大量に出すより、より良い動画を少なく」と助言。削除→再アップは「スパム扱いのリスク」として非推奨 — [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)
- Metricool(79.9万本・7.1万アカウント): 2〜4本/週の出発点が最良。1本あたり再生: 2-4本/週 5,872、0.5-1本/週 5,812、4-7本/週および7本以上/週は約5,000〜5,100(逓減)。一方で別セクションでは月間合計再生は投稿量とともに増え「実質的な上限は無い」とも述べる(1本あたりと総量で結論が異なる) — [Metricool 要約](https://metricool.com/youtube-trends/) / [検索要約](https://metricool.com/youtube-shorts-algorithm/)
- Metricool: 週0.5〜1本の層と2〜4本の層の差は約1%で、頻度の効果は小さい(上の数値からの単純計算)。
- 因果の向きが不明(伸びているチャンネルが投稿を増やす等)。

#### 4. 同じ型の繰り返しと減衰 — 格付け: 根拠なし〜二次情報(公式の「型の減衰」説明は見つからず)
- 「各Shortは独立に評価され、1本のヒットが次を保証しない」という説明は二次情報のみ(ブログ。YouTube一次ソース無し) — [Neal Schaffer](https://nealschaffer.com/youtube-shorts-not-getting-views/)
- 学術: 70,000チャンネル・990万Shorts(2021-01〜2022-12)の比較研究はあるが、同型反復の減衰は扱っていない — [arXiv 2403.00454](https://arxiv.org/abs/2403.00454)
- 自前集計(日本のアニメ系ch): 型を固定している ch で、新しい半分が古い半分より中央値が低いのは fuziko(155k vs 320k)、hajimemashite(275k vs 410k)、takatume(865k vs 1.18M)、一方 sorotani は新しい方が高い(2.05M vs 1.59M)。減衰一貫せず。詳細はQ3。

#### 5. 冒頭1〜3秒のフック — 格付け: 二次情報(専門家の経験則)。公式の秒数規定は未確認
- YouTube公式ブログのShorts深掘り記事はJenny Hoyos(クリエイター)の引用でフックに触れるのみで、Todd Shermanの直接の引用は含まない — [YouTube Blog](https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/)
- Todd Sherman: 評価の中心は「watch time・re-watch・いいね・シェア・コメント」等のエンゲージメント要素 — [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)
- Socialinsider/vidIQ等は「最初の数秒が重要」と記述するが、秒数別の再生数データは提示していない(Socialinsiderのガイドを確認、定義の説明のみ) — [Socialinsider](https://www.socialinsider.io/blog/youtube-shorts-analytics-guide/)

#### 6. ループ設計 — 格付け: 公式(カウント仕様の変更)+二次情報(効果の主張)
- YouTube公式ヘルプ: 2025-03-31から、Shortsの再生数は「再生開始またはリプレイの回数」で、最低視聴時間の要件なし。「Engaged views」が別指標 — [YouTubeヘルプ](https://support.google.com/youtube/answer/10059070)
- 「ループで再生が増える/アルゴリズムの強い推薦シグナル」はブログ/AI記事の主張で一次データ無し — [vidIQ ブログ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/)(本文は未取得、検索要約のみ)
- 示唆: 2025-03-31以降は公開再生数がループ・短尺に有利に出る仕様。それ以前のデータ(Galloway 2023等)と直接比較できない。

#### 7. コメント誘導・固定コメント — 格付け: 根拠薄(二次情報、Shortsに限定した検証なし)
- 「良い固定コメントで返信が最大30%増(200チャンネル、100万〜1,000万再生帯)」という主張はあるが、方法が不明な二次情報で、Shortsの再生数への効果ではなくコメント返信数 — [Air.io](https://air.io/en/youtube-hacks/what-to-write-in-your-youtube-pinned-comment-to-get-a-reaction-from-your-audience)
- Shorts vs 通常動画: Shortsはコメント率が低い(いいね率は高い) — [arXiv 2403.00454](https://arxiv.org/abs/2403.00454)
- Galloway研究: いいね・シェア・コメントと成績に強い関係は見られなかった — [Thread Reader (Galloway)](https://threadreaderapp.com/thread/1646898356419981315.html)
- Todd Sherman自身はコメントをエンゲージメント要素の一つとして挙げるのみで、固定コメントには言及なし — [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)

#### 8. 「Viewed vs Swiped away」70%以上 — 格付け: 実データ(小標本・非公開データ由来)。YouTube公式の閾値は見つからず
- Galloway(33チャンネル・5,400 Shorts・33億再生): VVSAが60%未満は「ほとんど成績が良くない」、最良は概ね70〜90%。ただし高VVSAは成功を保証しない — [Thread Reader (Galloway)](https://threadreaderapp.com/thread/1646898356419981315.html)
- 「70%超が目安」は上記が出所と見られる。クリエイターのThreads投稿等でも拡散(個人の報告、n=1) — [Threads @_daobeezy](https://www.threads.com/@_daobeezy/post/DOaAfxuDVm3/for-creators-trying-to-get-more-views-on-youtube-shorts-make-sure-to-pay-attenti)
- 2025-03-31の再生定義変更後に同じ閾値が成り立つかのデータは見つからず(Gapsへ)。

#### 9. 動画の長さと再生数 — 格付け: 実データ(ただし割れる)。下の自前結果は逆の傾向
- Galloway(33ch・5,400本): 平均視聴時間が50〜60秒で平均410万再生、40〜50秒で180万、30〜40秒で130万、20〜30秒では20万。動画長50〜60秒は平均170万再生、40〜50秒は80万。「保持できるなら長い方が良い」。ただし最も多く作られているのは20〜40秒 — [Creator Buzz](https://www.thecreatorbuzz.com/p/youtube-shorts-study-worth-checking) / [Thread Reader](https://threadreaderapp.com/thread/1646898356419981315.html)
- 注意: 「50〜60秒で170万再生」は Socialinsider 調査と書く二次記事があるが、一次の出所は Galloway 研究(33ch)。検索要約の「Socialinsider=50-60秒」の帰属は誤りの可能性が高い — [検索要約(要注意)](https://www.socialinsider.io/blog/youtube-shorts-analytics-guide/)(同ガイド本文に該当の記述は見つからなかった)
- vidIQ: 13秒または60秒前後が良い、30〜45秒が最適等の記述は、データ提示の乏しい二次・検索要約(「vidIQ Data Study 2026」)であり未検証 — [検索要約](https://vidiq.com/blog/post/get-more-views-youtube-shorts/)
- Metricool: 1本あたり平均視聴時間は約16秒(前年比約-67%)、Shortsはプラットフォーム全体のオーガニック視聴の61% — [Metricool](https://metricool.com/youtube-trends/)

#### 10. 新規チャンネルの初動の仕組み — 格付け: 公式(概念)+二次情報(詳細)
- Todd Sherman(Creator Insider等): 新規動画はまず少数の視聴者に提示され、反応(視聴継続など)を見て広げる、という説明の二次要約が複数あるが、一次動画の書き起こしは未取得。 — [Creator Handbook(二次)](https://www.creatorhandbook.net/youtube-explains-how-the-youtube-shorts-algorithm-works/)
- Metricool: 登録者1万未満の小規模アカウントでShorts再生が200%超伸びた(2025→2026) — [Metricool](https://metricool.com/youtube-trends/)
- 自前: kenozakaanime(登録者約4,100、Shorts全7本=全履歴)の初期は1,701〜13,000回で、ここからの外挿は不可(n=7)。

#### 11. 過去の動画がバズると次も伸びるか — 格付け: 二次情報のみ。自前データでは一定ではない
- 「各Shortは独立、次の保証はない」「Shortsはフィードで見つけられ、チャンネルへの忠誠より発見向け」という二次記事 — [Neal Schaffer](https://nealschaffer.com/youtube-shorts-not-getting-views/) / [Miraflow](https://miraflow.ai/blog/why-youtube-shorts-get-views-but-no-subscribers)
- 登録者換算: Galloway研究は10,000再生あたりの登録増は長尺22.7人・Shorts16.9人、ただし登録者100万超のchでは逆転 — [検索要約(Galloway)](https://nowbam.com/decoding-the-youtube-shorts-algorithm/)
- 自前: ヒット集中度が高い(sorotani 上位10%の動画が合計再生の37%)一方で、ヒット後の次回作の再生が必ず上がる/下がる傾向は確認できず(Q3)。

#### 12. チャンネルテーマの一貫性 — 格付け: 根拠なし(公式は「視聴者起点」の一般論のみ)
- Todd Sherman:「アルゴリズムではなく視聴者を考えよ」 — [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)
- テーマ一貫性が再生数を上げるという定量研究は今回の検索では見つからず。Shortsは entertainment カテゴリに集中、教育・政治は相対的に低い、という学術結果はある(カテゴリ差であって一貫性ではない) — [arXiv 2403.00454](https://arxiv.org/abs/2403.00454)

### Inferences
- 「70%以上」「50〜60秒」は同一の起点(2023年のGalloway研究、33ch・5,400本)に遡る数字が多い。これが2025-03-31の再生定義変更後も成り立つかは未検証。
- 時間帯・ハッシュタグ・頻度はいずれも効果が小さい(数%〜10%程度の差)ため、結果に影響が大きいのは内容と視聴継続という仮説の方が、データに整合的。
- Shortsの再生定義(再生開始/リプレイ)が変わったため、2025年前後のデータをまたぐ比較は注意が必要。

### Gaps
- 秒数単位のフック効果(最初の1〜3秒の離脱)の公開された大規模データ: 見つからず。
- YouTube公式が示す「Viewed vs Swiped away」の目安: 見つからず(70%は非公式)。
- 固定コメントがShorts再生数に与える効果: 見つからず。
- 「同型反復で減衰する」「テーマ一貫性が効く」の定量根拠: 見つからず。
- Creator Insiderの動画本体は書き起こしを取得できず(YouTube Blogの記事も引用なし)。Todd Shermanの発言はSocial Media Today(2023-08)の転載経由。
- Medium版Galloway記事は403で取得不可、X/Thread Readerの転載経由で確認。

## Q2. 大規模分析(vidIQ・Socialinsider・Buffer・Tubular Labs等)の事例

### Takeaway
Shorts単独で「尺・視聴維持率・エンゲージメントと再生数」を結んだ公開大規模分析は少なく、最も具体的なのは2023年Galloway(33ch・5,400本)。Buffer・Metricool・Tubularは時間帯、頻度、市場規模の集計が中心で、Tubular・vidIQ・Socialinsiderの数値は今回、本文確認ができていない(検索要約止まり)ものが多い。

### Cited Findings
- **Galloway & Gileta(2023-04)**: 33チャンネル、5,400 Shorts、33億再生。尺・VVSA・視聴時間・RPM・登録者転換を分析。主な数値はQ1の#8,#9参照。RPMは約0.06ドル/1,000再生で10〜60秒で差が無い。尺とは別に、いいね・シェア・コメントと成績に強い関係は無い — [Creator Buzz](https://www.thecreatorbuzz.com/p/youtube-shorts-study-worth-checking) / [Thread Reader](https://threadreaderapp.com/thread/1646898356419981315.html) / [検索要約](https://nowbam.com/decoding-the-youtube-shorts-algorithm/)
- **Buffer(2026-07-24)**: 約180万本の時間帯別エンゲージメント中央値。Shorts=金曜16/18/19時、長尺=日曜10時 — [Buffer](https://buffer.com/resources/best-time-to-post-on-youtube/)
- **Metricool(2026)**: 799,718本・71,177アカウント。頻度・ハッシュタグ・平均視聴時間(約16秒、約-67%)など — [Metricool](https://metricool.com/youtube-trends/)
- **学術 Violot et al. (2024)**: 70,000チャンネル、990万Shorts+690万通常動画(2021-01〜2022-12)。Shortsは通常動画より再生数・いいね率が高く、コメント率は低い。教育・政治カテゴリでShortsは相対的に弱い。Google所属研究者が共著 — [arXiv 2403.00454](https://arxiv.org/abs/2403.00454)
- **Tubular Labs**: 2025年の世界のYouTube再生の77%は1分未満の動画(2024年は70%)、1分未満の再生数は2023年24.5兆→2025年41.5兆、一方で視聴時間の57%超は20分以上の動画(2025年5月末まで)。検索要約からの転記で、一次ページ(Adweek/TVREV)の本文は未取得 — [TVREV](https://www.tvrev.com/news/tube-trends-over-75-of-youtube-views-came-from-shorts-in-2025-tubular) / [Adweek](https://www.adweek.com/adweek-wire/tubular-shorts-longform-both-drive-significant-youtube-audience-gains-in-june/)
- **Socialinsider**: ガイド記事(2026)は用語定義(Viewsは数秒視聴、Engaged viewsは30秒または最後まで)のみ確認。「Shortsの平均投稿頻度は月7本、コメント率0.05%」は検索要約のみで本文未確認 — [Socialinsider ガイド](https://www.socialinsider.io/blog/youtube-shorts-analytics-guide/)
- **vidIQ**: 自社ブログに「平均視聴率73.6%(vidIQチャンネルのShorts、直近12か月)」「30〜45秒が最適」等の記述が検索要約に出るが、方法・標本が不明で本文未確認(vidIQ本体は429で取得不可) — [vidIQ](https://vidiq.com/blog/post/youtube-shorts-algorithm/)

### Inferences
- 年・標本つきで検証できたのは Galloway(2023, 33ch/5,400本)、Buffer(2026, 約180万本)、Metricool(2026, 約80万本)、Violot ほか(2024, 990万Shorts)の4件。尺と再生数の関係を直接扱う大規模分析は Galloway のみで、標本が小さく、チャンネル選定バイアスもありうる。
- 「Shortsが再生の大半」(Tubular)と「視聴時間は長尺が優位」は両立する市場統計で、個別動画の伸び条件の証拠ではない。

### Gaps
- Tubular Labs・vidIQ・Socialinsiderの一次レポート本文(標本数・集計方法)は未確認。
- 日本市場に限った大規模Shorts分析は見つからず。

## Q3. 日本のアニメ・キャラ系ショートチャンネルの自前集計

### Takeaway
小標本の探索的集計(8ch、うちYouTube側の制限で尺・公開日つき詳細が取れたのは1ch)。結果: (c)尺と再生数は sorotani(n=38)で負の相関(ρ=-0.58)、(b)新しい半分の方が低いch(fuziko・hajimemashite・takatume)と高いch(sorotani)が混在し減衰は一貫せず、(d)頻度と再生は ch間 n=7で結論不能。いずれも相関で因果ではない。

### Cited Findings
**取得方法・日**: 2026-10-06〜07 に Bash の curl で youtube.com から取得。チャンネルの /shorts ページ(ytInitialData の shortsLockupViewModel)で最新から最大48本の再生数(「◯万回視聴」の丸め表示)と順序、チャンネルRSS(`feeds/videos.xml`、最新15件、公開日と正確な再生数、Shorts以外を含む)、動画ページ(ytInitialPlayerResponse の viewCount/lengthSeconds/publishDate)。動画ページ取得は並列度6で試行後、YouTubeがreCAPTCHAを返し(IP単位のレート制限)、回避せず待機・再試行(5分待ち複数回)したが復旧せず、sorotani 38本のみ完全取得。ほかの7chは尺が取れていない。元データは `/home/user/career-consultant-quiz/research_notes/YouTubeアルゴリズム徹底分析/empirical_data/`(listing.json=一覧48本、rss.json、raw_watch.json=動画ページ38本、収集・集計スクリプト)。

**対象チャンネル(登録者数は取得時)**: sorotani そろ谷のアニメっち(127万)、ikuze_1111 いくぜ!(53.5万)、fuziko-fuziko ふじこふじこ(33.3万)、kawisouni 可哀想に!(132万)、hajimemashite はじめまして松尾です(131万)、takatume_ncj タカツメ(5.15万、ゲーム実況の切り抜きアニメで固定キャラだが原作は第三者動画。属性が異なる)、kyomuo 虚無男(3.33万、BL系)、kenozakaanime けの坂アニメ(約4,100、Shorts全7本)。顔出し無し・固定キャラの条件を全chで厳密には確認していない(タイトルとチャンネル名からの判断)。

**チャンネル別(/shorts一覧、最新から並ぶ前提、再生数は丸め)**
| ch | n | 中央値 | 最大 | 最小 | 新しい半分の中央値 | 古い半分の中央値 |
|---|---|---|---|---|---|---|
| sorotani | 48 | 187.5万 | 2,073万 | 14万 | 204.5万 | 158.5万 |
| ikuze_1111 | 48 | 180万 | 1,094万 | 41万 | 172.5万 | 195.5万 |
| fuziko | 48 | 25.5万 | 148万 | 4.9万 | 15.5万 | 32万 |
| kawisouni | 45 | 772万 | 1,746万 | 121万 | 830.5万 | 588万 |
| hajimemashite | 48 | 35.5万 | 93万 | 13万 | 27.5万 | 41万 |
| takatume | 48 | 99万 | 560万 | 37万 | 86.5万 | 117.5万 |
| kyomuo | 19 | 3.4万 | 25万 | 1.5万 | 3.6万 | 3.05万 |
| kenozakaanime | 7 | 約4,400 | 1.3万 | 1,701 | 4,884 | 1,789 |

順序の確認: RSSの公開日と照合して新しい順に並んでいると確認できたのは sorotani・fuziko・hajimemashite・takatume・kenozakaanime(kyomuoは概ね)。ikuze_1111 と kawisouni は RSS との重複が1件・4件で、順序が公開日順かを確認できていない(kawisouniの重複分は2024〜2025年で、最新RSS(2026-09)と離れており、一覧が最新順でない可能性)。この2chの新旧比較は参考値。

**(a) 最初の数本の伸び方**: 新規立ち上げ直後を観測できたのは kenozakaanime(全7本、公開順: 1,701 / 1,824 / 13,000 / 1,754 / 4,378 / 4,884 / 5,394)のみで、最初の3本のうち1本が約1.3万と突出、その後は5,000前後。他のchは直近48本(sorotani 2026-06〜、fuziko 2026-08〜等)のみで、初動は観測不能。RSSの10件(Shorts以外含む)では 5,470 / 1,701 / 1,824 / 6,315 / 13,649 / 1,754 / 73,095(2025-04-12、一覧外の動画) と、ばらつきが大きい。kyomuo は一覧19本が 1.8万〜25万(最古は2026-05-22以前)で最初の5本に特別な傾向は無い。

**(b) 同じ型の繰り返しと減衰**(sorotani 完全データ38本、2026-06-07〜09-27): 公開順とのρ=-0.14(弱い)、先頭5本の中央値499万→直近5本295万。ただし最大2,073万・1,646万・1,639万といった大ヒットが6月に集中し、直近でも 384万・409万が出ている。一覧ベース(48本)の新旧順位相関は fuziko +0.56、hajimemashite +0.49、takatume +0.22(正=古い動画ほど多い=新しい動画が低い)、sorotani +0.25(中央値は新しい半分が高く、結果が割れる)、kyomuo -0.05。注意: 古い動画は累積期間が長く、新しい動画は成長途中のため、この比較は古い方に有利に出る。減衰の証拠とは言えず、一貫性もない。型の同一性は未判定(タイトルのみで、ほぼ全ch同一フォーマットの連作)。

**(c) 尺と再生数**(sorotani 38本のみ、尺7〜175秒、中央値33秒): Spearman ρ=-0.58(短いほど多い)。チャンネル中央値で正規化した中央値は、15秒以下(15本)が1.78倍、16〜30秒(3本)が2.19倍、31〜45秒(6本)が0.88倍、46秒以上(14本)が0.35倍。上位3本は15秒・17秒・11秒。他のchの尺は取得できず。これはGallowayの「長いほど良い」と逆だが、標本は1チャンネルのみ。2025-03-31以降はループ・短尺の再生が数に入りやすい定義変更の影響もありうる(因果は不明)。

**(d) 投稿頻度と1本あたり再生数**: 同一ch内(sorotani)で「前回投稿からの間隔日数」と再生数のρ=+0.02(ほぼ無関係)。ch間はRSS(最新15件、Shorts以外含む)から推定した頻度(本/週)と一覧の中央値: sorotani 約3.0(187.5万)、ikuze 4.7(180万、RSS中央値は1.5万=長尺混在で不整合)、fuziko 1.4(25.5万)、hajimemashite 1.3(35.5万)、kyomuo 0.8(3.4万)、takatume 0.3(99万)、kawisouni 0.1(772万)。頻度が高いchほど再生が低い/高い、のどちらの傾向も無く、チャンネル規模(登録者)の方が再生に効くように見える(n=7、規模・題材が異なる)。

### Inferences
- 同型の連作でも「新しい動画ほど減衰」は fuziko・hajimemashite・takatume で見えるが、sorotani・kawisouni では逆で、チャンネルごとに違う。累積期間の偏りもあるため、減衰の一般法則は言えない。
- 再生数の分布が極端に偏る(sorotani で上位10%が合計の37%)ため、中央値で見るとヒット前後の差は小さく、平均や最大値だけ見ると誤読する。
- sorotani の尺と再生の関係は、短いネタ型(10秒前後のオチ)が当たりやすい可能性を示すが、1チャンネル・38本の相関で一般化はできない。

### Gaps
- 7チャンネルの尺・正確な公開日つきデータ(動画ページがreCAPTCHAで取得不能。回避は行わず)。やり直す場合は時間を置いて直列・低頻度で再取得する(`empirical_data/collect2.py` は途中再開可)。
- 立ち上げ直後(最初の数本)を観測できたのは kenozakaanime のみ(n=7)。
- 「顔出し無し・固定キャラ」の厳密な確認、型(フォーマット)の同一性判定、チャンネルの総Shorts数の確認は未実施。
- 登録者数・インプレッション・VVSAは公開データに無く、再生数と登録者規模の分離ができない。
