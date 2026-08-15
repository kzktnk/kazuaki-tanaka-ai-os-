# Kazuaki Tanaka AI OS

## Architecture

**Version:** v1.0 Navigation  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Repository-wide architectural blueprint

---

## 1. Purpose

This document defines the architecture of the Kazuaki Tanaka AI OS.

The AI OS is a model-independent knowledge and judgment system designed to preserve and reuse:

- professional identity
- principles and values
- reasoning and decision criteria
- quality standards
- domain knowledge
- frameworks
- execution playbooks
- lessons, decisions, and reusable patterns
- model-specific instructions

The repository is not intended to be a collection of unrelated notes.

It is intended to become a coherent operating system that enables different AI tools to work with consistent context, judgment, and quality expectations.

---

## 2. Architectural Objective

The architecture must enable the AI OS to remain useful even when:

- the preferred AI model changes
- the preferred vendor changes
- tools are repriced, retired, or replaced
- individual projects end
- knowledge grows across multiple domains
- implementation environments change

The architecture therefore separates enduring knowledge from temporary implementations.

The central rule is:

> Model-independent knowledge is the source of truth.  
> Model-specific files are adapters, not independent knowledge bases.

---

## 3. Design Principles

### 3.1 Judgment before content

The repository should preserve not only what is known, but also:

- why a conclusion was reached
- which criteria were used
- which trade-offs were considered
- what conditions would change the decision

### 3.2 Reusable assets before one-time outputs

Important work should be converted into reusable assets such as:

- standards
- frameworks
- templates
- playbooks
- decision records
- lessons learned
- patterns

### 3.3 Separation of concerns

Each directory must have a clear responsibility.

The same knowledge should not be copied into multiple locations unless there is a deliberate derived form.

### 3.4 Progressive disclosure

AI systems should load only the context required for the task.

They should begin with the core layer, then load relevant standards, domains, frameworks, and project context.

### 3.5 Generalize before preserving

Client-specific experience should be translated into reusable principles before being stored in the AI OS.

### 3.6 Human accountability

The AI OS supports judgment and execution.

It does not replace professional accountability.

### 3.7 Living architecture

The repository may evolve, but structural changes should be intentional, documented, and versioned.

---

## 4. Logical Architecture

The AI OS consists of eight logical layers.

```text
┌─────────────────────────────────────────────┐
│  8. Model and Tool Adapters                 │
│     Claude, ChatGPT, Cursor, Copilot, etc.  │
├─────────────────────────────────────────────┤
│  7. Project Context                         │
│     Objectives, constraints, local rules    │
├─────────────────────────────────────────────┤
│  6. Prompts and Templates                   │
│     Reusable interaction and output forms   │
├─────────────────────────────────────────────┤
│  5. Knowledge Assets                        │
│     Lessons, decisions, patterns            │
├─────────────────────────────────────────────┤
│  4. Playbooks                               │
│     How work is executed                    │
├─────────────────────────────────────────────┤
│  3. Frameworks and Domain Knowledge         │
│     How issues are structured and understood│
├─────────────────────────────────────────────┤
│  2. Standards                               │
│     What good looks like                    │
├─────────────────────────────────────────────┤
│  1. Core                                    │
│     Identity, principles, values, reasoning │
└─────────────────────────────────────────────┘
```

The lower layers are more stable and broadly applicable.

The upper layers are more task-specific and implementation-specific.

---

## 5. Repository Structure

```text
kazuaki-tanaka-ai-os/
│
├── README.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── DEVELOPMENT.md
├── SECURITY.md
├── .gitignore
│
├── core/
├── standards/
├── domains/
├── technology/
├── frameworks/
├── playbooks/
├── knowledge/
│   ├── index/          ← master-index, domain indexes
│   ├── source/         ← preserved originals (not default load)
│   ├── patterns/
│   ├── lessons/
│   ├── decisions/
│   └── migrations/
├── templates/
├── prompts/
├── projects/
├── adapters/
└── archive/
```

Not all directories need to be fully populated during v0.9.

The architecture defines the intended structure; implementation may proceed incrementally.

---

## 6. Layer Responsibilities

## 6.1 `core/` — Kernel

### Purpose

Defines the enduring identity and judgment system of the AI OS.

### Typical contents

- `principles.md`
- `identity.md`
- `values.md`
- `reasoning.md`
- `decision-making.md`
- `communication.md`
- `learning.md`
- `ai-collaboration.md`

### Contains

- professional identity
- values and priorities
- reasoning patterns
- decision rules
- collaboration expectations
- enduring behavioral principles

### Does not contain

- client-specific facts
- temporary project details
- tool-specific instructions
- detailed domain reference material
- one-time prompts

### Stability

High. Changes should be infrequent and deliberate.

---

