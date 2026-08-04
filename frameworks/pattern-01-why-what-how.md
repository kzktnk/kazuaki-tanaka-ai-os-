---
type: framework
title: "Pattern 1｜Why → What → How（目的逆算型）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 1, p.12）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
last_updated: 2026-08-03
---

# Pattern 1｜Why → What → How（目的逆算型）

## この型が使われる場面
戦略・構想・提案書のように、まず全体の納得感（なぜやるのか）を作ってから中身を詰める場面で使う基本構造。

**適用場面の例**
- 提案書作成
- DX戦略立案
- AI導入構想
- ロードマップ策定

## 構造

| 階層 | 問い | 例 |
|---|---|---|
| Why | なぜ | 熟練者不足・業務負荷の高騰 |
| What | 何を | 知識継承・保全判断の迅速化 |
| How | どうやって | RAG構築・AI Agent実装 |

## 使い方の原則
「なぜやるのか」から考え、「何を実現するか」を決め、最後に「どう実現するか」を落とし込む。

順序を逆にしない。Howから始めると、目的なきツール導入（「とりあえずAIを入れる」）になりやすい。

## Inputs
- 対象テーマ（施策・提案・構想の対象）
- なぜそれが必要とされているかの背景情報（環境変化、課題感など）

## Outputs
Why/What/Howの3階層に整理された構造。多くの場合、提案書・構想資料の骨子としてそのまま使える。

## Limitations
Whyについて複数のステークホルダー間で合意が取れていない場合は機能しにくい。その場合はWhy自体の合意形成が先に必要で、この型はまだ使えない。

## Risks
Howから書き始めてWhyを後付けすると、目的なきツール導入を正当化するための「見た目だけの構造化」になる。

## 関連ファイル
AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 1行を参照。

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
