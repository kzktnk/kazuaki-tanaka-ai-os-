# Pattern: MCP as Integration, Not Authority

**Status:** Active  
**Origin:** Generalized from MCP Part 1–2 and Tool Use study notes (2026-09). Exam items, scores, and credential materials are **not** stored here.

## Pattern statement

> **MCP は外部 Tools / Data への接続を標準化する層である。認証・認可・監査・検証の代替ではなく、Agent アーキテクチャそのものでもない。**

Standardized connection ≠ trusted connection. Connectivity does not imply authority.

```text
MCP            = how tools / data are exposed
Tool Use       = how the model selects and uses a tool
Application    = validation + authorization + enforcement
```

> **MCP connects. Claude decides. Application controls.**

## Core distinction

Prompt / Project Knowledge が向くもの:

- 比較的静的な参照
- 毎回ほぼ同じ情報
- 外部 Action が不要

MCP が向くもの:

- いまの状態（設備、在庫、センサ）
- 実行時の取得
- Tool execution / 業務システムとの Interaction

変化するコーパス（保全履歴、大量文書）は Retrieval / RAG。ライブ状態と混ぜない。経路の選び方は `knowledge/patterns/choose-access-by-volatility.md`。

```text
Static knowledge              → Context / Knowledge
Changing corpus               → Retrieval / RAG
Live or actionable capability → MCP
Iterative information need    → Agentic Search (bounded)
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

分析なのに DBA、読み取りなのに Write、検索なのに本番操作、は設計不良。公開する Tool を増やすほど blast radius（誤判断時の影響範囲）と Prompt Injection の到達範囲が広がる。使わせたくない Tool を公開したまま Prompt で「使うな」と書くのは制御ではない。非公開にする。

> **Give only the capability needed for the task. Narrow tool surface reduces blast radius.**
> **Broad permissions are not a reliability feature.**

現在の状態を月次 CSV・会話記憶・静的スナップショットから推測させない。ライブで取る。変化するコーパスは Retrieval。小さく安定した参照は managed context のままにする。

高影響 Action（設備停止等）は、状態取得 → 推奨 → 実行要否で Human approval、が先。接続できても自動実行してよいとは限らない。権限の段階は `knowledge/patterns/authority-levels.md`。

接続できるだけでは足りない。契約・権限・失敗処理・高影響の制御までが MCP 設計である。

## Tool / Resource / Prompt

同じ MCP でも役割が違う。混ぜない。

| 要素 | 役割 | 例 |
|---|---|---|
| **Tool** | Do something（外部 Action） | `create_ticket`、`restart_service` |
| **Resource** | Read something（参照データ / context） | 規程、顧客プロファイル、設備状態 |
| **Prompt** | 再利用可能な聞き方 / 対話の型 | インシデントレビューの章立て |

Prompt は Tool ではない。外部 Action を実行しない。モデルを fine-tune しない。System instruction を必ず上書きするものでもない。

既存 API があっても、MCP は AI 向けの共通 Interface として載ることがある。API を置き換える必要はない。

## Tool contract

名前・説明・Schema が曖昧だと、誤選択・誤実行が増える。`update_data` ではなく、何を・どの ID で・副作用は何か、まで契約にする。説明には、いつ使うか、何をするか、何をしないか、副作用、を書く。責任は1 Tool に1つ。

良い定義に含めるもの: 明確な名前、説明、必須パラメータと型、期待出力、副作用、エラー条件、権限境界。

似た名前の Tool を並べない（`update_customer` / `edit_customer` / `modify_customer`）。重なりを減らし、不要な Tool は公開しない。Tool 面が広いほど選択も曖昧になり、blast radius も広がる。万能 Tool にまとめるのも誤り。選択ミスの多くは Interface 設計の問題である。

> **Ambiguous tool contract → ambiguous model behavior. Warning text is not a security control.**
> **Tool-selection errors are often interface-design errors.**

「慎重に使え」と説明文に書くだけでは、高影響 Tool の制御にならない。Authorization、承認ゲート、権限境界、監査、Escalation を先に置く。

## Authentication vs Authorization

- **Authentication:** Who are you?（身元）  
- **Authorization:** What are you allowed to do?（操作範囲）  

認証済みでも全 Tool が使えるわけではない。同じ MCP Server でも、読み取りと破壊的操作は Control を変える。

失敗は前提にする。Timeout / 権限拒否 / 部分結果 / Rate limit は、構造化したエラーで返し、bounded retry → 代替 → 安全に止めて Escalate。無制限 Retry は設計不良（`knowledge/patterns/workflow-vs-agent-vs-human.md`）。

## Signals

- MCP があるので Authentication は不要  
- MCP を使えば API は不要  
- MCP は Agent 専用  
- Tool を増やすほど柔軟で良い  
- MCP 経由なら外部データは正しい  
- 静的参照を毎回 MCP で取りに行く / ライブデータを CLAUDE.md に貼る  
- 現在の状態を RAG やスナップショットで代用する  
- 変化するコーパスとライブ状態を同じ経路にする  
- Authentication 済みだから全 Tool 利用可  
- Tool 説明の警告文で高影響操作を制御する  
- MCP Prompt を Tool / 外部 Action と同一視する  
- 似た Tool を増やして柔軟だと考える  
- 広い権限の方が失敗が減る、と考える  
- 使わせない Tool を公開したまま Prompt で禁止する  
- Tool Use と MCP を同一視する  

## Core rule

> MCP standardizes access. It does not replace security, validation, or authority design. Changing corpora go through retrieval; current state is read live. Tool / Resource / Prompt are different contracts; authentication is not authorization; warning text is not a control. MCP connects; the model decides; the application controls.

## Related

- `knowledge/patterns/workflow-vs-agent-vs-human.md` — MCP は両方を支えうる  
- `knowledge/patterns/ai-capability-vs-authority.md` — できること ≠ してよいこと  
- `knowledge/patterns/llm-judgment-vs-deterministic-enforcement.md` — API / アプリ境界  
- `knowledge/patterns/choose-access-by-volatility.md` — 安定 / 変化 / ライブ / 探索  
- `knowledge/patterns/tool-output-as-untrusted-data.md` — 戻り値は命令ではない  
- `knowledge/patterns/logical-vs-physical-document-unity.md` — 静的コーパスの置き方  
- `frameworks/human-oversight.md`  
- `adapters/claude/CLAUDE.md` — Connector / MCP vs Project knowledge  
