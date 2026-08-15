# Migration Report — LinkedIn No.17

## Asset

- English: `How Much Authority Should We Give AI?`
- Japanese: `AIにどこまで「権限」を与えるべきか`

## Files to create

- `knowledge/source/linkedin/017/en.md`
- `knowledge/source/linkedin/017/ja.md`
- `knowledge/source/linkedin/017/metadata.md`
- `knowledge/patterns/ai-capability-vs-authority.md`
- `knowledge/patterns/authority-levels.md`

## Files to update

- `frameworks/ai-governability.md`
- `frameworks/decision-ownership.md`
- `frameworks/human-oversight.md`
- `knowledge/lessons/governance-messaging.md`
- `knowledge/source/linkedin/013/metadata.md`
- `knowledge/source/linkedin/014/metadata.md`

## Primary contribution

Capability and authority are separate design dimensions. Operational AI should use graduated authority levels per decision (Decision × Risk × Context), aiming for appropriate autonomy—not maximum autonomy.

## Knowledge extracted

### Patterns

| Pattern | Insight |
|---------|---------|
| `ai-capability-vs-authority.md` | Technical capability ≠ organizational authority; same agent, different authority per action |
| `authority-levels.md` | Recommend → Prepare → Act within limits → Execute with approval → Execute autonomously |

### Framework updates

| Framework | Addition |
|-----------|----------|
| `ai-governability.md` | Authority Design section; appropriate autonomy |
| `decision-ownership.md` | Links authority design to ownership and granting body |
| `human-oversight.md` | Oversight aligned to authority levels, not capability |

### Lesson merge

- `governance-messaging.md` — "Appropriate Autonomy" executive framing (No.17)

## Writing standard assessment

No new writing pattern required. Article follows existing Concept-Distinction pattern:

- Autonomy question vs Authority question
- Capability vs Authority
- Maximum autonomy vs Appropriate autonomy

## Relationship to LinkedIn No.13 and No.14

| Article | Contribution |
|---------|--------------|
| No.13 | Human-in-the-Loop as accountability mechanism |
| No.14 | Decision Execution vs Decision Ownership |
| No.17 | AI Capability vs AI Authority; graduated authority levels |

Combined insight:

> As AI capability rises, organizations must explicitly design authority, ownership, and oversight together—per decision context—not expand autonomy by default.

## Migration status

| Step | Status |
|------|--------|
| Source archived (EN + JA) | ✅ |
| Metadata | ✅ |
| Patterns extracted | ✅ |
| Frameworks updated | ✅ |
| Lesson merged | ✅ |
| Cross-links (No.13/14) | ✅ |
| Migration complete | ✅ |

## Suggested commit message

```text
feat(knowledge): migrate LinkedIn No.17 AI authority design
```
