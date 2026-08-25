# Migration Report — Cross-project program management (2026-08)

## Source (not stored in repo)

Revised local coaching materials for a subordinate PgMO role:

- `Downloads/cross-project-management-playbook.md`（truth for body; **v1.8** as of 2026-08-25）
- `Downloads/Cross-Project-Management-Playbook.docx`（structure parity with md; Word-only TOC / font packaging / cover metadata ignored）
- `Downloads/Cross-Project-Management-Playbook-Templates.xlsx`（referenced by Appendix; binary not re-checked this adopt — no nearby updated copy found）

Indexed anonymously as **multi-vendor cross-project PgMO coaching / 2026**. Originals not archived. Docx binary not committed.

## Files adopted or updated

- `playbooks/cross-project-program-management.md` — revised to match v1.8 body（scope boundary note, 5-domain mental model, Steering Decision Request coaching）; repo Version **v0.5**; Archetype J pointer retained
- `knowledge/migrations/cross-project-program-management-2026-08.md` — refreshed to reflect v1.8 extraction scope
- `knowledge/index/legacy-source-index.md` — Program Line W registration note for this revise

## Material changes since prior adopt (v1.7 → v1.8)

| Area | What changed |
|------|----------------|
| Scope boundary (v1.8) | **射程の明示** — this playbook covers Cross-Project Integration & Control only; Benefits / Strategic Alignment / Business Case / Stakeholder-Change / Resource Prioritization / Program Lifecycle（Tranche）are out of scope |
| Chapter 1 title (v1.8) | Renamed to **Project Management と Cross-Project Program Management の違い** |
| Mental model (v1.8) | **Chapter 2.6** — one-page model for Scope Boundary / Dependency / Interface / Consistency / Schedule with one-line definitions |
| Steering ask (v1.8) | **Chapter 9 Session 2** step 7 — Detect → Analyze → Recover → Recommend → Ask Decision Request; sample + review checklist |
| Already present (kept) | Org chart / dual-role (1.4–1.5); RAG (8.2); Consistency rewrite (6.1/6.5); vendor boundary (5.4); IF review; premortem; Control Cycle; Archetype J header pointer |

## Excluded (not registered)

- xlsx workbook binary itself
- docx binary
- cover metadata such as creation date / named reader profile
- author personal review checklist（「全体レビュー用メモ（Kazuaki記入欄）」）
- Word-only TOC field / font packaging notes / revision-history dump in source md
- local YAML frontmatter（draft status / gap_fill / related list）— repo header retained
- sample rows that would register live program facts rather than reusable template classes
- vendor names, personal names, costs, exchange-rate figures, contract facts, or client-identifying details
- customer weekly/monthly narrative content（already in Archetype J / Program Line Z; not force-merged into this playbook body）

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| PgMO scope | Manage **between** projects, not inside each project |
| Playbook boundary | Cross-project integration & control only — not full program management |
| 5 domains | Scope Boundary, Dependency, Interface, Consistency, Schedule（mental model + one-liners） |
| Org stance | PgMO stands **beside** Vendor PMs; draw the real escalation map |
| Dual role | Dual PgMO/PMO is common but neutrality must be designed |
| Diagnostic lens | Unconnected / undecided / inconsistent / no-lag / single-point-of-failure checks |
| Interface practice | Joint sender-receiver IF review with item-level checks and agreement record |
| Consistency evidence | Matrix = overview; Issue Log = evidence; fill Issue Log first |
| RAG | Shared Green/Amber/Red criteria tied to Baseline / Variance / Recovery |
| Control loop | Baseline → Current → Variance → Impact → Action, plus Forecast / Recovery Plan |
| Forward warning | Future Amber/Red question, no-penalty early warning, premortem |
| Weekly meeting | Cross-Project Control Cycle (not vendor status round-robin) |
| Vendor boundary | Contract vs operational Scope Boundary Matrix; gray zones; PgMO-complete vs Change Control / Steering |
| Steering ask | Detect → Analyze → Recover → Recommend → Ask as one Decision Request |
| Coaching | 90min × 2 sessions, then monthly consistency review |
| Template classes | 8 workbook sheets represented only by class / field definitions |

## Overlap with existing assets

| Existing | Relationship |
|----------|-------------|
| `program-governance-cadence.md` | Complementary — **who meets where**; this playbook covers **what to manage between projects and how to control it** |
| `transformation-pmo.md` | Parent framework — program layer definition |
| `pmo-operating-guide.md` | Integration management domain; less artifact-specific coaching detail |
| `deliverable-archetypes.md` Archetype J | Customer-facing weekly/monthly **presentation**; this playbook is internal PJ間 control — header pointer only |
| `public-multi-lot-construction-pmo.md` | Different context (public multi-lot start-gates) |

## Suggested commit message

```text
update(playbooks): adopt cross-project PgMO playbook v1.8 coaching revisions
```
