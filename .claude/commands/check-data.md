---
description: index.html の QUIZ_DATA の整合性を検査する
argument-hint: "[検査するHTMLファイル（省略時 index.html）]"
allowed-tools: Bash(python3 scripts/check_quiz_data.py:*), Read, Edit
---

## 検査結果

!`python3 scripts/check_quiz_data.py $ARGUMENTS`

## あなたのタスク

上の検査結果を確認してください。

- **OK の場合**: 回次ごとの問題数を 1 行で報告して終了する。修正は行わない。
- **NG の場合**: 検出された各項目について `index.html` の該当箇所を読み、原因を特定した上で修正する。
  - 修正後は必ず `python3 scripts/check_quiz_data.py` を再実行し、OK になったことを確認する。
  - 正答（`answer`）そのものが疑わしい場合は、勝手に変更せず、根拠とともにユーザーに確認する。

### QUIZ_DATA の規約（修正時に厳守）

- `QUIZ_DATA[回次][問番号]` = `{ stem, choices, answer, explanations }`
- `answer` は 1 始まりの選択肢番号
- `choices` と `explanations` は同じ件数・同じ順序
- 解説の先頭記号は設問タイプで決まる:
  - 通常（「最も適切なものはどれか」）→ 正答が **○**、他が **×**
  - 否定形（「不適切」「誤っている」「誤りである」「適切でない」）→ 正答が **×**、他が **○**
