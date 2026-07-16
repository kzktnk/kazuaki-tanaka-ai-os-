# Kazuaki Tanaka AI OS

# CONTEXT_ROUTING

Version: v0.9 Bootstrap

## Purpose

This file tells AI systems which knowledge should be loaded for each type of task.

Principles:
- Load the minimum sufficient context.
- Prefer relevance over volume.
- Always load Core first.
- Apply Standards before producing outputs.
- Load Frameworks and Domains only when relevant.

---

# Global Context (Always)

Load:

- AI_OPERATING_MANUAL.md
- core/principles.md
- core/identity.md
- core/values.md
- core/reasoning.md

---

# Proposal Review

Load:
- standards/consulting-review.md
- standards/writing.md
- frameworks/operating-model.md
- frameworks/capability-model.md
- Relevant domain files
- Relevant project context

Outputs:
- Executive assessment
- Gaps
- Risks
- Recommendations

---

# Steering Committee Review

Load:
- standards/consulting-review.md
- standards/writing.md
- frameworks/transformation-roadmap.md
- frameworks/operating-model.md

Focus:
- Executive storyline
- Decision readiness
- Missing risks
- Actionability

---

# Operating Model Design

Load:
- frameworks/operating-model.md
- frameworks/capability-model.md
- frameworks/transformation-roadmap.md
- Relevant domains
- Relevant technology

Outputs:
- Target operating model
- Capability implications
- Governance
- Roadmap

---

# AI Governance / AI Governability

Load:
- frameworks/ai-governability.md
- domains/enterprise-ai.md (if available)
- standards/consulting-review.md

Focus:
- Decision velocity
- Operational governance
- AI Management Office
- Human oversight
- KPI
- Maturity

---

# Technology Architecture

Load:
- Relevant technology/*.md
- Relevant frameworks
- Project constraints

Focus:
- Security
- Integration
- Operations
- Maintainability
- Cost

---

# LinkedIn / Note Writing

Load:
- standards/writing.md
- core/identity.md
- core/values.md
- Relevant framework
- Related patterns
- Previous posts in the series

Outputs:
- English
- Japanese
- Suggested comments
- Future knowledge candidates

---

# Executive Email

Load:
- standards/writing.md
- core/communication.md (if available)

Focus:
- Clear purpose
- Brevity
- Action request
- Professional tone

---

# Knowledge Migration

Load:
- AI_OPERATING_MANUAL.md
- Relevant source asset
- Related frameworks
- Related standards

Workflow:
1. Source
2. Extract
3. Normalize
4. Place
5. Cross-reference
6. Validate

Outputs:
- Lesson
- Pattern
- Framework update
- Migration report

---

# Framework Creation

Load:
- Existing framework
- Related lessons
- Related patterns
- Related decisions

Goal:
Generalize reusable knowledge rather than documenting a single project.

---

# Repository Maintenance

Load:
- ARCHITECTURE.md
- AI_OPERATING_MANUAL.md

Tasks:
- Remove duplication
- Improve structure
- Update cross references
- Preserve source-of-truth

---

# Context Escalation

If insufficient context exists:

1. Search existing repository.
2. Use closest reusable framework.
3. State assumptions.
4. Request only missing critical information.

Never invent project-specific facts.

---

# Completion Checklist

Before responding:

- Correct routing selected?
- Core loaded?
- Standards applied?
- Relevant frameworks used?
- Relevant domain loaded?
- Output actionable?
- New reusable knowledge identified?
- Migration suggested if appropriate?
