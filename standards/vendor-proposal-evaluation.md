---
type: standard
---

# Vendor Proposal Evaluation Standard

**Version:** v1.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** 大規模民間 ERP/RFP（2002–2003）の評価シート設計・一次／二次評価・SteerComm を一般化。社名、点数実値、円、RFP 本文は登録しない。  
**Document role:** Quality standard for evaluating vendor proposals in private-enterprise IT sourcing

---

## Purpose

提案評価を「採点作業」ではなく、**発注者の目的に対する理解、課題解決能力、実行信憑性、見積妥当性、契約可能性を証拠ベースで判断する行為**として実施する。

目的は点数を付けることではなく、**選定判断の根拠を残し、評価のばらつきを会話可能にする**こと。

`standards/consulting-review.md` が資料品質を見るのに対し、本書は**複数ベンダー比較・選定**に特化する。

法定の公共調達（総合評価・公平性・抗議耐性）は `frameworks/public-it-procurement-support.md`。民間でも他社機密の漏洩や後付けルール変更はしない。

---

## When to Use

- 民間 IT 導入の RFP に対する一次・二次評価
- 評価シートの設計・すり合わせ
- SteerComm / 選定会議向けの評価結果報告
- クライアント側評価担当者との評価基準合意

実行の順番は `playbooks/private-it-rfp-vendor-selection.md`。RFP の問いの設計は `frameworks/private-it-rfp.md`。

---

## Evaluation model — five dimensions

| Dimension | Core question |
|-----------|----------------|
| Understanding | 発注者の背景・目的・スコープ・ゴールを理解しているか |
| Proposal capability | 要件に対し、妥当な前提・実現方法・工程・体制を設計できるか |
| Delivery credibility | 書いたことを実際に実行できる根拠があるか |
| Estimate credibility | 要求・スコープ・工程・体制がコストに一貫して反映されているか |
| Contractability | 契約後の重大な条件不一致を許容可能な範囲にできるか |

---

## Sheet design (2003 practice, still valid)

### 二層構成

| 層 | 目的 | 例 |
|----|------|-----|
| **全体評価シート** | 横断的な提案能力・アーキテクチャ | 全体アーキテクチャ、提案能力、付加価値 |
| **領域別評価シート** | 領域固有の実現性・網羅性 | 基盤、業務領域 等 |

「全体概要」と「全体アーキテクチャ」が同じことを評価していないか確認する。領域別では **変化に強いアーキテクチャ**、**運用コスト**、**必要コンポーネントの漏れ** に焦点を当てる。

### 評価枠

各カテゴリに、評価 Point の**根拠・定義**を書く。ラベルだけにしない。

| 枠 | 記述すべき内容 |
|----|----------------|
| **前提** | 何を前提に提案しているか。現実性の判断基準 |
| **実現化** | 技術・スケジュール・移行の実現可能性の見方 |
| **体制** | プロジェクト体制・運用体制の妥当性の見方 |
| **工程** | スケジュール・マイルストーンの評価観点（全項目が基準になるとは限らない） |

枠は備忘録ではなく、**評価者間の認識合わせのための説明欄**。

---

## Principles

### 1 — Understanding before solution

良いソリューションに見えても、発注者の問題を理解していなければ高評価にしない。

Test: 会社名を変えても別案件の RFP に成立するか。Yes なら理解不足の可能性。

### 2 — Separate compliance, reasoning, and value-add

- **Mandatory:** 満たすこと。addressed / complete / correct / feasible。  
- **Reasoning-required:** どう考えたか。assumptions, options, risk, method, organization。  
- **Value-add:** 要求されていないから加点、ではない。目的に関連し、実問題を解き、コミットでき、過剰複雑にしないこと。型は (a) 要件外だが妥当な提案 (b) 発注側の盲点。追加機能の数ではない。

### 3 — Assumption, method, and delivery together

前提で複雑と書き工程が短い、高度方式なのに専門家がいない、大量移行なのに見積に移行がない、は矛盾として減点する。

### 4 — Confirmed vs uncertain requirements

確定要件は completeness / feasibility / estimate 反映。未確定は assumption、scenario、いつ決めるか、impact。未確定に一つの断定解を出すことが必ずしも優ではない。

### 5 — Credibility ≠ proposal writing quality

類似規模・複雑性、指名キーパーソンの実配置、資産の**今回への適用**。全候補が満たす会社プロファイルは項目から外してよい。

### 6 — Estimate is a work-model check

何の作業か、量、役割、期間、除外、前提、前提が変わったら何か。Requirement ↔ Scope ↔ WP ↔ Schedule ↔ Role ↔ Effort ↔ Cost を tick-and-tie。総額比較だけにしない。`knowledge/patterns/estimate-target-commitment.md`。

### 7 — Contractability is not a legal afterthought

