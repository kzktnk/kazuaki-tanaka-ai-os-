# SAP Implementation Phase Model

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** ERP package implementation methodology (ASAP-derived, Phase 0–6 end-to-end model), generalized and anonymized. Original vendor overview PDF remains local; not committed.

---

## Purpose

Provide a **reusable phase and activity-group model** for large SAP (or similar ERP) implementation programs — from pre-project evaluation through sustain — without proprietary task catalogs, work-product IDs, or client-specific templates.

Use when:

- Structuring a program roadmap or SteerComm narrative for ERP build
- Mapping investigation/requirements work to downstream build phases
- Aligning test strategy, go-live, and benefit realization across vendors and client teams
- Tailoring a standard methodology when **Phase 0 assumptions do not match** the actual deal (e.g. strategy already fixed)

---

## Lineage (Generalized)

| Element | Description |
|---------|-------------|
| **Base** | SAP Accelerated SAP (ASAP) lifecycle |
| **Extensions** | **Phase 0 Evaluation** (pre-project) and **Phase 6 Sustain** (post go-live) |
| **Scope** | End-to-end: evaluation → preparation → blueprint → realization → cutover → hypercare → sustain |
| **Regional variants** | Country-specific tailoring of the global model is common; **register principles, not local WP catalogs** |

Related product lines (Implementation, Upgrade, Global, BW, etc.) share the same phase logic; variant-specific cutovers are out of scope for this document.

---

## Cross-Cutting Workstreams

All phases are governed in parallel by five workstreams (names may vary by program):

| Workstream | Role |
|------------|------|
| **Program management** | Schedule, scope, risk, steering, PMO |
| **Business** | Process, org, change, training |
| **Organization** | Roles, RACI, org design |
| **Application architecture** | Solution footprint, integration, technical direction |
| **Operations** | Run-state, support model, handover to BAU |

---

## Phase 0–6 Overview

| Phase | Name (EN / JP) | Primary outcomes |
|-------|----------------|------------------|
| **P0** | Evaluation / 構想 | Strategy alignment, scope, business case, **benefit realization plan**, proposal |
| **P1** | Project preparation / プロジェクト準備 | Team, environment, procedures, detailed plan, kickoff |
| **P2** | Business blueprint / ビジネス設計 | To-Be process, Fit/Gap, org change reqs, training approach, value-realization execution plan |
| **P3** | Realization / 実現化 | Build, test, cutover prep (see Activity Groups below) |
| **P4** | Final preparation / 本番移行 | Production cutover, EUT, **service-in approval** |
| **P5** | Go-live and support / 本稼働とサポート | Stabilization, benefit metrics timing, handover to sustain, project close |
| **P6** | Sustain / 維持 | Performance tuning, post-implementation review, archive, continuous improvement |

### Phase summaries (client collaboration emphasis)

**P0 — Evaluation**  
Understand strategy, goals, As-Is pain, improvement opportunities; define scope; quantify benefits; propose approach. Client provides interviews and current-state data.

**P1 — Project preparation**  
Establish governance, environments, standards; refine WBS/schedule; kick off. Client embeds owners early — not observer-only.

**P2 — Business blueprint**  
Workshops for To-Be flows; Fit/Gap vs package; finalize build scope; org-change and training direction; **value realization** execution plan. Client confirms and approves target processes.

**P3 — Realization**  
Prototype → design/develop → integrate test → UAT/rehearsal (Activity Groups P3-A–D). Client reviews add-on design/tests and participates in UAT.

**P4 — Final preparation**  
System operation test (incl. load/DR where applicable), production migration, end-user training, service-in sign-off.

**P5 — Go-live and support**  
Hypercare; define benefit measurement; transition to sustain; formal project closure.

**P6 — Sustain**  
Optimize performance; post-go-live assessment; archiving; ongoing improvement with client feedback.

---

## Phase 2 Activity Groups

| Group | Focus |
|-------|--------|
| **P2-A** | Major (stream) business design |
| **P2-B** | End-to-end business design across streams |

Typical contents: To-Be process models, Fit/Gap, prototype environment, org requirements, training plan, value-realization plan update.

---

## Phase 3 Activity Groups

| Group | Name | Focus |
|-------|------|--------|
| **P3-A** | Prototype | Confirm standard/custom specs; master data detail; scenarios, workshops, baseline vs final prototype |
| **P3-B** | External design → development | Specs, add-on dev, unit test, QA promotion, interfaces, migration identification/plan, **CTP** (comprehensive test plan from UT onward) |
| **P3-C** | Integration test | ITa (in-module), ITb (cross-module / interfaces), migration test prep, service-in criteria |
| **P3-D** | UAT & production rehearsal | UAT, rehearsal (object promotion & migration checklist), SOT prep, final ops docs, EUT prep |

