# Application Outsourcing Solution Planning Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Application Outsourcing SAE (AOSAE) course structure (~2015), generalized. No client names, vendor tool names, rate cards, or proprietary case numbers.

---

## Purpose

Structure **pre-contract Solution Planning** for Application Management Services (AMS) and application outsourcing engagements — from scope understanding through To-Be design, estimating, delivery sourcing, transition planning, and proposal assembly.

This is the **execution layer** for RFP response and deal shaping. It complements — does not replace — strategic sourcing decisions in `frameworks/it-strategy-foundations.md` §Sourcing. Infrastructure towers use `frameworks/infrastructure-outsourcing-solution-planning.md`.

| Layer | Question | Typical artifact |
|-------|----------|------------------|
| **IT Strategy Sourcing** | Should we outsource this capability? | Sourcing grid, make/buy |
| **AO Solution Planning** (this framework) | How do we win, price, and transition? | Solution Plan, proposal, transition plan |
| **Post-go-live operations** | How do we run and improve? | SLA, operating model, AI adoption roadmap |

---

## When to Use

- RFP / RFQ response for application management or AMS
- Solution Architect (SA) or deal team structuring a multi-year outsourcing bid
- Internal solution review before pricing or contract signature
- Transition planning at contract award (handoff from sales to delivery)

---

## Solution Architect Role

The SA owns **coherent end-to-end design** across scope, operating model, staffing, location, estimating assumptions, transition, and proposal narrative.

| Responsibility | Not the SA alone |
|----------------|------------------|
| As-Is baseline and To-Be delivery model | Legal / contract terms |
| Scope split and services pyramid | Final commercial approval |
| Estimating approach and assumptions | Client-side strategic sourcing policy |
| Transition approach and milestones | Day-to-day service delivery after steady state |
| Solution Plan completeness | Tool-specific pricing engines |

Use `standards/ams-solution-plan-checklist.md` before internal review gates.

---

## Solution Planning Phases

Map a typical three-day Solution Planning curriculum to engagement workstreams:

```text
Phase 1 — Understand & baseline     … scope, As-Is, opportunity context
Phase 2 — To-Be delivery model      … operating model, location, pyramid
Phase 3 — Size & source             … estimating, delivery mix, risks
Phase 4 — Transition design         … waves, KT, governance, readiness
Phase 5 — Solution model & proposal … assumptions, financials, outline
Phase 6 — Review & handoff          … peer/QA, contract to delivery
```

### Phase 1 — Understand & baseline

- Confirm opportunity timeline, stakeholders, and win themes (buyer values)
- Inventory application portfolio in scope (ERP modules, legacy apps, interfaces)
- Capture As-Is: volumes (users, tickets, changes), current org, cost baseline, pain points
- Identify constraints: regulatory, audit, data residency, language, support hours

**Output:** Baseline fact pack, scope boundary draft

### Phase 2 — To-Be delivery model

Design the **future state service** the client will receive after transition:

| Element | Design questions |
|---------|------------------|
| **High-level delivery model** | Governance, service management, service delivery layers |
| **Operating model** | Service desk → L2/L3 → discretionary / enhancement work |
| **Scope split** | Application management vs development vs infrastructure (explicit boundaries) |
| **Location strategy** | Onsite / nearshore / offshore mix and rationale |

See `frameworks/ams-services-pyramid.md` for scope hierarchy.

**Output:** To-Be operating model one-pager, scope split diagram

### Phase 3 — Size & source

- Choose estimating approach by application type (see §Estimating Approaches)
- Build staffing pyramid and experience-level mix
- Decide delivery center placement against decision axes (§Location Strategy)
- Document assumptions, issues, and risks with mitigations

**Output:** Staffing model, location map (generic), assumption register

### Phase 4 — Transition design

- Wave plan (e.g., legacy estate → new ERP modules)
- Knowledge transfer evaluation and execution path
- Parallel workstreams: program, service management, KT, tooling, readiness
- Joint governance with client (SME availability, access, completion criteria)

See `frameworks/service-transition-approach.md`.

**Output:** Transition timeline, milestone list, RACI sketch

### Phase 5 — Solution model & proposal

- Consolidate into Solution Plan sections (checklist-driven)
- Draft client-facing proposal outline
- Financial summary aligned to assumptions (no proprietary rate structures in repo artifacts)

**Output:** Solution Plan, proposal deck per `standards/deliverable-archetypes.md` Archetype I

### Phase 6 — Review & handoff

- Internal peer / quality review against checklist
- Capture review feedback and resolution
- Handoff package for delivery start (Transition team)

---

## As-Is → To-Be Pattern (AMS Domain)

Generalizes `frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md` for outsourcing:

