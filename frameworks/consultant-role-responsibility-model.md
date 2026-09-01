---
type: framework
title: "Strategy Consultant Role Model ― Role／Responsibility層（v0.3 ― 構造確定・Pilot移行）"
source: "frameworks/consultant-capability-skill-model.md（v0.6、Capability IVを統合済み）の上位層。v0.1へのレビューを反映しv0.2化（Legal/Regulatory L2化、Skill/Knowledge原則修正）。v0.2へのレビューを反映し、Governance/ManagementのRequired LevelをL2に修正、Capability I〜IIIのRequired Levelを補完、v0.5世代の残存表記を整合（v0.3）。"
status: draft
extracted: false
gap_fill: "Capability IVの6 Skill本体（Prerequisite Knowledge・L0→L4 Evidence・Learning/OJT）はframeworks/consultant-capability-skill-model.md（v0.6）側に統合。本ファイルはRole／Responsibility層とRequired Levelの一覧に特化する。構造検討はv0.3で終了し、以降はPilotで発生した運用上の問題のみを入力とする。"
related:
  - frameworks/consultant-capability-skill-model.md（v0.6、Capability IV統合済み）
  - frameworks/pilot-assessment-strategy-consultant.md（Pilot実施用ワークシート）
  - playbooks/strategy-scn.md
last_updated: 2026-09-01
---

# Strategy Consultant Role Model
## ― Role／Responsibility層（v0.3 ― 構造確定・Pilot移行） ―

**Status:** 構造検討は終了。次は実在メンバー1名によるPilot（24 Skill、`frameworks/pilot-assessment-strategy-consultant.md`使用）。以降はPilotで発生した運用上の問題のみを次版への入力とする

## 変更履歴

**v0.2→v0.3**（今回）：

1. **Corporate Governance／ManagementのRequired LevelをL1→L2に修正**：「Governance／Escalationと重複するから軽くする」という判断を撤回した。両者は問い自体が異なる（Corporate Governance／Management＝実際に誰が・なぜ決めるのか＝Business Literacy、Governance／Escalation＝その人へどう決裁・エスカレーションを流すか＝Delivery／Stakeholder Skill）。この結果、Capability IVの6項目は全てRequired Level L2で揃った（§5.3）
2. **Capability I〜IIIのRequired Levelを補完**（§5.4）：Pilotの「Role Required Level Gap」ステップを実際に計算可能にするため、既存18 SkillについてもStrategy ConsultantとしてのRequired Levelを指定した。Capability II（Delivery／Execution）はほぼ全滅L0（対象外）――Gate 1までを担うStrategy Consultantには、個別PJ実行管理のSkillは不要という判断
3. **v0.5世代の残存表記を整合**：`consultant-capability-skill-model.md`側の「3系統」「18 Skill、全展開」を「4系統」「24 Skill、全展開」に修正（v0.5→v0.6統合時の残骸）
4. **構造検討ラウンドを終了**：これ以上机上でSkillを追加せず、Pilotで見つかった運用上の問題だけを次版のインプットにする

**v0.1→v0.2**：Role→Responsibility→Capability構造を確定、Skill／Knowledgeの二重Level管理をやめてPrerequisite Knowledge方式へ、「Skillは常にL0〜L4・RoleがRequired Levelを決める」原則を明示、Commercial／Contract LiteracyとRegulatory／Risk LiteracyのRequired LevelをL1→L2に修正、Capability IVの6 Skillをフル展開して`consultant-capability-skill-model.md`（v0.6）に統合。

---

## 0. 位置づけ

`frameworks/consultant-capability-skill-model.md`（v0.5）は、Capability I〜III・18 Skillまでを扱う。今回はその**上位**に、次の4層構造を検証する。

```text
Role（Mission・Responsibility）
        │
        ▼
Capability（I〜III、必要ならIV）
        │
        ▼
Skill／Knowledge
        │
        ▼
Level／Evidence（既存18 Skillはv0.5のまま。新設分はこの段階では作らない）
```

