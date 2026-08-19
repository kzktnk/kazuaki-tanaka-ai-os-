# Migration Report — Local-government shared IT operator PMO (2026-08)

## Source (not stored in repo)

Local 2022 pack: public notice for process-management support, seller proposal decks, then buyer-side construction PMO artefacts (quality gates, start-of-stage reviews, ops-document merge, environment rules, executive briefings).

Indexed anonymously as **local-government shared IT operator / 2022**. Originals not archived.

## Files created

- `knowledge/patterns/shared-operator-vs-ministry-vs-municipality.md`
- `playbooks/public-multi-lot-construction-pmo.md`
- `knowledge/migrations/local-gov-shared-it-2026-08.md`

## Files updated

- `domains/public-defense.md`（共同利用の第三アクター。新 Domain ファイルは作らない）
- `frameworks/public-it-procurement-support.md` §Construction-phase PMO
- `knowledge/index/legacy-source-index.md` Program Line U
- `knowledge/index/master-index.md`
- `CONTEXT_ROUTING.md`
- `domains/README.md`, `playbooks/README.md`, `playbooks/pmo-function-standup.md`

## Excluded（未登録）

- 公示の仕様・総合評価実項目・契約案・入札書様式  
- 提案本文（表紙・目次含む評価対応）  
- 系統・統合構成、設計書、試験結果、手順・操作書本文  
- 名簿、要員計画、円、機器数、個人名、契約ID  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Operator ≠ ministry ≠ municipality | Pattern: three actors; one acceptance story |
| Congested multi-lot tests / cutover | Playbook: plan-then-result gates, start-of-stage, ops-doc merge |
| PMO vendor vs SI lots | Seller of advisory, buyer-side toward build lots |

## Suggested commit message

```text
feat(knowledge): add shared local-gov IT operator PMO judgment
```
