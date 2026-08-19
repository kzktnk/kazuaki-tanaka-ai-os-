# Infrastructure Outsourcing Solution Planning Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Generalized from Infrastructure Outsourcing Solution Architect (IO SA) Intermediate and Advanced training (~2014–2016). No client names, rate cards, costing tools, delivery-center catalogs, or firm-specific approval policies.

---

## Purpose

Structure **pre-contract solution architecture** for infrastructure outsourcing (ITO) and related managed infrastructure — from deal qualification through To-Be design, commercial alignment, contract match, and handoff into mobilization / run.

This is the **infrastructure twin** of `frameworks/application-outsourcing-solution-planning.md`. **Build / SI** uses `frameworks/systems-integration-solution-planning.md`. Do not collapse the three: AMS prices application support; IO prices towers; SI prices design-build-test-deploy. Bundled deals need an **enterprise SA** who owns seams.

| Layer | Question | Typical artifact |
|-------|----------|------------------|
| **IT Strategy Sourcing** | Should infrastructure be outsourced, and in which towers? | Sourcing grid |
| **IO Solution Planning** (this file) | What will we run, transform, take as-is, and price? | Solution Plan, SLA/commercial design, contract assumptions |
| **Post-signature** | Mobilize, introduce service, then run | Transition / transformation / realization plans |

---

## When to Use

- RFP / BAFO for infrastructure managed services, hosting, workplace, network, or security operations
- Solution Architect (lead or tower) on a multi-year ITO bid
- Bundled AO + IO, or service-integrator roles over third parties
- Internal review before pricing lock or contract signature

---

## Solution Architect job

The IO SA constantly balances three constraints. A solution that wins on only one fails later.

```text
What the client will buy
        ×
What can actually be delivered
        ×
What meets the provider’s financial requirements
```

| Role | Owns | Does not own alone |
|------|------|--------------------|
| **Lead SA** | End-to-end solution, in-scope cuts, risk, reviews, contract synchronization, TPA interface | Legal terms, final commercial approval |
| **Tower / domain SA** | Current-capability analysis, scoping, estimate, cost-to-serve in that tower | Cross-tower seams |
| **Enterprise SA** (multi-tower) | Dependencies across IO / AO / SI / security; challenge list | Deep estimate of every tower |

Onshore vs offshore SA is a **work split**, not a rank. Whoever is Lead owns reviews. Support SAs exist to make those reviews possible — estimates, staffing, delivery-center connectivity, peer review inputs.

Interfaces that must be designed, not hoped for: delivery, mobilization, tools, connectivity, data protection, business continuity, commercial modeling, contract documentation, PMO, supplier management.

---

## Deal qualification (before deep solutioning)

Qualify in / out with explicit criteria. Typical signals (not a scorecard to copy):

| Dimension | Watch |
|-----------|--------|
| Relationship | Known account vs cold bid |
| Type of work | Transformation component vs run-only commodity |
| Financials | Capital required; staff/asset redundancy in the business case |
| Competitive field | Incumbent plus multiple bidders |
| Advisors | Third-party advisor (TPA) running the process |

The SA’s job in qualification is **scope and delivery honesty**, not “always pursue.”

---

## Clarify requirements: Read → Ask → Assume → Diligence

Incomplete RFPs are normal. Do not invent a complete estate.

1. **Read** what is written (and what is missing).  
2. **Ask** — structured questions, not a dump.  
3. **Assume** — write assumptions that can later sit in the contract.  
4. **Due diligence** — close assumptions; do not use DD as a second solutioning workshop.

If the buyer says “you run my IT,” they usually expect **cross-functional services** (change, problem, capacity, reporting) even when the RFP lists only towers. Make ownership of those processes explicit.

---

## Take-on shape: three solution approaches

