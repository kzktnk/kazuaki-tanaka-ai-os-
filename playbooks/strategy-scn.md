---
type: playbook
---

# Strategy / SCN Playbook

**Version:** v0.2  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** 戦略立案（IT戦略を含む）から SCN 構造化・KPI・プロジェクト化（Gate 1）までを、メンティーが自走できる順序でつなぐ  
**Use when:** 経営課題／IT課題の定義→分析→SCN→KPI→Program／Project 分解までを一気通貫でコーチングするとき  
**Do not use as-is for:** SCN 記法・WS 運営の詳細（`standards/scn-creation-guide.md`）、型の定義本体（`frameworks/consulting-strategy-process.md` / `frameworks/strategic-capability-network.md`）、複数ベンダー PJ 間統合（`playbooks/cross-project-program-management.md`）、運用・定着化（`playbooks/operations-transition-playbook.md`）、Stakeholderを実際に動かす技術（`playbooks/stakeholder-activation-playbook.md`）  
**Source revision:** local Strategy-SCN Playbook v1.2（2026-08-28 pointer update）

Pairs with `frameworks/consulting-strategy-process.md`（問題設定〜提言）、`frameworks/strategic-capability-network.md`＋`standards/scn-creation-guide.md`（SCN 本体）、`frameworks/it-strategy-foundations.md`（Insight→Architecture→Investment）。下流の実行動員は `playbooks/cross-project-program-management.md`（Gate 2）。本 Playbook は **どの順序で型をつなぐか** と **Gate 1 までの引継ぎ** を扱う。

## このPlaybookの目的

戦略立案からプロジェクト化までを任された担当者が、次の3つに自力で答えられるようにする。

1. 経営課題・IT課題をどう定義し、構造化するか（Chapter 2）
2. 現状分析から SCN（Value／Capability／Enabler）にどう分解するか（Chapter 3・4）
3. KPI をどう設定し、プロジェクト化まで持っていくか（Chapter 5〜7）

個々の型の詳細定義は最小限に留め、詳細は各原典を参照する。本 Playbook が担うのは **順序とつなぎ** である。

### 射程とシリーズ位置

扱うのは、経営戦略を所与として受け取ってから、SCN で構造化し、実行可能な単位（プロジェクト）に落とすまで。経営戦略そのものの意思決定（中計・M&A・事業ポートフォリオ入替等）は対象外。プロジェクト化後の複数ベンダー統合は②、実現化後の運用・定着化は③の対象。

```text
① 戦略立案・SCN Playbook（本書）
   戦略立案 → SCN → KPI → プロジェクト化（Gate 1）
                        │
                        ▼
② Cross-Project Management（`cross-project-program-management.md`）
   複数ベンダー・複数PJの実現化工程
                        │
                        ▼
③ Operations Transition Playbook（`playbooks/operations-transition-playbook.md`）
   AMS・インフラ運用・AI運用への移行設計と、実現化後の安定運用・定着化
```

ゴールは Chapter 7.4 の **Gate 1（Strategic Projectization Complete）**。Gate 2（Execution Mobilization Ready：体制図・WBS・契約スコープ等）は②の着手前チェック側。複数の相手（Sponsor・事業部等）を実際に動かす技術は、①②③共通の横串Playbook `playbooks/stakeholder-activation-playbook.md`（Stakeholder Activation Playbook）を参照する。

### 使い方

1. Chapter 1 で全体地図と②・③境界を掴む  
2. Chapter 2〜3 で問題定義と分析の上流型  
3. Chapter 4〜5 で SCN と KPI  
4. Chapter 6〜7 で評価〜Gate 1 引継ぎ  
5. Chapter 8 で工程横断の失敗パターンを確認  
6. Chapter 9 か実案件のどちらかで手を動かす（必須）

読むだけで終わらせない。

---

## Trigger

