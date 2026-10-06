# YouTubeの推薦システムに関する公開論文と実務への含意

読了範囲: Covington 2016、Chen 2019(Top-K)、Wang 2023(Fresh)、Wang 2025(Item-centric)は本文PDFを取得して読んだ。Zhao 2019(MMoE)は本文PDFを取得できず(ACM等はHTMLを返した)、Google Research公式ページの要旨のみ。Xu 2021(Values of Exploration)と Xu 2022(Surrogate)は検索結果の要旨のみ。以下の「Inferences」は全て推測であり、論文が述べたことではない。

## Covington et al. 2016: 2段階構成、ウォッチタイム、example age、新しさ

### Takeaway
候補生成(数百本に絞る)とランキング(特徴量を増やして精密にスコア付け)の2段階構成。ランキングの目的は「クリック率ではなく期待ウォッチタイム」で、新しさは example age 特徴量と学習データの作り方で扱う。2016年当時の論文で、現行の仕組みそのものではない。

### Cited Findings
- 著者 Paul Covington, Jay Adams, Emre Sargin。2016年、RecSys '16(第10回ACM Conference on Recommender Systems)。要旨は「標準的な2段階情報検索の構成に従い、deep candidate generation modelと別のdeep ranking modelを提示する」 — [Google Research](https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/)
- 本文PDF(読了): https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf
- システムは候補生成用と ranking用の2つのニューラルネットワークで構成される。候補生成はユーザーの活動履歴を入力に、巨大なコーパスから数百本の動画を取り出す。推論時は近似最近傍探索を使う — Covington et al. 2016 本文 Sec.2-3
- 設計上の課題として論文は Scale、Freshness、Noise を挙げる。Freshnessは「新規アップロード動画と最新のユーザー行動の両方に反応する必要がある。新しいコンテンツと確立した動画のバランスは探索/活用の観点で理解できる」と述べる。Noiseは「ユーザー満足の正解はほとんど得られず、ノイズの多い暗黙フィードバックをモデル化している」 — 同 Sec.1
- ランキングの最終目的関数は「A/Bテストの結果に基づいて常時調整されるが、概ね impression あたりの期待ウォッチタイムの単純な関数」。CTRでランキングすると、最後まで見られない欺瞞的な動画(clickbait)が上がりやすく、ウォッチタイムの方がエンゲージメントをよく捉える、と記述 — 同 Sec.4
- 期待ウォッチタイムは weighted logistic regression で予測。クリックされたimpressionを視聴時間で重み付けし、未クリックは重み1。推論時は e^x を最終活性化にして期待視聴時間に近い値を出す。ウォッチタイム加重の評価指標でCTR直接予測よりかなり良かった — 同 Sec.4.2, 5
- example age 特徴量: 「ユーザーは新しいコンテンツを好むことを一貫して観察しているが、関連性を犠牲にしてまでではない」。新規動画の推薦には一次効果に加え、バイラルコンテンツをブートストラップ/伝播させる二次効果がある。MLは過去の訓練データから学ぶため過去への暗黙のバイアスを持つ。訓練例の経過時間を特徴量として入れ、サービング時は0(または僅かに負)にして「訓練窓の終わり」で予測させる。図4では、この特徴量により動画のアップロード時刻と時間依存の人気を正確に表現できた — 同 Sec.3.3
- 訓練例は自分たちの推薦経由の視聴だけでなく、他サイトへの埋め込み視聴を含む全YouTube視聴から作る。理由は「そうしないと新しいコンテンツが浮上しづらく、推薦が活用に偏りすぎる」。他経路での発見を協調フィルタリングで素早く他ユーザーに伝播させたい、とある。ユーザーあたりの訓練例数を固定して、ヘビーユーザーが損失を支配しないようにした — 同 Sec.3.4
- 「サロゲート問題の選択がA/Bテスト性能に過大な影響を持つが、オフライン実験では測りにくい」 — 同 Sec.3.4

### Inferences
- 推測: 「クリック率だけでなく視聴時間(視聴完了に近い指標)を取りにいく設計」だった、という2016年時点の設計思想は確実に言える。だが現行の目的関数が今も「期待ウォッチタイムの単純な関数」かどうかは、この論文だけでは言えない(次の質問の通り、後続論文は複数目的と満足度を扱う)。
- 推測: 新しい動画への一定の配慮(example age)が仕組みとして存在した、は言える。ただし「新しいから優遇される」は論文は主張していない。「ユーザーは新しさを好むが関連性は犠牲にしない」であり、新しさは関連性と引き換えにはならない。

### Gaps
- 論文は2016年のホーム画面/関連動画向けで、Shorts(2020年開始)は含まない。現在も同じ構成かどうかをYouTube自身が述べた一次情報は今回見つけられなかった。

## Zhao et al. 2019: 多目的ランキング(MMoE)と選択バイアス

### Takeaway
「次に何を見るか」のランキングを、エンゲージメント(クリック・視聴時間)と満足(いいね・評価等)など複数目的の同時最適化として扱い、MMoE で目的間のパラメータを共有。位置などによる選択バイアスは Wide&Deep の「浅いタワー」で緩和する。ただし本文は未読で、以下は要旨と二次要約のみ。

