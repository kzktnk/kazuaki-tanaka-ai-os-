# Migration Report — AI / transformation playbooks (2026-08)

## Source (not stored in repo)

Local playbook drafts under Downloads (business Before/After, utilization and steering roadmap, AI PoC evaluation, offering review, Responsible AI assessment, RAG table diagnosis, Power Platform interim connectivity extraction). Dated 2026-08.

**Originals not archived.** No operator names, IBM branding as differentiator, annual-report figures, FQDN lists, or current vendor scores.

## Files created

- `playbooks/ai-work-before-after.md`
- `playbooks/ai-utilization-roadmap.md`
- `playbooks/ai-poc-quality-review.md`
- `playbooks/offering-review.md`
- `playbooks/responsible-ai-assessment.md`
- `playbooks/rag-structure-diagnosis.md`
- `playbooks/interim-connectivity.md`
- `knowledge/decisions/interim-connectivity-is-not-the-target.md`
- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`
- `knowledge/migrations/ai-playbooks-2026-08.md`

## Files updated

- `technology/azure-enterprise.md`
- `frameworks/ai-adoption-roadmap.md`
- `playbooks/README.md`
- `knowledge/decisions/README.md`
- `knowledge/index/legacy-source-index.md` Program Line R
- `knowledge/index/master-index.md`
- `CONTEXT_ROUTING.md`

## Excluded

- 部門名・スローガン実案、年次の実タスク表  
- 公開報告書の KPI 数値、Chunk JSON の製品コピー  
- Gateway の公式 FQDN カタログ、PowerShell 実コマンドの固定化  
- オファリング資料の社内ブランド主張  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Field AI story | Same process left/right; humans keep the decision |
| Roadmap execution | Use cases last; states not tasks; six feasibility gates |
| Buyer PoC | Ground truth owner; layers; Go is not “it ran” |
| Offering | To-Be ≠ mechanism ≠ PMO ≠ change |
| Responsible AI | Accountability first, then failure, data, transparency, fairness |
| RAG tables | Search hit ≠ structured cell correspondence |
| Interim path | Not the new target; network before auth |

## Suggested commit message

```text
feat(knowledge): add AI transformation playbooks, PoC review, and interim connectivity
```
