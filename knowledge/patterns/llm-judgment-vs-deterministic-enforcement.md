# Pattern: LLM Judgment vs Deterministic Enforcement

**Status:** Active  
**Origin:** Generalized from Claude API access study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **LLM は判断・分類・構造化・Tool 候補に使う。認可・秘密・Schema 検証・承認・不可逆操作の執行は、Application / Backend / Policy に置く。モデル出力はそのまま実行命令ではない。**

能力と権限の切り分けは `knowledge/patterns/ai-capability-vs-authority.md`。接続と権限は `knowledge/patterns/mcp-as-integration-not-authority.md`。本パターンは **API / アプリ境界** の置き場所である。

## Core distinction

```text
Untrusted user input
       ↓
LLM (judgment / recommendation)
       ↓
Schema / business-rule validation
       ↓
Authorization (application)
       ↓
Approval if consequential
       ↓
Execution
```

| Concern | 置く場所 |
|---|---|
| 安定した振る舞い | System-level instruction |
| 今回の動的な依頼 | User message |
| Secret / credential | モデル文脈の外（secret manager / env / backend） |
| 出力契約 | Structured output + アプリ側 validation |
| Authorization | Application / policy。モデルではない |
| 人の承認 | Workflow / approval |
| Retry / timeout | Application / infrastructure。bounded |
| 監査 | Application / platform |

認証済みでも、高影響の実行可否をモデルに任せない。モデルは推奨する。アプリが許可する。Structured output でも validation は残す。高性能モデルでも、不可逆操作の承認は消えない。

Secret を user prompt / system prompt / `CLAUDE.md` に置かない。

失敗は前提：timeout、欠測、Rate limit、壊れた応答。無制限 Retry は設計不良。bounded retry → 安全停止 → Escalate（`knowledge/patterns/workflow-vs-agent-vs-human.md`）。

モデル選定は Task fit × Quality × Latency × Cost。ベンチマークより実ユースケース評価。

## Signals

- モデルが危険かを判断できるので Authorization をモデルに任せる  
- System prompt に credential を入れて安全だとする  
- Structured output なら validation 不要とする  
- 高性能モデルなら Human approval 不要とする  
- API 失敗を無限 Retry する  
- 未検証の自由文をそのまま下流実行する  

## Core rule

> LLM for judgment. Deterministic layers for enforcement. Secrets stay outside model context. Untrusted input must not become trusted action.

## Related

- `knowledge/patterns/ai-capability-vs-authority.md` — できること ≠ してよいこと  
- `knowledge/patterns/mcp-as-integration-not-authority.md` — 接続 ≠ 権限  
- `knowledge/patterns/workflow-vs-agent-vs-human.md` — bounded retry / HITL  
- `knowledge/patterns/define-success-before-prompt-change.md`  
- `frameworks/human-oversight.md`  
- `adapters/claude/CLAUDE.md`  
