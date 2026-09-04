# Migration Report — CCAR Agentic / MCP / Subagent distillation (2026-09)

## Source (not stored in repo)

Local CCAR study cheat sheets (2026-09-03 / 2026-09-04):

- Introduction to Agentic AI (前半 / 後半)
- Introduction to Model Context Protocol (MCP) — Part 1
- Introduction to subagents

Exam items, scores, and credential materials are **not** archived. Cheat sheet files stay in Downloads.

## Files created

- `knowledge/patterns/workflow-vs-agent-vs-human.md`
- `knowledge/patterns/mcp-as-integration-not-authority.md`
- `knowledge/patterns/subagent-when-isolation-justifies-cost.md`
- `knowledge/migrations/ccar-agentic-mcp-subagents-2026-09.md`

## Files updated

- `adapters/claude/CLAUDE.md` — v1.1: static knowledge vs MCP; Workflow / Agent / Human; Subagent 判断
- `frameworks/human-oversight.md` — risk-based HITL pointer
- `knowledge/patterns/ai-capability-vs-authority.md`
- `knowledge/patterns/authority-levels.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`
- `playbooks/responsible-ai-assessment.md`
- `core/ai-collaboration.md`

## Excluded

- 得点、模試結果、試験問題と選択肢
- チートシート原本の `knowledge/source/` 登録
- MCP Part 2（architecture / schema / injection）— 未受領

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Known path vs observation-dependent path | Workflow vs Agent。重い結果は Human。bounded autonomy |
| MCP | 接続の標準化。Security / Agent の代替ではない。静的は Knowledge、ライブは runtime |
| Subagent | 複雑さでは分けない。隔離・専門・権限分離の便益が orchestration を上回るとき |

## Placement rationale

- 判断はモデル非依存 → `knowledge/patterns/`
- Claude の Connector / Project knowledge の切り方 → adapter
- 監督・権限の既存枠（HITL、authority levels）は複製せず pointer

## Suggested commit message

```text
feat(knowledge): distill workflow-vs-agent, MCP-as-integration, and subagent-cost patterns
```
