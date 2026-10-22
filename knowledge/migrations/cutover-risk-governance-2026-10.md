# Migration Report — Cutover risk families then four controls (2026-10)

## Source (not stored in repo)

Local generic brief on risk management and governance for large IT migration programs (2026-10). Client names, filled registers, hour counts, and the PDF are **not** archived.

Operations take-on, introduction vs transition, stepwise change, RAID, and program cadence were already ingested. The brief restates those offices; it does not replace them.

## Files created

- `knowledge/patterns/cutover-risk-families-then-four-controls.md`
- `knowledge/migrations/cutover-risk-governance-2026-10.md`

## Files updated

- `knowledge/patterns/transition-vs-transformation-vs-realization.md`
- `knowledge/patterns/all-at-once-vs-stepwise-change.md`
- `frameworks/service-transition-approach.md`
- `frameworks/delivery-leadership.md`
- `playbooks/operations-transition-playbook.md`
- `playbooks/operations-transition-playbook-selfstudy.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`
- `knowledge/index/legacy-source-index.md`

## Excluded

- 原本 PDF
- サンプル登録の点数・行本文
- 役職カタログの再掲（既存ケイデンスで足りる）

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| 仕事 | アプリ／データ移動 ≠ 運用 take-on |
| リスク | Technical / Data / Integration / Operational / Business。1行にまとめない |
| 緩和 | Pilot / Rollback / Parallel / Test は構成選択 |
| ガバナンス | 既存の SteerComm / PMO / Architecture / Delivery。第二事務局を作らない |
| 登録 | Impact × Probability × Mitigation。ライフサイクルを通して更新 |

## Suggested commit message

```text
feat(knowledge): split cutover risk into families and choose four controls; do not stand up a second PMO
```