### Cited Findings
- 著者(Google Research掲載): Zhe Zhao, Lichan Hong, Li Wei, Jilin Chen, Aniruddh Nath, Shawn Andrews, Aditee Kumthekar, Mahesh Sathiamoorthy, Xinyang Yi, Ed Chi。2019年、RecSys '19。要旨: 「複数の競合するランキング目的と、ユーザーフィードバックの暗黙の選択バイアスという実世界の課題がある。複数目的を効率よく最適化するために MMoE などのソフトパラメータ共有技術を探索し、Wide & Deep の枠組みで選択バイアスを緩和した」 — [Google Research](https://research.google/pubs/recommending-what-video-to-watch-next-a-multitask-ranking-system/)
- 選択バイアスの緩和は、位置など単純な特徴量を使う線形の「浅いタワー」が担う、という説明(二次的な要約。本文は未確認) — [検索要約](https://research.google/pubs/pub49380/)
- 論文の対象は「次に見る動画」の推薦(関連動画の文脈)で、ホーム画面全体や Shorts ではない(要旨の表現による)。

### Inferences
- 推測: 目的が複数あり、満足系の指標が含まれるため、「視聴時間だけを伸ばせば良い」という単純な理解は2019年時点でも不十分。個別の目的の重みや組み合わせ方は要旨からは分からない。
- 推測: 位置バイアスの補正があることは、「上位に出た動画がクリックされやすいのはランキング位置のせい」も分解して学習していることを示唆する。クリエイターにとっての行動指針にはならない。

### Gaps
- MMoEの具体的な目的リスト、目的の重み付け、実験数値は本文未読のため記載しない。

## Chen et al. 2019 ほか: 探索、コールドスタート、多様性、満足度(2018〜2025)

### Takeaway
Googleは新しい動画を「探索」と「新規コンテンツ専用スタック」の両面から扱っている。2023年と2025年の論文は、新規コンテンツに最低限の露出を与えつつ、予測の不確実性と満足度を使って「誰に見せるか」を選ぶ設計を述べている。ただし多くはプラットフォーム名を明示しない。

### Cited Findings
- Chen, Beutel, Covington, Jain, Belletti, Chi(Google)「Top-K Off-Policy Correction for a REINFORCE Recommender System」。arXiv 2018年12月、WSDM 2019。数百万アイテムの行動空間でREINFORCEを適用し、ログデータの偏りをオフポリシー補正で緩和する。YouTubeでのライブ実験を含む — [arXiv](https://arxiv.org/abs/1812.02353)
- 対象は候補生成モデル(本番のRNN候補生成)で、候補は別のランキングモデルでスコア付けされホームページに出る — Chen 2019 本文 Sec.6
- 探索: ε-greedy のような力任せの探索は本番では不適切な推薦を招くため採用せず、Boltzmann探索を使う。上位K'件は確定、残りのK-K'件は上位M件から確率的にサンプリングする — 同 Sec.5
- ライブ実験: 確率的ポリシー自体では ViewTime に有意な変化なし(T=1)。探索データを学習に入れると ViewTime +0.07%(ユーザーの5%のみ確率的ポリシー)。ただし本文は「大きな改善ではない」と認めている — 同 Sec.6.2.1
- Wang et al. 2023「Fresh Content Needs More Attention: Multi-funnel Fresh Content Recommendation」(Wang, Lu ほか、Ed Chi, Cristos Goodrow, Minmin Chen ら、Google)。KDD 2023、arXiv 2306.01720。専用の新規コンテンツ推薦スタックを構築。ツータワーモデル(カバレッジ)と、ユーザーフィードバックでほぼリアルタイム更新するシーケンスモデル(関連性)を組み合わせる複数経路の候補選定。ランキングでは「予測の不確実性」を考慮して露出の少ないコンテンツをブートストラップ — [arXiv](https://arxiv.org/pdf/2306.01720)
- 同論文は「500時間以上/分のコンテンツがYouTubeにアップロードされる」ことを動機に挙げるが、評価対象は「大規模な商用プラットフォーム」と記述しYouTubeとは明記しない(著者はYouTube関係者を含む) — 同上
- 同論文の結果: 専用スタックでコーパスカバレッジとdiscoverable corpus(投入後に一定数の正の反応を得たコンテンツ数)が増加。アップロード数が増加(クリエイターが投稿を増やす)。fresh content の7日間の正の反応数が平均+2.52%。ユーザー側とコーパス側を同時に分割するco-diverted実験を使う。新規コンテンツ専用スタックの経由の反応は「ブートストラップ後」の指標には含めない — 同 Sec.4-5
- 同論文は、ユーザーの活動度と新規コンテンツへの親和性に関係があり、それが文脈依存の複数経路設計の動機になった、と述べる(Sec.3) — 同上
- Wang, Jiao, Bhadury, Zhang, Gao, Dalal「Item-centric Exploration for Cold Start Problem」(著者はGoogle/YouTube所属との報道。本文は短尺動画の推薦に注力)。arXiv 2507.09423、RecSys 2025 Industry Track。「このユーザーに最良のアイテムは何か」ではなく「この新規アイテムに最適なユーザーは誰か」を考える。Beta分布のベイズモデルで、アイテム固有の満足率を推定し、あるユーザーの予測満足度がアイテムの満足率の事後平均より大幅に低ければ、そのアイテムをそのユーザーの候補から外す — [arXiv](https://arxiv.org/abs/2507.09423)、本文PDF https://arxiv.org/pdf/2507.09423
- 同論文のライブ実験: 探索アイテムのimpressionは20%減少、一方ユーザー満足度は維持/向上、探索の対象となる recommendable corpus は10%拡大(本文表1と記述)。満足度(satisfied impression)の定義は本文の確率モデルを参照(アンケート由来かどうかは本文で確認できていない) — 同上
- Xu et al.「Values of Exploration in Recommender Systems」RecSys 2021。探索は短期的にもユーザー体験を損なうとは限らないと論じ、正確性・多様性・新規性・セレンディピティの4軸で評価 — [Google Research](https://research.google/pubs/values-of-exploration-in-recommender-systems/)(要旨のみ)
- Xu et al.「Surrogate for Long-Term User Experience in Recommender Systems」KDD 2022。長期の再訪頻度を予測する短期行動をRLの報酬サロゲートに使う — [Google Research](https://research.google/pubs/surrogate-for-long-term-user-experience-in-recommender-systems/)(要旨のみ)
- YouTube自身の説明: 推薦はユーザーの視聴行動、高評価・低評価、登録、フィードバック(満足度アンケートを含む)を使う — [How YouTube Works](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)(取得した要約による)
- 参考(YouTubeとは無関係): arXiv 2507.19346 はEコマース事業者の短尺動画推薦の論文で、YouTubeには言及しない — [arXiv](https://arxiv.org/abs/2507.19346)。arXiv 2507.04534 と 2507.21467 はYouTube Shortsを外部から分析した研究で、YouTube/Google自身の論文ではない(今回は本文未確認)。

### Inferences
- 推測: 新規動画は「全体から通常のランキング競争」だけでなく、専用の探索・新規コンテンツ経路で、少数のユーザーに試験的に提示され、その反応(満足度、視聴)でさらに配信が広がる/絞られる、という設計が少なくとも研究レベルにある。ただしYouTubeの現行本番で同じ形かは不明。
- 推測: Item-centricの考え方では、早期の反応が良い層に絞って配信するため、「誰に最初に見せられたか」が結果に影響する可能性がある。ただし論文はクリエイターが制御できる要素に言及していない。
- 推測: 初期の反応が悪いと配信が広がらない、という形で作用しうる(Beta事後分布は少数impressionでは不確実性が大きく、観測が増えるほど収束する)。しきい値や期間の具体値は論文に無い。
- 推測(クリエイター向け含意として言えること): 視聴時間の質、視聴後の満足が最適化対象に含まれる、という方向性までは論文が支持する。サムネイル/タイトル/長さ/投稿頻度/時刻の個別の「コツ」を論文は支持しない。

### Gaps
- Shorts専用の公式な推薦論文(Google/YouTube著、Shortsと明記)は見つからなかった。2025年の item-centric 論文は短尺動画が中心という記述にとどまり、Shortsと明記されているかは未確認。
- 満足度アンケートを直接扱ったGoogle/YouTube論文の本文確認は未了(Xu 2022 等は要旨のみ)。多様性・公平性(Beutel 2019 等)、content provider aware(Mladenov 2020)は未調査。

## 論文が現在のアルゴリズムと一致しない可能性(YouTube自身の言及)

### Takeaway
論文は特定時点のスナップショットであり、YouTube自身も現行の詳細は公開していない。論文の記述内でも、目的関数は「A/Bテストで常時調整される」と述べている。

### Cited Findings
- Covington 2016 は、最終ランキング目的が「A/Bテスト結果に基づいて常時調整されている」と明記する — Covington 2016 本文 Sec.4
- Chen 2019 は、各実験は「各コンポーネントを個別に分析したもの」で、比較対象は直前の旧システムだと断る — Chen 2019 Sec.6
- YouTube公式の説明ページは、新規アップロード動画の扱いや、システムの進化の詳細には言及していない(取得要約による) — [How YouTube Works](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)
- YouTubeが「論文は古い」と明言した一次情報は、今回の調査では見つからなかった。

### Inferences
- 推測: 2016、2019年の論文は、深層学習ベースの構成の出発点として読むべきで、現行の重みや仕様の根拠にはできない。2023、2025年の論文は新しいが、プラットフォーム名を伏せたもの/部分的な改善の報告に留まる。
- 推測: 論文に書かれていない要素(チャンネル単位の評価、投稿頻度、SEO的な要素)は、「論文からは言えない」。

### Gaps
- YouTube公式の「論文は現行と異なる」旨の声明、Shortsの推薦アーキテクチャの公式記述は未確認。
