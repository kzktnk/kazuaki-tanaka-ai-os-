# Pattern: Unowned Work in Effort Analysis

**Status:** Active  
**Origin:** Anonymized coaching on structuring current work for hearing and effort sketch (Program Line AE, 2026-08-28). Client facts, names, yen, and effort numbers are **not** stored here.

## Pattern statement

> **人に紐づく PDC の箱だけで現状工数を整理すると、まだ人が当たっていない仕事が漏れる。網羅とヒアリングしやすさが要るときは、検討主体を中段に置き、その下で実行と管理を分ける。**

「誰がどのくらいの時間を何に使っているか」は拾える。ただしそれは**人がやっている箱**である。未割当・未明確のタスクは、人軸では見えない。いまの作業一覧が洗い出し済みだという前提が持てるなら人軸でも成り立つ。一覧に穴があり得るなら、漏れる。

代替の骨格（例）:

```text
検討主体（ワーキング／共通検討）
    └── 実行（準備 → 実施 → アフター）
    └── 管理（報告・統制）
```

フレーム（計画・実行・管理）を先に当てはめてから下に降ろすより、**検討の主体**を中段にした方が、網羅とヒアリングの両方に乗りやすいことが多い。

## Actuals, not a WBS redesign

これは現状のアクチュアルを並べる仕事であり、WBS を聖地化して作り直す話ではない。精度に時間を使いすぎない。ゴールは「だいたいこんな感じ／だいたいこう使っている」が言えること。

スコープが今フェーズ（例: 要件定義の範囲）なら、見えていないものは未確定でもあるし、想像が追いつかない未来でもある。完全洗い出しより、現状のやり方に**見えざる分の控え目なバッファ**を乗せる割り切りの方が、時間対効果に合う。

メンバーへの軽い確認（漏れがないか）は、構造を一度置いてからでよい。

## Tests

- 人に紐づかない仕事が、どの箱に入るか言えるか  
- 「WBS 再設計」と「現状の使い方のスケッチ」を混同していないか  
- 将来投影が要るのに、今やっていることだけを精度高く積んでいないか  
- ゴールが方向感（だいたい）なのに、網羅精度を追っていないか  

## Use with

- 箱を仕事の塊から作る → `frameworks/top-down-thinking.md`  
- 支援工数の報告軸（個別／PJ間／横断）→ `knowledge/patterns/support-effort-classification.md`  
- 成果物逆算 WBS そのもの → `playbooks/wbs-design.md`（本パターンの代替ではない）  

## Related

- `frameworks/top-down-thinking.md`  
- `knowledge/patterns/support-effort-classification.md`  
- `playbooks/wbs-design.md`  
- `knowledge/migrations/coaching-20260828-change-effort-buyer-gap-2026-08.md`  
