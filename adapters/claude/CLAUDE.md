# Kazuaki Tanaka AI OS

# Claude Adapter

**Version:** v1.1  
**Status:** Active  
**Applies to:** Claude (Projects, Artifacts, Skills, Claude Code, connectors)  
**Document role:** Tool-specific operating card. Does not replace `AI_OPERATING_MANUAL.md`, `CONTEXT_ROUTING.md`, or files under `core/`, `standards/`, `frameworks/`, or `knowledge/`.

---

## Purpose

Claude 固有の機能を、仕事の種類に合わせて選ぶ。機能名の暗記ではなく、**何を知っているか / どう振る舞うか / どう進めるか / 何を作るか / 何に繋ぐか**を分ける。

評価語（Accuracy / Completeness / Groundedness 等）は `knowledge/lessons/ai-output-evaluation-terms.md`。ガバナンス・監督は `frameworks/`。

---

## Feature differentiation

| キーワード | まず考えるもの | 意味 |
|---|---|---|
| ongoing work / related chats | Project | 継続業務をまとめる |
| reusable reference documents | Project knowledge | Claude が参照する背景知識 |
| persistent behavior / rules | Project instructions | Project 内での継続的な振る舞い |
| substantial standalone content | Artifact | 会話と並行して作成・反復する成果物 |
| repeatable workflow / expertise | Skill | 再利用可能な手順・専門ワークフロー |
| external tools / data | Connector / MCP | 外部システム・データとの接続 |
| model capabilities / safety | System Card | モデル特性・評価・安全情報 |
| agentic coding | Claude Code | コードベースに対するエージェント型作業 |
| codebase guidance | CLAUDE.md | Claude Code 向けの永続ガイダンス |
| inspect before changing | Plan mode | 変更前に分析・計画を提示 |

覚え方:

- Knowledge = What Claude knows
- Instructions = How Claude behaves
- Skill = How Claude works
- Artifact = What Claude creates
- Connector / MCP = What Claude connects to

このリポジトリでは、モデル非依存の判断は AI OS 側に置く。Claude の Project knowledge に案件原本を複製して第二の source-of-truth を作らない。

正の remote は `https://github.com/kzktnk/kazuaki-tanaka-ai-os-`（末尾ハイフンあり）。ハイフンなしの `kazuaki-tanaka-ai-os` は最初のコミットで止まったスナップショット。ファイルが見つからないと結論する前に、URL を1文字単位で確認する。③は `playbooks/operations-transition-playbook.md`。

---

## Knowledge vs MCP vs Agent vs Subagent

機能名ではなく、仕事の型で選ぶ。判断の本体は patterns。

| 仕事 | こちら | ではない |
|---|---|---|
| 毎回ほぼ同じ静的参照 | Project knowledge / この adapter | ライブデータを CLAUDE.md に貼る |
| 頻繁に変わる外部データ / 外部 Action | Connector / MCP | MCP があれば認証不要、という読み |
| 手順が事前に書ける | Workflow（Skill / 固定手順） | ステップ数が多いから Agent |
| Goal は明確、次の一手が観察依存 | Agent（Claude Code 等） | Plan があるから検証不要 |
| 専門・context 隔離・権限分離の便益が orchestration を上回る | Subagent | 工程数や複雑さだけで分割 |

MCP は接続レイヤであり、Agent でも Security でもない。権限・停止・Retry・HITL は `knowledge/patterns/workflow-vs-agent-vs-human.md`。接続 ≠ 権限は `knowledge/patterns/mcp-as-integration-not-authority.md`。分ける条件は `knowledge/patterns/subagent-when-isolation-justifies-cost.md`。

---

## Diagnosis order

出力が弱いとき、いきなりモデルを変えない。

1. Task が曖昧？ → purpose / outcome を明確化
2. Output が曖昧？ → format / structure / length
3. 判断が不安定？ → criteria / rubric / examples
4. 複雑すぎる？ → decomposition
5. Context 不足？ → relevant authoritative context
6. Knowledge conflict？ → source-of-truth を curate
7. 能力不足？ → 評価してから model 変更

原則: **Knowledge 問題を Prompt で誤魔化ししない。**

衝突・陳腐化した参照は、指示を足す前に整理する。文脈は多いほど良い、ではない。

---

## Model selection

**Task fit × Quality × Cost × Latency**

- 高性能モデルが常に正解ではない
- 実ユースケースの evaluation が general benchmark より重要
- 必要品質を満たすなら、より高速・低コストのモデルが合理的
- safety-critical / 複雑な推論では、capability 差が material かを見る

---

## Task-type switch (short)

タスク種類を混ぜない。Research / Planning / Brainstorming / Drafting / Process optimization は別物。

| 種類 | 先に固定するもの |
|---|---|
| Analysis | decision objective, criteria / rubric, evidence → implication |
| Research | question / scope / sources; 事実と推論を分離 |
| Drafting | audience / purpose / tone / length / structure |
| Brainstorming | 発散と収束を分ける。最初から1案に絞らせない |
| Planning | goal / constraints / dependencies / owner / risk。assumption 確認を先に |
| Process optimization | 現行プロセス・例外・decision rights を先に。自動化対象と人の責任を分離 |

詳細な評価分類は `knowledge/lessons/ai-output-evaluation-terms.md`。

---

## Workflow

良い Claude workflow は次を明示する。

- Claude が担当する仕事
- Human が担当する仕事
- source / context
- evaluation criteria
- escalation
- fail-safe / fail-closed
- logs / traceability
- review / feedback

既存業務に矛盾・例外・責任不明がある場合、先に業務を整理してから自動化する。

---

## Related

- `AI_OPERATING_MANUAL.md`
- `CONTEXT_ROUTING.md`
- `core/ai-collaboration.md`
- `knowledge/lessons/ai-output-evaluation-terms.md`
- `knowledge/patterns/logical-vs-physical-document-unity.md`（参照コーパスの置き場所議論）
- `playbooks/ai-poc-quality-review.md`
- `frameworks/human-oversight.md`
- `knowledge/patterns/workflow-vs-agent-vs-human.md`
- `knowledge/patterns/mcp-as-integration-not-authority.md`
- `knowledge/patterns/subagent-when-isolation-justifies-cost.md`
