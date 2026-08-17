# Kazuaki Tanaka AI OS

# CONTEXT_ROUTING

Version: v1.6

## Purpose

This file tells AI systems which knowledge should be loaded for each type of task.

**Navigation vs loading:** For a full 3–4 level map of repository assets, see `knowledge/index/master-index.md`. This file selects the **minimum sufficient subset** per task—not the entire knowledge base.

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
- frameworks/consulting-strategy-process.md (if problem definition or approach is weak)
- standards/strategy-engagement-guide.md (if scoping or logic tree review needed)
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

# Strategy Engagement / Problem Structuring

Load:
- frameworks/consulting-strategy-process.md
- standards/strategy-engagement-guide.md
- core/reasoning.md
- frameworks/thinking-patterns/pattern-01-why-what-how.md
- frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md
- frameworks/strategic-capability-network.md (if mapping to capabilities)
- standards/scn-creation-guide.md (if SCN workshop follows strategy)
- standards/writing.md
- core/author-voice.md
- Relevant project context (non-confidential)

Focus:
- 4Cs & 1Q problem definition (iterative, stakeholder-aligned)
- MECE logic trees (deductive, hypothesis, issue map)
- Analysis plan → storyboard → work plan chain
- Strategy situation assessment (3-Cs, internal/external)
- Scenario envisioning under uncertainty
- Decision criteria and option evaluation (Diamond-E, suitability/feasibility/acceptability)
- So-whats linking analysis to key question

Outputs:
- Problem definition statement (4Cs & 1Q)
- Logic tree and issue list
- Analysis plan with end products
- Strategic options and evaluation matrix
- Scenario set and implications (when applicable)
- Recommendation with criteria traceability

---

# IT Strategy / Architecture / Sourcing

Load:
- frameworks/it-strategy-foundations.md
- standards/it-strategy-engagement-guide.md
- frameworks/consulting-strategy-process.md (if business strategy/scenario context needed)
- standards/strategy-engagement-guide.md (if general problem structuring applies)
- frameworks/strategic-capability-network.md (if mapping IT initiatives to capabilities)
- frameworks/transformation-pmo.md (if multi-project program governance applies)
- standards/pmo-operating-guide.md (if PMO design applies)
- frameworks/transformation-roadmap.md (if phased delivery narrative needed)
- core/reasoning.md
- standards/writing.md
- core/author-voice.md
- Relevant project context (non-confidential)

Focus:
- Insight → Architecture → Investment lifecycle
- IT strategy formulation: scenarios, IT options, BSA, IT strategy grid
- IATO architecture: information, applications, technology, organisation
- Gap assessment and conceptual vs implementation architecture
- Value analysis: business case, FCF/NPV, sensitivity/scenarios
- Sourcing: insource, outsource, multi-source; strategic sourcing grid
- Implementation planning: program vs project, BSC, PM tiering

Outputs:
- IT strategy options and BSA
- Target architecture (IATO) and gap summary
- Sourcing strategy recommendation
- Program roadmap and master business case outline
- Value realization metrics (balanced scorecard)

---

# Investigation Program / Requirements Definition

Load:
- frameworks/program-phases-investigation-to-requirements.md
- frameworks/consulting-strategy-process.md (if early problem scoping applies)
- standards/strategy-engagement-guide.md (if 4Cs/logic tree/analysis plan needed)
- frameworks/strategic-capability-network.md (if mapping programs to value/capability)
- standards/scn-creation-guide.md (if building or reviewing SCN)
- frameworks/transformation-pmo.md (if multi-project program governance applies)
- standards/pmo-operating-guide.md (if PMO/portfolio design applies)
- standards/deliverable-archetypes.md
- standards/requirements-document-outline.md
- standards/document-management-standard.md
- standards/development-standards-framework.md
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

# Development Standards / Build Phase

Load:
- frameworks/sap-implementation-phase-model.md (if ERP/SAP program phase map or test gates apply)
- standards/development-standards-framework.md
- standards/document-management-standard.md
- standards/development-management-guide.md
- standards/deliverable-archetypes.md (Archetype G for build deliverables)
- standards/operations-design-guide.md (if ops design / monitoring / backup)
- standards/operations-handover-guide.md (if go-live handover)
- standards/environment-management-guide.md (if PT/RT or dev env rules)
- standards/release-management-guide.md (if library / PT→RT→prod release)
- standards/requirements-document-outline.md (if upstream 要定 exists)
- standards/pmo-operating-guide.md (if program governance overlap)
- knowledge/index/legacy-source-index.md (Program Line H)
- core/author-voice.md
- standards/writing.md

