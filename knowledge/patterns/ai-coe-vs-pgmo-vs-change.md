---
type: pattern
---

# Pattern — AI CoE vs PgMO vs Change

**Version:** v0.1  
**Status:** Active  
**Type:** Knowledge pattern  
**Owner:** Kazuaki Tanaka  
**Pattern name:** AI CoE vs PgMO vs Change  
**Applies to:** AI CoE design, AI program office, AI change, offering that bundles the three

---

## Pattern

> **AI の専門家集団、活用の司令塔、現場定着の支援は別機能である。比重は企画 → 導入 → 運用で移る。三つを一つの「AI PMO」に畳むと、PoC の QCD だけが残る。**

| Function | Job | Typical failure if missing |
|----------|-----|----------------------------|
| **CoE** | 標準・基盤・ガバナンス・人材のプール。サイロと重複開発を止める | 部門ごとに道具とルールが分岐する |
| **PgMO** | 戦略との整合、施策間依存、成果の森。木（個別 PJ の QCD）ではない | PoC が並び、ROI も本番計画も無い |
| **Change** | 行動と感情。利用率・責任分界・倫理の説明。導入完了後も続く | 影のツール利用、過剰期待、定着しない |

企画では CoE と PgMO が厚い（目指す姿、テーマ、技術アセス、ガバナンス）。導入では PgMO が厚い（進捗・成果・チーム間）。運用では Change が厚い（利用モニタ、追加訓練、文化）。CoE のガバナンス運用は全フェーズに残る。

## CoE shape over time

人が少ないうちは **中央の専門組織** に集める。成熟したら育成した人を主管部へ戻し、CoE は全社テーマと高難度に残る（**ハイブリッド**）。最初から分散 SME だけだと経営から効果が見えない。中央のまま戻さないと主管部が他人事のまま。

## AI program is not project control

部門 PoC がバラバラなら、先に戦略（北極星）が無いかを見る。無ければプログラム定義の前に戦略を短く固定する。成果物の型は、戦略／プログラム定義／フェーズ完了状態／依存／効果の集約、であり、個別 WBS の合算ではない。

## AI change is not ERP change

ERP は要件が閉じ、導入後は安定運用が主。AI はモデルと使われ方が導入後も変わる。役割は「人が使い方を決める道具」ではなく、判断・推論への介入と責任分界が要る。リスクは QCD に加え、バイアス・説明・データ誤用・評価制度のずれ。Change は伝え方・訓練に加え、倫理と継続変化の設計になる。

PoC 疲れの典型は、導入そのものが目的、本番計画が無い、精度 100 点を現場に要求する。意図的設計は Why、本番までの道、人とループで不足分を補う前提。

## Headwinds (design, not pep talk)

惰性（小さく始めて慣らす）、労力と茫漠（作業を簡単にしロードマップを見せる）、感情・脅威（個別会話と共同デザイン）、心理的反発（自分事と **通常の指揮命令系統**）。初期は少人数で骨子、早い段階でラインに落とす。プロジェクト広報だけで数千人は動かない。

## Signals

- 「AI PMO を置けば CoE も Change も足りる」  
- CoE がインフラ票だけを持ち、優先順位と倫理を持たない  
- PgMO が個別 PoC の進捗会議になっている  
- Change がキックオフ資料と e-learning  
- 影の生成 AI を禁止ポスターだけで止めようとする  

## Underlying mechanism

技術・施策・人は時間軸が違う。一つの事務局に三つを足すと、測定しやすい QCD に吸い寄せられる。

## Implications

オファリングと社内設計は三つを分け、フェーズで厚みを変える。`frameworks/ai-management-office.md` は CoE の器、`frameworks/transformation-pmo.md` はプログラム層、`frameworks/change-management.md` は人側。本パターンはその接続。

## Exceptions

- 単一部門の閉じた実験で、全社標準もポートフォリオも要らない  
- すでにハイブリッド CoE とプログラム層が切れずに回っている  

## Do not

- ベンダーの CoE カタログ、成熟度診断製品、統計％、事例社名、連絡先を登録する  
- コッター段階を百科事典として転載する  