| Approach | Idea | Risk |
|----------|------|------|
| **Design–Build–Run a rationalized estate** | Transform first (or in a controlled window), then run the standard | Delay: IO run cost starts while transformation slips; needs hard change control |
| **Integrate transition and transformation** | One program, one governance | Unstable operations after cutover; client must still run as-is during the move |
| **Take on as-is run** | Provider operates the current mess, then (maybe) transforms | Custom, non-standard, expensive DD; “we can manage your mess” is a sales message with a delivery bill |

**As-is take-on vs transformed-only** is a configuration, not a virtue:

- As-is: more visibility and control; heavier DD; parallel run; larger early mobilization; possible **service transformation** of the support model itself.  
- Transformed-only: less legacy risk and DD on operations; delivery org must track a moving transformation date; less visibility of the live estate.

Do not run **service transition on a moving target** without naming that risk.

---

## Detailed solution (To-Be) — test of completeness

The detailed solution is done when the team can **deliver, cost, and assess risk**, and every stated requirement is addressed qualitatively or quantitatively.

Typical components (include only what the deal needs; never treat the list as a product catalog):

- Client requirements and industry context  
- Scope (towers, volumes, hours, geographies)  
- Operating model and organization (roles by region; who is client / provider / third party)  
- Staff transfer  
- Mobilization / connectivity  
- Delivery tools and process (including ITIL-class CFS)  
- Supplier / alliance model  
- Data protection, continuity, legal/political constraints  
- Pricing and market price-to-win  
- Assumptions, dependencies, risks  

Organization charts must match the commercial document at a high level. Color-code **who owns** desk, LAN, servers, apps, and discretionary work — ambiguity here becomes an incident later.

Towers that commonly appear (names only; no cost-model files): service desk / EUC, network, servers and storage / data center, DBA, messaging and collaboration, monitoring / events, security operations, SAP basis-class platform ops, cloud IaaS ops, cross-functional (change, problem, capacity, reporting).

---

## Run vs discretionary vs project

**Run** keeps a defined estate at specified volumes: incidents, a small volume of one-off changes, steady-state administration.

**Discretionary** is optional client-decided work. **Project** is large discretionary work, usually separately funded.

Indicators that “run” is actually project or transformation:

- High volume of unrelated changes  
- Unstable environment (stabilization is transformation, not run)  
- Tech refresh, OS/platform swaps, new applications needing new servers and desk content, volume step-changes, decommission factories  

Standard run may **cap** a small amount of change (e.g. DB changes per year). Put the cap in the contract.

Solution options: include a small hour pool; add named FTE capacity; or a rate card. Never bury unlimited project work in run price.

---

## SLAs and commercials that look “innocuous”

- Design **excused performance** (and a RACI) before go-live, not after the first default.  
- **Low-volume protection:** a single miss in a tiny sample must not auto-fail a percentage SLA.  
- Model **fee-at-risk** (pool allocation × credit %). Set a **cap**; get delivery sign-off before accepting an aggressive regime.  
- Watch: client unilateral right to add/change SLAs; mismatch between penalty pool and what is actually measured; no exclusions/waivers.

Volume mechanisms (ARC / RRC or equivalent): extra resource charges and reduced-rate credits must match how cost actually moves. Setup to establish a new volume band is often **project**, not run.

**Price-to-win** is a range the client will award — triangulated from competitor behavior, market, and buyer insight. It is **not** lowest price, and it is not expressed as the provider’s margin. The SA solutions **to** that range and keeps **cost and price aligned** when volume or scope moves.

Pricing shapes (pros/cons for the buyer, not a recommendation):

| Shape | Buyer gets | Buyer pays with |
|-------|------------|-----------------|
| Time & materials | Comparability, pays for use | Overrun risk |
| Adjustable fixed fee | Predictability; delivery risk on provider | Scope fights; corner-cutting if scope is loose |
| Transaction / volume | Cost tracks business volume | Pays for volume-risk transfer |
| Value / gain-share | Fees tied to outcomes | Complexity when it works |

