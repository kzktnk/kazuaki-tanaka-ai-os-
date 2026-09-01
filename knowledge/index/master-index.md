# Knowledge Master Index

**Version:** v1.20  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Expandable 3–4 level map of the AI OS knowledge base  
**Last updated:** 2026-09-01

---

## 日本語 — このファイルの役割

知識体系の**全体像を3〜4階層まで**確認するための統合インデックスです。

- **構造の設計思想** → `ARCHITECTURE.md` §4（8論理層）
- **実務で何を読むか** → `CONTEXT_ROUTING.md`（タスク別。全件は読まない）
- **本ファイル** → リポジトリ内の資産所在と、主要な知識の流れ

**メンテナンス:** 知識の追加・移行（migration）のたびに本ファイルを更新する（下記 §Maintenance）。

---

## Purpose (English)

This is the **inventory and navigation map** for the Kazuaki Tanaka AI OS.

It is **not** a context-loading list. AI systems and humans should use `CONTEXT_ROUTING.md` to load only task-relevant files. This index answers: *where does knowledge live, and how do layers connect?*

---

## What Gets Loaded in Practice

Expanded knowledge is **stored** in the repository but **not fully read** during normal tasks.

| Layer | Typical use in work | Usually loaded? |
|-------|---------------------|---------------|
| `core/`, `standards/` | Judgment and quality bar | Yes — minimum core always; standards per task |
| `frameworks/`, `playbooks/` | Structure and execution | Yes — when task-relevant |
| `knowledge/patterns/`, `lessons/` | Distilled insight | Yes — when routed or cross-linked |
| `knowledge/source/` | Original posts, PDFs, archives | **No** — except migration, writing continuity, or audit |
| `knowledge/migrations/` | Change records | **No** — except migration or maintenance |
| `knowledge/index/` | Navigation | Humans: yes for orientation. AI: only for repo maintenance tasks |

**Flow:** Experience → `source/` → extract → `patterns/` / `lessons/` / `frameworks/` → `CONTEXT_ROUTING.md` selects subset for each task.

---

## Level 1 — Eight Logical Layers

From `ARCHITECTURE.md` §4 (bottom = most stable):

```text
1. Core                    identity, principles, values, reasoning
2. Standards               what good looks like
3. Frameworks & domains    how problems are structured
4. Playbooks               how work is executed
5. Knowledge assets        lessons, patterns, decisions, sources
6. Templates & prompts     reusable forms and instructions
7. Project context         temporary, often external repos
8. Adapters                tool-specific loading (Cursor, etc.)
```

---

## Level 2 — Repository Directories

```text
kazuaki-tanaka-ai-os/
├── AI_OPERATING_MANUAL.md      ← primary execution entry (AI)
├── ARCHITECTURE.md             ← structural blueprint
├── CONTEXT_ROUTING.md          ← task-based context selection
├── core/                       ← 8 files (kernel)
├── standards/                  ← 19 files (quality criteria)
├── frameworks/                 ← 33 files + thinking-patterns/
├── playbooks/                  ← 23 playbooks (+ README)
├── knowledge/
│   ├── index/                  ← this file + domain indexes
│   ├── source/                 ← preserved originals (LinkedIn, etc.)
│   ├── patterns/               ← 40 distilled patterns
│   ├── lessons/                ← 6 lessons
│   ├── migrations/             ← 31 migration reports
│   └── decisions/              ← 4 records
├── templates/                  ← 1 template
├── prompts/                    ← README placeholder
├── projects/                   ← project template structure
├── adapters/cursor/            ← Cursor adapter
├── adapters/claude/            ← Claude adapter (CLAUDE.md)
├── domains/                    ← energy-utilities.md, public-defense.md
├── technology/                 ← azure-enterprise.md (parent)
└── archive/                    ← README placeholder
```

**Domain indexes (Level 3 detail in separate files):**

| Index | Scope |
|-------|--------|
| [linkedin-series-index.md](./linkedin-series-index.md) | LinkedIn / Note sources 001–022, sp01–09, erf01–03 |
| [legacy-source-index.md](./legacy-source-index.md) | Local legacy PDFs → repo extraction map (Program Lines A–X) |

---

## Level 3 — Core

```text
core/
├── principles.md
├── identity.md
├── values.md
├── reasoning.md              ← source of truth for reasoning
├── reasoning_update.md       ← pending / patch material
├── reasoning.md.patch.md
├── author-voice.md
└── ai-collaboration.md
```

---

## Level 3 — Domains

```text
domains/
├── README.md
├── energy-utilities.md           ← parent (generation / T&D stub / retail + cross-cutting)
└── public-defense.md             ← parent (Japan public / defense IT; buyer vs seller; shared local-gov operator)
```

---

## Level 3 — Technology

```text
technology/
├── README.md
└── azure-enterprise.md           ← parent (communication chain, APIM as contract, identity by host, sandbox cost)
```

