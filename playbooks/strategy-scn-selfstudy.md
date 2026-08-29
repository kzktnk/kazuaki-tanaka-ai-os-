---
type: playbook
---

# Strategy / SCN Playbook【自己学習版】

**Version:** v0.3  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** 戦略立案（IT戦略を含む）から SCN 構造化・KPI・プロジェクト化（Gate 1）までを、一人で読み進めながら自走できる順序でつなぐ  
**Use when:** 経営課題／IT課題の定義→分析→SCN→KPI→Program／Project 分解までを一気通貫で、自分の案件に当てはめるとき  
**Do not use as-is for:** SCN 記法・WS 運営の詳細（別紙の記法ガイド）、型の定義本体（原典フレームワーク）、複数ベンダー PJ 間統合（②）、運用・定着化（③）、Stakeholder を実際に動かす技術（横串）  
**Source:** ①本編（`playbooks/strategy-scn.md`）の自己学習版。2026-08-29。主張・型・表・演習は本編と同一。

本 Playbook は、SCN の記法や型の定義そのもの（原典）ではなく、**どの順序で型をつなぐか**と**Gate 1 までの引継ぎ**を扱う。下流の実行動員は②（Gate 2）。

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
② Cross-Project Program Management
   複数ベンダー・複数PJの実現化工程
                        │
                        ▼
③ Operations Transition Playbook
   AMS・インフラ運用・AI運用への移行設計と、実現化後の安定運用・定着化
```

シリーズ全体は、次の Gate 1〜5 でつながっている（詳細は③ Chapter 1.3）。本書が担うのは Gate 1 のみである。

```text
Gate 1            Gate 2              Gate 3               Gate 4                Gate 5
Strategic     →  Execution       →   Service Transition →  Responsibility   →   Steady State
Projectization    Mobilization        Planning Ready        Transfer Ready        Accepted
Complete          Ready
  (①完了)          (②着手)             (②③並走開始)          (③へ責任移転)          (③終了)
