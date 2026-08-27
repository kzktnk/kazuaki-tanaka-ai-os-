# Migration Report — Cross-project program management (2026-08)

## Source (not stored in repo)

Revised local coaching materials for a subordinate PgMO role:

- `Downloads/cross-project-management-playbook.md`（truth for body; **v2.1** as of 2026-08-27）
- `Downloads/Cross-Project-Management-Playbook.docx`（structure parity with md; Word-only TOC / font packaging / cover metadata ignored）
- `Downloads/cross-project-management-playbook-selfstudy.md`（voice rewrite of main; method extracted only）
- `Downloads/Cross-Project-Management-Playbook-SelfStudy.docx`（parity with selfstudy md; binary ignored）
- `Downloads/Cross-Project-Management-Playbook-Templates.xlsx`（Cover + 8 sheets; field inventory refreshed; binary not committed）

Indexed anonymously as **multi-vendor cross-project PgMO coaching / 2026**. Originals not archived. Docx / xlsx binaries not committed.

## Files adopted or updated

- `playbooks/cross-project-program-management.md` — repo Version **v0.7**; source revision **v2.1**
- `knowledge/migrations/cross-project-program-management-2026-08.md` — this file (supersedes prior v1.9 note in place)
- `knowledge/index/legacy-source-index.md` — Program Line W
- `playbooks/strategy-scn.md` — upstream ① pointer / Gate 1 connection (separate migration)

## Material changes since prior adopt (v1.9 → v2.1)

| Area | What changed |
|------|----------------|
| Series position (v2.1) | ① Strategy-SCN → ② this playbook → ③ ops/定着化; upstream+downstream exclusions made symmetric |
| Purpose bullets (v2.0) | Chapter refs on the three coaching questions |
| Pre-start checklist (v2.0) | **着手前チェック** — required/desired inputs per artifact; what to do when inputs missing; Gate 2 framing vs ① Gate 1 |
| Dirty PJ boundary (v2.0 / 2.0.1) | **Chapter 2.7** program-structure Health Assessment (contract vs system unit); generalized (no client-grain examples) |
| Mental model wording (v2.0) | Chapter 2.6 forward-reference wording fix |
| RAID (v2.0) | R/A/I/D definition table + Assumption ↔ premortem link |
| Appendix (v2.0) | Sample-row note; field inventory columns added in repo |
| Templates xlsx | Sheet count / fields **unchanged** (Cover + 8) |
| Self-study | Method unchanged; add series-boundary awareness; full SelfStudy still not registered |

## Excluded (not registered)

- xlsx / docx binaries（main + SelfStudy）
- SelfStudy full text
- cover metadata / author personal review checklist / revision-history dump
- local YAML frontmatter
- sample rows that would register live program facts
- vendor names, personal names, costs, exchange-rate figures, contract facts, or client-identifying details

## Overlap with existing assets

| Existing | Relationship |
|----------|-------------|
| `playbooks/strategy-scn.md` | Upstream ① — Gate 1 handoff into this playbook’s 着手前チェック（Gate 2） |
| `program-governance-cadence.md` | Complementary — **who meets where** |
| `transformation-pmo.md` | Parent framework |
| `pgmo-presence-via-client-stance.md` | Compressed three moves; Chapter 1.6 expansion |

## Suggested commit message

```text
update(playbooks): adopt cross-project PgMO playbook v2.1 (Gate 2 / Health Assessment)
```