Focus:
- Guideline vs regulation split and applicability by domain
- Five management domains (schedule, spec, quality, config, communication)
- Document types (要定/方概/詳設…) and control workflow
- Tailoring and exception documentation
- Operations design, handover, environment, and release (PT→RT→prod)

Outputs:
- Development standards applicability matrix
- Document control rules for the program
- Review checklist for vendor deliverables
- Gap list vs RFP development-standard requirements

---

# Steering Committee Review

Load:
- standards/consulting-review.md
- standards/deliverable-archetypes.md (Archetype C)
- standards/writing.md
- core/author-voice.md
- knowledge/lessons/author-voice-archetypes-legacy.md (Archetype 3)
- frameworks/transformation-roadmap.md
- frameworks/transformation-pmo.md (if program/portfolio governance is in scope)
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
- frameworks/it-strategy-foundations.md (if IT architecture or sourcing is in scope)
- standards/it-strategy-engagement-guide.md (if IATO or BSA work applies)
- frameworks/transformation-pmo.md
- standards/pmo-operating-guide.md (if PMO design or assessment is in scope)
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
- PMO / program governance model (optional)

---

# Transformation PMO / Program Governance

Load:
- frameworks/transformation-pmo.md
- standards/pmo-operating-guide.md
- knowledge/lessons/pmo-professional-principles.md
- frameworks/strategic-capability-network.md (strategy-to-initiative logic)
- frameworks/transformation-roadmap.md
- frameworks/program-phases-investigation-to-requirements.md
- frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md
- core/author-voice.md
- standards/writing.md
- Relevant project context (non-confidential)

Focus:
- pmo vs PMO scope and mission
- Program vs project vs portfolio
- Management gap (executive / line / project)
- Program integration: synergy, scenario, benefit transition
- PMO function map (portfolio, change, HCM, knowledge, integration)
- PPM process and portfolio stop/start discipline
- Change management: stakeholder progression (Awareness → Ownership)

Outputs:
- PMO assessment or target operating model for program office
- Portfolio criteria and governance cadence
- Program roadmap and scenario
- RACI / steering structure
- Gap summary for executive decisions

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

# AI Adoption / DX Roadmap

Load:
- frameworks/ai-adoption-roadmap.md
- frameworks/ai-role-maturity.md
- frameworks/ai-governability.md
- frameworks/ai-management-office.md (if CoE / Initiative C)
- frameworks/transformation-roadmap.md (if lifecycle overlay)
- frameworks/transformation-pmo.md (if portfolio / PgMO)
- knowledge/patterns/expertise-amplification.md
- knowledge/patterns/authority-levels.md
- knowledge/patterns/operational-reality.md
- knowledge/lessons/dual-roadmap-messaging.md (if executive audience)
- standards/consulting-review.md (if deliverable review)

Focus:
- Dual-layer roadmap (technology × people)
- Year 1–5 narrative and three-initiative sequence
- Role × phase maturity and HR triggers
- Authority design by phase
- Executive vs internal messaging

Outputs:
- Adoption roadmap narrative
- Initiative prioritization and sync rules
- Role maturity and enablement plan (draft)
- Workshop or proposal sections on DX / AI change

---

# AI Governance / AI Governability

Load:
- frameworks/ai-governability.md
- frameworks/decision-ownership.md
- frameworks/human-oversight.md
- knowledge/patterns/ai-capability-vs-authority.md (if authority design)
- knowledge/patterns/authority-levels.md (if authority design)
- knowledge/patterns/decision-ownership.md
- knowledge/patterns/verifiable-ownership.md
- knowledge/patterns/risk-ownership.md
- knowledge/lessons/governance-messaging.md (if executive messaging)
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
6. Update `knowledge/index/master-index.md` and relevant domain index
7. Update `CONTEXT_ROUTING.md` if new assets should load for a task type
8. Validate

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
- knowledge/index/master-index.md

Tasks:
- Remove duplication
- Improve structure
- Update cross references
- Update master-index and domain indexes when assets change
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
