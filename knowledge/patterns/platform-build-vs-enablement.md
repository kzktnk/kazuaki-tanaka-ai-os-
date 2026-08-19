# Pattern: Platform Build vs Enablement

**Status:** Active  
**Origin:** Generalized from customer-data-platform launch plus user education in a utility retail program (Program Line K)

## Pattern statement

A data or CRM platform that is built without a matching ability to **promote, operate, and decide with it** becomes a searchable archive. Build and enablement are one design, two workstreams.

## Core distinction

### Build-only

Integration, data model, and first release are funded. Training is a course about the tool. After go-live, nobody owns campaigns, data repair, or measurement.

### Build + enablement

The same program defines:

- who designs interventions
- who fixes data when joins fail
- who judges outcome
- how the platform is introduced to the people who must use it (not only IT)

Education is not a separate “analytics class” unless it maps onto the live operating cycle.

## Signals

- CDP / data lake released; marketing still runs on extracts
- “We need an analytics team” as the only org answer
- Dashboard PoC before data definitions and keys exist
- Requirements review never asks whether the operating capability exists (viewpoint 7)

## Core rule

> Shipping the platform is not the same as being able to run the loop: collect → integrate → decide → intervene → learn.

## Related

- `domains/energy-utilities.md`
- `standards/requirements-artifact-review.md` (viewpoint 7)
- `knowledge/patterns/connected-organizational-memory.md` (capture without connection)
- `frameworks/ai-role-maturity.md` (users and managers, not only developers)
