---
type: framework
---

# Private Enterprise IT RFP Framework

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Framework for designing an RFP for private-enterprise IT implementation  
**Origin:** Generalized from 2002–2003 private ERP/RFP practice and later selection work. RFP body, appendices, yen, and vendor names stay in local originals.  
**Scope:** System replacement, ERP/package implementation, custom development, platform/infrastructure, data migration, and related implementation sourcing  
**Does not contain:** client names, prices, vendor names, product-specific instructions, or project-specific inventories

---

## Purpose

民間企業が IT 導入・刷新を外部ベンダーへ依頼する際に、RFP を「要求事項の羅列」ではなく、**発注者が決めるべきことと、ベンダーに考えさせることを分離し、比較可能な提案と有効なコミットメントを引き出すための設計物**として作るための Framework。

RFP の品質は、文章量ではなく次で決まる。

1. なぜ変えるかが明確である
2. 何を対象とするかが明確である
3. 何が確定し、何が未確定かが明確である
4. ベンダーに何を答えさせたいかが明確である
5. 提案評価と見積比較に使える構造になっている
6. 契約・実行フェーズへつながる

---

## When to use

- 民間企業が IT 導入・刷新を競争選定する  
- 調査〜要件の後に、提案依頼の構造を決める  
- 詳細仕様を書く前に、何を固定し何を開くかを決める  

使わない: 法定の総合評価・仕様書調達（`frameworks/public-it-procurement-support.md`）。実行の週次手順は `playbooks/private-it-rfp-vendor-selection.md`。

## Inputs

- 事業目的と優先する成果  
- 現状課題と目標状態  
- スコープ仮説（組織／業務／アプリ／データ／IF／基盤／移行／運用）  
- アーキテクチャ原則と、製品決定が先行すべきかの判断  
- 発注者側の未決事項リスト  
- 予算・時期の制約（金額そのものはリポジトリに置かない）  

## Structure

`RFP design model` 節のとおり。RFP の問いと評価基準は一体。

## Outputs

- RFP の章立てと回答構造  
- 要件クラス（confirmed / variable / intentionally open）  
- 見積回答の構造  
- 評価に使う問いの対応  
- 配布前の readiness gate 結果  

---

## Core principle

> **Do not issue an RFP before the buyer has made the decisions that only the buyer can make.**

ベンダーは実現方法、工程、体制、リスク、代替案を提案できる。  
一方で、投資目的、優先順位、対象組織、業務責任、許容できる制約、意思決定権限までベンダーへ委ねると、提案の比較軸そのものがなくなる。

---

## RFP is not a detailed specification

RFP と詳細仕様書は同じではない。

RFP が定義すべきものは、少なくとも以下である。

- Business context
- Project purpose
- Target outcomes
- Scope
- Known requirements
- Constraints
- Known uncertainties / change factors
- Required proposal structure
- Required commitments
- Evaluation logic
- Commercial / contractual response requirements

ベンダーの課題解決能力を見たい領域まで詳細仕様で固定すると、提案能力を評価できない。

逆に、発注者が決めるべきことまで「自由提案」にすると、提案同士を比較できない。

---

## RFP design model

```text
Business context
      ↓
Issues / drivers
      ↓
Target outcomes
      ↓
Scope
      ↓
Requirements
      ↓
Known uncertainties
      ↓
Constraints
      ↓
Proposal questions
      ↓
Estimate structure
      ↓
Evaluation criteria
```

RFP と評価基準は別作業ではない。

**RFP で問い、評価基準でその答えを見る。**

---

## 1. Business context

ベンダーが「要求された機能」だけでなく、なぜその要求が必要なのかを理解できるだけの背景を提示する。

最低限:

- 事業・組織の概要
- 現行業務・現行システムの問題
- 外部環境・経営施策・制度変更等の重要な変動要因
- 今回の投資が必要な理由
- 後続の事業・組織変更の可能性

### Quality gate

- 背景からプロジェクト目的が論理的につながっているか
- 「老朽化しているため刷新」だけで終わっていないか
- 重要な将来変化を提案者が考慮できる情報があるか

---

## 2. Purpose, goals, and success factors

### Project purpose

「何を作るか」ではなく、「何を変えるか」を書く。

Weak:

> 新しい基幹システムを導入する。

Better:

> 現行システムの硬直性・高コスト・情報提供の遅さを解消し、将来の事業・組織変更にも対応できる業務・システム基盤を構築する。

### Goals

ゴールは優先順位を持たせる。

例:

- Operating cost reduction
- Process lead-time reduction
- Information quality / timeliness
- User service improvement
- Change adaptability

すべてを「最優先」にしない。

