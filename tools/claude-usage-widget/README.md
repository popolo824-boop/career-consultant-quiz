# Claude 利用状況ウィジェット（iPhone ホーム画面）

Claude Code の稼働状況と利用枠の残量を、iPhone のホーム画面に常時表示します。

```
 ● 実行中                    たった今
 5時間枠                          63%
 ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░
 1時間57分後にリセット
 7日枠                            31%
 ▓▓▓▓▓░░░░░░░░░░░░░░
 3日11時間後にリセット
 quiz slash commands
 Opus 5 · ctx 13% · 1時間15分 · +210/-34
```

## しくみ

```
Mac の Claude Code
  └ statusLine が claude-status-export.sh を呼ぶ
      └ claude-status.json を iCloud (Scriptable フォルダ) に書き出す
          └ iCloud 同期
              └ iPhone の Scriptable ウィジェットが読んで描画
```

サーバーもトークンも不要です。データは自分の iCloud の中だけを通ります。

## 必要なもの

- Mac 上で動く Claude Code（`jq` も必要: `brew install jq`）
- Claude Pro または Max のサブスクリプション
- iPhone に [Scriptable](https://apps.apple.com/app/scriptable/id1405459188)（無料）
- Mac と iPhone が同じ Apple ID で iCloud Drive 同期

## セットアップ

### 1. iPhone に Scriptable を入れる

App Store から入れて一度起動します。これで iCloud 上に
`iCloud Drive/Scriptable/` が作られます。

### 2. ウィジェットのスクリプトを登録する

Scriptable で「＋」から新規スクリプトを作り、`ClaudeUsage.js` の中身を
貼り付けて、名前を **ClaudeUsage** にして保存します。

### 3. Mac にエクスポータを置く

```bash
mkdir -p ~/.claude
cp claude-status-export.sh ~/.claude/
chmod +x ~/.claude/claude-status-export.sh
```

`~/.claude/settings.json` に以下を追加します。

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/claude-status-export.sh",
    "refreshInterval": 30
  }
}
```

`refreshInterval` は、セッションがアイドルの間もリセットまでの残り時間を
更新するためのものです。

### 4. 動作確認

Mac で Claude Code を起動し、何か 1 回やり取りします
（`rate_limits` は最初の API 応答の後から入るため）。
ターミナル下部に `Opus 5 | ctx 13% | 5h 63% | 7d 31%` のような行が出れば成功です。

書き出しを直接確認する場合:

```bash
cat ~/Library/Mobile\ Documents/iCloud~dk~simonbs~Scriptable/Documents/claude-status.json
```

### 5. ホーム画面に置く

ホーム画面を長押し →「＋」→ Scriptable → 小 or 中サイズを配置 →
ウィジェットを長押しして「ウィジェットを編集」→ Script に **ClaudeUsage** を指定。

- **小**: 5時間枠 / 7日枠のバーとリセットまでの時間
- **中**: 上記に加えてセッション名、モデル、コンテキスト使用率、経過時間、増減行数

## 把握できること

| 表示 | 元データ |
|---|---|
| 5時間枠の使用率とリセット時刻 | `rate_limits.five_hour` |
| 7日枠の使用率とリセット時刻 | `rate_limits.seven_day` |
| 利用額の上限（ゲートウェイ利用時のみ） | `rate_limits.spend_limit` |
| コンテキスト使用率 | `context_window.used_percentage` |
| セッション名・モデル・経過時間・増減行数 | `session_name`, `model`, `cost.*` |

`resets_at` を過ぎた枠は、ウィジェット側で「リセット済み / 0%」と判定します。

## 制約（把握しておいてください）

- **Mac で Claude Code が動いている間しか更新されません。**
  ステータスラインは Claude Code のプロセスが呼び出すものなので、
  終了中は値が止まります。最終更新から 15 分を過ぎると「待機中」表示になり、
  ヘッダーに経過時間が出ます。
- **Web 版（claude.ai/code）のセッションでは書き出せません。**
  ステータスラインはローカルの Claude Code の機能です。
  利用枠はアカウント単位なので、Mac 側のセッションで表示される値が
  Web 側の消費をどこまで含むかは、実際に使いながら確認してください。
- **`rate_limits` は Pro / Max 契約者のみ**に入ります。
  API キー利用のみの場合、この枠は `—` 表示になります。
- **更新間隔は iOS が決めます。** ウィジェットは 5 分後の再描画を要求しますが、
  実際には 15 分程度空くこともあります。すぐ見たい時はウィジェットをタップすると
  Scriptable が開いて最新の値を描画します。

## Mac を使わない場合

`ClaudeUsage.js` の `REMOTE_URL` に状態 JSON の URL を設定すると、
ローカルファイルではなくその URL から取得します
（例: GitHub の raw URL に `claude-status.json` を置く）。
その場合、利用状況が置き先から読める点に注意してください。
