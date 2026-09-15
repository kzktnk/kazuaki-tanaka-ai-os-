# Migration Report — Interim as confirmation set (2026-09)

## Source (not stored in repo)

Local interim-report pack on a running multi-project asset-management program (2026-09-14 pre-read / 2026-09-15 confirmation): two deck versions and two meeting recordings.

Client names, plant names, org unit identifiers, filled From–To rows, people, and recordings are **not** archived. No transcript was provided; oral remarks were not harvested. The reusable signal is the job change from working extraction pack to confirmation set.

Between-PJ extraction views were already ingested (`pj-between-review-viewpoints-2026-09.md`). Site-led activation was already ingested (`site-led-activation-first-2026-09.md`).

## Files created

- `knowledge/patterns/interim-as-confirmation-set.md`
- `knowledge/migrations/interim-as-confirmation-set-2026-09.md`

## Files updated

- `standards/consulting-review.md` — v0.11
- `standards/deliverable-archetypes.md` — v1.5
- `core/author-voice.md`
- `knowledge/patterns/topology-map-vs-issue-log.md`
- `knowledge/patterns/formulation-comms-vs-adoption-comms.md`
- `knowledge/patterns/activation-first-for-site-led-work.md`
- `domains/energy-utilities.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`
- `knowledge/index/legacy-source-index.md`

## Excluded

- 社名、発電所名、部課名、製品・プログラム略号を識別子として使う記述
- 記入済み From–To、課題本文、統合スケジュール実体
- 個人名、ステークホルダー実名表
- 録音（mp4）。議事録なし

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| 中間報告の仕事 | 作業紙の全件提示ではない。前提固定 → 今期 Critical/High の確認セット → 方向性と次アクション |
| 課題の絞り | 目標×マイルストンに加え、今期施策影響で今日の確認対象を切る |
| スケジュール | 現行整理 → 課題載せ → 更新案。中間では③を先に出さない |
| 巻き込み vs 期限 | 黙って削らない。短期トップダウン / ハイブリッド / 現場協働をオプション化 |

## Suggested commit message

```text
feat(knowledge): treat interim reports as a confirmation set, not the working extraction
```
