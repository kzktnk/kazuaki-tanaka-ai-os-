# Decision: Interim connectivity is not the target architecture

**Date:** 2026-08  
**Status:** Active  
**Review trigger:** The deferred component (policy, private link, API gateway) is available; or security has approved a different permanent path

## Decision

When the target private chain is not yet usable, choose a minimal interim path that preserves security constraints. Record exit criteria at the same time. Do not let the interim design become the documented target.

## Context

Verification would have stopped until a target component was approved. A public endpoint would have unblocked the demo but violated the client standard.

## Options considered

1. Wait for the target path and stop all verification  
2. Add a public IP / internet RDP to move faster  
3. Minimal private interim with Bastion-class management and a written return path  

## Criteria

- Does not create a permanent exception  
- Can be removed when the target component arrives  
- Failure diagnosis still walks network before identity  

## Rationale

Time-to-access is not a reason to change the architecture principle. An interim that cannot be exited becomes shadow production.

## Consequences

Handovers include target diagram, interim diagram, and kill conditions. Cost playbooks apply: do not leave gateway VMs after the target path works.

## Related

- `playbooks/interim-connectivity.md`  
- `technology/azure-enterprise.md`  
