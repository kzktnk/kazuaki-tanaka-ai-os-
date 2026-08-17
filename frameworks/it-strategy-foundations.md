# IT Strategy Foundations Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Source:** Legacy IT Strategy Foundations training materials (2002), generalized and anonymized. Original PDFs remain local; not committed.

---

## Purpose

Define the **end-to-end IT strategy engagement model** — from business-driven IT vision through architecture, sourcing, implementation planning, and value analysis.

Use this framework when:

- Scoping an IT strategy, digital transformation, or enterprise architecture engagement
- Linking business strategy scenarios to IT options and investment choices
- Designing target IT architecture (information, applications, technology, organization)
- Deciding insource vs outsource vs multi-source
- Planning multi-project IT programs with measurable value realization

This complements:

- `frameworks/consulting-strategy-process.md` — general strategy problem structuring and scenario work
- `frameworks/strategic-capability-network.md` — capability and enabler mapping after direction is set
- `frameworks/transformation-pmo.md` — program governance and portfolio execution
- `frameworks/transformation-roadmap.md` — phased delivery narrative

---

## Why Clients Need IT Strategy

Clients typically seek two things:

1. **IT vision** — direction aligned with business ambition
2. **Detailed plan** — how to realize that vision with measurable outcomes

Common triggers (pattern, not client quotes):

- IT consumes too many resources with unclear return
- Current systems cannot support the business
- Users are chronically dissatisfied with IT delivery
- Projects rarely finish on time, on budget, at quality
- Internet/digital is obviously important but path is unclear
- M&A, global expansion, or supply-chain integration need flexible IT

**IT role evolution:**

| Era | IT role | Investment logic |
|-----|---------|----------------|
| Old economy | Constraint; tactical service | Cost-based; incremental budget; application-centric |
| Transition | Enabler and driver | Option-based; intangible benefits; process/information-centric |
| New economy | Strategic business partner | Value-based; competitive advantage; time-to-market |

---

## Three-Stage Model: Insight → Architecture → Investment

| Stage | Value delivered |
|-------|-----------------|
| **Insight** | Understand current IT capability and future possibilities; assess business impact |
| **Architecture** | Design a feasible target — information, applications, technology, organization |
| **Investment** | Manage funding, portfolio, and change to deliver the chosen architecture |

**Scope principle:** IT strategy work must consider **business strategy and processes**, not IT in isolation.

Supporting enablers across all stages:

- Program / portfolio management
- IT investment forecasting
- Change management

---

## Five Workstreams

| # | Workstream | Primary output |
|---|------------|----------------|
| 1 | **IT strategy formulation** | Scenarios, business/IT drivers, strategic IT options |
| 2 | **Architecture design** | Conceptual and implementation architecture (IATO) |
| 3 | **Value analysis** | Business case, prioritization, benefit/cost quantification |
| 4 | **Sourcing** | Insourcing, outsourcing, or multi-sourcing strategy |
| 5 | **Implementation planning** | Program plan, dependencies, governance, success metrics |

Value analysis runs **across all phases** — not only at the end — to prioritize options, size benefits/costs, and feed budgeting.

---

## IT Strategy Typology (Five Categories)

Classify the engagement to calibrate ambition and integration complexity:

| Category | Value source | Integration complexity |
|----------|--------------|------------------------|
| **Conservation** | Cost reduction | Within organizational boundary |
| **Experimentation** | Enables growth | Within boundary |
| **Evolution** | Delivers growth | Within and beyond boundary |
| **Consolidation** | Cost reduction | Cross-boundary integration and migration |
| **Transformation** | Delivers growth | Cross-boundary integration and migration |

**E-business driver lens (4-box):** channel expansion, value-chain integration, industry structure change, cross-industry convergence — each maps to business improvement vs business transformation impact.

---

## Workstream 1 — IT Strategy Formulation

### Scenario planning for IT

Scenarios are **stories about the future** — not single-point forecasts. They:

- Surface multiple possibilities
- Escape linear extrapolation from the past
- Focus on factors that drive decisions

**Process (condensed):**

```
Macro environment (PEST) → Industry/value-chain impact
    → Time horizon → Scenario drivers (impact × uncertainty)
        → Driver interactions → Scenario narratives
            → Static business model → Dynamic business model
                → Strategy per scenario → Integrated strategy portfolio
```

**Uncertainty matrix:** Prioritize drivers with **high impact and high uncertainty** for scenario construction. Lower-impact or certain factors become monitoring items or near-term planning tasks.

**Strategy types from scenarios:**

| Type | When |
|------|------|
| **Execute now** | Required across all scenarios |
| **Execute if triggered** | Conditional on environment signal |
| **Real options** | Early entry preserves future advantage despite upfront risk |

### IT strategic options

An **IT strategic option** is an IT-centric action responding to a business driver or business strategy option.

**Option development workflow:**

