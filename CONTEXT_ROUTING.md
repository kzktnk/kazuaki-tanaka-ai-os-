# Kazuaki Tanaka AI OS

# CONTEXT_ROUTING

Version: v1.22

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
- Relevant domain files (`domains/energy-utilities.md` if energy / utilities; `domains/public-defense.md` if public / defense)
- Relevant project context

Outputs:
- Executive assessment
- Gaps
- Risks
- Recommendations

---

# AI PoC Quality Review (buyer)

Load:
- playbooks/ai-poc-quality-review.md
- knowledge/decisions/buyer-owns-ai-poc-ground-truth.md
- playbooks/rag-structure-diagnosis.md (if retrieval vs table/structure)
- playbooks/responsible-ai-assessment.md (if principles / accountability)
- standards/vendor-proposal-evaluation.md (if scoring-sheet design, not AI metrics)
- standards/consulting-review.md

Focus:
- Requirement → scenario → metric → pass condition
- Ground truth owned by the business
- Retrieval vs answer vs business vs operations
- Go / Conditional Go / No-Go, not “it ran”

---

# Offering Review

Load:
- playbooks/offering-review.md
- standards/consulting-review.md
- frameworks/change-management.md
- frameworks/transformation-pmo.md

Focus:
- To-Be ≠ transformation mechanism ≠ offering
- Program management vs change management
- Pain → value → what the client buys

---

# Responsible AI Assessment

Load:
- playbooks/responsible-ai-assessment.md
- frameworks/human-oversight.md
- frameworks/decision-ownership.md
- frameworks/ai-governability.md
- domains/public-defense.md (if authorization / evidence)
- domains/energy-utilities.md (if operational reality)

Focus:
- Accountability first, then failure impact, data, transparency, fairness
- Evidence and owner per principle
- Do not copy NIST / vendor principle catalogs

---

# Vendor Proposal Evaluation

Load:
- standards/vendor-proposal-evaluation.md
- knowledge/patterns/scoring-vs-calibration.md
- knowledge/patterns/reproposal-as-uncertainty-reduction.md (if first-stage gaps)
- standards/vendor-key-person-interview.md (if named PM / key people)
- playbooks/private-it-rfp-vendor-selection.md (if end-to-end selection)
- standards/deliverable-archetypes.md (Archetype B)
- standards/consulting-review.md
- core/author-voice.md
- knowledge/lessons/author-voice-archetypes-legacy.md (Archetype 2)
- Relevant RFP / domain context (if available, non-confidential)

Focus:
- Evaluation criteria design (rationale per scoring point)
- Understanding / capability / credibility / estimate / contractability
- Even-stage scoring; calibrate variance instead of averaging
- Value-add definition
- First vs second evaluation
- Fair comparison across vendors

Do not load public-procurement protest logic unless the engagement is buyer-side public sector.

Outputs:
- Evaluation sheet design
- Scoring rationale
- Gap / concern summary
- Shortlist or selection recommendation with evidence

---

# Private IT RFP / Vendor Selection

Load:
- frameworks/private-it-rfp.md
- frameworks/vendor-delivery-model-gap-analysis.md (if prime vs in-house / lot split is still open)
- playbooks/private-it-rfp-vendor-selection.md
- standards/vendor-proposal-evaluation.md
- standards/vendor-key-person-interview.md
- knowledge/patterns/scoring-vs-calibration.md
- knowledge/patterns/reproposal-as-uncertainty-reduction.md
- knowledge/patterns/estimate-target-commitment.md (if estimate integrity)
- frameworks/program-phases-investigation-to-requirements.md (if requirement baseline is still open)
- standards/requirements-document-outline.md (if requirement structure)

Focus:
- Buyer decisions before RFP issue
- Confirmed vs variable vs intentionally open requirements
- RFP questions that have an evaluation use
- Staged uncertainty reduction, not a one-shot beauty contest
- Re-proposal as commitment, not slide polish
- Do not mix with statutory public procurement

