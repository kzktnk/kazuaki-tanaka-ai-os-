---
type: framework
---

# Vendor Delivery Model Gap Analysis

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Framework for comparing a vendor’s proposed delivery model with the work the buyer actually needs  
**Does not contain:** vendor names, rate cards, yen, or named staffing tables

---

## Purpose

提案上の「体制・拠点・工場・下請・指名」が、**見積の作業モデルおよび発注者の制約**と一致しているかを構造化する。

会社の提案文が上手いことと、そのモデルで届くことは別である。矛盾は減点コメントではなく、ギャップ表にする。

## When to use

- 一次・二次評価で、前提・実現化・体制・工程が食い違う  
- オフショア／ニアショア／客先常駐／工場の配分を比較する  
- キーパーソン面接の前に、配置モデルの穴を特定する  
- SI 提案の tick-and-tie（範囲 ↔ 工数 ↔ 役割）が崩れている  

売手の自社 Solution Plan 最適化だけに使わない。発注者側の比較に使う。

## Inputs

- 提案の体制図、役割、稼働率、開始時期  
- 工程・WBS / work package  
- 見積内訳（原本。リポジトリに実数は置かない）  
- RFP の移行・cutover・多拠点・言語・保全制約  
- 下請・第三者・パッケージベンダーの記載  
- 発注者側の意思決定・レビュー負荷の前提  

## Structure

四つの面を並べ、交差でギャップを書く。

```text
Work to be done          (scope, volume, migration, integration)
        ×
Who does it              (named roles, factory vs site, subcontract)
        ×
Where / how              (location, language, access, hours)
        ×
What the estimate pays for
```

各セルで問う:

1. その作業は提案のどの役割が持つか  
2. その役割は見積のどの工数か  
3. 発注者制約（常駐、保全、時間帯、承認）と両立するか  
4. 欠けているなら誰の負荷に転嫁されているか（しばしば発注者）  

## Steps

1. 発注者が必要とする作業の塊を列挙する（アプリ、データ移行、IF、基盤、テスト、切替、教育、運用引継）。  
2. 提案の delivery model を同じ塊に写す。書けない塊はギャップ。  
3. 指名人材・専任度・工場／現場の比率を、工程の山と重ねる。  
4. 下請・他社依存を境界として明示する。責任空白がないか。  
5. 見積から「払っている仕事」を逆引きする。モデルにあるが払っていない、払っているがモデルにない、を印す。  
6. ギャップを、再提案質問／面接シナリオ／契約条件／残リスクに振り分ける。  

## Outputs

- 作業塊 × delivery model のギャップ表  
- 発注者に転嫁されている作業のリスト  
- キーパーソン面接で確認すべき配置条件  
- 契約に残す条件（専任、工場比率の上限、下請開示）  

## Limitations

- 実行の選定手順は Playbook。本ファイルは比較の切り方だけ。  
- レートや円の妥当性そのものは扱わない。作業モデルの対応だけ。  
- ベンダー内部の実工場プロセスを監査する手順ではない。  
- 公共調達の公平な精査コメントの書き方は `public-it-procurement-support.md`。  

## Risks

- 体制図の役職名だけ見て、稼働と場所を見ない。  
- 工場モデルを「安い」と読み、cutover 週の現場負荷を発注者が肩代わりする。  
- 指名 PM が提案専用で、実行は別部隊。  
- 下請を隠したまま、品質とコミュニケーションのギャップが後工程で出る。  
- ギャップを「要確認」のまま契約し、変更管理で取り返す前提になる。  

## Examples

- 移行が工程表に「移行」一語、体制はアプリ PM 配下のみ → 移行リード欠落。  
- 高可用を主張するが監視・運用の役割が見積にない。  
- 客先レビューを週次前提にしているが、提案は遠隔工場 100% でレビュー工数が発注者側に無い。  
実案件の組織名は書かない。

## Related files

- `standards/vendor-proposal-evaluation.md` (assumption / method / organization together)  
- `standards/vendor-key-person-interview.md`  
- `playbooks/private-it-rfp-vendor-selection.md`  
- `frameworks/private-it-rfp.md`  
- `frameworks/systems-integration-solution-planning.md`  
- `knowledge/patterns/estimate-target-commitment.md`  
- `knowledge/patterns/reproposal-as-uncertainty-reduction.md`  
