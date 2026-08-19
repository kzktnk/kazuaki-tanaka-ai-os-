# Public Sector & Defense IT Domain

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Parent file for reusable Japan public-sector / defense IT consulting knowledge  
**Does not contain:** ministry or force names, program identifiers, yen, bid prices, system inventories, network designs, personal data, current proposal text

---

## Purpose

省庁・防衛の情報システム案件で毎回ゼロから「この世界の拘束」を説明し直さないための Domain 親ファイル。

- **縦軸（官側ライフサイクル）:** 構想 → 要件 → 調達設計 → 見積精査／選定 → 構築PMO → 運用・情報保証  
- **横軸:** 買手支援か売手提案か。**同じプログラムで混ぜない。**

既存の厚い資産（方式〜要件、ベンダー評価）はここに再掲しない。Domain は **拘束と役割** だけを持つ。

---

## How to use

官側の調査〜要件なら `frameworks/program-phases-investigation-to-requirements.md` を先に読む。  
調達仕様・評価基準・見積精査なら `frameworks/public-it-procurement-support.md`。  
民間と同じ「提案を勝つ」話なら SI / IO / AMS の枠を使い、この Domain で **保全・総合評価・分割調達** だけ足す。

Technology 製品手順は書かない。系統図・機器一覧・拠点数は **原本に残し、リポジトリに入れない。**

---

## Industry structure

### Principle

公共ITは「大きい民間」ではない。少なくとも次が同時に効く。

| 拘束 | 実務への意味 |
|------|----------------|
| 会計・契約 | 単年度、仕様書と対価の対応、変更は契約行為 |
| 総合評価 | 価格点と技術点。適合条件を満たさない提案は採点前に落ちる |
| 公平性 | 官側支援者は特定ベンダーに寄り添わない。精査コメントは全社に同じ土俵 |
| 保全 | 立入、資料持出、情報区分。提案のうまさより先に運用できるか |
| 標準 | 政府のIT標準ガイドライン類は「参考」ではなく工程の骨格になり得る |

防衛は上記の **厳格なインスタンス**（情報保証、訓令、許可された場所での作業）。論理は公共と同じ。固有の系統構成は書かない。

### Common error

民間SIのSolution Planを、官側の調達支援成果物だと思い込む。逆に、官側の公平な精査ロジックを、自社の応札価格作りに流用する。

### Related

- `frameworks/public-it-procurement-support.md`
- `knowledge/patterns/buyer-vs-seller-in-public-procurement.md`
- `standards/vendor-proposal-evaluation.md`
- `frameworks/program-phases-investigation-to-requirements.md`

---

## Engagement types（官側）

材料の主座はローカル原本。リポジトリには **型** のみ。

| 型 | 問うこと | 典型成果 |
|----|----------|----------|
| 次期構想・要件 | 何を残し、何を換装し、方式をどう切るか | 調査研究、方式比較、要件書（Phase 100–500） |
| 調達支援 | 何を買い、どう評価し、仕様をどう書くか | 実施計画、調達方式比較、総合評価基準、仕様・適合条件 |
| 見積精査 | 提案価格は何の作業量か。過不足はどこか | ベースライン、評価基準、ヒアリング、精査報告 |
| 構築PMO | 契約後、官側は何を見て止めるか | 進捗・課題・変更・検収の官側PMO |
| CIO／計画支援 | 横断の優先と予算の言い方 | 短い助言。個別仕様の代筆ではない |

構想と調達仕様は別契約になりやすい。**要件がFIXする前に仕様書を書き始めない**（既存の要件書ゲートと同じ）。

---

## Engagement types（売手）

応札は SI の三角制約と同じ（買える × 届く × 財務）。公共では加えて:

- 評価項目の区分（必須／任意）に提案を **対応づけて** 書く  
- 関連する分割調達（運用、申請、監査など）があるなら、**自社ロットだけ最適化しない**  
- 契約後に対象一覧が確定する前提なら、着手後調査を計画に書く。在庫を捏造しない  
- 社内の Solution Baseline / 提案前レビューは、見積・WBS・役割・検収を tick-and-tie する場（中身の金額は登録しない）

情報保証・RMF 系役務の原則（制度の中身のコピーではない）:

- **認可・リスク判断は官の責任。** 支援は手順、様式、教育、進捗、助言  
- 脆弱性検査を伴う／伴わない分析は別作業として切り、官作業の進捗把握と請負範囲を混同しない  
- 未習熟の担当が本業の傍らで書くなら、選択式・記入要領・ガイドが本体より先に効く  
- マルチベンダーならスケジュールとロットのすり合わせがクリティカルパス  

NIST SP 800-37 / 800-53 等は **参照クラス**。章を転載しない。

---

## Do not mix

- 発電・小売の論理を省OAに持ってこない（逆も）。共通なのは権限・記録・現場例外だけ。  
- 防衛の構築仕様と、RMF制度運用支援は別仕事。システムを「知っている」ことと制度を回すことは同じ提案に雑に載せない。

---

## Related files

| Layer | File |
|-------|------|
| Domain parent | this file |
| Framework | `frameworks/public-it-procurement-support.md` |
| Pattern | `knowledge/patterns/buyer-vs-seller-in-public-procurement.md` |
| Index | `knowledge/index/legacy-source-index.md` Program Line P |
| Migration | `knowledge/migrations/public-defense-2026-08.md` |
