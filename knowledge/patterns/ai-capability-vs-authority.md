# Pattern: AI Capability vs AI Authority

**Status:** Active  
**Origin:** LinkedIn No.17

## Pattern statement

Technical capability does not imply organizational authority. An AI system may be able to analyze, decide, and execute—and still not be authorized to do so for a given decision.

## Core distinction

### Capability

What the AI can technically perform:

- analyze data
- generate recommendations
- prepare actions
- execute within system boundaries

### Authority

What the organization has explicitly authorized the AI to do:

- under which conditions
- within which limits
- with or without human approval
- for which decision types

## Signals

Use this pattern when:

- "the AI can do it" is treated as sufficient justification to automate
- the same agent receives uniform authority across different decision types
- maintenance rescheduling and equipment shutdown are governed identically
- autonomy maturity is measured by how many humans are removed from the loop

## Design response

For each operational decision, define separately:

1. What the AI **can** do (capability)
2. What the AI **may** do (authority)
3. Who **grants** that authority
4. Who **owns** the outcome (see Decision Ownership pattern)
5. Who can **revoke or override** authority when context changes

## Example (operational)

| Action | Likely capability | Likely authority |
|--------|-------------------|------------------|
| Reschedule routine maintenance within constraints | High | Act within limits |
| Adjust resource allocation on condition change | Medium–High | Execute with approval |
| Shut down critical equipment during abnormal event | High | Recommend or Execute with approval—not default autonomous |

Same AI agent. Different authority per decision.

## Core rule

> Capability answers "Can AI do this?" Authority answers "Should AI be allowed to do this—and under what conditions?"

## Related patterns

- `knowledge/patterns/authority-levels.md`
- `knowledge/patterns/decision-ownership.md`
- `knowledge/patterns/decision-delegation.md`
