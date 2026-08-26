---
type: pattern
---

# Pattern — Related-Project / External-Coordination Radar

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Related-Project / External-Coordination Radar  
**Applies to:** Multi-project / multi-vendor programs where adjacent work and external parties can block tests, cutover, or acceptance before they appear on the Dependency Register  
**Origin:** Anonymized **related-project / external coordination support template** (Program Line U extension). Client names, personal names, yen, inventories, and filled rows are **not** stored here.

**Does not contain:** operator / ministry / vendor names, project titles from live packs, yen, org charts with real names, contract IDs, inventory counts

---

## Pattern statement

> **プログラム契約内の Dependency Register だけでは、隣接案件と対外アクターの遅れを拾えない。関連案件レーダーと対外調整台帳を別物として回し、仮説→確認→本体台帳への移管の出口を最初に決める。**

`playbooks/cross-project-program-management.md` の Dependency Register は、**すでにプログラム管理対象として認識された Hand-off** を扱う。本パターンは、その手前の **レーダー層** である。

| Register | Job | Not for |
|----------|-----|---------|
| **Related-project radar** | 隣接・並行する他案件が、いつ・どのワークストリームに波及しうるかを仮説で洗う | 契約内 Hand-off の詳細仕様レビュー |
| **External stakeholder coordination** | プログラム組織図の外（他事業者・他部署・他プログラム窓口）で調整が必要な相手と時期を固定する | ステコミ決定依頼の本文（Archetype C） |
| **Master risk / issue / ToDo** | 確認済みでプログラムが追跡すべきものだけを受け取る | 未確認の噂の永久保管 |

`playbooks/public-multi-lot-construction-pmo.md` が「関連案件・対外調整は見る」と言うときの **見る型** が本パターンである。

---

## Template class (fields only)

実シート・実データは原本。リポジトリに登録するのは **列のジョブ** だけ。

### Related-project radar

| Field class | Judgment to lock |
|-------------|------------------|
| Identity | 案件を識別する短いラベル（固有名詞は原本） |
| Impact scope tags | どの並行ストリーム／ロットに触れるか（複数可）。進捗％ではない |
| Impact window | 影響が出る時期の仮説（マスタスケジュール上の帯） |
| Impact hypothesis | 「遅れる／ずれると何が止まるか」を一文で |
| Hearing / evidence | 内部ヒアリングや観測の結果（未確認は未確認と書く） |
| Next action | 誰が何を確認するか |
| Promote-to | 本体の risk / issue / ToDo への移管先（または「レーダーに留める」） |

### External stakeholder coordination

| Field class | Judgment to lock |
|-------------|------------------|
| Stakeholder | 役割で書く（人名は原本；台帳の主キーにしない） |
| Role vs this program | 何を握っているか（決定／作業／情報提供のみ、等） |
| Impact scope tags | 関連案件レーダーと同じタグ軸を使う |
| Coordination window | いつまでに何を合わせるか |
| Assumed ask | 支援側の仮説としての調整事項 |
| Confirmation | 運用者／発注側との確認結果 |
| Next action / Promote-to | 同上。確認後に本体台帳へ移す |

**参考マイルストン表**はレーダーの補助であり、統合スケジュールの代替ではない。統合は Dependency / Integrated Milestone 側。

---

## Operating rules

1. **仮説と確認を混ぜない** — 初期行は「想定」、確認列が空なら未確定のまま報告する。  
2. **レーダーを本体台帳の影にしない** — 影響がプログラムの開始判定・Hand-off・受入に効くと分かったら Promote-to で移し、レーダー側は「移管済」にする。  
3. **タグ軸を先に決める** — 案件名の増殖より、並行ストリームへの当たり判定を優先する。  
4. **対外は役割で管理する** — 人名は連絡手段。交代しても行が死なないようにする。  
5. **会議の読み合わせ台帳にしない** — 週次は Next action と Promote 候補だけ見る。全文朗読は禁止。

---

## Tests

- Dependency Register に無い遅れで試験／切替が止まったとき、レーダーに先行行があったか  
- 「関連案件は把握している」が、仮説列のない案件名リストになっていないか  
- 確認前の想定を、顧客向け月次の確定事実として書いていないか（Archetype J）  
- Promote-to が空のまま行が増え続けていないか  

---

## Use with

- 共同利用・複数ロットの官側工程管理 → `playbooks/public-multi-lot-construction-pmo.md`  
- 契約内 PJ 間 Hand-off → `playbooks/cross-project-program-management.md`（本パターンの後段）  
- 会議層 → `playbooks/program-governance-cadence.md`  
- 顧客向け物語 → `standards/deliverable-archetypes.md` Archetype J（レーダー全文は載せない）  
- 支援工数の箱 → `knowledge/patterns/support-effort-classification.md`（対外調整は Between / Cross-cutting に置きやすい）

## Related

- `knowledge/patterns/shared-operator-vs-ministry-vs-municipality.md`
- `knowledge/patterns/pgmo-presence-via-client-stance.md`（交点／隣接を広げて Value を出すときの姿勢）
- `frameworks/transformation-pmo.md`
- `knowledge/migrations/related-project-radar-and-et-case-pack-2026-08.md`
