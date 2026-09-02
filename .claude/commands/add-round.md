---
description: 新しい回次（第N回）をアプリに追加する
argument-hint: "<回次番号>"
allowed-tools: Bash(python3 scripts/check_quiz_data.py:*), Bash(grep:*), Read, Edit
---

第 `$1` 回を出題対象に追加してください。UI とデータの両方の更新が必要です。

## 手順

1. **データ**: `QUIZ_DATA` に `"$1": { … }` を回次の昇順で追加する。
   設問の形式は `/add-question` と同じ規約に従う。
   設問データがまだ手元にない場合は、先に空の枠だけ作らず、ユーザーに設問の提供を求める。
2. **UI**: 回次選択のボタン（`.round-opt`）とモード選択まわりを更新する。
   - `grep -n 'round-opt\|data-round\|"29"\|selectedRound\|roundsToUse' index.html` で該当箇所を洗い出す。
   - 追加が必須の 2 箇所: 回次選択ボタン（`<button class="opt-btn round-opt" data-round="…">`）と、
     「全部」選択時の回次一覧をハードコードしている `roundsToUse()` の配列。
3. **タイトル**: `<title>` と `<h1>` の「第29〜31回」表記を、追加後の範囲に合わせて更新する。
4. `python3 scripts/check_quiz_data.py` を実行して OK を確認する。
5. `/preview` でブラウザ動作（回次選択 → 出題 → 結果表示）を確認する。

回次を跨ぐ既存の学習履歴（localStorage `careercc_wrong_questions_v1`、キーは `"回次-問番号"`）を
壊さないよう、キーの形式は変更しないこと。
