# Migration Report — Between-PJ review viewpoints (2026-09)

## Source (not stored in repo)

Local weekly working pack on a running multi-project program (pre-meeting deck, annotated wrap-up, meeting transcript). Client names, plant names, product names used as identifiers, people, filled rows, and the transcript/recording are **not** archived.

## Files created

- `knowledge/patterns/scn-as-landscape-not-completeness.md`
- `knowledge/patterns/topology-map-vs-issue-log.md`
- `knowledge/patterns/formulation-comms-vs-adoption-comms.md`
- `knowledge/migrations/pj-between-review-viewpoints-2026-09.md`

## Files updated

- `standards/consulting-review.md` — artifact job before MECE; diagram vs table; question-first
- `core/author-voice.md` — auxiliary thinking patterns
- `playbooks/strategy-scn.md` / `strategy-scn-selfstudy.md` — Landscape vs Gate 1
- `playbooks/cross-project-program-management.md` / `-selfstudy.md` — topology vs issue log; question-first
- `frameworks/strategic-capability-network.md` — fifth use with warning
- `standards/scn-creation-guide.md` — anti-pattern
- `frameworks/change-management.md` — formulation vs adoption comms
- `knowledge/patterns/change-agent-vs-communication-plan.md` — related pointer
- `knowledge/index/master-index.md`
- `knowledge/index/legacy-source-index.md`
- `CONTEXT_ROUTING.md`

## Excluded

- Client / plant / product identifiers  
- Live SCN nodes, issue IDs, filled PJ×PJ matrices  
- Hearing questionnaires and stakeholder sample rows  
- Meeting transcript and recording  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| SCN を配置図として使う（MECE・新規立ち上げではない） | `scn-as-landscape-not-completeness.md`。口頭補足の中核 |
| 課題は PJ の間。図は位相、表は課題。5領域 | `topology-map-vs-issue-log.md`。5領域自体は② Playbook 既存。図と表の分離と質問先行が追加 |
| ヒアリングの前に問いを固定し、窓口が答えられる／要個別を仕分ける | 同上 |
| 個別 PJ の既知課題に潜らない | Landscape パターンの operating rule 3 |
| 定着コミュニケーションと、ロードマップ策定のための場は別ジョブ。キック条件が先 | `formulation-comms-vs-adoption-comms.md`。会議論点の一般化（口頭補足の主線ではない） |

## Suggested commit message

```text
feat(knowledge): separate SCN landscape use and topology maps from issue logs
```
