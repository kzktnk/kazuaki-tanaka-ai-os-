# Migration Report — Project management policy layer (2026-08)

## Source (not stored in repo)

Local only: anonymized legacy SI proposal chapter on project management policy (requirements-to-cash style program; filename contains Q2C / RM). PPTX not copied into git.

Anonymous label: **requirements-to-cash style program / project management policy chapter**. Indexed as **Program Line Y**.

## Files created

- `knowledge/patterns/project-management-policy-layer.md`
- `knowledge/migrations/project-management-policy-layer-2026-08.md`

## Files updated

- `standards/development-management-guide.md` — policy-layer boundary section + related assets
- `standards/pmo-operating-guide.md` — project vs program control pointer
- `playbooks/program-governance-cadence.md` — related link
- `CONTEXT_ROUTING.md` — Transformation PMO / Development Standards routes (v1.23)
- `knowledge/index/legacy-source-index.md` Program Line Y
- `knowledge/index/master-index.md`

## Excluded（未登録）

- PPTX 本体・スライド全文  
- EVM／タスク予実の数値・表  
- 会議曜日カレンダー、プログラム／チーム固有名  
- 製品名・リモートツール宣伝、COVID 時代の運用スライド  
- 失敗原因・品質原因の汎用リストの写し  
- 社名、円、人名、組織図、RACI 実名、WBS ID、スケジュール実績  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| PM policy TOC | Intent / progress / project cadence / quality / issue·risk·ToDo / change / baselines |
| Project vs program | Measurement & registers inside PJ; SteerComm / cross-PJ / inspection outside |
| Progress measure | Work-value variance vs task-count % |
| Registers | Loss × uncertainty → risk / issue / neither; ToDo as assigned work |
| Change | Ticket lifecycle; QCD triggers vs baselined requirements / contract / WBS |
| Reporting | Fact-check before escalate; do not mix decision and status |

## Suggested commit message

```text
feat(knowledge): add project management policy layer pattern
```
