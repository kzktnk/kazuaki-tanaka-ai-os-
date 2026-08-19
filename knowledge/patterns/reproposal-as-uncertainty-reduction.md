---
type: pattern
---

# Pattern — Re-proposal as Uncertainty Reduction

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Re-proposal as uncertainty reduction  
**Applies to:** private-enterprise vendor selection, competitive sourcing, complex IT implementation

---

## Pattern

> **The purpose of re-proposal is not to let vendors rewrite weak slides. It is to convert evaluation uncertainty into explicit commitments.**

一次提案で不明な点があるからといって、すぐに「評価できない」「低評価」で終わらせる必要はない。

民間企業の競争選定では、候補を絞った後に質問・再提案・面接・見積再提示を使い、**発注者にとってより良い条件と実行コミットメントを引き出す**ことができる。

## Signals

- 必須情報が欠けている、前提が書いていない  
- 体制が一般論で、指名がコミットされていない  
- 見積が総額だけで work package に落ちない  
- 一次で評価者が「判断不能」で止まっている  
- 契約条件の重大差が二次まで持ち越されそう  
- 再提案依頼が「詳細化してください」だけになっている  

## Underlying mechanism

初回提案は情報・前提・コミットが揃わないのが常態。一度で完成回答を求めると、情報不足で良い候補を落とすか、見た目で過大評価する。再提案は救済回数ではなく、**不確実性をコミットメントに変換する手段**。

## Implications

一次の不明は即減点確定しなくてよい。ただし質問には判断用途と回答種別（情報／提案／コミット）を付ける。民間でも他社機密は渡さない。

## Response

Concern register → 優先（意思決定・コスト・不可逆・キーパーソン・契約）→ 判断に使える質問 → 回答種別を指定 → 二次では「何が変わったか」を評価。詳細は下記ステップ。

## Exceptions

再提案しない（選外・失格になり得る）場合は `When not to request re-proposal`。無償の追加設計の搾取、後付け必須要件、無限の確認で意思決定を先送りする場合は、このパターンの適用外（アンチパターン）。

---

## Why this pattern exists

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Applies to:** private-enterprise vendor selection, competitive sourcing, complex IT implementation

---

## Pattern

> **The purpose of re-proposal is not to let vendors rewrite weak slides. It is to convert evaluation uncertainty into explicit commitments.**

一次提案で不明な点があるからといって、すぐに「評価できない」「低評価」で終わらせる必要はない。

民間企業の競争選定では、候補を絞った後に質問・再提案・面接・見積再提示を使い、**発注者にとってより良い条件と実行コミットメントを引き出す**ことができる。

---

## Why this pattern exists

初回提案には以下が残りやすい。

- missing information
- wrong assumptions
- weak rationale
- ambiguous scope
- unclear responsibility
- generic organization
- uncommitted key people
- rough estimate
- contract qualifications
- unaddressed risk

一度の提案で完全回答を期待すると:

- 良い候補を情報不足だけで落とす
- presentation quality を過大評価する
- 比較不能な見積をそのまま比較する
- 契約直前まで重要条件が残る

---

## Re-proposal objective

再提案依頼には目的を付ける。

### 1. Completeness

必須情報を補う。

### 2. Correctness

誤認・誤記・前提違いを直す。

### 3. Reasoning

曖昧だった前提・リスク・実現方法を深掘りする。

### 4. Feasibility

工程・体制・移行・品質・依存関係を現実化する。

### 5. Commitment

「可能」から「実施する」へ変える。

### 6. Estimate accuracy

スコープ、作業量、前提を明確にする。

### 7. Commercial clarity

重大な契約条件差を前倒しで確認する。

---

## Uncertainty-to-action matrix

| Evaluation uncertainty | Best next action |
|---|---|
| RFP理解が曖昧 | written clarification |
| 方式の妥当性が不明 | technical deep dive |
| PM能力が不明 | key-person interview |
| 配置が不明 | written staffing commitment |
| 見積範囲が不明 | estimate breakdown / revised estimate |
| 前提が競合 | common assumption reset |
| 移行が弱い | migration plan revision |
| 契約条件差 | commercial clarification |
| 提案の一貫性に懸念 | integrated re-proposal |

