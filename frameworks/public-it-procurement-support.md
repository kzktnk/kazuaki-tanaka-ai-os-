# Public IT Procurement Support Framework

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Generalized from Japan ministry-OA / defense-adjacent buyer-side support (procurement design, estimate scrutiny, construction PMO). No specifications, yen, vendor names, or inventories.

---

## Purpose

官側（発注者）の **調達を設計し、公平に通す** ための枠。調査〜要件（`program-phases-investigation-to-requirements.md`）の **後工程**、またはそれと並行する調達トラック。

売手の Solution Plan ではない。選定の根拠を残し、後の監査とベンダー抗議に耐えることが目的である。

---

## When to Use

- 大規模OA／ネットワーク／情報システムの調達方式と仕様の支援  
- 総合評価基準と適合条件の設計  
- 複数社見積の精査・ヒアリング  
- 構築フェーズの官側プロジェクト管理支援  

売手応札には使わない。`knowledge/patterns/buyer-vs-seller-in-public-procurement.md`。

---

## Lifecycle (buyer)

```text
構想・要件（既存 Phase 100–500）
        ↓ 方式が切れる
調達方式     … 何をどの契約形態で買うか（例: 構築／電借／保守の切り方）
仕様・適合   … 何を満たせば入札できるか（適合）と、何をどう作るか（仕様）
評価基準     … 技術点の見方。ラベルではなく定義
見積精査     … 価格の作業量を、官側ベースラインと突き合わせる
契約・着手
構築PMO     … 進捗・課題・変更・検収。請負の代行ではない
```

**適合条件** は採点の前のゲートである。ここが甘いと評価シートが壊れる。  
**カタログ／機能性能の書き方** は、後の検収で「書いてない／書きすぎ」で争う点なので、記載要領を先に固定する。

政府の標準ガイドライン類は、WBSや成果物品質の **外部拘束** になり得る。社内方法論で上書きしない。

---

## Procurement design

調達方式比較は「安い方式」ではなく、**リスクの所在**（所有、保守年限、換装、運用分担）を切る。

総合評価:

- 価格点と技術点の重みは政策と案件性質で決まる。コンサルタントは **重みの説明責任** を官と共有する  
- 評価項目は `standards/vendor-proposal-evaluation.md` と同じく、根拠付きの枠。偶数段階  
- 領域シートと全体シートの二重採点を避ける  

仕様書（案）は要件書の写しではない。調達できる粒度（検証可能性、除外、インタフェース、運用条件）に落とす。

---

## Estimate scrutiny

提案評価（良さ）と **見積精査（量と単価の妥当）** は別成果物である。

推奨手順:

1. **官側ベースライン** — 作業分解と前提を先に持つ。ベンダー見積を「正解」にしない  
2. **評価基準** — 何をもって過大／過小とするかを書く  
3. **社別ヒアリング** — 同じ質問構造。特定社だけ深掘りしない  
4. **コメント一覧** — 指摘は再利用可能な論点（範囲、前提、工数ドライバ）にする。社名付きの生ファイルはリポジトリに入れない  
5. **評価実施報告** — 判断と残リスク。選定会議が読める長さ  

ヒアリング日程と従事者名簿は運営であり、知識ではない。

---

## Construction-phase PMO (buyer)

官側PMOは、請負の進捗会議の書記ではない。

見るもの: 契約範囲との差分、検収条件、他調達との依存、情報保全、官側作業（承認・接続・データ）の遅れ。  
売手の Delivery Lead 枠（`frameworks/delivery-leadership.md`）を官側にそのまま当てない。成功指標が違う。

共同利用基盤で複数ロットが同時にテスト・移行するときは、進捗の合算ではなく **次工程の開始判定**（計画確認 → 結果確認、受入、本番）が成果になる。手順は `playbooks/public-multi-lot-construction-pmo.md`。運用者／省／団体の混同は `knowledge/patterns/shared-operator-vs-ministry-vs-municipality.md`。

---

## Relationship to other assets

| Asset | Relationship |
|-------|----------------|
| `domains/public-defense.md` | 拘束と役割 |
| `program-phases-investigation-to-requirements.md` | 構想〜要件 |
| `requirements-document-outline.md` | 要件書。仕様書の前 |
| `vendor-proposal-evaluation.md` | 技術評価。精査は価格・工数。民間の選定手順は `private-it-rfp` 側 |
| `frameworks/private-it-rfp.md` | 民間 RFP。法定調達と混ぜない |
| `transformation-pmo.md` | プログラムガバナンスの一般論 |
| `estimate-target-commitment.md` | 売手見積の健全性。官側精査の鏡 |

---

## Do not register from source

- 仕様本文、適合条件の実項目、機器・ソフト一覧  
- 各社見積、円、WBS実数、社内価格ツール  
- 立入証、従事者名簿、契約書、NDA  
- 現行応札の提案本文・社内レビュー資料  

---

## Related files

- `domains/public-defense.md`
- `knowledge/patterns/buyer-vs-seller-in-public-procurement.md`
- `knowledge/migrations/public-defense-2026-08.md`
