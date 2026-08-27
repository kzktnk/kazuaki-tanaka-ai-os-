# AI Adoption Roadmap Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Dual-layer AI roadmap model (technology adoption × people maturity), generalized from utility / process-industry practice. No client names or proprietary task tables.

---

## Purpose

Plan **operational AI adoption** as two synchronized layers:

| Layer | Answers | Typical artifact |
|-------|---------|------------------|
| **Technology & business roadmap** | What to deploy, when, in which domains | Use cases, platforms, initiative sequence |
| **People & role maturity roadmap** | Who must reach which capability by when | Role profiles, learning paths, HR triggers |

Technology alone reads as “tool rollout.” People alone reads as “training.” Together they explain why, for example, **limited production use cases in Year 2 require baseline risk literacy and governance in Year 1**.

See `frameworks/ai-role-maturity.md` for the people layer.

---

## When to Use

- DX / AI strategy or multi-year adoption planning (utilities, process industry, OT-heavy assets)
- Executive narrative: **Mechanism × People × Data** (+ Governance)
- PgMO or program design linking initiatives, HR, and platform work
- Client workshops where detailed internal maturity tables must **not** be shown

---

## Core Model — Four Elements + Governance

| Element | Meaning | Roadmap hook |
|---------|---------|--------------|
| **Mechanism** | Business redesign, approval routes, human–AI role split | Year 3: embed AI in workflows (BPR before agents) |
| **People** | Role-based skill maturity | `ai-role-maturity.md` |
| **Data** | Decision-critical SSOT; not wholesale cleanup | Year 1: owners and rules; Year 2: domain data products |
| **Governance** | Capability ≠ authority; who owns risk | Year 1–2: usage review; Year 3+: operational control |

Governance is explicit as a fourth element so scale and rollout do not outpace accountability (`frameworks/ai-governability.md`).

---

## Year 1–5 Narrative (Executive-Facing)

Use **phase names**, not internal level numbers, with executives.

| Phase | Label (example) | Technology & business | People (summary) |
|-------|-----------------|----------------------|------------------|
| **Year 1** | Foundation | Rules, data owners, CoE, prioritized reference data | All roles: AI risk and usage rules |
| **Year 2** | Field impact | Few production UCs; RAG / agents at **Recommend / Prepare** | Users & managers: daily use; developers: implement; governors: usage review |
| **Year 3** | Business integration | AI embedded in workflows; judgment support | Managers: workflow design; users: improvement cycles |
| **Year 4** | Scale | Cross-domain KPIs, quality / LLMOps, control maturity | Governors & developers: run quality; users: human–AI collaboration |
| **Year 5** | Optimized co-work | Routine execution to AI; people on strategy & exceptions | All roles: AI-native operating assumptions |

Detailed role-by-phase matrix: `frameworks/ai-role-maturity.md`.

---

## Three-Initiative Model (Utility / Asset-Intensive)

Generic sequence for large asset operators (planning, maintenance, operations, administration):

```text
Initiative A  Business efficiency & elevation  … judgment support in core domains
Initiative B  Tacit → explicit knowledge       … expert judgment types, exception libraries
Initiative C  AI adoption foundation           … organization / people, process, technology
```

**Recommended order**

```text
C (Year 1)  →  B (Year 2–3)  →  A in earnest (Year 2–5, deepening through Year 5)
```

- **C first:** CoE, rules, data owners, skill visibility — without these, A and B stall.
- **B parallel to early A:** Expertise amplification (`knowledge/patterns/expertise-amplification.md`) — not full manualization. Organizational memory: `knowledge/patterns/organizational-memory.md` (No.18); exception capture: `knowledge/patterns/exception-as-memory-entry.md` (No.19); connection after capture: `knowledge/patterns/connected-organizational-memory.md` (No.20); return at the decision: `knowledge/patterns/memory-at-decision.md` (No.21); feed warranted learning into the standard: `knowledge/patterns/standard-as-learned-memory.md` (No.22).
- **Full agent autonomy:** Year 4–5 at earliest; authority design stays gradual (`knowledge/patterns/authority-levels.md`).

### Initiative C — three pillars

