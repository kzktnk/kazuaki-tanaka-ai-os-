# Migration Report — Consultant skill model UX split (v0.6.2 / Role v0.3.1) (2026-09)

## Source (not stored in repo)

Current body: local pack `Downloads/S&T_Cons_capa_260902_2313/` (md). Preceded by `S&T_Cons_Capa_260903_2050/` (same three files, earlier copy). Word binaries not archived. `skill-playbook-directory` is referenced in both packs but was **not** included; not registered.

## Files updated

- `frameworks/consultant-capability-skill-model.md` — v0.6.2: 副題を Manager Source of Truth に変更。若手の日常入口は Directory、Learning Map は個別指示
- `frameworks/consultant-role-responsibility-model.md` — v0.3.1: 理解確認 3 問（Manager／育成担当向け）。IV は「判定できる Skill を置く。教材は後から」
- `frameworks/pilot-assessment-strategy-consultant.md` — Assessor が 1on1 で記入する診断カルテ
- `CONTEXT_ROUTING.md`
- `frameworks/readme.md`

## Path alignment on ingest

`playbooks/operations-transition.md` → `operations-transition-playbook.md`. ③／横串は `origin/main` に本編・自習版がある。Claude が再 clone で見つからないとしたのは、ファイル名が `operations-transition.md`（正: `operations-transition-playbook.md`）だったため。①②の selfstudy（`strategy-scn-selfstudy.md` / `cross-project-program-management-selfstudy.md` / `wbs-design-selfstudy.md`）も既に登録済み。`frmeworks/` 誤記を修正。

## Excluded

- docx
- `skill-playbook-directory.md`（パックに無し。Capability / Role からポインタのみ）

## Suggested commit message

```text
update(knowledge): register consultant skill model UX split (Assessor-owned assessment)
```
