# Migration Report — Capability Model path correction (v0.6.4) (2026-09)

## Source (not stored in repo)

Local pack `Downloads/FInal_260902_2347/` (md). Word binaries not archived.

## Files updated

- `frameworks/consultant-capability-skill-model.md` — v0.6.4: §4 records that ③ / 横串 already exist; the missing-file look-up used `operations-transition.md` (wrong; suffix is `-playbook`)
- `frameworks/skill-playbook-directory.md` — SoT pointer only (v0.6.4)
- `frameworks/readme.md`
- `knowledge/index/master-index.md`
- `knowledge/migrations/consultant-skill-model-path-correction-2026-09.md`

## Path alignment on ingest

Pack yaml still said ③／横串 were Docx-only, used `frmeworks/` in gap_fill, dated 2026-09-01, and dropped the `frameworks/` prefix on the Financial Analysis L0→L1 cell. Did **not** take those.

Pack Directory was an older snapshot (no selfstudy line, no financial-analysis / learning-map related, no Assessor footer). Kept the repo Directory as source of truth.

Pack Pilot §6 still listed Markdown化 of ③／横串 as a next step. Did **not** restore that; files are already in the repo.

## Excluded

- docx (`consultant-capability-skill-model.docx`, `skill-playbook-directory.docx`)

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| 見つからない教材 | 先にファイル名を疑う。③・横串は `-playbook` 付き |
| Directory | Learner 入口はリポジトリ登録済みの早見表。パックの古いスナップショットで上書きしない |

## Suggested commit message

```text
feat(knowledge): record playbook path correction in consultant skill model v0.6.4
```
