# Migration Report — CCAR Prompt Engineering Techniques (2026-09)

## Source (not stored in repo)

Local CCAR study cheat sheet (2026-09-09): Building with the Claude API — Prompt engineering techniques.

Exam items, scores, and credential materials are **not** archived. Evaluation loop and API enforcement were already ingested (`ccar-prompt-eval-and-api-2026-09.md`).

## Files created

- `knowledge/patterns/explicit-before-elaborate-prompt.md`
- `knowledge/migrations/ccar-prompt-engineering-2026-09.md`

## Files updated

- `knowledge/patterns/define-success-before-prompt-change.md`
- `adapters/claude/CLAUDE.md` — v1.4
- `core/ai-collaboration.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Explicit before elaborate | 長くする前に Task / Output / Constraints を明示 |
| Failure → intervention | 曖昧→指示、形式→format、境界→diverse examples、抜け→分解、必須→決定論 |
| Examples | 境界の具体化。指示の代替でも量産でもない |
| Engineering vs Evaluation | 介入と証拠を分ける |

## Suggested commit message

```text
feat(knowledge): make prompts explicit before elaborate, and match the fix to the failure
```
