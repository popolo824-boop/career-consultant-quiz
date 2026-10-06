# YouTube公式が説明している推薦アルゴリズムの仕組み(2026年10月時点)

注記: 確度ラベルは [公式]=YouTube自身のページ/発言をWebFetchで直接取得、[二次]=報道・ブログによる公式発言の要約、[推測]=出典なし。WebFetchは小型モデルによる要約を返すため、引用符内の文言は原文そのままとは限らない(要原文確認)。

## 1. 推薦の目的と使うシグナル

### Takeaway
YouTubeは推薦の目的を「視聴者が見たい、価値を感じる動画と出会わせること」と説明し、視聴履歴・検索履歴・登録・高評価/低評価・「興味なし」・満足度アンケート等をシグナルとする。Todd Beaupré(2026年9月)は、単一指標では価値を判断できず、人・端末・時間帯で重みが変わると述べた。

### Cited Findings
- 目的は「人々が見たい動画、価値を与える動画を見つける手助けをして、ユーザーのニーズを満たすこと」[公式] — [How YouTube Works: Recommendations](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)
- シグナル: 視聴履歴、検索履歴、チャンネル登録、高評価/低評価、「興味なし」、「チャンネルをおすすめに表示しない」、満足度アンケート。「80 billion超のシグナル」を処理し、似た視聴習慣の人と比較して提案する(要約経由、数値は原文確認推奨)[公式] — [YouTube Help 16089387](https://support.google.com/youtube/answer/16089387)
- 推薦面: ホーム(個人化+登録+最新ニュースの混合)、次の動画(Up Next、再生中の動画に基づく)、ショートフィード、トピック/チャンネルのシェルフ [公式] — 上記2ページ
- チャンネルの評判・品質も考慮し、外部評価者が「平均的な視聴者がどう受け取るか」を判断する補助をする [公式] — [How YouTube Works: Recommendations](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)
- 公式ヘルプは成果を3区分で説明: Appeal(選ばれたか/無視or「興味なし」か)、Engagement(見始めて留まるか)、Satisfaction(楽しんだか)。タイトル・サムネは価値を伝え期待値を設定するもの、冒頭数秒で視聴者は残るか決める [公式] — [YouTube Help 16559650](https://support.google.com/youtube/answer/16559650?hl=en)
- Beaupré(Creator Insider、2026年9月1日公開と報じられる): 推薦は大半が視聴者ごとの「pull」で、プッシュは通知のみ。ランキングは視聴者・端末・時間帯で異なり、「No metric on its own is a good indicator of value」。「全ての時間が価値あるとは仮定したくない」 [二次、元動画は公式] — [PPC Land](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/)(元動画: youtube.com/watch?v=rHLjxrbXmmY とされるが未検証)
- 2025年版のBeaupré×Ritchie対談では、朝はニュース、夜はコメディなど文脈(時間帯)が考慮されると要約されている [二次、仏語ブログ] — [Les Gens d'Internet](https://gensdinternet.fr/2025/02/03/tout-sur-lalgorithme-de-youtube-en-2025)
- 「推薦は同じ動画を8回超は薦めない」というテストへの言及(文脈不明)[二次] — PPC Land(上記)

### Inferences
- 端末・場所への言及はHow YouTube Worksの取得要約には出ず、時間帯・端末はBeaupré発言(二次)が根拠。場所が公式シグナルかは未確認。

### Gaps
- howyoutubeworks のRecommendationsページ原文全体、Shorts固有のシグナル説明の一次ソースは取得できず。
- Creator Insider動画の字幕は未取得(curl未実施)。上記引用は二次要約経由。

## 2. チャンネル単位の評価・新規チャンネル・過去動画の影響

### Takeaway
公式は「主に動画単位」と説明し、「ペナルティボックス」は否定。一方で「チャンネルの評判・品質」への言及もあり、完全に無関係とはされていない。

### Cited Findings
- Beaupré(2024年3月報道): 「For the most part, the algorithm for Discovery is focused more on individual videos」「If your last video wasn't so great and your next video is great, we want to realize the potential of each video」。休止や再生減による罰はなく、将来を予測しない過去データを過度に重視しない [二次] — [Search Engine Journal 2024-03-04](https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/)
- 公式FAQ: 休止の長さと再生数変化に相関はないが、視聴者の「ウォームアップ」が必要な場合がある [公式要約] — [YouTube Help 141805](https://support.google.com/youtube/answer/141805?hl=en)
- 公開直後は登録者以外にも多様な視聴者に見せて反応を見る。反応は視聴者層ごとに別評価で、全体平均ではない(2026年9月) [二次] — [PPC Land](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/)
- 登録者の購読フィードでのCTRは「多くて約10%以下」、「90%の場合、登録者は視聴を選ばない」とBeaupré [二次] — PPC Land
- Cristos Goodrow(VP Engineering、2021年9月): 小規模・新規チャンネルは視聴者適合のデータが少なく推薦されにくい。登録者がほとんど見ないなら、その登録者には推薦されない [二次、2021] — [Search Engine Journal](https://www.searchenginejournal.com/how-youtube-recommends-videos/)
- 公式: 「チャンネルの評判と品質」を考慮 [公式] — How YouTube Works(上記)

### Inferences
- 「動画単位」と「チャンネル評判」の併存は、品質ポリシー(有害・低品質)と日常のランキングで層が違う可能性。公式は両者の関係を詳述していない(推測)。

### Gaps
- 新規チャンネルが不利かを明言する2023〜2026年の公式一次ソースは未発見(2021のGoodrow発言は二次経由)。

## 3. CTRと視聴維持率、「ウォッチタイムだけではない」

### Takeaway
公式は、選ばれる(CTR的な魅力)→留まる(維持)→満足の3段階で説明し、ウォッチタイム単独や単一指標を否定。重みは視聴者・動画で変わる。

### Cited Findings
- Appeal/Engagement/Satisfactionの3区分(上記)[公式] — [YouTube Help 16559650](https://support.google.com/youtube/answer/16559650?hl=en)
- 公式FAQ: 発見システムは絶対・相対ウォッチタイムをシグナルにする。「相対ウォッチタイムは短尺で、絶対ウォッチタイムは長尺でより重要」。オーディエンス維持を見て調整する [公式要約] — [YouTube Help 141805](https://support.google.com/youtube/answer/141805?hl=en)
- Goodrow(2021): 満足度が責任に次いで重要。視聴割合が高いほど満足しやすいが、どちらが重要かは視聴者・動画で変わる。アンケート、高評価/低評価/興味なし、視聴割合がシグナル [二次、2021] — [Search Engine Journal](https://www.searchenginejournal.com/how-youtube-recommends-videos/)
- 「CTR3%未満でサムネ表示停止」「4〜10%が健全」といった数値は、公式出典なし。Beaupréは単一指標を否定しており、この数値は公式主張として扱うべきでない [推測/二次、不採用推奨] — 出典は検索結果の要約のみ
- サムネ・タイトルの変更で順位が変わりうるのは、視聴者の反応が変わるから [公式要約] — YouTube Help 141805

### Inferences
- 公式は具体的な重み・閾値を公開していない。

### Gaps
- CTRの公式な「良い値」の基準は公式に存在しない(未発見)。

## 4. 公式が否定する俗説

### Takeaway
投稿時間、頻度、タグ、休止ペナルティ、24〜48時間待ち、はいずれも公式が影響を否定または小さいと説明。

### Cited Findings
- タグ: 主に綴り間違いの補正用で、発見には重要でない [公式要約] — [YouTube Help 141805](https://support.google.com/youtube/answer/141805?hl=en)
- 投稿時間: 長期成績に影響しない。初動は視聴者がアクティブな時間が有利な場合あり [公式要約] — 同上
- 頻度: 投稿頻度と視聴成長に相関なし、量より質 [公式要約] — 同上
- 休止: 罰則なし [公式要約/二次] — 同上、SEJ 2024
- アルゴリズムは「動画を押し出す」のではなく視聴者ごとに引く。「アルゴリズムに合わせるより視聴者を喜ばせよ」(Ritchie)[二次] — [Tubefilter 2024-08-26](https://www.tubefilter.com/2024/08/26/rene-ritchie-shorts-creator-faqs/)
- 24〜48時間待ってから公開に利点なし [二次] — 検索結果の要約(原文未取得、Digitrendz報道)
- 「長尺を優遇している」という見方へ:「人はテレビで見て長い動画を求めている」(Beaupré)[二次] — PPC Land
- ハッシュタグの効果: 取得できず(Gap)

### Gaps
- ハッシュタグ、動画ファイル名、カテゴリの公式見解は、Tubefilterが話題として触れるのみで内容は取得できず。

## 5. YouTube Studioで公式に見られる指標、ショートフィード

### Takeaway
公式ヘルプは視聴維持率とウォッチタイムの確認を推奨する。Shortsの「Stayed to watch」は存在するが、ランキングへの影響の説明は二次ソースのみ。

### Cited Findings
- 公式ヘルプはAnalyticsの視聴者維持率で調整することを推奨 [公式要約] — [YouTube Help 141805](https://support.google.com/youtube/answer/141805?hl=en)
- Beaupré×Ritchie(2025)はStudioの登録者タブで主要視聴者を分析、Google Trendsで季節傾向を見る、90日ごとの分析を推奨と要約 [二次] — [Les Gens d'Internet](https://gensdinternet.fr/2025/02/03/tout-sur-lalgorithme-de-youtube-en-2025)
- Shorts: 「Stayed to watch」「Viewed vs swiped away」は指標として存在し、小規模シード視聴者で試して配信拡大を決めるとの説明は第三者サイト [二次/推測混在] — [Creator Essentials glossary](https://www.creatoressentials.com/glossary/stayed-to-watch/)(公式かは未確認)

### Gaps
- Studio指標(インプレッション、CTR、平均視聴時間等)の公式定義ページは今回取得できず。Shortsフィードの公式ランキング説明も未取得。YouTube Help の「Analytics」各指標ページを別途確認すること。
