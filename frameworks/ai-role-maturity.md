# AI Role Maturity Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Five-role × phased maturity model for AI adoption, generalized from internal HR roadmap practice. No client-specific level tables or year-by-year task breakdowns.

---

## Purpose

Define **who** must mature **how**, synchronized with the technology roadmap in `frameworks/ai-adoption-roadmap.md`.

Five roles cover the minimum set for governable AI at scale. Maturity is expressed as **phases** (Year 1–5 narrative) for executives and **levels** (1–5) for program design — do not expose raw level grids to executives.

---

## When to Use

- HR / L&D planning tied to AI programs  
- CoE and governance staffing  
- Workshop design: map questions to role + phase  
- Internal WBS for skills, champions, and control bodies  

---

## Five Roles

| Role | Primary accountability |
|------|------------------------|
| **User (利用者)** | Safe daily use; domain judgment; validates AI output |
| **Manager (管理者)** | Usage rules, escalation, **workflow design** with AI embedded |
| **Governor (統制者)** | Risk, usage review, audit, policy enforcement |
| **Developer (開発者)** | Build, integrate, quality, LLMOps |
| **Executive (経営者)** | Investment, risk appetite, transformation sponsorship |

Initiative C (AI adoption foundation) maps: organization & people → User / Manager / Executive; process → Governor; technology → Developer (`ai-adoption-roadmap.md`).

---

## Maturity Levels (Design Language)

Abstract progression — align to your organization's L&D taxonomy as needed.

| Level | User-oriented label | Typical evidence |
|-------|---------------------|------------------|
| **1** | Understand | AI risks, rules, acceptable use |
| **2** | Use | Daily tasks with approved tools / UCs |
| **3** | Improve | Proposes workflow improvements; structured exceptions |
| **4** | Collaborate | Human–AI split is routine; mentors others |
| **5** | Lead | AI-native assumptions; drives domain standards |

Not every role must reach Level 5. Year 1 target is often **Level 1 across roles**.

---

## Role × Phase Matrix (Simplified)

Executive-facing summary — detail internally as needed.

| Role | Year 1–2 | Year 3–4 | Year 5 |
|------|----------|----------|--------|
| **User** | Safe use; daily adoption | Business improvement; human–AI split | Field leadership |
| **Manager** | Usage control; escalation | **Embed AI in workflows (HITL design)** | Operating model change |
| **Governor** | Risk literacy; usage review | Control operations; audit | Enterprise policy |
| **Developer** | LLM / RAG basics | Quality, monitoring, LLMOps | Enterprise AI platform |
| **Executive** | Impact awareness | Investment & risk decisions | AI-assumed strategy |

**Year 3 is the manager-centric year** — BPR and workflow integration before pushing autonomous agents.

---

## Education Design Principles

1. **Shift from knowledge transfer to judgment support** — expertise amplification, not replacement (`knowledge/patterns/expertise-amplification.md`).
2. **Formalize judgment types**, not exhaustive manuals — when / what to check / what to prioritize.
3. **Experts as reviewers** — veterans validate AI output; they do not write every artifact.
4. **Exception libraries** — capture workarounds and edge cases; 100% codification is not the goal. This is the operational layer of **organizational memory** (`knowledge/patterns/organizational-memory.md`). Libraries are useful when they return at the decision (`knowledge/patterns/memory-at-decision.md`). Recurring exceptions with consistent reasoning may need to change the standard (`knowledge/patterns/standard-as-learned-memory.md`) — not stay exceptions forever.

Initiative B (tacit → explicit knowledge) peaks in **Year 2–3**.

---

## HR Integration

### Three-layer capability model

| Layer | Horizon | Examples |
|-------|---------|----------|
| **Core** | Annual | Safety, regulation, equipment judgment |
| **Domain** | Quarterly | Program themes (AM, BPR, DX) |
| **Mission** | Per project | PoC, pilot plant, single UC |

### Update triggers

- New project or UC launch  
- Major incident  
- Regulatory change  
- Business redesign from AI  

### Granularity

Manage **Capability × role × phase**, linked to SCN or program capability gaps when available (`frameworks/capability-model.md`, `strategic-capability-network.md`).

Initiative C tasks such as **skill visibility and learning plans** should use the same triggers as HR updates.

---

## Future-Scarce Profiles (Illustrative)

Roles that typically grow in importance rather than disappear:

1. Domain expert who **governs** AI output  
2. Process architect (BPR + agent flows)  
3. Data product owner (SSOT and quality)  
4. Human–AI workflow designer  
5. Plant- or site-level change leader  

Relative decline: routine search, templated reporting, simple pattern matching.  
Relative rise: anomaly judgment, trade-offs, verification and **accountability for AI output**.

---

## Distinction from General Maturity

| Model | Scope | File |
|-------|-------|------|
| Organization / process CMMI-style | Broad transformation | `frameworks/maturity-model.md` |
| **AI role maturity** | AI-specific roles and phases | This file |

Use both: general maturity for enterprise assessment; role maturity for AI program execution.

---

## Related Files

- `frameworks/ai-adoption-roadmap.md`
- `frameworks/ai-management-office.md`
- `frameworks/ai-governability.md`
- `knowledge/patterns/expertise-amplification.md`
- `knowledge/patterns/organizational-memory.md`
- `knowledge/lessons/dual-roadmap-messaging.md`
- `knowledge/migrations/ai-dual-roadmap-2026-08.md`
