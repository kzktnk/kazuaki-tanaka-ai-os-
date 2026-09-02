# Systems Integration Solution Planning Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Generalized from systems-integration solution-architect training (~FY16). No client cases, rate cards, estimating tools, or firm approval matrices.

---

## Purpose

Structure **pre-contract solution architecture for systems integration / build** — scope, blueprint, delivery strategy, estimate, commercial construct, and contract — so what is sold can be delivered.

This is the **build twin** of:

| File | Sells |
|------|--------|
| This file | Design / build / test / deploy (SI) |
| `application-outsourcing-solution-planning.md` | Application run |
| `infrastructure-outsourcing-solution-planning.md` | Infrastructure run |

Do not price a build like a run. After go-live, **service introduction** (existing ops take a new system) is not the same as **service transition** (stand up a new run organization). See `knowledge/patterns/transition-vs-transformation-vs-realization.md`.

The SA still balances **what the client will buy × what can be delivered × financial requirements**. Same triangle as IO; different work.

---

## When to Use

- Fixed-price or mixed SI / custom development / package implementation bids
- Solution Plan review before deal approval
- Handoff from Solution Architect to Delivery Lead
- When sales pressure is collapsing estimate into price

---

## Estimate vs target vs commitment

See `knowledge/patterns/estimate-target-commitment.md`.

**The work is the work.** How the deal is priced is independent of effort, delivery approach, and resource plan. Do not let pricing discussions rewrite the estimate. Then **tick and tie**: estimate, commercial model, SOW, and Solution Plan must tell the same story. If you were given only the estimate file, you should still understand what is delivered, how, and where risk sits.

---

## Solution Architect accountabilities

Primary:

- Solution Plan: scope, estimates, contingency, cost, schedule, delivery model, sourcing, assumptions, risks  
- **Deliverability** signed off before contract approval  
- Consistency across Solution Plan, baseline scope, estimate, proposal, and contract  
- Transition of that package to the Delivery Lead (understanding and agreement, not a file drop)

Supports: proposal, orals, negotiation, pricing, mobilization approach. Does not own legal terms or final commercial approval alone.

**Managed-delivery habits in the opportunity stage** (principles, not a product):

1. Baselined scope and change control  
2. Estimate, schedule, work plan, sourcing against that baseline; uncertainty captured as assumptions  
3. Standard Solution Plan as one composite  
4. Delivery involved in QA of the opportunity  
5. SA visible to the client; delivery-center SA involved if they will execute  
6. Cost-to-serve optimized without hiding delivery risk  
7. Shared objectives between sales, solution, and delivery teams  

---

## Confirm scope, capability, constraints

Iterate. Do not front-load a census. Effort is bounded by **time available** (sole-source often needs more discovery than a competitive clock).

Capture **buyer values**: relationship and onshore presence, track record, industry knowledge vs commodity skill, technology preference, price pressure vs certainty, quality vs speed, competition shape.

Customer capability: people they will provide, skill/maturity, implicit constraints on sourcing, assets they furnish, schedule and quality goals.

**Solution to win** is “best value” as the buyer defines it — competitive insight, budget, and relationships — not the thickest architecture.

---

## Solution Plan — questions it must answer

A Solution Plan overview that cannot answer these is not ready:

| Topic | Question |
|-------|----------|
| Business case | Why this work? |
| Scope | How is it defined? In / out? |
| Assumptions | What, how validated, when? |
| Estimates | Validated? Contingency appropriate? Economics sound? |
| Schedule | Doable? Rollout responsibilities clear? |
| Technology | Risks and mitigations? |
| Staffing | Mix and ramp realistic? Delivery org right? |
| Delivery leadership | Strong enough? |
| Contract | How is delivery structured (if drafted)? |
| Risk | Key delivery risks and mitigations? |
| Change control | How is change controlled? |

---

## Blueprint before a firm estimate

Business, application, and technology blueprints must be **traceable to drivers**. No gold-plating. The SA uses them as **estimating factors**, not as decoration. Vendor-verified configurations when the stack is not the firm’s to invent.

---

## Delivery strategy

For complex work: **multiple releases**. For each release, a **V-model** that states which activities are onshore vs offshore (or client vs provider). Iterate the V as releases and locations change.

Also design: support services, technical infrastructure, programme office, pyramid and skills **across** releases — plus lead times (ramp, connectivity, visas, start-up).

Cost-to-serve (loaded delivery cost ÷ hours) is a **shaping metric**, not a substitute for estimate integrity. Levers: location mix, workforce mix, pyramid. Tailor to client maturity and work type; a leveraged pyramid is a goal, not a religion.

The estimate must cover **through go-live**: plan–analyze–design–build–test–deploy, plus PMO, QA, data protection, change enablement, service introduction, and cross-phase specialists. Contingency is additional, not a hiding place for forgotten workstreams.

---

## Risk and two contingencies

Keep a risk-response log from confirm-scope onward.

Two different pots in price:

| Type | For |
|------|-----|
| **Negotiation contingency** | Commercial give in bargaining |
| **Solution / delivery contingency** | Variability around **our** estimates after we have architected diligently |

Solution contingency **covers** (examples): a confirmed resource quits; rework from quality; pioneering technology; estimating assumptions that prove wrong *inside* our control of method.

It **does not cover** (these belong in **contract relief** or better architecture): client/third-party dependencies late; good-faith assumptions that were never diligence; client sign-off delays; scope the client was to do; failure to follow estimating method; failure to use standard staffing channels.

Sales owns getting relief rights into the contract. The SA must not “buy” those risks with solution contingency.

---

## Commercials and contract

Expenses are always larger than the first model. Every assumption needs a worst case. Finance translates the solution; the SA still owns whether the model matches the work.

**Deliverable** = a tangible product created without relying on another party — a thing, not an action. Not every work product is a contractual deliverable. Deliverables carry warranty, indemnity, and ownership. Red flags: payment tied to acceptance of a thin deliverable; a one-line definition on a large artifact.

SOW / work order must state in-scope and out-of-scope, acceptance clock and non-acceptance path, change control that produces new work orders, ownership, and payment ties to dates.

Do not start work without a written contract except under explicit escalation. Client data protection is priced and contracted, not hoped.

---

## Handoff

If Lead SA ≠ Delivery Lead, the Delivery Lead must **agree** the documented solution before signature is treated as done. See `frameworks/delivery-leadership.md`.

---

## Do not register from source

- Estimating / pricing tools and training URLs  
- Case RFPs, solution plans with client names, contract amendments  
- Certification systems and approval-dollar matrices  
- Logistics and attendee lists  

---

## Related files

- `knowledge/patterns/estimate-target-commitment.md`
- `frameworks/delivery-leadership.md`
- `frameworks/infrastructure-outsourcing-solution-planning.md`
- `frameworks/application-outsourcing-solution-planning.md`
- `knowledge/migrations/si-delivery-leadership-2026-08.md`