Multi-year deals: **inflation** and **FX** sit in the cost base and in the contract. Inflation is a risk/return split between parties — model it; do not absorb silently. FX risk appears if invoice currency does not match delivery economics, or if foreign-resource costs are unhedged operationally. Do not copy firm treasury policy; escalate currency-structure choices.

---

## Suppliers: prime/sub vs operational management

| Model | Contract | SLA accountability |
|-------|----------|-------------------|
| **Prime / sub** | Provider contracts the client for all services, including subcontracted | Provider is accountable for self-delivered **and** sub performance |
| **Operational management** | Third parties contract the client; provider manages them day-to-day | Provider accountable as integrator + own towers, **not** for unmanaged suppliers’ SLAs unless explicitly taken |

Taking contractual accountability for someone else’s contracted service is a **financial and legal event**, not a slide. Direct vs subcontract has different margin, control, and client politics — choose it; do not default.

---

## Security, PMO, SDM

Security is a **tower plus regulation**, not a logo. Identify applicable standards and who operates IAM, monitoring, code review, PKI, etc.

**PMO** coordinates program, risk, budget, contract change. **Service delivery management** runs the service. Do not park SDM / contract SDM hours inside PMO estimates — they get cut as “overhead” while delivery still needs them. Borrowed vs dedicated PMO labor has different load; classify honestly.

SDM cost drivers (examples): number of delivery nodes, multi-tower vs single, environment stability and refresh, non-standard SLAs/KPIs/reports, audit load, onsite requirement, third parties under management, geographic footprint.

---

## Contract must match the approved solution

Treat contract schedules and the approved solution as a **two-way trace**. Assumptions that protect delivery must appear in the contract; client T&Cs that break the solution must change the solution or the terms. The SA stays in negotiation until that match exists.

TPAs: the process is the client’s process. Differentiate on paper; stay patient, persistent, pleasant. Fighting the advisor is not a strategy.

Due diligence types worth distinguishing:

- **Pre-contract** — enough to make the contract commercially sound  
- **Reverse** — client tests provider claims  
- **Post-contract** — true-up, joint verification, transition inputs  

DD is not 100% accuracy, not a negotiation, not a technical fishing trip, and not a place for collectors to invent the solution.

---

## Client response and orals

RFI shows capability (often ROM). RFP shows a technical blueprint plus a commercial. Win themes: **good** cites rank and reuse; **great** shows a client-specific starting point and a time/risk consequence.

Orals: tell **this** client’s story; keep the deal-team line; bring delivery into the room; prepare full and short versions.

After signature the SA is not finished: **solution realization** is the early-delivery period where the as-is capability must actually reach the benefits in the plan. Stay for mitigations (scope drift, missing SMEs, unstable estate, transformation vs run collision).

---

## Relationship to other assets

| Asset | Relationship |
|-------|----------------|
| `application-outsourcing-solution-planning.md` | Application twin; bundled deals need both |
| `systems-integration-solution-planning.md` | Build / SI twin |
| `delivery-leadership.md` | Post-signature; SA → Delivery Lead |
| `service-transition-approach.md` | Mobilization / KT / waves — **not** the same as transformation |
| `transition-vs-transformation-vs-realization.md` | Introduction / transition / transformation / realization |
| `ams-solution-plan-checklist.md` | Completeness habit; IO uses the same discipline with tower-specific sections |
| `transformation-pmo.md` | Program office when transformation is large |
| `change-management.md` | People-side of staff transfer and new operating model |
| `it-strategy-foundations.md` §Sourcing | Upstream make/buy |
| `operations-handover-guide.md` | Run handover patterns |

---

## Do not register from source

- Costing tools, installers, master-data workbooks, estimators  
- Delivery-center maps, rate cards, firm approval percentages  
- Named client cases, RFPs, SOWs, orals decks  
- Certification playbooks and internal campaign catalogs  
- Personal / T&E correspondence  

---

## Related files

- `knowledge/patterns/transition-vs-transformation-vs-realization.md`
- `knowledge/migrations/iosa-2026-08.md`
- `frameworks/application-outsourcing-solution-planning.md`
