---
type: pattern
---

# Pattern — Topology Map vs Issue Log

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Topology Map vs Issue Log  
**Applies to:** Multi-project programs where a relationship diagram is being asked to carry issues, or a hearing is requested before questions are locked  
**Origin:** Anonymized working session on a running multi-project program (2026-09). Client names, plant names, product names used as identifiers, and transcripts are **not** stored here.

**Does not contain:** live issue IDs, filled matrices, hearing questionnaires, org names

---

## Pattern statement

> **関係図が答えるのは「何が繋がっているか」である。課題表が答えるのは「その間のどこが壊れているか」である。図を見て「これで課題を洗い出しきれるのか」と問うのは、図に課す仕事を間違えている。**

課題は PJ の中ではなく **PJ と PJ の間** にある。各 PJ の中の課題は、基本的に各 PJ が解けばよい。間に落ちたものは見落とされるか、お見合いする。そこを取る。

導出される課題の型は、次の5領域で足りる（管理表の名前を覚える必要はない）。

| 領域 | 問い | 課題の例 |
|------|------|----------|
| Boundary | 誰が、どこまでやるか | 「そこは相手の担当」で抜け／重複 |
| Dependency | 何を、いつ、誰から誰に渡すか | 後続が前提にしているアウトプットが、先行ではまだ決まっていない |
| Interface | どう繋ぐか | 連携方式・タイミング・経路の前提が違う |
| Consistency | 内容が一致しているか | 各 PJ では承認済みでも、繋ぐと ID・粒度・定義が合わない |
| Schedule | 全体として期日に間に合うか | 個別計画は順調でも、合算すると間に合わない |

「A のアウトプットを B がインプットとして受け取るには用事が足りない」は Dependency と Consistency の境目に出やすい。カテゴリを先に完璧にしなくてよい。行を先に書く。

線が増えて図が読みにくくなったら、線は残し、**線ごとに何が流れるか**は別表にする。その表が Dependency Register である。

---

## Question first, hearing second

情報収集の順序を逆にしない。

```text
① 各 PJ ペア × 5領域で「何を確認したいか」を書く
② 窓口に見せ、「これは答えられる／これは個別確認が要る」と仕分けてもらう
③ ヒアリングか、質問票か、窓口回答か、を決める
```

「各 PJ にヒアリングさせてください」は、①②の前に出す依頼ではない。深さは「どこまで掘りたいか」で決まる。PJ 間の依存レベルなら、既存情報で大半が足りることがある。システム連携設計の整合まで掘るなら、質問が先に要る。

マトリクス（PJ × PJ の関連あり／課題がありそう）は、深掘り対象の特定用である。セルを埋めることが成果ではない。1行でもよいから、型が見えるまで1組を埋めてから横展開する。

---

## Signals

- 関係図の矢印に課題番号が載り、因果が読めないと指摘されている  
- 課題一覧が無い、または図の脚注だけになっている  
- ヒアリング依頼が、確認したい問いより先に出ている  
- 5領域のどれに当たるかより、SCN ノード名で課題を分類している  
- 個別 PJ 内の進捗・Risk・ノウハウ定義が、間の課題と同じ表に混ざっている  

---

## Operating rules

1. **図は位相、表は課題** — 図のゴールはつながりまで。課題は一覧表。  
2. **間を取る** — 各 PJ の既知課題に潜らない。お見合い・抜け・受け渡し不足を取る。  
3. **質問を先に固定する** — 方法（ヒアリング／票／窓口回答）は後。  
4. **1組で型を見せる** — 全 PJ を同時に埋めない。フォーマットに1組入れてから広げる。  
5. **「ここはまだわからない」を残す** — 未確認を確定口調にしない。  

---

## Tests

- 関係図を外しても、課題表だけで Between-PJ の論点が残るか  
- 矢印ごとに「何が流れるか」が図または別表にあるか  
- ヒアリング依頼文に、確認したい問いが先に並んでいるか  
- 窓口が「答えられる／要個別」を仕分けできる粒度になっているか  

---

## Use with

- 管理表の本体 → `playbooks/cross-project-program-management.md` Chapter 2–6  
- SCN を配置図として使ったあと → `knowledge/patterns/scn-as-landscape-not-completeness.md`  
- まだ認識されていない隣接案件 → `knowledge/patterns/related-project-external-coordination-radar.md`  
- レビュー → `standards/consulting-review.md`  

## Related

- `knowledge/patterns/unowned-work-in-effort-analysis.md` — 間に落ちた仕事の別断面  
- `knowledge/migrations/pj-between-review-viewpoints-2026-09.md`  
