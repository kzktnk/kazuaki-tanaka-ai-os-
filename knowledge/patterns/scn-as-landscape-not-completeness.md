---
type: pattern
---

# Pattern — SCN as Landscape, Not Completeness

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** SCN as Landscape, Not Completeness  
**Applies to:** Engagements that overlay already-running projects onto Value / Capability / Enabler to see adjacency  
**Origin:** Anonymized working session on a running multi-project program (2026-09). Client names, plant names, product names used as identifiers, and transcripts are **not** stored here.

**Does not contain:** operator names, project titles from live packs, org charts, yen, capability-node inventories from a live SCN

---

## Pattern statement

> **SCN の本来の仕事は、戦略を Capability / Enabler に分解し、抜けを見てプロジェクト化することである。すでに走っているプロジェクトで組織が満杯のとき、同じ絵を「MECE 完成度テスト」や「新規立ち上げのエンジン」として使うと、議論が層の定義に吸われる。そのときは配置図として使う：どの既存 PJ がどのノードに紐づきそうか、まで。**

`playbooks/strategy-scn.md` の Gate 1 用途（抜け洗い出し → プロジェクト化）と、本パターンの用途（既存 PJ の俯瞰）は別ジョブである。絵が似ていても、レビュー基準を混ぜない。

| Job | SCN に聞くこと | 聞かないこと |
|-----|----------------|--------------|
| **Gate 1（本来）** | Value に対して Capability / Enabler は足りるか。何をプロジェクトにするか | 走っている PJ の Hand-off 詳細 |
| **Landscape（本パターン）** | 既存 PJ はどのノードに載るか。隣の PJ と線が引けそうか | この Capability をどこまで埋めればゴールか。今から新規 PJ を立てるか |
| **Capability depth（別ジョブ）** | ノードの定義・到達条件・中の課題 | PJ 間の受け渡し |

組織がすでに「お腹いっぱい」なら、抜けを見つけて新規プロジェクト化する話は現実的でないことが多い。仮説は「やりたいことは既存の箱でほぼカバーされている」側に置き、あとの仕事は **箱と箱の間** に移す（`playbooks/cross-project-program-management.md`）。

整理の途中で領域漏れが見えたら、「なさそうなんですけどどうなんですか？」と一度聞く。漏れ探しを本線にしない。

---

## Signals

- SCN の Capability / Enabler が「必要十分か」「どこまで掘るか」で会議が止まっている  
- レビューが MECE・網羅性の採点になっている（今回の仕事が配置図なのに）  
- 個別 PJ がすでに認識している中の課題（ノウハウの定義など）に、支援側が時間を使っている  
- 関係図や課題表の前に、SCN の大きな更新が作業計画のクリティカルパスになっている  

---

## Operating rules

1. **仕事を先に言い切る** — 「抜け洗い出し」か「既存 PJ の配置」か。前者なら Gate 1 のレビュー。後者なら Completeness を採点しない。  
2. **ノードの深さは後回し** — Landscape のときは Enabler 粒度を揃えることより、PJ が載る場所を先に決める。  
3. **中の既知課題に潜らない** — 個別 PJ がすでに持っている課題は、その PJ に返す。間に落ちるものだけを取る。深掘りが要るなら、本線のあとで別枠にする。  
4. **SCN を大きく更新しない** — Landscape として一度置けたら、線と課題表の側へ移る。  

---

## Tests

- 今回の SCN の仕事を、Gate 1 と Landscape のどちらと一文で言えるか  
- Capability の定義深さへのコメントを、PJ 間課題の本線から外しているか  
- 「足りないプロジェクトを立てる」提案を、満杯の実行環境に出していないか  

---

## Use with

- Gate 1 の本線 → `playbooks/strategy-scn.md`、`frameworks/strategic-capability-network.md`  
- 配置のあとの間 → `playbooks/cross-project-program-management.md`、`knowledge/patterns/topology-map-vs-issue-log.md`  
- レビュー → `standards/consulting-review.md`（成果物の仕事を先に名指す）  

## Related

- `standards/scn-creation-guide.md`  
- `knowledge/patterns/related-project-external-coordination-radar.md` — まだ認識されていない隣接案件のレーダー。本パターンは **すでに見えている PJ を SCN に載せる** 側  
- `knowledge/migrations/pj-between-review-viewpoints-2026-09.md`  
