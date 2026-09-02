// Variables used by Scriptable.
// These must be at the very top of the file. Do not edit.
// icon-color: deep-purple; icon-glyph: gauge-high;
//
// Claude Code の稼働状況と利用枠の残量を表示するホーム画面ウィジェット。
//
// データ元: Mac 上の Claude Code のステータスラインが書き出す
//           claude-status.json（claude-status-export.sh を参照）。
//
// 使い方:
//   1. このファイルを Scriptable に新規スクリプトとして貼り付け、
//      "ClaudeUsage" という名前で保存する。
//   2. ホーム画面に Scriptable ウィジェット（小 or 中）を追加し、
//      Script に ClaudeUsage を指定する。
//
// Mac を使わず、状態 JSON を URL 経由で取得する場合は
// REMOTE_URL に JSON の URL を設定する（ローカルファイルより優先）。

const FILE_NAME = "claude-status.json";
const REMOTE_URL = "";        // 例: "https://raw.githubusercontent.com/user/repo/main/claude-status.json"
const STALE_AFTER_SEC = 15 * 60;  // これを過ぎたら「待機中」扱い

// ---- 配色（ライト / ダーク両対応）------------------------------------------
const C = {
  bg:    Color.dynamic(new Color("#ffffff"), new Color("#1c1c1e")),
  text:  Color.dynamic(new Color("#1f2937"), new Color("#f2f2f7")),
  sub:   Color.dynamic(new Color("#6b7280"), new Color("#98989f")),
  track: Color.dynamic(new Color("#e5e7eb"), new Color("#3a3a3c")),
  ok:    Color.dynamic(new Color("#16a34a"), new Color("#30d158")),
  warn:  Color.dynamic(new Color("#d97706"), new Color("#ff9f0a")),
  crit:  Color.dynamic(new Color("#dc2626"), new Color("#ff453a")),
};

const isSmall = config.runsInWidget && config.widgetFamily === "small";
const BAR_W = isSmall ? 130 : 250;

// ---- データ取得 -------------------------------------------------------------

async function loadStatus() {
  if (REMOTE_URL) {
    try {
      return await new Request(REMOTE_URL).loadJSON();
    } catch (e) {
      return { error: "取得失敗: " + e.message };
    }
  }
  try {
    const fm = FileManager.iCloud();
    const path = fm.joinPath(fm.documentsDirectory(), FILE_NAME);
    if (!fm.fileExists(path)) return { error: FILE_NAME + " がありません" };
    // iCloud 上でファイルが実体化されていないことがある。
    if (!fm.isFileDownloaded(path)) await fm.downloadFileFromiCloud(path);
    return JSON.parse(fm.readString(path));
  } catch (e) {
    return { error: "読み込み失敗: " + e.message };
  }
}

// ---- 表示ヘルパー -----------------------------------------------------------

const nowSec = () => Math.floor(Date.now() / 1000);

function barColor(pct) {
  if (pct >= 80) return C.crit;
  if (pct >= 50) return C.warn;
  return C.ok;
}

// 経過秒を「2時間3分」「45分」「12日」の形にする。
function humanizeSec(sec) {
  if (sec < 60) return "1分未満";
  const m = Math.floor(sec / 60);
  if (m < 60) return `${m}分`;
  const h = Math.floor(m / 60);
  if (h < 24) return m % 60 === 0 ? `${h}時間` : `${h}時間${m % 60}分`;
  return `${Math.floor(h / 24)}日${h % 24 ? h % 24 + "時間" : ""}`;
}

// 枠の状態を、リセット済みかどうかまで含めて解釈する。
// resets_at を過ぎていれば Claude 側の枠は空になっているので 0% と見なす。
function readWindow(w) {
  if (!w || w.used_pct == null) return null;
  const left = w.resets_at ? w.resets_at - nowSec() : null;
  if (left != null && left <= 0) return { pct: 0, note: "リセット済み" };
  return {
    pct: Math.max(0, w.used_pct),
    note: left == null ? null
        : left < 60 ? "まもなくリセット"
        : `${humanizeSec(left)}後にリセット`,
  };
}

