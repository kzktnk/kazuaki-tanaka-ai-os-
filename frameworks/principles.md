# Framework-Layer Principles

**Version:** v1.0  
**Status:** Active (stub — framework-specific extensions of core)  
**Owner:** Kazuaki Tanaka  
**Related:** `core/principles.md` (constitutional layer — takes precedence)

---

## Purpose

Principles that apply when **structuring problems and frameworks**, not when writing every deliverable. Use with `frameworks/` and `standards/`; defer to `core/principles.md` on conflict.

---

## Principles

### 1. Structure before solution

Define the decision, scope, and causal chain before recommending actions or tools.

### 2. Generalize without erasing conditions

Extract reusable patterns from experience; preserve limitations and context where they change the recommendation.

### 3. Separate layers

Do not conflate:

- **Strategy** (whether / why)
- **Framework** (how to structure)
- **Standard** (what good looks like)
- **Playbook** (how to execute)

### 4. Governance and memory are operational

Authority design (No.13–17) and organizational memory (No.18) must be embeddable in how work runs—not slide-only concepts.

### 5. Reuse through reference

Prefer linking to existing patterns and frameworks over duplicating prose across files.

---

## Related files

- `core/principles.md`
- `core/values.md`
- `core/reasoning.md`
- `ARCHITECTURE.md` §4 — eight logical layers
