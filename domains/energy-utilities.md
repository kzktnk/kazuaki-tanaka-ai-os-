# Energy & Utilities Domain

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Parent file for reusable energy / utilities knowledge  
**Does not contain:** client names, commercial terms, system product names, personal data

---

## Purpose

電力・公益案件で毎回ゼロから事業構造を説明し直さないための **Domain 親ファイル**。

- **縦軸（価値連鎖）:** 発電 → 送配電 → 小売・顧客  
- **横軸（横断能力）:** Data / Digital / AI、Operating Model、変革原則  

CX / CRM / CDP は発電と同格のセグメントではない。**小売およびグループ顧客接点の中の能力**として扱う。

送配電は骨格だけ残し、中身は薄い（材料不足）。空の章を埋めない。

発電・アセットの知見と、小売・顧客接点の知見は**混ぜない**。共通原則だけを横断節に置く。

将来の分離先（厚くなったら。**今は分割しない**）:

- `domains/energy-utilities/asset-management.md`
- `domains/energy-utilities/retail-customer.md`
- `domains/energy-utilities/transmission-distribution.md`
- `domains/energy-utilities/digital-ai.md`

---

## Scope boundary

This file contains reusable domain knowledge about energy and utilities.

It does not contain:

- client-specific facts or decisions
- detailed technology implementation procedures
- product configuration guidance
- project-specific schedules or commercial terms
- generic consulting methods that apply across industries

Generic methods belong in `frameworks/`, `playbooks/`, or `standards/`.  
Technical implementation knowledge belongs in `technology/`.  
Client-specific facts remain outside the reusable domain layer unless generalized first.

---

## How to use

案件が発電・保全中心なら Generation と Operational Reality を先に読む。  
小売・CIS/CRM/CX 中心なら Retail と Transformation principles を先に読む。  
どちらでも Operating Model と「体験から入るか、システムから入るか」を確認する。

Technology 製品手順はここには書かない → `technology/azure-enterprise.md`。

---

## Industry structure

### Principle

電力事業は単一の「ユーティリティ」ではない。少なくとも次が共存する。

| 層 | 主な成果 | 主な拘束 |
|----|----------|----------|
| 発電 | 電力量・設備信頼性・コスト | 安全、長期資産、現場例外 |
| 送配電 | 系統安定・接続 | 規制、容量、レジリエンス |
| 小売 | 契約・料金・顧客関係 | 自由化後のリスク移転、接点コスト、データ分断 |

自由化は「電気を売ること」だけでなく **リスクの所在** を移す（`knowledge/source/linkedin/sp04/`）。安定供給と事業性は同じ KPI では測れない。

### Common error

発電の保全DXの論理を、小売ポータルやコールセンターにそのまま適用する。逆も同様。

### Related

- `knowledge/source/linkedin/sp01/`–`sp07/`（レジリエンス、市場、系統の問題設定）
- `knowledge/patterns/ai-resilience-shift.md`

---

## Generation & asset management

材料の主座は既存パターン。今回の顧客系資料からの新規は薄い。

### Principle

現場DXは「設備管理システムを高度化する」ことが目的ではない。

**設備信頼性と保全効率を両立しながら、業務・データ・組織・意思決定を一体で変える。**

現場の例外・回避策・暗黙の判断を消す前に、それがなぜ残っているかを見る。

発電所の「自立」は、KPI を現場に投げれば成立しない。**誰が指標を設計し、誰が達成責任を持ち、どこまで決めてよいか**が揃って初めて、自律と統制が同時に立つ。

### Common error

- きれいな To-Be プロセスを先に描き、Operational Reality をノイズ扱いする  
- 暗黙知を「全部マニュアル化」しようとする（Initiative B の誤り）  
- 権限委譲をイベントとして一度きりで終わらせる  

### Related

- `knowledge/patterns/operational-reality.md`
- `knowledge/patterns/organizational-memory.md`
- `knowledge/patterns/exception-as-memory-entry.md`
- `knowledge/patterns/connected-organizational-memory.md`
- `knowledge/patterns/authority-levels.md`
- `frameworks/ai-adoption-roadmap.md` Initiative B
- `frameworks/capability-model.md` / `strategic-capability-network.md`

