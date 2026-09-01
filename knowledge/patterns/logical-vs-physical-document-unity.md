# Pattern: Logical vs Physical Document Unity

**Status:** Active  
**Origin:** Generalized from a policy discussion on document administration versus generative-AI reference corpora (2026-09). Client names, org units, schedules, and target architecture are **not** stored here.

## Pattern statement

> **生成AIが文書を安全に参照できる状態は、格納場所を1つにすることではない。オーナーシップ・メタデータ・権限・AI利用区分・ライフサイクルが、参照対象全体で一貫していることである。**

物理的な一元管理と、AIから見た論理的な一元管理は別物である。

## Core distinction

### Physical unity

文書を1つのシステム、1つの格納場所に集約する。検索対象が同じ箱に入る。

これだけでは、最新版がどれか、誰が捨ててよいか、AIに渡してよいか、は決まらない。

### Logical unity

格納場所が分かれていても、次が全社（または合意したスコープ）で一貫していれば、AIから見て「一元管理された状態」は実質的に成り立つ。

1. オーナーシップ  
2. 共通のメタデータ・分類  
3. 権限・機密区分の継承  
4. AI利用区分（渡す／渡さない／要約のみ 等）  
5. 最新版管理と、廃止・改訂時の更新  

逆に、箱を1つにしてもガバナンスがなければ、あるべき姿には到達しない。

## Why programs diverge

文書管理プログラムは、しばしば**法令・会計・電子保存**から始まる。生成AIが欲しいのは、技術文書・許認可・運用知など、**参照して判断するためのコーパス**である。求められる特性（保存年限、改ざん防止、検索性、AI利用区分）は同じではない。

したがって、進行中の文書管理システムを「将来のAI参照基盤」と前提にしてよいかは、最初の問いである。現行のAI参照経路（オブジェクトストレージ等）が既にあるなら、その前提を見直す。

`standards/document-management-standard.md` は、開発成果物の**番号・承認・台帳**の標準である。本パターンは、企業内の文書エステートをAIが参照するときの**論理／物理**の切り方である。混ぜない。

## Signals

- 「まず文書を1箇所に集めてからAI」が、未決のまま前提になっている  
- 法令対応の文書管理と、AI参照要件が同じプロジェクトに無批判に載っている  
- 置き場所の製品選定が先で、ガバナンス主体と対象スコープが後回し  
- 格納は統合済みだが、権限・最新版・AI利用区分が部署ごとに違う  
- 検索は当たるが、根拠にできない文書が混ざる（評価は `knowledge/lessons/ai-output-evaluation-terms.md`）

## Design response

置き場所を決める前に、次を合意する。

- **ガバナンス主体:** 誰が基準を確立し、維持するか  
- **対象スコープ:** 一部門か、全社か。投資と体制が変わる  

そのうえで、実装の型はだいたい3つに落ちる。

| 型 | 動き | 使う条件 | 主なリスク |
|---|---|---|---|
| 独立構築 | 現行のAI参照経路で先に進める | 活用時期が先、法令系システムと目的が違う | 独自ルールが固定し、後から全社基準と食い違う |
| 統合待ち | AI要件を文書管理プログラムに載せる | 同じガバナンスで一体運用する必然がある | 目的の違うプロジェクトへのスコープ拡大。活用が止まる |
| 段階移行 | 先行構築し、統合の判断基準とトリガーを先に書く | 短期の利用と中長期の整合を両立させたい | 暫定が本番化する。移行コスト |

物理的な格納の一致は、あるべき姿の**必要条件ではない**。どの型でも、先行する設計に全社へ伸ばせるメタデータと権限モデルを残す。

蓄積だけでは記憶にならない、は `knowledge/patterns/connected-organizational-memory.md`。本パターンは、その前段の「何を正本とし、どの箱に置くか」である。

## Core rule

> Unify governance first. Co-locate stores only when the purpose of the store matches the purpose of the reference.

## Related

- `standards/document-management-standard.md` — SDLC 文書の版・承認・台帳  
- `knowledge/patterns/connected-organizational-memory.md` — 溜めることと繋ぐこと  
- `knowledge/patterns/organizational-memory.md` — 検索と組織記憶  
- `knowledge/lessons/ai-output-evaluation-terms.md` — 根拠のない生成を切る語彙  
- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`  
- `playbooks/rag-structure-diagnosis.md`  
- `playbooks/ai-poc-quality-review.md`  
- `adapters/claude/CLAUDE.md` — Knowledge を Prompt で誤魔化ししない  
