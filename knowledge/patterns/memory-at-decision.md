# Pattern: Memory at Decision

**Status:** Active  
**Origin:** LinkedIn No.21 (author voice, lock A)

## Pattern statement

Organizational memory becomes useful when it returns at the **moment of decision**. Connected records sitting unused in a system are not yet memory-in-use.

## Core distinction

### Knowledge system / retrieval

Waits for someone to ask. People often do not search, or they search after the decision has already been made.

The missing piece is often not information. It is **timing**.

### Memory at the decision

The system sometimes knows when prior experience may be relevant—and brings it into the room **before** someone decides.

Not: tell the operator what to do.

Not: “AI knows what we did last time.”

Yes: “AI knows when something we learned before may be worth considering again.”

## What to surface (example)

An unusual vibration–temperature combination. Instead of searching hundreds of incident reports, the system quietly says: we have seen a similar combination three times.

- One: continued operation, no issue
- One: shutdown six hours later
- One: an experienced operator stopped the equipment despite values within limits — what they looked at, why they made that call, what happened afterward

The human still owns the decision. They should not have to make it as if the organization has never seen the situation before.

## Context questions (memory, not retrieval)

1. What is happening now?
2. How similar is it to what happened before?
3. What was different?
4. What happened after the earlier decision?
5. Is the old reasoning still valid under today's conditions?

## Failure modes (timing, not connection)

- Nobody thinks to search
- Search happens after the decision
- Surface too much → people stop paying attention
- Weak similarities → noise
- Previous decisions presented as answers → automation bias

## AI role

Bring prior experience into the room before the decision. Do not own the decision. In many operational environments, perhaps it should not recommend the action.

## Core rule

> Organizational memory is not valuable because the organization remembers. It is valuable because, at the right moment, someone does not have to start from zero.

## Signals

Use this pattern when:

- Exception capture and connection exist, but cases are not reused at decision time
- Operators or PMs reconstruct familiar situations from scratch
- Search is treated as the memory interface
- AI recommendations risk replacing judgment instead of returning context
- Alert or case-surfacing volume is already causing people to ignore the system

## Related patterns

- `knowledge/patterns/connected-organizational-memory.md` — connection after capture (No.20)
- `knowledge/patterns/exception-as-memory-entry.md` — capture at deviation (No.19)
- `knowledge/patterns/organizational-memory.md` — why memory vs intelligence (No.18)
- `knowledge/patterns/expertise-amplification.md` — AI prepares; experts decide
- `knowledge/patterns/authority-levels.md` — AI may surface context without being given the decision
- `knowledge/patterns/standard-as-learned-memory.md` — whether a recurring case should change the standard (No.22)

## Related source

- `knowledge/source/linkedin/021/metadata.md`
- `knowledge/source/linkedin/022/metadata.md`
