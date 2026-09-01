# Migration Report — Consultant skill model v0.6, Role layer, Pilot (2026-09)

## Source (not stored in repo)

Local pack `Downloads/S&T Cons Capa/` (md). Word binaries not archived.

## Files created

- `frameworks/consultant-role-responsibility-model.md`
- `frameworks/consultant-learning-map-example.md`
- `frameworks/pilot-assessment-strategy-consultant.md`
- `knowledge/migrations/consultant-skill-model-v06-2026-09.md`

## Files updated

- `frameworks/consultant-capability-skill-model.md` — v0.1 (Capability A only) → v0.6 (4 Capability / 24 Skill)
- `frameworks/capability-model.md`
- `frameworks/readme.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`

## Path alignment on ingest

Drafts pointed at `playbooks/operations-transition.md` and claimed ③ / 横串 had no markdown in-repo. Repo already has `operations-transition-playbook.md` and `stakeholder-activation-playbook.md` (plus selfstudy pairs). Those pointers and the leftover Markdown化 task were corrected. `frmeworks/` typo fixed. Docx not copied.

## Excluded

- docx
- `capabilities/` 新ディレクトリ
- 実在メンバーの Assessment 記入値（worksheet は空欄のまま）

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Skill 粒度 | 単独で L0→L4 評価できる最小単位。Playbook ≠ Skill |
| Level / Evidence | 共通ものさしと Skill ごとの測定を分離。1回の成功では認定しない |
| Role が Required Level を決める | Skill は常に L0〜L4。Strategy Consultant は I / III / IV が L2、II は L0 |
| Prerequisite Knowledge | Level 化しない。Pass / Not Yet |
| Capability IV | 型をクライアント実態に当てはめる事業実務知識。6 Skill |
| Learning Map | Capability Model × Current Level × Assignment。Confirmed / Provisional |

## Suggested commit message

```text
feat(knowledge): promote consultant skill model to v0.6 with Role and Pilot
```
