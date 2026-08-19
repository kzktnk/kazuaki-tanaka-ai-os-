# Public Sector & Defense IT Domain

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Parent file for reusable Japan public-sector / defense IT consulting knowledge  
**Does not contain:** ministry or force names, program identifiers, yen, bid prices, system inventories, network designs, personal data, current proposal text

---

## Purpose

省庁・防衛の情報システム案件で毎回ゼロから「この世界の拘束」を説明し直さないための Domain 親ファイル。

- **縦軸（官側ライフサイクル）:** 構想 → 要件 → 調達設計 → 見積精査／選定 → 構築PMO → 運用・情報保証  
- **横軸:** 買手支援か売手提案か。**同じプログラムで混ぜない。**

既存の厚い資産（方式〜要件、ベンダー評価）はここに再掲しない。Domain は **拘束と役割** だけを持つ。

作業を始める前に役割を分類する。分析の途中で決めない。

将来の分離先（厚くなったら。**今は分割しない**）:

- `domains/public-defense/procurement.md`
- `domains/public-defense/security-assurance.md`
- `domains/public-defense/defense-it.md`
- `domains/public-defense/public-program-governance.md`

---

## How to use

作業開始前に `Buyer / seller boundary` を読む。  
官側の調査〜要件なら `frameworks/program-phases-investigation-to-requirements.md`。  
調達仕様・評価基準・見積精査なら `frameworks/public-it-procurement-support.md`。  
民間と同じ「提案を勝つ」話なら SI / IO / AMS の枠を使い、この Domain で **保全・総合評価・分割調達** だけ足す。

Technology 製品手順は書かない。系統図・機器一覧・拠点数は **原本に残し、リポジトリに入れない。**

---

## Industry structure

### Principle

**公共ITは「大きい民間」ではない。** 少なくとも次が同時に効く。

| 拘束 | 実務への意味 |
|------|----------------|
| 会計・契約 | 単年度、仕様書と対価の対応、変更は契約行為 |
| 総合評価 | 価格点と技術点。適合条件を満たさない提案は採点前に落ちる |
| 公平性 | 官側支援者は特定ベンダーに寄り添わない。精査コメントは全社に同じ土俵 |
| 保全 | 立入、資料持出、情報区分。提案のうまさより先に運用できるか |
| 標準 | 政府のIT標準ガイドライン類は「参考」ではなく工程の骨格になり得る |

防衛は上記の **厳格なインスタンス**（情報保証、訓令、許可された場所での作業）。論理は公共と同じ。固有の系統構成は書かない。

### Principle — specification, contract, delivery, and acceptance are linked

In public IT, the chain is:

```text
Requirement
        → Specification
        → Evaluation
        → Contract
        → Deliverable
        → Acceptance
```

A requirement that is not expressed in the specification may not be enforceable later.  
A deliverable that cannot be tied back to the contracted scope creates acceptance risk.

Therefore:

- requirement traceability matters
- deliverable definitions matter
- acceptance criteria matter
- scope changes are not merely project-management events

民間でも同じ連鎖はある。公共では **契約行為との結びつきが強い**。

---

## Buyer / seller boundary

Public-sector consulting must explicitly classify the engagement role **before any analysis begins**.

**同じプログラムで買手支援と売手提案を混ぜない。**

### Buyer-side support

Objective:

- define requirements
- structure procurement
- evaluate proposals
- verify estimates
- support governance and acceptance

Quality criteria:

- neutrality
- reproducibility
- traceability
- equal treatment
- evidence-based challenge

### Seller-side proposal

Objective:

- maximize proposal value within procurement rules
- demonstrate compliance
- differentiate delivery capability
- build a viable solution and commercial model

Quality criteria:

- requirement coverage
- evaluation-point alignment
- delivery feasibility
- risk control
- financial viability

### Rule

Never reuse buyer-side confidential reasoning, evaluation logic, vendor-specific findings, or pricing insight to improve a seller-side proposal.

The frameworks may be similar.  
The information boundary is not.

See `knowledge/patterns/buyer-vs-seller-in-public-procurement.md`.

---

## Engagement types — buyer side

材料の主座はローカル原本。リポジトリには **型** のみ。

| 型 | 問うこと | 典型成果 |
|----|----------|----------|
| 次期構想・要件 | 何を残し、何を換装し、方式をどう切るか | 調査研究、方式比較、要件書（Phase 100–500） |
| 調達支援 | 何を買い、どう評価し、仕様をどう書くか | 実施計画、調達方式比較、総合評価基準、仕様・適合条件 |
| 見積精査 | 提案価格は何の作業量か。過不足はどこか | ベースライン、評価基準、ヒアリング、精査報告 |
| 構築PMO | 契約後、官側は何を見て止めるか | 進捗・課題・変更・検収の官側PMO |
| CIO／計画支援 | 横断の優先と予算の言い方 | 短い助言。個別仕様の代筆ではない |

