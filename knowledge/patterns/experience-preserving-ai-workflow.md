# Pattern: Experience-Preserving AI Workflow — Compress Effort, Keep Exposure

**Status:** Draft (pending No.25 publication)  
**Origin:** LinkedIn No.25 final-candidate text ("AI Should Compress Work, Not Experience"). Design checks, measures, and guardrails from the same draft are folded here. Source archived as draft in `knowledge/source/linkedin/025/`.

## Pattern statement

When AI takes over work that used to train junior judgment, two responses are tempting, and both fail:

- Keep juniors doing tasks the organization no longer needs. This preserves effort and wastes the AI gain.
- Have juniors review finished AI output. This looks like oversight. Reviewing well requires the judgment that reviewing alone does not fully build.

Separate **effort** (hours spent producing the output) from **exposure** (contact with the evidence, ambiguity, and challenge that form judgment). Design the workflow so AI compresses the first without quietly removing the second.

## Core distinction: effort vs. exposure

| AI can remove the effort of… | …without removing exposure to… |
|---|---|
| Copying and reconciling data | Messy, inconsistent evidence (two sites using the same term differently; a clean trend concealing missing records) |
| Drafting the recommendation | Defending it, and being asked what would make the conclusion wrong |
| Routine checks | Investigating why a particular exception matters |

## Five-step sequence

1. **Raw contact.** Before any AI summary, the junior works through a small sample of authorized primary records. This is where they learn what to doubt, which is what makes later review meaningful.
2. **AI organizes.** AI processes the rest and prepares a first view. The junior then identifies what cannot yet be trusted, which assumptions matter, and what to verify with the people doing the work.
3. **Independent judgment.** Before seeing AI's recommendation, the junior commits to a provisional judgment and the evidence or assumptions behind it. This need not be the final decision.
4. **Compare.** Set that judgment against AI's. Where did they disagree? What evidence would resolve it? Resolve material differences with a domain expert where necessary.
5. **Retrospect.** After the decision, return to it when outcome evidence exists. What actually happened? What did the learner get right, miss, or examine differently next time?

Steps 1 and 3 sit *before* AI output reaches the junior. Without them, later judgment is anchored to AI's framing.

This sequence is one illustrative design, not a procedure every junior must follow. Scale exposure to the learner's competence, the task's risk, the time available, and information sensitivity. Apply it to the work that actually carries learning.

## Signals

Use this pattern when:

- An AI rollout is justified mainly by time saved on work that juniors used to do.
- Juniors' role has shifted to "checking AI output," and nobody can say how they will learn what to check for.
- Output quality has gone up while the team's ability to handle novel or ambiguous cases has not.
- The work requires judgment under uncertainty, and a manager or qualified expert can coach.

## Boundaries

- **Not a mandate.** Do not impose the same sequence on every task or every learner.
- **Not nostalgia.** Not every old learning experience deserves preserving. Some work was only waste.
- **AI adds exposure too.** Testing alternative scenarios, surfacing cases a junior would not have found, and faster feedback can be new learning experiences. The test is whether the person is building judgment or only supervising a finished answer.
- **Training is not authority.** A learning sequence does not transfer operational decision authority. Qualified decision owners remain responsible for consequential actions. See `human-reserved-two-rationales.md` (Authority Rationale).

## Design checks

- Which part of the current workflow develops judgment, rather than only consuming time?
- What primary evidence should the learner encounter before AI summarizes it?
- Can the learner state an independent hypothesis before seeing the AI recommendation?
- Who challenges assumptions and gives substantive feedback?
- How will the learner see downstream outcomes?
- Are privacy, security, safety, and access controls preserved? Use only records the learner and the AI system are authorized to access.

## Measures and investment

Illustrative indicators, not validated KPIs.

| Lens | Ask |
|------|-----|
| Delivery | Cycle time, output quality, error or rework rate |
| Capability | Assumptions identified, detection of missing or conflicting evidence, strength of independent reasoning, calibration of confidence, improvement across repeated cases |

Do not treat speed, or the number of AI-reviewed outputs, as sufficient evidence of expertise growth. Use coaching observation alongside any quantitative indicator.

Teams that depend on expertise should also ask whether people are becoming capable of harder decisions over time. Some hours AI saves may need to be reinvested in manager coaching, challenge, and feedback. That can look inefficient in a quarterly report and still be essential over a five-year horizon. If outcomes are delayed, use supervised case reviews or simulations, and label them as such.

## Risks and guardrails

| Risk | Guardrail |
|------|-----------|
| Automation bias / anchoring | Withhold the AI recommendation until the learner has an initial view, when that is appropriate |
| False independence | A first judgment formed after an AI summary may already be anchored. Raw contact comes first |
| Token exposure | A trivial or unrepresentative sample does not guarantee learning. Select records that show real ambiguity |
| Overhead | Preserve selected learning moments, not every historical manual task |
| Feedback gaps | If outcomes are unavailable, use labeled case reviews or simulations |
| Information handling | Authorized records only; keep data governance and confidentiality |

## Illustrative example

A junior preparing an asset-maintenance recommendation first reads a limited set of inspection records and notes inconsistencies and open questions. AI then processes a larger authorized set and produces an initial analysis. The junior records a provisional recommendation before seeing AI's. A manager challenges the assumptions and asks what evidence would change the conclusion. After the decision, the team reviews what actually happened.

Hypothetical. Not a claim about any engagement.

## Core rule

> AI should compress the work that does not need our time. It should not quietly remove the experiences that teach us what to do when the answer is not obvious.

## Relationship to Human Reserved (No.23–24)

`human-reserved-two-rationales.md` identifies *why* some work and decisions should stay human (Authority, Development). This pattern is the **design response for the Development Rationale**. It expands that pattern's sequencing lever into a workflow by adding raw contact (step 1) and retrospection (step 5). No.25 frames the work so that both authority and capability can survive AI adoption. Fixing an approval gate does not fix a missing learning sequence.

This is a practitioner pattern, not an empirically proven universal method. Adapt it and check it against observed learning.

## Related patterns

- `knowledge/patterns/human-reserved-two-rationales.md` (No.23 / No.24, draft)
- `knowledge/patterns/expertise-amplification.md` (No.11)
- `knowledge/patterns/exception-as-memory-entry.md` (No.19)
- `knowledge/patterns/organizational-memory.md` (No.18)

## Related frameworks

- `frameworks/ai-role-maturity.md` — how future-scarce judgment roles get developed in practice
- `frameworks/ai-governability.md`

## Status note

Drafted from the No.25 final-candidate text ahead of publication. Source text is archived under `knowledge/source/linkedin/025/` with status draft. When No.25 is published, promote this pattern to Active and mark the source migrated.
