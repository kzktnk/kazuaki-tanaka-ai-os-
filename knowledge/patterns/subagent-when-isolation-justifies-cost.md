# Pattern: Subagent When Isolation Justifies Cost

**Status:** Active  
**Origin:** Generalized from subagent study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **複雑だから分けるのではない。Specialization・Context isolation・権限の分離・独立並列の便益が、orchestration のコストを上回るときに Subagent を使う。**

More agents ≠ better architecture.

## Core distinction

Main agent は分解・委任・統合・最終判断 / Escalation を持つ。Subagent は専門タスク・隔離された context・最小 Tool・構造化した結果返却に集中する。

使う理由（どれか明確であること）:

| 理由 | 何が得か |
|---|---|
| **Specialization** | 専用 instructions / 専門領域 |
| **Context isolation** | Main の context を汚さない。budget と競合を抑える |
| **Distinct tool permissions** | 役割ごとに最小権限。Research は search、Reviewer は read-only |
| **Parallelism** | 依存が弱く、後で統合できる作業 |

使わない方がよい:

- 単純な 1 タスク  
- 同一 context / tools / instructions で足りる  
- 強い順序依存、同じ state の同時更新  
- coordination / latency / 失敗処理のコストが高いだけ  

## Return shape

結論だけ（「問題なし」）は不足。Main が統合できる形で返す。

```text
Findings:
Evidence:
Uncertainty:
Risks:
Recommended next step:
```

> **Return evidence, not just conclusions.**

並列は、タスクが十分独立しているときに限る。B が A の結果に強く依存するなら直列のまま。

各 Subagent に与える Tool は仕事に必要な最小。Log 分析に production deploy 権限は権限過多。Agent 全体の blast radius は `knowledge/patterns/workflow-vs-agent-vs-human.md`。

## Signals

- 工程が 5 つあるから 5 Agents  
- 精度が上がるはずだから Subagent  
- 並列化できるから分ける（依存を見ていない）  
- Role 名が違うだけで分ける（context / tool / workflow の便益を見ていない）  
- Subagent が結論だけ返し、根拠と不確実性がない  

## Core rule

> Complexity alone does not justify a subagent. Specialize, isolate context, or split permissions only when the benefit pays for orchestration cost.

## Related

- `knowledge/patterns/workflow-vs-agent-vs-human.md` — 先に Workflow vs Agent を決める  
- `knowledge/patterns/mcp-as-integration-not-authority.md` — Tool 面は最小権限  
- `adapters/claude/CLAUDE.md`  