### Success factors

成功要因は、機能要件より上位に置く。

例:

- target operating model is agreed
- migration can be executed within the cutover constraint
- package / custom boundary is explicit
- key business decisions are made by agreed gates
- ownership of master data is assigned

---

## 3. Scope

RFP ではスコープを複数の軸で定義する。

| Scope axis | Typical content |
|---|---|
| Organization | 対象会社、部門、拠点、利用者 |
| Business | 対象業務、対象外業務 |
| Application | 新規、改修、廃止、継続利用 |
| Data | 移行対象、マスタ、履歴、アーカイブ |
| Interface | 他システム、外部連携 |
| Infrastructure | 環境、ネットワーク、監視、運用 |
| Migration | system / data / business transition |
| Operation | 運用設計、保守、サポート |
| Delivery | design / build / test / migration / training |
| Responsibility | buyer / vendor / third party |

### Common error

「対象システム」を示しただけで、移行・教育・運用設計・データ・インターフェースを暗黙に含める。

---

## 4. Requirement classes

要件は「全部同じ確定度」で扱わない。

### 4.1 Confirmed requirements

発注者が現時点で確定している要求。

ベンダーには次を答えさせる。

1. Assumptions
2. Realization method
3. Delivery process and organization
4. Estimate impact

### 4.2 Variable / uncertain requirements

経営・制度・組織・他プロジェクト等により変更可能性がある要求。

ベンダーには次を答えさせる。

- what assumption is used
- how the solution changes by scenario
- what must be decided by when
- schedule / cost / organization impact
- risk and contingency

### 4.3 Intentionally open requirements

発注者が詳細を固定せず、ベンダーの課題解決能力を見たい領域。

「曖昧だから書けていない」のではなく、**何を考察してほしいかを明示した上で開く。**

---

## 5. Mandatory / reasoning-required / value-add

提案評価につなげるため、要求・問いを次の3つに分類できる。

### Mandatory

プロジェクト目的を成立させるために必須。

- 満たさなければ受容困難
- 明確な確認ポイントを設定する

### Reasoning-required

ベンダーの問題解決能力を見る領域。

評価対象例:

- assumptions
- risks
- design rationale
- alternatives
- implementation approach
- organization
- schedule

### Value-add

明示要求を超えた提案で、以下を満たすもの。

- 発注者が見落としていた重要論点を示す
- より良い実現方法を示す
- リスクを下げる
- 運用・保守・変更容易性を改善する
- 妥当性が説明されている

Value-add は「追加機能の多さ」ではない。

---

## 6. Functional requirements

機能要件は業務目的と紐づける。

推奨項目:

- business process / function
- requirement
- priority / class
- current issue
- expected outcome
- known constraint
- data / interface dependency
- acceptance viewpoint
- proposal question

大量の機能一覧を作る場合でも、ベンダーが「なぜ必要か」を理解できる上位構造を先に置く。

---

## 7. Data and interface requirements

最低限確認する。

- master / transaction / history
- data ownership
- source and destination
- migration
- retention / archive
- quality issues
- external interfaces
- internal interfaces
- timing / frequency
- reconciliation
- security / access

### Principle

> Data migration is not an appendix to application development.

データ量、品質、変換、照合、cutover が工程・見積・リスクに反映されるよう RFP に含める。

---

## 8. Architecture and platform requirements

RFP に書くのは、製品手順ではなく設計制約と期待品質。

例:

- architecture principles
- interoperability
- changeability / extensibility
- reliability
- performance
- security
- availability
- operability
- maintainability
- standards
- development / test / production environments
- monitoring
- backup / recovery
- disaster considerations

技術を指定する場合は、「なぜ指定するか」と「指定により何が制約されるか」を明確にする。

---

## 9. Package / custom boundary

Package selection が調達前に必要な場合がある。

特に以下の場合:

- package choice materially changes scope
- package choice changes implementation method
- package choice changes vendor qualification
- package choice affects estimate accuracy
- package / custom integration is a major risk

### Gate

RFP 配布前に確認する。

```text
Is the product decision required to compare proposals fairly?
        ├─ Yes → product/package selection first
        └─ No  → leave options open and define evaluation logic
```

---

## 10. Migration and cutover

RFP で問う。

- data migration approach
- system transition
- business transition
- rehearsal
- cutover
- rollback / fallback
- parallel operation if applicable
- dependency on other projects
- training / readiness
- support after go-live

### Quality gate

工程表に「移行」とだけ書かれていないか。

---

## 11. Delivery standards and quality

必要に応じて要求する。

