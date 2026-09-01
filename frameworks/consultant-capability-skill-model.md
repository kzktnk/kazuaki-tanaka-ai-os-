---
type: framework
title: "コンサルタント Capability／スキル／レベル モデル（v0.1 パイロット）"
source: "①②③横串のPlaybook群を若手に配布する前提での育成マップ。クライアント組織の Capability 階層（SCN用）とは別物。"
status: draft
related:
  - frameworks/capability-model.md
  - playbooks/wbs-design.md
  - playbooks/wbs-design-selfstudy.md
  - playbooks/strategy-scn.md
  - playbooks/cross-project-program-management.md
  - playbooks/operations-transition-playbook.md
  - playbooks/stakeholder-activation-playbook.md
  - frameworks/thinking-patterns/
last_updated: 2026-09-01
---

# コンサルタント Capability／スキル／レベル モデル

**Version:** v0.1  
**Status:** Draft（Round 1 — Capability A のみレベルまで設計。B〜E は一覧のみ）  
**Owner:** Kazuaki Tanaka

クライアント組織が何をできるべきか（`frameworks/capability-model.md`、SCN）とは別物である。本書は **コンサルタント本人／チームメンバー** のスキルと習熟度、および渡す教材の対応である。`capabilities/` ディレクトリは切らない。枠組みは `frameworks/` に置く。

## このファイルの目的

①②③と横串の各 Playbook を「読ませて終わり」にせず、次の3点を一枚のマップにする。

1. コンサルタントとして育つ上で必要な **Capability**（能力の大分類）は何か
2. それぞれの Capability は、どんな **スキル**（個別の技・型）に分解されるか
3. 各スキルについて、どの **レベル** まで到達したら、どのファイルを次に渡すか

若手に配るのは個々の Playbook そのものだが、**この地図を先に本人と共有しておく**と、「今どこにいて、次に何を読むべきか」を本人が自分で判断できるようになる。

---

## 1. レベル定義（全 Capability・全スキル共通のものさし）

特定のスキルに関する熟達度を、次の5段階で共通に測る。段階の呼び方・境界はスキルを問わず揃える（揃えないと「Aさんのレベル3」と「Bさんのレベル3」が比較できなくなるため）。

| Level | 呼称 | 状態 | 教材の使い方 |
|---|---|---|---|
| **L0** | 未着手 | そのスキルの存在を知らない、または名前だけ知っている | まだ何も渡さない |
| **L1** | 型を知る | 型の名前と手順を説明できる。実施には指導者の同席・レビューが要る | **本編（指導者同席前提）**を渡す |
| **L2** | 自走できる | 指導者なしで、一人で最初から最後まで実施できる | **セルフスタディ版**を渡す |
| **L3** | レビューできる | 他者のアウトプットを見て、抜け・粒度のズレを指摘できる | 教材の「レビュー観点」部分を本人に運用させる |
| **L4** | 教えられる | 状況に応じて型をカスタマイズし、他者に指導できる | 本人が次の指導者役になる（教材の書き手候補） |

**読み方の補足**：L1→L2の壁が一番厚い（「知っている」から「一人でできる」への移行）。①②③横串の各 Playbook に本編／自己学習版の2バージョンを用意しているのは、この L1→L2 の壁をそのまま教材構成に対応させているため。L3・L4向けの独立教材は、まだ本文に埋め込まれている領域が多い。

---

## 2. Capability 一覧（大分類）

| # | Capability | 対応する主な Playbook／フレームワーク | 状態 |
|---|---|---|---|
| A | 構造化思考・WBS設計 | `frameworks/thinking-patterns/`、`playbooks/wbs-design.md` | 教材あり（本ファイルでパイロット設計） |
| B | 戦略構想・SCN構造化 | `playbooks/strategy-scn.md` | 教材あり（レベル設計は未展開） |
| C | 複数PJ横断管理（PgMO） | `playbooks/cross-project-program-management.md` | 教材あり（レベル設計は未展開） |
| D | 運用移行・定着化 | `playbooks/operations-transition-playbook.md` | 教材あり（レベル設計は未展開） |
| E | ステークホルダー活性化 | `playbooks/stakeholder-activation-playbook.md` | 教材あり（レベル設計は未展開） |

Capability A（構造化思考・WBS設計）は①②の土台になる横断スキルであるため、他より先に単独で育てておく価値が高い。Round 1 はここをパイロットとして下まで設計する。

---

## 3. パイロット：Capability A「構造化思考・WBS設計」

### 3.1 スキル分解

| スキルID | スキル名 | 一言で | 中核教材 |
|---|---|---|---|
| A-1 | Thinking Pattern の選定・適用 | 対象に合った Pattern（Why-What-How 等、全8種）を選び、箱を埋める | `frameworks/thinking-patterns/` |
| A-2 | 成果物逆算によるWBS設計 | 成果物・完了状態から逆算し、詳細タスクまで分解する | `playbooks/wbs-design.md` |
| A-3 | AIを使った構造化支援 | 箱（構造）を渡してから AI に埋めさせ、レビュー観点で検証する | `playbooks/wbs-design.md` Step 5、`core/ai-collaboration.md` |

### 3.2 スキル A-2「成果物逆算によるWBS設計」のレベル別教材マッピング

（他の2スキルより中身が具体的なため、レベル設計のサンプルとして A-2 を最初に完成させた）

| Level | 到達の目安 | 渡す教材 | 現状 |
|---|---|---|---|
| L0 | ― | ― | ― |
| L1 | Step1〜5の順番と、詳細化5問を説明できる。指導者と一緒なら分解できる | `playbooks/wbs-design.md`（本編） | あり |
| L2 | 一人で成果物から WBS を組み立て、分解チェックリストで自己採点できる | `playbooks/wbs-design-selfstudy.md` | あり |
| L3 | 他者が作った WBS を見て、`templates/wbs-breakdown-sheet.md` の STEP4 項目で指摘できる | 本編 Step 5 の3つの問いを流用可能。独立教材ではない | 部分あり |
| L4 | 案件特性に応じて Step の粒度（pt 基準等）を調整し、他者に教えられる | ― | 未整備 |

L3・L4 は「レビューする側」専用の独立教材がない。次の Round で、他者の WBS に対する指摘の型だけを切り出すかは別判断とする。

---

## 4. 置き場所と判断（Round 1 で固定）

- **置き場所:** `frameworks/consultant-capability-skill-model.md`。新ディレクトリ `capabilities/` は切らない。
- **衝突回避:** `frameworks/capability-model.md` はクライアント組織。本書はコンサルタント側。
- **配布物:** 当面はこのファイルそのもの。Capability ごとの1ページ「成長マップ」は、B〜E を展開してから決める。
- **B〜E のレベル設計:** 本編／自己学習版は既にある。次 Round で A-2 と同じ表を足す。

---

## Related

- `frameworks/capability-model.md` — クライアント組織の Capability 層。混ぜない  
- `playbooks/wbs-design.md` / `playbooks/wbs-design-selfstudy.md` — L1 / L2  
- `playbooks/strategy-scn.md`  
- `playbooks/cross-project-program-management.md`  
- `playbooks/operations-transition-playbook.md`  
- `playbooks/stakeholder-activation-playbook.md`  
- `frameworks/thinking-patterns/`  
- `core/ai-collaboration.md`  
