# Pattern: Final Cut Hands Over Decision Themes

**Status:** Active  
**Origin:** Generalized from a final-report pack on a running multi-project program (2026-09). Client names, plant names, org units, filled issue rows, counts, and decks are **not** stored here.

## Pattern statement

> **最終報告の仕事は、抽出行を読み上げることでも、次フェーズの進め方を決めることでもない。全量は別紙。本編は「誰が何を決めれば複数行が同時に解消するか」の決定論点である。統合スケジュールの更新は案。次の巻き込み方式はオプションのまま渡す。事実が揃わない観点には、対応方針を書かない。**

中間報告の確認セットは `knowledge/patterns/interim-as-confirmation-set.md`。持ち主交代で継続を決めないのは `knowledge/patterns/stay-then-repropose-on-handover.md`。本パターンは **今契約の最終断面を、何として渡すか** である。

## Core distinction

| 作業紙・中間 | 最終の本編 |
|---|---|
| 全量抽出、From–To の行 | 別紙。本編では開かない |
| 今期 Critical / High の確認セット | それを決定論点へ畳む |
| 現行計画の上に課題を載せる | 更新案を出してよい。正式化はまだ |
| 巻き込み方式のオプションカード | 条件付き推奨は残してよい。選択は incoming |

絞り込みは3段で足りる。

```text
全量（間の5領域）
  → 今見ているプログラム能力／イネーブラーに関連するもの
    → 今期施策に効く Critical / High
      → 決定論点へグルーピング（1行が複数論点にまたがってよい。件数は延べ）
```

能力マップは **関連のフィルタ** である。課題の分類は Boundary / Dependency / Interface / Consistency / Schedule のまま（`knowledge/patterns/topology-map-vs-issue-log.md`）。ノード名で行を分類し始めない。

事実が揃わない観点は、対応方針を空にして残す。現行インターフェース仕様が未把握なら、Interface 行に方針を書かない。確認項目が開いている行に答えを先置きしない（`playbooks/cross-project-program-management.md` §8.8）。

横断の場は、既存の Control Cycle に決定論点を載せる書き方にする。「行ごとに WG」に読める文は、最終でも出さない。

次の策定ワークショップは、期間と成果水準のトレードオフをオプションとして渡す。条件付き推奨（スピードと実行性なら重点テーマだけ協働、など）は選択ではない。モデルサイトは施策ごとに候補を切り、データ可否・変革体制・展開性で評価する。サイト名は後（`knowledge/patterns/activation-first-for-site-led-work.md`）。部門レベルの期待関与はマップ。出席者名簿ではない。

## Signals

- 最終報告が、重要課題行のウォークになっている  
- 能力マップのノード名が、課題分類の代わりになっている  
- 仕様未把握の観点に、対応方針が書いてある  
- 最終本編で統合スケジュールを正式化している  
- ワークショップ方式やモデルサイト名を、outgoing の最終会で選ばせている  
- 「横断 WG を設置」が、行ごとの新設に読める  
- 条件付き推奨を、決定として扱っている  

## Core rule

> Hand over decision themes. Keep the log as appendix. Treat the schedule update as a proposal. Leave next-mode options as options. Do not write a response plan for a view whose facts are not yet in.

## Related

- `knowledge/patterns/interim-as-confirmation-set.md` — 中間は確認セット。最終はそれを論点へ畳む  
- `knowledge/patterns/stay-then-repropose-on-handover.md` — 選択は incoming  
- `knowledge/patterns/topology-map-vs-issue-log.md` — 5領域は分類。能力マップはフィルタ  
- `playbooks/cross-project-program-management.md` §8.8 — 対応方針のレビュー  
- `knowledge/patterns/activation-first-for-site-led-work.md` — 施策ごと基準。サイト名は後  
- `standards/consulting-review.md`  
- `core/author-voice.md`  
