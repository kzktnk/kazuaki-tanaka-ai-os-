# Pattern: Support Effort Classification

**Status:** Active  
**Origin:** Anonymized coaching on customer-facing status (Program Line Z, 2026-08-24). Client facts, names, and effort numbers are **not** stored here.

## Pattern statement

横断支援の工数を「なんとなく忙しい」で語ると、顧客向け報告も WBS も崩れる。**個別プロジェクト／プロジェクト間／横断＋課題管理**の軸で先に分け、Confirm とフォローの負荷差を混同しない。

| Bucket | What it covers | Typical signal |
|--------|----------------|----------------|
| **Individual (per PJ)** | 単一 PJ 内のレビュー、確認、助言 | その PJ の台帳・成果物に閉じる |
| **Between projects** | 受け渡し・依存・整合の調整 | 2つ以上の PJ が動かないと閉じない |
| **Cross-cutting + issue mgmt** | プログラム横断の方針、未決・課題の追跡、顧客共有リストの手入れ | どの単一 PJ の WBS にも落ちない |

## Tests

- 今週の工数を上表のどれかに置けるか（「その他」だらけなら軸が未完）  
- Confirm（確認・合意取得）と Follow（追跡・催促・再説明）を同じ箱に詰めていないか  
- 課題管理が「個別支援」に吸収されて消えていないか  

## Use with

- 顧客向け月次の支援概要（`standards/deliverable-archetypes.md` Archetype J）で、概要レベルだけ語る  
- 成果物逆算 WBS（`playbooks/wbs-design.md`）の**前段**で、支援仕事の箱を作るとき。WBS 手順そのものの代替ではない  

## Related

- `standards/deliverable-archetypes.md` Archetype J  
- `knowledge/patterns/project-management-policy-layer.md`  
- `playbooks/cross-project-program-management.md`  
- `frameworks/top-down-thinking.md`  
