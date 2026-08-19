---
type: pattern
---

# Pattern — Shared Operator vs Ministry vs Municipality

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Shared Operator vs Ministry vs Municipality  
**Applies to:** Japan local-government shared IT, multi-municipality platforms, buyer-side construction PMO on an operator

**Does not contain:** operator names, program names, inventories, yen, proposal or specification text

---

## Pattern

> **共同利用のIT運用者は、省でも団体でもない第三の発注者である。制度の期限、運用者の契約、団体の窓口は別の成功条件を持つ。一つの「公共案件」に畳むと、ロットごとの請負進捗だけが残る。**

| Actor | Owns | Typical failure if treated as another actor |
|-------|------|-----------------------------------------------|
| **Policy / ministry** | Statute, national deadline, standard | Operator PMO is asked to “explain policy” instead of accepting contracted lots |
| **Shared operator** | Joint platform procurement, operations, executive accountability to members | Work is scoped as one city’s ERP, or as ministry OA procurement design |
| **Municipality / counter / user** | Connection, window, local process | Cutover is declared per SI lot; the operator still cannot run one production story |

The operator is **buyer** of build lots. A firm hired via notice to run 工程管理 is **seller of advisory**, then **buyer-side PMO** toward those lots. Do not reuse bid messaging as quality-gate logic. See `knowledge/patterns/buyer-vs-seller-in-public-procurement.md`.

## Multi-lot acceptance is one story

Concurrent lots (core, facility or site move, new channel) congest tests and documentation. Success is not three green traffic lights. Success is:

- the operator can **start** the next stage (開始判定) with evidence, not with a status meeting
- operational procedures from several vendors **merge** before service-in
- executives hear residual risk at their altitude; working PMO keeps the registers

Integrated drawings and procedure bodies stay in the original pack. Generalized knowledge is the **gate**, not the diagram.

## Tests

- If we removed the operator, would this still be a ministry program or a single-city program? If yes, the actor map is wrong.  
- Can each lot claim done while the operator cannot accept or operate? If yes, the PMO is still vendor-shaped.  
- Are we writing a **提案の評価対応** or a **次工程を始めてよいかの証拠**? The former is seller; the latter is buyer-side construction PMO.

## Related

- `domains/public-defense.md`（共同利用の第三アクター）
- `playbooks/public-multi-lot-construction-pmo.md`
- `frameworks/public-it-procurement-support.md` §Construction-phase PMO
- `playbooks/pmo-function-standup.md`（改革PMOの立ち上げ。法定の複数ロット切替には使わない）