- IT／業務変革の「戦略資料はあるが Capability／Enabler／KPI／Project 単位まで落ちていない」
- メンティーがツールから手を動かし、Key Question に戻らない
- ②着手時に「何のための Project か／KPI が仮置き」で手戻りが出ている

## Objective

Gate 1 完了条件を満たす状態（Charter 骨子・Project 切り・検証可能な KPI・Sponsor 進行合意／未合意の明示）を作る。

## Prerequisites

- 承認済みまたは合意可能な戦略／中計／プログラム意図がある（戦略そのものの再訴訟は本 Playbook の主務ではない）
- 担当者は SCN・4Cs の記法を最低限知っている（未習なら `scn-creation-guide.md` を先に）
- 機密・金額・固有名詞は原本のみ。repo／共有テンプレには一般化のみ

## Required inputs

- Key Question の候補（未確定可）
- 現状の断片情報（インタビュー要約、リードタイム比較、システム棚卸し等）
- ステークホルダー一覧（意思決定者／抵抗要因の仮説）

## Escalation conditions

- Criteria／Constraints 未合意のまま分析が肥大化 → ワークショップをやり直す  
- Enabler（特に Technology）から書き始めている → Value に戻す  
- Gate 1 未充足のまま②へ引き渡し → 引継ぎを止める  
- 「契約しやすいから1 Project」だけで束ねている → 7.2 Health Assessment を強制

---

## Chapter 1. 全体像

### 1.1 なぜ一気通貫か

「良い戦略ができた」で仕事が終わったと錯覚すると絵に描いた餅になる。戦略は Capability と Enabler に分解し、誰が・何を・いつまでに実行するかが分かる単位まで落ちて初めて価値になる。

### 1.2 Consulting Strategy Process × IT戦略3段階

| Consulting Strategy Process | IT戦略3段階 | 本Playbook |
|---|---|---|
| 問題の設定と進め方の計画 | Insight（前半） | Chapter 2 |
| 問題を解く（分析） | Insight（後半） | Chapter 3 |
| 問題を解く（SCN） | Architecture | Chapter 4・5 |
| 提言を伝える | Architecture〜Investment | Chapter 6・7 |

IT戦略に別プロセスがあるわけではない。4Cs・ロジックツリー・SCN 等は共通で、その上に Architecture／Data／Security／Investment Governance 等の IT 固有論点を重ねる。SCN はビジネス–IT 整合用；IT 構造品質（使いやすさ・運用性・詳細 I/O）は SCN 単体では扱いきれない。

### 1.3 Why → What → How

| 階層 | 問い | 章 |
|---|---|---|
| Why | なぜこの変革が必要か | Chapter 2 |
| What | 何を実現するか（Value／Capability） | Chapter 4 |
| How | どう実現するか（Enabler／Project） | Chapter 5〜7 |

How（Enabler／Technology）から始めない。Pattern 1（`frameworks/thinking-patterns/pattern-01-why-what-how.md`）と一貫させる。

### レビュー用メモ

- [ ] Consulting Strategy Process の3段階を自分の言葉で言えるか  
- [ ] 今の案件がどの段階か言えるか  
- [ ] ②との境界（本書は Gate 1 まで）を説明できるか  

---

## Chapter 2. 問題を定義する

### 2.1 4Cs＆1Q

分析の前に Key Question を合意する。要素：Context／Client／Criteria／Constraints／Question。一度で終わらせず、関係者ごとに反復。Criteria と Constraints を先に決めると「立派だが採用されない提言」を防ぐ。

### 2.2 ロジックツリー

MECE に論点分解。Deductive／Hypothesis／Issue Map を習熟度と論点の具体性で選ぶ。描いた後「この枝を全部潰せば Key Question に答えられるか」を自問。

### 2.3 Analysis Plan

論点ごとに「どんな分析が・何のために・いつまでに」。End Product・担当・期限を先に決める。ストーリーボードと Work Plan まで合意すると分析が収束する。**Tool-first**（手元の枠から手を動かす）を禁止。

