---
type: framework
title: "Pattern 8｜Business / Application / Data / Infrastructure（レイヤー構造）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 8, p.19）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
last_updated: 2026-08-03
---

# Pattern 8｜Business / Application / Data / Infrastructure（レイヤー構造）

議論の混線を防ぐための型。

## この型が使われる場面
複雑なシステムアーキテクチャや組織の責任分界を整理する場面で使う。

**適用場面の例**
- システムアーキテクチャ設計
- IT組織の役割分担整理
- 障害時の原因切り分け

## 構造

| レイヤー | 内容 | 例 |
|---|---|---|
| Business（ビジネス） | 業務そのもの | 受発注フロー |
| Application（アプリ） | 業務を支えるアプリ | ECサイト・在庫管理 |
| Data（データ） | 扱うデータ | 商品マスタ・購買履歴 |
| Infrastructure（インフラ） | 基盤 | クラウド基盤・CDN |

## 使い方の原則
一つの事象が複数レイヤーにまたがって語られ、論点が混線していないかを確認する。「動かない」という一言の中に、実はBusiness（そもそも業務要件が曖昧）とInfrastructure（サーバーの障害）が混在している、といった事態を防ぐのがこの型の役割。

## Inputs
対象システム・組織の範囲

## Outputs
Business/Application/Data/Infrastructureの4層に整理された構造。責任分界の議論の土台になる。

## Limitations
技術要素を含まない純粋な業務課題には適用しにくい。

## Risks
一つの事象を複数レイヤーにまたがって記述したまま整理を終えると、この型を使う意味がなくなる（混線防止という目的を達成できない）。

> **実務での位置づけ**：本Patternは教育用の簡略版（4層）。実務では `core/reasoning.md` の「Architecture thinking」（Business → Operating Model → Process → People → Governance → Data → Application → Infrastructure → Operations → Security → Costの11層）を優先する。Pattern 6（Strategy→Org→Process→System）とあわせて、reasoning.md側では1つのモデルに統合されている。

## 関連ファイル
AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 8行を参照。

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
