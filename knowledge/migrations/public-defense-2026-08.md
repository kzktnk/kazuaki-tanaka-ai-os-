# Migration Report — Public Sector & Defense IT (2026-08)

## Source (not stored in repo)

Local folders and files under Downloads (ministry OA procurement support, defense-adjacent programs, estimate scrutiny, construction PMO, concept work, seller RMF proposal / internal review, public notice PDF).

**Originals not archived.** No yen, inventories, network designs, vendor files, or current proposal body.

## Files created

- `domains/public-defense.md`
- `frameworks/public-it-procurement-support.md`
- `knowledge/patterns/buyer-vs-seller-in-public-procurement.md`
- `knowledge/migrations/public-defense-2026-08.md`

## Files updated

- `domains/README.md`
- `frameworks/readme.md`
- `frameworks/program-phases-investigation-to-requirements.md`
- `standards/vendor-proposal-evaluation.md`
- `knowledge/index/legacy-source-index.md` Program Line P
- `knowledge/index/master-index.md`
- `CONTEXT_ROUTING.md`

## Excluded

- 仕様・適合条件・機器一覧・見積実数・DPM  
- 社名付き精査コメント、契約、NDA、立入・名簿  
- 現行RMF提案の体制図、対象件数、予算・入札想定、社内レビュー金額  
- 個人名、機会ID  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Public vs commercial IT | Accounting, 総合評価, fairness, 保全, standard guidelines |
| Buyer lifecycle | 方式 → 仕様/適合 → 評価基準 → 見積精査 → 構築PMO |
| Estimate scrutiny | Baseline first, then hearing, then report |
| Seller public bid | Evaluation-item mapping; split lots; officials keep risk decisions |
| Role split | Buyer vs seller pattern |

## Suggested commit message

```text
feat(knowledge): add public-defense domain and buyer-side procurement support
```