1. Understand initial conditions and hypotheses
2. Determine strategic significance of IT (IT strategy grid, current-state diagnosis)
3. Extract strategic IT opportunities (value chain, Porter 5 Forces IT lens)
4. Assess IT capabilities (capability matrix / assessment wheel)
5. Define To-Be capability target
6. Identify capability gaps
7. Identify new IT-enabled capabilities
8. Build **Business Systems Architecture (BSA)**
9. Evaluate option impact

### IT strategy grid

Plot applications by **strategic impact on future business** vs **strategic impact of existing systems**:

| | High future impact | Low future impact |
|---|-------------------|-------------------|
| **High existing impact** | **Turnaround** — invest to transform legacy strategic systems | **Strategic** — protect and extend differentiators |
| **Low existing impact** | **Factory** — efficient backbone; rarely differentiating | **Support** — necessary but not strategic |

Use the grid to prioritize portfolio and sourcing posture.

### Business Systems Architecture (BSA)

BSA fuses **business drivers, value propositions, high-level processes, and required business systems** — the bridge from strategy options to IT architecture.

| Axis | Content |
|------|---------|
| **Horizontal** | Value-chain / process stages |
| **Vertical** | Key drivers (or system characteristics, org structure — purpose-dependent) |
| **Cells** | Logical groupings of business-system capabilities |

BSA feeds:

- Conceptual application maps
- Process maps linked to applications
- Portfolio and investment discussions

### IT opportunity lenses

**Value chain:** Decompose activities that create market value; prioritize IT options where IT changes cost, speed, quality, or customer experience materially.

**5 Forces (IT angle):** Can IT raise entry barriers, increase switching costs, create new products/services, shift supplier/buyer power, or affect substitutes?

**Option evaluation criteria:** Vision/mission fit, CSF/KPI coverage, competitive factor leverage, market requirements, emerging IT leverage, high-value process support, transformation toward more advantaged business models.

---

## Workstream 2 — Architecture Design

Architecture is **not everything, but without architecture there is only ad-hoc engineering**. It maps rigorous structure onto ambiguous business environments.

### IATO four views

| View | Focus questions |
|------|-----------------|
| **Information** | KM, data repositories, DW/OLAP, EIS, master data, compliance records |
| **Applications** | ERP vs best-of-breed, legacy renewal, integration, customer-facing apps |
| **Technology** | Web-enabled platforms, components, networks, databases, presentation layers |
| **Organisation** | Sourcing model, governance, budget, IS structure, skills |

### Architecture design process

```
Assess current IT environment
    → Identify gaps (business requirements vs current IT; quality gaps)
        → Develop conceptual architecture (idealized from strategy)
            → Design implementation architecture (constraints, phasing, investment guide)
```

**Current-state assessment:** Use a structured assessment wheel covering strategy, delivery, technology, people, and systems dimensions (typically ~20+ elements grouped across direction, architecture, applications, infrastructure, organization, project management, service delivery, quality, data, security).

**Gap identification:** Map required business-system support levels against current IT; compare application functional and technical quality vs required quality.

**Conceptual architecture artifacts:**

- **Information map** — major information domains; shared vs local; duplication hotspots
- **Application map** — BSA projected onto application domains; strategic / tactical / operational layers
- **Technology map** — platform layers (hardware → OS → DB → network → API → applications → presentation)
- **Organisation map** — governance model, IT roles/skills, sourcing structure

**Governance architecture options** (illustrative patterns):

| Pattern | IT leadership | IT function role | Typical context |
|---------|---------------|------------------|-----------------|
| **Conglomerate / arms-length** | Facilitator | Knowledge broker | Diverse businesses, weak central IT mandate |
| **Federal / participatory** | Arbiter | Monitor + rules for business units | Partially integrated divisions |
| **Centralized / top-down** | Dictator | Active central control | Single business model, tight integration |

Organization structure variants: decentralized, centralized, integrated, shared services, virtual IT, outsourced IT — each fits different corporate forms.

**Implementation architecture:** Reflects organizational priorities, constraints (cost, risk, time-to-solution, time-to-benefit), and becomes the basis for **system investment guidelines**.

---

## Workstream 3 — Value Analysis

Quantify and compare options across the engagement — not only at final business case.

**Techniques (select by need):**

- Cost build-up; activity-based costing
- Value analysis (VA) for function/cost trade-offs
- Intangible asset consideration in new-economy contexts
- DCF / NPV / ROI / ROR
- **Free cash flow (FCF)** and enterprise/business value
- **MVA / economic profit** — value created above cost of capital
- Sensitivity, scenario, decision tree, simulation, real options for uncertainty

**Project economics structure:**

| Phase | Cost types | Benefit types |
|-------|------------|---------------|
| Lifecycle | Initial (build/buy/customize) + running (maintain, labor, telecom, training) | Tangible savings/revenue + intangible/strategic |

**Terminal value methods** (when projecting beyond explicit forecast): perpetuity, constant growth, harvest (no further cash flow), liquidation, book/replacement value — choice depends on asset life and competitive advantage period.

**MVA intuition:** Business value = PV of future FCF; MVA = business value − invested capital; positive MVA ≈ positive NPV ≈ economic value created.

See `standards/it-strategy-engagement-guide.md` for valuation checklist.

