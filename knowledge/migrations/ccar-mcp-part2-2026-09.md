# Migration Report — CCAR MCP Part 2 (2026-09)

## Source (not stored in repo)

Local CCAR study cheat sheet (2026-09-05): Introduction to Model Context Protocol (MCP) — Part 2.

Part 1 and Subagents sheets in the same folder were already ingested (`ccar-agentic-mcp-subagents-2026-09.md`). No re-ingest.

Exam items, scores, and credential materials are **not** archived.

## Files updated

- `knowledge/patterns/mcp-as-integration-not-authority.md` — Tool / Resource / Prompt; tool contract; Authentication ≠ Authorization; warning text ≠ control; structured errors
- `adapters/claude/CLAUDE.md` — v1.2
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`
- `knowledge/migrations/ccar-mcp-part2-2026-09.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本
- MCP Part 3（client/server、trust boundary、injection）— 未受領。Tool 戻り値の信頼境界は Tool Use シートから `ccar-tool-use-2026-09.md` で別途取り込み済み

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Tool / Resource / Prompt | 実行・参照・再利用の聞き方。Prompt は Tool ではない |
| Tool contract | 名前・Schema・副作用が曖昧だと誤実行。似た Tool を増やさない |
| Authn vs Authz | 身元確認 ≠ 操作範囲。同じ Server でも Tool ごとに Control |
| High-impact | 説明文の警告は制御ではない。承認・権限・監査 |
| Failure | 構造化エラー + bounded retry + 安全停止 |

## Suggested commit message

```text
feat(knowledge): extend MCP pattern with tool contracts, authz, and error handling
```