Do not split yet.

---

## Level 3 — Standards (19)

Grouped by domain for navigation:

```text
standards/
├── Consulting & strategy
│   ├── consulting-review.md
│   ├── strategy-engagement-guide.md
│   ├── it-strategy-engagement-guide.md
│   ├── vendor-proposal-evaluation.md
│   └── vendor-key-person-interview.md
├── Deliverables & documents
│   ├── deliverable-archetypes.md
│   ├── requirements-document-outline.md
│   ├── requirements-artifact-review.md
│   ├── document-management-standard.md
│   └── writing.md
├── Application outsourcing / AMS
│   └── ams-solution-plan-checklist.md
├── Development & ERP delivery
│   ├── development-standards-framework.md
│   ├── development-management-guide.md
│   ├── environment-management-guide.md
│   ├── release-management-guide.md
│   ├── operations-design-guide.md
│   └── operations-handover-guide.md
├── Program & PMO
│   └── pmo-operating-guide.md
└── Strategy consulting (SCN)
    ├── scn-creation-guide.md
    └── (execution) playbooks/strategy-scn.md
```

---

## Level 3 — Frameworks (33 + thinking patterns)

```text
frameworks/
├── readme.md                         ← framework catalog (summary)
├── thinking-patterns/
│   ├── README.md
│   └── pattern-01 … pattern-08       ← reusable thinking structures
├── AI & governance
│   ├── ai-governability.md
│   ├── ai-governability_update.md
│   ├── decision-ownership.md
│   ├── human-oversight.md
│   ├── governance-operating-model.md
│   ├── ai-adoption-roadmap.md
│   ├── ai-role-maturity.md
│   └── ai-management-office.md
├── Strategy & consulting
│   ├── consulting-strategy-process.md
│   ├── it-strategy-foundations.md
│   ├── strategic-capability-network.md
│   ├── top-down-thinking.md
│   ├── decision-velocity.md
│   └── new-venture-three-track-assessment.md
├── Transformation & operating model
│   ├── operating-model.md
│   ├── capability-model.md
│   ├── maturity-model.md
│   ├── transformation-roadmap.md
│   ├── transformation-pmo.md
│   ├── dx-grand-design.md
│   ├── change-management.md
│   └── program-phases-investigation-to-requirements.md
├── Application outsourcing / AMS
│   ├── application-outsourcing-solution-planning.md
│   ├── ams-services-pyramid.md
│   └── service-transition-approach.md
├── Infrastructure outsourcing / ITO
│   └── infrastructure-outsourcing-solution-planning.md
├── Systems integration / delivery
│   ├── systems-integration-solution-planning.md
│   └── delivery-leadership.md
├── Public IT procurement (buyer)
│   └── public-it-procurement-support.md
├── Private IT RFP (buyer)
│   ├── private-it-rfp.md
│   └── vendor-delivery-model-gap-analysis.md
├── ERP / SAP
│   └── sap-implementation-phase-model.md
└── principles.md                     ← framework-layer principles
```

---

## Level 3 — Knowledge

```text
knowledge/
├── index/
│   ├── master-index.md               ← this file
│   ├── linkedin-series-index.md
│   └── legacy-source-index.md
├── source/
│   └── linkedin/
│       ├── 001–022/                  ← Operational AI main series
│       ├── sp01–sp09/                ← special posts
│       └── erf01–erf03/              ← Enterprise Redesign Framework
├── patterns/                         ← 41 files (see table below)
├── lessons/
│   ├── governance-messaging.md
│   ├── dual-roadmap-messaging.md
│   ├── pmo-professional-principles.md
│   ├── author-voice-archetypes-legacy.md
│   ├── client-deliverable-voice-jera-2026-08.md
│   └── ai-output-evaluation-terms.md
├── migrations/
│   ├── linkedin-bulk-001-015-sp-erf.md
│   ├── linkedin-013.md
│   ├── linkedin-014.md
│   ├── linkedin-016.md
│   ├── linkedin-017.md
│   ├── linkedin-018.md
│   ├── linkedin-019.md
│   ├── linkedin-020.md
│   ├── linkedin-021.md
│   ├── linkedin-022.md
│   ├── ai-dual-roadmap-2026-08.md
│   ├── ao-sae-2026-08.md
│   ├── energy-utilities-domain-2026-08.md
│   ├── change-management-2026-08.md
│   ├── iosa-2026-08.md
│   ├── sisa-sidl-dma-2026-08.md
│   ├── public-defense-2026-08.md
│   ├── azure-enterprise-2026-08.md
│   ├── ai-playbooks-2026-08.md
│   ├── private-it-rfp-2026-08.md
│   ├── enterprise-engagements-2013-2023-2026-08.md
│   ├── pgmo-ai-change-2026-08.md
│   ├── local-gov-shared-it-2026-08.md
│   ├── related-project-radar-and-et-case-pack-2026-08.md
│   ├── program-governance-cadence-2026-08.md
│   ├── cross-project-program-management-2026-08.md
│   ├── strategy-scn-2026-08.md
│   ├── operations-transition-2026-08.md
│   ├── stakeholder-activation-2026-08.md
│   ├── fisc-audit-tech-ops-facility-2026-08.md
│   ├── project-management-policy-layer-2026-08.md
│   ├── customer-status-weekly-monthly-2026-08.md
│   ├── coaching-20260828-change-effort-buyer-gap-2026-08.md
│   └── claude-foundations-and-logical-unity-2026-09.md
└── decisions/
    ├── diagnose-from-gateway-not-client-error.md
    ├── sandbox-cost-controls-before-resources.md
    ├── interim-connectivity-is-not-the-target.md
    └── buyer-owns-ai-poc-ground-truth.md
```

