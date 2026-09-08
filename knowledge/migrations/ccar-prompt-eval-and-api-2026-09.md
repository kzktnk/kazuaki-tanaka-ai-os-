# Migration Report — CCAR Prompt Evaluation and Claude API access (2026-09)

## Source (not stored in repo)

Local CCAR study cheat sheets (2026-09-08):

- Building with the Claude API — Prompt evaluation
- Building with the Claude API — Accessing Claude with the API

Exam items, scores, and credential materials are **not** archived.

## Files created

- `knowledge/patterns/define-success-before-prompt-change.md`
- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md`
- `knowledge/migrations/ccar-prompt-eval-and-api-2026-09.md`

## Files updated

- `knowledge/lessons/ai-output-evaluation-terms.md` — 1件の語彙と、Prompt 変更の評価ループを分離
- `adapters/claude/CLAUDE.md` — v1.3
- `playbooks/ai-poc-quality-review.md`
- `knowledge/patterns/ai-capability-vs-authority.md`
- `knowledge/patterns/mcp-as-integration-not-authority.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Prompt 改善の順序 | 成功条件が先。代表＋edge＋high-risk。回帰を見る。grader を評価する。平均点だけでは採用しない |
| API / アプリ境界 | LLM は判断。認可・秘密・検証・承認は決定論レイヤ。出力は実行命令ではない |

## Suggested commit message

```text
feat(knowledge): define success before prompt change, and keep enforcement off the model
```
