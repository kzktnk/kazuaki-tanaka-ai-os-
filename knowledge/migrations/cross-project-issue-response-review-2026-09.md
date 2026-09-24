# Migration Report — Cross-project issue-list response-plan review (2026-09)

## Sources (not stored in repo)

Local review notes only (not committed):

1. **Review of response plans added to a cross-project issue list** — the plans were AI-drafted, and a second pass diffed a revised version that carried stakeholder comments (multi-subcommittee asset-management program, 2026)

Originals (issue-list workbook, review documents) stay in the engagement workspace. Nothing from them is copied into git.

## Files created

- `knowledge/migrations/cross-project-issue-response-review-2026-09.md`

## Files updated

- `playbooks/cross-project-program-management.md` — v0.9.2: new §8.8 (response-plan review: body-first sequence, 8-item tailored format, six review lenses, typical decision clusters, revision diff review); three items added to the Chapter 8 review memo
- `playbooks/cross-project-program-management-selfstudy.md` — v0.9.2: same §8.8 content (Chapter 1.6 pointer instead of repo path); three items added to the Chapter 8 self-study memo
- `standards/consulting-review.md` — v0.13: new section AI-Drafted Content Check
- `CONTEXT_ROUTING.md` — v1.48: Transformation PMO Load + Focus; Proposal Review consulting-review pointer
- `knowledge/index/master-index.md` — Knowledge flow AP, migration count, task-map pointers

## Knowledge extracted

| Source observation | Disposition | Generalized as |
|--------|-------------|----------------|
| Response plans answered questions still listed as "to confirm" | **Newly added** | §8.8 lens 4 — branch on open questions |
| One new WG / log / document per issue (about 15 across the list) | **Newly added** | §8.8 lens 5 — bundle issues into decisions; manage in existing registers |
| Past deadlines and governance bodies the client does not have | **Newly added** | consulting-review §AI-Drafted Content Check; §8.8 lenses 2–3 |
| Revised version: plan text unchanged, but stakeholder fact corrections broke its premises | **Newly added** | §8.8 revision diff review |
| Issue / risk format (Theme, Program Impact, Status/Trend, Next Milestone, Owner, Due Date, Escalation) | **Tailored** | §8.8 format for issue-list rows (adds fact vs inference and our-side role) |
| Facts vs inference in the issue body | **Already covered** | Pointer only (Chapter 3.4, 6.4; red-text marking named in §8.8) |
| PMO stance (client-side PM/PO) | **Already covered** | Pointer to `pgmo-presence-via-client-stance.md` / Chapter 1.6 |

## Excluded（未登録）

- Client name, subcommittee and program names, project codes, personal names
- Actual dates, yen figures, system product combinations specific to the engagement
- Row-level findings and the review documents themselves

## Suggested commit message

```text
feat(knowledge): add cross-project issue-list response-plan review (§8.8) and AI-drafted content check
```
