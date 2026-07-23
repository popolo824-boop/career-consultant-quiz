#!/usr/bin/env bash
# claude-auto-resume.sh — 5時間制限で止まっても自動で作業を再開するウォッチドッグ
#
# Claude Code をヘッドレスモード(-p)で実行し、使用制限で停止した場合は
# リセット時刻(またはフォールバック間隔)まで待機してから `claude --continue` で
# 同じセッションの続きを自動再開する。タスクが完了するまで繰り返す。
#
# 使い方:
#   scripts/claude-auto-resume.sh "最初の指示(例: index.htmlに問題を50問追加して)"
#   scripts/claude-auto-resume.sh            # 引数なし → /resume でチェックポイントから再開
#
# 長時間の無人実行は tmux / nohup 推奨:
#   nohup scripts/claude-auto-resume.sh "タスク内容" > auto-resume.log 2>&1 &
#
# 環境変数:
#   MAX_ROUNDS      最大再開回数(デフォルト: 20)
#   FALLBACK_WAIT   リセット時刻を検出できないときの待機秒数(デフォルト: 1800 = 30分)

set -uo pipefail

PROMPT="${1:-/resume して。.claude/session-state.md の「次のステップ」が残っていれば続きから作業し、チェックポイントを取ること。}"
MAX_ROUNDS="${MAX_ROUNDS:-20}"
FALLBACK_WAIT="${FALLBACK_WAIT:-1800}"
CONTINUE_PROMPT="使用制限で中断された。CLAUDE.md の作業継続プロトコルに従い、.claude/session-state.md を確認して続きから作業を再開し、チェックポイントを取ること。すべて完了したら最後に「AUTO_RESUME_DONE」とだけ出力すること。"

if ! command -v claude >/dev/null 2>&1; then
  echo "エラー: claude コマンドが見つかりません。Claude Code CLI をインストールしてください。" >&2
  exit 1
fi

log() { echo "[auto-resume $(date '+%Y-%m-%d %H:%M:%S')] $*"; }

# 出力から使用制限エラーを検出する(例: "Claude AI usage limit reached|1735689600")
is_limit_error() {
  grep -qiE 'usage limit|limit reached|rate.?limit' <<< "$1"
}

# 出力からリセット時刻(unix epoch 10桁)を抽出。見つからなければ空を返す
extract_reset_epoch() {
  grep -oiE '(usage limit|limit reached)[^0-9]*[0-9]{10}' <<< "$1" \
    | grep -oE '[0-9]{10}' | tail -1
}

wait_until_reset() {
  local output="$1" epoch now wait_sec
  epoch="$(extract_reset_epoch "$output")"
  now="$(date +%s)"
  if [ -n "$epoch" ] && [ "$epoch" -gt "$now" ]; then
    wait_sec=$((epoch - now + 120))  # リセット時刻 + 2分の余裕
    log "制限リセット時刻を検出: $(date -d "@$epoch" '+%H:%M:%S' 2>/dev/null || date -r "$epoch" '+%H:%M:%S')(${wait_sec}秒待機)"
  else
    wait_sec="$FALLBACK_WAIT"
    log "リセット時刻を検出できないため ${wait_sec} 秒待って再試行します"
  fi
  sleep "$wait_sec"
}

round=1
current_prompt="$PROMPT"
while [ "$round" -le "$MAX_ROUNDS" ]; do
  log "ラウンド ${round}/${MAX_ROUNDS}: claude を実行します"

  if [ "$round" -eq 1 ]; then
    output="$(claude -p "$current_prompt" 2>&1)"
  else
    output="$(claude --continue -p "$current_prompt" 2>&1)"
  fi
  exit_code=$?
  echo "$output"

  if is_limit_error "$output"; then
    log "使用制限を検出しました。リセットを待って自動再開します。"
    wait_until_reset "$output"
    current_prompt="$CONTINUE_PROMPT"
    round=$((round + 1))
    continue
  fi

  if [ "$exit_code" -ne 0 ]; then
    log "claude が終了コード ${exit_code} で失敗しました(制限以外のエラー)。60秒後に1回だけ再試行します。"
    sleep 60
    current_prompt="$CONTINUE_PROMPT"
    round=$((round + 1))
    continue
  fi

  log "正常に完了しました(ラウンド ${round})。"
  exit 0
done

log "最大再開回数(${MAX_ROUNDS})に達しました。.claude/session-state.md を確認してください。" >&2
exit 1
