---
type: reference
title: "Thinking Patterns 早見表・AIプロンプト・レビュー観点"
source: "frameworks/thinking-patterns/ Pattern 1〜8 および frameworks/top-down-thinking.md から集約"
status: active
version: v0.1
last_updated: 2026-08-04
related:
  - frameworks/top-down-thinking.md
  - frameworks/thinking-patterns/pattern-01-why-what-how.md
  - frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md
  - frameworks/thinking-patterns/pattern-03-input-process-output.md
  - frameworks/thinking-patterns/pattern-04-plan-build-run-improve.md
  - frameworks/thinking-patterns/pattern-05-transformation-elements.md
  - frameworks/thinking-patterns/pattern-06-strategy-org-process-system.md
  - frameworks/thinking-patterns/pattern-07-lifecycle.md
  - frameworks/thinking-patterns/pattern-08-layer.md
  - core/reasoning.md
---

# Thinking Patterns Reference

## Purpose

Thinking Pattern 1〜8 の早見表、Pattern 選定の目安、AI への依頼例、AI 出力のレビュー観点を 1 か所に集約する。

各 Pattern の詳細定義は `frameworks/thinking-patterns/` 配下の個別ファイルを正本とする。本ファイルは参照用インデックスである。

## Scope

- Pattern 選定（どの型を使うか）
- 構造の早見表
- AI プロンプト例（構造を指定して依頼するためのテンプレート）
- AI 出力のレビュー観点

## Intended Use

1. 構造化の前に、適切な Pattern を選ぶ
2. AI に依頼する前に、プロンプトに Pattern と制約を明示する
3. AI の回答を、Pattern 固有の観点でレビューする

トップダウン思考の全体像は `frameworks/top-down-thinking.md` を先に読む。

---

## Pattern 選定ガイド

| やりたいこと | 推奨 Pattern | 補足 |
|---|---|---|
| 提案書・構想の骨子を作る | **1** Why → What → How | `core/reasoning.md` の Communication rule と整合 |
| 現状分析・ギャップ整理 | **2** As-Is → Gap → To-Be | コンサルで最頻出 |
| 業務・WBS・工程分解 | **3** Input → Process → Output | 詳細手順は `playbooks/wbs-design.md` |
| ロードマップ全体像 | **4** Plan → Build → Run → Improve | 詳細工程は Pattern 7 |
| DX・変革の全方位整理 | **5** 変革の 9 要素 | `core/reasoning.md` Transformation thinking 準拠 |
| 戦略から IT まで一気通貫 | **6** Strategy → Org → Process → System | 実務は reasoning.md Architecture thinking を優先 |
| 詳細工程・WBS 粒度 | **7** 企画→構想→設計→構築→テスト→運用→改善 | Pattern 4 の詳細版 |
| システム・責任分界の整理 | **8** Business / Application / Data / Infrastructure | 実務は reasoning.md Architecture thinking を優先 |

Pattern 4 と 7、Pattern 6 と 8 は粒度・用途が異なるペアとして使い分ける。

---

## 早見表

| Pattern | 名称 | 構造（箱） | 主な適用場面 | 詳細ファイル |
|---|---|---|---|---|
| **1** | Why → What → How（目的逆算型） | Why / What / How | 提案書、DX 戦略、AI 導入構想、ロードマップ | `frameworks/thinking-patterns/pattern-01-why-what-how.md` |
| **2** | As-Is → Gap → To-Be（現状分析型） | As-Is / Gap / To-Be | 現状分析、BPR、Operating Model、AI 成熟度評価 | `frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md` |
| **3** | Input → Process → Output（工程分解型） | Input / Process / Output | 業務整理、WBS、要件定義、プロセス設計 | `frameworks/thinking-patterns/pattern-03-input-process-output.md` |
| **4** | Plan → Build → Run → Improve（ライフサイクル展開型） | Plan / Build / Run / Improve（循環） | ロードマップ、AI・クラウド導入、大規模 IT 推進 | `frameworks/thinking-patterns/pattern-04-plan-build-run-improve.md` |
| **5** | 変革の 9 要素（Transformation Elements） | Purpose / People / Process / Technology / Governance / Capability / Measurement / Change / Sustainability | DX 推進、AI 導入、全社改革、Operating Model 設計 | `frameworks/thinking-patterns/pattern-05-transformation-elements.md` |
| **6** | Strategy → Organization → Process → System（上位下達） | Strategy / Organization / Process / System | 全社業務改革、IT 投資計画、アーキテクチャ構想 | `frameworks/thinking-patterns/pattern-06-strategy-org-process-system.md` |
| **7** | 時系列／Lifecycle（詳細工程） | 企画 / 構想 / 設計 / 構築 / テスト / 運用 / 改善 | 詳細工程計画、WBS、進捗管理 | `frameworks/thinking-patterns/pattern-07-lifecycle.md` |
| **8** | レイヤー構造 | Business / Application / Data / Infrastructure | アーキテクチャ設計、IT 組織の役割分担、障害切り分け | `frameworks/thinking-patterns/pattern-08-layer.md` |

