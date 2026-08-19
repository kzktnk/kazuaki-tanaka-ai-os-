---
type: playbook
title: "AI PoC quality review (buyer side)"
status: active
last_updated: 2026-08-19
related:
  - standards/vendor-proposal-evaluation.md
  - knowledge/decisions/buyer-owns-ai-poc-ground-truth.md
  - playbooks/rag-structure-diagnosis.md
---

# AI PoC quality review (buyer side)

発注者側の品質保証として、RFP → 提案 → 検証計画 → 結果を一貫して見る。「動いたか」ではなく **業務利用可能か**。公共調達の評価シート設計は `standards/vendor-proposal-evaluation.md`。

## Trigger

生成AI / RAG の PoC で、検証計画や評価結果をレビューする。売手の自社提案勝ち筋ではない。

## Five roles

1. 要求との整合  
2. 評価可能性（入力・期待・指標・判定が事前にあるか）  
3. 再現可能な客観性  
4. 業務適合性  
5. 次アクションが決められるか  

精度（検索・Faithfulness 等）と業務適合（使えるか、続けたいか）を混ぜない。

## Sequence

いきなり検証計画を読まない。

1. 業務目的・方針  
2. RFP / 要求  
3. ユースケース（誰が、場面、入力、期待、参照データ）  
4. 提案の約束  
5. 検証計画  
6. 評価セット  
7. 結果（改善前後差と残課題）  

各要求を `要求 → ユースケース → シナリオ → 指標 → 合格条件` に変換する。変換できない要求は終了時に判定できない。

提案は Covered / Partial / Missing / Changed / Additional。書いてあるかではなく検証可能な具体か。

必須が空なら止める: 対象外、データセット、Ground Truth、定量／定性、件数、評価者、Baseline、再評価、Go 判定、本番への引継ぎ。

「指標を測る」と「未達時に何をするか」を分ける。

## Evaluation layers

| Layer | 問うこと |
|-------|----------|
| Retrieval | 必要な情報を取れたか |
| Answer | 取った情報から正しい答えを作れたか |
| Business | 業務で使えるか |
| Operational | 変更管理・ログ・ドリフト・コスト・再評価 |
| Decision | Go / Conditional Go / No-Go / Re-PoC / ユースケース見直し |

公開ベンチマークは合格点ではない。評価観点の参照枠。業務正解は Ground Truth。ベンダーだけで正解を決めない。

セットは簡単問いに偏らせない。言い換え、横断、表、専門用語、更新、権限、正解なし。重大事故系は別枠。

平均スコアだけで決めない。失敗を原因分類する。改善は `Baseline → 変更 → 再評価 → 差分`。

## Outputs

- 要求〜検証のギャップ表  
- Ground Truth の所有と層別  
- Go / Conditional / No-Go と本番改善項目  

## Related

- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`  
- `playbooks/rag-structure-diagnosis.md`  
- `playbooks/responsible-ai-assessment.md`  
