# Service Transition Approach Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Application outsourcing transition methodology (~2015), generalized from transition planning patterns. No client names, FTE counts, site names, or calendar-specific schedules.

---

## Purpose

Define how to **plan and execute service transition** from client incumbent or implementation partner to the target AMS operating model — from contract signature through steady-state service start.

Transition is where most outsourcing deals fail or succeed. This framework covers **Phase 4** of `frameworks/application-outsourcing-solution-planning.md`.

Do not use this file as a stand-in for **client transformation** or **solution realization**. Those are separate jobs and cost plans: `knowledge/patterns/transition-vs-transformation-vs-realization.md`. IO take-on shape (as-is vs transformed-only) is in `frameworks/infrastructure-outsourcing-solution-planning.md`.

---

## When to Use

- Solution Planning: transition section of RFP response
- Contract award → delivery kickoff
- Multi-wave take-on (legacy + new ERP modules)
- Handover from ERP implementation partner to AMS provider

---

## Core Principles

1. **Joint planning** — Client and provider co-own transition; neither side "hands off" passively.
2. **Wave-based take-on** — Sequence by risk, dependency, and readiness; avoid big-bang unless proven.
3. **KT before responsibility** — Knowledge transfer quality gates precede operational ownership dates.
4. **Parallel workstreams** — Program, service management, KT, tooling, and readiness run concurrently.
5. **Explicit completion criteria** — System Responsibility Date (or equivalent) is defined per wave, not assumed.
6. **Governance with SME access** — Client subject-matter experts, tool access, and documentation are contractual enablers.

---

## Transition Lifecycle

```text
Plan          Joint transition plan, waves, RACI, governance
Prepare       Environment, tools, access, transition team mobilization
Assess KT     KT readiness evaluation (documentation, SMEs, volume samples)
Execute KT    Structured transfer, shadowing, reverse shadowing
Pilot / parallel run   Limited production support with fallback
Responsibility transfer   Formal service start per wave
Steady state  Hypercare exit, BAU operating model
```

---

## Wave Planning

Split take-on when:

- Application estates differ in maturity (legacy vs new ERP)
- Geographic or language coverage ramps in stages
- Incumbent vendor contracts end on different dates
- Risk concentration in specific towers (e.g., integrations)

Each wave defines:

| Element | Content |
|---------|---------|
| **Scope** | L2/L3 towers included |
| **Start / end** | Planning window and responsibility date |
| **Prerequisites** | Access, data, incumbent cooperation |
| **Exit criteria** | SLA-ready operations, open issue threshold |
| **Fallback** | Rollback or extended parallel run triggers |

---

## Parallel Workstreams

Run these workstreams in parallel under a **Transition Program** (see `frameworks/transformation-pmo.md` for governance patterns):

| Workstream | Focus |
|------------|--------|
| **Program management** | Plan, status, risks, steering, dependencies |
| **Service management design** | SLAs, reporting, incident/problem processes, tools |
| **Knowledge transfer** | KT plan, sessions, artifacts, competency sign-off |
| **Tooling & environment** | Ticketing, monitoring, CMDB, remote access |
| **Workforce & readiness** | Hiring, training, shadowing, language coverage |
| **Commercial / contract** | Scope clarifications, change control during transition |

---

## Knowledge Transfer (KT)

### KT assessment (before execution)

- Documentation inventory and gap analysis
- SME map and availability calendar
- Sample ticket / change history representativeness
- Environment and data access readiness
- Language and time-zone coverage gaps

### KT execution methods (generic)

| Method | Use when |
|--------|----------|
| **Structured sessions** | Process, application overview, key scenarios |
| **Job shadowing** | Incumbent performs; incoming team observes |
| **Reverse shadowing** | Incoming team performs; incumbent validates |
| **Runbook / playbook build** | Tacit knowledge capture into operational artifacts |
| **Pilot support** | Limited production tickets with escalation path |

**Sign-off:** Competency criteria per tower before responsibility transfer.

---

## Milestone Types (Generic)

Use client-appropriate names; typical sequence:

| Milestone | Meaning |
|-----------|---------|
| **Transition kickoff** | Joint plan approved, teams mobilized |
| **KT complete (wave n)** | Competency sign-off for wave scope |
| **Parallel operations start** | Incoming team handles scoped volume with fallback |
| **System / service responsibility date** | Incoming team owns SLA for wave scope |
| **Hypercare end** | Enhanced support period closes; BAU model |
| **Transition close** | All waves complete; program formally closed |

Durations vary by scope — document **drivers** (app count, KT quality, access delays), not copied week counts from historical deals.

---

## Client Joint Governance

Transition requires active client participation:

| Client obligation | Why it matters |
|-------------------|----------------|
| SME time for KT | Cannot transfer tacit knowledge without experts |
| Timely tool and system access | Blocks shadowing and parallel run |
| Incumbent cooperation | Dual-vendor periods need explicit rules |
| Decision forum | Scope clarifications during transition |
| Acceptance of completion criteria | Prevents premature responsibility transfer |

Embed in transition plan and contract schedules where appropriate.

---

## ERP Implementation → AMS Handover

Common pattern when AMS follows packaged ERP go-live:

- Implementation partner retains hypercare; AMS provider ramps in parallel
- KT from implementation team on configured modules
- Wave alignment to **module go-live sequence**
- Interface and batch jobs often transition last

Reference: `frameworks/sap-implementation-phase-model.md`, `standards/operations-handover-guide.md`.

---

## Risks & Mitigations (Typical)

| Risk | Mitigation |
|------|------------|
| Incomplete documentation | KT assessment gate; extended parallel run |
| SME unavailability | Contractual SME allocation; executive escalation |
| Incumbent non-cooperation | Dual-vendor governance; exit clauses |
| Tool access delays | Early environment workstream; critical path tracking |
| Scope ambiguity at responsibility date | Per-wave exit criteria tied to L3 scope |
| Volume surge at transition | Surge staffing plan; hypercare definition |

---

## Related Files

- `frameworks/application-outsourcing-solution-planning.md`
- `frameworks/infrastructure-outsourcing-solution-planning.md`
- `knowledge/patterns/transition-vs-transformation-vs-realization.md`
- `frameworks/ams-services-pyramid.md`
- `standards/ams-solution-plan-checklist.md` §Service Introduction
- `frameworks/transformation-pmo.md`
- `standards/operations-handover-guide.md`
- `knowledge/index/legacy-source-index.md` — Program Line J
