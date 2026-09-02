---
description: 既存の設問の誤りを修正する
argument-hint: "<回次> <問番号> [修正内容]"
allowed-tools: Bash(python3 scripts/check_quiz_data.py:*), Bash(grep:*), Read, Edit
---

第 `$1` 回 問 `$2` を修正してください。

修正の指示: $ARGUMENTS

## 手順

1. `index.html` の `QUIZ_DATA["$1"]["$2"]` を読み、現状（stem / choices / answer / explanations）を把握する。
2. 修正内容を適用する。修正は指示された範囲に留め、周囲の設問には触れない。
3. `answer` を変更する場合は、`explanations` の ○/× 記号も併せて付け替える:
   - 通常（「最も適切なものはどれか」）→ 正答が **○**、他が **×**
   - 否定形（「不適切」「誤っている」「誤りである」「適切でない」）→ 正答が **×**、他が **○**
4. `python3 scripts/check_quiz_data.py` を実行して OK を確認する。
5. 修正前後の差分を要約してユーザーに報告する。

正答の変更はユーザーが明示的に指示した場合のみ行い、
解説と正答の食い違いを自分の判断で「正しい方」に寄せて解決しないこと。
どちらが正しいか判断が必要な場合は、根拠を示してユーザーに確認する。
