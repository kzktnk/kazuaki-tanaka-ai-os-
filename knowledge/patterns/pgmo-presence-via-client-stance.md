---
type: pattern
---

# Pattern — PgMO Presence via Client-Side Stance

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** PgMO Presence via Client-Side Stance  
**Applies to:** Multi-vendor / multi-project PgMO teams whose process pack is running but client trust and “proposal value” still sit with a long-tenured specialist PM (or similar incumbent)  
**Origin:** Anonymized **mentor–mentee Slack coaching thread** on cross-project PgMO presence (2026). Client names, personal names, yen, schedule actuals, and system/program identifiers are **not** stored here.

**Does not contain:** raw thread dump, handles, client or plant identifiers, vendor swap rumors as facts, calendar/effort numbers

---

## Pattern statement

> **「自分は PMO だから」と構えると後手になる。クライアント側 PM／PO のつもりで不足を見ると提案が生まれる。信頼が厚い既存プレイヤーと組んで仮説まで持っていく構図にし、複数関係者の「交点」のリスクと状態を定義して月次→週次へ逆算する。**

顧客向け週次／月次の**見せ方**は Program Line Z（Archetype J）の仕事。本パターンは **プレゼンスと打ち手の姿勢** である。

---

## Three moves

| Move | Judgment | Not |
|------|----------|-----|
| **1. Stance** | 「PMO だから事務局」ではなく、**クライアント側 PM／PO なら何が足りないか**を先に見る。名前に PM が付く理由をオーナーシップとして解釈する | 既存方針書の写しだけで独自提案を出したつもりになる |
| **2. Ally framing** | 論点出しで止まり、結論が「既存信頼者＋顧客」だけで決まると外様化が進む。先に既存信頼者と関係を作り、**仮説まで共有したうえで**顧客に出す。構図は「PgMO 対（既存＋顧客）」ではなく「**PgMO＋既存 対 顧客論点**」 | 既存プレイヤーを敵に回して単独で顧客に刺さる提案をする |
| **3. Intersection risk** | 大規模・多関係者では、やりとり／合流の**交点**にリスクが集まる。交点を洗い出すか定義し、**状態定義 → 月次→週次の準備状況トラッキング**へ逆算する（重点マイルストン／節目管理と同型） | 個別 PJ の進捗％だけを増やして「管理している」と言う |

現場・他ベンダーは管理を嫌うことが多い。定義した運用を**なだめすかして定着させる**こと自体が Change Management の実務である（手順書は `frameworks/change-management.md`）。

交点の洗い出しを**契約内 Hand-off の外**（隣接案件・対外）まで広げるときは、先に `knowledge/patterns/related-project-external-coordination-radar.md` を使う。

---

## Tests

- 今週の打ち手が「確認・督促・書記」だけになっていないか（Stance が事務局止まり）  
- 顧客に出す仮説を、既存の信頼ハブと**先に**擦ったか（Ally framing）  
- 管理対象が「交点の状態」になっているか、単 PJ 進捗の寄せ集めか（Intersection risk）  
- 顧客向け月次で「独自提案がない」と言われたとき、本パターンの3手に戻れるか（Archetype J の物語修正だけでは足りない）

## Use with

- PJ 間の構造化・途中参画の指導展開 → `playbooks/cross-project-program-management.md` Chapter 1.6  

- 会議階層 → `playbooks/program-governance-cadence.md`  
- 隣接・対外のレーダー → `knowledge/patterns/related-project-external-coordination-radar.md`  
- 顧客向け週次／月次 → `standards/deliverable-archetypes.md` Archetype J  
- 支援工数の箱 → `knowledge/patterns/support-effort-classification.md`  
- 姿勢の一般論 → `knowledge/lessons/pmo-professional-principles.md`

## Related

- `frameworks/transformation-pmo.md`
- `frameworks/change-management.md`
- `knowledge/migrations/pgmo-presence-client-stance-2026-08.md`
