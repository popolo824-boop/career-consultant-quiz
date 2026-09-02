#!/usr/bin/env bash
# Claude Code のステータスラインとして動作しつつ、
# iPhone ウィジェット用の状態 JSON を iCloud に書き出す。
#
# 設定 (~/.claude/settings.json):
#   {
#     "statusLine": {
#       "type": "command",
#       "command": "~/.claude/claude-status-export.sh",
#       "refreshInterval": 30
#     }
#   }
#
# refreshInterval を入れておくと、セッションがアイドルの間も
# 残り時間の表示が更新される。

set -uo pipefail

# Scriptable の iCloud Documents フォルダ。
# Scriptable をインストールし iCloud 同期を有効にすると作られる。
OUT_DIR="${CLAUDE_WIDGET_DIR:-$HOME/Library/Mobile Documents/iCloud~dk~simonbs~Scriptable/Documents}"
OUT_FILE="$OUT_DIR/claude-status.json"

input=$(cat)

# --- ステータスライン表示（ターミナル用）------------------------------------
line=$(printf '%s' "$input" | jq -r '
  def pct($v): if $v == null then "--" else ($v | round | tostring) + "%" end;
  [
    (.model.display_name // "Claude"),
    (if .context_window.used_percentage != null
     then "ctx " + pct(.context_window.used_percentage) else empty end),
    (if .rate_limits.five_hour.used_percentage != null
     then "5h " + pct(.rate_limits.five_hour.used_percentage) else empty end),
    (if .rate_limits.seven_day.used_percentage != null
     then "7d " + pct(.rate_limits.seven_day.used_percentage) else empty end)
  ] | join(" | ")
' 2>/dev/null)
[ -n "$line" ] && printf '%s\n' "$line"

# --- ウィジェット用 JSON の書き出し -----------------------------------------
# 出力先が無い場合（Scriptable 未導入など）は静かに終了する。
[ -d "$OUT_DIR" ] || exit 0

payload=$(printf '%s' "$input" | jq -c --argjson now "$(date +%s)" '
  {
    updated_at: $now,
    session: {
      name:          (.session_name // null),
      model:         (.model.display_name // null),
      dir:           ((.workspace.current_dir // "") | split("/") | last),
      repo:          (if .workspace.repo then
                        (.workspace.repo.owner + "/" + .workspace.repo.name)
                      else null end),
      duration_ms:   (.cost.total_duration_ms // null),
      cost_usd:      (.cost.total_cost_usd // null),
      lines_added:   (.cost.total_lines_added // null),
      lines_removed: (.cost.total_lines_removed // null)
    },
    context: {
      used_pct: (.context_window.used_percentage // null),
      size:     (.context_window.context_window_size // null)
    },
    limits: {
      five_hour: (if .rate_limits.five_hour then
                    {used_pct: .rate_limits.five_hour.used_percentage,
                     resets_at: .rate_limits.five_hour.resets_at}
                  else null end),
      seven_day: (if .rate_limits.seven_day then
                    {used_pct: .rate_limits.seven_day.used_percentage,
                     resets_at: .rate_limits.seven_day.resets_at}
                  else null end),
      spend:     (if .rate_limits.spend_limit then
                    {used_pct: .rate_limits.spend_limit.used_percentage,
                     resets_at: .rate_limits.spend_limit.resets_at}
                  else null end)
    }
  }
' 2>/dev/null)

# jq が失敗したら前回のファイルを壊さずに終了する。
[ -n "$payload" ] || exit 0

# ウィジェットが書きかけを読まないよう、一時ファイル経由で差し替える。
tmp="$OUT_FILE.tmp.$$"
printf '%s\n' "$payload" > "$tmp" && mv -f "$tmp" "$OUT_FILE" || rm -f "$tmp"
