# Kazuaki Tanaka AI OS

Model-independent knowledge and judgment system for consistent AI-assisted consulting, writing, and delivery work.

---

## Where to Start

| Goal | Document |
|------|----------|
| **Overall structure** (8 logical layers) | [`ARCHITECTURE.md`](./ARCHITECTURE.md) |
| **3–4 level asset map** (what exists today) | [`knowledge/index/master-index.md`](./knowledge/index/master-index.md) |
| **What to load for a task** (AI / practical execution) | [`CONTEXT_ROUTING.md`](./CONTEXT_ROUTING.md) |
| **How AI should operate** | [`AI_OPERATING_MANUAL.md`](./AI_OPERATING_MANUAL.md) |

**Quick rule:** Use `master-index.md` to see *where* knowledge lives. Use `CONTEXT_ROUTING.md` to decide *what to read* for the task at hand. Expanded sources in `knowledge/source/` are archived for migration and continuity—not loaded in full during normal work.

---

## Repository Layers (summary)

```text
core/           → identity, principles, values, reasoning
standards/      → quality criteria and review standards
frameworks/     → problem structures, governance, ERP, strategy
domains/        → industry constraints and roles
technology/     → Azure / integration principles (not product manuals)
playbooks/      → execution procedures
knowledge/      → patterns, lessons, decisions, sources, indexes, migrations
templates/      → reusable document forms
adapters/       → tool-specific instructions (e.g. Cursor)
projects/       → project context templates (confidential work stays external)
```

---

## Domain Indexes

- [`knowledge/index/master-index.md`](./knowledge/index/master-index.md) — full map and maintenance rules
- [`knowledge/index/linkedin-series-index.md`](./knowledge/index/linkedin-series-index.md) — LinkedIn / Note archive
- [`knowledge/index/legacy-source-index.md`](./knowledge/index/legacy-source-index.md) — legacy PDF → repo extraction map

---

## Version

Architecture: v1.0 Navigation (see `ARCHITECTURE.md`). Knowledge map: v1.0 (see `master-index.md`).
