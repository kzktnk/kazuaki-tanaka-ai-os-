---
type: playbook
title: "AI utilization roadmap"
status: active
last_updated: 2026-08-19
related:
  - frameworks/ai-adoption-roadmap.md
  - playbooks/ai-work-before-after.md
  - playbooks/wbs-design.md
---

# AI utilization roadmap

構想をユースケース一覧にせず、**基盤 → 知識化 → 業務高度化**の因果と、直近実行に落とす。 Dual-layer の年次骨格は `frameworks/ai-adoption-roadmap.md`。本ファイルは作業順序とレビューゲート。

## Trigger

- 複数年の AI 活用ロードマップ  
- PoC から本格利用への説明  
- 役員レビュー前の実現性チェック  

## Do not start with

チャットボット／検索／判断支援の一覧。先に「環境変化の中で、どの業務能力を維持・向上するか」。

## Sequence

1. **最終状態** — 誰の仕事が、何を探さず／書かず／迷わず、人に何が残るか。  
2. **介入レベル** — L1 探索 → L2 作成支援 → L3 判断支援 → L4 プロセス → L5 横断。原則この順。  
3. **知識の逆算** — 文書化済みと暗黙知を分ける。暗黙知は独立施策（抽出→構造化→有識者検証→蓄積→参照→利用結果の更新）。AI生成をそのまま正式知識にしない。  
4. **基盤3領域** — 組織・人材／プロセス・ガバナンス／テクノロジ・データ。アプリ開発より基盤だけが先行し過ぎていないか。  
5. **矢印** — 「これがないと次ができない」を言えない箱は削除または再配置。  
6. **年次は状態** — その年の終わりに何が可能か。作業リストにしない。  
7. **直近計画** — 中長期施策をそのまま WBS にしない。タスク名・目的・ゴール・活動。抽象語（伴走、高度化、整備）を具体化する。  

### 実現性6ゲート

| Gate | 問うこと |
|------|----------|
| Who | 主体は業務か CoE か IT か。支援と実行を混ぜない |
| When | 意思決定を含め期間内か。他案件と競合しないか |
| What | タスク名で活動が想像できるか |
| Dependency | データ・ルール・対象業務・システムの順が成立するか |
| Operate | 誰がデータ更新・品質確認・ルール改善するか |
| Measure | 1年後まで測らない設計になっていないか |

クライアントコメントは字面で直さない。誰がやる＝Ownership、間に合う＝Feasibility、具体的に何＝Activity、データは誰が更新＝Operating model。構造の問題を表現だけ直して終わらせない。

### Steering で潰す論点

Why / What / How / Who / When / Dependency / Measure / AIに任せない領域 / 役員に何を決めてもらうか。

スローガンは使命型（何を目指すか）と施策サマリ型（何をどう変えるか）を混ぜない。事業環境 → 使命 → 目指す姿 → 施策 の後に作る。

## Outputs

- Target operating state  
- 施策因果（3層）と年次の状態目標  
- 直近タスク（目的・ゴール付き）  
- 6ゲートの未通過項目  

## Related

- `frameworks/ai-adoption-roadmap.md` (C → B → A, Year 1–5)  
- `playbooks/ai-work-before-after.md`  
- `playbooks/wbs-design.md`  
- `knowledge/patterns/organizational-memory.md`  
