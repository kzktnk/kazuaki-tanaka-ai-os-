# AI Management Office Framework

**Version:** v1.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Generalized from AI adoption foundation (Initiative C) — organization, process, and technology enablement. CoE vs PgMO vs Change phase-shift from later method notes (no vendor catalogue).

---

## Purpose

Describe the **operating structure** for sustained AI adoption: not a one-time project office, but coordination across use cases, platforms, governance, and HR.

Pairs with:

- `frameworks/ai-adoption-roadmap.md` — Initiative C and Year 1 foundation  
- `frameworks/ai-role-maturity.md` — roles the office develops and connects  
- `frameworks/ai-governability.md` — authority and risk rules the office helps enforce  

---

## When to Use

- Designing a **Center of Excellence (CoE)** or AI management function  
- Scoping Year 1 foundation work (rules, owners, champions)  
- Distinguishing **program PgMO** (portfolio) from **AI CoE** (capability)  

---

## Core Functions

| Function | Owner role (typical) | Year 1 focus |
|----------|----------------------|--------------|
| **Standards & patterns** | Developer + Governor | Usage policy, reference architectures, UC templates |
| **Use case intake & prioritization** | Manager + Executive sponsor | 100 → 10 UCs; outcome linkage |
| **Governance operations** | Governor | Usage review, data access, approval paths |
| **Enablement & champions** | Manager + User champions | Training, community, field support |
| **Platform & integration** | Developer | RAG, APIs, EAM/APM/data product links |
| **HR / skill alignment** | Manager + HR partner | Skill visibility, learning plans, triggers |

---

## Three Pillars (Initiative C)

```text
Organization & people   … CoE, champions, executives, HR links
Process                 … intake, review, change control, audit
Technology              … platform standards, dev practices, LLMOps path
```

Do not treat technology as the only pillar — Year 1 failures are usually process and people (`ai-adoption-roadmap.md`).

---

## CoE vs PgMO

| | **AI CoE / management office** | **PgMO** |
|---|-------------------------------|----------|
| Scope | AI capability, standards, reuse | Multi-project portfolio, dependencies |
| Horizon | Ongoing | Program-bound (may persist) |
| Typical home | Digital / IT + business sponsors | Transformation or PMO |

Both may exist; clarify interfaces so AI pilots are not orphaned between project PMs and enterprise AI standards (`frameworks/transformation-pmo.md`).

**Change is a third office**, not a CoE workstream and not a PgMO status slide. Weight moves: plan (CoE + PgMO) → build (PgMO) → run (Change), with CoE governance remaining. Full split: `knowledge/patterns/ai-coe-vs-pgmo-vs-change.md`.

**Shape:** scarce talent → central CoE. Then return people to the line (**hybrid**). Scattered SMEs only: local speed, no enterprise view. Central forever: the line never owns the work.

---

## Maturity Path

| Phase | Office emphasis |
|-------|-----------------|
| Year 1 | Charter, policies, intake, first champions, data owner registry |
| Year 2 | UC factory lite, governance ops, developer guild |
| Year 3 | Workflow design support, embedded governors in domains |
| Year 4–5 | LLMOps, enterprise catalog, federated enablement |

---

## Related Files

- `frameworks/ai-adoption-roadmap.md`
- `frameworks/ai-role-maturity.md`
- `frameworks/governance-operating-model.md`
- `frameworks/transformation-pmo.md`