Outputs:
- RFP structure / readiness gate
- Evaluation pack
- Shortlist, re-proposal questions, interview plan
- Preferred-vendor recommendation without relying on total score alone

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
- standards/requirements-artifact-review.md
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
- knowledge/patterns/borrowed-operating-model-must-fit.md (if copying another firm's process)
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
- playbooks/pmo-function-standup.md (if the office exists on paper but not in operation)
- playbooks/program-governance-cadence.md (if SteerComm / program board / standup / inspection are collapsing into one status meeting)
- playbooks/cross-project-program-management.md (if PgMO is buried in vendor WBS detail; PJ間 dependency / consistency / hand-off control is missing)
- knowledge/patterns/hybrid-talent-in-transformation.md (if the program has no people who can redesign work)
- knowledge/patterns/multi-year-transformation-sequence.md (if strategy, HR, systems, and purchasing are split across years)
- frameworks/change-management.md (if people-side design, not only PMO ownership)
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
- Cadence stack: who meets for what; escalation between layers; inspection vs status
- Cross-project artifacts: 5 domains (scope boundary, dependency, interface, consistency, schedule); Control Cycle; template classes
- Phase 1 controlled document set (policy, roadmap, meeting pack) vs live minutes
- Change management: stakeholder progression (Awareness → Ownership); readiness and strategy in `change-management.md`

Outputs:
- PMO assessment or target operating model for program office
- Portfolio criteria and governance cadence
- Program roadmap and scenario
- RACI / steering structure
- Gap summary for executive decisions
- Standup sequence (rules → pilot → people) when the office is being created
- Cadence design and Phase 1 document classes when the office is already named

---

# DX Grand Design

Load:
- frameworks/dx-grand-design.md
- frameworks/transformation-roadmap.md
- frameworks/change-management.md
- knowledge/patterns/hybrid-talent-in-transformation.md (if reform will not stick)
- domains/public-defense.md (if the sponsor is a public / research body — buyer constraints only)

Focus:
- Next-year execution needs a promotion system this year
- Compound causes: understanding/silos, unvalued contribution, HR practice
- Do not treat a slogan pack as a grand design

Outputs:
- Structured issues
- Promotion operating sketch
- Boundary of what next year will actually change

---

# New Venture Assessment

Load:
- frameworks/new-venture-three-track-assessment.md
- frameworks/consulting-strategy-process.md (if problem / options are still mushy)
- standards/strategy-engagement-guide.md (if scoping)

Focus:
- Market scenario, technology constraint, and firm-fit in parallel
- Do not let a thick tech pack substitute for commercialization
- Do not copy another firm's development coalition

Outputs:
- Three-track findings with unresolved contradictions kept visible
- Conditional go / no-go language, not a single TAM slide

---

# B2B Sales Workflow Reform

Load:
- knowledge/patterns/sales-capacity-via-center-functions.md
- frameworks/operating-model.md
- frameworks/change-management.md
- playbooks/offering-review.md (if the pitch confuses To-Be, mechanism, PMO, and change)

Focus:
- Center functions free seller time; CRM/AI sit on a workflow
- Future-state β before program/KPI
- Lost-bid method may be reusable; lost-bid gossip is not knowledge

Outputs:
- Center-function sketch
- Envision → β → program outline

---

# Change Management

Load:
- frameworks/change-management.md
- knowledge/patterns/all-at-once-vs-stepwise-change.md
- knowledge/patterns/ai-coe-vs-pgmo-vs-change.md (if the change is AI adoption, not a system cutover)
- standards/pmo-operating-guide.md (§Change Management Operating Standard)
- frameworks/transformation-pmo.md (if program-owned change)
- knowledge/patterns/platform-build-vs-enablement.md (if platform / data adoption)
- knowledge/patterns/authority-levels.md (if decision rights must transfer)
- core/author-voice.md
- standards/writing.md

Focus:
- Readiness before communication calendar
- All-at-once vs stepwise configuration
- Why / unit / me; time-phased messages; resistance as design input
- Transfer of ownership, not only training

Outputs:
- Readiness findings and barrier actions
- Change strategy choice and sequence
- Stakeholder action log and message map
- Soft-landing / hypercare communication outline

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
- knowledge/patterns/organizational-memory.md
- knowledge/patterns/exception-as-memory-entry.md
- knowledge/patterns/connected-organizational-memory.md
- knowledge/patterns/authority-levels.md
- knowledge/patterns/operational-reality.md
- knowledge/lessons/dual-roadmap-messaging.md (if executive audience)
- playbooks/ai-utilization-roadmap.md (if building or reviewing the roadmap pack)
- playbooks/ai-work-before-after.md (if field Before / After)
- knowledge/patterns/ai-coe-vs-pgmo-vs-change.md (if CoE / PgMO / Change are being mixed)
- standards/consulting-review.md (if deliverable review)

Focus:
- Dual-layer roadmap (technology × people)
- Year 1–5 narrative and three-initiative sequence
- Role × phase maturity and HR triggers
- Authority design by phase
- Executive vs internal messaging
- CoE vs AI PgMO vs Change as three offices (`knowledge/patterns/ai-coe-vs-pgmo-vs-change.md`)

Outputs:
- Adoption roadmap narrative
- Initiative prioritization and sync rules
- Role maturity and enablement plan (draft)
- Workshop or proposal sections on DX / AI change

---

# AI CoE / AI PgMO / AI Change

Load:
- knowledge/patterns/ai-coe-vs-pgmo-vs-change.md
- frameworks/ai-management-office.md
- frameworks/transformation-pmo.md
- frameworks/change-management.md
- playbooks/offering-review.md (if the three are sold as one blur)
- playbooks/pmo-function-standup.md (if the program office is paper-only)

Focus:
- Three functions; weight shifts by phase
- Central CoE then hybrid return to the line
- Program value vs project QCD; strategy before a PoC portfolio
- AI change ≠ ERP change

Outputs:
- Interface sketch among CoE, PgMO, Change
- What not to fold into one “AI PMO”

---

# Application Outsourcing / AMS Proposal

Load:
- frameworks/application-outsourcing-solution-planning.md
- frameworks/ams-services-pyramid.md
- frameworks/service-transition-approach.md
- standards/ams-solution-plan-checklist.md
- standards/deliverable-archetypes.md (Archetype I)
- frameworks/it-strategy-foundations.md (§Sourcing — if strategic fit check)
- frameworks/sap-implementation-phase-model.md (if SAP AM / post-go-live scope)
- frameworks/transformation-pmo.md (if large transition program)
- standards/operations-handover-guide.md (if handover from implementation partner)
- standards/vendor-proposal-evaluation.md (if client-side evaluation mirror)
- frameworks/infrastructure-outsourcing-solution-planning.md (if bundled AO+IO or infra towers)
- core/author-voice.md
- standards/consulting-review.md (if deliverable review)

Focus:
- Solution Planning phases (baseline → To-Be → size → transition → proposal)
- Services pyramid scope split (AM / dev / infra)
- Estimating approach and assumption traceability
- Location and staffing pyramid decisions
- Transition waves, KT, and responsibility transfer
- Proposal outline vs internal Solution Plan consistency

Outputs:
- Solution Plan sections (checklist-driven)
- AMS / outsourcing proposal deck (Archetype I)
- Transition approach summary
- Assumption and risk register

---

# Infrastructure Outsourcing / ITO Proposal

Load:
- frameworks/infrastructure-outsourcing-solution-planning.md
- knowledge/patterns/transition-vs-transformation-vs-realization.md
- frameworks/service-transition-approach.md
- frameworks/application-outsourcing-solution-planning.md (if bundled AO+IO)
- frameworks/change-management.md (if staff transfer or operating-model change)
- frameworks/transformation-pmo.md (if large transformation program)
- standards/operations-handover-guide.md (if run handover)
- standards/vendor-proposal-evaluation.md (if client-side evaluation mirror)
- core/author-voice.md
- standards/consulting-review.md (if deliverable review)

Focus:
- Buyable × deliverable × financial
- Take-on: D-B-R vs integrate transition+transformation vs as-is run
- Run vs discretionary; CFS assumed when “you run IT”
- SLA: excused performance, low volume, fee-at-risk cap
- Contract ↔ approved solution two-way; inflation and FX in multi-year cost
- Prime/sub vs operational management of third parties

Outputs:
- IO Solution Plan (towers, OM ownership, assumptions)
- Take-on and transformation sequence
- SLA / commercial outline
- Risk and diligence plan

---

# Systems Integration / SI Proposal

Load:
- frameworks/systems-integration-solution-planning.md
- knowledge/patterns/estimate-target-commitment.md
- frameworks/delivery-leadership.md (if handoff or post-signature)
- knowledge/patterns/transition-vs-transformation-vs-realization.md (if go-live support / warranty)
- frameworks/application-outsourcing-solution-planning.md (if AM after build)
- frameworks/infrastructure-outsourcing-solution-planning.md (if infra towers bundled)
- core/author-voice.md
- standards/consulting-review.md (if deliverable review)

Focus:
- Estimate ≠ target ≠ commitment; work is the work
- Solution Plan completeness questions
- Blueprint before firm estimate; V-model by release
- Negotiation vs solution contingency; contract relief not eaten by contingency
- Tick and tie: estimate, commercial, SOW, Solution Plan
- Deliverable = thing not action

Outputs:
- SI Solution Plan
- Estimate basis and contingency split
- Delivery strategy (releases, locations)
- Handoff pack for Delivery Lead

---

# Delivery Leadership

Load:
- frameworks/delivery-leadership.md
- frameworks/systems-integration-solution-planning.md (if sold SI solution)
- frameworks/transformation-pmo.md
- frameworks/change-management.md
- knowledge/patterns/transition-vs-transformation-vs-realization.md
- frameworks/service-transition-approach.md (if outsourcing take-on)
- core/author-voice.md
- standards/pmo-operating-guide.md (if program office)

Focus:
- Project vs program; value scorecard vs SLA
- Contract vs customer expectation
- ODE vs EAC; no surprises in transition
- Introduction vs transition vs warranty
- Release at a rate the organization can absorb

Outputs:
- Mobilization and expectation plan
- Change-control setup
- EAC / original-deal comparison narrative
- Service introduction or transition outline

---

# Energy / Utilities

Load:
- domains/energy-utilities.md
- knowledge/patterns/operational-reality.md
- knowledge/patterns/experience-before-scope.md (if customer-facing / portal / CRM)
- knowledge/patterns/platform-build-vs-enablement.md (if data platform / CDP / enablement)
- standards/requirements-artifact-review.md (if requirements review)
- frameworks/operating-model.md
- frameworks/ai-adoption-roadmap.md (if DX / AI in operations or retail)
- knowledge/patterns/authority-levels.md (if plant autonomy or group decision rights)

Focus:
- Do not mix generation-AM logic with retail-customer logic
- Experience → process → data → scope (not feature lists first)
- Continuity investment vs transformation investment
- Build vs enablement for data platforms

Outputs:
- Domain-informed problem framing
- Layered customer-system map (CIS / CRM / CDP / CC)
- Scope cuts for transition
- Requirements review notes (business bench)

---

# Public Sector / Defense IT

Load:
- domains/public-defense.md
- knowledge/patterns/buyer-vs-seller-in-public-procurement.md
- knowledge/patterns/shared-operator-vs-ministry-vs-municipality.md (if shared local-government IT, not a ministry or a single municipality)
- frameworks/public-it-procurement-support.md (if buyer-side procurement, scrutiny, or construction PMO)
- playbooks/public-multi-lot-construction-pmo.md (if concurrent lots, start-of-stage gates, ops-doc merge)
- frameworks/program-phases-investigation-to-requirements.md (if concept → requirements)
- standards/vendor-proposal-evaluation.md (if technical evaluation)
- standards/requirements-document-outline.md (if requirements document)
- frameworks/systems-integration-solution-planning.md (if seller SI bid)
- core/author-voice.md
- standards/consulting-review.md (if deliverable review)

Focus:
- Buyer fairness vs seller win — do not mix on the same program
- Shared operator ≠ ministry ≠ municipality; multi-lot acceptance is one story
- 適合条件 before scoring; estimate scrutiny ≠ proposal scoring
- Officials keep authorization / risk decisions
- No inventories, yen, or network designs in generalized output

Outputs:
- Role-clear engagement framing
- Procurement or scrutiny workplan (buyer)
- Evaluation-item-mapped proposal outline (seller, no confidential facts)

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
- `technology/azure-enterprise.md`
- `playbooks/private-api-connectivity-diagnosis.md` (if 502/500, APIM, private path, environment switch)
- `playbooks/interim-connectivity.md` (if target path blocked; gateway / outbound looks like auth)
- `playbooks/rag-structure-diagnosis.md` (if search hits but table/KPI answer is wrong)
- `playbooks/azure-sandbox-cost-guard.md` (if PoC / sandbox / unexpected Azure cost)
- `knowledge/decisions/diagnose-from-gateway-not-client-error.md` (if diagnosing the chain)
- `knowledge/decisions/interim-connectivity-is-not-the-target.md` (if choosing an interim path)
- `knowledge/decisions/sandbox-cost-controls-before-resources.md` (if creating or stopping a sandbox)
- Project constraints (non-confidential)

Focus:
- Communication chain, not connector-only design
- Security, integration, operations, maintainability, cost
- Client HTTP status as symptom; gateway backend response as split
- High-fixed-cost SKUs as explicit decisions

Do not load FQDNs, yen, or resource names from local originals.

---

# LinkedIn / Note Writing

Load:
- standards/writing.md (including §De-AI Writing Pass)
- core/author-voice.md
- core/identity.md
- core/values.md
- Relevant framework
- Related patterns (e.g. `organizational-memory.md`, `exception-as-memory-entry.md`, `connected-organizational-memory.md` for Memory Arc)
- Previous posts in the series

Focus:
- Author voice over AI-polished uniformity
- De-AI pass before publish (see `writing.md`)
- Series continuity (Governance Arc No.13–17; Memory Arc No.18+)

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