function addBar(stack, label, win) {
  const row = stack.addStack();
  row.layoutHorizontally();
  const l = row.addText(label);
  l.font = Font.mediumSystemFont(11);
  l.textColor = C.sub;
  row.addSpacer();
  const v = row.addText(win ? `${Math.round(win.pct)}%` : "—");
  v.font = Font.boldSystemFont(11);
  v.textColor = win ? barColor(win.pct) : C.sub;

  stack.addSpacer(3);

  const track = stack.addStack();
  track.size = new Size(BAR_W, 6);
  track.cornerRadius = 3;
  track.backgroundColor = C.track;
  if (win && win.pct > 0) {
    const fill = track.addStack();
    // 1% でも視認できるよう下限を、超過時はトラック幅を上限とする。
    const filled = Math.min(BAR_W, Math.max(4, (BAR_W * win.pct) / 100));
    fill.size = new Size(filled, 6);
    fill.cornerRadius = 3;
    fill.backgroundColor = barColor(win.pct);
    fill.addSpacer();
  }

  if (win && win.note) {
    stack.addSpacer(2);
    const n = stack.addText(win.note);
    n.font = Font.systemFont(9);
    n.textColor = C.sub;
  }
}

// ---- ウィジェット構築 -------------------------------------------------------

function buildWidget(data) {
  const w = new ListWidget();
  w.backgroundColor = C.bg;
  w.setPadding(12, 14, 12, 14);
  // 5分ごとの更新を要求する（実際の間隔は iOS が決める）。
  w.refreshAfterDate = new Date(Date.now() + 5 * 60 * 1000);

  if (data.error) {
    const t = w.addText("Claude");
    t.font = Font.boldSystemFont(13);
    t.textColor = C.text;
    w.addSpacer(6);
    const e = w.addText(data.error);
    e.font = Font.systemFont(11);
    e.textColor = C.sub;
    e.lineLimit = 4;
    return w;
  }

  const age = nowSec() - (data.updated_at || 0);
  const stale = age > STALE_AFTER_SEC;

  // ヘッダー: 稼働状態と最終更新
  const head = w.addStack();
  head.layoutHorizontally();
  head.centerAlignContent();
  const dot = head.addText(stale ? "○" : "●");
  dot.font = Font.systemFont(10);
  dot.textColor = stale ? C.sub : C.ok;
  head.addSpacer(4);
  const title = head.addText(stale ? "待機中" : "実行中");
  title.font = Font.boldSystemFont(12);
  title.textColor = C.text;
  head.addSpacer();
  const ago = head.addText(age < 60 ? "たった今" : humanizeSec(age) + "前");
  ago.font = Font.systemFont(10);
  ago.textColor = C.sub;

  w.addSpacer(10);

  const limits = data.limits || {};
  addBar(w, "5時間枠", readWindow(limits.five_hour));
  w.addSpacer(isSmall ? 8 : 10);
  addBar(w, "7日枠", readWindow(limits.seven_day));
  if (limits.spend) {
    w.addSpacer(isSmall ? 8 : 10);
    addBar(w, "利用額", readWindow(limits.spend));
  }

  // タスクの状況（中サイズのみ）
  const s = data.session || {};
  if (!isSmall) {
    w.addSpacer(10);
    const name = s.name || s.repo || s.dir;
    if (name) {
      const n = w.addText(name);
      n.font = Font.mediumSystemFont(11);
      n.textColor = C.text;
      n.lineLimit = 1;
      w.addSpacer(2);
    }
    const bits = [];
    if (s.model) bits.push(s.model);
    if (data.context && data.context.used_pct != null) {
      bits.push(`ctx ${Math.round(data.context.used_pct)}%`);
    }
    if (s.duration_ms) bits.push(humanizeSec(Math.floor(s.duration_ms / 1000)));
    if (s.lines_added != null || s.lines_removed != null) {
      bits.push(`+${s.lines_added || 0}/-${s.lines_removed || 0}`);
    }
    if (bits.length) {
      const m = w.addText(bits.join("  ·  "));
      m.font = Font.systemFont(10);
      m.textColor = C.sub;
      m.lineLimit = 1;
      m.minimumScaleFactor = 0.8;
    }
  }

  w.addSpacer();
  return w;
}

// ---- エントリポイント -------------------------------------------------------

const status = await loadStatus();
const widget = buildWidget(status);

if (config.runsInWidget) {
  Script.setWidget(widget);
} else {
  await widget.presentMedium();
}
Script.complete();