### レビュー用メモ

- [ ] Key Question を1文で言えるか  
- [ ] Criteria／Constraints を分析前に合意したか  
- [ ] 分析計画の各行が Key Question に接続しているか  

---

## Chapter 3. 現状分析と Findings

### 3.1〜3.3 ツール地図・データ収集・シナリオ

内部／外部／策定・評価の局面でツールを選ぶ（詳細は thinking-patterns 等）。インタビューは仮説生成／ハードデータ／視点検証の目的を先に決める。シナリオは変化が中〜大きいときだけ（静的市場に無理に作らない）。

### 3.4 分析の出口＝Findings

出口は分析の山ではなく、経営層向け **3〜5件の Findings**（Fact → Issue → Cause／Implication）。揃ったら Chapter 4 へ。

### 3.5 AI利用の原則（要約）

1. 箱（構造）を渡してから埋めさせる  
2. 比較軸を自分で決めてから複合検索させる  
3. 数値・固有名詞・引用は裏取り  
4. 機密を外部 AI に入れない（匿名化）

### レビュー用メモ

- [ ] ツールありきになっていないか  
- [ ] Findings が3〜5件に収束しているか  
- [ ] AI に構造なし丸投げしていないか  

---

## Chapter 4. SCN 構築

記法・WS・広がり／深さの詳細は `strategic-capability-network.md` / `scn-creation-guide.md`。ここではつなぎと失敗だけ。

### 4.1〜4.4 層の書き方（要約）

- **Value**: ステークホルダー／Value proposition／Outcome indicator  
- **Capability**: 「〜できる能力」、2〜3層、同一 KPI は統合  
- **Enabler (KOPT)**: Knowledge／Organization／Process／Technology。施策名を Enabler 上位に置きグルーピング  

### 4.5 As-Is → To-Be と Findings の再配置

ギャップをネットワーク上の欠落として可視化し、Chapter 3.4 の Findings を SCN ノードに位置づけ直す。

### 4.6 よくある失敗

- How（Technology）から書き始める  
- Capability 粒度が枝ごとにバラバラ  
- 早い段階で Enabler を描き込みすぎる  
- SCN を作って終わり（PDCA 背骨にしない）  
- IT 構造品質を無理に SCN に混ぜる  
- 単一プログラムで完結し Enterprise integration を怠る  
- Findings が観察の羅列で因果がない  

### レビュー用メモ

- [ ] Value から書けているか  
- [ ] As-Is→To-Be ギャップから Findings を言い切れるか  

---

## Chapter 5. KPI設計

| 層 | 指標 | 注意 |
|---|---|---|
| Value | Outcome | 効果目標 |
| Capability | Monitor | 使用量（ログイン数等）を成果にしない |

重要 Capability に絞る。Value Worksheet の3フィールドは「言葉」の整理。実行に渡す前に次を確定：

KPI名／種別（Outcome｜Monitor）／紐づく SCN Node／Baseline／Target／Formula／Data Source／Owner／Frequency

Baseline・Formula・Data Source が空ならまだ言葉の段階。財務評価指標（NPV 等）と PDCA 用 KPI を混同しない。

---

## Chapter 6. 解の評価と意思決定

- Needs vs Benefits；Diamond-E（環境／リソース／組織／経営意向／戦略）  
- オプションを Suitability／Feasibility／Acceptability で評価（都合の悪い制約も隠さない）  
- 実行テーマは重要度×実現可能性で優先順位  
- ステークホルダー：Awareness → Ownership。全員 Acceptance 待ちにしない；未合意は Risk／Assumption として記録してから進む（Gate 1 と同趣旨）

---

## Chapter 7. プロジェクト化（Gate 1）

### 7.1 分解

Vision → Strategic objectives → **Program**（SCN 単位）→ **Project**（Enabler の束）。SCN 上の施策名グルーピングが Project 候補になる。共有 Capability／Enabler の重複も確認（Enterprise integration）。

