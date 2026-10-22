# Pattern: Cutover Risk Families Then Four Controls

**Status:** Active  
**Origin:** Generalized from a generic large-IT migration risk/governance brief (2026-10). Client names, filled registers, and the source PDF are **not** stored here.

## Pattern statement

> **アプリケーション／データのカットオーバーは、運用 take-on とは別の仕事である。リスクを Technical / Data / Integration / Operational / Business に分けて先に取る。「移行リスク」1行にまとめない。緩和は Pilot・Rollback・Parallel・Test の組み合わせであり、四つを貼る仕事ではない。ガバナンスは既存の SteerComm / PMO / Architecture / Delivery に載せる。第二の移行事務局を作らない。登録はライフサイクルを通して更新する。**

運用への引き継ぎ・take-on は `playbooks/operations-transition-playbook.md` と `frameworks/service-transition-approach.md`。仕事の切り分けは `knowledge/patterns/transition-vs-transformation-vs-realization.md`。本パターンは **システムを移すプログラム側の、リスクの切り方と制御の選び方** である。

## Core distinction

| カットオーバー（このパターン） | 運用 take-on（③） |
|---|---|
| アプリ・データ・基盤を移す | 走る組織・KT・責任日を移す |
| 互換、欠損、IF、停止、業務影響 | 属人化、ドキュメント、Wave、SRD |
| 既存サポート組織への導入に近い | 新しい運用能力の立ち上げ |

リスクは先に家族で取る。

| 家族 | 見るもの |
|---|---|
| Technical | 互換、対象の作り |
| Data | 欠損、改変、復元 |
| Integration | API・接続の切れ |
| Operational | 移行中のサービス停止 |
| Business | 重要業務への波及 |

緩和は構成選択である。一度きり／段階の判断は `knowledge/patterns/all-at-once-vs-stepwise-change.md`。技術側のレバーは次の四つ。

| 制御 | 向くとき |
|---|---|
| Pilot | 全体の前に、小さい対象で壊し方を見る |
| Rollback | 失敗したら戻せる条件が先にある |
| Parallel | 新旧を時限で併走させる。常設にしない |
| Test | 機能・性能・結合。どれを合格条件にするかを先に書く |

四つ全部をスライドに並べて「対策済み」としない。選ばなかった制御は、なぜ不要かを残す。

ガバナンスは既存スタックで足りる。SteerComm が決める。PMO が登録と報告を回す。Architecture が設計を妥当性確認する。Delivery が実行する。移行専用の第二 PMO を横に置かない（`playbooks/program-governance-cadence.md`）。

登録の列は Impact / Probability / Mitigation で足りることが多い。作って終わりにしない。週次の進捗、リスク／課題、経営レビュー、マイルストンは、既存のケイデンスに載せる。

## Signals

- アプリ／データの移動に、運用 Transition Playbook をそのまま当てている  
- RAID に「移行リスク」が1行しかない  
- Pilot・Rollback・Parallel・Test を全部貼って対策済みとしている  
- プログラム事務局の横に Migration PMO を新設している  
- キックオフで登録を作り、その後更新していない  
- take-on（人・KT）とカットオーバー（データ移動）を一つの計画・一つの予算にしている  

## Core rule

> Name the cutover job. Split risk into five families. Choose among the four controls. Use the existing governance stack. Keep the register live.

## Related

- `knowledge/patterns/transition-vs-transformation-vs-realization.md` — 導入／take-on／変革  
- `knowledge/patterns/all-at-once-vs-stepwise-change.md` — 一度きりか段階か  
- `frameworks/service-transition-approach.md` — 同じ四制御を take-on 側で使う  
- `frameworks/delivery-leadership.md` — Service introduction  
- `playbooks/operations-transition-playbook.md` — 運用移行。カットオーバーの代用にしない  
- `playbooks/program-governance-cadence.md`  
- `playbooks/cross-project-program-management.md` — RAID  
- `frameworks/systems-integration-solution-planning.md`  