---

## Pattern 1｜Why → What → How

**詳細:** `frameworks/thinking-patterns/pattern-01-why-what-how.md`

### AI プロンプト例

```
以下のテーマを Pattern 1（Why → What → How）で構造化してください。

【テーマ】{対象テーマ}
【背景】{環境変化・課題感}

制約:
- Why（なぜ）→ What（何を）→ How（どうやって）の順で記述する
- How から書き始めない
- 各階層は 1〜3 文で簡潔に
- 根拠のない一般論は避け、不明点は「要確認」と明記する
```

### AI レビュー観点

- [ ] Why が先に書かれており、How から始まっていないか
- [ ] What が Why から論理的に導かれているか
- [ ] How が What を実現する具体手段になっているか（ツール名の羅列だけになっていないか）
- [ ] 「とりあえず AI を入れる」型の目的なき How になっていないか
- [ ] ステークホルダー間で Why が未合意の場合、その旨が明示されているか

---

## Pattern 2｜As-Is → Gap → To-Be

**詳細:** `frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md`

### AI プロンプト例

```
以下の対象について Pattern 2（As-Is → Gap → To-Be）で構造化してください。

【対象】{分析対象}
【現状情報】{データ・ヒアリング結果}
【To-Be の方向性】{方針・仮説}

制約:
- As-Is は客観的事実ベースで記述する
- Gap は As-Is と To-Be の差分から導く構造的課題・能力差として書く
- Gap を先に決めてから As-Is / To-Be を当てはめない
- 主観的な不満の羅列にしない
```

### AI レビュー観点

- [ ] As-Is が客観的事実・データに基づいているか（伝聞・不満ベースでないか）
- [ ] Gap が As-Is と To-Be の差分から論理的に導かれているか
- [ ] To-Be が合意可能な粒度で書かれているか
- [ ] Gap が改善施策の根拠として使える具体性があるか
- [ ] To-Be 未確定の場合、その前提が明示されているか

---

## Pattern 3｜Input → Process → Output

**詳細:** `frameworks/thinking-patterns/pattern-03-input-process-output.md`

### AI プロンプト例

```
以下の業務を Pattern 3（Input → Process → Output）で分解してください。

【対象業務】{業務名}
【範囲】{どこからどこまでを 1 工程とするか}

制約:
- Process は動詞（〜する）、Output は名詞（形のある成果物）で書く
- 「〜を検討する」のような未完了状態を Output にしない
- WBS に展開できる粒度まで分解する
```

### AI レビュー観点

- [ ] Process が動詞、Output が名詞（成果物）で書き分けられているか
- [ ] Output が完了状態を判定できる具体性があるか
- [ ] Input が Process の前提として十分か
- [ ] 工程の範囲（スコープ）が明示されているか
- [ ] WBS に展開したとき、タスクの完了条件が曖昧にならないか

---

## Pattern 4｜Plan → Build → Run → Improve

**詳細:** `frameworks/thinking-patterns/pattern-04-plan-build-run-improve.md`

### AI プロンプト例

```
以下の施策を Pattern 4（Plan → Build → Run → Improve）でロードマップ化してください。

【施策】{導入・変革の対象}
【スコープ】{対象範囲・期間}

制約:
- 4 フェーズすべてに具体的内容を記載する
- Improve は次の Plan へ接続する循環構造を意識する
- Build に偏重せず、Run・Improve を具体化する
- 「作って終わり」にならないこと
```

### AI レビュー観点

- [ ] Plan / Build / Run / Improve の 4 フェーズがすべて埋まっているか
- [ ] Run・Improve が具体化されているか（Build 偏重でないか）
- [ ] Improve が次の Plan へ接続する循環構造になっているか
- [ ] 単発施策に無理やり当てはめていないか
- [ ] 詳細粒度が必要な場合、Pattern 7 への展開が示唆されているか

---

## Pattern 5｜変革の 9 要素

**詳細:** `frameworks/thinking-patterns/pattern-05-transformation-elements.md`  
**上位参照:** `core/reasoning.md` の Transformation thinking

### AI プロンプト例

```
以下の変革施策を Pattern 5（変革の 9 要素）で構造化してください。

【施策】{DX・AI 導入・組織改革の概要}
【対象組織・スコープ】{範囲}

9 要素:
Purpose / People / Process / Technology / Governance / Capability / Measurement / Change / Sustainability

制約:
- Purpose を最初に固めてから他の 8 要素に着手する
- 9 要素を同程度の粒度で埋める
- Technology だけが厚くならないよう注意する
- 根拠のない一般論は避け、不明点は「要確認」と明記する
- 小規模・短期施策の場合は 4 要素（People/Process/Technology/Governance）で足りる旨を示す
```