### 7.2 Projectization Health Assessment（事前予防）

②の「PJ境界が汚い」検知の **事前版**。1 Enabler 塊＝1 Project でよいか、次の観点で確認する。

| 観点 | 問い |
|---|---|
| Outcome | 同じ成果を目指すか |
| Ownership | 同じ責任者で管理できるか |
| Capability | 同じ Capability の塊か |
| Dependency | 内部依存が高く外部依存が低いか |
| Architecture | 技術的に独立か |
| Release | 同じタイミングでリリース可能か |
| Contract | 同じ契約が合理的か（**これだけで束ねない**） |
| Change | 同じ組織・業務への変革として扱えるか |

No が多い／Contract だけ Yes → 分割を検討。

### 7.3 Program Charter 骨子

目的／スコープ／体制（Sponsor・Business Owner・Program Owner まで；実行 PJ 体制図は Gate 2）／KPI／マイルストーン。詳細 WBS は書かない。

### 7.4 Gate 1 / Gate 2

| Gate | 内容 | 担い手 |
|---|---|---|
| **Gate 1** Strategic Projectization Complete | なぜ／何を／どの Project に分けるか／KPI／Scope 概要／Sponsor・Owner | ①（本書） |
| **Gate 2** Execution Mobilization Ready | ベンダー／体制図／WBS／契約スコープ／マスタースケジュール | ②着手前チェック |

**Gate 1 完了条件**

- [ ] Charter 5項目が埋まっている  
- [ ] 7.2 を通過している  
- [ ] KPI の Baseline・Formula・Data Source が確定  
- [ ] Sponsor から進行合意。抵抗・未合意は Risk／Assumption として明示  

Gate 2 情報が①時点で未確定なのは正常。

---

## Chapter 8. つまずきやすいポイント（工程横断）

| 症状 | 対策の要点 | 章 |
|---|---|---|
| クライアントが症状の話ばかり | 4Cs＆1Q をやり直す | 2.1 |
| 論点が思いつき | 先に MECE ツリー | 2.2 |
| 枠のスライドはあるが So What がない | すべて Key Question に接続 | 2.3・3.1 |
| スコープが際限なく広がる | End Product を先に決める | 2.3 |
| 提言が採用されない | Criteria を分析前に合意 | 2.1・6.1 |
| シナリオを単一予測扱い | 複数シナリオでオプションをテスト | 3.3 |
| Technology から書く | Value から降りる | 1.4・4.6 |
| SCN が更新されない | KPI とセットで見直し運用を決める | 4.6・5 |
| Findings が主張の羅列 | Fact→Issue→因果を SCN ノードへ | 3.4・4.5 |
| 契約都合だけで1 Project | 7.2 の8観点 | 7.2 |
| ②で Landscape が埋まらず前提待ち | Gate 1 完了条件を満たしてから引継ぎ | 7.4 |

---

## Chapter 9. 実践演習（パターン）

**ケース型（一般化）**: 中堅製造業の DX／生産対応力再構築。複数工場・ばらばらな生産管理・熟練依存・小ロット短納期圧力、など。売上高・社名・固有事実は案件ごとに差し替え（金額は repo に載せない）。

**Data Pack（断片情報の型）**: 工場別リードタイム比、システム棚卸し、熟練者年齢構成、顧客要求変化、経営者／工場長コメント要約。

**Session 1（90分）**: 4Cs → ツリー → Analysis Plan → Findings 3件 → SCN（Value→Capability→KOPT）  
**Session 2（90分）**: KPI → Suitability／Feasibility／Acceptability → Program／Project 分解 → 7.2 → Charter → Gate 1 チェック  

ゴールは SCN 完成ではなく **Gate 1 を満たす Charter** まで。参考解答は観点チェック用；先に見せない。

---

## Sequence（コーチング要約）

