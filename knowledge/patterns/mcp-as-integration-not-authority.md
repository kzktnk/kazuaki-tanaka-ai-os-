# Pattern: MCP as Integration, Not Authority

**Status:** Active  
**Origin:** Generalized from MCP Part 1 study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **MCP は外部 Tools / Data への接続を標準化する層である。認証・認可・監査・検証の代替ではなく、Agent アーキテクチャそのものでもない。**

Standardized connection ≠ trusted connection. Connectivity does not imply authority.

## Core distinction

Prompt / Project Knowledge が向くもの:

- 比較的静的な参照
- 毎回ほぼ同じ情報
- 外部 Action が不要

MCP が向くもの:

- 頻繁に変わる外部データ（在庫、Ticket、設備状態）
- 実行時の取得
- Tool execution / 業務システムとの Interaction

```text
Static knowledge → Context / Knowledge
Live or actionable capability → MCP
```

MCP は Context Window を増やす仕組みではない。裏側で API を使うこともあり、API を不要にはしない。Agent 専用でもない。

| 使い方 | 流れ |
|---|---|
| **Agentic** | Agent が Tool を選び、結果を見て次を決める |
| **Deterministic** | Workflow が固定の MCP call をする |

MCP = integration layer. Agent = decision / orchestration pattern. 混ぜない。

## What MCP does not replace

- Authentication / Authorization  
- Least privilege / Access control  
- Audit logging  
- Input / output validation  
- Secrets management  
- Human approval（高影響操作）  

分析なのに DBA、読み取りなのに Write、検索なのに本番操作、は設計不良。公開する Tool を増やすほど blast radius（誤判断時の影響範囲）と Prompt Injection の到達範囲が広がる。

> **Give only the capability needed for the task. Narrow tool surface reduces blast radius.**

頻繁に変わるデータを月次 CSV や会話記憶から推測させない。実行時に取る。

高影響 Action（設備停止等）は、状態取得 → 推奨 → 実行要否で Human approval、が先。接続できても自動実行してよいとは限らない。権限の段階は `knowledge/patterns/authority-levels.md`。

## Signals

- MCP があるので Authentication は不要  
- MCP を使えば API は不要  
- MCP は Agent 専用  
- Tool を増やすほど柔軟で良い  
- MCP 経由なら外部データは正しい  
- 静的参照を毎回 MCP で取りに行く / ライブデータを CLAUDE.md に貼る  

## Core rule

> MCP standardizes access. It does not replace security, validation, or authority design. Retrieve frequently changing data at runtime.

## Related

- `knowledge/patterns/workflow-vs-agent-vs-human.md` — MCP は両方を支えうる  
- `knowledge/patterns/ai-capability-vs-authority.md` — できること ≠ してよいこと  
- `knowledge/patterns/logical-vs-physical-document-unity.md` — 静的コーパスの置き方  
- `frameworks/human-oversight.md`  
- `adapters/claude/CLAUDE.md` — Connector / MCP vs Project knowledge  
