# Pattern: Issue Structuring Reserves Three Judgments

**Status:** Active  
**Origin:** Generalized from an issue-structuring Skill and a fictional first-pass trial (2026-09). Client names, filled case numbers, and the trial memo are **not** stored here.

## Pattern statement

> **論点整理の入口は手順を持たない。4Cs の各項は事実／仮定／不明と出典を付ける。顧客の問いが打ち手先行なら、採用した読みを冒頭1行で残し、打ち手は仮説の枝に置く。Key Question・Criteria・検証の着手順は人が決める。仮説は支持と反証の両方。空欄は「未確認」。分析計画の End product は「どの図で何が言えるか」。ストーリーボードは章タイトルだけ。自己検証は項目ごとに判定し、全部OKで済まない。**

手順の本体は `standards/strategy-engagement-guide.md` Step 1〜3。入口の三層は `knowledge/patterns/skills-point-to-rules-not-source.md`。本パターンは **人が残す3点と、打ち手先行の読み方** である。

## Core distinction

| AI がやってよい | 人が決める |
|---|---|
| 4Cs を事実／仮定／不明で埋める | Key Question の一文 |
| ツリーの型を選び、理由を1行残す | Criteria（実際に何で決めるか） |
| 末端を問いの形にし、仮説を1つ置く | どの仮説から検証するか |
| 支持する事実と支持しない事実 | 推測した判断軸を確定扱いにすること |

ユーザーが不在でも止まらない。最も妥当な読みで進め、その読みを冒頭に1行で書く。

顧客の問いが How から始まっているときは、How を Key Question にしない。What を問い、How は供給・能力の枝の仮説に置く（`frameworks/thinking-patterns/pattern-01-why-what-how.md`）。前回頓挫した打ち手から検証を始めない。

比率目標だけが Criteria のとき、本業の伸びで達成度が変わる。絶対額・投資上限・現場負荷のどれが先かを `【要判断】` に残す。

確度の低い仮説（伝聞のみ、真偽未確認）は、本文の奥に隠さない。朝いちばんに見る3点の3番に置く。

分析計画の End product は成果物の種類名で止めない。「どの図で、何が言えるか」まで書く。ストーリーボードは各章のメッセージ1文。スライド化は別仕事。

自己検証はチェックリストを1項目ずつ判定する。満たさない項目は理由を残す。この工程の外（Work plan 等）は「範囲外・次工程」と書く。

Cursor での入口は `.cursor/skills/issue-structuring/SKILL.md`。出力は `outputs/`（gitignore）。追跡対象ファイルに顧客実名を書かない。

## Signals

- 顧客が言った打ち手が、そのまま Key Question になっている  
- Criteria を推測で確定している  
- 4Cs に出典も区分もない  
- 仮説表が賛成材料だけ、または空欄のまま  
- 前回失敗した打ち手から検証を始めている  
- End product が「分析する」「資料を作る」で止まっている  
- 自己検証が「全部OK」  
- Skill 本文に Step 1〜3 の手順を再掲している  

## Core rule

> Reserve the key question, the real decision criteria, and the verification order for the human. Adopt a reading and name it. Put How on a hypothesis branch. Cite facts. Write both supporting and contradicting evidence. Do not stop when the user is absent.

## Related

- `standards/strategy-engagement-guide.md` — Step 1〜3 と品質チェック  
- `knowledge/patterns/skills-point-to-rules-not-source.md` — 入口は手順を持たない  
- `frameworks/thinking-patterns/pattern-01-why-what-how.md` — How を先にしない  
- `core/reasoning.md` — 事実と仮定  
- `frameworks/consulting-strategy-process.md` — Common Failure Modes  
- `standards/writing.md`  
- `.cursor/skills/issue-structuring/SKILL.md`  