### Patterns (40)

| Pattern | Primary themes |
|---------|----------------|
| `buyer-side-gap-vs-vendor-pmo.md` | Vendor PMO ≠ buyer ハザマ; continuation ≠ next-phase value; monthly as go-live-path education |
| `unowned-work-in-effort-analysis.md` | Person-tied PDC leaks unowned work; 検討主体 then execute/manage; actuals ≠ WBS |
| `change-agent-vs-communication-plan.md` | Agent hunt ≠ communication plan; plan before samples |
| `pgmo-presence-via-client-stance.md` | Client-side PM/PO stance; ally with trusted incumbent; intersection risk → monthly→weekly reverse tracking |
| `related-project-external-coordination-radar.md` | Adjacent-project radar + external coordination; hypothesis → confirm → promote |
| `transformation-practice-case-pack.md` | Internal ET practice case-pack anatomy; Role × type matrix; theme-card schema |
| `support-effort-classification.md` | Support effort buckets: per-PJ / between projects / cross-cutting + issue mgmt |
| `project-management-policy-layer.md` | Project-layer PM policy TOC; progress measure; issue/risk/ToDo; change vs baseline; customer-shared open items |
| `fis-system-audit-as-assurance.md` | Industry system-audit guidance as buyer assurance, not checklist paste |
| `operational-governance.md` | Operational AI, governance as capability |
| `operational-reality.md` | OT / field reality vs DX narrative |
| `experience-before-scope.md` | Experience → process → data → scope |
| `platform-build-vs-enablement.md` | Platform release vs ability to run the loop |
| `all-at-once-vs-stepwise-change.md` | Change strategy: cutover vs sequenced steps |
| `transition-vs-transformation-vs-realization.md` | Introduction / transition / transformation / realization |
| `estimate-target-commitment.md` | Estimate ≠ target ≠ commitment; work is the work |
| `buyer-vs-seller-in-public-procurement.md` | Public IT: buyer fairness vs seller bid |
| `shared-operator-vs-ministry-vs-municipality.md` | Shared local-gov IT: operator ≠ ministry ≠ municipality |
| `scoring-vs-calibration.md` | Score makes judgment visible; calibration makes it reliable |
| `reproposal-as-uncertainty-reduction.md` | Re-proposal converts uncertainty into commitment |
| `hybrid-talent-in-transformation.md` | Knowledge + design + action; train in the program |
| `borrowed-operating-model-must-fit.md` | Peer L2 flows copy only if the business model matches |
| `multi-year-transformation-sequence.md` | Strategy→people→system; delay ≠ missing executive information |
| `sales-capacity-via-center-functions.md` | B2B productivity from centers, not from CRM slogans |
| `ai-coe-vs-pgmo-vs-change.md` | CoE, AI PgMO, and Change are three offices; AI change ≠ ERP |
| `expertise-amplification.md` | AI amplifies experts |
| `organizational-memory.md` | Intelligence vs organizational memory; decision context |
| `exception-as-memory-entry.md` | Exceptions as memory entry; capture at deviation |
| `connected-organizational-memory.md` | Capture vs connection; retrieval vs memory; standard-review signals |
| `memory-at-decision.md` | Timing vs retrieval; return memory at the decision; surfacing risks |
| `standard-as-learned-memory.md` | Standard as compressed learning; exception → standard loop; AI visible, humans govern |
| `operating-model-advantage.md` | Competitive advantage from operating model |
| `ai-resilience-shift.md` | Productivity → resilience |
| `decision-ownership.md` | Execution ≠ ownership |
| `decision-delegation.md` | Delegation boundaries |
| `verifiable-ownership.md` | Ownership must be provable |
| `risk-ownership.md` | Work delegation ≠ risk accountability |
| `ai-capability-vs-authority.md` | Capability ≠ authority |
| `authority-levels.md` | Graduated authority design |
| `jera-scn-ebitda-tree.md` | SCN / EBITDA tree (client voice lesson) |
| `logical-vs-physical-document-unity.md` | Physical store ≠ logical AI corpus; governance first |

