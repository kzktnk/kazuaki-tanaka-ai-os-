# Kazuaki Tanaka AI OS

# CONTEXT_ROUTING

Version: v1.0

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
- core/author-voice.md

---

# Proposal Review

Load:
- standards/consulting-review.md
- standards/deliverable-archetypes.md
- standards/writing.md
- core/author-voice.md
- knowledge/lessons/author-voice-archetypes-legacy.md (Archetype 1: Proposal)
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

# Vendor Proposal Evaluation

Load:
- standards/vendor-proposal-evaluation.md
- standards/deliverable-archetypes.md (Archetype B)
- standards/consulting-review.md
- core/author-voice.md
- knowledge/lessons/author-voice-archetypes-legacy.md (Archetype 2)
- Relevant RFP / domain context (if available, non-confidential)

Focus:
- Evaluation criteria design (rationale per scoring point)
- Weighting and team assignment
- Value-add definition
- Multi-evaluator reconciliation
- Fair comparison across vendors

Outputs:
- Evaluation sheet design
- Scoring rationale
- Gap / concern summary
- Selection recommendation with evidence

---

# Investigation Program / Requirements Definition

Load:
- frameworks/program-phases-investigation-to-requirements.md
- frameworks/strategic-capability-network.md (if mapping programs to value/capability)
- standards/scn-creation-guide.md (if building or reviewing SCN)
- standards/deliverable-archetypes.md
- standards/requirements-document-outline.md
- core/author-voice.md
- knowledge/lessons/author-voice-archetypes-legacy.md (Archetypes 4–7)
- knowledge/index/legacy-source-index.md (if tracing source lineage)
- frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md
- frameworks/thinking-patterns/pattern-01-why-what-how.md
- standards/writing.md

Focus:
- Phase gate compliance (100→500)
- As-Is before Gap; approach before requirements
- Option comparison and evaluation sheets
- Requirements document structure
- Report storyline as compression of prior phases
- SCN for initiative integration and gap visibility (when multi-program or strategy alignment)

Outputs:
- Phase deliverable checklist
- Gap / issue extraction
- Option evaluation matrix
- Requirements outline
- Investigation report storyline
- SCN map or Findings on SCN (when applicable)

---

# Steering Committee Review

Load:
- standards/consulting-review.md
- standards/deliverable-archetypes.md (Archetype C)
- standards/writing.md
- core/author-voice.md
- knowledge/lessons/author-voice-archetypes-legacy.md (Archetype 3)
- frameworks/transformation-roadmap.md
- frameworks/operating-model.md

Focus:
- Executive storyline
- Decision readiness
- Missing risks
- Actionability
- Priority of issues before asking for decisions

---

# Operating Model Design

Load:
- frameworks/operating-model.md
- frameworks/capability-model.md
- frameworks/strategic-capability-network.md
- standards/scn-creation-guide.md (if SCN workshop or map is in scope)
- frameworks/transformation-roadmap.md
- Relevant domains
- Relevant technology

Outputs:
- Target operating model
- Capability implications
- Governance
- Roadmap
- SCN linking value, capabilities, and KOPT enablers (optional)

---

# SCN / Findings Analysis

Load:
- frameworks/strategic-capability-network.md
- standards/scn-creation-guide.md
- frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md
- frameworks/thinking-patterns/pattern-06-strategy-org-process-system.md
- frameworks/capability-model.md
- core/author-voice.md
- standards/writing.md
- Relevant project context (non-confidential)

Focus:
- Value → Capability → Enabler (KOPT) causal logic
- As-Is vs To-Be on the same network
- 3–5 structural Findings as gaps on the SCN (not a flat issue list)
- KPI placement: outcome on Value, monitor on Capability
- Program / project mapping and cross-program integration
- Workshop quality: notation consistency, breadth/depth, actionable enablers

Outputs:
- SCN map (draft or reviewed)
- Findings register tied to SCN nodes
- Gap summary for steering / executive discussion
- Initiative prioritization and resource allocation view

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