## 6.2 `standards/` — Quality Criteria

### Purpose

Defines what good work looks like.

Standards should be written as observable or checkable criteria rather than vague adjectives.

### Typical contents

- consulting review standard
- proposal standard
- executive communication standard
- presentation standard
- research standard
- architecture review standard
- writing standard
- technical delivery standard

### Contains

- quality criteria
- review checklists
- minimum acceptance conditions
- required elements of deliverables
- common failure conditions

### Does not contain

- detailed execution procedures
- project-specific requirements
- general domain knowledge
- model-specific behavior

### Key distinction

- A **standard** defines what good looks like.
- A **playbook** defines how to produce it.

---

## 6.3 `domains/` — Reusable Domain Knowledge

### Purpose

Stores model-independent knowledge about industries, functions, and professional disciplines.

### Typical domains

- enterprise AI
- AI governance and governability
- energy and utilities
- public sector and defense
- program management
- change management
- enterprise transformation

### Contains

- domain concepts
- operating characteristics
- recurring industry issues
- stakeholder structures
- regulatory and governance considerations
- generalized insights from experience

### Does not contain

- confidential client information
- raw project notes
- credentials or private system information
- product-specific technical procedures

### Rule

Project experience must be generalized before being stored here.

---

## 6.4 `technology/` — Technical Knowledge and Principles

### Purpose

Stores reusable technical knowledge, architecture principles, and implementation guidance.

### Typical contents

- Azure
- Azure OpenAI
- Azure AI Foundry
- Azure AI Search
- API Management
- Power Platform
- Python
- secure enterprise integration
- networking and identity concepts

### Contains

- architecture principles
- design patterns
- implementation considerations
- security and operational concerns
- trade-offs
- reusable troubleshooting insights

### Does not contain

- secrets
- access tokens
- internal URLs
- client-specific resource names
- unapproved production configurations

### Relationship with `domains/`

`domains/` explains the business and operational context.

`technology/` explains the technical means and constraints.

---

## 6.5 `frameworks/` — Thinking Structures

### Purpose

Stores reusable structures for analyzing and designing solutions.

### Typical contents

- operating model
- capability model
- AI governability
- transformation roadmap
- program governance
- architecture review
- risk assessment

### Each framework should define

- purpose
- when to use
- inputs
- structure
- steps
- outputs
- limitations
- risks
- examples
- related standards and playbooks

### Key distinction

A framework helps structure a problem.

It does not necessarily prescribe the full execution sequence.

---

## 6.6 `playbooks/` — Execution Procedures

### Purpose

Defines repeatable procedures for performing work.

### Typical contents

- proposal review
- steering committee review
- executive message creation
- client interview
- architecture review
- LinkedIn post creation
- lessons learned extraction

### Each playbook should define

- trigger
- objective
- prerequisites
- required inputs
- sequence of actions
- decision points
- quality checks
- outputs
- escalation conditions

### Key distinction

- Framework: how to structure the problem.
- Playbook: how to execute the work.
- Standard: how to judge the output.

---

## 6.7 `knowledge/` — Accumulated Intellectual Capital

### Purpose

Stores knowledge extracted from experience, plus preserved sources and navigation indexes.

The knowledge layer has two roles:

1. **Distilled assets** (`patterns/`, `lessons/`, `decisions/`) — loaded during relevant tasks via `CONTEXT_ROUTING.md`
2. **Preserved sources and indexes** (`source/`, `index/`, `migrations/`) — inventory, audit trail, and migration; not loaded wholesale during normal execution

```text
knowledge/
├── index/
│   ├── master-index.md           ← 3–4 level map; update on every expansion
│   ├── linkedin-series-index.md
│   └── legacy-source-index.md
├── source/
│   └── linkedin/                 ← en.md, ja.md, metadata.md per article
├── patterns/
├── lessons/
├── decisions/
├── migrations/
└── glossary.md                   ← optional; not yet populated
```

**Navigation entry:** For an up-to-date expandable map, read `knowledge/index/master-index.md`.

### `knowledge/index/`

Indexes record where assets live and how layers connect.

- `master-index.md` — repository-wide 3–4 level map and maintenance rules
- Domain indexes — e.g. LinkedIn series, legacy PDF extraction map

Indexes are for orientation and maintenance. They are not substitutes for `CONTEXT_ROUTING.md`.

### `knowledge/source/`

Preserves authoritative originals (e.g. LinkedIn posts, archived articles).

Preferred structure:

```text
knowledge/source/linkedin/014/
├── en.md
├── ja.md
├── metadata.md
└── assets/
```

Sources support migration, writing continuity, and audit. They should **not** be loaded in full for unrelated tasks.

### `knowledge/migrations/`

Records what was extracted, created, or updated during a knowledge migration.

