# Pattern: Risk Ownership

**Status:** Active  
**Origin:** LinkedIn No.16

## Pattern statement

AI agents may execute work, recommend actions, and run workflows—but they cannot own risk. Risk ownership remains a human and institutional responsibility.

## Core distinction

### AI Agent

An entity that can analyze, recommend, and execute within technical boundaries.

Calling AI an "agent" does not make it a risk owner.

### Risk Owner

A person or institution expected to:

- understand consequences
- balance competing objectives
- accept accountability
- justify decisions to regulators, boards, and society

## What AI cannot assume (today)

- legal responsibility
- appearance before a regulator
- explanation to a board of directors
- accountability to society

AI can assist with analysis and execution. It cannot replace the risk-bearing role.

## Reframed question

| Avoid | Prefer |
|-------|--------|
| Can AI make this decision? | Who continues to own the risk after AI makes the recommendation? |

## Execution vs risk ownership

| | Decision execution | Risk ownership |
|---|-------------------|----------------|
| **Trend** | May become increasingly autonomous (AI) | Remains fundamentally human / institutional |
| **Design focus** | Scale throughput, speed, consistency | Named owner, escalation, explainability |

Related to Decision Ownership (No.14): ownership of consequences and ownership of risk align in practice but **risk ownership** emphasizes the non-delegable stake that persists after AI acts.

## Design response

For each AI-enabled workflow:

1. Identify the **risk owner** (role / institution)—not the model
2. Define what happens **after** AI recommendation or execution
3. Ensure the owner can override, explain, and accept consequences
4. Treat AI delegation as **work delegation**, not accountability delegation

## Strategic framing

> Organizations don't delegate accountability. They delegate work.

Operational AI competitive advantage:

**Humans retain risk ownership while AI scales execution.**

## Core rule

> AI may take the work. Humans and institutions must keep the risk.

## Related patterns

- `knowledge/patterns/decision-ownership.md`
- `knowledge/patterns/decision-delegation.md`
- `knowledge/patterns/ai-capability-vs-authority.md` (No.17)
