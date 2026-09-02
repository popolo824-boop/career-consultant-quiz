#!/usr/bin/env python3
"""index.html 内の QUIZ_DATA の整合性を検査する。

チェック項目:
  - JSON として解析できるか
  - 各設問に stem / choices / answer / explanations が揃っているか
  - choices と explanations の件数が一致しているか
  - answer が 1..len(choices) の範囲内か
  - 解説の ○/× マークが正答と整合しているか
    （通常の設問は正答が「○」、「不適切／誤っている」型の設問は正答が「×」）
  - 問番号が 1 から連番になっているか
  - stem の「問N」表記がキーと一致しているか

使い方: python3 scripts/check_quiz_data.py [index.html]
終了コード: 問題なし=0 / 問題あり=1
"""
import json
import re
import sys

MARKER = "const QUIZ_DATA = "

# 「最も不適切なものはどれか」型の設問。正答の解説が「×」始まりになる。
NEGATIVE_KEYWORDS = ("不適切", "誤っている", "誤りである", "適切でない")


def extract(html):
    start = html.index(MARKER) + len(MARKER)
    depth = 0
    i = start
    in_str = False
    esc = False
    while i < len(html):
        c = html[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return html[start:i + 1]
        i += 1
    raise ValueError("QUIZ_DATA の終端 } が見つかりません")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    html = open(path, encoding="utf-8").read()
    try:
        data = json.loads(extract(html))
    except Exception as e:
        print(f"NG: QUIZ_DATA を JSON として解析できません: {e}")
        return 1

    errors = []
    for rnd in sorted(data, key=int):
        qs = data[rnd]
        nums = sorted(qs, key=int)
        expected = [str(n) for n in range(1, len(nums) + 1)]
        if nums != expected:
            missing = sorted(set(expected) - set(nums), key=int)
            extra = sorted(set(nums) - set(expected), key=int)
            errors.append(f"第{rnd}回: 問番号が連番でない (欠番={missing} 余分={extra})")

        for qn in nums:
            q = qs[qn]
            where = f"第{rnd}回 問{qn}"
            for field in ("stem", "choices", "answer", "explanations"):
                if field not in q:
                    errors.append(f"{where}: {field} がありません")
            if not all(f in q for f in ("stem", "choices", "answer", "explanations")):
                continue

            choices, expls, ans = q["choices"], q["explanations"], q["answer"]
            if len(choices) != len(expls):
                errors.append(
                    f"{where}: choices({len(choices)}) と explanations({len(expls)}) の件数が不一致"
                )
            if not isinstance(ans, int) or not 1 <= ans <= len(choices):
                errors.append(f"{where}: answer={ans!r} が選択肢の範囲外")
                continue

            negative = any(k in q["stem"] for k in NEGATIVE_KEYWORDS)
            answer_mark = "×" if negative else "○"
            other_mark = "○" if negative else "×"
            for idx, ex in enumerate(expls, start=1):
                head = ex.strip()[:1]
                want = answer_mark if idx == ans else other_mark
                if head != want:
                    errors.append(
                        f"{where}: 解説{idx} は「{want}」で始まるべきですが「{head}」です"
                        + ("（不適切・誤りを選ぶ設問）" if negative else "")
                    )

            m = re.match(r"問\s*(\d+)", q["stem"])
            if m and m.group(1) != qn:
                errors.append(f"{where}: stem の「問{m.group(1)}」がキーと不一致")

    total = sum(len(v) for v in data.values())
    rounds = "、".join(f"第{r}回 {len(data[r])}問" for r in sorted(data, key=int))
    print(f"回次: {rounds}（合計 {total}問）")
    if errors:
        print(f"\nNG: {len(errors)} 件の問題を検出しました")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: 整合性チェックをすべて通過しました")
    return 0


if __name__ == "__main__":
    sys.exit(main())