v0.5の18 Skill・Level・Evidenceはベースラインとして**一切変更していない**。本ファイルは新しいレイヤーの追加提案であり、既存部分への変更ではない。

---

## 1. Role：Strategy Consultant

### Mission

クライアントの経営課題・IT課題を構造化し、検証可能なKPIを伴う戦略とSCNに落とし込み、実行可能な単位（Program／Project）まで分解して、Gate 1（Strategic Projectization Complete）の状態で②へ引き継ぐ。

### Responsibility（主要な説明責任）

| # | Responsibility |
|---|---|
| R1 | 経営課題・IT課題を定義し、構造化する（Key Question、ロジックツリー） |
| R2 | 現状分析からFact→Issue→仮説→Findingsを構築する |
| R3 | SCN（Value／Capability／Enabler）を設計する |
| R4 | 検証可能なKPIを設計する（Baseline／Target／Formula／Data Source） |
| R5 | 戦略オプションを評価し、実行可能な単位（Program／Project）に分解する |
| R6 | 経営層・キーパーソンとの関係を構築し、提言をOwnershipまで導く |
| R7 | 分析・提言を、クライアントの事業実態（財務・ビジネスモデル・投資判断・ガバナンス・契約・規制環境）に照らして妥当なものにする |
| R8 | Gate 1完了条件を満たし、②への引き継ぎを成立させる |

---

## 2. Responsibility → Capability マッピング

| Responsibility | マッピング先 | カバー状況 |
|---|---|---|
| R1 | Capability I／問いを立てる、構造化する | 充足 |
| R2 | Capability I／仮説を作る、分析する | 充足 |
| R3 | Capability I／構造化する（SCN固有の記法・ワークショップ運営自体は`standards/scn-creation-guide.md`が別途カバー、Capability IIIのFacilitationとも接続） | 概ね充足 |
| R4 | Capability I／構造化する、評価・意思決定する | **部分充足**（後述） |
| R5 | Capability I／評価・意思決定する | 充足 |
| R6 | Capability III／Stakeholder Diagnosis、Communication、Influence／Activation | 充足 |
| R7 | ― | **未充足（Gap）** |
| R8 | R1〜R7の統合結果として、Capability I（評価・意思決定するのGate 1関連判断）とCapability III（Governance／EscalationのSponsor合意形成）の組み合わせ | 概ね充足（単独のCapabilityにマッピングされる性質のものではない） |

### R4についての補足（小さな部分Gap）

KPI設計（Baseline／Formula／Data Source／Owner／Frequencyを確定させる作業）は、「構造化する」の型と「評価・意思決定する」のS／F／A的判断の組み合わせで大部分をカバーできるが、KPI設計固有の型（Outcome指標とMonitor指標の使い分け等）を独立のSkillとして持つべきかは、将来的な検討課題として残す。今回はBusiness／Management Literacyほど大きな欠落ではないため、深掘りの対象からは外す。

---

## 3. Gap：R7「Business / Management Literacy」

Capability I〜IIIは、**考え方・進め方の型（プロセス・技法）**を扱っている。Key Questionの立て方、SCNの構造化の仕方、S／F／Aでの評価の仕方――これらはどんな業界・どんなクライアントでも共通して使える型である。

しかし、その型を**具体的なクライアントの実態に正しく当てはめる**には、型とは別に、クライアントの事業を理解するための実務知識が要る。財務諸表が読めなければ「現状分析」は表面的になり、投資判断のロジックを知らなければ「Program Charter骨子」のKPIは絵に描いた餅になる（実際、`playbooks/strategy-scn.md` Ch5には「財務評価指標（NPV等）とPDCA用KPIを混同しない」という一文があり、この区別ができる前提の記述になっているが、その前提を教える教材は存在しない）。

この「型を実際のクライアントに正しく当てはめるための事業実務知識」が、Capability I〜IIIのどこにも属さないResponsibility（R7）として残る。

---

## 4. 「Skill」と「Prerequisite Knowledge」の関係（v0.1から修正）

