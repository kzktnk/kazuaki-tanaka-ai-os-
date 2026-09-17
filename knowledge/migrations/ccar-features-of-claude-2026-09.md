# Migration Report — CCAR Features of Claude (2026-09)

## Source (not stored in repo)

Local study cheat sheet (2026-09-17): Building with the Claude API — Features of Claude.

Access-by-volatility, Tool Use vs MCP, and LLM vs application enforcement were already ingested. This sheet adds the layering: persistent project context for stable reuse, relevant context over maximum context, centralized team behavior, and the reminder that persistence / structure / tool access are not trust.

Exam items, scores, and credential materials are **not** archived.

## Files created

- `knowledge/patterns/match-capability-to-context-job.md`
- `knowledge/migrations/ccar-features-of-claude-2026-09.md`

## Files updated

- `knowledge/patterns/choose-access-by-volatility.md`
- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md`
- `adapters/claude/CLAUDE.md` — v1.7
- `playbooks/ai-poc-quality-review.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Feature selection | 安定再利用 → 永続コンテキスト。大／変化 → Retrieval。ライブ／外部 → Tool。機械出力 → Structured。秘密・認可・執行 → モデルの外 |
| Persistence | 永続に置ける ≠ 置いてよい。秘密・ライブ状態・認可ロジックは入れない |
| Team reuse | 繰り返す振る舞いを中央管理する。個人のプロンプトに頼らない |
| Context volume | Relevant context > maximum context |
| Trust reminders | Persistent ≠ trusted. Structured ≠ validated. Tool access ≠ permission |

## Suggested commit message

```text
feat(knowledge): match each capability to the job of the context, not to the largest window
```
