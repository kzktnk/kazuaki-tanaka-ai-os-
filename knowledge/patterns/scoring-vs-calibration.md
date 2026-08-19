---
type: pattern
---

# Pattern — Scoring vs Calibration

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Scoring vs Calibration  
**Applies to:** vendor proposal evaluation, interview evaluation, architecture review, option comparison

---

## Pattern

> **Scoring makes judgment visible. Calibration makes judgment reliable.**

評価を点数化しても、判断が自動的に客観化されるわけではない。

評価者は異なる。

- experience
- domain knowledge
- interpretation
- risk tolerance
- evidence noticed
- preference

その差を隠すのではなく、**点差として見えるようにし、差が大きいところを会話する**。

## Signals

- 同一項目で Good と Poor、または 0 と上限点が共存する  
- 評価者によって shortlist が変わる  
- 根拠として引用している提案箇所が違う  
- 業務側と IT 側で「何が重要か」が違う  
- 差を会議せず平均・中央値・多数決で消そうとしている  
- 奇数段階で点が中央に張り付いている  

## Underlying mechanism

点数は判断を**比較可能な記号**にする。信頼性は、独立評価のあと、差の理由（問い・証拠・好み）を解くことでしか上がらない。精緻な係数は、入力判断が弱ければ客観性の錯覚になる。

## Implications

Variance はノイズとは限らない。見逃したリスク、要件解釈の割れ、提案の曖昧さ、評価基準の穴の診断信号である。総合点だけで説明すると、その信号が消える。

## Response

独立評価 → 意味のある差だけキャリブレーション → 同じ問い・同じ証拠かを先に揃える → 事実合意のうえ残る解釈差は Decision owner 付きで残す → 情報不足なら再提案・面接等のアクションへ。詳細は下記 Operating model。

## Exceptions

- 差が定義上無視できる（隣接段階のみ、shortlist が動かない）  
- 評価者が一人で、その旨が明示されている（推奨しない）  
- 法定手続が「合計点の機械的順位」を強制する場合でも、**内部の根拠会話は省略しない**。対外手続と内部キャリブレーションは別物  
- 事実が揃ったあとの risk appetite の差は、無理に同一点にしない  

---

## Problem

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Applies to:** vendor proposal evaluation, interview evaluation, architecture review, option comparison

---

## Pattern

> **Scoring makes judgment visible. Calibration makes judgment reliable.**

評価を点数化しても、判断が自動的に客観化されるわけではない。

評価者は異なる。

- experience
- domain knowledge
- interpretation
- risk tolerance
- evidence noticed
- preference

その差を隠すのではなく、**点差として見えるようにし、差が大きいところを会話する**。

---

## Problem

複数評価者で提案を採点すると、同じ提案・同じ評価項目でも点が異なる。

よくある誤った対応:

- 平均点を取る
- 中央値を使う
- 多数決する
- 評価項目をさらに細かくする
- 係数を増やす

これらは差を処理しているだけで、差の理由を解いていない。

---

## Why variance matters

点差はノイズとは限らない。

例えば:

- 一人だけ重要な技術リスクに気づいた
- 要件の解釈がチーム内で違う
- 提案書の記述が曖昧
- 評価基準が曖昧
- 評価者が事実ではなく好みを採点した
- 業務側とIT側で重要度が違う

したがって variance は、**評価品質の診断信号**として使える。

---

## Operating model

```text
Independent review
      ↓
Evidence recorded
      ↓
Initial score
      ↓
Variance detection
      ↓
Calibration discussion
      ↓
Agreed rationale
      ↓
Final judgment
```

---

## Step 1 — Independent evaluation

最初から会議で評価しない。

各評価者が独立して以下を記録する。

- judgment / score
- evidence
- rationale
- concern
- question

集団思考を避ける。

---

## Step 2 — Detect meaningful variance

Calibration 対象例:

- Good vs Poor
- 100 vs 0
- acceptable vs unacceptable
- shortlist decision changes depending on evaluator
- evidence interpretation differs
- risk severity differs

すべての小さな差を会議しない。

---

## Step 3 — Calibrate the question before the score

最初に聞く。

> 我々は同じ問いを評価しているか。

次に:

1. What requirement are we evaluating?
2. What evidence are we using?
3. What does “good” mean here?
4. Is the disagreement factual or judgmental?
5. Is there missing information?
6. Does the vendor need to clarify?

---

## Step 4 — Keep valid disagreement when needed

Calibration = 全員同じ点にすることではない。

事実が揃っても、risk appetite や経営判断で意見が異なる場合がある。

その場合:

```text
Fact agreement
+
Interpretation A
+
Interpretation B
+
Decision owner
```

として残す。

---

## Step 5 — Convert uncertainty into action

評価差の原因が情報不足なら:

- clarification
- re-proposal
- interview
- reference check
- estimate breakdown
- architecture deep dive

へ変換する。

「評価者の意見が割れた」で止めない。

---

## Calibration record

最低限残す。

```md
Evaluation item:
Initial ratings:
Material variance:
Evidence:
Reason for variance:
Agreed interpretation:
Remaining disagreement:
Action:
Final judgment:
```

---

## Anti-pattern — Mathematical objectivity

精緻な重み、係数、小数点付き点数を使うほど客観的に見える。

しかし、入力判断が弱ければ精緻さは錯覚。

> **Do not use mathematical precision to hide judgment uncertainty.**

---

## Anti-pattern — Middle-score gravity

奇数段階評価では、判断を避けて真ん中に集中しやすい。

対策:

- 評価定義を明確にする
- evidence を必須にする
- 明確な選択肢を使う
- midpoint を「わからない」の代用にしない

必要なら偶数段階（本 OS の既定は 0–3）や Good / Partial / Poor を使う。記号の種類を混ぜて精緻化したつもりにしない。

---

## Anti-pattern — Consensus pressure

上位者の評価を先に共有し、他評価者が寄せる。

独立評価を先に行う。

---

## When to use

- vendor selection
- PM / key-person interview
- architecture options
- proposal review
- PoC evaluation
- risk assessment

---

## Decision principle

Score is an input.

Final decision should be explainable as:

```text
Evidence
→ Interpretation
→ Risk / value
→ Trade-off
→ Decision
```

総合点だけで説明しない。

---

## Related files

- `standards/vendor-proposal-evaluation.md`
- `standards/vendor-key-person-interview.md`
- `playbooks/private-it-rfp-vendor-selection.md`
- `knowledge/patterns/reproposal-as-uncertainty-reduction.md`
