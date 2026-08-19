# Knowledge Master Index

**Version:** v1.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Expandable 3–4 level map of the AI OS knowledge base  
**Last updated:** 2026-08-19

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
├── standards/                  ← 17 files (quality criteria)
├── frameworks/                 ← 23 files + thinking-patterns/
├── playbooks/                  ← 1 playbook (+ README)
├── knowledge/
│   ├── index/                  ← this file + domain indexes
│   ├── source/                 ← preserved originals (LinkedIn, etc.)
│   ├── patterns/               ← 13 distilled patterns
│   ├── lessons/                ← 5 lessons
│   ├── migrations/             ← 7 migration reports
│   └── decisions/              ← (reserved, empty)
├── templates/                  ← 1 template
├── prompts/                    ← README placeholder
├── projects/                   ← project template structure
├── adapters/cursor/            ← Cursor adapter
├── domains/                    ← (reserved, empty)
├── technology/                 ← (reserved, empty)
└── archive/                    ← README placeholder
```

**Domain indexes (Level 3 detail in separate files):**

| Index | Scope |
|-------|--------|
| [linkedin-series-index.md](./linkedin-series-index.md) | LinkedIn / Note sources 001–018, sp01–09, erf01–03 |
| [legacy-source-index.md](./legacy-source-index.md) | Local legacy PDFs → repo extraction map (Program Lines A–J) |

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

## Level 3 — Standards (17)

Grouped by domain for navigation:

```text
standards/
├── Consulting & strategy
│   ├── consulting-review.md
│   ├── strategy-engagement-guide.md
│   ├── it-strategy-engagement-guide.md
│   └── vendor-proposal-evaluation.md
├── Deliverables & documents
│   ├── deliverable-archetypes.md
│   ├── requirements-document-outline.md
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
    └── scn-creation-guide.md
```

---

## Level 3 — Frameworks (23 + thinking patterns)

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
│   └── decision-velocity.md
├── Transformation & operating model
│   ├── operating-model.md
│   ├── capability-model.md
│   ├── maturity-model.md
│   ├── transformation-roadmap.md
│   ├── transformation-pmo.md
│   └── program-phases-investigation-to-requirements.md
├── Application outsourcing / AMS
│   ├── application-outsourcing-solution-planning.md
│   ├── ams-services-pyramid.md
│   └── service-transition-approach.md
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
│       ├── 001–018/                  ← Operational AI main series
│       ├── sp01–sp09/                ← special posts
│       └── erf01–erf03/              ← Enterprise Redesign Framework
├── patterns/                         ← 12 files (see table below)
├── lessons/
│   ├── governance-messaging.md
│   ├── dual-roadmap-messaging.md
│   ├── pmo-professional-principles.md
│   ├── author-voice-archetypes-legacy.md
│   └── client-deliverable-voice-jera-2026-08.md
├── migrations/
│   ├── linkedin-bulk-001-015-sp-erf.md
│   ├── linkedin-013.md
│   ├── linkedin-014.md
│   ├── linkedin-016.md
│   ├── linkedin-017.md
│   ├── linkedin-018.md
│   ├── ai-dual-roadmap-2026-08.md
│   └── ao-sae-2026-08.md
└── decisions/                        ← reserved
```

### Patterns (13)

| Pattern | Primary themes |
|---------|----------------|
| `operational-governance.md` | Operational AI, governance as capability |
| `operational-reality.md` | OT / field reality vs DX narrative |
| `expertise-amplification.md` | AI amplifies experts |
| `organizational-memory.md` | Intelligence vs organizational memory; decision context |
| `operating-model-advantage.md` | Competitive advantage from operating model |
| `ai-resilience-shift.md` | Productivity → resilience |
| `decision-ownership.md` | Execution ≠ ownership |
| `decision-delegation.md` | Delegation boundaries |
| `verifiable-ownership.md` | Ownership must be provable |
| `risk-ownership.md` | Work delegation ≠ risk accountability |
| `ai-capability-vs-authority.md` | Capability ≠ authority |
| `authority-levels.md` | Graduated authority design |
| `jera-scn-ebitda-tree.md` | SCN / EBITDA tree (client voice lesson) |

---

## Level 3 — Playbooks, Templates, Adapters

```text
playbooks/
├── README.md
└── wbs-design.md

templates/
└── wbs-breakdown-sheet.md

prompts/
└── README.md

archive/
└── README.md

adapters/cursor/
└── CURSOR.md                         ← Cursor-specific behavior + migration rules
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
Local legacy (Program Line A, H, I)     ← legacy-source-index.md
        ↓ generalize
standards/development-standards-framework.md
standards/development-management-guide.md
standards/deliverable-archetypes.md
frameworks/sap-implementation-phase-model.md
        ↓ task routing
CONTEXT_ROUTING.md  →  Proposal Review, ERP, PMO sections
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

### F. Organizational memory (LinkedIn No.18)

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
        ↓ task routing
CONTEXT_ROUTING.md  →  AI Adoption / DX Roadmap
```

---

## Level 4 — CONTEXT_ROUTING Task Map (summary)

Full detail in `CONTEXT_ROUTING.md`. High-traffic routes:

| Task | Primary loads |
|------|----------------|
| Proposal review | `standards/consulting-review.md`, `deliverable-archetypes.md`, `writing.md` |
| IT strategy | `frameworks/it-strategy-foundations.md`, `standards/it-strategy-engagement-guide.md` |
| PMO / transformation | `frameworks/transformation-pmo.md`, `standards/pmo-operating-guide.md` |
| AI governance | `frameworks/ai-governability.md`, `decision-ownership.md`, `human-oversight.md`, related `patterns/` |
| AI adoption / DX roadmap | `frameworks/ai-adoption-roadmap.md`, `ai-role-maturity.md`, `organizational-memory.md`, `dual-roadmap-messaging.md` |
| Application outsourcing / AMS | `application-outsourcing-solution-planning.md`, `ams-services-pyramid.md`, `service-transition-approach.md`, `ams-solution-plan-checklist.md` |
| LinkedIn / Note writing | `standards/writing.md`, series `source/`, related `patterns/` and `frameworks/` |
| Knowledge migration | `AI_OPERATING_MANUAL.md`, source asset, migration workflow |
| Repository maintenance | `ARCHITECTURE.md`, `master-index.md` (this file) |

---

## Maintenance — Update on Every Knowledge Expansion

When adding or migrating knowledge, update **in the same change set**:

| Change type | Update |
|-------------|--------|
| New file in `core/`, `standards/`, `frameworks/`, `playbooks/`, `knowledge/patterns|lessons|decisions` | This file — Level 3 tree and counts |
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