---

## Step 1 — Build the concern register

一次評価から以下を抽出する。

```md
Concern ID:
Evaluation item:
Evidence:
Why it matters:
Type:
- missing
- incorrect
- ambiguous
- feasibility
- commitment
- estimate
- commercial
Required response:
Decision impact:
```

---

## Step 2 — Prioritize

すべてを再提案対象にしない。

Priority criteria:

- decision-critical
- large cost impact
- schedule impact
- irreversible architecture
- migration / cutover risk
- key-person risk
- contract deal-breaker

---

## Step 3 — Ask a decision-useful question

Weak:

> 移行計画を詳細化してください。

Better:

> 現行データの品質確認、変換、照合、リハーサル、本番切替の各工程について、発注者／ベンダーの責任、必要期間、前提条件、cutover失敗時のfallbackを明示してください。見積変更がある場合は対応するwork packageを示してください。

質問は「資料を増やす」ためではなく、判断するために書く。

---

## Step 4 — Specify commitment level

回答種別を明示する。

- information
- proposal
- assumption
- option
- recommendation
- commitment
- contract condition

「検討可能です」という回答では足りない場合、明示的に commitment を求める。

---

## Step 5 — Preserve fairness without becoming public procurement

民間競争でも不健全な操作は避ける。

Do not:

- disclose competitor-confidential details
- reveal competitor price structure
- ask one vendor to copy another vendor’s proprietary solution
- change decision rules only to favor a preferred vendor

Can do:

- use competing proposals to identify missing buyer requirements
- tighten common assumptions
- ask shortlisted vendors for stronger commitments
- improve estimate comparability
- negotiate commercial conditions

---

## Step 6 — Re-evaluate the change, not just the document

二次評価で見る。

1. What changed?
2. Which concern was resolved?
3. Is the new answer credible?
4. Is it now a commitment?
5. Did scope / cost / schedule change?
6. Did one improvement create another risk?
7. What remains unresolved?

---

## Re-proposal categories

### Mandatory correction

要求漏れ・誤認を修正。

### Sufficient / reasoning improvement

前提、リスク、実現方法、工程、体制を具体化。

### Commitment enhancement

- named role
- dedicated allocation
- milestone
- quality target
- response time
- delivery responsibility

### Estimate normalization

- missing work
- duplicate work
- assumptions
- option separation
- third-party cost
- contingency
- scope boundary

### Contractability

重大な契約条件の確認。

---

## When not to request re-proposal

以下はそのまま失格・選外判断になり得る。

- mandatory requirement cannot be met
- material misrepresentation
- unacceptable integrity issue
- fundamental delivery capability missing
- non-negotiable commercial condition conflict
- no credible key-person commitment
- solution violates a fixed architecture / security constraint

再提案は「何度でも救済する制度」ではない。

---

## Common failure patterns

### Slide polishing

見た目だけ改善され、実現性が増えない。

### Free consulting extraction

採用意思が薄いベンダーから大量の追加設計を無償要求する。

### Moving goalposts

RFP にない新要件を後から評価必須にする。

### Competitor leakage

他社提案の固有アイデアを別社へ渡す。

### Endless clarification

意思決定を避け、回答要求を続ける。

### Commitment ambiguity

「対応可能」「検討予定」をコミットメントと誤認する。

---

## Re-proposal quality checklist

- [ ] every request maps to a decision concern
- [ ] priority is explicit
- [ ] expected response type is explicit
- [ ] expected commitment level is explicit
- [ ] estimate impact is requested where relevant
- [ ] scope impact is requested where relevant
- [ ] no competitor-confidential information is disclosed
- [ ] second-stage evaluation use is defined
- [ ] response deadline is reasonable
- [ ] unresolved issues after response are retained

---

## Outcome

良い再提案プロセスの成果は、文章量ではない。

```text
Less uncertainty
+
Stronger commitments
+
More comparable estimates
+
Clearer residual risk
=
Better vendor decision
```

---

## Related files

- `playbooks/private-it-rfp-vendor-selection.md`
- `standards/vendor-proposal-evaluation.md`
- `standards/vendor-key-person-interview.md`
- `knowledge/patterns/scoring-vs-calibration.md`
