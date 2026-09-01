# Lesson: AI Output Evaluation Terms

**Status:** Active  
**Origin:** Distilled from Claude Certified Associate — Foundations exam preparation (2026-08). Credential, score, and exam items are **not** stored here.

## Observation

「精度が低い」「幻覚がある」を一つの不満にまとめると、直し方が決からない。失敗の種類が違う。

## Lesson

出力を評価するときは、次を混ぜない。

| 用語 | 問うこと | 失敗の例 |
|---|---|---|
| **Accuracy** | 書いてある内容が正しいか | 予算 9M なのに 12M と記載 |
| **Completeness** | 重要な情報が抜けていないか | 重大な規制リスクを書かない |
| **Groundedness / Faithfulness** | 主張が根拠資料に裏付けられているか | 資料に原因がないのに「保全不足が原因」 |
| **Inconsistency** | 同一条件なのに結論や分類が食い違うか | 同じ例外を案件ごとに別判断 |
| **Hallucination** | 根拠のない事実・引用・数値・因果を作っていないか | 存在しない規程番号を引用 |
| **Bias** | 特定の集団・属性・観点を不当に有利／不利にしていないか | 評価基準そのものが一方に偏る |

覚え方:

1. Wrong = Accuracy  
2. Missing = Completeness  
3. Unsupported = Groundedness  
4. Repeated inconsistency = criteria / rubric / source-of-truth  

Claude 自身の confidence は根拠にしない。authoritative source で検証する。

## Why it matters

平均 Accuracy が高いことと、自動化してよいかは別である。Completeness や Bias の失敗は、平均点では見えにくい。

PoC の層別（Retrieval / Answer / Business / Operational）は `playbooks/ai-poc-quality-review.md`。こちらは**1件の出力を切る語彙**。

## Prompt / knowledge の切り方

- prompt 問題 → prompt  
- knowledge 問題 → knowledge を curate  
- workflow 問題 → process / ownership  
- model 問題 → 評価してから model  

Knowledge の衝突は、指示を足す前に source-of-truth を決める。コーパスをどこに置くかは `knowledge/patterns/logical-vs-physical-document-unity.md`。

## Consequential / sensitive cases

- 重大な判断: human oversight, accountability, escalation, traceability  
- 機微データ: 必要最小限。渡しても使わせなければよい、は不十分  
- Ethics: fairness, explainability, 影響を受ける人、可逆性、automation bias  

原則の案件への落とし方は `playbooks/responsible-ai-assessment.md`。監督は `frameworks/human-oversight.md`。

## Related

- `adapters/claude/CLAUDE.md`
- `core/ai-collaboration.md`
- `playbooks/ai-poc-quality-review.md`
- `playbooks/rag-structure-diagnosis.md`
- `playbooks/responsible-ai-assessment.md`
- `knowledge/patterns/logical-vs-physical-document-unity.md`
- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`
