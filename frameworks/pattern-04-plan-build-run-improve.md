---
type: framework
title: "Pattern 4｜Plan → Build → Run → Improve（ライフサイクル展開型）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 4, p.15）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
  - frameworks/thinking-patterns/pattern-07-lifecycle.md
last_updated: 2026-08-03
---

# Pattern 4｜Plan → Build → Run → Improve（ライフサイクル展開型）

## この型が使われる場面
プロジェクトや施策を時系列・ライフサイクルに沿って構造化する場面で使う。

**適用場面の例**
- ロードマップ策定
- AI・クラウド導入
- 大規模ITプロジェクト推進

## 構造

| フェーズ | 内容 |
|---|---|
| Plan | 計画 |
| Build | 構築 |
| Run | 運用 |
| Improve | 改善 |

**循環構造**：Improveの後は次のPlanへ戻る。一直線で終わる工程ではない。

## 使い方の原則
全体像を大きな4フェーズで説明したいときはPattern 4を、各フェーズをさらに詳細な工程レベルまで分解したいときはPattern 7（時系列／Lifecycle）を使う。目的の粒度に応じて使い分ける。

## Inputs
対象施策・プロジェクトのスコープ（何を導入・変革するか）

## Outputs
Plan/Build/Run/Improveの4フェーズに整理されたロードマップ。Improveが次のPlanへ接続する循環構造を持つ。

## Limitations
単発で終了し、運用フェーズが存在しない施策には強引に当てはめない。

## Risks
Buildの記述に偏重し、Run・Improveが具体化されないまま資料が完成しがち。「作って終わり」の説明になっていないか確認する。

## 関連ファイル
- AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 4行を参照
- より詳細な工程レベルは `frameworks/thinking-patterns/pattern-07-lifecycle.md` を参照

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