v0.1では Skill と Knowledge を並列の二軸でLevel管理する案を出したが、レビューで指摘の通りこれは管理が複雑になりすぎる。修正後の原則は次の通り。

- **Levelを持つのはSkillだけ**：L0〜L4は既存18 Skillと共通の定義（`consultant-capability-skill-model.md` §2）をそのまま使う
- **Knowledgeは各SkillのPrerequisite**として位置づけ、Pass／Not Yetの二値で管理する（Level化しない）。例：Company／Financial Analysisという1つのSkillに対し、「PL／BS／CFの構造を知っているか」「三表のつながりを説明できるか」といったPrerequisite Knowledgeの一覧を持たせ、それが一通りPassしていることをL0→L1の前提とする
- **SkillはL0〜L4まで常に定義可能**。「このSkillはL2までしか要らない」という判断は、Skillの定義を削るのではなく、**Role側がRequired Levelとして指定する**ことで表現する。これにより、将来別のRole（例：M&A Strategy）が同じFinancial Analysis SkillにL3を要求する、といった拡張が構造を壊さずにできる

Capability IVの6 Skillの本体（Prerequisite Knowledge・L0→L4 Evidence・Learning／OJT・判定者）は、`frameworks/consultant-capability-skill-model.md`（v0.6）の「3.4 Capability IV｜Business / Management Literacy」に統合した。以下§5.2は、Roleの視点からの要約（Required Levelの一覧）に絞る。

---

## 5. Business / Management Literacyの詳細検討

### 5.1 スコープの前提（指定された絞り込み）

- **法律領域**：専門家として法的判断を下すことは範囲外とする。論点を発見し、Business Impactを考え、Legal等の専門家に確認すべきQuestionへ変換できることを中心に置く
- **財務領域**：深い財務分析・モデリングの専門性ではなく、経営層との会話が成立し、経営課題の仮説形成に使える実務能力として扱う

### 5.2 6候補の評価（v0.2 ― Required Level修正版）

法律・規制系の2項目について、v0.1では「範囲が狭い（法的判断はしない）」ことを理由にRequired LevelをL1としたが、これは誤りだった。**範囲の狭さとLevelの高さは別軸である。** 「論点を自力で発見し、Business Impactを整理し、専門家へのQuestionとして自分の力でまとめる」のは、指導下（L1）ではなく自走（L2）の定義そのものに該当する。「法的結論を出す」ことは全Levelを通じてScope外のままだが、「論点を発見する」ことはL2を要求する。

| # | 候補 | ①Capabilityとして必要か | ②構成 | ③Strategy ConsultantのRequired Level |
|---|---|---|---|---|
| 1 | Company／Financial Analysis | 必要。ほぼ全案件でクライアントの財務状況を踏まえた会話が発生する | Skill＋Prerequisite Knowledge（PL/BS/CF構造、三表のつながり、主要指標等） | **L2** |
| 2 | Business Model／Economics | 必要。SCNのValue／Capability層の精度は、事業経済性の理解に直結する | Skill＋Prerequisite Knowledge（収益モデル類型、コスト構造、Unit Economics等） | **L2** |
| 3 | Investment／Business Case | 必要。Program Charter骨子のKPI・投資ロジックが、この理解なしでは絵に描いた餅になる（`strategy-scn.md` Ch5の既知の前提） | Skill＋Prerequisite Knowledge（NPV/IRR/Payback、投資指標とPDCA用KPIの違い等） | **L2** |
| 4 | Corporate Governance／Management | 必要。**L1から修正**：Skill本体のL2定義（真のSponsor・decision makerと権限範囲を自力で特定）は、Strategy ConsultantのR6（提言をOwnershipまで導く）・R8（Gate 1を成立させる）に照らして必要である。「Governance／Escalationと重複するから軽くする」という前回の判断は誤りだった。両者は問いが違う：Corporate Governance／Management＝「実際に誰が・なぜ決めるのか」（Business Literacy）、Governance／Escalation＝「その人へどう決裁・エスカレーションを流すか」（Delivery／Stakeholder Skill）。重複ではなく相互補完のため、深さを妥協する理由がない | Skill＋Prerequisite Knowledge（取締役会・執行役員構造、権限委譲パターン等） | **L2**（修正） |
| 5 | Commercial／Contract Literacy | 必要。範囲は「専門家として契約書を扱う」ではなく「論点を発見し、Legalへの質問に変換する」に限定 | Skill＋Prerequisite Knowledge（契約基本構造、典型的リスクポイント等） | **L2**：契約・責任分界・知財・検収等の潜在論点を自力で発見し、Business Impactを説明した上でLegalへのQuestionとして整理できる水準。法的判断はL2でも範囲外のまま |
| 6 | Regulatory／Risk Literacy | 必要。範囲は5と同様、専門的な法解釈ではなく論点発見と質問への変換 | Skill＋Prerequisite Knowledge（業界別規制カテゴリ、規制論点の典型的な経営影響パターン等） | **L2**：Cross-border、Data、業規制等の潜在的規制論点を自力で発見し、Business Impactと専門家確認事項を整理できる水準。法的判断はL2でも範囲外のまま |

