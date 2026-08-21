# Migration Report — Cross-project program management (2026-08)

## Source (not stored in repo)

Revised local coaching materials for a subordinate PgMO role:

- `Downloads/cross-project-management-playbook.md`（truth for body; v1.5.1 as of 2026-08-21）
- `Downloads/Cross-Project-Management-Playbook.docx`（aligned on structure; Chapter 5.4 wording lagged md at adopt time）
- `Downloads/Cross-Project-Management-Playbook-Templates.xlsx`（referenced by Appendix; binary not re-checked this adopt — no nearby updated copy found）

Indexed anonymously as **multi-vendor cross-project PgMO coaching / 2026**. Originals not archived.

## Files adopted or updated

- `playbooks/cross-project-program-management.md` — revised to match the updated playbook body and coaching flow（latest: Chapter 5.4 vendor responsibility boundary detail, source rev v1.5.1）
- `knowledge/migrations/cross-project-program-management-2026-08.md` — refreshed to reflect the revised extraction scope
- `knowledge/index/legacy-source-index.md` — registration date / scope note for this revise

## Material changes in the revised source

| Area | Revised source now emphasizes |
|------|-------------------------------|
| Structure | Full chaptered playbook format with explicit use sequence and appendix linkage |
| Diagnostic coaching | Added **PgMO abnormal-signal 5 questions** to teach how to read the artifacts, not just fill them |
| Interface management | Added a concrete **IF design review 5-step procedure** |
| Consistency evidence | Added **Consistency Issue Log** as evidence behind the matrix |
| Control depth | Added **Forecast / Recovery Plan** and a stronger distinction between monitoring and control |
| Forward-looking control | Added **pre-read / early warning / premortem** guidance to make anticipation teachable |
| Governance practice | Added guidance for **vendor conflict handling** and **update cadence / PMIS scaling** |
| Scope / contract boundary | **Chapter 5.4 expanded** — structural causes of boundary drift, gray-zone examples, 5-step handling, PgMO-complete vs escalate criteria, delegated-authority definition of “PgMO完結”（v1.5 / v1.5.1） |
| Coaching sequence | Expanded practice section with reviewed answer patterns, not only session prompts |
| Templates | Workbook still **8 sheet classes** (Issue Log included); no template-class change detected this revise |

## Excluded (not registered)

- xlsx workbook binary itself
- cover metadata such as creation date / named reader profile
- author personal review checklist（「全体レビュー用メモ（Kazuaki記入欄）」）
- Word-only TOC field / font packaging notes
- sample rows that would register live program facts rather than reusable template classes
- vendor names, personal names, costs, exchange-rate figures, contract facts, or client-identifying details

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| PgMO scope | Manage **between** projects, not inside each project |
| 5 domains | Scope Boundary, Dependency, Interface, Consistency, Schedule |
| Diagnostic lens | Unconnected / undecided / inconsistent / no-lag / single-point-of-failure checks |
| Interface practice | Joint sender-receiver IF review with item-level checks and agreement record |
| Consistency evidence | Matrix = overview; Issue Log = evidence and detail |
| Control loop | Baseline → Current → Variance → Impact → Action, plus Forecast / Recovery Plan |
| Forward warning | Future Amber/Red question, no-penalty early warning, premortem |
| Weekly meeting | Cross-Project Control Cycle (not vendor status round-robin) |
| Vendor boundary | Contract vs operational Scope Boundary Matrix; gray zones; PgMO-complete vs Change Control / Steering |
| Coaching | 90min × 2 sessions, then monthly consistency review |
| Template classes | 8 workbook sheets represented only by class / field definitions |

## Overlap with existing assets

| Existing | Relationship |
|----------|-------------|
| `program-governance-cadence.md` | Complementary — **who meets where**; this playbook covers **what to manage between projects and how to control it** |
| `transformation-pmo.md` | Parent framework — program layer definition |
| `pmo-operating-guide.md` | Integration management domain; less artifact-specific coaching detail |
| `public-multi-lot-construction-pmo.md` | Different context (public multi-lot start-gates) |

## Suggested commit message

```text
update(playbooks): detail vendor responsibility boundary in cross-project PgMO playbook
```
