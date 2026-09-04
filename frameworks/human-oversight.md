## Human-in-the-Loop as an Accountability Mechanism

Human-in-the-Loop should not be treated only as a safety mechanism designed to compensate for imperfect AI.

Its more fundamental role is to preserve accountability.

As AI systems become capable of recommending actions, making operational judgments, and executing workflows, two questions must be separated:

1. Can the AI perform the action?
2. Who remains accountable for the consequences?

The first is a capability question.

The second is a governance question.

Human oversight therefore remains relevant even when AI performance becomes sufficiently reliable for autonomous execution.

### Accountability Functions of Human Oversight

Human oversight should make it possible to identify:

- Who reviewed the AI recommendation?
- Who approved the action?
- Who had authority to override it?
- Who owns the resulting outcome?

This creates an accountability chain:

AI Recommendation
→ Review
→ Approval
→ Execution
→ Outcome
→ Accountable Owner

### Non-Delegable Responsibilities

Certain responsibilities remain assigned to humans and institutions even when AI participates in operational decisions.

Examples include:

- legal responsibility
- safety responsibility
- regulatory responsibility
- operational responsibility
- organizational accountability

Therefore:

> Human oversight is not necessarily evidence of insufficient AI capability.

It may instead be a structural requirement for accountable AI operation.

### Design Principle

The objective of advanced AI systems should not automatically be to remove humans from the loop.

The more important design question is:

> Where, when, and how should humans remain in the loop?

Human oversight should therefore be designed according to the accountability requirements of the decision rather than applied uniformly to every AI action.

---

## Authority Design (LinkedIn No.17)

Human oversight levels should align with **designed authority levels**, not with AI capability alone.

See `knowledge/patterns/authority-levels.md`:

Recommend → Prepare → Act within limits → Execute with approval → Execute autonomously

Higher authority levels require clearer ownership, approval paths, and override mechanisms—not fewer humans by default.

The design question is not only *where humans remain in the loop* but *what authority the AI has been granted for each decision type*.

### Risk-based HITL for agents

全 Action を Human review にする必要はない。低リスク・可逆は Agent が実行してよい。高リスク・不可逆は事前の閾値で承認する。不確実な例外は Escalate する。要否を Agent 自身に決めさせない。

経路が既知か観察依存か、自律をどこまで縛るかは `knowledge/patterns/workflow-vs-agent-vs-human.md`。接続できることと実行してよいことは `knowledge/patterns/mcp-as-integration-not-authority.md`。