---

## T&D

**Status:** Stub — 親ファイルに枠のみ。

系統は「再エネの問題」ではなくグリッドと市場設計の問題になりやすい（`sp05`, `sp06`）。  
運用制約・接続・レジリエンスの型は、十分な一般化材料が揃ってから書く。空の節を埋めない。

### Future knowledge areas

分類枠のみ。材料が揃うまで本文を書かない。

- network planning and capacity
- connection management
- grid operations
- outage and restoration
- resilience
- distributed energy resources
- regulatory constraints
- field workforce
- asset management
- T&D data and AI use cases

---

## Retail & customer

今回の一般化の本体。基幹（契約・料金）と接点（ポータル・CC・マーケ）を混ぜない。

### Principle — 層を分ける

| 層 | 担うもの | 混ぜると起きること |
|----|----------|-------------------|
| CIS / 契約・料金 | 契約、請求、使用量、制度対応 | マーケ施策のたびに基幹を壊す |
| CRM / 統合ポータル | 接点、顧客単位の対話、セルフサービス | 料金計算をポータル側に複製する |
| コンタクトセンター | 応対、保留、セールス、運用継続 | 「システム刷新」と「応対変革」を同一案件の目的にする |
| CDP / マーケ基盤 | 統合、セグメント、施策、測定 | 入れただけで施策が回ると仮定する |

### Principle — 顧客・契約・地点を同一視しない

Utility customer data often contains multiple identities:

- customer / person
- household
- contract
- service point / premise
- meter
- member ID
- portal ID
- service subscription

These are not interchangeable.

Legacy utility data is often organized around contracts or supply points, while CRM and CX require a customer-centric view.

Therefore:

```text
Contract-centric data
        → identity resolution
        → customer-level view
        → relationship / household view
```

Customer 360 should not be assumed to exist merely because multiple datasets have been integrated.

### Principle — 体験から範囲を決める

統合ポータルや接点改革は、機能一覧から入らない。

**顧客体験 → 必要機能 → 業務の変化 → 必要データ → 実装範囲（と過渡期にやらないこと）**

料金シミュレーションや30分値連携のように、本設投資が大きいデータは、過渡期に「やる / やらない / 暫定」を先に切る。

### Principle — 重要顧客と KPI

「重要顧客」はシステムのラベルではない。KGI から CSF を特定したあとの定義である。  
KPI を複数並べると、施策もデータも散る。

### Common error

- 基幹刷新・ポータル・CDP・CC を一つの「顧客システム」として同じ成功指標で測る  
- VIP 定義を先にシステム実装し、戦略指標を後付けする  

### Related

- `knowledge/patterns/experience-before-scope.md`
- `standards/requirements-artifact-review.md`
- `frameworks/operating-model.md`

---

## Customer experience & CRM / CDP

Retail の下位能力。接点からデータを取り、個客単位でつなぎ、評価して施策に戻す。

### Principle

統合対象は契約・使用実績だけではない。サイト／アプリログ、問い合わせ、配信履歴まで「顧客の記憶」になりうる。

基盤をリリースしても、**誰が施策を回し、誰がデータを直し、誰が効果を見るか**が無いとリポジトリで終わる。

構築と利用教育は別プロジェクトにしない（`knowledge/patterns/platform-build-vs-enablement.md`）。

ロイヤルティやポイントは商品設計で終わらない。**会計処理・発行主体・グループ按分**が先に折れることがある。制度制約はオペレーティングモデルの一部である。

### Common error

- CDP 導入をデータ分析チーム設置と同義にする  
- 施策効果の PoC を、データが繋がる前に始める  
- 「一律自動化」で、人が見るべきリスト確認まで消す（HITL）  

### Related

- `knowledge/patterns/platform-build-vs-enablement.md`
- `knowledge/patterns/expertise-amplification.md`
- `frameworks/human-oversight.md`
- `knowledge/patterns/organizational-memory.md`（顧客側の記憶にも同じ論理が使える）

---

## Data / digital / AI（横断）

