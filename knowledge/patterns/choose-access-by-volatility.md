# Pattern: Choose Access by Volatility

**Status:** Active  
**Origin:** Generalized from RAG and Agentic Search study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **情報へのアクセス手段は、揮発性・権威・検索の複雑さで選ぶ。小さく安定なら managed context。大きく変わるなら Retrieval。現在の状態なら live source。探索が観察依存なら Agentic Search。**

接続の標準化は `knowledge/patterns/mcp-as-integration-not-authority.md`。経路の型は `knowledge/patterns/workflow-vs-agent-vs-human.md`。本パターンは **何をどの経路で取るか** である。

## Core distinction

```text
Stable knowledge          → Static / managed context
Frequently changing corpus → Retrieval / RAG
Real-time state           → Live tool / authoritative live source
Complex / iterative need  → Agentic Search (bounded)
```

| 例 | 経路 |
|---|---|
| 改定の少ない規程・手順 | Managed context |
| 日次の保全履歴・大量文書 | Retrieval / RAG |
| いまの設備状態・在庫・センサ | Live tool / API |
| 初期クエリでは足りない障害切り分け | Agentic Search |

RAG は Retrieve → Evidence を渡す → Grounded に生成、である。検索したことと正しいこと、新しいことは別である。

> **Freshness depends on the source, not on the fact that retrieval occurred.**
> **RAG does not guarantee correctness.**

現在の状態を静的スナップショットやコーパス検索で代用しない。小さく安定した参照を毎回 Retrieval しない。

## Retrieval vs generation

失敗を混ぜない。

```text
Bad answer
→ Needed evidence retrieved?
  ├─ No → Retrieval（relevance / recall / version / authority / chunk / metadata）
  └─ Yes
      → Faithful to evidence?
         ├─ No → Generation / grounding
         └─ Yes → Requirement / evaluation
```

Topical に近い Chunk と、問いに答える Evidence は別。Evidence 外の主張を足すと Grounded ではない。矛盾は版・権威・日付で解き、解けなければ不確実性を出して Escalate。最新が常に正本ではない。

表・KPI の切り方は `playbooks/rag-structure-diagnosis.md`。1件の語彙は `knowledge/lessons/ai-output-evaluation-terms.md`。

> **Topical similarity ≠ sufficient evidence.**
> **Evaluate retrieval quality separately from generation quality.**
> **No evidence → uncertainty, not invention.**

## Agentic Search

1回の確定クエリで足りるなら、Agentic Search にしない。情報要求が途中で変わる、複数経路を見る、クエリを作り直す、ときに使う。

停止条件を先に置く: 最大反復、証拠閾値、新規情報なし、timeout、不確実回答、Escalate。無制限探索は設計不良。

> **More autonomy is not automatically better retrieval.**
> **Bound search loops.**

## Signals

- RAG を使っているので最新だとする  
- 現在の状態を静的スナップショットや文書検索で答える  
- 小さく安定した文書を毎回 Retrieval する  
- 関連文書が当たったので Evidence 十分だとする  
- Evidence を渡せば Grounding される、とする  
- Agentic Search は通常 RAG より常に優れる、とする  
- 矛盾する Evidence をモデルに選ばせる  
- 検索ループに停止条件がない  

## Core rule

> Match the access path to volatility and authority. Retrieve changing corpora; read live state live. Diagnose retrieval before generation. Iterate search only when the information need itself is observational, and stop on purpose.

## Related

- `knowledge/patterns/mcp-as-integration-not-authority.md` — ライブ接続 ≠ 権限  
- `knowledge/patterns/workflow-vs-agent-vs-human.md` — 探索を無制限にしない  
- `knowledge/patterns/logical-vs-physical-document-unity.md` — 正本・版・メタデータ  
- `knowledge/patterns/tool-output-as-untrusted-data.md` — 取得結果は命令ではない  
- `knowledge/lessons/ai-output-evaluation-terms.md`  
- `playbooks/rag-structure-diagnosis.md`  
- `playbooks/ai-poc-quality-review.md`  
- `adapters/claude/CLAUDE.md`  