Governance／Managementの修正の結果、**Capability IVの6項目はすべてRequired Level L2で揃った**。これは見た目を揃えたのではなく、「Strategy Consultantは、標準的な案件であればBusiness／Management Literacyの各領域について自力で気づき、判断し、必要な行動（仮説形成・Question化・Governance／Escalation設計への反映等）につなげられる」という、Role側の最低線の思想から自然に導かれた結果である。

L3・L4も他のSkill同様に定義してある（本体は`consultant-capability-skill-model.md` §3.4）。Strategy ConsultantというRoleが要求するのは上表のLevelまでで、L3（他者の分析・見落としをレビューできる）・L4（非標準状況に適応し指導できる）はこのRoleでは要求しないが、Skillの定義としては存在する。将来別のRoleがより高いLevelを要求する可能性に備えている。

### 5.3 確定：Capability IV「Business / Management Literacy」

上記6候補を、**Capability IV｜Business / Management Literacy**として新設した（v0.1では提案段階、今回で確定）。Capability I〜IIIとは性質が異なる点を明示する位置づけは維持する。

- Capability I〜III＝「型（プロセス・技法）」。業界・クライアントを問わず適用できる
- Capability IV＝「実務知識・literacy」。型を具体的なクライアントに正しく当てはめるための事業理解

Capability IVの6項目は、すべて他の18 Skillと同じ形式（Prerequisite Knowledge・L0→L4 Evidence・Learning／OJT・判定者）で`consultant-capability-skill-model.md`（v0.6）に統合した。

前回レビュー（v0.3〜v0.4）で「Consulting Skill ModelをPresentation／Leadership／Negotiation……と一般的なCompetency Frameworkに広げるとモデルの強みが失われる」という指摘があった。Capability IVはこの懸念に対する回答として、**「教えられる教材があり、実際に判定できるSkillだけを置く」という原則は維持しつつ、「型を現実のクライアントに正しく当てはめるための実務知識」という、Capability I〜IIIでは埋まらない領域**として切り分けている。Presentation・Negotiationのような汎用ビジネススキル一般には広げていない。

### 5.4 Capability I〜IIIのRequired Level（Pilotに必要な補完）

Pilot（§7）でRole Required Level Gapを見るには、Capability IVだけでなく既存18 Skillについても、Strategy ConsultantとしてのRequired Levelが要る。Skillの新規追加ではなく、既存Skillに対するRole側の「必要な水準」の指定であり、机上でSkillを新たに増やす作業ではない。

R1〜R8のマッピング（§2）に基づく。

