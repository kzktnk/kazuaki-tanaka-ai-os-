# Pattern: Human Reserved — Two Rationales

**Status:** Draft (pending No.23 / No.24 publication)  
**Origin:** LinkedIn No.23, No.24 (content drafted ahead of formal source migration)

## Pattern statement

Bill Gates's "Human Reserved" idea (2026) argues that some jobs should stay off-limits to automation even when AI is technically capable of doing them. Applied to Operational AI, the useful unit is often smaller than a job — a **decision**, or a **piece of work** — and there are at least **two distinct reasons** to reserve something for a human, not one. Conflating them leads to the wrong fix: gating approval when the real risk is a learning gap, or protecting tasks when the real need is protecting judgment.

## Two rationales

### 1. Authority Rationale (No.23)

Some decisions must remain human because **capability does not imply authority**. Even where AI can analyze, recommend, and would likely decide correctly, someone must still own what the decision means — because it sets precedent, exposes people who did not participate in it, or changes a standard that will govern future decisions.

| | |
|---|---|
| Question it answers | Should AI be allowed to decide this — regardless of whether it is capable of deciding it well? |
| Protects | Accountability for a specific decision, right now |
| Failure mode if ignored | An accountability gap — a decision nobody truly owns |
| Extends | `ai-capability-vs-authority.md` and `authority-levels.md` (No.17) from the agent/job level down to the individual decision |

### 2. Development Rationale (No.24)

Some work must remain human — at least in part — because **doing it is how judgment is formed**, not only how output is produced. If AI absorbs the work that used to train junior judgment (research, first drafts, analysis, spotting the exception), the organization may gain short-term productivity while losing its supply of future experts.

| | |
|---|---|
| Question it answers | Should a junior do this themselves — regardless of whether AI could do it faster or better? |
| Protects | The organization's future supply of judgment, not today's output |
| Failure mode if ignored | An expertise gap — a generation with no one able to evaluate whether AI's output is actually right |
| Extends | `expertise-amplification.md` (No.11) and `exception-as-memory-entry.md` (No.19). No.11 explains how existing experts should work with AI; No.19 explains that intuition is accumulated exposure to exceptions; No.24 answers how someone becomes the expert who has that intuition, once AI does the exposure-generating work first |

## Comparison

| | Authority Rationale (No.23) | Development Rationale (No.24) |
|---|---|---|
| What is protected | Who decides | Who learns by doing |
| Time horizon | This decision, now | The organization's next 5–10 years |
| Applies to | Consequential, often irreversible decisions | Recurring, learnable tasks |
| Failure mode if ignored | Accountability gap | Expertise gap |
| Resolved by AI getting better? | No — authority is a governance choice, not a capability threshold | No — the more AI absorbs the task, the fewer natural learning opportunities remain |
| Design lever | Authority ladder per decision (`authority-levels.md`) | Sequencing of when/how AI's output reaches the junior |

## Signals

Use this pattern when a team proposes automating a task and the only question being asked is "can AI do this reliably?" Two follow-up questions are missing if the pattern applies:

1. Even if AI can do it well, **who is accountable** for the outcome? (Authority)
2. Even if AI can do it well, is this currently **how someone learns** to do it themselves? (Development)

A given task can trigger neither, either, or both:

| Case | Rationales | Response |
|------|------------|----------|
| Routine, low-stakes, already-mastered | Neither | Automate freely |
| High-stakes, irreversible, precedent-setting | Authority only | e.g. a senior expert's own routine analysis still needs a Decision Owner |
| Done mainly by juniors as a training ground, individually low-stakes | Development only | Keep exposure in the path |
| Both | Both | Human Reserved on two independent grounds; fixing one does not fix the other |

## Design response

For a given task or decision:

1. **Ask the Authority question first.** If it applies, the design response in `ai-capability-vs-authority.md` / `authority-levels.md` governs: name the authority level, the granting body, and the Decision Owner.
2. **Separately ask the Development question.** If it applies, do not only gate who approves the output — redesign how the work reaches the junior:
   - AI produces the first analysis; the junior must challenge it before it goes further.
   - AI drafts the recommendation; the junior must state what evidence would change it.
   - AI finds candidate precedents/cases; the junior decides which analogy actually holds.
   - The junior makes a first judgment before seeing AI's output, then compares.
3. Treat Authority and Development as **independent axes**, not one sliding scale. A task can be automated for productivity and still need a human-in-the-path for either reason, and the two require different fixes (an approval workflow vs. a sequencing/exposure design).

## Core rule

> "Human Reserved" is not one category but two. One protects who is accountable for a decision today (Authority). The other protects who will be capable of making that judgment tomorrow (Development). A task can be sped up by AI and still need to stay partly human for either reason — and the two failures look different, so they need different fixes.

## Related patterns

- `knowledge/patterns/ai-capability-vs-authority.md` (No.17)
- `knowledge/patterns/authority-levels.md` (No.17)
- `knowledge/patterns/decision-ownership.md` (No.14 / 17)
- `knowledge/patterns/expertise-amplification.md` (No.11)
- `knowledge/patterns/exception-as-memory-entry.md` (No.19)
- `knowledge/patterns/organizational-memory.md` (No.18)

## Related frameworks

- `frameworks/ai-governability.md`
- `frameworks/decision-ownership.md`
- `frameworks/ai-role-maturity.md` — the Development Rationale is a mechanism by which "future-scarce" roles (domain expert who governs AI output, etc.) actually get filled

## Status note

Drafted from No.23 / No.24 article content ahead of formal publication. When both posts are published, run the Knowledge Migration workflow to: archive `en.md` / `ja.md` / `metadata.md` for No.23 and No.24; cross-link from `frameworks/decision-ownership.md` and `frameworks/ai-governability.md` if not already done; promote this pattern to Active; and complete the Human Reserved Arc entry in `knowledge/index/linkedin-series-index.md`.
