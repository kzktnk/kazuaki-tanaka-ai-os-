---
type: framework
title: "Pattern 7｜企画→構想→設計→構築→テスト→運用→改善（時系列／Lifecycle）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 7, p.18）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
  - frameworks/thinking-patterns/pattern-04-plan-build-run-improve.md
last_updated: 2026-08-03
---

# Pattern 7｜企画→構想→設計→構築→テスト→運用→改善（時系列／Lifecycle）

Pattern 4をさらに細かくした工程レベルの型。

## この型が使われる場面
企画〜改善のフェーズごとに網羅的に整理する場面で使う。

**適用場面の例**
- システム開発の詳細工程計画
- WBS策定
- 進捗管理

## 構造

| フェーズ | 内容 |
|---|---|
| 企画 | 課題の言語化 |
| 構想 | To-Beモデル策定 |
| 設計 | 要件〜詳細設計 |
| 構築 | 開発・データ移行 |
| テスト | 単体〜受入テスト |
| 運用 | 本稼働・保守 |
| 改善 | 効果検証 |

## 使い方の原則
全体像の説明にはPattern 4（Plan→Build→Run→Improve）、詳細工程の説明にはPattern 7を使う。両者は同じライフサイクルを異なる粒度で見ているだけなので、対象読者や資料の目的に応じて使い分ける。

## Inputs
Pattern 4（Plan→Build→Run→Improve）で定義した大枠のフェーズ、または詳細化したい対象工程

## Outputs
企画〜改善の7フェーズに展開された詳細工程表。WBSの土台になる。

## Limitations
全体像の説明資料としては粒度が細かすぎる（その場合はPattern 4を使う）。

## Risks
フェーズ間の成果物の受け渡しを明示しないまま並べると、実質的にただの箇条書きになり、工程表としての機能を果たさない。

## 関連ファイル
- AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 7行を参照
- より粗い全体像レベルは `frameworks/thinking-patterns/pattern-04-plan-build-run-improve.md` を参照

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
