---
type: framework
title: "Pattern 3｜Input → Process → Output（工程分解型）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 3, p.14）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
  - playbooks/wbs-design.md
last_updated: 2026-08-03
---

# Pattern 3｜Input → Process → Output（工程分解型）

WBSの土台となる思考法。

## この型が使われる場面
業務や仕事を一連の「工程」として捉える場面で使う。

**適用場面の例**
- 業務整理
- WBS策定
- システム要件定義
- プロセス設計

## 構造

| 階層 | 内容 | 例 |
|---|---|---|
| Input | 何を受け取るか | RFP・提案書・既存データ |
| Process | 何をするか | 評価設計・ベンチマーク調査 |
| Output | 何を残すか | PoC評価計画書・完了報告書 |

## 使い方の原則
「Process」は動詞（〜する）、「Output」は名詞（形のある成果物）で書き分ける。ここが曖昧だと、そのままWBSに展開したときにタスクの完了状態が判定できなくなる。

## Inputs
対象業務・工程の範囲定義（どこからどこまでを1つの工程として扱うか）

## Outputs
Input/Process/Outputに整理された業務構造。WBSへ展開できる粒度まで持っていける。

## Limitations
単発の意思決定や、繰り返しのない一回限りの判断には向かない（「工程」として捉えにくい）。

## Risks
ProcessとOutputの境界が曖昧になりやすい。「〜を検討する」のような動詞のままのOutputは、実質的に未完了のタスクを完了扱いしてしまっている。

## 関連ファイル
- AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 3行を参照
- WBSへの具体的な展開手順は `playbooks/wbs-design.md` を参照

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
