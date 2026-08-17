# AMS Services Pyramid Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Application Outsourcing Services Pyramid templates (~2015), generalized. No client portfolio names or proprietary staffing numbers.

---

## Purpose

Define **scope hierarchy** for Application Management Services (AMS) and application outsourcing Solution Plans.

The services pyramid answers: *what is in scope, at what level of abstraction, and how does it roll up to the Solution Plan?*

Use with `frameworks/application-outsourcing-solution-planning.md` and `standards/ams-solution-plan-checklist.md`.

---

## When to Use

- Structuring RFP scope for AMS / application outsourcing
- Splitting towers (application mgmt, development, infrastructure)
- Aligning staffing pyramids to service tiers
- Building Solution Plan table of contents

---

## Three-Level Hierarchy

```text
L1  Service domain          … e.g., Application Management
L2  Service tower           … e.g., ERP Application Support, Legacy Application Support
L3  Service component       … e.g., Incident Mgmt, Problem Mgmt, Change Support, Enhancement
```

| Level | Definition | Example questions |
|-------|------------|-------------------|
| **L1** | Major service domain in the deal | Is infrastructure in scope or adjacent? |
| **L2** | Logical tower within L1 | ERP vs custom legacy vs integration |
| **L3** | Repeatable service components | Which ITIL-aligned activities are included? |

Each L3 item should be **SLA- or KPI-measurable** or explicitly marked as discretionary / out of scope.

---

## Typical L1 Domains

| L1 Domain | Usually includes | Often excluded |
|-----------|------------------|----------------|
| **Application Management** | L2/L3 support, minor fixes, release support | Major development programs |
| **Application Development** | Enhancements, projects, packaged config | Steady-state break/fix |
| **Infrastructure** | Server, network, middleware ops | Functional ERP support |

Boundary disputes are common — document **in / out / interface** for each L1 in the Solution Plan.

---

## Vertical Depth — Strategy to Operations

Beyond L1–L3, Solution Plans often stack **vertical layers** from execution to governance:

```text
Strategy & relationship     … account governance, innovation roadmap, value reporting
Service management          … SLAs, reporting, continual improvement, demand mgmt
Service delivery            … L1 desk, L2/L3 support, release, environment support
Infrastructure (if in scope) … platform operations underlying applications
```

This vertical stack maps to **To-Be delivery model** sections in `application-outsourcing-solution-planning.md`.

---

## Solution Plan Table of Contents (Generic)

Use as the backbone for internal Solution Plan and client proposal alignment:

| # | Section | Pyramid hook |
|---|---------|--------------|
| 1 | Opportunity overview | Win themes, timeline, baseline |
| 2 | Solution overview | Portfolio in scope, L1 split, delivery model |
| 3 | Detailed solution | L2/L3 breakdown, staffing, location, operating model |
| 4 | Assumptions / issues / risks | Scope boundaries per L3 |
| 5 | Service introduction (transition) | Ramp by tower |
| 6 | Financials & pricing | Sized from L3 volumes |
| 7 | Review feedback | Internal QA record |

Detailed checklist: `standards/ams-solution-plan-checklist.md`.

---

## Mapping to Operating Model Tiers

| Operating tier | Typical L3 components |
|----------------|----------------------|
| **L1 — Service desk** | Ticket intake, routing, known-error workarounds |
| **L2 — Functional / technical support** | Diagnosis, config, data fixes, user support |
| **L3 — Deep technical / vendor liaison** | Code-level fixes, performance, vendor SR coordination |
| **Discretionary / projects** | Enhancements, small projects (often separate L1 or bolt-on) |

Staffing **pyramid** (junior/senior mix) is sized **per L2/L3 tower**, not once for the whole deal.

---

## ERP / Packaged Application Pattern

For packaged ERP AMS, L2 often follows **module or process towers**:

- Finance, logistics, HR, manufacturing, etc. (generic — adapt to client landscape)
- Cross-cutting: interfaces, batch, authorizations, reporting

Post-go-live AM scope typically **ramps by module wave** — align L3 availability to go-live sequence (`sap-implementation-phase-model.md`).

---

## Legacy Estate Pattern

For heterogeneous legacy:

- L2 by **application cluster** or business capability
- L3 by activity type (incident, problem, change, small enhancement)
- Higher unknown complexity → more explicit assumptions in Phase 3

---

## Related Files

- `frameworks/application-outsourcing-solution-planning.md`
- `standards/ams-solution-plan-checklist.md`
- `standards/deliverable-archetypes.md` (Archetype I)
- `frameworks/sap-implementation-phase-model.md`
- `knowledge/index/legacy-source-index.md` — Program Line J
