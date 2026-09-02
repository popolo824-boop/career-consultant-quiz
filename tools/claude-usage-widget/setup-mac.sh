#!/usr/bin/env bash
# Mac 側のセットアップ。エクスポータを ~/.claude/ に配置し、
# ~/.claude/settings.json に statusLine 設定をマージする。
#
#   ./setup-mac.sh          セットアップを実行
#   ./setup-mac.sh --check  現在の状態を確認するだけ（変更しない）

set -euo pipefail

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
SETTINGS="$CLAUDE_DIR/settings.json"
EXPORTER="$CLAUDE_DIR/claude-status-export.sh"
ICLOUD_DIR="${CLAUDE_WIDGET_DIR:-$HOME/Library/Mobile Documents/iCloud~dk~simonbs~Scriptable/Documents}"

CHECK_ONLY=0
[ "${1:-}" = "--check" ] && CHECK_ONLY=1

ok()   { printf '  \033[32m✓\033[0m %s\n' "$1"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$1"; }
bad()  { printf '  \033[31m✗\033[0m %s\n' "$1"; }

echo "Claude 利用状況ウィジェット — Mac セットアップ"
echo

# --- 前提の確認 --------------------------------------------------------------
echo "前提の確認"
fail=0
if command -v jq >/dev/null 2>&1; then
  ok "jq: $(jq --version)"
else
  bad "jq が見つかりません → brew install jq"
  fail=1
fi

if [ -d "$ICLOUD_DIR" ]; then
  ok "Scriptable の iCloud フォルダを検出"
else
  warn "Scriptable の iCloud フォルダがありません"
  echo "      $ICLOUD_DIR"
  echo "      iPhone に Scriptable を入れて一度起動すると作られます。"
  echo "      （フォルダができるまで、書き出しは静かにスキップされます）"
fi

[ "$fail" = 1 ] && { echo; echo "前提が足りないため中断しました。"; exit 1; }

if [ "$CHECK_ONLY" = 1 ]; then
  echo
  echo "現在の設定"
  [ -f "$EXPORTER" ] && ok "エクスポータ: $EXPORTER" || warn "エクスポータ未配置"
  if [ -f "$SETTINGS" ] && jq -e '.statusLine.command' "$SETTINGS" >/dev/null 2>&1; then
    ok "statusLine: $(jq -r '.statusLine.command' "$SETTINGS")"
  else
    warn "statusLine 未設定"
  fi
  if [ -f "$ICLOUD_DIR/claude-status.json" ]; then
    updated=$(jq -r '.updated_at // 0' "$ICLOUD_DIR/claude-status.json")
    ok "最終書き出し: $(date -r "$updated" 2>/dev/null || echo "$updated")"
  else
    warn "まだ書き出されていません（Mac で Claude Code を 1 往復すると出ます）"
  fi
  exit 0
fi

# --- エクスポータの配置 ------------------------------------------------------
echo
echo "エクスポータの配置"
mkdir -p "$CLAUDE_DIR"
install -m 755 "$SRC_DIR/claude-status-export.sh" "$EXPORTER"
ok "$EXPORTER"

# --- settings.json のマージ --------------------------------------------------
echo
echo "settings.json の更新"
# 設定にはチルダ表記で書く（Claude Code 側で展開される）。
SL_CMD="${EXPORTER/#"$HOME"/\~}"
NEW_SL=$(jq -n --arg cmd "$SL_CMD" \
  '{type:"command", command:$cmd, refreshInterval:30}')

if [ ! -f "$SETTINGS" ]; then
  jq -n --argjson sl "$NEW_SL" '{statusLine: $sl}' > "$SETTINGS"
  ok "新規作成しました"
else
  # 壊れた JSON を上書きしない。
  if ! jq -e . "$SETTINGS" >/dev/null 2>&1; then
    bad "$SETTINGS が JSON として読めません。手動で確認してください。"
    exit 1
  fi
  if existing=$(jq -er '.statusLine.command' "$SETTINGS" 2>/dev/null); then
    warn "既存の statusLine を置き換えます: $existing"
  fi
  backup="$SETTINGS.bak.$(date +%Y%m%d%H%M%S)"
  cp "$SETTINGS" "$backup"
  tmp="$SETTINGS.tmp.$$"
  jq --argjson sl "$NEW_SL" '.statusLine = $sl' "$SETTINGS" > "$tmp" && mv -f "$tmp" "$SETTINGS"
  ok "更新しました（バックアップ: $backup）"
fi

# --- 動作確認 ----------------------------------------------------------------
echo
echo "動作確認（サンプル入力で 1 回実行）"
now=$(date +%s)
sample=$(cat <<JSON
{"model":{"display_name":"Opus 5"},
 "session_name":"setup test",
 "workspace":{"current_dir":"$PWD"},
 "cost":{"total_cost_usd":0,"total_duration_ms":1000,"total_lines_added":0,"total_lines_removed":0},
 "context_window":{"used_percentage":5,"context_window_size":1000000},
 "rate_limits":{"five_hour":{"used_percentage":10,"resets_at":$((now+3600))},
                "seven_day":{"used_percentage":5,"resets_at":$((now+86400))}}}
JSON
)
out=$(printf '%s' "$sample" | "$EXPORTER")
if [ -n "$out" ]; then
  ok "ステータスライン出力: $out"
else
  bad "出力がありません。$EXPORTER を直接実行して確認してください。"
fi

if [ -f "$ICLOUD_DIR/claude-status.json" ]; then
  ok "書き出し成功: $ICLOUD_DIR/claude-status.json"
else
  warn "書き出しなし（Scriptable の iCloud フォルダ待ち）"
fi

cat <<'NEXT'

セットアップ完了。

次にやること:
  1. Mac で claude を起動し、何か 1 往復する
     （rate_limits は最初の API 応答の後に入ります）
  2. ターミナル下部に "Opus 5 | ctx .. | 5h .. | 7d .." が出れば成功
  3. iPhone のウィジェットに数分で反映されます

状態を見たいとき:  ./setup-mac.sh --check
NEXT
