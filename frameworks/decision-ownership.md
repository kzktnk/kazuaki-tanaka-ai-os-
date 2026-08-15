## Relationship to Human-in-the-Loop

Human-in-the-Loop is one mechanism through which Decision Ownership can be operationalized.

Decision Ownership requires more than assigning a nominal owner.

The operating model should make clear:

- who reviews an AI-generated recommendation
- who has authority to approve execution
- who may override or stop the action
- who remains accountable for the outcome

A useful accountability chain is:

AI Recommendation
→ Human Review
→ Human Approval
→ Execution
→ Outcome Ownership

Human approval and Decision Ownership are related but not identical.

The person approving an individual action may not always be the ultimate owner of the resulting business, safety, or regulatory outcome.

Therefore, AI governance should distinguish between:

- Reviewer
- Approver
- Executor
- Decision Owner

This distinction becomes increasingly important as AI execution becomes more autonomous.

The objective is not to require human approval for every AI action.

The objective is to ensure that consequential decisions retain an identifiable accountability structure.

---

## Authority vs Capability (LinkedIn No.17)

Decision ownership defines **who accepts consequences**.

Authority design defines **what the AI is permitted to do** for each decision type.

These are related but distinct:

- An AI may be **capable** of executing an action.
- The organization may still **withhold authority** for that action.
- The **Decision Owner** (or governance body) grants authority levels—not the model's technical limits.

Use graduated authority levels per decision:

Recommend → Prepare → Act within limits → Execute with approval → Execute autonomously

Authority should follow **Decision × Risk × Context**, not a single autonomy setting for the whole agent.

See:

- `knowledge/patterns/ai-capability-vs-authority.md`
- `knowledge/patterns/authority-levels.md`

---

## Risk Ownership (LinkedIn No.16)

Granting authority or delegating execution does **not** transfer risk ownership to the AI.

Every consequential AI workflow requires a named **risk owner** who remains accountable after the AI recommends or acts.

> Organizations delegate work—not accountability.

See `knowledge/patterns/risk-ownership.md`.
