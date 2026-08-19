---
type: playbook
---

# Private IT RFP & Vendor Selection Playbook

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** 民間企業の IT 導入において、RFP 設計から提案評価・再提案・候補決定・契約準備までを一貫して実行する手順  
**Use when:** ERP / package implementation, custom development, platform modernization, enterprise application replacement, large integration sourcing  
**Do not use as-is for:** statutory public procurement — use `frameworks/public-it-procurement-support.md` and `domains/public-defense.md` instead. Fairness still matters; the legal process and protest surface are different.

## Trigger

民間 IT 導入の競争選定を設計する、または一次評価のあと shortlist / 再提案 / 面接に進む。

## Objective

一回の採点イベントではなく、理解 → 解法 → 実行信憑 → 見積 → 契約 → 指名チームまで、不確実性を段階的に減らして契約可能な判断にする。

## Prerequisites

- Executive sponsor と Business owner が特定されている  
- 投資自体をやるかの意思決定は済んでいる（本 Playbook の範囲外）  
- 発注者が決めるべき目的・優先・権限が、RFP でベンダーに丸投げされていない（未決は明示）  
- 評価者と最終決裁者が分かれている  
- 公共の法定調達手続を、この Playbook で代替しようとしていない  
- 発注体制（誰にプライムを任せ、何を自社に残すか）が未確定なら、先に `frameworks/vendor-delivery-model-gap-analysis.md`  

## Required inputs

Stage 0 Inputs に同じ。加えて配布後は提案書、見積内訳、契約逸脱回答、キーパーソン情報。機密の実数・社名は原本のみ。

## Escalation conditions

- 必須要件を満たせない／虚偽／インテグリティ問題 → 再提案せず選外判断へ  
- 評価者が同一点に収束せず shortlist が割れる → Evaluation lead がキャリブレーションを主催。決まらなければ Decision owner  
- 重大な契約条件差 → Legal / 決裁者。技術点で相殺しない  
- 他社提案の固有内容を質問に含めそう → 即停止  

Sequence, decision gates, quality checks, and outputs are in the stages and completion checklist below.

---

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** 民間企業の IT 導入において、RFP 設計から提案評価・再提案・候補決定・契約準備までを一貫して実行する手順  
**Use when:** ERP / package implementation, custom development, platform modernization, enterprise application replacement, large integration sourcing  
**Do not use as-is for:** statutory public procurement — use `frameworks/public-it-procurement-support.md` and `domains/public-defense.md` instead. Fairness still matters; the legal process and protest surface are different.

---

## Operating principle

> **Vendor selection is not one scoring event. It is a staged reduction of uncertainty.**

良い選定では、最初から「最も点の高い会社」を決めない。

順番に不確実性を減らす。

```text
What are we buying?
        ↓
Can the vendor understand it?
        ↓
Can the vendor solve it?
        ↓
Can the vendor actually deliver it?
        ↓
Is the estimate credible?
        ↓
Can we contract on acceptable terms?
        ↓
Can the named team mobilize?
```

---

## Roles

最低限以下を定義する。

| Role | Responsibility |
|---|---|
| Executive sponsor | final business decision |
| Business owner | business requirements / priority |
| IT owner | architecture / delivery / operating constraints |
| Procurement | sourcing process / commercial coordination |
| Legal | contract review |
| Finance | budget / business case |
| Evaluation lead | evaluation design / calibration |
| Domain evaluators | functional / technical evaluation |
| PMO / advisor | process, evidence, issue management |
| Vendor | proposal, clarification, commitment |

評価者と最終決裁者を曖昧にしない。

---

## End-to-end flow

### Stage 0 — Confirm sourcing readiness

**Goal:** RFP を出す前に、発注者が決めるべきことを決める。

**Inputs**
- systemization strategy
- current-state findings
- target state
- business case
- scope hypothesis
- package / build strategy
- architecture principles

**Actions**
1. Confirm project purpose and prioritized outcomes.
2. Confirm target organization / business / system scope.
3. Identify change factors and unresolved decisions.
4. Decide whether package / product choice must precede RFP.
5. Define procurement lot / responsibility boundary.
6. Confirm governance and decision authority.

For steps 4–5, use `frameworks/vendor-delivery-model-gap-analysis.md` (money flow × management structure → patterns A–E → capability gap) before defaults are frozen.

**Gate**
- RFP を出すことで「要件を決めてもらう」状態になっていないか。

**Outputs**
- sourcing strategy
- scope baseline
- decision log
- RFP workplan

---

### Stage 1 — Build the requirement baseline

**Goal:** 何を要求し、何をベンダーに考えさせるかを分離する。

**Actions**
1. Structure requirements by business / application / data / interface / platform / migration / operations.
2. Classify each important requirement:
   - confirmed
   - variable
   - intentionally open
3. Identify:
   - mandatory items
   - reasoning-required items
   - candidate value-add areas