```

ゴールは Chapter 7.4 の **Gate 1（Strategic Projectization Complete）**。Gate 2（Execution Mobilization Ready：体制図・WBS・契約スコープ等）は②の着手前チェック側。①②だけを読むとシリーズが Gate 2 で終わるように見えるが、実際は②③が Gate 3 から並走し、Gate 5 まで続く。複数の相手（Sponsor・事業部等）を実際に動かす技術は、①②③共通の横串Playbook（Stakeholder Activation Playbook）を参照する。

### 使い方

1. Chapter 1 で全体地図と②・③境界を掴む  
2. Chapter 2〜3 で問題定義と分析の上流型  
3. Chapter 4〜5 で SCN と KPI  
4. Chapter 6〜7 で評価〜Gate 1 引継ぎ  
5. Chapter 8 で工程横断の失敗パターンを確認  
6. Chapter 9 か実案件のどちらかで手を動かす（必須）

読むだけで終わらせない。各Chapter末の振り返りメモは、指導者に問われて答えるものではなく、自分自身に問いかけるものとして使う。答えに詰まった項目があれば、そこが理解の甘い場所である。一人で判断がつかない場合は、無理に自己完結させず、先輩・上司に短く相談してよい。

---

## Trigger

- IT／業務変革の「戦略資料はあるが Capability／Enabler／KPI／Project 単位まで落ちていない」
- ツールから手を動かしてしまい、Key Question に戻れていない
- ②着手時に「何のための Project か／KPI が仮置き」で手戻りが出ている

## Objective

Gate 1 完了条件を満たす状態（Charter 骨子・Project 切り・検証可能な KPI・Sponsor 進行合意／未合意の明示）を作る。

## Prerequisites

- 承認済みまたは合意可能な戦略／中計／プログラム意図がある（戦略そのものの再訴訟は本 Playbook の主務ではない）
- 担当者は SCN・4Cs の記法を最低限知っている（未習なら別紙の記法ガイドを先に）

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

How（Enabler／Technology）から始めない。Why→What→How の思考パターンと一貫させる。

### 振り返りメモ（自己学習用）

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

### 振り返りメモ（自己学習用）

- [ ] Key Question を1文で言えるか  
- [ ] Criteria／Constraints を分析前に合意したか  
- [ ] 分析計画の各行が Key Question に接続しているか  

---

## Chapter 3. 現状分析と Findings

### 3.1 ツール地図

内部／外部／策定・評価の3局面でツールを使い分ける（型の詳細は原典・指導者を参照）。

| 局面 | 主なツール | 見るもの |
|---|---|---|
| 内部（Company） | 7S、バリューチェーン、コアコンピタンス | 自社の強み・制約 |
| 外部（Customer／Competitive） | セグメンテーション、5 Forces、ポジショニングマップ | 市場・競合の構造 |
| 策定・評価 | シナリオ、Suitability／Feasibility／Acceptability | オプションの選定（Chapter 6） |

**よくある失敗**：Key Question を決める前にツール一覧から選び始める（Tool-first）。ツールは Key Question に答えるための手段である。枠を埋めることが目的化すると、精緻だが誰の意思決定にも効かない資料ができあがる。

### 3.2 データ収集

インタビューは目的を先に決めてから設計する。

| 目的 | 使うとき |
|---|---|
| 仮説生成 | 分析初期、論点の見当がついていない段階 |
| ハードデータ補完 | 定量分析だけでは埋まらない実態確認 |
| 視点検証 | 提言前の抜け・盲点・政治的実現性の確認 |

インタビュー順は、経営層 → 実務・営業層 → 業界専門家 → 顧客 → 販売代理店 → 代替品提供者 → 競合 → サプライヤーが基本形。

**よくある失敗**：目的を決めずに「とりあえず聞く」。後から「これは仮説生成だったのか検証だったのか」が本人にも分からなくなり、聞いた内容を Findings（3.4）に落とせない。

### 3.3 シナリオ

業界・市場の変化が中〜大きいときだけ使う（静的市場に無理に作らない）。10ステップの詳細は原典を参照。

**よくある失敗**：シナリオを「当たる未来を1つ予測するもの」として扱う（Chapter 8 参照）。シナリオの目的は単一予測ではなく、複数の未来それぞれでオプションが機能するかをテストすることである（Chapter 6 のオプション評価と接続）。

### 3.4 分析の出口＝Findings

出口は分析の山ではなく、経営層向け **3〜5件の Findings**（Fact → Issue → Cause／Implication）。揃ったら Chapter 4 へ。

### 3.5 AI利用の原則（要約）

1. 箱（構造）を渡してから埋めさせる  
2. 比較軸を自分で決めてから複合検索させる  
3. 数値・固有名詞・引用は裏取り  
4. 機密を外部 AI に入れない（匿名化）

### 振り返りメモ（自己学習用）

- [ ] ツールありきになっていないか  
- [ ] インタビューの目的（仮説生成／ハードデータ／視点検証）を先に決めてから設計したか  
- [ ] シナリオを単一予測として扱っていないか  
- [ ] Findings が3〜5件に収束しているか  
- [ ] AI に構造なし丸投げしていないか  

---

## Chapter 4. SCN 構築

記法・WS・広がり／深さの詳細は原典フレームワーク・記法ガイドを参照。ここではつなぎと失敗だけ。

### 4.1 層の全体像

SCN は Value → Capability → Enabler の3層で構成する。Findings（3.4）を、この3層のどこに位置づけ直せるかが Chapter 4 の仕事である。上位層（Value）から下ろす。Enabler、特に Technology から書き始めない。

### 4.2 Value

ステークホルダー／Value proposition／Outcome indicator の3点で書く。

**よくある失敗**：「業務効率化」のような抽象語で止める。抽象的な表現は Capability 層に降ろし、Value 自体は誰にとって何が良くなるかが読み手に伝わる具体性を持たせる。同じ Value が複数箇所に現れた場合は、ステークホルダー別か内容別かで統合または分割する。

### 4.3 Capability

「〜できる能力」の形で書く。2〜3層まで。同一 KPI に紐づく Capability は統合する。

**よくある失敗**：枝によって Capability の粒度がバラバラになる（ある枝は部門レベル、別の枝は作業レベル）。粒度は SCN 全体で揃え、細かすぎる枝は上位に括り直す。

### 4.4 Enabler（KOPT）

Knowledge／Organization／Process／Technology の4種で分解する。施策名は Enabler の上位に置き、個別 Enabler をその下にグルーピングする。

**よくある失敗**：Chapter 4 の早い段階から Enabler、特に Technology の詳細（画面・I/O）まで描き込む。SCN はビジネス–IT 整合の地図であり、IT 構造品質（使いやすさ・運用性）の検討はここでは扱わない。IT 詳細が出てきたら「これは SCN か、それとも下流の要件定義か」を自問する。

### 4.5 As-Is → To-Be と Findings の再配置

ギャップをネットワーク上の欠落として可視化し、Chapter 3.4 の Findings を SCN ノードに位置づけ直す。

### 4.6 よくある失敗（層をまたぐもの）

- SCN を作って終わり（PDCA 背骨にしない）  
- 単一プログラムで完結し Enterprise integration を怠る  
- Findings が観察の羅列で因果がない  

### 振り返りメモ（自己学習用）

- [ ] Value から書けているか  
- [ ] Value・Capability の粒度が SCN 全体で揃っているか  
- [ ] Enabler の詳細まで早期に描き込んでいないか  
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
- ステークホルダー：Unawareness → Awareness → Buy-in → Ownership（業界のチェンジマネジメント標準と共通の Commitment 段階。②③横串とも同じ4段階を使う）。Gate 1 で必要なのは Sponsor の Buy-in までの進行合意であり、Ownership（自分ごと化）まで揃うのは通常②③以降である。全員 Acceptance 待ちにしない；未合意は Risk／Assumption として記録してから進む（Gate 1 と同趣旨）

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

**②2.7（プログラム構造のHealth Assessment）との対応**

7.2 は Gate 1 時点の**事前予防**、②2.7 は実現化工程に入ってからの**事後検知**である。7.2 で以下の軸を甘く判定すると、②2.7 が検知する「PJ境界が汚い」状態として跳ね返ってくる。

| 7.2 の観点（本書） | 甘く判定した場合に②2.7で現れる症状 |
|---|---|
| Architecture（技術的に独立か） | 契約単位とシステム単位が一致せず、1契約の中に独立したサブシステムが混在する |
| Contract（同じ契約が合理的か） | 「契約しやすいから」で束ねた箇所が、②の「汚い」構造のサインとして検出される |
| Dependency（内部依存が高く外部依存が低いか） | PJ内サブシステム間の連携密度が、PJ間の連携密度より高くなる |
| Release（同じタイミングでリリース可能か） | 独立してテスト・リリースできるはずのサブシステムが、1つのリリース単位に縛られる |

Outcome／Ownership／Capability／Change の4軸は主に業務・組織側の切り方を扱うため、②2.7では再検証しない（②2.7が扱うのは技術的・契約的な境界のみ）。7.2 で Architecture／Contract／Dependency／Release のいずれかに No が残ったまま Gate 1 を通すと、②側での手戻りが大きい。

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
| Technology から書く | Value から降りる | 4.1・4.4 |
| SCN が更新されない | KPI とセットで見直し運用を決める | 4.6・5 |
| Findings が主張の羅列 | Fact→Issue→因果を SCN ノードへ | 3.4・4.5 |
| 契約都合だけで1 Project | 7.2 の8観点 | 7.2 |
| ②で Landscape が埋まらず前提待ち | Gate 1 完了条件を満たしてから引継ぎ | 7.4 |

---

## Chapter 9. 実践演習

**ケース**：老朽化した基幹システムの刷新。20年以上稼働し、担当者の高齢化とブラックボックス化が進んでいる。外部連携は個別I/F実装の積み重ねで保守コストが増加。複数事業のデータが基幹・周辺システムに分散し、経営判断に必要な統合データがすぐに得られない。周辺システムの一部は、既存ベンダーX社が長年個別に運用している。売上高・社名・固有事実は案件ごとに差し替え（金額は伏せる）。

**Data Pack（断片情報の型）**：基幹システムの保守コスト推移（5年で1.4倍）、外部連携I/Fの数と個別対応履歴（32本、うち20本がこの3年で追加）、システム構成の暫定棚卸し（基幹システム＋周辺システム6本、うち1本はX社が個別運用）、基幹システム有識者の年齢構成（主要担当者3名中2名が55歳以上）、経営層コメント要約（「今のシステムで次の中計は支えられるのか」）。

### Session 1（90分）：4Cs → ツリー → Analysis Plan → Findings 3件 → SCN

**4Cs＆1Q の記入例**

| 要素 | 内容 |
|---|---|
| Context | 基幹システムが20年以上稼働し老朽化。外部連携は個別対応の積み重ねで保守コストが増加。経営データが分散し統合的な判断ができない |
| Client | 情報システム部門長（Sponsor：担当役員） |
| Criteria | 事業を止めない移行、外部連携の標準化、次期中計を支えるデータ活用基盤 |
| Constraints | 投資上限、稼働中システムを止められない、基幹システム知識の属人化、既存ベンダーX社との契約関係 |
| Question | 限られた投資と移行リスクの中で、基幹システムをどう刷新すれば、次期中計を支えるデータ活用基盤に転換できるか |

**Findings の記入例（3件）**

1. 保守コストが5年で1.4倍に増加し、有識者3名中2名が55歳以上（Fact）→現行維持コストの増加が続き、技術継承が崩れる前に手を打つ必要がある（Issue／Implication）
2. 外部連携I/F 32本中20本がこの3年で個別追加（Fact）→標準化されたI/F基盤がないまま刷新すると、同じ問題を再生産する（Issue）
3. 基幹・周辺システムにデータが分散し、経営会議向けレポートに手作業の突合が必要（Fact）→刷新の価値を「システムの入れ替え」ではなく「データ活用基盤への転換」に置かないと、経営が刷新の意義を認識しない（Issue）

**SCN の記入例（要約）**

- Value：迅速な事業判断を支えるデータ活用／変化に強い基幹業務基盤／外部連携の俊敏性
- Capability：統合的な基幹業務処理能力／標準化された外部連携能力／データ移行・活用能力／複数ベンダー横断のテスト・品質保証能力
- Enabler（KOPT）：新基幹システム・標準I/F基盤・データ移行基盤（Technology）／業務要件定義・BPR、テスト・移行リハーサル手順（Process）／PMO・テスト統括体制（Organization）／基幹業務知識の形式知化（Knowledge）

想定される「抜けやすいポイント」：Finding 3（データ分散）を Capability 層に落とさず Value のまま止めてしまう。「データ活用能力」という Capability まで分解できているかを確認する。

### Session 2（90分）：KPI → Suitability／Feasibility／Acceptability → Program／Project 分解 → 7.2 → Charter → Gate 1 チェック

**KPI の記入例**

| KPI名 | 種別 | Baseline／Target（例） |
|---|---|---|
| 新機能リリースリードタイム | Outcome | 現状比で短縮（数値は案件ごとに設定） |
| 経営レポート作成工数 | Outcome | 手作業突合の削減 |
| 外部連携I/Fの標準化率 | Monitor | 個別実装比率の低下 |

**オプション評価の記入例**

- Suitability：Key Question（データ活用基盤への転換）に適合するか
- Feasibility：4ベンダー体制のコントロール難度、稼働中システムを止めない移行の技術的実現性
- Acceptability：55歳以上の有識者2名の協力が得られるか、既存ベンダーX社との関係

**ステークホルダー進行合意の記入例**：Sponsor（担当役員）は Buy-in まで到達。既存ベンダーX社を管掌する部門はまだ Awareness 段階。Gate 1 では全員の Buy-in を待たず、後者は Risk／Assumption として記録したうえで進む（Chapter 6）。

**7.2 Health Assessment を通した Project 分解の記入例**

「基幹システム刷新」を1つの Project で束ねようとすると Contract 軸以外で No が並ぶため、次の5 Project に分割する。

| Project | 中身 | 7.2 判定の要点 |
|---|---|---|
| PJ-A | 業務要件定義・BPR | Outcome／Capability が他と独立。要件を握る主体は基幹システム開発の主体と同一である必要はない |
| PJ-B | 基幹システム本体の設計・開発 | Ownership／Architecture の中核。技術的に最も独立性が高い |
| PJ-C | 外部連携・周辺システムI/F | Capability が独立（標準I/F基盤の専門性）。ただし PJ-B への Dependency が高い |
| PJ-D | データ移行 | Dependency は高いが、専門スキル（移行ツール・データクレンジング）が別（Capability） |
| PJ-E | テスト統括・移行リハーサル | 全 Project 横断。特定の実行主体に持たせると Change の中立性を欠くため、社内／PMO 兼任とする |

既存ベンダーX社が運用する周辺システムは、契約更改の時期が基幹刷新と重なるが、Capability／Ownership の観点で PJ-C とは切り離せると判定し、Gate 1 時点の Project Scope には含めない。契約更改後の運用移行は、③（Transition Manager）が扱うシナリオB として引き継ぐ。**これは「今すぐ全部やる」ではなく「Gate 1 の射程を正しく引く」判断であり、7.2 の Contract 軸だけで束ねない原則の実例でもある。**

**Charter 骨子の記入例**：目的（データ活用基盤への転換）／スコープ（PJ-A〜E）／体制（Sponsor＝担当役員）／KPI（上表）／マイルストーン。

**Gate 1 完了条件チェック**：Charter 5項目が埋まっている／7.2 を通過している／KPI の Baseline・Formula・Data Source が確定／Sponsor から Buy-in（進行合意）。既存ベンダーX社側の Awareness／Buy-in 未達は Risk として明示済み。

ゴールは SCN 完成ではなく **Gate 1 を満たす Charter** まで。参考解答は観点チェック用；先に見せない。

Gate 1 完了後、この Charter がそのまま②Chapter 9 の演習ケース（PJ-A〜E）の出発点になる。①で「なぜこの5分割か」を自分で組み立てた読み手は、②で「この5つの間をどう管理するか」に入ったときも、Project の切り方自体を疑わずに済む。既存ベンダーX社の周辺システムは、③Chapter 8 の演習（シナリオB）で再登場する。

---

## Sequence（要約）

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

- 戦略プロセスの原典フレームワーク（問題設定〜提言）
- SCN 本体の原典フレームワークと記法ガイド
- ②（Cross-Project Program Management Playbook／Gate 2・PJ間）
- ③（Operations Transition Playbook／運用移行・定着化）
- 横串（Stakeholder Activation Playbook／①②③共通）