### Principle

顧客系では、分析の価値検証より先に **データの課題（定義、鮮度、結合キー、利用権限）** が見えることが多い。PoC の第一成果は「効いた施策」ではなく「何が足りないか」でよい。

現場 OT の AI は、きれいなマスタと手順がある前提を置かない（Operational Reality）。  
顧客系 AI は、きれいな 360° プロファイルがある前提を置かない。

Operational AI のガバナンス・権限・記憶の型は業界非依存で既にある。Domain は **どこに例外とデータ分断が積もるか** を足す。

### Principle — Prediction is useful only when it changes a decision

A more accurate model does not automatically create more operational value.

Always ask:

1. Who consumes the prediction?
2. What decision changes because of it?
3. How quickly can action be taken?
4. What happens when the prediction is wrong?
5. Is the required data available at decision time?

Model accuracy should be optimized only after the decision loop is defined.

料金予測、離脱予測、呼量予測、設備異常予測に共通する。精度議論は、この5問の後である。

### Common error

- ダッシュボード完成を DX の完了とみなす  
- 予測モデル（料金・呼量・離脱）を、業務が使わないまま精度議論する  

### Related

- `frameworks/ai-governability.md`
- `frameworks/ai-adoption-roadmap.md`
- `knowledge/patterns/operational-reality.md`
- LinkedIn Memory Arc No.18–20

---

## Operating model（横断）

### Principle

本社／現場（または本体／グループ／事業会社）の役割が曖昧なままシステムを統合すると、データは繋がっても意思決定が繋がらない。

DX 組織は「データ分析チーム」だけでは足りない。少なくとも次を横断させる。

- 事業戦略との接続  
- 分析  
- 施策・マーケの意思決定  
- アジャイルな作り方（必要なら）  
- 権限・予算・人材制度  

合議だけでグループ横断の CX を決めると、責任が薄まる。配置（経営直下か、事業内か、兼務か）は組織図の好みではなく、**誰がトレードオフを切るか**の問題である。

コンタクトセンター等の大型投資は、目的を混ぜない。

| 軸 | 問い |
|----|------|
| 継続性 | 保守切れ、拠点、共同利用の解消 — やらざるを得ないか |
| 変革 | 応対効率化か、収益化（プロフィットセンター）か、両方か |

両方やるなら、成功指標とスコープを分ける。金額モデルは Domain に置かない。

### Related

- `frameworks/operating-model.md`
- `frameworks/transformation-pmo.md`
- `frameworks/change-management.md`
- `knowledge/patterns/authority-levels.md`
- `standards/deliverable-archetypes.md` Archetype C（SteerComm）

---

## Transformation principles（横断）

1. **システム機能から入らない。** 体験（または現場の例外）から入り、実装範囲で終わる。  
2. **層を混ぜない。** CIS と CDP と CC は同じ「顧客DX」ではない。  
3. **作ると使うは同時設計。** 基盤リリースと利用能力は別成果物にしない。  
4. **過渡期にやらないことを決める。** 本設データが無い機能は、暫定か延期かを先に切る。  
5. **制度・会計は後工程ではない。** 商品・ポイント・料金充当は経理制約で折れる。  
6. **自動化は判断を消さない。** 一律自動化してよい業務と、人が残す確認を分ける。  
7. **発電の型と小売の型を交換しない。** 共通なのは「現実と権限と記憶」だけである。

---

## Knowledge provenance

This domain file is distilled from multiple utility-sector engagements and reusable knowledge assets.

Generalization rule:

```text
Client-specific observation
        → recurring pattern
        → reusable domain principle
```

No single client example should be treated as an industry-wide fact unless independently validated.

---

## Related files

| Layer | File |
|-------|------|
| Domain parent | this file |
| Standard | `standards/requirements-artifact-review.md` |
| Patterns | `experience-before-scope.md`, `platform-build-vs-enablement.md`, `all-at-once-vs-stepwise-change.md` |
| Index | `knowledge/index/legacy-source-index.md` Program Line K |
| Migration | `knowledge/migrations/energy-utilities-domain-2026-08.md` |