scope qualification、検収、支払、IP、瑕疵、責任、下請、キーパーソン、変更管理。重大な条件差は技術点で相殺しない。

---

## Scoring model

**本 OS の既定:** 偶数段階 **0–3**。奇数段階の「真ん中＝わからない」を避ける。

| 点 | 意味（例） |
|----|-----------|
| 0 | 要件を満たさない／重大な懸念 |
| 1 | 部分的に満たす／懸念あり |
| 2 | 概ね満たす／実現可能 |
| 3 | 明確に優れている／付加価値あり |

Good / Partial / Poor や 0 / 50 / 100 は **同じ判断の別記号**。数学的真実ではない。点差を見えるようにする。一枚のシートで尺度を混ぜない。

大規模ではチームごとに持ち点（ウェイト）を割り当ててよい。重みは細かく見えるためではなく、事業クリティカル・不可逆設計・移行・指名リーダー・大きなコストドライバに置く。同じ概念の重複加点と、点数設計で結論を作ることを避ける。

See `knowledge/patterns/scoring-vs-calibration.md`.

---

## Evidence

各評価に残す: judgment / score、提案参照、evidence、comment、concern、未解決の問い。

Weak: 「体制が弱い。△」  
Better: 移行責任者が明示されずアプリ PM 配下との記載のみ、量と cutover 制約に対し Partial。二次で専任度を確認。

---

## Process

1. 評価項目ピックアップ → 必須確定 → 領域別カスタマイズ → 発注者とすり合わせ → FIX。RFP 配布後に採点方法を発明しない。  
2. 複数評価者が**独立**に評価。1社1人にしない。  
3. 意味のある点差だけキャリブレーション。平均が目的ではない。  
4. 一次: screening、懸念、情報不足、shortlist。契約判断まで完結させない。  
5. 不明は即減点確定せず、再提案・質問・面接に変換してよい。`knowledge/patterns/reproposal-as-uncertainty-reduction.md`。  
6. 二次: 「強い提案か」から「契約して実行できるか」。懸念解消、一貫性、コミット、見積、指名チーム、残リスク、契約。  
7. キーパーソンは提案書だけでは評価しない。`standards/vendor-key-person-interview.md`。  
8. 報告: 一次は論点と差分、二次は収束と推奨根拠、SteerComm は決定・未決・次アクション。総合点だけで説明しない。

---

## Architecture evaluation checklist

- [ ] 変化に強いアーキテクチャか  
- [ ] 運用コストを考慮しているか  
- [ ] 必要コンポーネントの漏れがないか  
- [ ] スケジュール・移行計画との整合  

---

## Common failure patterns

印象点（プレゼン上手＝高得点）。全案件同一シート。同じ内容の三重カウント。根拠なし点数。差を平均で消す。付加価値＝機能の数。安さを credibility の代わりにする。1人評価。項目羅列シート。

---

## Definition of done

- 最終判断の前に基準が定義されている  
- 重大判断に evidence がある  
- 評価差がキャリブレーションされている  
- 未解決が見える  
- 見積とスコープが正規化されている  
- キーパーソンが評価されている  
- 残リスクがある  
- 総合点なしでも推奨を説明できる  

評価シート設計完了前（既存ゲート）:

- [ ] 各評価 Point に根拠・定義がある  
- [ ] 領域別に不要項目を削除した  
- [ ] 付加価値の項目がある  
- [ ] 複数評価者・差分解消ルールがある  
- [ ] 偶数段階になっている  
- [ ] 発注者と基準をすり合わせた  

---

## Relationship to author voice

| 観点 | 本標準 | `core/author-voice.md` |
|------|--------|------------------------|
| 仮説 | 評価基準自体が発注側の見方 | 仮説として自分の答えを置く |
| 構造 | 内側に根拠、表側は結果と論点 | 骨格は内側、表側はストーリー |
| 留保 | 主観性を前提にプロセスで担保 | たたき台・案として提示 |

---

## Related assets

| ファイル | 関係 |
|---------|------|
| `frameworks/private-it-rfp.md` | RFP の問い |
| `frameworks/vendor-delivery-model-gap-analysis.md` | Stage 0 発注体制。提案の体制図採点ではない |
| `playbooks/private-it-rfp-vendor-selection.md` | 実行手順 |
| `standards/vendor-key-person-interview.md` | 指名人材 |
| `knowledge/patterns/scoring-vs-calibration.md` | 点差の扱い |
| `knowledge/patterns/reproposal-as-uncertainty-reduction.md` | 一次の不明をコミットへ |
| `standards/consulting-review.md` | 資料品質 |
| `frameworks/program-phases-investigation-to-requirements.md` | 調査〜要件の前工程 |
| `frameworks/public-it-procurement-support.md` | 官側。混ぜない |
| `knowledge/lessons/author-voice-archetypes-legacy.md` | 提案評価・SteerComm の声 |
