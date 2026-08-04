---
type: framework
title: "Pattern 5｜変革の9要素（Transformation Elements）"
source: "構造化とは何か_r5.pptx（Ch2-2.1, Pattern 5, p.16）を core/reasoning.md の Transformation thinking に合わせて9要素へ拡張"
status: validated
extracted: false
gap_fill: "元スライドは4要素（People/Process/Technology/Governance）。core/reasoning.mdのTransformation thinking（9要素）に合わせてKazuaki承認のもと拡張。新規5要素（Purpose/Capability/Measurement/Change/Sustainability）の内容・例はAI起案、要レビュー"
related:
  - references/thinking-patterns-reference.md
  - core/reasoning.md
last_updated: 2026-08-03
---

# Pattern 5｜変革の9要素（Transformation Elements）

`core/reasoning.md` の「Transformation thinking」に準拠した9要素版。元教材（構造化とは何か_r5.pptx）の4要素（People/Process/Technology/Governance）を拡張している。

## この型が使われる場面
組織・DX・変革構想において、要素の偏りを防ぎ全方位で構造化する場面で使う。

**適用場面の例**
- DX推進
- AI導入
- 全社組織改革
- Operating Model設計

## 構造

| 視点 | 内容 | 例 | 出典 |
|---|---|---|---|
| Purpose（目的） | なぜこの変革が必要か | AI活用による保全判断の迅速化 | 新規 |
| People（人・体制） | 人・体制 | AI推進チームの設置 | 元スライド |
| Process（業務プロセス） | 業務プロセス | 承認フローの見直し | 元スライド |
| Technology（技術・ツール） | 技術・ツール | RAG基盤の選定 | 元スライド |
| Governance（統制・リスク管理） | 統制・リスク管理 | AI利用ガイドライン | 元スライド |
| Capability（ケイパビリティ） | 実行・維持する能力 | AI人材の育成計画 | 新規 |
| Measurement（測定） | 成果指標 | 判断時間の短縮率 | 新規 |
| Change（チェンジマネジメント） | 定着・浸透 | 現場への説明・トレーニング計画 | 新規 |
| Sustainability（持続可能性） | 継続の仕組み | 運用体制の引き継ぎ計画 | 新規 |

「出典」列は移行の経緯を示すための一時的な記載。レビュー後に削除して構わない。

## 使い方の原則
9つの視点を同程度の粒度で埋める。特にTechnologyだけが厚くなる偏りが起きやすいのは元の4要素版と同じ。加えて、Purpose（なぜやるか）が曖昧なまま他の8要素を埋め始めると、施策同士の整合が取れなくなる。Purposeを最初に固めてから他の要素に着手する。

## Inputs
変革・DX施策の概要、対象組織・スコープ

## Outputs
9要素で偏りなく整理された変革構想の骨子。Operating Model設計や全社改革構想書の章立てにそのまま転用できる。

## Limitations
小規模・短期の個別施策（例：単一ツールの導入）には要素が過剰な場合がある。その場合はPeople/Process/Technology/Governanceの4要素、またはPattern 1（Why→What→How）で足りることが多い。

## Risks
新規5要素（Purpose/Capability/Measurement/Change/Sustainability）は、AIが `core/reasoning.md` の項目名から論理展開して起案したものであり、実案件での使用実績を経ていない。特にMeasurement・Sustainabilityの「例」列は仮置き。実際の案件で使いながら精度を確認する。

## 関連ファイル
- 元の4要素版のAIプロンプト例・レビュー観点は `references/thinking-patterns-reference.md` のPattern 5行を参照（9要素化に伴い更新が必要）
- 上位の考え方は `core/reasoning.md` の「Transformation thinking」

---
**レビュー用メモ（Kazuaki記入欄）**
- [ ] 新規5要素（Purpose/Capability/Measurement/Change/Sustainability）の「内容」列の定義は妥当か
- [ ] 「例」列（特に新規5要素分）は実務で使える精度か、それとも仮置きのままでよいか
- [ ] 「出典」列は削除してよいか
- [ ] status を `validated` に変更してよいか
