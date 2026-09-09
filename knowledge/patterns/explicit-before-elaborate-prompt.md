# Pattern: Explicit Before Elaborate Prompt

**Status:** Active  
**Origin:** Generalized from Prompt Engineering Techniques study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **Prompt を長く複雑にする前に、Task / Context / Constraints / Output / Success を明示する。失敗の種類を見て、打ち手を1つ選ぶ。Examples は境界の具体化であり、指示の代替ではない。**

評価（証拠）は `knowledge/patterns/define-success-before-prompt-change.md`。本パターンは **介入** である。必須遵守の執行は Prompt に書いても足りない（`knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md`）。

## Core distinction

順序:

```text
Clarify task → Clarify output → Relevant context
→ Representative examples → Decompose if needed
→ Evaluate → Iterate
```

長い Prompt は1段落に詰め込まない。Context / Task / Constraints / Examples / Output format を分ける。長さより構造と明確さ。

| 失敗 | 先にすること |
|---|---|
| 依頼が曖昧 | 指示を明確にする（何を見て、何を返すか） |
| 形式が不安定 | Output format。推論を足す前に形式を固定 |
| Label / 境界が混ざる | 代表的で多様な Examples。同じ例の量産はしない |
| 手順抜け | 明示的に分解。単純 Task まで細分化しない |
| 無関係な長文 | Context を減らす / 整理する。Relevant > more |
| Critical rule 違反 | Deterministic enforcement。Prompt を強く書かない |
| 改善が分からない | 評価スイート。全面書き換えしない |

Role は視点の補助であり、Task / Criteria の代替ではない。「〜として振る舞え」だけで品質は保証しない。大きい Model に乗り換える前に、Failure mode を特定する。

Examples は desired pattern・境界・edge の望む判断を示す。少ないが代表的で多様な例の方が、似た例の大量投入より強い。似た例を増やすと表面的な Pattern に過学習する。

複数の問題を一度に全面書き換えしない。Failure category ごとに狙って直し、代表スイートで回帰を見る。

> **Prompt Engineering = intervention. Prompt Evaluation = evidence.**

## Signals

- 曖昧な依頼に、まず Examples を足している  
- System prompt を長くすれば安定する、と考えている  
- Role 指定だけで品質を保証しようとしている  
- Few-shot は多いほど良い、としている  
- Critical rule を Prompt の強い言い回しで守らせようとしている  
- 失敗の種類を見ずに Model を上げている  
- 形式の問題なのに推論を足している  

## Core rule

> Be explicit before being elaborate. Diagnose the failure, then change one thing. Examples clarify boundaries; they do not replace instructions. Evaluate every meaningful change.

## Related

- `knowledge/patterns/define-success-before-prompt-change.md` — 成功条件と評価スイート  
- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md` — 必須遵守はアプリ側  
- `knowledge/lessons/ai-output-evaluation-terms.md`  
- `core/ai-collaboration.md` — 問いの設計  
- `adapters/claude/CLAUDE.md`  
