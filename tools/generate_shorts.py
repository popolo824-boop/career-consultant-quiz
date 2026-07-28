#!/usr/bin/env python3
"""index.html の QUIZ_DATA からショート動画（TikTok / YouTube Shorts / リール）用の
台本を生成する。

使い方:
    python3 tools/generate_shorts.py --count 10            # 短い問題から10本
    python3 tools/generate_shorts.py --count 10 --offset 10  # 次の10本
    python3 tools/generate_shorts.py --round 31 --count 5    # 第31回だけから

出力: shorts/scripts_batch_<offset+1>-<offset+count>.md と同名の .csv
CSV は Vrew / CapCut などの一括字幕・読み上げツールにそのまま貼れる列構成。
"""
import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOKS = [
    "これ解けたら合格レベル。",
    "キャリコン受験生の9割が迷う問題。",
    "3秒で答えられますか？",
    "本番で出たらどうする？",
    "この問題、意外と落とします。",
]
CTA = "答え合わせと全{total}問はプロフィールのリンクから。"


def load_quiz_data() -> dict:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    m = re.search(r"const QUIZ_DATA = (\{.*?\n\});", html, re.DOTALL)
    if not m:
        raise SystemExit("QUIZ_DATA が index.html から見つかりません")
    return json.loads(m.group(1))


def shorten(text: str, limit: int) -> str:
    text = re.sub(r"^問\s?\d+\s*", "", text).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--round", dest="round_", default=None, help="回で絞る（例: 31）")
    args = ap.parse_args()

    data = load_quiz_data()
    items = []
    total = 0
    for rnd, questions in data.items():
        total += len(questions)
        if args.round_ and rnd != str(args.round_):
            continue
        for qnum, q in questions.items():
            size = len(q["stem"]) + sum(len(c) for c in q["choices"])
            items.append((size, rnd, int(qnum), q))
    # 短い（＝動画向きの）問題から順に
    items.sort(key=lambda t: (t[0], t[1], t[2]))
    batch = items[args.offset : args.offset + args.count]
    if not batch:
        raise SystemExit("対象の問題がありません（offset が大きすぎる可能性）")

    out_dir = ROOT / "shorts"
    out_dir.mkdir(exist_ok=True)
    tag = f"{args.offset + 1}-{args.offset + len(batch)}"
    if args.round_:
        tag = f"r{args.round_}_{tag}"
    md_path = out_dir / f"scripts_batch_{tag}.md"
    csv_path = out_dir / f"scripts_batch_{tag}.csv"

    md = ["# ショート動画台本\n"]
    rows = []
    for i, (_, rnd, qnum, q) in enumerate(batch):
        hook = HOOKS[i % len(HOOKS)]
        stem = shorten(q["stem"], 90)
        answer_idx = q["answer"] - 1
        answer_choice = re.sub(r"^\d+\.\s*", "", q["choices"][answer_idx])
        expl = q["explanations"][answer_idx].lstrip("○×△ ").strip()
        cta = CTA.format(total=total)
        md.append(f"## 動画{i + 1}（第{rnd}回 問{qnum}）\n")
        md.append(f"- **フック（0-2秒）**: {hook}")
        md.append(f"- **問題（2-10秒）**: {stem}")
        for c in q["choices"]:
            md.append(f"  - {c}")
        md.append("- **カウントダウン（3秒）**: 「答えは…」＋効果音")
        md.append(f"- **正解**: {q['answer']}. {answer_choice}")
        md.append(f"- **解説（1文）**: {expl}")
        md.append(f"- **CTA**: {cta}\n")
        rows.append({
            "no": i + 1,
            "round": rnd,
            "q": qnum,
            "hook": hook,
            "stem": stem,
            "choices": " / ".join(q["choices"]),
            "answer": f"{q['answer']}. {answer_choice}",
            "explanation": expl,
            "cta": cta,
        })

    md_path.write_text("\n".join(md), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(batch)} 本分の台本を出力: {md_path.name}, {csv_path.name}")


if __name__ == "__main__":
    main()
