# Pattern: Transition vs Transformation vs Realization

**Status:** Active  
**Origin:** Infrastructure outsourcing SA training (Program Line M); Service Introduction vs Transition from delivery-management training (Program Line O)

## Pattern statement

Outsourcing and SI programs fail when **different jobs share one plan and one budget**. Name them separately. Cost them separately. Sequence them on purpose.

## The jobs

| Job | What it is | Whose benefit | Timing |
|-----|------------|---------------|--------|
| **Service introduction** | Move a **new or changed system** into an **existing** support organization (operability + support readiness). No new run org; usually no staff transfer. | Makes **go-live supportable** | Alongside build; rehearsals and go/no-go before live |
| **Service transition / mobilization** | Stand up a **new** ability to run: people, access, tools, KT, catalog, possible staff transfer | Makes **run** possible | Independent workstream; usually around outsourcing contract start |
| **Transformation** | Fundamental change to the client’s processes, technology, and/or culture | **Client** capability and cost base | May precede, parallel, or follow transition; must have **stand-alone value** even if run never started |
| **Solution realization** | Initiatives that move as-is operational capability to the benefits promised in the Solution Plan | Closes the **sold** gap | May start before transition, during mobilization, or in run |

**Warranty** after go-live is typically a **defect-fix window**, not incident management or operations. Agree what is in warranty before live; do not staff it as run.

Transition on a **moving** estate (transformation in flight) multiplies delivery risk. Realization **during** transition does the same. Introduction into an unready support org fails silently after the build team leaves.

Accounting: true transformation is not the same as transition (cost to establish run). Do not relabel to dress the P&L. Introduction is a build workstream, not an outsourcing take-on.

## Tests

- Is there already a support organization that will keep the new system? If yes, you need **introduction**, not a full **transition**.  
- If we cancelled the outsourcing run, would this initiative still be worth doing for the client? If yes, closer to **transformation**.  
- If we cancelled transformation, could we still introduce service on the as-is? If yes, **transition** can stand.  
- Are benefits dated to events with **owners and work plans** after signature? If not, **realization** is missing.  
- Does “warranty” include incidents and how-to support? If yes, the contract is mixing warranty with run.

## Related

- `frameworks/infrastructure-outsourcing-solution-planning.md`
- `frameworks/systems-integration-solution-planning.md`
- `frameworks/delivery-leadership.md`
- `frameworks/service-transition-approach.md`
- `playbooks/operations-transition-playbook.md`
- `frameworks/change-management.md`
- `knowledge/patterns/all-at-once-vs-stepwise-change.md`
