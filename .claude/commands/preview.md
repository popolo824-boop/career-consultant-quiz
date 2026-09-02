---
description: ローカルサーバーを起動してアプリをプレビューする
argument-hint: "[ポート番号（省略時 8000）]"
allowed-tools: Bash(python3 -m http.server:*), Bash(curl:*), Bash(lsof:*)
---

`index.html` をローカルで配信し、動作を確認してください。

1. ポート番号は `$1`（未指定なら `8000`）を使う。
2. `python3 -m http.server <ポート>` をバックグラウンドで起動する。
3. `curl -sI --noproxy '*' http://127.0.0.1:<ポート>/index.html` で 200 が返ることを確認する。
   （`--noproxy` を付けないと環境のプロキシ設定に吸われて応答が返らない）
4. ユーザーに `http://localhost:<ポート>/` を案内する。

このアプリは単一の `index.html`（ビルド不要・依存なし）です。
学習履歴は localStorage キー `careercc_wrong_questions_v1` に保存されるため、
挙動を確認する際はブラウザの保存データの有無に注意してください。
