# Pattern: Decision Ownership

**Status:** Active  
**Origin:** LinkedIn No.14 and No.16

## Pattern statement

AI-enabled decision systems should separate the entity that executes a decision from the person or institution that owns its consequences.

## Core distinction

### Decision Execution

Who—or what—analyzes, selects, recommends, or performs an action.

### Decision Ownership

Who has the authority to:

- accept the decision
- override the decision
- intervene when conditions change
- explain the decision
- remain accountable for its outcome

## Signals

Use this pattern when:

- an AI agent can execute an operational workflow
- decision rights are unclear
- human approval is treated as a generic control
- accountability appears only after an incident
- technical feasibility is mistaken for organizational authority

## Design response

For each consequential decision, define:

- the AI's permitted role
- the designated owner
- override authority
- escalation conditions
- required evidence
- audit trail
- explanation responsibility

## Decision factors

The degree of human involvement should depend on:

- impact
- reversibility
- uncertainty
- regulatory significance
- safety implications
- monitoring capability

## Core rule

> Decision execution can be automated. Decision ownership must remain explicit.

## Relationship to Risk Ownership (No.16)

Decision ownership and **risk ownership** overlap in practice but serve different emphasis:

- **Decision ownership** — who accepts, overrides, explains, and remains accountable for the decision
- **Risk ownership** — who bears the non-delegable stake after AI recommends or acts

No.16: organizations delegate **work** to AI, not **accountability**. The risk owner must remain identifiable even when execution is autonomous.

See `knowledge/patterns/risk-ownership.md`.
