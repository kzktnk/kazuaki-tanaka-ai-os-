---
type: framework
---

# Framework — Delivery Model Selection & Capability Gap Analysis

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Framework for choosing the buyer’s delivery model (who is prime, what stays in-house) before RFP issue  
**Origin:** Generalized from private-enterprise sourcing-readiness work (2002). Client names, personnel, and case-company identities removed. Vendor-type examples are types, not a current market list.  
**Applies to:** Stage 0 of `playbooks/private-it-rfp-vendor-selection.md`  
**Does not contain:** client names, vendor company names, personnel, yen

---

## Purpose

RFP を発行する前に、発注者が **どの発注体制（誰にプライムを任せ、何を自社に残すか）を選ぶか** を、勘や前例ではなく、過去事例の構造と自部門の能力ギャップから決める。

どのベンダーと組むか（vendor selection）と、どう組むか（delivery model）は別の意思決定である。発注体制が決まらないまま RFP を出すと、スコープ分担・責任分界・契約構造が提案ごとに違い、比較不能になる。

> **The delivery model is a decision the buyer must make before writing the RFP — not a question to leave open for vendors to answer.**

評価段階で「提案の体制図と見積の作業が一致するか」を見るのは `standards/vendor-proposal-evaluation.md` と SI の tick-and-tie。本ファイルはそれより前の **ロットとプライムの形** である。混ぜない。

## When to use

- Stage 0 で、誰にプライムを任せ、何を自社に残すかを決める  
- package / build と procurement lot の切り方が相互依存している  
- 自部門の能力が、想定する開発体制に足りるか不明  

使わない: 発注体制が既に確定し、個社提案を採点する段階。

## Inputs

- 過去の類似プロジェクト（自社・業界。一般化して扱う）  
- 自部門の現状体制・人数・スキルの粗い見立て  
- 想定する規模・期間・領域数（会計・人事・基盤など複数か）  
- 経営が許容するリスク選好（堅実 vs 能力蓄積）  
- 金額そのものはリポジトリに置かない  

## Structure

2軸で過去事例を分類する。

- **金の流れ（契約構造）:** 1社とのみ契約するか、複数社と個別契約するか  
- **仕事の流れ（マネジメント構造）:** 全体マネジメントと開発標準を誰が持つか  

交差から典型 5 パターン（A–E）へ落とす。その後、ベンダー類型の適合、自部門能力ギャップ、リスク選好で絞る。

## Steps

### Step 1 — Classify past cases into delivery patterns

#### Pattern A — 完全プライム型（Full-prime）

IS は1社（プライム）とのみ契約。プライムが全体マネジメント・開発標準・各領域開発を担う。発注側に必要な能力は最小（現行把握、選定、RFP、評価、進捗、検収、社内調整）。成功はプライムの PM。失敗は監督能力すら無くブラックボックス化。

#### Pattern B — 半完全プライム依存型

プライムが全体マネジメント・開発標準。特定領域は別会社。A に加え、会社間の評価・調整と、標準の妥当性判断が要る。

#### Pattern C — 軽量プライム型

IS が全体マネジメント。プライムは標準の策定・調整。領域ごとに別契約。立上げ、責任切り分け、予算、品質評価が追加で要る。

#### Pattern D — 軽量プライム＋大規模開発

C に近いが、大領域を持つ1社の標準を他社が流用する。汎用性の管理が論点。

#### Pattern E — 非プライム依存型

IS が全体マネジメント。各社が個別標準。プライムなし。発注側能力が最大（インフラ、ドキュメント管理が追加）。失敗はマネジメント不足、費用超過、保守性の低下。

### Step 2 — Vendor types against the patterns

類型と担いやすい役割の **考え方** だけ残す。社名リストは陳腐化する。案件ごとに市場を当て直す。

| ベンダー類型 | 担いやすい役割（典型） |
|---|---|
| 大手メーカー系 | プライム（A/B）。製品誘導リスクに注意 |
| 中堅メーカー系 | 特定領域の開発（C/E） |
| 大手独立系 | プライム（A/B） |
| 中堅独立系 | 特定領域（B/D/E） |
| 会計事務所系コンサル | プライム／標準／大領域（A/B/C）。コストに注意 |
| 独立系コンサル | 特定領域（C/E） |

### Step 3 — Map current capability against each pattern

**自部門が最小限持つべき能力**（安易に外に出さない）: 予算・コスト、ユーザー／経営調整、進捗評価、検収、開発会社評価、責任切り分け、ドキュメント管理。

**アウトソース可能な能力**: 選定・RFP・評価支援、現行分析、ベンダー間調整、標準の妥当性判断、立上げ支援、品質評価、システム間調整、インフラ管理。

A → E の順に発注側に求めるレベルが上がる。ギャップが大きいほど外部依存・リスク・コストが増える。

観点: スキルギャップ / パターン固有リスク（単一プライムのブラックボックス、非プライムの標準分裂） / 将来像（コストセンター寄り A、戦略部門寄り C/D、精鋭運用寄り E）。

### Step 4 — Narrow with risk appetite

堅実グループとチャレンジグループに分け、IS 戦略（効率 vs 能力蓄積）と照らして推奨と次点を出す。結果は lot 定義、RFP スコープ、評価基準へ渡す。

```text
Money flow × management structure
        → patterns A–E
        → vendor-type fit
        → capability gap (must-have / outsourceable / risk / future)
        → conservative vs challenge
        → recommended model
        → procurement lot / RFP / evaluation design
```

## Outputs

- 推奨パターンと次点  
- 自前で強化する能力／外部依存を続ける能力  
- 最大リスクと牽制（例: コンサルタントによるプライム監督）  
- 選択が自部門の将来像に与える影響  

## Limitations

- A–E は典型。中間・ハイブリッドがある。無理に1つに当てはめない。  
- 類型と役割の対応は市場再編で変わる。  
- 単一領域・短期間では 5 パターン自体が過剰。  
- 2002 年の構造分析の一般化であり、現行の特定社の能力表ではない。  

## Risks

- パターン当てはめのために案件固有を落とす。  
- 「外に出せる」を続け、自部門に発注能力が残らない。  
- 一度堅実を選ぶと以降も固定する。環境変化で再評価しない。  
- ベンダーを先に決め、契約の形を後付けにする。  

## Examples

A（必要能力最小、ブラックボックスリスク）と E（必要能力最大、直接コントロール）の両極のどこに立つかを、スキル／リスク／将来像で決める。実社名の事例は載せない。

## Anti-pattern — Choosing the vendor before choosing the model

発注体制を決めずに「良さそうなベンダー」を先に選ぶと、契約・責任分界・評価が後付けになり、RFP の比較可能性が壊れる。

> **Decide the shape of the deal before you decide who fills it.**

## Related files

- `playbooks/private-it-rfp-vendor-selection.md`  
- `frameworks/private-it-rfp.md`  
- `standards/vendor-proposal-evaluation.md`（提案後の体制 vs 作業モデル。本ファイルの後工程）  
- `frameworks/systems-integration-solution-planning.md`  
