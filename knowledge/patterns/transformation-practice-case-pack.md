---
type: pattern
---

# Pattern — Transformation Practice Case Pack

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Transformation Practice Case Pack  
**Applies to:** Internal practice communities packaging transformation / PgMO / change lessons for reuse (monthly forums, coaching packs)  
**Origin:** Anonymized **enterprise transformation case pack 2019** structure only. Case narratives, client identifiers, and personal names are **not** stored here.

**Does not contain:** client stories with identifiers, org charts with real names, yen, proposal bodies, contact directories

---

## Pattern statement

> **変革の「事例パッケージ」は、物語の集積ではなく、読者が自分のロールと案件タイプから入れる学習装置である。テーマカードは壁→組織としての型→前提知識／姿勢→アプローチの順で固定し、事例本文は原本に残す。**

クライアント成果物（Archetype A/C/J）や PgMO 手順書（`cross-project-program-management.md` 等）とはジョブが違う。本パターンは **社内／コミュニティの学習パッケージの骨格** である。

---

## Pack anatomy

| Block | Job |
|-------|-----|
| **Positioning** | なぜこのパックがあるか（例: 月次フォーラムの蓄積を再利用する） |
| **How to read** | 最初から通読／テーマだけ／付録から、の許可 |
| **Audience contract** | 若手＝疑似体験、中堅＝気づき、ベテラン＝刺激、など読み方の約束 |
| **Navigation matrix** | 縦軸＝ロール（PM / TL / Member 等）、横軸＝案件タイプ（構想 Plan／実行 Do／評価・改善 Check-Action） |
| **Theme cards** | 各学習単位。サマリー＋本編に分けてよい |
| **References** | 古典・方法論のポインタ（著者・書誌の羅列は最小。案件固有は載せない） |

案件タイプの例（ラベルは一般化）:

| Type | Typical work |
|------|----------------|
| **Plan** | 構想、ビジョニング、組織設計、リサーチ |
| **Do** | PrjMO / PgMO / change delivery |
| **Check / Action** | 評価、改善、定着の振り返り |

---

## Theme card schema

各テーマは、次の欄を揃える（挑発的タイトルは可。固有名詞は不可）:

| Field | Purpose |
|-------|---------|
| **Title** | 議論のフックになる問い／見出し |
| **Wall** | 直面した悩み・壁（一般化した状況） |
| **Org response pattern** | 個人の武勇伝ではなく、組織として取りうる型 |
| **Prerequisite knowledge** | 知らないと対応しにくい体系・方法論 |
| **Enrichment knowledge** | 知っていると上手くなりやすい補助 |
| **Mindset** | 姿勢・心構え |
| **Approach** | 実際の進め方の骨格 |

**登録しないもの:** 生の事例ストーリー、クライアント名、担当者名、金額、組織図、連絡先、「該当する参考事例／コンタクト先」の実データ。

---

## Design rules

1. **サマリーと本編を分ける** — 忙しい読者はサマリーだけで型を持ち帰れるようにする。  
2. **ロール×タイプで入れる** — 目次が時系列だけだと、学習装置にならない。  
3. **知識を「必須／あると良い」に分ける** — 方法論の百科事典化を防ぐ。  
4. **型と物語を分離する** — リポジトリには型だけ。物語はローカル原本。  
5. **クライアント提出物に転用しない** — 社内学習のトーンと、顧客向けステータス／提案のトーンを混ぜない。

---

## Tests

- クライアント名を消したあとも、カードが「誰向けのどの壁か」で読めるか  
- ナビゲーション行列なしにテーマが並んでいないか  
- Org response が個人名の英雄譚になっていないか  
- References が案件固有の社内パスや個人連絡先になっていないか  

---

## Use with

- 変革 PMO の位置づけ → `frameworks/transformation-pmo.md`  
- 人側の壁 → `frameworks/change-management.md`  
- PJ 間の型が必要なとき → `playbooks/cross-project-program-management.md`（本パックの代替ではない）  
- 顧客向け月次 → Archetype J（本パックを顧客資料にしない）

## Related

- `knowledge/migrations/related-project-radar-and-et-case-pack-2026-08.md`
- `knowledge/lessons/pmo-professional-principles.md`
