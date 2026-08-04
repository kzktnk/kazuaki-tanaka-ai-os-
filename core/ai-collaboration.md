---
type: core
title: "AIを「思考拡張パートナー」として使う"
source: "構造化とは何か_r5.pptx（Ch4, p.28-33）"
status: validated
extracted: true
gap_fill: "Purpose/Scope/Intended Use/Limitationsの各項目はARCHITECTURE.md 11節の様式に合わせて新規追加。本文（Content）はCh4からの抽出のまま"
related:
  - core/reasoning.md
  - playbooks/wbs-design.md
  - exercises/exercise-05-spotting-plausible-ai-errors.md
version: v0.1
last_updated: 2026-08-03
---

# AIを「思考拡張パートナー」として使う

## Purpose
AIとの協働において、「答えを聞く」のではなく「自ら考えるためにAIを使う」という基本姿勢を定義する。最終的な妥当性判断は常に人間が担う、という原則を `core/reasoning.md` の推論システムと接続する。

## Scope
AIへの依頼の設計、依頼のレベル分け、AIの回答の検証、人とAIの役割分担に適用する。個別ツール（Claude／ChatGPT等）固有の操作方法は対象外（`adapters/` を参照）。

## Intended Use
新しい依頼をAIにする前、またはAIの回答をレビューする前に参照する。特にLevel 3（レビュー・批判的検討）としての使い方に迷ったときに立ち返る。

## Content

### 「問い」の設計が最重要
AIの回答品質は、プロンプトの質（情報の解像度）に完全に依存する。依頼前に明確にすべき前提情報：目的／背景／前提条件／制約事項／期待する成果。これらを明確にし、構造化された文脈を与えて初めてAIは真価を発揮する。

### AIへの依頼を3段階に分ける

| レベル | 内容 | 例 |
|---|---|---|
| Level 1 | 情報収集・要約 | 調査、用語整理、海外事例の要約など |
| Level 2 | 構造化・フレームワーク化 | Input-Process-Outputやマトリクスへの整理、WBSのたたき台作成 |
| Level 3（★最も価値が高い） | レビュー・批判的検討 | 論理の飛躍の指摘、反対意見の抽出、クライアント視点での壁打ち |

Level 3（レビュー相手としての活用）が、最もコンサルタントとして価値が高い。

### 「もっともらしい間違い」を見抜く
生成AIは、文章が流暢であるほど、誤った情報でも正しく見えてしまう。

例（RAGの評価について）：「翻訳評価用のBLEUを使うべきです」→ 一般論としては正しくても、案件の文脈や技術要件に合致しない提案。

AIは「選択肢を広げる道具」。最終的な意思決定と妥当性の担保は、常に人間が担う。

### 人とAIの役割分担マトリクス

| 人が担う領域 | AIが支援する領域 |
|---|---|
| 目的設定・ゴール定義 | 情報収集・リサーチの壁打ち |
| 構造設計（Thinking Patternの選択） | 大量のアイデア・代替案の網羅的生成 |
| 優先順位付けと意思決定 | 文章の要約、分類、初期ドラフト作成 |
| クライアントとの合意形成・ファシリテーション | プロセスの壁打ち、多角的なレビュー視点の提供 |

### AIを「セルフレビューの相手」として使う
「WBSを作ってください」と聞くのではなく、次のように問いかけてみる。

- 「このWBSの構成に、プロジェクト管理上抜け落ちているリスクやレビュー工程はありますか？」
- 「別のThinking Pattern（例えばAs-Is/To-Be）でこの課題をとらえ直すと、どういう視点追加があり得ますか？」
- 「この提案に対するクライアント（経営層）からの厳しい反対意見を3つ挙げてください。」

対話を重ねることで、AIは自動生成ツールから、思考を拡張する最高のパートナーへと進化する。

## Limitations
教育教材（若手コンサル向け研修）からの抽出のため、記載は基本姿勢にとどまる。`core/reasoning.md` の「Suggested Reasoning Rule」（execution／authority／accountabilityの分離）のような、より高度な責任分界の議論は含んでいない。必要に応じて拡張する。

## Related Assets
- `core/reasoning.md`（Partner review mode、Suggested Reasoning Rule）
- `playbooks/wbs-design.md`（Step 5：AIの使い方）
- `exercises/exercise-05-spotting-plausible-ai-errors.md`

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] core/の他ファイル（identity.md、values.md等）とトーンが揃っているか
- [ ] Limitationsの記述で十分か。reasoning.mdとの役割分担がこれで伝わるか
- [ ] status を `validated` に変更してよいか
