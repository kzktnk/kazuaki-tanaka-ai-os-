# Migration Report — Related-project radar + ET practice case pack (2026-08)

## Sources (not stored in repo)

Local files only (binaries not committed):

1. **Related-project / external coordination support template** (`.xlsx`, three sheets) — anonymized; extends Program Line U  
2. **Enterprise transformation case pack 2019** (`.pptx`, practice MM packaging) — structure only; new Program Line AA  
3. **Shared-operator program experience deck for ops community MM** (`.pptx`) — **method extraction skipped** (duplicate of Line U / cross-project / Archetype J / change); indexed under Line U as skip

Originals stay in the user’s Downloads. No binaries copied into git.

## Files created

- `knowledge/patterns/related-project-external-coordination-radar.md`
- `knowledge/patterns/transformation-practice-case-pack.md`
- `knowledge/migrations/related-project-radar-and-et-case-pack-2026-08.md`

## Files updated

- `knowledge/index/legacy-source-index.md` — Line U rows + Program Line AA; MM deck skip row  
- `knowledge/index/master-index.md` — pattern count, tree, Level 4 pointers  
- `CONTEXT_ROUTING.md` — Public Sector / Transformation PMO loads  
- `playbooks/public-multi-lot-construction-pmo.md` — Related pointer  
- `playbooks/cross-project-program-management.md` — Do-not-use / Related pointer (radar ≠ Dependency Register)

## Knowledge extracted

| Source | Disposition | Generalized as |
|--------|-------------|----------------|
| Related-project / external coordination xlsx | **Newly added** | Pattern: radar vs Dependency Register; two template classes; hypothesis → confirm → promote |
| Enterprise transformation case pack 2019 | **Newly added** (structure only) | Pattern: pack anatomy; Role × type matrix; theme card schema |
| Shared-operator OCS MM experience deck | **Skipped** (already covered) | Index only — multi-PJ chaos, cutover politics, living knowledge share already adjacent to existing assets |

## Excluded（未登録）

- シート実データ、スライド本文の事例ストーリー  
- 共同利用運用者名・案件名・ベンダー名・人名  
- 円、在庫・台数、系統図詳細、契約ID、提案／入札本文  
- MM デッキの用語集・固有エピソード・組織図  

## Suggested commit message

```text
feat(knowledge): add related-project radar and ET case-pack patterns
```