Each migration report should list source, new files, updated files, and primary contribution.

### `knowledge/lessons/`

Captures what was learned from a meaningful event or result.

A lesson should include:

- context
- observation
- interpretation
- reusable lesson
- applicability
- limitations

### `knowledge/decisions/`

Captures important decisions and their rationale.

A decision record should include:

- decision
- date
- context
- options considered
- criteria
- rationale
- consequences
- review trigger

### `knowledge/patterns/`

Captures recurring observations across multiple situations.

A pattern should include:

- pattern name
- signals
- underlying mechanism
- implications
- response
- exceptions

### Rules

- The knowledge layer should preserve distilled insight, not unprocessed meeting notes.
- Promote experience → pattern → framework → standard only when reusable and validated.
- On every knowledge expansion, update `knowledge/index/master-index.md` and relevant domain indexes in the same change set.

---

## 6.8 `templates/` — Reusable Structures

### Purpose

Provides reusable document and record structures.

### Typical contents

- lesson learned template
- decision record template
- framework template
- project context template
- deliverable review template
- prompt template

Templates define form, not substantive knowledge.

---

## 6.9 `prompts/` — Reusable AI Instructions

### Purpose

Stores reusable prompts for recurring tasks.

### Suggested categories

```text
prompts/
├── consulting/
├── writing/
├── research/
├── architecture/
└── knowledge-extraction/
```

### Contains

- task prompts
- review prompts
- extraction prompts
- structured interaction patterns

### Does not contain

- core principles duplicated from `core/`
- full domain knowledge duplicated from `domains/`
- model-specific syntax unless clearly separated

Prompts should reference source-of-truth files wherever practical.

---

## 6.10 `projects/` — Project Context

### Purpose

Provides a standard structure for temporary or project-specific context.

```text
projects/
├── README.md
└── _template/
    ├── context.md
    ├── objectives.md
    ├── constraints.md
    ├── decisions.md
    ├── lessons.md
    └── local-instructions.md
```

### Architectural rule

The AI OS repository should not become the primary storage location for confidential project materials.

Where appropriate, each project should have a separate private repository that references the AI OS.

### Preferred pattern

```text
AI OS repository
    shared principles, standards, frameworks, and knowledge

Project repository
    project-specific context, files, decisions, and local rules
```

---

## 6.11 `adapters/` — Model and Tool Interfaces

### Purpose

Translates the model-independent AI OS into instructions usable by specific tools.

### Suggested structure

```text
adapters/
├── claude/
│   ├── CLAUDE.md
│   └── skills/
├── chatgpt/
│   └── CHATGPT_INSTRUCTIONS.md
├── cursor/
│   └── README.md
├── gemini/
│   └── GEMINI.md
└── github-copilot/
    └── copilot-instructions.md
```

### Contains

- tool-specific file names
- tool-specific loading instructions
- tool-specific constraints
- references to source-of-truth files
- tool-specific automation or skill definitions

### Does not contain

- unique independent domain knowledge
- unique principles not represented in the core
- duplicated copies of the entire AI OS

### Rule

Adapters may summarize, reference, or operationalize the AI OS.

They must not become separate knowledge silos.

---

## 6.12 `archive/` — Retired Assets

### Purpose

Stores deprecated, superseded, or historically useful assets.

### Rule

Archive is not a dumping ground.

Every archived item should indicate:

- why it was archived
- what replaced it
- whether it may still be referenced

---

## 7. Source-of-Truth Rules

The following hierarchy applies when content conflicts.

1. `core/`
2. `standards/`
3. `frameworks/`
4. `domains/` and `technology/`
5. `playbooks/`
6. `knowledge/`
7. `projects/`
8. `prompts/`
9. `adapters/`

This hierarchy does not mean lower layers are less valuable.

It means they must not override more foundational layers without an explicit documented exception.

---

## 8. Context Loading Model

AI systems should not load the entire repository for every task.

Expanded knowledge is **stored** in the repository but **selected** at runtime. `knowledge/source/` and `knowledge/migrations/` are normally excluded from task context unless the task is migration, writing continuity, or repository maintenance.

Use:

- `CONTEXT_ROUTING.md` — which files to load per task type
- `knowledge/index/master-index.md` — where assets live (orientation, not default load)

The recommended loading sequence is:

### Step 1 — Always load the minimum core

- `core/principles.md`
- `core/identity.md`
- `core/values.md`
- `core/reasoning.md`

### Step 2 — Load task-specific standards

Examples:

- proposal review → consulting and presentation standards
- LinkedIn post → writing and external communication standards
- architecture review → technical and architecture standards

### Step 3 — Load relevant domain and technology knowledge

Examples:

- utility operating model → energy and utilities domain
- AI governance → enterprise AI and governability domain
- Azure network design → relevant technology files

