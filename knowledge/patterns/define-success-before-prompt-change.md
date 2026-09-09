# Pattern: Define Success Before Prompt Change

**Status:** Active  
**Origin:** Generalized from Prompt Evaluation study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **Prompt を直す前に、成功条件・代表ケース・重大失敗を定義する。1例の成功や平均点の上昇は、改善の証明ではない。**

1件の出力を切る語彙（Accuracy / Completeness / Groundedness 等）は `knowledge/lessons/ai-output-evaluation-terms.md`。本パターンは **Prompt を変える仕事の順序** である。

## Core distinction

| 悪い | 良い |
|---|---|
| 良さそうになるまで試して Deploy | Success criteria → Eval set → Baseline → 変更 → 再評価 → 失敗分析 |
| 「高品質」で採点者が割れる | 観測できる次元へ分解する |
| 簡単なケース・今の Prompt が得意なケースだけ | 本番入力を代表し、edge と high-risk を含む |
| 平均点が最も高い案を採用 | 事業目的と Risk weighting。Safety-critical が弱い案は落とす |
| 1ケース成功で修正完了 | 代表スイート再実行。改善と回帰の両方を見る |
| Automated / LLM grader を無条件に信じる | Grader 自体を評価する。Rubric・人の校正・抜検 |

評価次元は内容の正しさだけではない。Relevance、指定形式、Safety、Consistency、Latency、Cost も、本番目的に入るなら測る。

```text
Quality × Risk × Latency × Cost
```

失敗の種類（抜け、幻覚、形式、不安全、誤った Tool 選択、根拠のない主張）が、直す対象を決める。種類を混ぜない。

LLM-as-a-Judge は流暢さを過大評価し、根拠のない主張を見逃しやすい。Judge を Judge する。

## Signals

- Prompt 改善の議論が、成功条件なしに始まっている  
- Easy cases だけ高得点で、例外・高リスクが測られていない  
- 平均点は高いが、重大失敗が残っている案を採用しようとしている  
- 修正後に1例だけ見て「直った」としている  
- LLM grader の点数を、人の校正なしに採用している  
- Accuracy だけ上がり、Latency / Cost / Risk を見ていない  

## Core rule

> Define success before optimizing. Representative cases include edge and high-risk. Re-run the suite and check regressions. Validate the grader. Do not pick the highest average score.

## Related

- `knowledge/lessons/ai-output-evaluation-terms.md` — 1件の切り方  
- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`  
- `playbooks/ai-poc-quality-review.md`  
- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md`  
- `knowledge/patterns/explicit-before-elaborate-prompt.md` — 介入。失敗の種類で打ち手を選ぶ  
- `adapters/claude/CLAUDE.md`  
