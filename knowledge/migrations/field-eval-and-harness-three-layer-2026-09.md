# Migration Report — Field practitioner eval and harness three-layer (2026-09)

## Source (not stored in repo)

Local packs (2026-09):

- Buyer-side prototype briefing for field evaluators, plus a blank feedback workbook (template + how-to + sample rows + picklists). Client names, plant names, people, filled answers, vendor slides, and channel names are **not** archived.
- Internal briefing on harness-style development for strategy consulting. Client names, product pitches, hour counts, and named engagement examples are **not** archived.

Existing buyer PoC review and ground-truth ownership were already ingested. Volatility / Tool Use / Skill-vs-subagent were already ingested.

## Files created

- `knowledge/patterns/field-practitioner-eval-before-uat.md`
- `knowledge/patterns/skills-point-to-rules-not-source.md`
- `knowledge/migrations/field-eval-and-harness-three-layer-2026-09.md`

## Files updated

- `playbooks/ai-poc-quality-review.md`
- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`
- `knowledge/patterns/define-success-before-prompt-change.md`
- `knowledge/patterns/subagent-when-isolation-justifies-cost.md`
- `knowledge/lessons/ai-output-evaluation-terms.md`
- `core/ai-collaboration.md`
- `adapters/claude/CLAUDE.md` — v1.8
- `domains/energy-utilities.md`
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`
- `knowledge/index/legacy-source-index.md`

## Excluded

- 社名、発電所名、部課名、個人名、チャネル名
- 記入済み行、サンプルの設備・許認可の実体
- ベンダーデモ画面、製品名・社内実行環境のカタログ
- 提案工数・受注事例の実数

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| 現場検証 | 正解率ではなく現場適合。職種×拠点の実務者。1問1行。分類→改善種類。2波。検証中は業務判断に使わない |
| Ground Truth | 期待回答＋本来参照してほしい資料。ボタン評価は入口 |
| ハーネス三層 | Skill＝入口（手順を持たない）。Rule＝手順。Knowledge＝原典。チャット設定では漏れる |
| 人が残す点 | 現状と目的、足場、成果物の見極め。レビュー詰まりは HITL を先に決める |
| 始め方 | 3箱から。並列化は後。調査は賛成と反証の両方 |

## Suggested commit message

```text
feat(knowledge): field practitioners judge prototype fitness before UAT; skills point to rules, not the source
```