| Pillar | Maps to roles (see `ai-role-maturity.md`) |
|--------|---------------------------------------------|
| Organization & people | Users, managers, executives; HR / skill maps |
| Process | Governance, approval, usage review |
| Technology | Developers; data platform, EAM/APM links |

---

## Business Domains (Generic)

Typical AI use domains in asset-intensive operations:

| Domain | Example use (Year 2+) | Initiative |
|--------|------------------------|------------|
| Planning | Schedule drafts, constraint checks | A |
| Maintenance | Triage, report drafts, similar cases | A + B |
| Operations | Procedure lookup, anomaly first-pass | A |
| Administration | Document summarization, comparison | A |
| Tacit knowledge | Expert Q&A, judgment patterns | B |

Initiative B implements **organizational memory** at program scale—judgment types, exception libraries, continuous enrichment (`knowledge/patterns/organizational-memory.md`, No.18; capture design at deviation: `knowledge/patterns/exception-as-memory-entry.md`, No.19; connection after capture: `knowledge/patterns/connected-organizational-memory.md`, No.20; return at the decision: `knowledge/patterns/memory-at-decision.md`, No.21; feed warranted learning into the standard: `knowledge/patterns/standard-as-learned-memory.md`, No.22).

Design for **operational reality** (`knowledge/patterns/operational-reality.md`): exceptions and field workarounds are inputs, not blockers to defer AI indefinitely.

---

## Sync Rules (Technology × People)

| If you plan… | You need concurrently… |
|--------------|------------------------|
| Year 2 production UC | Year 1 governance literacy; Year 2 user & manager baseline; developer implementers |
| Year 3 workflow-embedded AI | Manager workflow design; authority levels per step |
| Year 4 enterprise scale | LLMOps, data lineage, governor operational control |
| Year 5 wide agent use | Documented authority grants; risk owners per domain |

**HR update triggers** (link people roadmap to events, not annual plans only):

1. New program or pilot  
2. Major incident  
3. Regulatory change  
4. Business redesign from AI introduction  

Granularity: **Capability × role × phase** — not “all skills per job” nor “all skills per person” (`frameworks/capability-model.md`).

---

## KPI Layers

| Layer | Examples | Avoid |
|-------|----------|-------|
| **Outcome** | Safety, EBITDA drivers, reliability | Attributing outcome to a single enabler |
| **Monitor** | Active users, decision latency, data quality | Confusing usage with value |
| **Enabler** | Training hours, platform uptime | Stopping at enabler metrics |

---

## Mapping to Other Frameworks

| Framework | Relationship |
|-----------|--------------|
| `transformation-roadmap.md` | Seven-phase lifecycle; Year 1–5 is AI-specific horizon |
| `thinking-patterns/pattern-04-plan-build-run-improve.md` | Plan/Build/Run/Improve loop across years |
| `transformation-pmo.md` | Cross-initiative dependencies and gates |
| `ai-governability.md` | Authority design by phase |
| `ai-management-office.md` | CoE and Initiative C operating structure |
| `strategic-capability-network.md` | Capability gaps as SCN nodes |

---

## Messaging (Executive vs Design)

| Audience | Show | Hide |
|----------|------|------|
| Executive / client | Year 1–5 narrative, three initiatives, four elements | Internal Role×Level grids, client task tables |
| Program / HR design | Role×phase matrix, HR triggers | Third-party confidential slides |

Generalized messaging patterns: `knowledge/lessons/dual-roadmap-messaging.md`.

---

## Related Files

- `playbooks/ai-utilization-roadmap.md` — execution sequence and feasibility gates
- `playbooks/ai-work-before-after.md` — field Before / After
- `frameworks/ai-role-maturity.md`
- `frameworks/ai-governability.md`
- `frameworks/ai-management-office.md`
- `knowledge/patterns/ai-coe-vs-pgmo-vs-change.md`
- `knowledge/patterns/organizational-memory.md`
- `knowledge/patterns/exception-as-memory-entry.md`
- `knowledge/patterns/connected-organizational-memory.md`
- `knowledge/migrations/ai-dual-roadmap-2026-08.md`
