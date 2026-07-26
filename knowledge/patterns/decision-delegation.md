# Pattern: Decision Delegation Is Not Decision Ownership

**Status:** Active  
**Origin:** LinkedIn No.14

## Pattern statement

Delegating analysis, recommendation, or execution to AI does not delegate accountability for the outcome.

## Distinction

Delegation determines:

- what the AI is allowed to do
- when the AI may act
- how far automation may proceed

Ownership determines:

- who authorizes the decision domain
- who may intervene
- who accepts the consequences
- who remains accountable

## Common failure mode

Organizations automate a decision process without explicitly redesigning decision rights.

The result is operational ambiguity:

- AI acts
- humans assume the system owns the choice
- accountability becomes visible only after failure

## Design response

Every delegated AI decision should include:

1. Scope of delegation
2. Decision owner
3. Override authority
4. Escalation threshold
5. Evidence requirement
6. Review cadence

## Reusable rule

> Authority to execute may be delegated. Accountability for consequential outcomes must remain assigned.
