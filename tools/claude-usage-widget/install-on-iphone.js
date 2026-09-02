// Scriptable に貼り付けて一度だけ実行すると、
// ClaudeUsage ウィジェット本体をダウンロードして保存する。
// 更新したいときも、これをもう一度実行するだけでよい。
const URL = "https://raw.githubusercontent.com/popolo824-boop/career-consultant-quiz/refs/heads/claude/command-support-juerey/tools/claude-usage-widget/ClaudeUsage.js";
const src = await new Request(URL).loadString();
const fm = FileManager.iCloud();
fm.writeString(fm.joinPath(fm.documentsDirectory(), "ClaudeUsage.js"), src);
console.log("ClaudeUsage.js を保存しました。Scriptable のスクリプト一覧に出ます。");
