# Migration Report — Azure enterprise technology (2026-08)

## Source (not stored in repo)

Local handover and incident notes under Downloads (enterprise private API chain verification; personal Azure learning sandbox cost handling). Dated 2026-08-19.

**Originals not archived.** No client names, FQDNs, ports, resource names, yen, invoice IDs, or support letter bodies.

## Files created

- `technology/azure-enterprise.md`
- `playbooks/private-api-connectivity-diagnosis.md`
- `playbooks/azure-sandbox-cost-guard.md`
- `knowledge/decisions/diagnose-from-gateway-not-client-error.md`
- `knowledge/decisions/sandbox-cost-controls-before-resources.md`
- `knowledge/migrations/azure-enterprise-2026-08.md`

## Files updated

- `technology/README.md`
- `playbooks/README.md`
- `knowledge/decisions/README.md`
- `domains/energy-utilities.md` (pointer to technology parent)
- `knowledge/index/legacy-source-index.md` Program Line Q
- `knowledge/index/master-index.md`
- `CONTEXT_ROUTING.md`
- `README.md`

## Excluded

- ホスト名、ポート実値、OData path、VNet 図  
- サブスクリプション名、リソースグループ、ストレージ URL、Key Vault 名  
- 円、請求書番号、サポート問い合わせ本文、アカウント選択の個人事情  

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| Private connectivity | Design the communication chain, not the connector |
| APIM | Contract face; diagnose from gateway backend response |
| Environment switch | URL plus DNS / firewall / identity / service activation |
| Client 502 | Symptom; HTTP 200 ≠ payload success |
| Execution host | User credential outside Azure vs Managed Identity on Azure |
| Sandbox cost | Budget first; delete ≠ billing stop; high-fixed-cost SKU is an explicit decision |

## Suggested commit message

```text
feat(knowledge): add Azure enterprise parent, connectivity playbook, and cost decisions
```
