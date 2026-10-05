# YouTubeショートでバズる動画の型・尺・フック・制作手法 (2026年時点)

注記: 調査時、searchenginejournal / VOICEVOX公式 / mobinc / miralab 等への WebFetch がネットワーク制限でブロックされ、本文の精読ができなかった。以下は検索結果スニペットに基づく。公式一次情報(YouTubeヘルプ、VOICEVOX・CoeFont公式規約)は未確認のため、利用前に原典確認が必要。

## 最初の1〜3秒のフックのパターンと事例

### Takeaway
最初の約3秒でスワイプを止めさせることが最重要とされ、好奇心ギャップ(オープンループ)、パターン割り込み、具体的な数字、警告などの型が定番。ただし多くは海外のマーケ系ブログ由来で、YouTube公式の数値ではない。

### Cited Findings
- 最初の3秒がショートで最重要で、視聴者は高速でスワイプするため冒頭で惹けないと次へ移られる — [国内解説(検索結果要約)](https://pamxy.co.jp/marke-driven/sns-marketing/youtube/youtube-shorts/amp/)
- 高成績のフック7型: 意外な矛盾、具体的な数字の約束、個人的な告白、思わず答えたくなる質問、ビフォーアフター、逆説的ハウツー、重大な警告 — [Opus Pro](https://www.opus.pro/blog/the-science-of-hooks)
- 他の型: 好奇心ギャップ(ループを開いたまま閉じない)、パターン割り込み(大胆な主張)、感情トリガー(体験談) — [Opus Pro](https://www.opus.pro/blog/youtube-shorts-hook-formulas)
- 「3秒保持」が配信拡大の閾値だという主張(YouTube公式の裏付けは未確認、ベンダー主張) — [Opus Pro](https://www.opus.pro/blog/youtube-shorts-hook-formulas)
- テスト法: 1文フックを3案作り各5秒の導入を撮って、10秒時点まで維持できる案を選ぶ — [Opus Pro](https://www.opus.pro/blog/youtube-shorts-hook-formulas)

### Inferences
- 日本語キャリア系では「年収・転職・知らないと損」系の数字提示+警告型が相性が良いと考えられる(未検証の推論)。

### Gaps
- 日本語ショートの具体的なバズ事例(チャンネル名・再生数)は取得できず。
- 保存・シェア・コメントを促す型(あるある、診断、2択、知らないと損)を裏付ける日本語の定量データは見つからず。
- テロップ、ループ設計、CTAの有効性を示す一次データは未取得。

## 最適な動画尺と視聴維持率の目安

### Takeaway
2024年10月15日から最大3分に拡張されたが、Adobe Expressの調査では30秒以下が推奨(クリエイターの平均46%)。3分尺はアルゴリズム対応が後追いとされた。

### Cited Findings
- 2024年10月15日からショートは最大3分(正方形・縦長)。1〜3分もショート広告で収益化され、YPP要件にカウントされる。長尺ショートの推薦改善は「今後数か月で」と告知 — [ppc.land](https://ppc.land/youtube-expands-shorts-duration-to-3-minutes/) / [Gigazine](https://gigazine.net/gsc_news/en/20241004-youtube-short-video-length-3-minutes)
- Adobe Expressの調査: 閲覧・シェア・CTR・保存の4指標で理想は30秒以下、平均46%のクリエイターが推奨 — [Adobe](https://www.adobe.com/express/learn/blog/youtube-shorts-length-study)
- ショートの平均視聴完了率は通常動画の約1.5倍という調査がある(出典の原典未確認) — [mobinc](https://mobinc.jp/column/2026/03/27/understanding-and-creating-youtube-shorts-guide/)

### Inferences
- 初期は15〜30秒で視聴完了率を稼ぎ、反応が良い題材のみ45〜60秒に伸ばす運用が妥当(推論)。

### Gaps
- 「何%以上が合格か」という視聴維持率の具体的な目安(例: 平均視聴率100%超でループ)は信頼できる出典が見つからず。
- 3分化後の実際の拡散への影響を示すデータなし。

## アルゴリズムが重視する指標と2025〜2026年の変更点

### Takeaway
「視聴者が選んだ割合(viewed vs swiped away)」が事実上のクリック率指標。2025年3月31日にショートの再生数定義が変わり、再生開始で即カウント、従来基準は「エンゲージビュー」に改称された。

### Cited Findings
- 「視聴 vs スワイプ」はショートのCTR相当の指標。60%以下は伸び悩み、70〜90%が好成績とする報告(YouTube側の説明を引用した二次情報、数値の一次確認未了) — [Search Engine Journal(検索結果要約)](https://searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953)
- 読むべき指標: 視聴 vs スワイプ、エンゲージビュー、平均視聴時間、平均視聴率の組み合わせ — [True Future Media](https://www.truefuturemedia.com/articles/youtube-shorts-algorithm-data-backed-guide)
- 2025年3月31日から、再生開始・リプレイで最低視聴時間なしに再生数カウント。従来の質ベース指標は「エンゲージビュー」として残る — [RouteNote](https://routenote.com/blog/how-are-views-counted-shorts-tiktok-reels/)
- エンゲージビューが収益化・YPP判断の主要指標として継続 — [Samproof](https://samproof.tv/2025/03/28/youtube-is-changing-how-shorts-views-are-counted-heres-what-creators-need-to-know/)
- 2025年7月15日、YPPの「inauthentic content(量産・反復コンテンツ)」の定義を明確化。AI音声・TTS自体は禁止ではないが、テンプレ的で変化の乏しい量産は対象。ショートにも適用。YouTubeのRene Ritchieは「新規則ではなく明確化」と説明 — [Typecast](https://typecast.ai/learn/youtube-ai-monetization-july-15-ypp-update/) / [Gulf News](https://gulfnews.com/technology/youtube-updates-monetisation-policies-ai-and-repetitive-content-ban-begins-july-15-1.500192660)

### Inferences
- 再生数の定義変更により、再生数よりエンゲージビューと「視聴者が選んだ割合」で評価すべき。
- AIナレーション+定型テンプレ量産は収益化リスクがあるため、各動画に独自の台本・映像・見解を入れる必要がある。

### Gaps
- 2026年内の追加アルゴリズム変更(公式発表)は確認できず。
- 保存・シェア・コメントが推薦に与える重みの公式な数値は見つからず。

## 日本語AIナレーション・字幕ツールの比較と商用利用

### Takeaway
VOICEVOXは無料で商用可だがクレジット表記が必須(キャラごと規約あり)。ElevenLabsは有料プラン(Starter $5/月〜)で商用ライセンス、無料プランは不可。CoeFontは有料プランで商用利用(月額2,178円〜との二次情報)。

### Cited Findings
- VOICEVOX: 無料、商用利用可、クレジット必須。キャラクター別規約があり、R18等の制限あり。YouTubeでは概要欄にクレジットを書くのが一般的 — [Crystal Method](https://crystal-method.com/blog/voicevox-commercial/) / [Miralab](https://miralab.co.jp/media/ai_voice_generation_apps/)(いずれも二次情報)
- CoeFont: 無料は月200回生成、商用は有料プラン(2,178円/月〜と記載)。二次情報で、現行料金は未確認 — [Crystal Method](https://crystal-method.com/blog/voicevox-commercial/)
- ElevenLabs: 無料プランは商用不可。無料または未ログインで公開する場合はタイトルに "elevenlabs.io" 等の帰属表記が必要。有料プランは商用ライセンス付き(ベータ機能除く)、Starter $5/月で30,000クレジット — [ElevenLabs公式ヘルプ](https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform) / [BigVu](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/)

### Inferences
- 低コスト開始ならVOICEVOX(キャラ規約とクレジット管理が必要)、自然さ重視ならElevenLabs有料、が現実的な選択肢。

### Gaps
- CoeFontの公式規約・現行料金、声ごとの商用条件は未確認(公式ページ未取得)。
- VOICEVOX公式規約の原文は取得不可(ブロック)。
- 字幕(自動テロップ)ツール(CapCut、Vrew等)の比較と規約は未調査。

## 初期の投稿頻度とテスト運用の推奨

### Takeaway
国内の解説では週2〜5本程度が目安で、継続可能性を優先する推奨が多い。根拠は運用会社の経験則で、YouTube公式の推奨ではない。

### Cited Findings
- ベスト投稿時間は平日17〜20時・土日10〜12時、頻度は週2〜4回との記載 — [pamxy](https://pamxy.co.jp/marke-driven/sns-marketing/youtube/youtube-shorts/amp/)
- 週3〜5本の投稿が推奨され、毎日投稿がベストだが無理のない継続が重要 — [mobinc](https://mobinc.jp/column/2026/03/27/understanding-and-creating-youtube-shorts-guide/)

### Inferences
- 最初の1〜2か月は週3〜5本で、フック・尺・題材を1変数ずつ変えるA/Bテストを行い、「視聴者が選んだ割合」と平均視聴率で勝ち型を選ぶ運用が妥当(推論)。

### Gaps
- タイトル・ハッシュタグの効果(#shortsの要否、個数)を示す一次情報は未取得。
- 投稿時間帯の根拠データは不明(各社経験則)。