- project management
- development management
- design standards
- coding / configuration standards
- test strategy
- defect management
- configuration management
- document standards
- quality metrics
- review gates
- issue / risk management
- change control

Standard を指定する目的は、文書を増やすことではなく、**複数チーム・複数ベンダー間で品質と統合を成立させること**。

---

## 12. Proposal response structure

比較可能性を高めるため、提案書の回答構造を指定する。

推奨:

1. Executive understanding
2. Understanding of business and project goals
3. Scope understanding
4. Overall solution
5. Assumptions
6. Realization approach
7. Architecture
8. Data / integration
9. Migration
10. Delivery process
11. Organization and named key people
12. Schedule and milestones
13. Risks and mitigations
14. Quality approach
15. Operations / support
16. Estimate
17. Commercial assumptions
18. Contract deviations / requested conditions
19. Value-add proposals

---

## 13. Estimate response design

金額だけでなく、**何の作業量か**を比較できる構造を要求する。

最低限:

- work package
- phase
- role / skill
- effort
- rate or cost basis where appropriate
- software / hardware / third-party
- assumptions
- exclusions
- optional items
- contingency / risk treatment
- recurring vs one-time
- change mechanism

### Principle

> An estimate is credible only when scope, assumptions, delivery approach, organization, and schedule tell the same story.

---

## 14. Contract response requirements

提案段階で契約上の重要論点を見える化する。

- payment conditions
- acceptance
- warranty / defect handling
- intellectual property
- confidentiality
- subcontracting
- liability / limitation
- termination
- change control
- ownership of deliverables / source / configuration
- post-go-live support

詳細な法務判断は Legal が行う。  
RFP では「後から初めて重大な条件差が発覚する」ことを避ける。

---

## 15. Evaluation traceability

RFP の各重要要求には評価方法を対応させる。

```text
RFP requirement
      ↓
Proposal response location
      ↓
Evaluation item
      ↓
Evidence / comment
      ↓
Score / judgment
      ↓
Clarification or re-proposal if needed
```

評価基準が RFP 配布後に作られると、後付け評価になりやすい。

---

## Limitations

- 実行順序・ゲート運営は Playbook 側。本ファイルは構造だけ。  
- 国・業界の法定手続、会計規則、総合評価の配点ルールは扱わない。  
- 機能要件の全文、データ辞書、帳票一覧はここには置かない。  
- パッケージ選定が必須な案件では、本 Framework だけでは製品比較を代替できない。  

## Risks

- 発注者未決をベンダー提案で埋め、比較不能になる。  
- 未確定を確定要件として書き、契約後に変更コスト化する。  
- 特定ベンダー前提の構造になり、競争が形骸化する。  
- 評価基準なしで配布し、後付け採点になる。  
- 移行・データ・運用を「含む」と暗黙にし、見積が割れない。  

## Examples

Purpose 節の Weak / Better（「新システムを導入する」対「何を変えるか」）。Requirement classes の confirmed / variable / open の問い分け。Estimate 節の「総額」対 work package 対応。クライアント実名の成功例は載せない。

---

## RFP readiness gate

RFP 配布前に Yes を求める。

- [ ] Business purpose is clear
- [ ] Target outcomes are prioritized
- [ ] Scope is explicit
- [ ] Buyer decisions have been made where necessary
- [ ] Confirmed and uncertain requirements are distinguished
- [ ] Package / architecture constraints are appropriately fixed
- [ ] Migration and operation are included
- [ ] Proposal response structure is defined
- [ ] Estimate structure is defined
- [ ] Evaluation criteria are drafted
- [ ] Q&A governance is defined
- [ ] Decision makers and evaluation team are assigned
- [ ] Commercial / contract response requirements are defined

---

## Common failure patterns

### Requirement dump

大量の要件を書いたが、目的・優先順位・評価軸がない。

### False certainty

未確定事項を確定要件として書き、提案後に変更する。

### Excessive openness

「最適な方式をご提案ください」で発注者の意思決定まで委ねる。

### Vendor-specific RFP

特定提案を前提に構造を作り、比較可能性を失う。

### Evaluation-after-RFP

RFP を出してから採点方法を考える。

### Price-only comparability

総額だけ比較し、スコープ・前提・工程・体制の差を見ない。

---

## Related files

- `playbooks/private-it-rfp-vendor-selection.md`
- `frameworks/vendor-delivery-model-gap-analysis.md`
- `frameworks/public-it-procurement-support.md` (do not mix statutory public process)
- `standards/vendor-proposal-evaluation.md`
- `standards/vendor-key-person-interview.md`
- `knowledge/patterns/scoring-vs-calibration.md`
- `knowledge/patterns/reproposal-as-uncertainty-reduction.md`
