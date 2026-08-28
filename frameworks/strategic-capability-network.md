# Strategic Capability Network (SCN)

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Source:** Legacy IBM consulting training materials (2003–2005), generalized and anonymized. Original PDFs remain local; not committed.

---

## Purpose

SCN is a strategy visualization and analysis method for mapping **how value is created** — from strategic intent through capabilities and enablers to measurable outcomes.

Use SCN when the task requires:

- Making the logic of a program or initiative explicit (why → what → how)
- Checking for gaps before execution planning
- Integrating multiple programs at an enterprise level
- Tracking outcomes through PDCA and prioritizing actions

Do **not** use SCN alone when the primary question is IT structural quality (usability, operability, detailed I/O). Use SCN for business–IT alignment; use application maps or assessments for IT-native issues.

---

## Definition

**SCN (Strategic Capability Network)** models a firm as a network of:

| Layer | Role | Description |
|-------|------|-------------|
| **Value (提供価値)** | Strategic positions / effects | Benefits delivered to stakeholders (shareholders, customers, employees). Often decomposed into 2–3 layers. |
| **Capability (ケーパビリティ)** | What the organization must be able to do | Expressed as “ability to ~” (e.g., ability to respond to customer needs quickly). Typically 2–3 layers. |
| **Enabler (イネーブラー)** | How capability is realized | Concrete means: **KOPT** — Knowledge, Organization, Process, Technology. |
| **KPI / indicators** | Measurement | **Outcome indicators** (effect targets) on Value; **monitor indicators** on Capability. |

Relationships:

- Value ← Capability (direct or indirect support)
- Capability ← Enabler (KOPT)
- Capabilities can support other capabilities (indirect path to Value)

---

## Four Uses of SCN

1. **Define logic** — Clarify causal links among program value, required capabilities, and initiatives (enablers).
2. **Gap check** — Verify missing initiatives before execution planning.
3. **Enterprise integration** — Cross-program SCN makes consolidation and resource allocation easier.
4. **PDCA tracking** — Use SCN as a backbone for outcome tracking and action decisions.

---

## Hierarchy: Strategy → Program → Project

```
Vision / Strategy
    └── Strategic objectives
            └── Program(s)          ← SCN unit for a transformation theme
                    └── Project(s)  ← Execution / initiative unit (enabler bundles)
```

- **Program** = investment / effect evaluation unit (e.g., sales reform, procurement reform).
- **Project** = execution unit (specific initiatives, systems, org changes).
- Multiple programs can share capabilities and enablers; enterprise SCN reveals overlap and synergies.

---

## KOPT (Enablers)

| Type | Examples |
|------|----------|
| **Knowledge** | Know-how, intellectual assets, skills, formalized expertise |
| **Organization** | Structure, roles, accountability, training |
| **Process** | Management and operational processes, rules |
| **Technology** | IT infrastructure, applications, components |

Enabler tips:

- Place **initiative names** (program/project bundles) at the top of the enabler layer to group lower enablers.
- For Technology, describe down to **component level** when system elements must be visible.
- Distinguish **master data** vs **transaction data** when defining data enablers.

---

## Capability Conventions

- Write as **“～できる能力”** (ability to ~).
- Prefer verbs from a consistent lexicon (Access, Analyze, Integrate, Monitor, Partner, etc.) when working in English or bilingual decks.
- **2–3 capability layers** is typical.
- **Merge** capabilities that would share the same KPI.
- **Split** when one capability has many downstream enabler paths, or when N:1 relationships from above indicate overload.

---

## Value Conventions

- Stakeholder categories: **shareholder, customer, employee** (extend as needed).
- Value should be **specific enough** that the jump to the next capability layer is small.
- Do not duplicate the same value in multiple places; merge or differentiate by recipient/content.
- Distinguish **values to pursue** vs **values deliberately not pursued** (Southwest Airlines pattern: low price vs premium services).

Value worksheet fields (when formalizing):

| Field | Content |
|-------|---------|
| Stakeholder | Who receives the value |
| Value proposition | What benefit is delivered |
| Outcome indicator | Quantified effect target |

---

## KPI Placement

| Level | Indicator type |
|-------|----------------|
| Value | Outcome indicators (effect targets, e.g., revenue, cost, satisfaction) |
| Capability | Monitor indicators (leading / operational, e.g., review rate, activity time) |

Important capabilities should have KPIs on the SCN. Mark KPIs visibly (e.g., red text) and emphasize critical capabilities (bold / thick links).

---

## As-Is → To-Be

As-Is capabilities and enablers **cannot** deliver To-Be value without strengthening or adding nodes.

```
As-Is Value ──gap──► To-Be Value
As-Is Capability ──strengthen/add──► To-Be Capability
As-Is Enabler ──strengthen/add──► To-Be Enabler
```

SCN supports **Findings**: structural gaps on the network (missing capability, weak enabler, broken causal link) become 3–5 executive-level findings, each with Fact → Issue → causal chain on the map.

---

## Relation to Other Repository Frameworks

| Framework | Relationship |
|-----------|--------------|
| `frameworks/capability-model.md` | SCN operationalizes capability layers (Strategic / Management / Operational / Supporting) in a **causal network**, not a flat list. |
| `frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md` | As-Is / Gap / To-Be on SCN nodes. |
| `frameworks/thinking-patterns/pattern-06-strategy-org-process-system.md` | SCN enablers map to Org / Process / System; Value / Capability sit above. |
| `frameworks/operating-model.md` | Operating model choices appear as Organization and Process enablers. |
| `frameworks/program-phases-investigation-to-requirements.md` | SCN fits Phase 200–300 (current state, gap, findings) and Phase 400 (approach alignment). |
| `frameworks/transformation-pmo.md` | SCN maps **what** to achieve; PMO governs **how** programs and projects deliver and integrate. |
| `core/author-voice.md` | Findings on SCN: Fact → Issue → Hypothesis → To-Be → Approach; avoid template tables. |

**Pattern 6 vs SCN:** Pattern 6 is a linear top-down stack. SCN is a **network** with direct/indirect links and cross-program visibility. Use both: Pattern 6 for narrative flow, SCN for diagnosis and integration.

---

## Limitations

- SCN shows **intent and alignment** of initiatives to value; it is not a substitute for detailed process design, data models, or application architecture.
- IT-specific defects (security, usability, ops) → annotate on SCN as callouts or map separately to application landscape.
- Do not over-specify enablers in early strategy phases; match depth to engagement scope (see `standards/scn-creation-guide.md`).

---

## Related Files

- `standards/scn-creation-guide.md` — Workshop, heuristics, notation, creation steps
- `playbooks/strategy-scn.md` — Strategy → SCN → KPI → Gate 1 projectization (execution / coaching)
- `frameworks/consulting-strategy-process.md` — Upstream strategy engagement before capability mapping
- `standards/strategy-engagement-guide.md` — Problem scoping and analysis planning
- `playbooks/cross-project-program-management.md` — Downstream Gate 2 / cross-project control
- `playbooks/operations-transition-playbook.md` — Downstream Gate 3–5 / ops transition
- `playbooks/stakeholder-activation-playbook.md` — Moving named actors (cross-cutting)
- `CONTEXT_ROUTING.md` — SCN / Findings Analysis route
- `knowledge/index/legacy-source-index.md` — Local source index (paths only)

---

## Maintenance

- Keep IBM/client names and engagement-specific examples out of this repo.
- When Tanaka’s SCN practice evolves (e.g., AI program mapping), update here first, then cross-link from lessons.
