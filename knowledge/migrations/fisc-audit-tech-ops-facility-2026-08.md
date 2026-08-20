# Migration Report — FIS audit + tech/ops/facility criteria (2026-08)

## Source

Local `Downloads/` (not committed):

| Path | Role |
|------|------|
| Industry system-audit guideline workbook (`.xls`, revised edition) | Assurance structure |
| `技術基準_v1.doc` / `運用基準_v1.doc` / `設備基準_v1.doc` | Three-criteria layering |
| Folders: ドキュメント標準, 運用設計/引継, 開発環境／試験環境, 開発規約, 開発管理ガイドライン | Alias of Program Line H pack |

Anonymous label: **financial-institution IT standards / legacy development standards pack**.

## Confidentiality / exclusions

- Bank / institution names  
- Verbatim proprietary checklist rows (risk / control / checkpoint text)  
- Yen amounts, personal names, client IDs  
- Z0C form bodies already marked 未登録 in Line H  
- Facility / ops / tech **item body** text (thresholds, room specs, procedure prose)

## Already covered (no re-extract)

Program Line H → existing standards (`development-standards-framework`, document / development-management, environment, operations-design, operations-handover, release-management). Downloads-root guideline folders treated as the same pack.

## Files created

- `knowledge/patterns/fis-system-audit-as-assurance.md`
- `knowledge/migrations/fisc-audit-tech-ops-facility-2026-08.md`

## Files updated

- `standards/development-standards-framework.md` (v1.1 — §三基準レイヤ)
- `knowledge/index/legacy-source-index.md` (v1.17 — Line H alias note + Program Line X)
- `knowledge/index/master-index.md`
- `CONTEXT_ROUTING.md` (Development Standards / Build Phase)

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Audit workbook meta-structure | Theme → risk → control → checkpoint; buyer/assurance stance |
| Mapping to build/run | Project to tech / ops / facility / Line H standards — do not paste rows |
| Tech / ops / facility criteria | Orthogonal layer to guideline vs 規約; major classes only |
| Finance domain encyclopedia | **Not created** (`public-defense` remains unrelated) |

## Intentionally 未登録

- Full industry audit checkpoint sheet (~1000 rows)  
- 小項目 / リスク / コントロール / チェックポイント本文  
- 三基準の項番・【概要】本文・閾値  
- 開発規約 第1–2, 4–9 編のクライアント固有ID・パッケージ技法（Line H どおり）  
- PS/SAP 開発手順編、実様式 xls/doc  

## Suggested commit message

```text
feat(knowledge): add FIS audit-as-assurance pattern and tech/ops/facility layer
```

## Migration status

| Item | Status |
|------|--------|
| Migration complete | ✅ |
| Commit | pending (not requested) |