4. Link requirements to expected outcomes.
5. Identify estimate-driving assumptions.

**Quality gate**
- variable requirement を「TBD」のまま放置していないか
- uncertain item について、提案で答えてほしい問いがあるか

**Outputs**
- requirement baseline
- uncertainty / assumption register
- scope boundary
- evaluation seed list

---

### Stage 2 — Draft RFP and evaluation criteria together

**Goal:** RFP と評価基準を一体設計する。

**Actions**
1. Draft RFP using `frameworks/private-it-rfp.md`.
2. For each material requirement, define how it will be evaluated.
3. Define proposal response structure.
4. Define estimate template / commercial response.
5. Define contract deviation response.
6. Define key-person information required.
7. Define Q&A process.

**Rule**

> Every major RFP question must have an intended evaluation use.

質問するが評価しない情報を減らす。

**Outputs**
- RFP draft
- proposal response template
- evaluation standard
- evaluation worksheet
- estimate response format

---

### Stage 3 — Review and freeze the RFP baseline

**Goal:** 配布後の不要なぶれを減らす。

**Review viewpoints**
- Purpose / scope consistency
- Requirement completeness
- Requirement class
- Uncertainty treatment
- Architecture constraint
- Migration / operation
- Proposal comparability
- Evaluation traceability
- Estimate comparability
- Contract conditions
- Internal ownership

**Decision**
- issue
- revise
- hold

---

### Stage 4 — Select invitees and issue RFP

**Goal:** 提案依頼先が、対象を実行し得る母集団になっていることを確認する。

**Evaluate as needed**
- relevant delivery experience
- domain / technology capability
- scale
- financial / organizational stability
- support capability
- package / platform experience
- availability
- conflict / dependency
- strategic fit

RFP 配布先の事前評価と提案評価を混同しない。

**Outputs**
- invitee list
- RFP issue record
- NDA / administrative setup
- proposal calendar

---

### Stage 5 — RFP briefing and Q&A

**Goal:** 不必要な解釈差を減らしながら、ベンダー固有の解法余地を残す。

**Actions**
1. Explain:
   - business purpose
   - target outcome
   - scope
   - major constraints
   - change factors
   - proposal format
   - evaluation process
2. Collect questions in one governance channel.
3. Separate:
   - clarification of buyer information
   - vendor-specific solution discussion
4. Update / correct RFP information if necessary.
5. Record all material changes.

**Rule**

Q&A は「回答会」ではなく、RFP の曖昧さを検査する場でもある。

---

### Stage 6 — First proposal evaluation

**Goal:** 候補を絞るとともに、提案の不確実性を構造化する。

一次評価では主に以下を見る。

#### A. Understanding

- business context
- current issues
- project purpose
- scope
- target state
- major milestones and dependencies

#### B. Proposal capability

For confirmed and variable requirements:

- assumptions
- realization method
- process
- organization
- risk thinking
- value-add

#### C. Delivery credibility

- relevant experience
- company capability
- named key people
- reusable knowledge / assets
- evidence supporting claims

#### D. Estimate logic

- requirements reflected in cost
- scope alignment
- major assumptions
- missing / duplicated work

#### E. Contract issues

At first stage, identify material deal-breakers; do not necessarily complete negotiation.

**Actions**
1. Individual evaluation.
2. Record evidence and rationale.
3. Compare evaluator variance.
4. Conduct calibration.
5. Create question / concern list.
6. Identify candidates for next stage.

**Outputs**
- first-evaluation result
- evaluation rationale
- vendor question list
- uncertainty / concern register
- shortlist recommendation

---

### Stage 7 — Clarification and re-proposal design

**Goal:** 一次評価で判明した不確実性を、明示的な回答・改善・コミットメントへ変える。

再提案依頼は全論点を送り返さない。

分類する。

| Category | Purpose |
|---|---|
| Missing mandatory information | completeness |
| Reasoning gap | problem-solving capability |
| Incorrect information | correction |
| Unclear assumption | comparability |
| Delivery concern | feasibility |
| Key-person concern | credibility |
| Estimate ambiguity | cost accuracy |
| Commercial issue | contractability |
| Value opportunity | stronger commitment |

**Actions**
1. Define what must be answered.
2. Define whether written response, interview, demo, or revised estimate is required.
3. State expected commitment level.
4. Define deadline and evaluation use.
5. Avoid disclosing competitor-confidential content.

**Output**
- re-proposal / clarification request

See `knowledge/patterns/reproposal-as-uncertainty-reduction.md`.

---

### Stage 8 — Key-person interview

**Goal:** 提案書の品質ではなく、実際に delivery を担う人材の能力・コミットメントを確認する。

対象例:
- project manager
- solution architect
- lead consultant
- migration lead
- business lead

Use `standards/vendor-key-person-interview.md`.

**Output**
- interview evaluation
- risks / conditions
- staffing commitments

---

### Stage 9 — Second evaluation

