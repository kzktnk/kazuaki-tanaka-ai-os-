# Thinking Patterns

## Purpose

このディレクトリは Thinking Pattern 1〜8 の**正本**を格納する。

各 Pattern は、コンサルティングや構想策定において「構造（箱）」を設計するための再利用可能な思考型である。トップダウン思考の入口は `frameworks/top-down-thinking.md`、早見表・AI プロンプト例・レビュー観点は `references/thinking-patterns-reference.md` を参照する。

## Scope

- Pattern 1〜8 の定義（適用場面、構造、Inputs/Outputs、Limitations、Risks）
- Pattern 間の相互参照（例: Pattern 4 ↔ 7）

本ディレクトリに含まれないもの:

- トップダウン思考の概念説明 → `frameworks/top-down-thinking.md`
- 早見表・AI 依頼テンプレート → `references/thinking-patterns-reference.md`
- WBS への展開手順 → `playbooks/wbs-design.md`
- 推論原則（Why/What/How、Transformation、Architecture） → `core/reasoning.md`

## Files

| Pattern | ファイル | 構造 |
|---|---|---|
| 1 | `pattern-01-why-what-how.md` | Why → What → How |
| 2 | `pattern-02-as-is-gap-to-be.md` | As-Is → Gap → To-Be |
| 3 | `pattern-03-input-process-output.md` | Input → Process → Output |
| 4 | `pattern-04-plan-build-run-improve.md` | Plan → Build → Run → Improve |
| 5 | `pattern-05-transformation-elements.md` | 変革の 9 要素 |
| 6 | `pattern-06-strategy-org-process-system.md` | Strategy → Organization → Process → System |
| 7 | `pattern-07-lifecycle.md` | 企画 → 構想 → 設計 → 構築 → テスト → 運用 → 改善 |
| 8 | `pattern-08-layer.md` | Business / Application / Data / Infrastructure |

## Intended Use

1. 構造化の前に、対象タスクに合った Pattern を選ぶ（選定ガイドは `references/thinking-patterns-reference.md`）
2. 選んだ Pattern ファイルを読み、構造に沿って整理する
3. AI に依頼する場合は reference ファイルのプロンプト例を使い、出力をレビュー観点で検証する

Pattern 6・8 は教育用の簡略版である。実務のアーキテクチャ議論では `core/reasoning.md` の Architecture thinking（11 層）を優先する。

## Related Assets

- `frameworks/top-down-thinking.md`
- `references/thinking-patterns-reference.md`
- `core/reasoning.md`
- `playbooks/wbs-design.md`
