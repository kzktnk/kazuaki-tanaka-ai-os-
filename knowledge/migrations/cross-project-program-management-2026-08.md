# Migration Report — Cross-project program management (2026-08)

## Source (not stored in repo)

Revised local coaching materials for a subordinate PgMO role:

- `Downloads/cross-project-management-playbook.md`（truth for body; **v1.9** as of 2026-08-26）
- `Downloads/Cross-Project-Management-Playbook.docx`（structure parity with md; Word-only TOC / font packaging / cover metadata ignored）
- `Downloads/cross-project-management-playbook-selfstudy.md`（voice rewrite of main; method extracted only）
- `Downloads/Cross-Project-Management-Playbook-SelfStudy.docx`（parity with selfstudy md; binary ignored）
- `Downloads/Cross-Project-Management-Playbook-Templates.xlsx`（referenced by Appendix; binary not re-checked this adopt）

Indexed anonymously as **multi-vendor cross-project PgMO coaching / 2026**. Originals not archived. Docx / xlsx binaries not committed.

## Files adopted or updated

- `playbooks/cross-project-program-management.md` — Chapter **1.6** mid-engagement presence coaching; Self-study companion（method only）; repo Version **v0.6**; source revision **v1.9**; thin pointer to `knowledge/patterns/pgmo-presence-via-client-stance.md`
- `knowledge/migrations/cross-project-program-management-2026-08.md` — refreshed to v1.9 + SelfStudy disposition
- `knowledge/index/legacy-source-index.md` — Program Line W registration note
- `knowledge/patterns/pgmo-presence-via-client-stance.md` — Use-with pointer to Chapter 1.6（thin）

## Material changes since prior adopt (v1.8 → v1.9)

| Area | What changed |
|------|----------------|
| Mid-engagement presence (v1.9) | **Chapter 1.6** — mid-program PgMO join when a trusted incumbent already holds client trust; structural asymmetry; five coping moves (client-side stance, ally framing, field ally first, intersection tracking, avoid admin burial) |
| Review checklist (v1.9) | Chapter 1 review memos add ally framing + admin-burial checks |
| Self-study (new artifact) | Full SelfStudy md/docx = voice rewrite of main — **not** registered wholesale; method only under「Self-study companion」 |
| Already present (kept) | Scope boundary; 5-domain mental model; Steering Decision Request; org chart / dual-role; RAG; Consistency rewrite; vendor boundary; IF review; premortem; Control Cycle; Archetype J header pointer |

## Excluded (not registered)

- xlsx workbook binary itself
- docx binaries（main + SelfStudy）
- SelfStudy full text / fill-in rewrite of Chapters 1–9（duplicate of main with second-person voice）
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
| Mid-join presence | Structural trust asymmetry vs incumbent; stance / ally / intersection / anti-admin burial |
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
| Self-study method | Self-check chapter ends; hands-on before peeking answers; content updates stay on coaching canonical |
| Template classes | 8 workbook sheets represented only by class / field definitions |

## Overlap with existing assets

| Existing | Relationship |
|----------|-------------|
| `program-governance-cadence.md` | Complementary — **who meets where**; this playbook covers **what to manage between projects and how to control it** |
| `transformation-pmo.md` | Parent framework — program layer definition |
| `pmo-operating-guide.md` | Integration management domain; less artifact-specific coaching detail |
| `deliverable-archetypes.md` Archetype J | Customer-facing weekly/monthly **presentation**; this playbook is internal PJ間 control — header pointer only |
| `pgmo-presence-via-client-stance.md` | Compressed three moves from Slack coaching; Chapter **1.6** is the playbook-side expansion |
| `public-multi-lot-construction-pmo.md` | Different context (public multi-lot start-gates) |

## Suggested commit message

```text
update(playbooks): adopt cross-project PgMO playbook v1.9 mid-join presence
```
