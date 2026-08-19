# LinkedIn Series Index

Master index of LinkedIn / Note article sources under `knowledge/source/linkedin/`.

**Status key:** `migrated` = source archived in repository.

---

## Operational AI (Main Series)

| ID | Publication | Title (EN) | Title (JA) | Languages | Path |
|----|-------------|------------|------------|-----------|------|
| 001 | Vol.1 | Will AI replace human work? I don't think that's the right question. | — | en | `001/` |
| 002 | Vol.2 | What AI actually replaces (and what it doesn't) | — | en | `002/` |
| 003 | Vol.3 | The missing piece: context | — | en | `003/` |
| 004 | Vol.4 | AI makes decisions easier… or does it? | — | en | `004/` |
| 005 | Vol.5 | So what kind of people matter in the age of AI? | なぜAI時代ほど「人の専門性」が重要になるのか | en, ja | `005/` |
| 006 | No.6 | Human expertise may become more important in the AI era — not less. | なぜOTの世界では「暗黙知」が消えないのか | en, ja | `006/` |
| 007 | No.7 | What Is Operational Governance? | Operational AIとは何か | en, ja | `007/` |
| 008 | No.8 | Why Accountability Matters More in the Age of AI Agents | なぜAIエージェント時代ほど「責任」が重要になるのか | en, ja | `008/` |
| — | *(No.9 Note → folder 013)* | Why Human-in-the-Loop Will Never Disappear | なぜHuman-in-the-Loopはなくならないのか | en, ja | `013/` |
| 010 | No.10 | What Is Operational Governance? | Operational Governanceとは何か | en, ja | `010/` |
| 011 | No.11 | Will AI Replace Experts, or Amplify Them? | AIは専門家を代替するのか、それとも増幅するのか | en, ja | `011/` |
| 012 | No.12 | Competitive Advantage in the AI Era Will Come from Operating Models, Not Models | AI時代の競争優位はモデルではなく運用体系から生まれる | en, ja | `012/` |
| 013 | No.13 (note_number: 9) | Human-in-the-Loop Is Not a Safety Mechanism—It's an Accountability Mechanism | Human-in-the-Loopは安全装置ではなく責任装置である | en, ja | `013/` |
| 014 | No.14 | Who Owns AI Decisions? | AIの意思決定は誰のものなのか | en, ja | `014/` |
| 015 | No.15 | Ownership Isn't Enough—It Must Be Verifiable | 責任者がいるだけでは足りない。「責任を証明できること」が重要になる | en, ja | `015/` |
| 016 | No.16 | Can AI Own Risk? | AIは「リスク」を負えるのか | en, ja | `016/` |
| 017 | No.17 | How Much Authority Should We Give AI? | AIにどこまで「権限」を与えるべきか | en, ja | `017/` |
| 018 | No.18 | The Future of Enterprise AI May Depend on Organizational Memory, Not Just Intelligence | AI時代の競争力は「知能」ではなく「組織の記憶」から生まれる | en, ja | `018/` |
| 019 | No.19 | Exceptions Are Where Organizational Memory Begins | 組織の記憶は「例外」から始まる | en, ja | `019/` |

**Note:** Folder `009/` is intentionally skipped. No.9 Note content is archived in `013/` with `note_number: 9`.

---

## Energy & AI Insights (Special Posts SP01–SP07)

| ID | Title (EN) | Title (JA) | Languages | Path |
|----|------------|------------|-----------|------|
| sp01 | The conversation is shifting from AI productivity to AI resilience. | 「AI Productivity」から「AI Resilience」へ | en, ja | `sp01/` |
| sp02 | AI is changing the economics of cyber defense | — | en | `sp02/` |
| sp03 | AI is not just improving utilities — it is redefining what they are. | — | en | `sp03/` |
| sp04 | Liberalization shifted risk, not just power. | — | en | `sp04/` |
| sp05 | Renewables are not an energy problem. They are a grid problem. | — | en | `sp05/` |
| sp06 | Electricity markets are no longer one market. They are three. | — | en | `sp06/` |
| sp07 | "Will AI surpass human intelligence?" That's the wrong question. | — | en | `sp07/` |

---

## Operational AI (JP) (Special Posts SP08–SP09)

| ID | Title (JA) | Languages | Path |
|----|------------|-----------|------|
| sp08 | 電力DXの本当の難しさは、AIではなくOperational Realityにある | ja | `sp08/` |
| sp09 | AIガバナンスは"ルール"ではなく"運用能力"になる | ja | `sp09/` |

---

## Enterprise Redesign Framework (ERF01–ERF03)

| ID | Title (EN) | Languages | Path |
|----|------------|-----------|------|
| erf01 | What should we expect from humans in an AI-first world? — Vol.1: Evaluation | en | `erf01/` |
| erf02 | How should we divide roles between humans and AI? — Vol.2: Role Design | en | `erf02/` |
| erf03 | How should business processes be redesigned in an AI-first world? — Vol.3: Process Re-architecture | en | `erf03/` |

---

## Governance Series Arc (No.13–17)

```
No.13  HITL = accountability mechanism (note_number: 9)
No.14  Decision execution ≠ decision ownership
No.15  Ownership must be verifiable
No.16  Execution ≠ risk ownership
No.17  Capability ≠ authority
```

## Memory / Knowledge Arc (No.18+)

```
No.18  Intelligence vs Organizational Memory
       Operational AI preserves, connects, and enriches decision context
No.19  Exceptions as memory entry + capture at deviation
       Intuition as accumulated exceptions; three capture questions
No.20+ How to scale capture and connect (future)
```

## New Patterns from Bulk Migration

| Pattern | Origin |
|---------|--------|
| `knowledge/patterns/operational-governance.md` | 007, 010, sp09 |
| `knowledge/patterns/verifiable-ownership.md` | 015 |
| `knowledge/patterns/operational-reality.md` | sp08 |
| `knowledge/patterns/expertise-amplification.md` | 011 |
| `knowledge/patterns/organizational-memory.md` | 018 |
| `knowledge/patterns/exception-as-memory-entry.md` | 019 |
| `knowledge/patterns/operating-model-advantage.md` | 012 |
| `knowledge/patterns/ai-resilience-shift.md` | sp01 |

---

## Related

- Master index: [`master-index.md`](./master-index.md)
- Bulk migration record: `knowledge/migrations/linkedin-bulk-001-015-sp-erf.md`
- Individual migrations: `knowledge/migrations/linkedin-013.md`, `linkedin-014.md`, `linkedin-016.md`, `linkedin-017.md`, `linkedin-018.md`, `linkedin-019.md`
