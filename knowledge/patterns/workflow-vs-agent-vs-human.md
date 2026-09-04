# Pattern: Workflow vs Agent vs Human

**Status:** Active  
**Origin:** Generalized from Agentic AI study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **経路が既知なら Workflow。目標は明確だが経路が観察依存なら Agent。結果が重いなら Human。ステップ数だけでは Agent にしない。**

Agent の設計は自律性の最大化ではない。権限・停止条件・Retry 上限・検証・承認をセットにした **bounded autonomy** である。

## Core distinction

| 型 | いつ使う | 特徴 |
|---|---|---|
| **Workflow** | 手順・分岐が事前に書ける | 再現・監査しやすい。不要な探索を避ける |
| **Agent** | Goal は明確だが、観察結果で次の行動が変わる | Observe → Plan → Act → Observe。Plan を最後まで固定しない |
| **Human** | 不可逆・高影響・不確実な例外 | 承認・Escalation。Agent 自身に要否を決めさせない |

現実は Hybrid が多い。

```text
Routine → Workflow
Dynamic exception → Agent
Consequential decision → Human / stronger controls
```

## Bounded autonomy (Agent を入れるとき)

Planning は正しさを保証しない。次を一緒に設計する。

- **Tools:** その仕事に必要なものだけ。Tool 利用可否と権限範囲は別
- **Stop:** Goal 達成 / 最大反復 / 同一失敗の反復 / 情報不足 / 高リスク / 承認待ち
- **Retry:** 上限 → 代替があれば試す → なければ Stop / Escalate。無制限 Retry は設計不良
- **HITL:** 低リスク・可逆は自動化してよい。高リスク・不可逆は事前の閾値で承認。全件レビューは必須ではない

自律レベルの目安:

```text
Risk + Reversibility + Blast radius + Permission scope + Verification
        ↓
Appropriate autonomy
```

権限の段階は `knowledge/patterns/authority-levels.md`。接続できることと実行してよいことは `knowledge/patterns/mcp-as-integration-not-authority.md`。

## Signals

- 複数ステップだから Agent、複数工程だから Multi-agent  
- Plan があるので Verification は不要  
- 使うかもしれないから全 Tool を渡す  
- 同じ失敗 Tool を止めずに繰り返す  
- 高額返金・本番操作の要否を Agent 自身が決める  
- 例外も含めて全部 Agent にする  

## Core rule

> Known path → Workflow. Unknown path, clear goal → Agent. Higher autonomy → stronger controls. Observation changes the next action.

## Related

- `knowledge/patterns/subagent-when-isolation-justifies-cost.md` — 分ける理由は複雑さではない  
- `knowledge/patterns/mcp-as-integration-not-authority.md` — MCP ≠ Agent  
- `knowledge/patterns/authority-levels.md` — 権限は段階  
- `knowledge/patterns/ai-capability-vs-authority.md` — 能力 ≠ 権限  
- `frameworks/human-oversight.md` — 監督は説明責任のため  
- `frameworks/decision-ownership.md`  
- `adapters/claude/CLAUDE.md`  
