# Decision: The buyer owns AI PoC ground truth

**Date:** 2026-08  
**Status:** Active  
**Review trigger:** The engagement is seller-side (proposal to win), not buyer-side quality advice; or there is no retrieval / generation quality claim

## Decision

For buyer-side AI / RAG PoC review, ground truth is defined and accepted by the business owner, not solely by the vendor. Public benchmarks inform the method; they are not the pass mark. A requirement that cannot be mapped to scenario, metric, and pass condition cannot be decided at PoC close.

## Context

Vendor verification plans often start from “we will measure Faithfulness” without expected answers, evaluators, or what happens on miss. Easy questions inflate scores.

## Options considered

1. Accept vendor-prepared expected answers as the score  
2. Treat public leaderboards as the acceptance bar  
3. Buyer-confirmed ground truth, layered tests, Go / Conditional / No-Go tied to business use  

## Criteria

- Reproducible  
- Separates retrieval, answer, business, and operations  
- Does not mix with seller-side bid coaching (`buyer-vs-seller-in-public-procurement.md`)  

## Rationale

Only the operator knows which miss is operationally unacceptable. Improvement must show what changed, not only a better absolute score.

## Consequences

PoC start includes a ground-truth set and evaluation owner. “It ran” is not a decision.

## Related

- `playbooks/ai-poc-quality-review.md`  
- `playbooks/rag-structure-diagnosis.md`  
- `standards/vendor-proposal-evaluation.md`  
