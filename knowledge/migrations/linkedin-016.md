# Migration Report — LinkedIn No.16

## Asset

- English: `Can AI Own Risk?`
- Japanese: `AIは「リスク」を負えるのか`

## Files to create

- `knowledge/source/linkedin/016/en.md`
- `knowledge/source/linkedin/016/ja.md`
- `knowledge/source/linkedin/016/metadata.md`
- `knowledge/patterns/risk-ownership.md`

## Files to update

- `knowledge/patterns/decision-ownership.md`
- `frameworks/decision-ownership.md`
- `frameworks/ai-governability.md`
- `knowledge/lessons/governance-messaging.md`
- `knowledge/source/linkedin/013/metadata.md`
- `knowledge/source/linkedin/014/metadata.md`
- `knowledge/source/linkedin/017/metadata.md`

## Primary contribution

AI agents are not risk owners. Organizations delegate work to AI—not accountability. Separate decision execution (may autonomize) from risk ownership (remains human/institutional).

## Suggested commit message

```text
feat(knowledge): migrate LinkedIn No.16 risk ownership
```

## Relationship to series

| Article | Layer |
|---------|-------|
| No.13 | Human oversight = accountability mechanism |
| No.14 | Decision execution ≠ decision ownership |
| No.16 | Execution ≠ **risk ownership**; delegate work, not accountability |
| No.17 | Capability ≠ authority; graduated authority levels |

## Migration status

Source archived (EN + JA): ✅  
Patterns / frameworks / lesson: ✅  
Cross-links: ✅  
Complete: ✅

## Note for bulk upload (27 articles)

Register each volume under `knowledge/source/linkedin/{NNN}/`. Not all volumes require new patterns—merge when the insight already exists. No.16 adds `risk-ownership.md` as a distinct pattern from No.14's decision ownership framing.