1. Key Question（4Cs＆1Q）を合意する  
2. ロジックツリーで論点を MECE 化する  
3. Analysis Plan（End Product 付き）を立てる  
4. 分析し Findings 3〜5件に収束させる  
5. SCN を Value → Capability → Enabler の順で書く  
6. 検証可能な KPI を重要ノードに紐づける  
7. オプション評価とステークホルダー進行合意  
8. Projectization Health Assessment のうえ Charter を埋める  
9. Gate 1 完了条件を満たしてから②へ渡す  

## Decision points

- シナリオをやるか（変化の大きさ）  
- どの Capability に KPI を付けるか  
- Project の切り方（7.2）  
- Gate 1 未充足なら引き渡し延期  

## Quality checks

- How から始めていない  
- Findings が因果連鎖で SCN ノードに載っている  
- KPI が言葉だけでない  
- Contract 単独で Project を束ねていない  
- Gate 1／Gate 2 境界を説明できる  

## Outputs

- 4Cs＆1Q／Logic Tree／Analysis Plan  
- Finding Sheet（SCN Node 付き）  
- SCN Canvas／Value Worksheet／KPI 設計  
- Option Evaluation／Program Charter 骨子  
- Gate 1 完了チェック結果  

## Limitations

経営戦略の最終意思決定そのもの、SCN 記法の百科事典、IT 構造品質アセスメント、複数ベンダーの PJ 間 Control、運用定着化は対象外。

---

## Appendix：テンプレートクラス（xlsx は commit しない）

ローカル `Strategy-SCN-Playbook-Templates.xlsx` のシートを、クラス／フィールドのみ登録。サンプル行の案件数値・社名は載せない。Optional: Scenario Canvas（Ch3.3、変化が中〜大の案件のみ）。

| No. | Class | Chapter | Fields |
|---|---|---|---|
| 1 | **4Cs＆1Q Worksheet** | 2.1 | Context, Client, Criteria, Constraints, Question（記入欄） |
| 2 | **Logic Tree／Issue Map** | 2.2 | ID, 親ID, 論点（Issue）, ツリー種別（Deductive｜Hypothesis｜Issue Map）, 備考 |
| 3 | **Analysis Plan** | 2.3 | 論点, 必要な分析, 分析手法, 成果物（End Product）, 担当, 期限, 備考 |
| 4 | **Finding Sheet** | 3.4 | ID, Fact, Issue, Cause／Implication, SCN Node, 備考 |
| 5 | **Value Worksheet** | 4.2・5.2 | ステークホルダー, Value proposition, Outcome indicator, 備考 |
| 6 | **SCN Canvas** | 4 | Layer（Value｜Capability｜Enabler）, ノード名, 親ノード, KOPT種別（Enablerのみ）, 備考 |
| 7 | **KPI設計シート** | 5 | KPI名, 種別（Outcome｜Monitor）, 紐づくSCN Node, Baseline, Target, Formula, Data Source, Owner, Frequency, 備考 |
| 8 | **Option Evaluation Matrix** | 6.2 | 戦略オプション, Suitability, Feasibility, Acceptability, 総合判定, 備考 |
| 9 | **Program Charter骨子** | 7.3 | 目的, スコープ, 体制（Sponsor／Business Owner／Program Owner）, KPI, マイルストーン |

テンプレートは本文とセットで使う。Excel だけ渡して自走させない。

---

## Related

- `frameworks/consulting-strategy-process.md`  
- `frameworks/strategic-capability-network.md`  
- `standards/scn-creation-guide.md`  
- `frameworks/it-strategy-foundations.md`  
- `frameworks/capability-model.md`  
- `frameworks/thinking-patterns/pattern-01-why-what-how.md`  
- `playbooks/cross-project-program-management.md`（Gate 2／PJ間）  
- `playbooks/operations-transition-playbook.md`（③／運用移行・定着化）  
- `playbooks/stakeholder-activation-playbook.md`（①②③共通／Stakeholderを動かす技術）  
- Program Line D（SCN legacy）＋本コーチングパック（2026）
