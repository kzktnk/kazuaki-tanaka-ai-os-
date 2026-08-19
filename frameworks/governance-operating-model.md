# Governance Operating Model Framework

**Version:** v1.0  
**Status:** Active (stub — expand from SP09 / operational cases)  
**Owner:** Kazuaki Tanaka  
**Origin:** LinkedIn SP09, `frameworks/ai-governability.md` §Operational Governance

---

## Purpose

Define how **AI governance runs as an operating capability**—not only as rules, policies, or approval documents.

In critical infrastructure and OT-heavy environments, AI enters daily operations (maintenance, incidents, planning, risk). Governance must execute in that context or fail in practice.

---

## Core distinction

| Rules-based governance | Operating-model governance |
|------------------------|---------------------------|
| Policies, compliance checklists | Detect, escalate, assign, log, adapt in production |
| Periodic review | Continuous alignment with operational reality |
| "Approved use cases" list | Authority design per decision type |

---

## Executable capabilities (minimum)

- Exception detection and escalation paths
- Accountability assignment and audit trails
- Model/agent logging, monitoring, and traceability
- Authority and permission control per decision
- Human-in-the-Loop where accountability must remain human (`knowledge/patterns/operational-governance.md`)
- Control adaptation as data, risk, and context evolve

---

## Related files

- `frameworks/ai-governability.md`
- `frameworks/ai-management-office.md`
- `knowledge/patterns/operational-governance.md`
- `knowledge/source/linkedin/sp09/`
