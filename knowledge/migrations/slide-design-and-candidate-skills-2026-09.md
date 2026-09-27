# Migration Report — Slide design standard and candidate Skills (2026-09)

## Source (not stored in repo)

- `carnot-tech/consulting-pptx-skill` `references/slide-rules.md`（MIT License, Copyright (c) 2026 Carnot AI Inc.）。原文・例文・パーツ集・スクリプトは複製していない。AI OS未収録の9項目だけを自分の言葉で書き直した
- 取り込み候補の選定（候補27件・優先度つき）は Claude Docs「slide-rules 取り込み候補一覧」（2026-09-26）で行った。本レポートは #1〜#9 と #27 の反映分

## Files created

- `standards/slide-design.md` — v0.1 draft（試行版）。タイトル5・配置2・表2の9項目、提出前チェック、既存ルールとの適用範囲（体言止め・So what・留保）
- `knowledge/migrations/slide-design-and-candidate-skills-2026-09.md`

## Files updated

- `standards/writing.md` — §Slide Writing から slide-design.md への入口1行
- `frameworks/consultant-capability-skill-model.md` — v0.7。§1.6「候補（Candidate）の扱い」新設。SI Project Literacy をB案（独立の候補Skill）で接続。Communication に slide-design.md 由来の〔候補〕Evidence
- `frameworks/si-project-literacy.md` — v0.6.1。Appendix を A案／B案の比較と旧5項目の行き先に書き換え
- `frameworks/readme.md`
- `CONTEXT_ROUTING.md` — v1.49。Proposal Review、Consultant Enablement
- `knowledge/index/master-index.md` — v1.42（Standards 21、migrations 56、flow AQ）
- `core/author-voice.md` — §4.1 から slide-design への入口
- `standards/consulting-review.md` — Artifact Job「Slide page」（v0.14）
- `frameworks/skill-playbook-directory.md` — Communication から slide-design（試行）へ

## Excluded

- slide-rules.md の見た目の具体値（フォント・色・罫線・角丸・充填率）— IBMテンプレートとブランドが優先
- ピッチデック（登壇用）の作法、口語を混ぜる等のメール向け助言、英字キッカー禁止
- 62型のHTMLパーツ集・check_deck.py（プレースホルダー検出が本文を見ない欠陥あり）
- 候補 #10〜#26（フレッシュアイ・レビュー、図の作法、語彙リスト等）— 次の取り込み単位

## Knowledge extracted

| Topic | Generalized as |
|-------|----------------|
| 1枚の中身の作り方が標準にない | slide-design.md（deliverable-archetypes＝何枚・何順、author-voice＝トーン、consulting-review＝判断の質と分担） |
| draft教材に依存する評価基準を先に確定させると、教材の欠陥が評価の欠陥になる | Capability Model §1.6〔候補〕：教材の試行後に正式化。正式化までSkill数・Worksheet・Required Levelに数えない |
| SI Literacyの5項目のうち3項目は判断であり、Pass／Not Yetでは入口条件がL2相当に逆転する | B案（2026-09-27 Owner決定）：知識2項目＝Prerequisite Knowledge、判断3項目＝L0〜L4 Evidence。②系4 Skillとは§1.5のsoft Prerequisite（SI未経験者のみ）で接続 |

## Deferred

- SI Project Literacy の正式化（〔候補〕を外す）— Chapter 5 Pilot後。正式化時に Skill数25、`pilot-assessment-strategy-consultant.md`、`consultant-role-responsibility-model.md`（PgMO Role）、`skill-playbook-directory.md` に反映
- Communication 〔候補〕Evidence の統合 — slide-design.md の試行デッキ1本の後
- 取り込み候補 #10〜#26

## Suggested commit message

```text
feat(standards): add slide-design trial standard; capability model v0.7 candidate rule (SI literacy as Option B skill, Communication evidence)
```
