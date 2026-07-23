#!/usr/bin/env bash
# 作業継続プロトコル(5時間制限対策)をユーザーレベル(~/.claude)にインストールし、
# このマシン上の「すべてのリポジトリ・すべてのセッション」に適用するスクリプト。
#
# 使い方: bash install-global.sh
# 何度実行しても安全(冪等)。

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_HOME="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
MARKER_BEGIN="<!-- BEGIN work-continuity-protocol -->"
MARKER_END="<!-- END work-continuity-protocol -->"

echo "インストール先: $CLAUDE_HOME"
mkdir -p "$CLAUDE_HOME/skills"

# 1. /checkpoint と /resume スキルを全プロジェクト共通のユーザースキルとしてコピー
for skill in checkpoint resume; do
  mkdir -p "$CLAUDE_HOME/skills/$skill"
  cp "$REPO_DIR/.claude/skills/$skill/SKILL.md" "$CLAUDE_HOME/skills/$skill/SKILL.md"
  echo "  スキルを配置: /$skill"
done

# 2. 作業継続プロトコルをユーザーレベル CLAUDE.md に追記(マーカーで重複防止・更新可能)
GLOBAL_MD="$CLAUDE_HOME/CLAUDE.md"
PROTOCOL_FILE="$(mktemp)"
trap 'rm -f "$PROTOCOL_FILE"' EXIT
{
  echo "$MARKER_BEGIN"
  # リポジトリの CLAUDE.md から「作業継続プロトコル」セクションのみ抽出
  awk '/^## 作業継続プロトコル/{flag=1} /^## プロジェクト概要/{flag=0} flag' "$REPO_DIR/CLAUDE.md"
  echo "$MARKER_END"
} > "$PROTOCOL_FILE"

touch "$GLOBAL_MD"
if grep -qF "$MARKER_BEGIN" "$GLOBAL_MD"; then
  # 既存ブロックを最新版に置換
  awk -v begin="$MARKER_BEGIN" -v end="$MARKER_END" -v file="$PROTOCOL_FILE" '
    $0 == begin {skip=1; while ((getline line < file) > 0) print line; close(file); next}
    $0 == end {skip=0; next}
    !skip {print}
  ' "$GLOBAL_MD" > "$GLOBAL_MD.tmp" && mv "$GLOBAL_MD.tmp" "$GLOBAL_MD"
  echo "  ~/.claude/CLAUDE.md のプロトコルを更新"
else
  { echo ""; cat "$PROTOCOL_FILE"; } >> "$GLOBAL_MD"
  echo "  ~/.claude/CLAUDE.md にプロトコルを追記"
fi

# 3. 自動再開ウォッチドッグをユーザーレベル bin にコピー
mkdir -p "$CLAUDE_HOME/bin"
cp "$REPO_DIR/scripts/claude-auto-resume.sh" "$CLAUDE_HOME/bin/claude-auto-resume"
chmod +x "$CLAUDE_HOME/bin/claude-auto-resume"
echo "  自動再開スクリプトを配置: $CLAUDE_HOME/bin/claude-auto-resume"

# 4. SessionStart フックをユーザーレベル settings.json にマージ(python3 が必要)
SETTINGS="$CLAUDE_HOME/settings.json"
HOOK_CMD='if [ -f "$CLAUDE_PROJECT_DIR/.claude/session-state.md" ]; then echo "=== 前回セッションの作業状態 (.claude/session-state.md) ==="; cat "$CLAUDE_PROJECT_DIR/.claude/session-state.md"; echo "=== 「次のステップ」が残っている場合、再開指示があれば即座に続きから着手すること ==="; fi'

if command -v python3 >/dev/null 2>&1; then
  HOOK_CMD="$HOOK_CMD" SETTINGS="$SETTINGS" python3 - <<'PY'
import json, os

settings_path = os.environ["SETTINGS"]
hook_cmd = os.environ["HOOK_CMD"]

settings = {}
if os.path.exists(settings_path):
    with open(settings_path) as f:
        content = f.read().strip()
        if content:
            settings = json.loads(content)

hooks = settings.setdefault("hooks", {})
session_start = hooks.setdefault("SessionStart", [])

already = any(
    h.get("command") == hook_cmd
    for entry in session_start
    for h in entry.get("hooks", [])
)
if not already:
    session_start.append({"hooks": [{"type": "command", "command": hook_cmd}]})
    with open(settings_path, "w") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("  ~/.claude/settings.json に SessionStart フックを追加")
else:
    print("  SessionStart フックは設定済み")
PY
else
  echo "  警告: python3 が見つからないため settings.json のマージをスキップしました。"
  echo "  $SETTINGS に以下の SessionStart フックを手動で追加してください:"
  echo "    $HOOK_CMD"
fi

echo ""
echo "完了。新しいセッションから全リポジトリで以下が有効になります:"
echo "  - サブタスク完了ごとの自動チェックポイント(コミット&プッシュ+状態記録)"
echo "  - Web セッション: デッドマンスイッチによる制限リセット後の自動再開"
echo "  - /checkpoint : 手動で状態保存(制限が近いとき)"
echo "  - /resume     : リセット後に続きから再開"
echo "  - セッション開始時に前回の作業状態を自動表示"
echo ""
echo "ローカル CLI での無人自動再開(どのリポジトリでも使用可):"
echo "  $CLAUDE_HOME/bin/claude-auto-resume \"タスク内容\""
echo ""
echo "注意: 各リポジトリに .claude/session-state.md がない場合、最初のチェックポイント時に自動作成されます。"