---

## Test Taxonomy

Maps to build deliverables (see `standards/deliverable-archetypes.md` Archetype G).

| Test | Intent | Typical phase |
|------|--------|---------------|
| **Unit test (UT)** | Add-ons / custom objects meet spec | P3-B |
| **Integration test a (ITa)** | In-module scenario connectivity | P3-C |
| **Integration test b (ITb)** | Cross-module and interface scenarios | P3-C |
| **Migration test** | Tools, data, procedures per migration plan | P3-C |
| **UAT** | Client validates To-Be process on new system | P3-D |
| **Production rehearsal** | Cutover steps, migration checklists, promotion accuracy | P3-D |
| **System operation test (SOT)** | Load, disaster recovery, whole-system ops tests; may overlap ITb; final confirmation in P4 | P3-D / P4 |

**CTP:** Single umbrella plan for all post-UT testing — purpose, owners, schedule — feeding detailed test plans.

---

## WBS and Work Products (Concept Only)

### WBS hierarchy

```
Phase
  └── Activity (Group)
        └── Task
              └── Subtask
```

Each level has defined purpose and content; lower levels elaborate upper levels.

### Work product (WP)

- Output of a task — may be a formal deliverable or an **intermediate** artifact  
- Tasks specify create vs update of WPs  
- WPs carry: description, rationale, guidance, downstream update triggers  

**Do not commit to the repo:** vendor task IDs, WP numbering schemes, sample templates, or step-by-step proprietary procedures.

---

## Why Use a Phase Model (Generalized)

1. **Common language** — Shared gates, artifacts, and dependencies across client and integrator  
2. **Quality and efficiency** — Explicit entry/exit criteria per task  
3. **Look-ahead** — Downstream work visible from early phases  
4. **Three success levers** — Methodology discipline; skilled people; project/program management (not methodology alone)

---

## Tailoring Principle

**Phase 0 assumptions often differ from reality** (e.g. RFP already issued, strategy fixed, partial legacy assessment done). Apply the model by **mapping and adapting** phases — skip, merge, or front-load — rather than forcing a literal Phase 0 workshop sequence. Document tailoring in the program charter or PMO operating model.

---

## Mapping to Repository Assets

| This model | Repository asset |
|------------|-------------------|
| P0–P1 | `frameworks/consulting-strategy-process.md`, `standards/deliverable-archetypes.md` Archetype A |
| P2 Fit/Gap, blueprint | `frameworks/program-phases-investigation-to-requirements.md` Phase 400–420 |
| P3 build & test | `standards/development-standards-framework.md`, `standards/development-management-guide.md`, Archetype G |
| P4–P5 cutover & hypercare | `standards/operations-handover-guide.md`, `standards/operations-design-guide.md` |
| P5 benefit realization | `frameworks/transformation-pmo.md` (benefit traceability) |
| P6 sustain | `standards/release-management-guide.md` |
| Program governance | `standards/pmo-operating-guide.md`, `frameworks/transformation-pmo.md` |

`standards/development-standards-framework.md` covers **build/run standards**; this document covers **ERP program phase logic** upstream and downstream of that layer.

---

## Review Checklist

- [ ] Phase tailoring (especially P0/P1) is documented when the deal did not start at evaluation  
- [ ] P3 Activity Groups appear on the integrated schedule with clear entry/exit  
- [ ] Test types (ITa/ITb/UAT/rehearsal/SOT) are named consistently in plans and SteerComm decks  
- [ ] Benefit realization (P0 plan → P2 execution plan → P5 measurement) is threaded, not orphaned  
- [ ] No proprietary task/WP IDs or vendor sample filenames in client-facing repo copies  
- [ ] Handover from P5 to P6 (and to BAU ops) has a named owner and artifact list  

---

## Related Assets

| File | Relationship |
|------|--------------|
| `standards/development-standards-framework.md` | Build-phase standards catalog |
| `standards/deliverable-archetypes.md` | Proposal/report (A–F) + build (G) archetypes |
| `standards/development-management-guide.md` | Build management and review/test flow |
| `frameworks/consulting-strategy-process.md` | Strategy / business case before ERP program (P0–P1) |
| `frameworks/transformation-pmo.md` | P5 benefit realization and program governance |
| `frameworks/program-phases-investigation-to-requirements.md` | Public-sector style 100–500 phases (parallel track) |
| `knowledge/index/legacy-source-index.md` | Program Line I — local PDF index only |

---

## Confidentiality

Original methodology PDFs (vendor overview and internal training decks) stay **local**. This file contains **generalized phase logic only** — aligned with `core/identity.md` Confidentiality Boundary.