### Step 4 — Load frameworks and playbooks

Load only those relevant to the task.

### Step 5 — Load project context

Use project-specific files after shared principles and standards.

### Step 6 — Apply adapter behavior

The adapter controls how the selected model or tool consumes and executes the context.

---

## 9. Knowledge Flow

Knowledge should move through the system as follows:

```text
Experience
    ↓
Raw observation
    ↓
Reflection
    ↓
Lesson or decision
    ↓
Recurring pattern
    ↓
Framework, standard, or playbook
    ↓
Adapter or prompt
    ↓
Improved future execution
```

Not every experience needs to reach every layer.

Promotion to a more enduring layer should occur only when the knowledge is reusable and sufficiently validated.

---

## 10. Confidentiality Architecture

The AI OS must not contain:

- confidential client documents
- client-identifying facts where unnecessary
- credentials
- API keys
- access tokens
- internal URLs
- non-public security configurations
- personal sensitive information
- proprietary content without authorization

### Generalization rule

Before storing project-derived knowledge:

1. remove identifying details
2. remove credentials and internal references
3. separate facts from interpretation
4. extract the reusable principle
5. state limitations and context
6. store only the generalized asset

---

## 11. File Design Standards

Every substantive file should include, where relevant:

- title
- purpose
- scope
- intended use
- content
- limitations
- related assets
- version or status

File names should use lowercase English and hyphens.

Examples:

```text
ai-governability.md
consulting-review.md
decision-record-template.md
lessons-learned-extraction.md
```

The body may be written in Japanese, English, or both.

For nuanced thinking, Japanese is acceptable as the primary language.

---

## 12. Change Management

Architectural changes should be reflected in:

- `ARCHITECTURE.md`
- `README.md`, when user-facing navigation changes
- `CHANGELOG.md`
- relevant directory README files

### Minor change

Examples:

- adding a new file
- adding a subcategory
- refining guidance

### Major change

Examples:

- changing directory responsibilities
- changing the source-of-truth model
- merging or splitting major layers
- changing confidentiality boundaries
- changing adapter architecture

Major changes should include an explicit rationale.

---

## 13. Version Roadmap

## v0.9 — Bootstrap

Objective:

- establish repository structure
- define core identity and principles
- define architectural boundaries
- begin basic standards and adapters

Success condition:

The repository can be used manually and remains understandable.

## v1.0 — Operational Foundation

Objective:

- complete the core layer
- establish primary consulting and writing standards
- define high-value frameworks and playbooks
- implement initial Claude, ChatGPT, and Cursor adapters
- establish decision and lesson capture

Success condition:

Different AI tools can produce meaningfully consistent work using the same source of truth.

## v1.x — Knowledge Compounding

Objective:

- expand domain knowledge
- accumulate lessons and patterns
- improve templates and prompts
- introduce regular review cycles

Success condition:

Each project measurably improves the AI OS.

## v2.0 — Executable AI OS

Objective:

- dynamic context selection
- automated adapter generation
- skill and agent orchestration
- automated lesson extraction
- repository consistency checks

Success condition:

The AI OS is not only read by AI systems; it actively guides and automates work.

## v3.0 — Personal Knowledge and Agent Platform

Potential objective:

- structured knowledge graph
- multiple specialist agents
- traceable decision support
- project-specific context loading
- long-term intellectual capital management

This phase remains exploratory and must not compromise security, confidentiality, or human accountability.

---

## 14. Architectural Decision Tests

Before adding a new directory or major file, ask:

- Does this content already have a natural home?
- Is this enduring knowledge or temporary context?
- Is it a standard, framework, playbook, lesson, decision, template, prompt, or adapter?
- Would duplication create inconsistency?
- Is the content sufficiently generalized?
- Does it preserve judgment, not only output?
- Can another AI or person understand how to use it?
- Does it respect confidentiality boundaries?

If the answers are unclear, do not add a new structural category yet.

---

## 15. Current Implementation Status

At v0.9 Bootstrap, the repository has begun implementation of:

- `core/`
- `standards/`
- `domains/`
- `technology/`
- `knowledge/`
- `projects/`
- `adapters/`

The following areas may still require creation or further implementation:

- `frameworks/`
- `playbooks/`
- `templates/`
- `prompts/`
- `archive/`
- root governance files
- model-specific adapter files

The documented architecture is the target state for the Bootstrap phase.

Implementation may proceed incrementally without creating empty structure that has no immediate use.

---

## 16. Guiding Principle

> Capture judgment, not just knowledge.

The architecture is successful when it helps future humans and AI systems understand:

- what matters
- how to think
- how to decide
- what good looks like
- how to execute
- what was learned
- how knowledge should be reused

That is the purpose of the Kazuaki Tanaka AI OS.