---

## Level 3 — Playbooks, Templates, Adapters

```text
playbooks/
├── README.md
├── wbs-design.md
├── ai-work-before-after.md
├── ai-utilization-roadmap.md
├── ai-poc-quality-review.md
├── offering-review.md
├── responsible-ai-assessment.md
├── rag-structure-diagnosis.md
├── private-it-rfp-vendor-selection.md
├── pmo-function-standup.md
├── program-governance-cadence.md
├── strategy-scn.md
├── strategy-scn-selfstudy.md
├── cross-project-program-management.md
├── cross-project-program-management-selfstudy.md
├── operations-transition-playbook.md
├── operations-transition-playbook-selfstudy.md
├── stakeholder-activation-playbook.md
├── stakeholder-activation-playbook-selfstudy.md
├── public-multi-lot-construction-pmo.md
├── interim-connectivity.md
├── private-api-connectivity-diagnosis.md
└── azure-sandbox-cost-guard.md

templates/
└── wbs-breakdown-sheet.md

prompts/
└── README.md

archive/
└── README.md

adapters/cursor/
└── CURSOR.md                         ← Cursor-specific behavior + migration rules

adapters/claude/
└── CLAUDE.md                         ← Claude feature differentiation; not a knowledge silo
```

---

## Level 4 — Knowledge Flow Examples

### A. Governance series (LinkedIn No.13–17)

```text
knowledge/source/linkedin/013–017/
        ↓ extract
knowledge/patterns/  (decision-ownership, verifiable-ownership, risk-ownership,
                      ai-capability-vs-authority, authority-levels)
        ↓ elevate
frameworks/  (ai-governability, decision-ownership, human-oversight)
        ↓ messaging
knowledge/lessons/governance-messaging.md
        ↓ record
knowledge/migrations/linkedin-*.md
        ↓ task routing
CONTEXT_ROUTING.md  →  AI Governance / LinkedIn Writing sections
```

### B. ERP / development standards (legacy → standards)

```text
Local legacy (Program Line A, H, I, X)     ← legacy-source-index.md
        ↓ generalize
standards/development-standards-framework.md  (+ tech/ops/facility layer)
standards/development-management-guide.md
standards/deliverable-archetypes.md
frameworks/sap-implementation-phase-model.md
knowledge/patterns/fis-system-audit-as-assurance.md
knowledge/patterns/project-management-policy-layer.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Development Standards / Build Phase
```

### C. IT strategy foundations (Program Line G)

```text
Local Module PDFs (IT_Strategy_Foundation/)
        ↓
frameworks/it-strategy-foundations.md
standards/it-strategy-engagement-guide.md
```

### D. AI dual roadmap (2026-08)

```text
Internal AI utilization + people maturity roadmaps (not archived)
        ↓ generalize
frameworks/ai-adoption-roadmap.md
frameworks/ai-role-maturity.md
frameworks/ai-management-office.md (update)
knowledge/lessons/dual-roadmap-messaging.md
        ↓ record
knowledge/migrations/ai-dual-roadmap-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  AI Adoption / DX Roadmap
```

---

### E. Application outsourcing SAE (Program Line J, 2026-08)

```text
Local AOSAE PDFs (Downloads/AO Materials/) — not archived
        ↓ generalize
frameworks/application-outsourcing-solution-planning.md
frameworks/ams-services-pyramid.md
frameworks/service-transition-approach.md
standards/ams-solution-plan-checklist.md
standards/deliverable-archetypes.md (Archetype I)
        ↓ record
knowledge/migrations/ao-sae-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Application Outsourcing / AMS Proposal
```

### F. Organizational memory (LinkedIn No.18–22)

```text
knowledge/source/linkedin/018/
        ↓ extract
knowledge/patterns/organizational-memory.md
        ↓ cross-link
frameworks/ai-adoption-roadmap.md (Initiative B)
frameworks/ai-role-maturity.md
knowledge/patterns/expertise-amplification.md
knowledge/patterns/operational-reality.md
        ↓ record
knowledge/migrations/linkedin-018.md
        ↓ continue (No.19)
knowledge/source/linkedin/019/
        ↓ extract
knowledge/patterns/exception-as-memory-entry.md
        ↓ standard
standards/writing.md (§De-AI Writing Pass)
        ↓ record
knowledge/migrations/linkedin-019.md
        ↓ continue (No.20)
knowledge/source/linkedin/020/
        ↓ extract
knowledge/patterns/connected-organizational-memory.md
        ↓ record
knowledge/migrations/linkedin-020.md
        ↓ continue (No.21)
knowledge/source/linkedin/021/
        ↓ extract
knowledge/patterns/memory-at-decision.md
        ↓ record
knowledge/migrations/linkedin-021.md
        ↓ continue (No.22)
knowledge/source/linkedin/022/
        ↓ extract
knowledge/patterns/standard-as-learned-memory.md
        ↓ record
knowledge/migrations/linkedin-022.md
        ↓ task routing
CONTEXT_ROUTING.md  →  AI Adoption / DX Roadmap, LinkedIn Writing
```

