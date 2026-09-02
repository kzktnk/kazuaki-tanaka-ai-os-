# Migration Report — Skill Directory and Financial Analysis entry (v0.6.3) (2026-09)

## Source (not stored in repo)

Local pack `Downloads/ALL_260902_2335/` (md). Word binaries not archived.

## Files created

- `frameworks/skill-playbook-directory.md` — Learner first read; 24 Skill → what to read. Previously referenced, never in the pack
- `frameworks/financial-analysis-for-consultants.md` — Capability IV entry (Company／Financial Analysis). Pack yaml said `type: playbook`; registered as framework (lives with the skill model, not an engagement playbook)
- `knowledge/migrations/consultant-skill-directory-financial-2026-09.md`

## Files updated

- `frameworks/consultant-capability-skill-model.md` — v0.6.3: IV Learning／OJT points at the entry material; 教材開発の進捗
- `frameworks/pilot-assessment-strategy-consultant.md` — 初回は Capability I から。IV は Financial Analysis だけ教材あり
- `frameworks/consultant-role-responsibility-model.md` — v0.3.2: IV は判定できる Skill が先。入口教材は Financial Analysis のみ
- `frameworks/readme.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Path alignment on ingest

`playbooks/operations-transition.md` → `operations-transition-playbook.md`. Pack still claimed ③／横串 were Docx-only; repo already has both coach and selfstudy. Did **not** regress those claims.

## Excluded

- docx
- Named people, filled Pilot rows

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Learner UX の入口 | Directory。Capability Model は Manager SoT |
| 数字→仮説 | 読む順序 → 三表のズレ → 5問 → 確信度。AI は抽出、変換は自分 |
| IV 残り5 Skill | 教材なし。次点は Business Model／Economics |

## Suggested commit message

```text
feat(knowledge): register skill directory and financial-analysis entry for Capability IV
```
