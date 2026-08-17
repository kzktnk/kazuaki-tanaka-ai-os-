# Pattern: Graduated AI Authority Levels

**Status:** Active  
**Origin:** LinkedIn No.17

## Pattern statement

AI authority should be designed as graduated levels per decision—not as a binary switch between human decision and AI decision.

## Authority ladder

```
Recommend
  ↓
Prepare
  ↓
Act within limits
  ↓
Execute with approval
  ↓
Execute autonomously
```

| Level | AI role | Typical human role |
|-------|---------|-------------------|
| **Recommend** | Suggest options | Human decides and executes |
| **Prepare** | Draft plan, options, or execution package | Human reviews and triggers |
| **Act within limits** | Execute inside predefined bounds | Human monitors exceptions |
| **Execute with approval** | Propose action; execute after approval | Human approver / owner |
| **Execute autonomously** | Full execution within delegated domain | Human owns outcome; periodic review |

## Design formula

Authority level should follow:

**Decision × Risk × Context**

Not model capability alone.

### Decision factors

| Factor | Question |
|--------|----------|
| **Consequence** | What happens if the decision is wrong? |
| **Reversibility** | Can the action be undone? |
| **Uncertainty** | How confident is the judgment? |
| **Regulatory / legal / safety** | Who bears statutory or safety responsibility? |
| **Risk ownership** | Who ultimately owns the risk? |

## Common failure modes

- Setting authority at model level instead of decision level
- Using capability benchmarks as autonomy targets ("remove humans")
- Applying one authority level to an entire agent across all workflows
- Confusing Execute with approval with Execute autonomously

## Design response

For each decision type in an operational workflow:

1. Name the authority level explicitly
2. Document the granting authority (role / governance body)
3. Define limits, approval paths, and override rules
4. Link to Decision Owner (No.14)
5. Review when context, regulation, or risk profile changes

## Strategic framing

| Avoid | Prefer |
|-------|--------|
| Maximum autonomy | Appropriate autonomy |
| Autonomy as maturity score | Authority as design artifact |
| "How autonomous should AI become?" | "How much authority should we give AI?" |

## Core rule

> The goal of Operational AI is not necessarily maximum autonomy. It is appropriate authority—designed per decision, risk, and context.

## Adoption phase (typical ceiling)

When using `frameworks/ai-adoption-roadmap.md` horizons:

- **Year 1–2:** Recommend and Prepare dominate production use  
- **Year 3:** Act within limits for bounded decisions; HITL explicit  
- **Year 4–5:** Execute with approval or bounded autonomy for selected domains  

Phase sets the default ceiling; Decision × Risk × Context still governs each decision.

## Related patterns

- `knowledge/patterns/ai-capability-vs-authority.md`
- `knowledge/patterns/decision-ownership.md`