### G. Energy & utilities domain (Program Line K + existing patterns)

```text
Local retail customer program decks (Downloads/) — not archived
        ↓ generalize
domains/energy-utilities.md
standards/requirements-artifact-review.md
knowledge/patterns/experience-before-scope.md
knowledge/patterns/platform-build-vs-enablement.md
        ↓ existing generation/AM
knowledge/patterns/operational-reality.md
        ↓ record
knowledge/migrations/energy-utilities-domain-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Energy / Utilities, Proposal Review
```

### H. Change management (Program Line L)

```text
Local CM Day1–Day2 .ppt (Downloads/CM/) — not archived
        ↓ generalize (English structure only)
frameworks/change-management.md
knowledge/patterns/all-at-once-vs-stepwise-change.md
        ↓ cross-link
frameworks/transformation-pmo.md
standards/pmo-operating-guide.md
        ↓ record
knowledge/migrations/change-management-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Change Management, Transformation PMO
```

### I. Infrastructure outsourcing SA (Program Line M)

```text
Local IO SA Intermediate / Advanced (Downloads/IOSA/) — not archived
        ↓ generalize
frameworks/infrastructure-outsourcing-solution-planning.md
knowledge/patterns/transition-vs-transformation-vs-realization.md
        ↓ cross-link
frameworks/application-outsourcing-solution-planning.md
frameworks/service-transition-approach.md
        ↓ record
knowledge/migrations/iosa-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Infrastructure Outsourcing / ITO Proposal
```

### J. SI solution planning & delivery leadership (Program Lines N–O)

```text
Local SISA/SIDL and DMA II–III — not archived
        ↓ generalize
frameworks/systems-integration-solution-planning.md
frameworks/delivery-leadership.md
knowledge/patterns/estimate-target-commitment.md
        ↓ extend
knowledge/patterns/transition-vs-transformation-vs-realization.md
        ↓ record
knowledge/migrations/sisa-sidl-dma-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Systems Integration / SI Proposal, Delivery Leadership
```

### K. Public sector & defense IT (Program Line P)

```text
Local ministry-OA / defense-adjacent packs — not archived
        ↓ generalize (no specs, yen, inventories)
domains/public-defense.md
frameworks/public-it-procurement-support.md
knowledge/patterns/buyer-vs-seller-in-public-procurement.md
knowledge/patterns/shared-operator-vs-ministry-vs-municipality.md
knowledge/patterns/related-project-external-coordination-radar.md
playbooks/public-multi-lot-construction-pmo.md
        ↓ cross-link
frameworks/program-phases-investigation-to-requirements.md
standards/vendor-proposal-evaluation.md
        ↓ record
knowledge/migrations/public-defense-2026-08.md
knowledge/migrations/local-gov-shared-it-2026-08.md
knowledge/migrations/related-project-radar-and-et-case-pack-2026-08.md (radar + Line U skip of MM deck)
        ↓ task routing
CONTEXT_ROUTING.md  →  Public Sector / Defense IT, Public Procurement Support (buyer)
```

---

### K2. Transformation practice case pack (Program Line AA)

```text
Local enterprise transformation case pack 2019 — not archived
        ↓ generalize (structure only; no case stories / identifiers)
knowledge/patterns/transformation-practice-case-pack.md
        ↓ record
knowledge/migrations/related-project-radar-and-et-case-pack-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Transformation PMO / Program Governance (internal practice packaging)
```

---

### L. Azure enterprise (Program Line Q)

```text
Local private-API handover + sandbox cost notes — not archived
        ↓ generalize (no FQDN, yen, resource names)
technology/azure-enterprise.md
playbooks/private-api-connectivity-diagnosis.md
playbooks/azure-sandbox-cost-guard.md
knowledge/decisions/diagnose-from-gateway-not-client-error.md
knowledge/decisions/sandbox-cost-controls-before-resources.md
        ↓ record
knowledge/migrations/azure-enterprise-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Technology Architecture
```

---

### M. AI / transformation playbooks (Program Line R)

```text
Local playbook drafts — not archived
        ↓ generalize (no operator names, KPI figures, FQDN catalogs)
playbooks/ai-work-before-after.md
playbooks/ai-utilization-roadmap.md
playbooks/ai-poc-quality-review.md
playbooks/offering-review.md
playbooks/responsible-ai-assessment.md
playbooks/rag-structure-diagnosis.md
playbooks/interim-connectivity.md
knowledge/decisions/interim-connectivity-is-not-the-target.md
knowledge/decisions/buyer-owns-ai-poc-ground-truth.md
        ↓ record
knowledge/migrations/ai-playbooks-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  AI Adoption, AI PoC, Offering, RAI, Technology
```

