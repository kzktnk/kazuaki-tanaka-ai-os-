# IT Strategy Engagement Guide

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Framework:** `frameworks/it-strategy-foundations.md`

---

## Purpose

Operational standard for **IT strategy engagements** — formulation, architecture, sourcing, implementation planning, and value analysis. Use as a phase checklist when scoping, facilitating, or reviewing IT strategy work.

---

## Engagement Entry Checklist

Before deep analysis:

- [ ] Client has (or is developing) business strategy context — not IT-only
- [ ] Triggers documented (cost, capability, delivery failure, digital pressure, M&A, etc.)
- [ ] IT strategy category identified (conservation / experimentation / evolution / consolidation / transformation)
- [ ] Sponsor and decision criteria for IT investment agreed
- [ ] Scope covers Insight + Architecture + Investment — or explicit subset with rationale

---

## Phase 1 — IT Strategy Formulation

### Scenario planning checklist

- [ ] PEST or equivalent macro scan completed
- [ ] Industry / value-chain impact analysis (customers, channels, competitors, substitutes, suppliers)
- [ ] Time horizon set (lead time + planning cycle + uncertainty visibility)
- [ ] Uncertainty factors listed and plotted (impact × uncertainty)
- [ ] Top drivers selected; interactions mapped
- [ ] 2–4 distinct scenarios named and narrated
- [ ] Static business model documented per competitor/archetype
- [ ] Dynamic business model (feedback loops) assessed per scenario
- [ ] Strategies defined per scenario
- [ ] Strategies classified: execute now / execute if triggered / real options

### IT options checklist

- [ ] Current IT diagnosed (management perception, competitive role, org environment, technical state)
- [ ] IT strategy grid populated for major applications
- [ ] Value-chain IT opportunities identified
- [ ] 5 Forces IT opportunities assessed (optional but useful for external pressure)
- [ ] IT capability assessment completed (current state)
- [ ] To-Be capability target defined
- [ ] Gaps and new IT-enabled capabilities listed
- [ ] **BSA** drafted (processes × drivers → business systems)
- [ ] Each IT option scored against evaluation criteria (vision, CSF/KPI, market, emerging tech, value creation)

### BSA template (conceptual)

| Process stage → | Stage 1 | Stage 2 | … |
|-----------------|---------|---------|---|
| **Driver A** | System/capability | | |
| **Driver B** | | | |

Layers (when useful): strategic / tactical / operational.

---

## Phase 2 — Architecture Design

### Current-state assessment

- [ ] Business system requirements reflected in assessment scope
- [ ] Assessment wheel applied (~20+ elements across strategy, delivery, technology, people)
- [ ] Application inventory with functional and technical quality rated
- [ ] Gap list: required vs current support level

### Conceptual architecture (IATO)

**Information**

- [ ] Major information domains identified
- [ ] Shared vs local vs duplicated data classified
- [ ] KM, DW, OLAP, compliance, operational records positioned

**Applications**

- [ ] BSA mapped to application domains
- [ ] ERP / best-of-breed / legacy renewal decisions framed
- [ ] Integration approach for new vs legacy stated

**Technology**

- [ ] Platform layers described (processor → OS → DB → network → API → apps → presentation)
- [ ] Web/e-commerce infrastructure requirements captured
- [ ] Component/building-block strategy noted

**Organisation**

- [ ] Target IT structure (centralized / federated / shared services / virtual / outsourced)
- [ ] Governance model selected (facilitator / arbiter / dictator pattern)
- [ ] Roles, skills, sourcing implications documented

### Implementation architecture

- [ ] Constraints explicit: cost, risk, time-to-solution, time-to-benefit
- [ ] Phasing / transition approach defined
- [ ] Output usable as **system investment guidelines**

---

## Phase 3 — Value Analysis

Run at **option comparison**, **architecture choice**, **sourcing decision**, and **program business case**.

### Business case structure

| Element | Content |
|---------|---------|
| **Strategic rationale** | Link to drivers, scenarios, BSA |
| **Benefits** | Tangible (cost, revenue, working capital) + intangible (speed, quality, flexibility) |
| **Costs** | Initial + running; by year |
| **Cash flow** | FCF or appropriate metric |
| **Valuation** | NPV, ROI, payback — per client standards |
| **Terminal value** | Method stated (perpetuity, growth, harvest, etc.) |
| **Uncertainty** | Sensitivity and/or scenarios on key assumptions |
| **Risks** | Implementation, technology, adoption |

### Valuation quick reference

