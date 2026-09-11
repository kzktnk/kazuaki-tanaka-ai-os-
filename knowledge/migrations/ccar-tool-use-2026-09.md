# Migration Report — CCAR Tool Use with Claude (2026-09)

## Source (not stored in repo)

Local CCAR study cheat sheet (2026-09-11): Building with the Claude API — Tool use with Claude.

MCP Part 1–2, Agentic, and API enforcement sheets were already ingested (`ccar-agentic-mcp-subagents-2026-09.md`, `ccar-mcp-part2-2026-09.md`, `ccar-prompt-eval-and-api-2026-09.md`). This sheet adds the Tool Use loop, tool-result trust boundary, and the MCP vs Tool Use split.

Exam items, scores, and credential materials are **not** archived.

## Files created

- `knowledge/patterns/tool-output-as-untrusted-data.md`
- `knowledge/migrations/ccar-tool-use-2026-09.md`

## Files updated

- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md`
- `knowledge/patterns/mcp-as-integration-not-authority.md`
- `knowledge/patterns/workflow-vs-agent-vs-human.md`
- `knowledge/patterns/ai-capability-vs-authority.md`
- `frameworks/human-oversight.md`
- `adapters/claude/CLAUDE.md` — v1.5
- `playbooks/responsible-ai-assessment.md`
- `knowledge/migrations/ccar-mcp-part2-2026-09.md` — Part 3 未受領注記を更新
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Tool Use vs MCP | Tool Use はモデルが Tool を選ぶ相互作用。MCP は Tools / Data の標準公開。Application が検証・認可・執行 |
| Model-generated input | Schema 通りでも未検証。Valid input ≠ authorized action |
| Prompt で禁止 | 使わせないなら非公開。広い権限は信頼性機能ではない |
| Tool result | 戻り値・Resource・外部文面は data。命令として採用しない |
| High-impact / audit | 承認は制御。監査は追跡可能性であり正しさの証明ではない |

## Suggested commit message

```text
feat(knowledge): treat tool output as untrusted data, and keep enforcement off the model
```