---

### N. Private IT RFP and vendor selection (Program Line A, 2026-08 refresh)

```text
Local 2002–2003 RFP / evaluation originals + generalized MD drafts — body not archived
        ↓ generalize (no RFP text, scores, yen, vendor names)
frameworks/private-it-rfp.md
frameworks/vendor-delivery-model-gap-analysis.md
playbooks/private-it-rfp-vendor-selection.md
standards/vendor-proposal-evaluation.md (v1.1)
standards/vendor-key-person-interview.md
knowledge/patterns/scoring-vs-calibration.md
knowledge/patterns/reproposal-as-uncertainty-reduction.md
        ↓ record
knowledge/migrations/private-it-rfp-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Private IT RFP / Vendor Selection
```

---

### O. Multi-year enterprise engagements (Program Line S)

```text
Local 2013–2023 engagement folders — not archived
        ↓ generalize (no client names, yen, specs, bid bodies, media)
playbooks/pmo-function-standup.md
frameworks/dx-grand-design.md
frameworks/new-venture-three-track-assessment.md
knowledge/patterns/hybrid-talent-in-transformation.md
knowledge/patterns/borrowed-operating-model-must-fit.md
knowledge/patterns/multi-year-transformation-sequence.md
knowledge/patterns/sales-capacity-via-center-functions.md
        ↓ record
knowledge/migrations/enterprise-engagements-2013-2023-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Transformation PMO, DX Grand Design, New Venture, B2B Sales WF
```

---

### P. AI CoE / PgMO / Change split (2026 method notes)

```text
Local 2026 method deck + 2016–2018 change-plan structure — not archived
        ↓ generalize (no TCV, names, org charts, plan body)
knowledge/patterns/ai-coe-vs-pgmo-vs-change.md
frameworks/ai-management-office.md (v1.1)
frameworks/change-management.md (v1.1)
        ↓ record
knowledge/migrations/pgmo-ai-change-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  AI CoE / AI PgMO / AI Change, Change Management, AI Adoption
```

---

### Q. Program governance cadence (Program Line V)

```text
Local live PgMO cadence folders — not archived
        ↓ generalize (no client names, yen, minutes bodies, inspection results, plant/site names)
playbooks/program-governance-cadence.md
playbooks/cross-project-program-management.md
playbooks/cross-project-program-management-selfstudy.md
playbooks/strategy-scn.md  (upstream Gate 1 companion; coach edition)
playbooks/strategy-scn-selfstudy.md
playbooks/operations-transition-playbook.md  (downstream Gate 3–5)
playbooks/operations-transition-playbook-selfstudy.md
playbooks/stakeholder-activation-playbook.md  (cross-cutting activation tactic)
playbooks/stakeholder-activation-playbook-selfstudy.md
        ↓ record
knowledge/migrations/program-governance-cadence-2026-08.md
knowledge/migrations/cross-project-program-management-2026-08.md
knowledge/migrations/strategy-scn-2026-08.md
knowledge/migrations/operations-transition-2026-08.md
knowledge/migrations/stakeholder-activation-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Transformation PMO / Program Governance; Strategy Engagement / SCN
```

---

### R. Project management policy layer (Program Line Y)

```text
Local anonymized SI proposal §PM policy (Q2C-style; PPTX not in git)
        ↓ generalize (no client names, yen, EVM tables, tool brands, calendars)
knowledge/patterns/project-management-policy-layer.md
        ↓ connect
standards/development-management-guide.md
standards/pmo-operating-guide.md
playbooks/program-governance-cadence.md
        ↓ record
knowledge/migrations/project-management-policy-layer-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Transformation PMO / Development Standards
```

---

### S. Customer weekly/monthly status (Program Line Z)

```text
Local coaching recording 2026-08-24 — content not archived
        ↓ generalize (no client names, yen, personal names, schedule numbers, transcript)
standards/deliverable-archetypes.md Archetype J
knowledge/patterns/support-effort-classification.md
        ↓ connect
knowledge/patterns/project-management-policy-layer.md
core/author-voice.md
frameworks/top-down-thinking.md
playbooks/program-governance-cadence.md (pointer only)
playbooks/cross-project-program-management.md (pointer only)
        ↓ record
knowledge/migrations/customer-status-weekly-monthly-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Customer Status Report (Weekly / Monthly)
```

---

### T. Multi-vendor PgMO presence coaching (Program Line AB)

```text
Local mentor–mentee Slack thread export (.rtf) — content not archived
        ↓ generalize (no names, client/program IDs, yen, schedule actuals, raw dump)
knowledge/patterns/pgmo-presence-via-client-stance.md
        ↓ connect (no new type)
knowledge/patterns/related-project-external-coordination-radar.md
playbooks/cross-project-program-management.md
knowledge/lessons/pmo-professional-principles.md
        ↓ record
knowledge/migrations/pgmo-presence-client-stance-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Transformation PMO / Program Governance
```

