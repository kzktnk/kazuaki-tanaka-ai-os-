# Delivery Leadership Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Generalized from SI Delivery Lead (SIDL) and Delivery Management Academy (DMA II–III) training (~2014–2015). No client cases, internal policy IDs, or tool names.

---

## Purpose

Define how a **Delivery Lead / program lead** turns a sold solution into outcomes — without surprising the client or the P&L.

Solution Architects **shape**. Delivery Leads **execute the commitment**: expectations, scope, estimates, mobilization, risk, and money. Split the roles; do not drop the file over the wall.

Use with `frameworks/systems-integration-solution-planning.md` (SI), `frameworks/transformation-pmo.md` (program office), `frameworks/change-management.md` (people), `frameworks/service-transition-approach.md` (take-on).

---

## When to Use

- Post-signature SI or multi-tower programs  
- When sold margin is eroding (EAC vs original deal)  
- Mobilization of build or run  
- Client says the contract is not what they “meant”  
- Program (benefit) vs project (output) confusion  

---

## Project vs program

| | Project | Program |
|--|---------|---------|
| Scope | Narrow, specified products | Wide; may change to protect benefits |
| Change | Minimize | Expected |
| Success | Time, budget, spec | ROI, capability, benefit delivery |
| Leadership | Task and directive | Relationships, conflict, politics |
| Planning | Detailed | High-level guidance to projects |

Multi-tower work (build + AO + IO + security) is a **program**. Program management exists to **deliver the business case**, not to collect status. Align program plan, business case, and change initiatives to the same benefits.

---

## Value, not only delivery metrics

Client value and provider delivery performance are different scorecards. A **value scorecard** applies balanced-scorecard logic to the **program**: customer, process, learning, finance — but the “strategy” is the program’s goals.

Use it to: monitor realized value, see each project’s contribution, spot external effects, and steer change requests. Do not substitute SLA dashboards for benefit tracking.

Release management is how value is **absorbed**: incremental capability at a rate the organization can take. A multiple-release schedule is the high-level view of products over the contract. Strategy = priorities and principles for what goes in which release. Distributed release: decide accountability early, automate distribution where possible, name a release owner.

---

## Change on a program

Speed, **conformance** to a prescribed process/outcome, and **commitment** vs mere compliance determine change governance. Map stakeholders to a commitment curve; put enablement on the program timeline; agree acceptance criteria with sponsors.

This file does not replace `frameworks/change-management.md`. It insists change is a **program workstream**, not a comms afterthought.

---

## SA → Delivery Lead: solution alignment

Before delivery is “started”:

- Reconfirm baseline with the client  
- Define how customer expectations will be managed  
- Define management processes  
- Mobilize resources  
- First delivery risk assessment (early after signature)  

Opportunity-stage defects (unsigned assumptions, missing relief, optimistic pyramid) become **EAC changes**. The Delivery Lead’s job in pursuit is to **see those coming**, not to discover them in month three.

---

## Contract vs customer expectation

Clients often contract for one thing and expect another. Internal client factions conflict. Sales and delivery may not share a story. Clients may expect the provider to make the **whole program** succeed beyond contractual scope.

Expectation management is proactive:

1. Gather (including C-level; stakeholder analysis is not a substitute for executive expectation)  
2. Document and confirm back  
3. Reconcile conflicts early  
4. Review on a cadence through delivery  

Shared objectives define success of **both** the engagement and the partnership. “No surprises” is the commercial posture in transition: small variances become large; stick to the plan while running change control.

---

## Change control and contingency

Stand up change control as a **system**: approach, tool, rollout/training. Unmanaged change becomes an unintended contract.

Use solution contingency only for estimate variability (see SI framework). Do not spend it on client delays, scope the client owned, or skipped diligence. Those are contract changes or relief.

---

## Money in delivery

| Term | Meaning for the lead |
|------|----------------------|
| **Original deal economics** | Approved sold financials; the commitment |
| **EAC** | Life-of-contract cost and revenue (actual + forecast) |
| **Sold vs delivered margin** | Cost of not executing the original deal |

Primary objective: meet or beat original economics. Forecast honestly. Cost-to-serve still applies in delivery (location mix, pyramid). Contract lifecycle: opportunity → price/approve → set-up → execute (bill, pyramid, EAC, recognition) → close (receivables, archive).

Revenue recognition and multi-contract programs are **compliance**, not optional admin. Escalate currency, unusual terms, and start-without-contract.

---

## Mobilization, introduction, transition

Poor mobilization is a root cause of delivery failure. Detect gaps vs solution assumptions while there is still time.

**Service introduction** (build → existing ops): operability of the solution **and** readiness of the support organization. Rehearsals, go/no-go, post-implementation review. **Warranty** is typically defect-fix for a window — not incident management. Agree warranty norms before go-live; keep design/build skill through the window.

**Service transition** (stand up run): new operating unit, processes, catalog, possible staff transfer. Deliverables include service/operating model, KT sign-off, readiness checklist, 30–60–90, exit criteria.

Do not staff warranty like run, or introduction like a full outsourcing take-on.

---

## Service management vs program vs project

Once live, work types differ (infra ops, AM, minor enhance, projects) but **management disciplines** still apply: user relationship, SLA performance, demand, resource capacity.

Keep four measurement layers distinct: relationship success (strategic), SLA (tactical), operational improvement metrics, and OLAs with other providers. Demand management prioritizes requests; resource management checks skill and capacity against SLAs.

If attributes of the commercial baseline move (scope, SLAs, volume, quality), **rebalance** — productivity alone is not a silent absorber.

---

## Governance and resourcing

Program governance and PMO setup belong here **and** in `transformation-pmo.md`. Do not invent a second PMO doctrine.

Sourcing strategy for the **build**: distributed vs centralized, iteration, pilots. For the **client’s IT**: what they retain, offshore experience, creative internal/external mix. Configuration management for distributed/multi-release work must be designed early (network, repository, overlapping releases).

Vendor/alliance management is a program workstream when third parties sit on the critical path.

---

## Do not register from source

- Named case companies and meeting-prep packs  
- Internal policy numbers, certification tools, monthly reporting product names  
- Social-style icebreakers, faculty logistics, attendee lists  
- SLA numeric examples from training (use the client’s contract)  

---

## Related files

- `frameworks/systems-integration-solution-planning.md`
- `frameworks/transformation-pmo.md`
- `frameworks/change-management.md`
- `frameworks/service-transition-approach.md`
- `knowledge/patterns/estimate-target-commitment.md`
- `knowledge/migrations/sisa-sidl-dma-2026-08.md`
