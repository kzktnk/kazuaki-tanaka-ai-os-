# Migration Report — Claude Foundations distillation and logical document unity (2026-09)

## Source (not stored in repo)

- Local post-exam cheat sheet for Claude Certified Associate — Foundations (2026-08). Exam items, score, and credential PDF are **not** archived.  
- Local policy-discussion deck on document administration versus generative-AI reference (2026-09 draft). Client identifiers, org units, dates, and architecture drawings are **not** archived.

## Files created

- `adapters/claude/CLAUDE.md`
- `knowledge/lessons/ai-output-evaluation-terms.md`
- `knowledge/patterns/logical-vs-physical-document-unity.md`
- `knowledge/migrations/claude-foundations-and-logical-unity-2026-09.md`

## Files updated

- `adapters/claude/README.md`
- `knowledge/index/master-index.md`
- `CONTEXT_ROUTING.md`
- `core/ai-collaboration.md`
- `standards/document-management-standard.md`
- `knowledge/patterns/connected-organizational-memory.md`
- `knowledge/patterns/organizational-memory.md`
- `playbooks/ai-poc-quality-review.md`
- `playbooks/rag-structure-diagnosis.md`
- `playbooks/responsible-ai-assessment.md`

## Excluded

- 資格証、Credly URL、得点、認定バッジ画像  
- 試験問題と選択肢  
- クライアント名、部門名、チーム記号、稼働時期  
- 現行／将来アーキテクチャ図、製品名を差別化に使う記述  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Claude 機能の使い分け | `adapters/claude/CLAUDE.md` — Knowledge / Instructions / Skill / Artifact / Connector |
| 出力評価語 | `knowledge/lessons/ai-output-evaluation-terms.md` — Accuracy ≠ Completeness ≠ Groundedness |
| 文書一元管理 × 生成AI | `knowledge/patterns/logical-vs-physical-document-unity.md` — 物理集約 ≠ 論理的一元管理 |

## Placement rationale

- Claude 固有の操作知 → adapter（モデル非依存層に製品機能カタログを置かない）  
- 評価語は Claude 以外の出力レビューにも使う → lesson（標準への昇格は再利用が積み上がってから）  
- 格納場所とガバナンスの切り方は案件を超えて繰り返す → pattern  
- 原本は機密または資格個人情報のため `knowledge/source/` に置かない  

## Suggested commit message

```text
feat(knowledge): distill Claude Foundations ops card and logical document unity
```
