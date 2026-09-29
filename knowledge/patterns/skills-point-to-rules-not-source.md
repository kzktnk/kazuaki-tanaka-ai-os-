# Pattern: Skills Point to Rules, Rules Extract from Knowledge

**Status:** Active  
**Origin:** Generalized from an internal harness-engineering briefing for strategy consulting (2026-09). Client names, product pitches, hour counts, and filled examples are **not** stored here.

## Pattern statement

> **入口（Skill）は手順を持たない。手順（Rule）は原典（Knowledge）から抽出する。チャットのプロジェクト設定に暗黙知を置くと漏れる。人が組むのは足場、人がやるのは成果物を見極めて次へ進める判断である。全部をおぼえてから始めない。**

層の仕事は `knowledge/patterns/match-capability-to-context-job.md`。Subagent は便益がコストを上回るときだけ `knowledge/patterns/subagent-when-isolation-justifies-cost.md`。本パターンは **足場の三層と、人が残す点** である。

## Core distinction

```text
Skill      → いつ発動するか。どの Rule を読むか。短い。毎回読まれる
Rule       → この仕事の手順。実践知はここに足す
Knowledge  → 手順の原典（教材・型）。毎回読ませない
```

Skill 本文に制約や長い手順を書くと、発動のたびに全体が載り、複数 Skill で重複し、更新が漏れる。Rule が無いと Skill が原典を直読みし、重くて回らない。

チャット画面だけのプロジェクト設定は、足場を読み込めないことが多い。同じフォルダを、足場が動く実行環境で開く。

このリポジトリへの写像（名前の暗記ではない）:

| 三層 | ここに置く |
|---|---|
| 入口 | `CONTEXT_ROUTING.md`（いつ何を読むか） |
| 手順 | `playbooks/`、`standards/` |
| 原典 | `frameworks/`、`knowledge/patterns/`、`lessons/` |
| 検査 | レビュー標準、hooks に相当する確認 |
| 分業 | isolation の便益があるときだけ Subagent |

案件ごとに変わる指示と、どの案件でも同じ規律は分ける。混ぜると漏れる。

## Four walls (why a harness)

| 壁 | 症状 |
|---|---|
| Skill Gap | プロンプト次第で成果が変わる。上手い人の型が個人に閉じる |
| Token Cost | 考えずに会話を続ける。速い感覚と進んだ量がずれる |
| Human Bottleneck | 生産量が増えるほどレビューが詰まる。人が入る点を先に決める |
| Governance & Trust | 何を正解とするか、誰が責任を持つか、どう監査するか |

対話で実行 → 仕組みで実行 → 自動で実行、の順。今日の仕事がどの段かを先に名指す。

人が残すもの:

- 現状と目的（丸投げ禁止）  
- 足場を組むこと  
- 出てきた成果物を見極め、次へ進める判断  

調査では、支持する事実と支持しない事実の両方を取る。平均点や賛成材料だけでは仮説を固めない。

始め方: 入口・手順・原典の3箱。並列化・MCP・検証ループは余力ができてから。最初の入口の実体は `.cursor/skills/issue-structuring/SKILL.md`（手順は `standards/strategy-engagement-guide.md`）。人が残す3点は `knowledge/patterns/issue-structuring-reserves-three-judgments.md`。

## Signals

- 手順と制約を Skill 本文に全部書いている  
- チャットのプロジェクト設定だけに暗黙知がある  
- 全部の部品をおぼえてからでないと始められない、としている  
- AI の生産量に合わせて、人が入る点を後から足している  
- 調査が賛成材料だけを集めている  
- 速い対話が、前に進んだ量だと勘違いされている  

## Core rule

> Skills trigger. Rules prescribe. Knowledge is the master. Humans build the harness and judge the output. Do not load the source on every trigger. Do not start from the full toolkit.

## Related

- `knowledge/patterns/match-capability-to-context-job.md` — 層の選び方  
- `knowledge/patterns/subagent-when-isolation-justifies-cost.md` — 並列は後  
- `knowledge/patterns/explicit-before-elaborate-prompt.md`  
- `knowledge/patterns/workflow-vs-agent-vs-human.md`  
- `core/ai-collaboration.md` — 人は判断を残す  
- `adapters/claude/CLAUDE.md`  
- `CONTEXT_ROUTING.md`  
- `knowledge/patterns/issue-structuring-reserves-three-judgments.md` — 論点整理で人が残す3点  
- `.cursor/skills/issue-structuring/SKILL.md` — 最初の入口の実体  