**Goal:** 「良い提案」から「契約して実行できる提案」へ評価軸を移す。

二次評価で重点を置く。

- solution feasibility
- internal consistency
- response to concerns
- commitment
- estimate accuracy / scope
- named team
- schedule feasibility
- assumptions
- commercial / contractual acceptability

### Core questions

1. Did the vendor resolve the first-stage concerns?
2. Are remaining assumptions explicit?
3. Does the proposal now constitute a credible commitment?
4. Does the estimate match scope and delivery plan?
5. Are key people acceptable and actually assigned?
6. Are major contract issues manageable?
7. What risks remain with the buyer?

**Outputs**
- second evaluation
- preferred vendor recommendation
- negotiation issue list
- residual risk list

---

### Stage 10 — Estimate normalization

**Goal:** 総額比較ではなく、同じ work model で比較する。

Normalize:

- in-scope / out-of-scope
- phases
- work packages
- roles
- effort
- third-party cost
- environment
- migration
- training
- support
- travel / expense if relevant
- contingency
- options
- recurring cost

### Test

For each major cost:

> What requirement, assumption, work package, role, and duration causes this cost?

答えられないコストは精査対象。

---

### Stage 11 — Preferred vendor decision

**Goal:** 点数だけでなく、リスクと契約条件を含めて意思決定する。

Decision package:

- evaluation summary
- strengths
- weaknesses
- unresolved risks
- estimate comparison
- key-person assessment
- contractual concerns
- conditions before signature
- recommendation and rationale

### Rule

Highest score ≠ automatic decision.

Score supports judgment; it does not replace it.

---

### Stage 12 — Contract negotiation

**Goal:** 提案を契約可能な commitments へ変換する。

Confirm:

- scope
- deliverables
- milestones
- acceptance
- estimate / payment
- assumptions
- change control
- key people
- subcontracting
- IP / ownership
- warranty / defects
- confidentiality
- liability
- support
- termination
- governance

**Rule**

提案上の「検討します」「対応可能です」が、契約上の義務になっているか確認する。

---

### Stage 13 — Mobilization / handoff

**Goal:** 選定プロセスで得た知識を実行チームへ渡す。

Handoff:

- agreed scope
- proposal commitments
- assumptions
- open decisions
- risks
- estimate basis
- contract conditions
- key people
- major dependencies
- evaluation concerns requiring monitoring

選定チームが解散すると同時に rationale を失わない。

---

## Evaluation cadence

推奨する基本リズム:

```text
RFP issue
  ↓
Proposal
  ↓
Individual evaluation
  ↓
Calibration
  ↓
Shortlist
  ↓
Clarification / re-proposal / interview
  ↓
Second evaluation
  ↓
Preferred vendor
  ↓
Contract negotiation
```

---

## Decision gates

| Gate | Decision |
|---|---|
| G0 | sourcing ready? |
| G1 | requirement baseline ready? |
| G2 | RFP/evaluation ready? |
| G3 | RFP issue? |
| G4 | shortlist? |
| G5 | re-proposal requests approved? |
| G6 | preferred vendor? |
| G7 | contract ready? |
| G8 | mobilization ready? |

---

## Common failure modes

### One-shot beauty contest

プレゼンの印象で一度に決める。

### Score worship

総合点の差を、そのまま事業判断の差と扱う。

### Re-proposal as rewrite

弱いスライドを書き直させるだけで、コミットメントを強めない。

### Unnormalized estimate

総額のみ比較する。

### Generic PM interview

「経験年数」「資格」だけで PM を評価する。

### Contract late surprise

最終候補決定後に初めて重要契約条件を確認する。

### Lost rationale

選定時の懸念・前提が実行 PMO に引き継がれない。

---

## Completion checklist

- [ ] buyer-side purpose and scope are fixed enough
- [ ] uncertainties are explicit
- [ ] RFP and evaluation are traceable
- [ ] shortlist rationale is documented
- [ ] evaluator calibration occurred
- [ ] material concerns became clarification / re-proposal questions
- [ ] key people were assessed
- [ ] estimate was normalized
- [ ] residual risk is explicit
- [ ] commercial / contract concerns are visible
- [ ] proposal commitments are carried into contract
- [ ] selection rationale is handed to delivery governance

---

## Related files

- `frameworks/private-it-rfp.md`
- `frameworks/vendor-delivery-model-gap-analysis.md`
- `standards/vendor-proposal-evaluation.md`
- `standards/vendor-key-person-interview.md`
- `knowledge/patterns/scoring-vs-calibration.md`
- `knowledge/patterns/reproposal-as-uncertainty-reduction.md`
- `knowledge/patterns/estimate-target-commitment.md`
- `playbooks/ai-poc-quality-review.md` (AI/RAG PoC is a subset; this playbook is full implementation sourcing)
- `frameworks/public-it-procurement-support.md` (public buyer track — do not mix)
