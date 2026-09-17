# Pattern: Match Capability to Context Job

**Status:** Active  
**Origin:** Generalized from Claude product-features study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **能力は、文脈や操作の仕事に合わせて選ぶ。安定して再利用するものは永続コンテキスト。大きく変わる知識は Retrieval。いまの状態と外部操作は Tool。機械が読む出力は Structured。秘密・認可・硬い執行はモデルの外。永続に置けることと、置いてよいことは別である。**

揮発性による経路は `knowledge/patterns/choose-access-by-volatility.md`。判断と執行の境界は `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md`。本パターンは **どの層に何を置くか** である。

## Core distinction

```text
Stable reusable instructions / knowledge  → Persistent project context
Large or changing knowledge               → Retrieval / RAG
Live or external systems                  → Tools / MCP
Machine-consumable response               → Structured output (then validate)
Secrets / authorization / enforcement     → Outside the model
```

| 層 | 仕事 | ではない |
|---|---|---|
| Persistent project context | 毎回同じ約束・再利用知・チームの型 | 秘密、いまの運用状態、認可ロジック |
| Retrieval | 大きく、または頻繁に変わるコーパス | 小さく安定した文書を毎回検索する |
| Tools | 現在値の取得と、承認済みの外部操作 | 使えること＝実行してよいこと |
| Structured output | 下流コードが読む契約 | 構造化したので信頼済み |
| Application / policy | 検証・認可・承認・監査 | Prompt の禁止文で強制する |

同じ長い参照を毎回全文投入しない。永続知識か Retrieval かを、関連性・鮮度・版・権威で選ぶ。大量ファイルを全部コンテキストに入れない。今の仕事に必要な分だけ。

```text
Relevant context > maximum context
```

チームで同じ品質を出したいなら、安定した指示・例・共有知識を中央に置く。個人のプロンプトの上手さに頼らない。

> **Projects remember. RAG retrieves. Tools act. Structured output talks to machines. Applications control.**
> **Persistent ≠ trusted. Structured ≠ validated. Tool access ≠ permission.**

## Signals

- 永続コンテキストがあるので、何を置いてもよいとしている  
- プロジェクト知識があるので Retrieval は不要だとしている  
- Structured output なら validation は不要だとしている  
- Tool が使えるので認可も済んでいるとしている  
- 永続指示で硬い業務ルールを強制できるとしている  
- コンテキスト窓が大きいほど全部入れるべきだとしている  
- 同じ品質を、各人のプロンプトの癖に任せている  

## Core rule

> Match the layer to the job of the context. Persist only what is stable and reusable. Keep secrets, authorization, and hard enforcement outside the model. Centralize repeatable team behavior.

## Related

- `knowledge/patterns/choose-access-by-volatility.md` — 安定 / 変化するコーパス / ライブ / Agentic Search  
- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md` — 判断はモデル、執行はアプリ  
- `knowledge/patterns/mcp-as-integration-not-authority.md`  
- `knowledge/patterns/tool-output-as-untrusted-data.md`  
- `knowledge/patterns/logical-vs-physical-document-unity.md` — 版・権威・AI利用区分  
- `adapters/claude/CLAUDE.md` — Claude の Project / Connector 名への写像  