| Capability | Skill | Required Level | 根拠 |
|---|---|---|---|
| I | 問いを立てる | L2 | R1 |
| I | 構造化する | L2 | R1、R3 |
| I | 仮説を作る | L2 | R2 |
| I | 分析する | L2 | R2 |
| I | 評価・意思決定する | L2 | R5 |
| II | Work Planning／WBS | L0（対象外） | strategy-scn.md Ch7.3「詳細WBSは書かない」。②以降・PgMO／ベンダーPMの領域 |
| II | Dependency Management | L0（対象外） | 同上、②以降の領域 |
| II | Schedule Integration | L0（対象外） | 同上 |
| II | Scope／Responsibility | L0（対象外） | 同上 |
| II | Risk／Issue Management | L0（対象外） | 同上 |
| II | Transition Due Diligence／Planning | L0（対象外） | ③の領域 |
| II | Knowledge Transfer | L0（対象外） | 同上 |
| II | Transition工数見積もり | L0（対象外） | 同上 |
| III | Stakeholder Diagnosis | L2 | R6 |
| III | Communication | L2 | R6、成果物全般 |
| III | Facilitation | L2 | R3（SCNワークショップ運営） |
| III | Influence／Activation | L2 | R6（Ownershipまで導く） |
| III | Governance／Escalation | L1 | R8（Gate 1のSponsor合意形成に最低限必要。継続的なガバナンス設計運用自体は②のPgMOが主体） |

Capability IIが軒並みL0（対象外）なのは意図的である。Strategy Consultant RoleはGate 1までを担い、個別PJの実行管理は②（PgMO）・③（Transition Manager）という別Roleの領域になる。将来PgMO RoleのRequired Levelを定義するときは、ここが逆にL2以上で埋まり、Capability Iの一部がむしろL1程度に下がる、という非対称が出るはずである。これもRole別にRequired Levelを分離した設計の効能として期待している。

---

## 6. 構造検討は終了。ここから先はPilotの入力のみ

**今回までに展開したもの**（`consultant-capability-skill-model.md` v0.6側）：Capability IVの6 Skillについて、Prerequisite Knowledge・L0→L4 Evidence・Learning／OJT・判定者を、既存18 Skillと同じ形式・同じ厳密さで作成した。Capability I〜IIIを含む24 Skill全部にStrategy ConsultantのRequired Levelを設定した（§5.4）。

**もう机上ではやらないこと**：

- 「他にSkillはないか」を探す追加のCapability／Skill探索
- Capability IVのLearning Map化（Pilotで実際に必要になった時点で作成する）
- 他Role（PgMO、Transition Manager等）のRole／Responsibility定義（Strategy ConsultantでのPilot後）

構造設計としてはここで一区切りとする。以降の変更は、次章のPilotで実際に発生した運用上の問題だけを入力とする。

---

## 7. 次に必要なもの：実在メンバー1名によるPilot

構造検討は終了。次は`frameworks/pilot-assessment-strategy-consultant.md`（本Roundで新規作成）を使い、実在メンバー1名について次を通しで実施する。

1. 24 Skill全部のCurrent Level Assessment（自己申告→Evidence確認）
2. Capability IVはPrerequisite Knowledge（Pass／Not Yet）も確認
3. Assessment Status（Confirmed／Provisional）の判定
4. §1.5（`consultant-capability-skill-model.md`）のPrerequisiteとの整合確認
5. §5.4の Required Level と Current Level の Gap 算出
6. Learning Map生成
7. 次のOJT決定

Pilotを通して見るべきは、モデルの美しさではなく実際に人を評価できるかである。特に、EvidenceがないSkillの扱い、「未経験」と「能力不足」の区別、Provisionalの確定方法、Knowledge Not YetのままSkill Evidenceがある場合の扱い、24 Skill評価の負荷が現実的か、Required L2に対するGapが大量に出た場合の優先順位づけ、Evidence／Knowledgeの保存場所――これらはPilotをやらなければ見えない。

Pilotの対象者、実施時期、Evidence／Knowledgeの記録方法（誰が・どこに）をご指定いただければ、`pilot-assessment-strategy-consultant.md`に沿って一緒に埋めていく。
