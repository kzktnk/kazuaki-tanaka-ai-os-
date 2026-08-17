# AMS Solution Plan & Assumptions Checklist

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Solution Plan and Assumptions Checklist structure (~2015), generalized. Internal review gate names replaced with generic labels.

---

## Purpose

Operational checklist for **completeness and consistency** of an Application Management Services (AMS) Solution Plan before internal review and client submission.

Use with:

- `frameworks/application-outsourcing-solution-planning.md`
- `frameworks/ams-services-pyramid.md`
- `frameworks/service-transition-approach.md`

---

## When to Use

- Solution Architect self-review before peer / quality review
- Deal team walkthrough before pricing approval
- Transition lead validating handoff package at contract award

---

## How to Use

1. Complete sections in order where possible (Assumptions may iterate).
2. Mark each item **Done / N/A / Open** with owner.
3. **Open** items with material cost or SLA impact must appear in §4 Assumptions/Issues/Risks.
4. Cross-check client proposal (`deliverable-archetypes.md` Archetype I) against §2–3.

---

## 1. Opportunity Overview

| # | Check | Notes |
|---|-------|-------|
| 1.1 | Deal team roles identified (SA, pricing, transition, legal interface) | |
| 1.2 | Client timeline and RFP milestones documented | |
| 1.3 | Business context and drivers captured (fact, not boilerplate) | |
| 1.4 | Win themes aligned to buyer values | |
| 1.5 | As-Is baseline summarized (volumes, org, cost reference if available) | |
| 1.6 | Competitive landscape and differentiation noted (generic) | |

---

## 2. Solution Overview

| # | Check | Notes |
|---|-------|-------|
| 2.1 | Application portfolio in scope listed (L1/L2) | |
| 2.2 | In-scope / out-of-scope / interface explicit per domain (AM / dev / infra) | |
| 2.3 | High-level delivery model defined (governance, SM, delivery) | |
| 2.4 | Business continuity approach addressed | |
| 2.5 | Data protection and access model summarized | |
| 2.6 | Service levels referenced (or marked TBD with plan to define) | |

---

## 3. Detailed Solution

| # | Check | Notes |
|---|-------|-------|
| 3.1 | L3 service components mapped to operating tiers | |
| 3.2 | Operating model (L1 → L3+) described per major tower | |
| 3.3 | Staffing model and pyramid by tower | |
| 3.4 | Location strategy with decision rationale | |
| 3.5 | Estimating approach stated (bottom-up / top-down / hybrid) | |
| 3.6 | Key estimating factors documented (no orphan numbers) | |
| 3.7 | Experience-level mix aligned to complexity | |
| 3.8 | Tools and automation assumptions stated | |
| 3.9 | Language and coverage hours explicit | |

---

## 4. Assumptions / Issues / Risks

| # | Check | Notes |
|---|-------|-------|
| 4.1 | Cost-driving assumptions listed and traceable to sizing | |
| 4.2 | Due diligence gaps identified with impact | |
| 4.3 | Risks rated with mitigation and owner | |
| 4.4 | Client dependencies explicit (access, SMEs, incumbent) | |
| 4.5 | Scope change rules during bid period understood | |
| 4.6 | Contractual and regulatory constraints captured | |

---

## 5. Service Introduction (Transition)

| # | Check | Notes |
|---|-------|-------|
| 5.1 | Transition approach summary (waves, principles) | |
| 5.2 | Ramp plan aligned to scope waves | |
| 5.3 | KT plan outline (assess → execute → sign-off) | |
| 5.4 | Transition governance and steering defined | |
| 5.5 | Milestones through steady state (generic names) | |
| 5.6 | Hypercare definition and exit criteria | |
| 5.7 | Dual-vendor / incumbent period rules if applicable | |

---

## 6. Financials & Pricing

| # | Check | Notes |
|---|-------|-------|
| 6.1 | Pricing structure matches scope split | |
| 6.2 | Assumptions tied to financial model | |
| 6.3 | Transformation / transition costs separated from BAU if needed | |
| 6.4 | Indexation / economic adjustment approach stated (concept) | |
| 6.5 | Internal margin / approval thresholds met (internal process) | |

---

## 7. Review Feedback

| # | Check | Notes |
|---|-------|-------|
| 7.1 | Peer review completed | |
| 7.2 | Quality / solution assurance review completed (if required) | |
| 7.3 | Open review items closed or tracked with owner | |
| 7.4 | Proposal deck consistent with Solution Plan | |
| 7.5 | Handoff pack ready for transition lead (post-award) | |

---

## Completion Gate

Do not submit externally until:

- [ ] All §2–5 items are **Done** or **N/A** with documented rationale
- [ ] No unresolved **Open** items with material SLA or price impact
- [ ] Assumption register matches proposal Appendix
- [ ] Transition section reviewed against `service-transition-approach.md`

---

## Related Files

- `frameworks/application-outsourcing-solution-planning.md`
- `frameworks/ams-services-pyramid.md`
- `frameworks/service-transition-approach.md`
- `standards/deliverable-archetypes.md` (Archetype I)
- `standards/consulting-review.md`
