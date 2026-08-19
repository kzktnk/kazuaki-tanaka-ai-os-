# Decision: Put sandbox cost controls in place before creating Azure resources

**Date:** 2026-08  
**Status:** Active  
**Review trigger:** Work moves to a shared enterprise subscription with existing FinOps; or the SKU catalogue changes so that “high fixed cost” no longer applies to the same products

## Decision

For personal learning and short PoC subscriptions: set Budget and cost alerts before resources exist; list SKUs in advance; do not create high-fixed-cost services without an explicit decision; do not equate portal deletion with billing stop; disable the subscription when the sandbox will not be reused.

Investigate unexpected cost by identifying SKU / meter / resource history first. Refund language comes after that fact pattern.

## Context

A learning sandbox produced charges inconsistent with the intended standard secret store. Portal deletion did not stop the cost line. Self-service refund was unavailable.

## Options considered

1. Rely on OpenAI / storage usage estimates only  
2. Delete resources at the end and assume billing stops  
3. Guardrails first (budget, SKU list, post-delete cost check, subscription stop)  

## Criteria

- Detectable within a day, not at month-end  
- No yen, invoice IDs, or resource names in this repository  
- Stops new charges when the experiment is over  

## Rationale

Some SKUs bill for existing, including after logical delete. Cost Analysis resource types can disagree with what the portal list currently shows. Subscription disable is the remaining control when resource-level delete is not trusted.

## Consequences

PoC start includes a cost checklist. Support conversations lead with meter identification, not with refund as the first sentence.

## Related

- `technology/azure-enterprise.md`  
- `playbooks/azure-sandbox-cost-guard.md`  
