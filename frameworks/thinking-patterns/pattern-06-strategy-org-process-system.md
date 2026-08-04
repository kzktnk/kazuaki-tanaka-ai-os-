---
type: framework
title: "Pattern 6｜Strategy → Organization → Process → System（上位下達の整流化）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 6, p.17）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
last_updated: 2026-08-03
---

# Pattern 6｜Strategy → Organization → Process → System（上位下達の整流化）

経営戦略から一気通貫で落とし込む型。

## この型が使われる場面
IT起点・システム起点の歪んだDXを防ぎ、上位の経営戦略から一気通貫で落とし込む場面で使う。

**適用場面の例**
- 全社業務改革
- IT投資計画
- アーキテクチャ構想

## 構造

| 階層 | 内容 |
|---|---|
| Strategy（戦略） | 中期経営計画の方針 |
| Organization（組織） | 推進部門・権限設計 |
| Process（業務） | 業務プロセスの標準化 |
| System（ITシステム） | 要件定義 |

## 使い方の原則
SystemやProcessの都合がStrategyに逆流していないかを確認する。「このシステムでできることから考える」のように下位から積み上げると、上位下達の型が崩れる。階層間のつながりに論理の飛躍がないかも合わせて確認する。

## Inputs
経営戦略・中期経営計画等の上位方針

## Outputs
戦略から一気通貫したStrategy/Organization/Process/Systemの整理。

## Limitations
上位の戦略自体が不在・未確定の場合は成立しない。

## Risks
System都合がStrategyに逆流する（システムの制約に合わせて戦略の説明を歪めてしまう）ことに注意する。

> **実務での位置づけ**：本Patternは教育用の簡略版（4層）。実務では `core/reasoning.md` の「Architecture thinking」（Business → Operating Model → Process → People → Governance → Data → Application → Infrastructure → Operations → Security → Costの11層）を優先する。

## 関連ファイル
AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 6行を参照。

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
