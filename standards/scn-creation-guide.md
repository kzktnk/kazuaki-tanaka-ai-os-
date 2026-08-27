# SCN Creation Guide

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Framework:** `frameworks/strategic-capability-network.md`

---

## Purpose

Operational standard for **creating and reviewing** Strategic Capability Networks in consulting engagements. Use when facilitating workshops, drafting SCN maps, or converting strategy documents into SCN.

---

## Prerequisites (Critical Success Factors)

| # | Factor | Requirement |
|---|--------|-------------|
| 1 | **Pre-research** | Pre-select important themes; at least one participant knows precedents / best practices (enables top-down and bottom-up analysis) |
| 2 | **Pre-learning** | All participants have baseline business knowledge of customer, product, systems |
| 3 | **Training** | Majority understand SCN notation and rules (framework is simple; inconsistent notation causes chaos) |
| 4 | **Workshop** | Dedicated facilitator + separate scribe; whiteboard, sticky notes, projector |

---

## Creation Workflow

### Step 1 — Anchor on strategy material

Start from approved strategy / mid-term plan / program charter. **Do not** re-litigate strategy validity beyond the scope needed for the engagement.

Extract:

- Strategic meaning of each initiative (not only the initiative label)
- Breadth and depth of coverage
- Visible, actionable level of measures

### Step 2 — Problem-solving chain

Apply to each theme:

```
Situation (Fact / As-Is)
    → Strategic meaning (judgment)
        → Direction / options
            → Concrete measures (actions)
                → Capabilities & Enablers
```

Decompose measures to derive capabilities; assign KOPT enablers per capability.

### Step 3 — Value tree per proposition

For each value proposition, build a tree:

```
To-Be Value (layer 1 → 2 → 3 as needed)
    └── Capabilities
            └── Enablers (initiatives + KOPT detail)
```

Combine trees from multiple value propositions into one SCN.

### Step 4 — As-Is overlay

Map current capabilities/enablers. Mark what **cannot** deliver To-Be value without change. Gaps drive Findings and initiative prioritization.

### Step 5 — KPI and emphasis

After structure stabilizes:

- Assign outcome KPIs to Value; monitor KPIs to key Capabilities
- Mark important capabilities (bold / thick border)
- Mark strong causal links (thick lines)

---

## End-Product Quality Conditions

An SCN deliverable should satisfy:

| Condition | If not met |
|-----------|------------|
| **Breadth and depth** | Local optimization, coin-flip solutions |
| **Client-specific** | Generic textbook answers |
| **Clear frame** | Subjective, inconsistent logic |
| **Forward view** | Short-sighted, only current pain |
| **Actionable** | “So what?” — cannot execute |

Three lenses before deep work:

1. **Must-satisfy conditions** (scope, stakeholders, constraints)
2. **Breadth of solution space** (segments, functions, time horizons)
3. **Depth emphasis** (where to go deep vs light touch)

---

## Breadth and Depth

**Breadth** — Cover the full solution space:

- Short-term vs long-term
- Individual vs integrated solutions
- Segment × business-function matrix (when relevant)
- Self vs partner (build vs alliance)

**Depth** — Logical drill-down, not slogans:

| Bad (diagnosis only) | Good (derived action) |
|----------------------|------------------------|
| Share is falling → Raise share | Share falling in regions → Shift sales capacity → Incentives or channel change |

Depth level depends on engagement phase; do not over-detail enablers in early strategy SCN.

**Emphasis (濃淡)** — Not every branch gets equal depth. Prioritize by differentiation factor and project purpose.

---

## Notation Rules

| Element | Shape / style |
|---------|----------------|
| Value | Rounded rectangle |
| Capability | Ellipse |
| Initiative (bundle) | White rectangle (top of enabler group) |
| Enabler | Rectangle — Technology: blue; others: green |
| KPI | Red text, corner of node |
| Important capability | Bold / blue thick border |
| Strong causal link | Thick line |
| Removed item | Dotted line + masking (do not erase in As-Is vs To-Be compare) |
| Added item | Distinct color / line style |
| Issue / comment | Callout bubble |

### As-Is vs To-Be on one map

1. Different line style/color for additions  
2. Retain deleted nodes as dotted/masked  
3. Callouts for change rationale  
4. Expected effect where known  

---

## Capability Consolidation Rules

| Rule | Guidance |
|------|----------|
| **Merge** | If two capabilities would share the same KPI → merge |
| **Split** | Many enablers attach to one capability; or N:1 from above → split or refactor |
| **Layers** | Target 2–3 capability layers |
| **Importance** | After draft complete: mark capabilities with problems or high executive priority; require KPI |
| **Causal strength** | Thick line where relationship is validated in practice |
| **Enabler split** | Split enablers when unrelated capabilities share one enabler; data/infra may stay shared |

---

## Enabler Breakdown Method

1. Break capability to the **smallest practical unit** (smaller gap to enabler = easier enabler identification).
2. For each capability, list KOPT candidate lists.
3. Select enablers from lists; place initiative names above detail nodes.

---

## Content Rules (Common Fixes)

| Issue | Fix |
|-------|-----|
| Value too abstract | Move abstract phrasing down to Capability; keep Value concrete |
| Duplicate value nodes | Merge or split by stakeholder/content |
| Capability phrase on enabler layer | Move up to Capability |
| Technology too coarse | Decompose to components |
| Same value in multiple branches | One node or explicit differentiation |

**Scope reminder:** SCN shows whether required IT capability is supported; it does not replace maintainability/usability analysis.

---

## Workshop Anti-Patterns

- Facilitator also scribing → discussion quality drops  
- No SCN training → incompatible notations  
- Too many themes in one session → pre-research filter  
- Discussion expands without “visible action” test → refocus on measure → capability chain  
- IT detail (I/O flows) on SCN → move to application map; use callouts on SCN only for business-relevant gaps  

---

## Outputs Checklist

Before publishing SCN:

- [ ] Value linked to stakeholders and outcome indicators  
- [ ] Every To-Be value supported by capability path  
- [ ] Enablers classified KOPT; initiatives named at enabler top  
- [ ] As-Is gaps visible or documented  
- [ ] Key capabilities have monitor KPIs  
- [ ] Important nodes visually emphasized  
- [ ] Notation consistent with team rules  
- [ ] Findings (if any) trace to specific SCN gaps  

---

## Related Files

- `frameworks/strategic-capability-network.md`
- `playbooks/strategy-scn.md` — execution sequence, Gate 1, template classes, coaching order
- `frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md`
- `core/author-voice.md`
- `standards/deliverable-archetypes.md`