| Concept | Use |
|---------|-----|
| **FCF** | Cash available after operating and investment needs |
| **Enterprise value** | PV of expected FCF (+ terminal value) |
| **MVA / EP** | Value above cost of capital; positive = value-creating |
| **Project NPV** | PV(benefits) − PV(costs) over project life |

### Uncertainty methods (pick one or more)

- Sensitivity analysis — single-variable swings
- Scenario analysis — discrete futures
- Decision tree — sequential choices
- Simulation — distribution of outcomes
- Real options — value of deferring/expanding/abandoning

### Prioritization

- [ ] Options ranked by strategic fit **and** economic merit
- [ ] Intangibles documented even when not fully monetized
- [ ] Value analysis feeds budget and portfolio — not only final deck

---

## Phase 4 — Sourcing

### Decision flow

1. Assess strategic and business position
2. Map IT functions on IT strategy grid and sourcing grid
3. Evaluate insource vs outsource vs multi-source by function
4. Build business/IT consensus on target sourcing model
5. Package scopes for providers (if external)

### Sourcing checklist

- [ ] Each major IT function classified: outsource candidate vs must retain internal
- [ ] Strategic/core IP services kept internal or under strict partnership
- [ ] Commodity/bounded services evaluated for outsource economics
- [ ] Fully loaded insource cost vs outsource quote compared (≈30–40% gap rule)
- [ ] Contract terms address: change, exit, SLA, technology refresh, competitive bid rights, transfer-back
- [ ] Governance model for provider relationship defined (trust but verify)

### Sourcing grid quick reference

| Quadrant | Presumption |
|----------|-------------|
| Strategic + high env impact | Insource; partnership if outsource |
| Turnaround | Insource |
| Factory | Outsource unless IT org exceptionally strong |
| Support | Outsource |

---

## Phase 5 — Implementation Planning

### Program setup

- [ ] Program charter links to IT strategy and architecture outcomes
- [ ] Projects identified with dependencies (matrix or diagram)
- [ ] Master business case aggregates project cases
- [ ] Executive sponsor and steering cadence defined
- [ ] Change management and communication plan at program level

### Value realization (Balanced Scorecard)

Define metrics in four perspectives aligned to strategy:

| Perspective | Example metrics |
|-------------|-----------------|
| Financial | ROI, cost vs plan, working capital |
| Customer | Satisfaction, retention, market share |
| Operational | Cycle time, error rate, utilization |
| Innovation | New capability readiness, skill build |

- [ ] Few, strategic metrics — avoid metric overload
- [ ] Baseline and target set before major spend
- [ ] Periodic strategy review scheduled

### Program PM tiering

Score each project on **complexity** and **change impact** → assign Tier 1 / 2 / 3 → apply proportional PM process depth.

**Complexity factors (examples):** new vs enhance application, cross-department scope, new technology/domain.

**Change impact factors (examples):** departments affected, process change depth, training breadth.

### Performance reporting (minimum)

Track per project and roll up to program:

- Time: planned vs actual
- Cost: budget vs actual (by category)
- Quality: rework, defects, scope change count
- Benefits: vs business case trajectory

Cross-reference `frameworks/transformation-pmo.md` for PMO operating model.

---

## Deliverable Map

| Phase | Typical deliverables |
|-------|---------------------|
| Formulation | Scenario set, driver matrix, IT options list, BSA, option evaluation |
| Architecture | Gap assessment, IATO conceptual maps, implementation architecture, investment guidelines |
| Value | Option business cases, portfolio comparison, sensitivity/scenario exhibits |
| Sourcing | Target operating model for IT delivery, sourcing strategy, RFP/contract principles |
| Implementation | Program roadmap, dependency/risk registers, master business case, BSC |

---

## Quality Gates

**Before architecture sign-off:**

- [ ] BSA approved by business stakeholders
- [ ] Gaps trace to business requirements, not technology fashion

**Before sourcing decision:**

- [ ] Strategic applications flagged; not bundled into commodity outsource by default

**Before program launch:**

- [ ] Master business case and BSC approved
- [ ] Tier-1 projects have full PM process; lower tiers scaled appropriately

---

## Related Files

- `frameworks/it-strategy-foundations.md` — concepts and lifecycle
- `frameworks/consulting-strategy-process.md` — general strategy and scenario patterns
- `frameworks/transformation-pmo.md` — program governance
- `frameworks/strategic-capability-network.md` — capability mapping post-direction
- `standards/strategy-engagement-guide.md` — 4Cs, logic trees, general strategy toolkit
