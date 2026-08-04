---
type: framework
title: "Pattern 2｜As-Is → Gap → To-Be（現状分析型）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 2, p.13）"
status: validated
extracted: true
gap_fill: "Inputs/Outputs/Limitations/Risksを新規追加。元スライドには無い項目のため、既存の構造・適用場面から論理展開して新規作成（ARCHITECTURE.md 6.5準拠）"
related:
  - references/thinking-patterns-reference.md
last_updated: 2026-08-03
---

# Pattern 2｜As-Is → Gap → To-Be（現状分析型）

コンサルティングで最も使用頻度が高い型。

## この型が使われる場面
現状分析とありたい姿のギャップを構造化する場面で使う。

**適用場面の例**
- 現状分析
- BPR（業務改革）
- Operating Model策定
- AI成熟度評価

## 構造

| 階層 | 内容 | 例 |
|---|---|---|
| As-Is | 現状 | IT人材不足・システム乱立 |
| Gap | 課題・能力差 | 標準プロセスの欠如 |
| To-Be | 理想 | AI前提のOperating Model |

## 使い方の原則
Gapは単なる「不満」の書き出しではなく、As-IsとTo-Beの差分から論理的に導かれる「構造的な課題・能力差」として書く。Gapが先にあって後からAs-Is/To-Beを当てはめると、根拠のない課題設定になりやすい。

## Inputs
- 現状に関する客観的な情報（データ、ヒアリング結果）
- To-Beの仮説、または既に合意されている方針

## Outputs
As-Is/Gap/To-Beの3階層に整理された構造。Gapがそのまま改善施策の根拠になる。

## Limitations
To-Beが定まっていない、または合意されていない段階では、Gapの妥当性そのものを検証できない。

## Risks
As-Isを主観や不満ベースで書くと、Gapも歪む。現状把握が実データではなく伝聞ベースになっていないか要確認。

## 関連ファイル
AIプロンプト例・AIレビュー観点は `references/thinking-patterns-reference.md` のPattern 2行を参照。

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] トーン・粒度は既存の `thinking.md` 等と揃っているか
- [ ] 「使い方の原則」は自分の言葉として違和感がないか
- [ ] status を `validated` に変更してよいか
