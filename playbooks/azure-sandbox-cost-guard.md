---
type: playbook
title: "Azure sandbox cost guard"
status: active
last_updated: 2026-08-19
related:
  - technology/azure-enterprise.md
  - knowledge/decisions/sandbox-cost-controls-before-resources.md
---

# Azure sandbox cost guard

個人学習、短期間 PoC、検証サブスクリプションで使う。本番の FinOps 全体像ではない。

## Trigger

- 新しい Azure 検証環境を作る  
- 想定外の Cost Analysis 増加  
- 検証を終えてリソースを消す  

## Objective

高額固定費 SKU の混入と、「消したつもりで課金が続く」状態を防ぐ。円・請求番号は記録しない。

## Sequence — before create

1. Budget と段階的 Cost Alert を先に置く  
2. 作るリソースと SKU を一覧化する  
3. 高額固定費（Managed HSM 相当など）は、明示決定なしに作らない  
4. Key Vault 等は意図した SKU であることを作成直後に確認する  

## Sequence — while running

1. 作成当日、翌日、数日後に Cost Analysis を見る  
2. Resource type が意図と違う行があれば、画面上のリソース有無と突き合わせる  
3. ノートブックを Azure の外で動かすなら、Managed Identity 前提の構成と混同しない（認証は `technology/azure-enterprise.md`）  

## Sequence — after finish

1. リソースを削除する  
2. Soft delete / purge が残る種別を確認する  
3. 翌日以降も Cost Analysis で **新規課金が止まったか** を見る  
4. 再利用しないならサブスクリプションを無効化する  
5. 個別削除だけでは確信が持てないときは、サブスクリプション停止を遅らせない  

## Decision points

- Portal 削除済みでも Cost が伸びる → 削除完了とみなさない。SKU / meter を特定するまでサポートや管理者に渡す。返金要求より先に **何に課金されたか**。  
- セルフサービス返金が使えない → 正式サポートへ。自動トラブルシュートに戻されたら別導線を探す。  

## Quality checks

- 作成前に Budget がある  
- 終了後に「課金停止を見た」記録がある（原本。リポジトリには金額を書かない）  

## Outputs

- SKU 一覧（意図したもの）  
- 停止確認の事実（日付のみ可）  
- 残リスク（soft delete、未特定の meter）  

## Related

- `technology/azure-enterprise.md`  
- `knowledge/decisions/sandbox-cost-controls-before-resources.md`  
