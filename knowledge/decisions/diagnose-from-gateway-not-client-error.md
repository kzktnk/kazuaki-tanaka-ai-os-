# Decision: Diagnose private API failures from the gateway log, not the client error

**Date:** 2026-08  
**Status:** Active  
**Review trigger:** The front-end is no longer in front of an API gateway; or the gateway is not on the path

## Decision

Treat the client HTTP code as a symptom. Locate the break with the API gateway’s backend response (or its absence), then walk DNS / NSG / route / firewall / peering / host / port / TLS.

Name a successful route as environment + FQDN + port + path + entry. Do not record “it connected.”

## Context

Front-end 502/500 appeared while the break was backend reachability, the wrong entry (application host vs reverse proxy), or an environment switch that changed URL but not DNS/firewall. Portal Test was sometimes unavailable.

## Options considered

1. Debug only in the front-end / connector  
2. Rely on the gateway portal Test tab  
3. Split the chain: did the request arrive → did the backend answer → which layer failed  

## Criteria

- Reproducible across environments  
- Ticket goes to the owner of the failed layer  
- HTTP 200 is not confused with payload/connector success  

## Rationale

The front-end often wraps downstream failure as 502. A missing backend response code means the call died before an HTTP answer. A backend 200 means connectivity is done; response shape is a different workstream.

## Consequences

Network, API, and application owners receive different work. Estimate and cutover checklists include DNS and firewall, not only backend URL.

## Related

- `technology/azure-enterprise.md`  
- `playbooks/private-api-connectivity-diagnosis.md`  
