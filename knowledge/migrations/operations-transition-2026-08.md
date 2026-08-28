# Migration Report — Operations Transition Playbook (2026-08)

## Source (not stored in repo)

- `Downloads/files 4/operations-transition-playbook.md`（指導者版；②の姉妹としてシリーズ③）
- `Downloads/files 4/operations-transition-playbook-selfstudy.md`（文体書き換え。方法のみ抽出）
- `Downloads/files 5/operations-transition-playbook.docx` / `-selfstudy.docx`（構造パリティ。バイナリ不登録）
- Templates xlsx は 2026-08-28 時点で未作成（本文 Appendix にクラスのみ）

Anonymous label: **operations transition / AMS–IO–AI ops coaching / 2026**. Originals stay local.

## Files adopted

- `playbooks/operations-transition-playbook.md` — repo **v0.1**
- `knowledge/migrations/operations-transition-2026-08.md` — this file

## What was registered

Transition Manager 一人称の実務手順: シナリオA/B、Service Introduction、take-on／KT、工数（L1/L2/L3 の二義）、定着（Readiness／Strategy／Commitment／Adoption Definition of Done）、Gate 3〜5、② RAID の Transition Category 継続。Chapter 5・6（AI 運用ロール）は Experimental。`frameworks/ai-operations-role-design.md` は **未登録**（Draft、ポインタのみ）。

②の正本は `playbooks/cross-project-program-management.md`。原本の `cross-project-management-playbook.md` 参照と「Kazuaki確認欄」は登録時に解消・除外。

## Excluded

- docx / 未作成 xlsx
- SelfStudy 全文
- ドラフトメタ（YAML frontmatter、外部レビュー履歴ダンプ、著者チェックリスト）
- クライアント名・円・契約事実

## Overlap

| Existing | Relationship |
|----------|-------------|
| `delivery-leadership.md` | Service introduction |
| `service-transition-approach.md` | Take-on |
| `ams-services-pyramid.md` / AO SA | 工数・ピラミッド |
| `change-management.md` | 定着の組織層。個人技術は stakeholder-activation |
| `cross-project-program-management.md` | 上流②。Gate 2 → Gate 3 並走 |
| `transition-vs-transformation-vs-realization.md` | ジョブの区別 |

## Suggested commit message

```text
add(playbooks): operations-transition playbook (Gate 3–5) as series ③
```
