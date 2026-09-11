# Migration Report — CCAR RAG and Agentic Search (2026-09)

## Source (not stored in repo)

Local CCAR study cheat sheet (2026-09-11): Building with the Claude API — RAG and Agentic Search.

Static vs live was already in `mcp-as-integration-not-authority.md`. Retrieval vs generation for tables was already in `playbooks/rag-structure-diagnosis.md`. This sheet adds the missing middle (changing corpus vs real-time state), Agentic Search as bounded iterative retrieval, and source-authority / freshness rules.

Exam items, scores, and credential materials are **not** archived.

## Files created

- `knowledge/patterns/choose-access-by-volatility.md`
- `knowledge/migrations/ccar-rag-agentic-search-2026-09.md`

## Files updated

- `knowledge/patterns/mcp-as-integration-not-authority.md`
- `knowledge/patterns/workflow-vs-agent-vs-human.md`
- `knowledge/patterns/logical-vs-physical-document-unity.md`
- `playbooks/rag-structure-diagnosis.md`
- `playbooks/ai-poc-quality-review.md`
- `knowledge/lessons/ai-output-evaluation-terms.md`
- `adapters/claude/CLAUDE.md` — v1.6
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Access path | 安定 → context。変化するコーパス → RAG。現在の状態 → live。探索が観察依存 → Agentic Search |
| RAG | 取得してから根拠生成。正しさも鮮度も保証しない。鮮度はソース依存 |
| Diagnosis | Retrieval と Generation を分ける。関連ヒット ≠ 必要 Evidence |
| Authority | 最新が常に正本ではない。解けない矛盾は隠さない |
| Agentic Search | 反復が必要なときだけ。停止条件を先に置く |

## Suggested commit message

```text
feat(knowledge): choose information access by volatility, not by defaulting to RAG
```