構想と調達仕様は別契約になりやすい。**要件がFIXする前に仕様書を書き始めない**（既存の要件書ゲートと同じ）。

---

## Engagement types — seller side

応札は SI の三角制約と同じ（買える × 届く × 財務）。公共では加えて:

- 評価項目の区分（必須／任意）に提案を **対応づけて** 書く  
- 関連する分割調達（運用、申請、監査など）があるなら、**自社ロットだけ最適化しない**  
- 契約後に対象一覧が確定する前提なら、着手後調査を計画に書く  
- 社内の Solution Baseline / 提案前レビューは、見積・WBS・役割・検収を tick-and-tie する場（中身の金額は登録しない）

NIST SP 800-37 / 800-53 等は **参照クラス**。章を転載しない。情報保証の中身は下記 Security / RMF 節。

---

## Procurement & estimate review principles

手続の詳細は `frameworks/public-it-procurement-support.md`。Domain は判断だけ。

### Principle — estimate review is not price negotiation

Estimate review asks:

1. What work is being performed?
2. What volume drives the effort?
3. What role / skill is required?
4. What assumptions drive the estimate?
5. What is fixed, variable, or uncertain?
6. Where is duplication or omission?
7. Which risks are priced separately?

The objective is not simply to reduce the number.  
The objective is to establish whether the price corresponds to a defensible work model.

### Principle — do not fabricate inventory certainty

At procurement or early design stages, exact inventories, locations, quantities, interfaces, or transition constraints may still be unknown.

When unknown:

- state the assumption
- define the confirmation activity
- define who owns confirmation
- define when the information must become fixed
- define what changes if the assumption is wrong

Do not fill gaps with plausible numbers merely to make the plan look complete.

---

## Assurance & evidence

In regulated public-sector work, compliance is not only about performing the control.

It is also about being able to demonstrate that the control was:

- defined
- assigned
- executed
- reviewed
- approved
- retained as evidence

Evidence quality therefore becomes part of delivery quality.

Typical evidence concerns include:

- version control
- approval history
- traceability
- configuration state
- test records
- exception records
- remediation status

これは RMF だけでなく、公共ITの監査・検収にも効く。

---

## Security / RMF support principles

### Principle — authorization responsibility remains with government authority

Security assurance support may:

- prepare evidence
- facilitate assessment
- track remediation
- support documentation
- provide technical advice

It does not transfer:

- authorization authority
- mission-risk acceptance
- formal accountability

Support can structure the decision.  
It cannot own the government decision.

See `frameworks/decision-ownership.md`, `frameworks/human-oversight.md`.

実務の型（制度のコピーではない）:

- 脆弱性検査を伴う／伴わない分析は別作業として切る。官作業の進捗把握と請負範囲を混同しない  
- 未習熟の担当が本業の傍らで書くなら、選択式・記入要領・ガイドが本体より先に効く  
- マルチベンダーならスケジュールとロットのすり合わせがクリティカルパス  

---

## Do not mix

- 発電・小売の論理を省OAに持ってこない（逆も）。共通なのは権限・記録・現場例外だけ。  
- **同じプログラムで買手支援と売手提案を混ぜない。**

### System delivery vs assurance operation

System engineering answers:

> How should the system be designed and implemented?

Assurance operation answers:

> How should risk, evidence, review, authorization, and exceptions be governed?

They interact, but they are not the same workstream.

Do not treat security governance as a technical appendix to system design.  
防衛の構築仕様と、RMF 制度運用支援は別仕事。システムを「知っている」ことと制度を回すことは同じ提案に雑に載せない。

---

## Common failure patterns

- 民間 SI の Solution Plan を、官側の調達支援成果物だと思い込む  
- 官側の公平な精査ロジックを、自社の応札価格作りに流用する  
- 仕様に書いていない要求を、後工程の「常識」で検収しようとする  
- 見積精査を値引き交渉にする  
- 未確定の対象件数・拠点を、計画を埋めるために仮置きする  
- 情報保証の認可を、支援ベンダーの成果物で代替したつもりになる  

---

## Related files

| Layer | File |
|-------|------|
| Domain parent | this file |
| Framework | `frameworks/public-it-procurement-support.md` |
| Pattern | `knowledge/patterns/buyer-vs-seller-in-public-procurement.md` |
| Decision | `frameworks/decision-ownership.md`, `frameworks/human-oversight.md` |
| Index | `knowledge/index/legacy-source-index.md` Program Line P |
| Migration | `knowledge/migrations/public-defense-2026-08.md` |
