# Migration Report — Issue-structuring Skill and three reserved judgments (2026-09)

## Source (not stored in repo)

Local pack (2026-09-29):

- Cursor Skill draft for issue structuring (trigger only; procedure stays in the strategy engagement guide)
- First-pass trial memo on a **fictional** maintenance-services case. Company names, ratios, installed-base counts, competitor labels, and role titles from the trial are **not** archived.

Harness three-layer, Why→What→How, and the strategy engagement guide were already ingested.

## Files created

- `.cursor/skills/issue-structuring/SKILL.md`
- `knowledge/patterns/issue-structuring-reserves-three-judgments.md`
- `knowledge/migrations/issue-structuring-skill-2026-09.md`

## Files updated

- `standards/strategy-engagement-guide.md` — v1.1
- `frameworks/thinking-patterns/pattern-01-why-what-how.md`
- `frameworks/consulting-strategy-process.md` — v1.1
- `knowledge/patterns/skills-point-to-rules-not-source.md`
- `adapters/cursor/CURSOR.md` — v0.10
- `CONTEXT_ROUTING.md`
- `knowledge/index/master-index.md`
- `knowledge/index/legacy-source-index.md`

## Excluded

- 架空事例の数値・競合ラベル・役職の読み
- 試験出力本体、面談メモ原本
- WBS・提案書体裁（Skill の範囲外）

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| 入口 | Skill は読むものと人が残す点だけ。手順は engagement guide |
| 人が残す3点 | Key Question、Criteria、検証の着手順。候補は `【要判断】` |
| 不在時 | 止まらない。採用した読みを冒頭1行 |
| 打ち手先行 | How は仮説の枝。前回頓挫した打ち手から始めない |
| 4Cs | 事実／仮定／不明＋出典 |
| 仮説 | 支持と反証。空欄は未確認。最低確度を冒頭に出す |
| 分析計画 | End product＝どの図で何が言えるか。章タイトルだけがストーリーボード |
| 自己検証 | 項目ごとに判定。全部OKで済まない。範囲外は次工程 |

## Suggested commit message

```text
feat(knowledge): reserve key question, criteria, and verification order in issue structuring
```
