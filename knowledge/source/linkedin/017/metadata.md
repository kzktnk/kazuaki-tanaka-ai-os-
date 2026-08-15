# Metadata — LinkedIn No.17

```yaml
id: "017"
title:
  en: "How Much Authority Should We Give AI?"
  ja: "AIにどこまで「権限」を与えるべきか"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
primary_framework:
  - frameworks/ai-governability.md
secondary_frameworks:
  - frameworks/decision-ownership.md
  - frameworks/human-oversight.md
patterns:
  - knowledge/patterns/ai-capability-vs-authority.md
  - knowledge/patterns/authority-levels.md
lessons:
  - knowledge/lessons/governance-messaging.md
core_updates: []
standard_updates: []
tags:
  - ai-governance
  - operational-ai
  - authority-design
  - ai-capability
  - appropriate-autonomy
  - decision-rights
  - critical-infrastructure
  - accountability
```

## Core Theme

Capability and authority are not the same. Operational AI design should assign graduated authority levels per decision—not treat autonomy as a binary switch or maximize it by default.

## Key Distinctions

| Common framing | Reframed question |
|----------------|-------------------|
| How autonomous should AI become? | How much authority should we give AI? |
| What can AI do? | What should AI be authorized to do—under what conditions, and by whom? |
| Maximum autonomy | Appropriate autonomy |

## Authority Levels

Recommend → Prepare → Act within limits → Execute with approval → Execute autonomously

## Authority Design Factors

Decision × Risk × Context:

- consequence of error
- reversibility
- uncertainty
- legal / regulatory / safety responsibility
- who owns the risk

## Relationship to No.16

No.16: AI cannot own risk; organizations delegate **work**, not **accountability**.

No.17: even when capable, **authority** must be designed per decision.

Sequence: retain risk ownership (16) → design authority levels (17) without conflating either with capability or execution alone.

## Relationship to No.13

No.13 establishes Human-in-the-Loop as an accountability mechanism—not merely compensating for AI limitations.

No.17 adds: even when AI is capable, authority must be designed separately; oversight levels follow authority design, not capability alone.

## Relationship to No.14

No.14 separates Decision Execution from Decision Ownership.

No.17 extends this by separating AI Capability from AI Authority, and by defining graduated authority levels rather than a human/AI binary.

Combined insight:

> Increasing AI capability does not automatically expand AI authority. Authority, ownership, and oversight must be designed together per decision context.