```text
As-Is     Current support model, costs, SLAs, org, tool landscape
Gap       Volume/complexity mismatch, skill gaps, location inefficiency
To-Be     Target operating model, scope, location mix, service levels
```

**To-Be model components** (always explicit in Solution Plan):

1. High-level delivery model (governance / SM / delivery)
2. Operating model tiers (L1 → L3+)
3. Location and organization strategy
4. Scope boundaries across AM / dev / infra

---

## Estimating Approaches

Use the approach that matches data availability and application type. Factor names only — no client-specific hours or FTE in repository artifacts.

### Bottom-up (packaged ERP / well-instrumented apps)

| Factor category | Examples |
|-----------------|----------|
| Scale | User counts, transaction volumes, module count |
| Support profile | Ticket rates, resolution times, change request mix |
| Complexity | Customization depth, interface count, regulatory load |
| Delivery mix | Onsite vs remote ratio, language coverage |
| Productivity | Tooling, automation, knowledge reuse |

### Top-down (legacy / heterogeneous estate)

| Factor category | Examples |
|-----------------|----------|
| Portfolio | Application count, platform diversity |
| Coverage | Support hours, escalation paths |
| Handover | Incumbent vendor transition effort |
| Risk adjustors | Unknown documentation, SME dependency |

### Cross-cutting

- Complexity adjustors (standard / elevated / critical)
- Productivity improvement assumptions (document, do not over-claim)
- Economic indices (COLA, FX) — **concept only** in generalized materials

---

## Location Strategy — Decision Axes

When placing work across onsite, nearshore, and offshore centers:

| Axis | Question |
|------|----------|
| **Skills** | Required depth by tower (ERP functional, technical, language) |
| **Proximity** | Need for onsite presence ( governance, critical incidents ) |
| **Time zone** | Follow-the-sun vs single-shift coverage |
| **Cost–quality** | Pyramid mix vs SLA risk |
| **Data & compliance** | Residency, access, audit constraints |
| **Client preference** | Existing relationships, prior offshore experience |

Do not copy vendor marketing one-pagers or site catalogs into client deliverables.

---

## Pyramid & Experience Mix

Staffing pyramids express **volume at each seniority tier** (e.g., analyst → senior → lead). Experience-level mix balances cost, quality, and risk.

- Align pyramid to **services pyramid** L1/L2/L3 scope (`ams-services-pyramid.md`)
- Higher complexity towers need more senior mix
- Transition periods often need temporary senior-heavy staffing

---

## Post-ERP-Go-Live Context

Large AMS deals often follow ERP implementation. Connection points:

- **Scope timing:** AM scope may ramp as modules go live in waves
- **Reference:** `frameworks/sap-implementation-phase-model.md` for build-phase handover expectations
- **Transition:** KT from implementation partner to AMS provider is a common Phase 4 workstream

Do not embed client ERP history, investment figures, or vendor names in generalized repo content.

---

## Relationship to Other Assets

| Asset | Relationship |
|-------|--------------|
| `it-strategy-foundations.md` §Sourcing | Upstream make/buy; this framework assumes outsourcing is in scope |
| `infrastructure-outsourcing-solution-planning.md` | Infrastructure twin; bundled AO+IO needs an enterprise SA |
| `ams-services-pyramid.md` | Scope hierarchy and Solution Plan TOC |
| `service-transition-approach.md` | Phase 4 detail |
| `ams-solution-plan-checklist.md` | Completeness standard |
| `deliverable-archetypes.md` Archetype I | Client proposal outline |
| `vendor-proposal-evaluation.md` | Client-side evaluation (mirror structure when reviewing competitors) |
| `transformation-pmo.md` | Large transition programs |
| `operations-handover-guide.md` | Operational handover patterns |
| `ai-adoption-roadmap.md` | Post-steady-state improvement (different time horizon) |

---

## Common Failure Modes

| Failure | Mitigation |
|---------|------------|
| To-Be designed before As-Is validated | Phase 1 baseline gate |
| Scope creep across AM / dev / infra | Explicit scope split in pyramid |
| Estimating without documented assumptions | Checklist §Assumptions |
| Transition underestimated | Dedicated Phase 4; joint client governance |
| Proposal narrative disconnected from Solution Plan | Single assumption register; Archetype I alignment |
| Strategic outsourcing debate inside RFP response | Escalate to IT Strategy Sourcing layer |

---

## Related Files

- `frameworks/ams-services-pyramid.md`
- `frameworks/service-transition-approach.md`
- `standards/ams-solution-plan-checklist.md`
- `standards/deliverable-archetypes.md` (Archetype I)
- `knowledge/index/legacy-source-index.md` — Program Line J