---

## Workstream 4 — Sourcing

Three major alternatives:

| Model | Definition |
|-------|------------|
| **Outsourcing** | Third party performs work previously in-house; function not replicated internally |
| **Multi-sourcing** | Multiple third parties for different scopes (selective sourcing) |
| **Insourcing** | Internal IT operates with market-style business relationship; often requires organizational redesign |

**Common outsource candidates:** Data center, telecom, help desk, desktop, applications maintenance — when scope is bounded and SLA-measurable.

**Keep internal:** Strategic services, business consultancy, vendor management, IT integration strategy, policies/standards.

### Sourcing strategic grid

Cross **strategic impact of IT environment on business** with **strategic impact of IT projects**:

| | High project impact | Low project impact |
|---|---------------------|---------------------|
| **High environmental impact** | **Strategic** — insource; outsourcing risky; partnership critical if used | **Turnaround** — insource; outsourcing generally inadvisable |
| **Low environmental impact** | **Factory** — outsource for scale/efficiency unless IT org is very strong | **Support** — outsource |

**Economics rule of thumb:** Outsourced price must be roughly **30–40% below** fully loaded insource cost to be competitive (margin + sales/marketing + provider profit).

**Outsource drivers:** Cost control, performance, right-sizing, cash infusion, access to skills, focus on core business.

**Execution layer (when outsourcing proceeds to RFP):** Strategic sourcing choice here does not produce a bid — for Solution Planning, To-Be AMS design, transition, and proposal structure, see `frameworks/application-outsourcing-solution-planning.md`.

**Insource drivers:** IP retention, strategic sensitivity, restructuring, IT competency building, technology access.

**Contract risk themes:** Change flexibility, exit clauses, SLA measurement, competitive bidding rights, technology refresh, governance of provider relationship.

---

## Workstream 5 — Implementation Planning

**Implementation planning** decides **how** the organization realizes the IT strategy — typically as a **program** coordinating multiple projects.

### Program vs project

| | Program management | Project management |
|---|-------------------|-------------------|
| Scope | Broad; multiple projects | Narrow; single deliverable |
| Coordination | Cross-project dependencies | Within project boundary |
| Sponsorship | Senior executives | Middle management (typical) |
| Focus | Strategy alignment, value realization | Scope/time/cost/quality of one initiative |

### Core program processes (value-focused)

| Process | Purpose |
|---------|---------|
| **Value realization management** | Define and track qualitative/quantitative success vs strategic goals; tools: balanced scorecard |
| **Program planning, prioritization, integration** | Roadmap, dependencies, risk/contingency, scope control, change impact |
| **Business case & financial management** | DCF/ROI standards, master business case, cost tracking, executive milestone reviews |
| **Performance management & reporting** | Progress vs plan (time, cost, quality, scope change) |

### Balanced scorecard (program level)

Four perspectives linked to strategy:

- **Financial** — shareholder value, cost vs plan
- **Customer** — satisfaction, loyalty, market metrics
- **Operational** — processes that must excel
- **Innovation/learning** — future capability and growth assets

### Program management tiers

Classify projects by **complexity** and **change impact** to scale PM rigor:

| Tier | Typical PM depth |
|------|------------------|
| **Level 1 (high change + high complexity)** | Full PM process set |
| **Level 2** | Planning, integration, performance, timeline, change, communication, business case, issue management |
| **Level 3 (lower)** | Performance, timeline, communication, business case, detailed plan |

Use tiering to avoid over-administering small projects while protecting high-risk transformations.

---

## Integration Map

```
Business strategy + scenarios (consulting-strategy-process)
        ↓
IT drivers + IT options + BSA (this framework §Formulation)
        ↓
IATO architecture + gaps (this framework §Architecture)
        ↓
Value analysis + sourcing choice (this framework §Value + §Sourcing)
        ↓
Program plan + BSC + PMO (transformation-pmo, this framework §Implementation)
        ↓
Capability/enabler map (strategic-capability-network) — optional deep dive
```

---

## Common Failure Modes

| Failure | Mitigation |
|---------|------------|
| IT strategy disconnected from business strategy | Scenario + BSA anchored on business drivers |
| Architecture slideware without gap analysis | Current-state assessment wheel + explicit gaps |
| Outsourcing for cost only on strategic systems | IT strategy grid + sourcing grid |
| Portfolio of projects without program integration | Implementation planning with dependencies and master business case |
| Benefits claimed but never tracked | Value realization + BSC from program start |
| Single-point forecast ignores uncertainty | Scenario planning + sensitivity on business case |

---

## Related Files

- `standards/it-strategy-engagement-guide.md` — checklists and templates
- `frameworks/consulting-strategy-process.md` — upstream strategy engagement
- `frameworks/transformation-pmo.md` — program office and governance
- `CONTEXT_ROUTING.md` — IT Strategy route
- `knowledge/index/legacy-source-index.md` — Program Line G
- `frameworks/application-outsourcing-solution-planning.md` — AMS RFP / Solution Planning (post-decision)
