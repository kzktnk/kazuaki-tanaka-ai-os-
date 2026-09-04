---
type: playbook
title: "Responsible AI assessment"
status: active
last_updated: 2026-08-19
related:
  - frameworks/human-oversight.md
  - frameworks/decision-ownership.md
  - frameworks/ai-governability.md
  - knowledge/patterns/workflow-vs-agent-vs-human.md
  - knowledge/patterns/mcp-as-integration-not-authority.md
---

# Responsible AI assessment

原則名の説明で終わらせず、案件で確認する事項と証跡に落とす。NIST / 各社カタログの転載ではない。

## Trigger

「公平性・透明性とは」など参照元が曖昧な依頼。PoC／本番化の原則レビュー。

## Sequence A — 何の「原則」か特定する

1. 利用心得か、倫理／Responsible AI か、リスク管理か、企業固有か。  
2. 原則数を「5大」に固定しない。組織で数が違う。  
3. 各原則を、守るもの／典型リスク／確認方法／証跡まで翻訳する。  
4. 必要なら公式体系へマッピングする（名称のコピーはしない）。  

Stop: 「この案件で何を確認すれば満たしたと言えるか」が言える。

## Sequence B — レビュー順（並列に並べない）

抽象原則から入らない。**誰が何の判断に使い、間違ったら何が起きるか**から逆算する。

```text
利用目的・意思決定への影響
        → Accountability（誰が責任を持つか）
        → Safety / Reliability（失敗したとき何が起きるか）
        → Privacy / Security（何のデータ・権限か）
        → Transparency（利用者・監査者が分かるか）
        → Fairness（ケース間の不当な偏り）
        → 統制・証跡・継続監視
```

各観点の確認物は、評価データ、出典表示、RACI、ログ、データ分類、IAM、異常系テスト、切り離し手段。プロンプトインジェクション等の攻撃手順は書かない。

## Infrastructure add-ons

現場フローに載るか、AI停止時も業務が続くか、高リスク判断を自動化しすぎないか。障害・品質劣化・データ異常を前提に縮退と停止。Agent / RAG も「AIだから信頼」せず、身分・最小権限・データアクセス・ネットワーク・ログ・継続検証。

`domains/energy-utilities.md` / `domains/public-defense.md` の現場現実・認可は官、と接続する。

## Output table

原則 / 想定リスク / 確認事項 / 現状 / 対応 / 証跡 / Owner

## Related

- `frameworks/human-oversight.md`  
- `frameworks/decision-ownership.md`  
- `knowledge/patterns/risk-ownership.md`  
- `knowledge/lessons/ai-output-evaluation-terms.md`  
- `domains/public-defense.md` (Assurance & evidence)  