---

### U. Monthly status / change / effort / buyer-gap coaching (Program Line AE)

```text
Local coaching recording 2026-08-28 — content not archived
        ↓ generalize (no client names, yen, personal names, schedule numbers, transcript)
knowledge/patterns/change-agent-vs-communication-plan.md
knowledge/patterns/unowned-work-in-effort-analysis.md
knowledge/patterns/buyer-side-gap-vs-vendor-pmo.md
        ↓ connect
standards/deliverable-archetypes.md Archetype J
knowledge/patterns/project-management-policy-layer.md
frameworks/change-management.md
frameworks/top-down-thinking.md
core/author-voice.md
playbooks/stakeholder-activation-playbook.md (pointer)
playbooks/cross-project-program-management.md (pointer)
        ↓ record
knowledge/migrations/coaching-20260828-change-effort-buyer-gap-2026-08.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Customer Status Report / Transformation PMO / Change Management
```

---

### V. Claude Foundations distillation and logical document unity (2026-09)

```text
Local CCAO-F post-exam notes + policy-discussion deck — not archived
        ↓ generalize (no credential, score, client names, schedules, architecture)
adapters/claude/CLAUDE.md
knowledge/lessons/ai-output-evaluation-terms.md
knowledge/patterns/logical-vs-physical-document-unity.md
        ↓ connect
core/ai-collaboration.md
standards/document-management-standard.md
knowledge/patterns/organizational-memory.md
knowledge/patterns/connected-organizational-memory.md
playbooks/ai-poc-quality-review.md
playbooks/rag-structure-diagnosis.md
playbooks/responsible-ai-assessment.md
        ↓ record
knowledge/migrations/claude-foundations-and-logical-unity-2026-09.md
        ↓ task routing
CONTEXT_ROUTING.md  →  AI PoC, Responsible AI, AI Adoption, Investigation / Requirements
```

---

## Level 4 — CONTEXT_ROUTING Task Map (summary)

Full detail in `CONTEXT_ROUTING.md`. High-traffic routes:

