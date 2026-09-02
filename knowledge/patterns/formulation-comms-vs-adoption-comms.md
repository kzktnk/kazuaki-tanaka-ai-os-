---
type: pattern
---

# Pattern — Formulation Comms vs Adoption Comms

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** Formulation Comms vs Adoption Comms  
**Applies to:** Change-management plans that sit next to a roadmap being written, not only next to a design already locked  
**Origin:** Anonymized working session on a running multi-project program (2026-09). Client names, plant names, people, and transcripts are **not** stored here.

**Does not contain:** stakeholder maps with names, sample org catalogues, channel calendars, branded field-team labels as a method to copy

---

## Pattern statement

> **コミュニケーション計画は一つに見えて、仕事が二つある。（1）関係者をめざす状態に動かす（定着）。（2）ロードマップを作るために場を使う（策定：要件・ユースケース・キック条件）。混ぜると、名簿と目指す姿のサンプルが先に埋まり、キックできる条件が後回しになる。**

定着の計画は `frameworks/change-management.md` と `knowledge/patterns/change-agent-vs-communication-plan.md` の射程である。本パターンは、**まだ中身が無い施策を、現場と本社で具体化するためのコミュニケーション**を、定着コミュニケーションから切る。

主線が策定なら、ステークホルダーの目指す状態は必要条件ではあるが、成果物の主語ではない。主語は「誰と、何を、どこまで決めれば次に着手できるか」である。

---

## Kickable requirements before a field team

クイック検証のために現場へ人を送る話が出たとき、先に固定するのはチームの呼び名ではない。

| 先に決める | 後でよい |
|------------|----------|
| 何が揃えば現場が始められるか（権限、対象業務、データの有無、止められる範囲） | チームの愛称、理想の一人二役人材 |
| 大きい投資案件の巻き込みと、現場で回すクイック検証を、同じ計画に載せるか分けるか | 年間カレンダーの全文 |
| 1ヶ月でどちらを優先するか | 両方を同じ粒度で並べたサンプル名簿 |

業界に「一人で前さばきから実装までできる人」はほぼいない。送り込むなら、業務をやれる人と実装側をセットにする前提で、キック条件を書く。理想人材が置けるなら「送り込むだけ」で足りる、という設計は使わない。

---

## Signals

- コミュニケーション目的が「巻き込み」だけで、施策の中身を決める場になっていない  
- ステークホルダー一覧・組織文化のサンプルが、キック条件より先に厚い  
- 投資委員会案件の計画と、現場クイック検証の計画が、一つの成果物に無自覚に混ざっている  
- 「FDE 的なチームを送る」が要件になっていて、何が揃えばキックできるかが空欄  

---

## Operating rules

1. **二つの仕事を名指す** — 定着か、策定か。両方やるなら成果物を分けるか、主線を一つにする。  
2. **キック条件から書く** — 現場派遣・クイック検証があるなら、先に「始められる条件」。  
3. **サンプルはサンプルのまま** — 名簿の型は、計画の骨格のあと。  
4. **本社だけで足りる話は本社で閉じる** — 現場が主体の施策にだけ、現場を入れる場を設計する。  

---

## Tests

- コミュニケーション計画の一文が、目指す状態への移動か、ロードマップ策定の場か、どちらか言い切れるか  
- 現場チーム派遣の前に、キックできる条件が書かれているか  
- 大きい投資案件とクイック検証を、同じ月次計画に無自覚に載せていないか  

---

## Use with

- 組織層の定着 → `frameworks/change-management.md`  
- エージェント探索との混同 → `knowledge/patterns/change-agent-vs-communication-plan.md`  
- 特定の人を動かす → `playbooks/stakeholder-activation-playbook.md`  
- レビュー → `standards/consulting-review.md`  

## Related

- `knowledge/patterns/who-vs-lever-family.md`  
- `knowledge/migrations/pj-between-review-viewpoints-2026-09.md`  