### AI レビュー観点

- [ ] Purpose が最初に固まっており、他要素と整合しているか
- [ ] 9 要素が偏りなく埋まっているか（Technology 偏重でないか）
- [ ] People / Process / Technology / Governance が具体性を持っているか
- [ ] Capability / Measurement / Change / Sustainability が空欄・一般論のままになっていないか
- [ ] 施策規模に対して 9 要素が過剰でないか（Pattern 1 への切り替え余地）
- [ ] `core/reasoning.md` の Transformation thinking と要素名が一致しているか

---

## Pattern 6｜Strategy → Organization → Process → System

**詳細:** `frameworks/thinking-patterns/pattern-06-strategy-org-process-system.md`  
**実務優先:** `core/reasoning.md` の Architecture thinking（11 層）

### AI プロンプト例

```
以下のテーマを Pattern 6（Strategy → Organization → Process → System）で構造化してください。

【上位方針】{経営戦略・中期計画}
【対象】{業務改革・IT 投資の対象}

制約:
- Strategy から下位へ一気通貫で落とし込む
- System や Process の都合が Strategy に逆流していないか確認する
- 階層間の論理の飛躍がないこと
- 教育用 4 層版であること。実務の詳細は reasoning.md Architecture thinking を参照
```

### AI レビュー観点

- [ ] Strategy から Organization → Process → System へ一方向に落ちているか
- [ ] System 都合が Strategy を歪めていないか（下位からの積み上げになっていないか）
- [ ] 階層間に論理の飛躍がないか
- [ ] 上位戦略が不在・未確定の場合、その前提が明示されているか
- [ ] 実務用途では reasoning.md の 11 層モデルへの昇格が必要か判断されているか

---

## Pattern 7｜時系列／Lifecycle（詳細工程）

**詳細:** `frameworks/thinking-patterns/pattern-07-lifecycle.md`

### AI プロンプト例

```
以下のプロジェクトを Pattern 7（企画→構想→設計→構築→テスト→運用→改善）で詳細工程化してください。

【プロジェクト】{対象}
【大枠フェーズ】{Pattern 4 で定義した Plan/Build/Run/Improve があれば記載}

制約:
- 7 フェーズすべてに具体的内容を記載する
- 各フェーズの成果物と次フェーズへの受け渡しを明示する
- 全体像説明には Pattern 4 を使い、本 Pattern は詳細工程向けであること
```

### AI レビュー観点

- [ ] 企画 / 構想 / 設計 / 構築 / テスト / 運用 / 改善の 7 フェーズが埋まっているか
- [ ] フェーズ間の成果物の受け渡しが明示されているか
- [ ] 箇条書きの羅列に留まらず、工程表として機能しているか
- [ ] 全体像資料として使うには粒度が細かすぎないか（Pattern 4 が適切な場合）
- [ ] WBS の土台として展開可能な粒度か

---

## Pattern 8｜Business / Application / Data / Infrastructure

**詳細:** `frameworks/thinking-patterns/pattern-08-layer.md`  
**実務優先:** `core/reasoning.md` の Architecture thinking（11 層）

### AI プロンプト例

```
以下の対象を Pattern 8（Business / Application / Data / Infrastructure）の 4 レイヤーで整理してください。

【対象】{システム・組織・障害事象}
【整理目的】{アーキテクチャ設計 / 責任分界 / 原因切り分け}

制約:
- 各論点を 1 つのレイヤーに分類する（混在させない）
- 一つの事象が複数レイヤーにまたがる場合は、レイヤーごとに分解して記述する
- 教育用 4 層版であること。実務の詳細は reasoning.md Architecture thinking を参照
```

### AI レビュー観点

- [ ] Business / Application / Data / Infrastructure に論点が分離されているか
- [ ] 一つの事象が複数レイヤーに混在したまま記述されていないか
- [ ] 各レイヤーの責任分界が議論できる具体性があるか
- [ ] 純粋な業務課題に無理やり IT レイヤーを当てはめていないか
- [ ] 実務用途では reasoning.md の 11 層モデルへの昇格が必要か判断されているか

---

## Limitations

- 本ファイルは Pattern 定義の要約である。詳細・制約・リスクは各 Pattern ファイルを正本とする。
- Pattern 5 の新規 5 要素（Purpose / Capability / Measurement / Change / Sustainability）は実案件での検証が十分でない。プロンプト例・レビュー観点も随時更新する。
- Pattern 6・8 は教育用簡略版。実務のアーキテクチャ議論では `core/reasoning.md` を優先する。

## Related Assets

- トップダウン思考の全体像: `frameworks/top-down-thinking.md`
- 推論原則（Why/What/How、Transformation、Architecture）: `core/reasoning.md`
- WBS 展開手順: `playbooks/wbs-design.md`
- Pattern 正本: `frameworks/thinking-patterns/pattern-01-why-what-how.md` 〜 `pattern-08-layer.md`