| Task | Primary loads |
|------|----------------|
| Proposal review | `standards/consulting-review.md`, `deliverable-archetypes.md`, `writing.md` |
| Customer weekly/monthly status | `deliverable-archetypes.md` Archetype J, `author-voice.md`, `project-management-policy-layer.md`, `support-effort-classification.md`, `change-agent-vs-communication-plan.md` / `unowned-work-in-effort-analysis.md` / `buyer-side-gap-vs-vendor-pmo.md` as needed, cadence / cross-project playbooks |
| IT strategy | `frameworks/it-strategy-foundations.md`, `standards/it-strategy-engagement-guide.md`, `playbooks/strategy-scn.md` (if SCN → projectization) |
| Strategy engagement / SCN | `consulting-strategy-process.md`, `strategy-engagement-guide.md`, `strategic-capability-network.md`, `scn-creation-guide.md`, `playbooks/strategy-scn.md` (sequence / Gate 1) |
| PMO / transformation | `frameworks/transformation-pmo.md`, `playbooks/pmo-function-standup.md`, `playbooks/program-governance-cadence.md`, `playbooks/strategy-scn.md` (upstream Gate 1), `playbooks/cross-project-program-management.md`, `playbooks/operations-transition-playbook.md` (Gate 3–5), `playbooks/stakeholder-activation-playbook.md` (if a specific person must act), `knowledge/patterns/related-project-external-coordination-radar.md` (if adjacent/external radar), `knowledge/patterns/pgmo-presence-via-client-stance.md` (if presence lost to trusted incumbent), `knowledge/patterns/buyer-side-gap-vs-vendor-pmo.md` (if vendor PMO is treated as buyer-side gap cover), `knowledge/patterns/transformation-practice-case-pack.md` (if internal practice packaging), `standards/pmo-operating-guide.md`, `knowledge/patterns/project-management-policy-layer.md` (if project-layer policy TOC), Archetype J if customer status, `frameworks/change-management.md` |
| DX grand design | `frameworks/dx-grand-design.md`, change / roadmap as needed |
| New venture assessment | `frameworks/new-venture-three-track-assessment.md` |
| B2B sales workflow | `knowledge/patterns/sales-capacity-via-center-functions.md` |
| Change management | `frameworks/change-management.md`, `all-at-once-vs-stepwise-change.md`, `change-agent-vs-communication-plan.md` (agent hunt ≠ communication plan), `pmo-operating-guide.md` §CM, `playbooks/stakeholder-activation-playbook.md` (person-level), `playbooks/operations-transition-playbook.md` Chapter 7 (ops adoption) |
| AI CoE / PgMO / Change | `knowledge/patterns/ai-coe-vs-pgmo-vs-change.md`, `ai-management-office.md`, `transformation-pmo.md`, `change-management.md` |
| AI adoption / DX roadmap | `frameworks/ai-adoption-roadmap.md`, `playbooks/ai-utilization-roadmap.md`, `playbooks/ai-work-before-after.md`, `logical-vs-physical-document-unity.md` if document unification is the AI enabler |
| AI PoC quality (buyer) | `playbooks/ai-poc-quality-review.md`, `rag-structure-diagnosis.md`, `buyer-owns-ai-poc-ground-truth.md`, `ai-output-evaluation-terms.md` if scoring an answer, `logical-vs-physical-document-unity.md` if corpus / store strategy is open |
| Offering review | `playbooks/offering-review.md`, `change-management.md`, `transformation-pmo.md` |
| Responsible AI assessment | `playbooks/responsible-ai-assessment.md`, `human-oversight.md`, `decision-ownership.md`, `ai-output-evaluation-terms.md` if classifying output failures |
| Energy / utilities | `domains/energy-utilities.md`, `operational-reality.md`, `requirements-artifact-review.md` (if requirements) |
| Public sector / defense IT | `domains/public-defense.md`, `public-it-procurement-support.md` (if buyer), `buyer-vs-seller-in-public-procurement.md`, shared-operator pattern + multi-lot construction PMO playbook if concurrent lots, `related-project-external-coordination-radar.md` if adjacent/external coordination |
| Private IT RFP / vendor selection | `frameworks/private-it-rfp.md`, `playbooks/private-it-rfp-vendor-selection.md`, `vendor-proposal-evaluation.md`, calibration / re-proposal patterns |
| Development standards / build / FIS audit mapping | `development-standards-framework.md`, related build standards, `fis-system-audit-as-assurance.md` when audit guidance or tech/ops/facility criteria apply, `project-management-policy-layer.md` when vendor PM-policy chapter applies |
| Application outsourcing / AMS | `application-outsourcing-solution-planning.md`, `ams-services-pyramid.md`, `service-transition-approach.md`, `ams-solution-plan-checklist.md`, `playbooks/operations-transition-playbook.md` (if Transition Manager coaching) |
| Infrastructure outsourcing / ITO | `infrastructure-outsourcing-solution-planning.md`, `transition-vs-transformation-vs-realization.md`, `playbooks/operations-transition-playbook.md` (if take-on coaching) |
| Systems integration / SI proposal | `systems-integration-solution-planning.md`, `estimate-target-commitment.md` |
| Delivery leadership | `delivery-leadership.md`, `transformation-pmo.md`, `change-management.md`, `playbooks/operations-transition-playbook.md` (if service introduction / take-on) |
| Azure / private API / sandbox cost | `technology/azure-enterprise.md`, connectivity and cost playbooks, related `decisions/` |
| LinkedIn / Note writing | `standards/writing.md` (§De-AI Writing Pass), series `source/`, related `patterns/` and `frameworks/` |
| Knowledge migration | `AI_OPERATING_MANUAL.md`, source asset, migration workflow |
| Repository maintenance | `ARCHITECTURE.md`, `master-index.md` (this file) |

---

## Maintenance — Update on Every Knowledge Expansion

When adding or migrating knowledge, update **in the same change set**:

| Change type | Update |
|-------------|--------|
| New file in `core/`, `standards/`, `frameworks/`, `playbooks/`, `technology/`, `knowledge/patterns|lessons|decisions` | This file — Level 3 tree and counts |
| New LinkedIn / Note source folder | `linkedin-series-index.md` + this file if structure changes |
| Legacy PDF extraction | `legacy-source-index.md` + this file Level 4 example if new Program Line |
| New migration | `knowledge/migrations/*.md` + migration checklist items below |
| New task route or load list | `CONTEXT_ROUTING.md` |
| Directory responsibility change | `ARCHITECTURE.md` §6 |
| Meaningful release | `CHANGELOG.md` (when present) |

**Migration checklist extension** (after cross-references):

1. Update domain index (`linkedin-series-index.md` or `legacy-source-index.md`) if applicable  
2. Update **this file** (`master-index.md`) — assets, counts, Level 4 flows  
3. Update `CONTEXT_ROUTING.md` if new assets should load for a task type  
4. Update `ARCHITECTURE.md` §6 only if layer responsibilities change  

Set **Last updated** at top of this file when edited.

---

## Related Documents

| Document | Role |
|----------|------|
| `ARCHITECTURE.md` | 8-layer design, directory responsibilities |
| `AI_OPERATING_MANUAL.md` | How AI executes and migrates knowledge |
| `CONTEXT_ROUTING.md` | Task → minimum context (operational loading) |
| `adapters/cursor/CURSOR.md` | Cursor-specific migration and search behavior |
