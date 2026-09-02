# Legacy Source Index

**Version:** v1.22  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** ローカル保管のレガシー原本と、リポジトリ内知識の対応索引。**原本の中身は含まない。**

**Related:** 全体マップ → [`master-index.md`](./master-index.md)

---

## Important

- 本索引は**パスと抽出先の対応**のみ記録
- クライアント名・ベンダー名・評価点数は記載しない
- 原本は GitHub に**コミットしない**（`core/identity.md` Confidentiality Boundary）
- ローカルパスはユーザー環境依存。必要に応じて更新

---

## Program Line A: 大規模ERP/RFP（2002–2003）

原本ファイル名と案件文書番号は索引に書かない。抽出先は本リポジトリの知識ファイル。

| 原本の種別 | 抽出先（リポジトリ） |
|-----------|---------------------|
| 提案書 | `deliverable-archetypes.md` Archetype A |
| 最終報告 | `author-voice-archetypes-legacy.md` Archetype 7（報告系） |
| 一次評価結果 | `vendor-proposal-evaluation.md`, Archetype B |
| 二次評価報告 | `vendor-proposal-evaluation.md` §Evaluation Process |
| SteerComm 資料 | `deliverable-archetypes.md` Archetype C |
| 評価設計議事 | `vendor-proposal-evaluation.md`（全章）、`scoring-vs-calibration.md` |
| 提案評価シート | `vendor-proposal-evaluation.md` 二層・枠定義。点数・社名は不登録 |
| PM面接チェック | `vendor-key-person-interview.md`。人名は不登録 |
| RFP本文 | **未登録**（機密）。構造は `frameworks/private-it-rfp.md`。Appendix Map のみ `requirements-document-outline.md` |
| 業務 Appendix | `requirements-document-outline.md` §AC category |
| 連携 Appendix | `requirements-document-outline.md` §IF category |
| 帳票 Appendix | `requirements-document-outline.md` §BS category |
| 基盤 Appendix | `requirements-document-outline.md` §ST category |
| 開発標準要求（RFP別添） | Program Line H 相互参照 |
| Appendix 索引 | `requirements-document-outline.md` §RFP Appendix Category Map |

---

## Program Line H: 開発標準（2003/12）

原本ファイル名と案件文書番号は索引に書かない。様式 ID は `standards/document-id-registry.md` が払い出す。

| 原本の種別 | 抽出先（リポジトリ） |
|-----------|---------------------|
| 開発標準の位置づけ | `development-standards-framework.md` |
| 開発標準目次 | 本索引（Program Line H） |
| ドキュメント分類図 | **未登録**（抽出困難）。`document-management-standard.md` §Document Types |
| 開発管理ガイドライン 管理概要 | `development-management-guide.md` §Overview（Phase 3） |
| 開発管理ガイドライン 管理本編 | `development-management-guide.md`（全章） |
| カスタム開発手順 | `deliverable-archetypes.md` Archetype G |
| 成果物様式目次 | 同上。ID は `AIOS-BLD-*` |
| パッケージ手順（PS/SAP） | **未登録**（パッケージ固有） |
| 記録類様式 | **未登録**（実様式）。用途は `AIOS-REC-*` |
| 設計様式 | **未登録**（実様式）。用途は `AIOS-BLD-*` |
| 文書管理・作成基準 | `document-management-standard.md` |
| 文書区分 | `document-management-standard.md` §Document Types |
| 表紙・台帳様式 | **未登録**（実様式）。用途は `AIOS-COV-*` |
| 環境管理 | `environment-management-guide.md` |
| 運用設計 | `operations-design-guide.md` |
| 運用引継 | `operations-handover-guide.md` |
| 命名・コード規約 | **未登録**（クライアント固有ID）。`development-standards-framework.md` §規約系 |
| リリース管理 | `release-management-guide.md` |
| 維持/UI/DB/技法 | **未登録**（索引のみ） |

**Note:** 原本はローカルのみ。クライアント名・担当者名・原本の文書番号・実様式はリポジトリに登録しない。Program Line A の開発標準要求（RFP別添）の**履行成果**が本 Line。

**Downloads 直下の別名フォルダ（同一パック）:** `ドキュメント標準` / `運用設計ガイドライン` / `開発環境／試験環境ガイドライン` / `運用引継ガイドライン` / `開発規約` / `開発管理ガイドライン` は上記と同じ financial-institution IT standards / legacy development standards pack のコピー配置。抽出先は変更なし（差分抽出なし）。`運用設計ガイドライン/` 内に運用引継ファイルが混在する場合あり — 索引上は種別で読む。

---

## Program Line X: 業界システム監査指針＋技術／運用／設備基準（〜2002–2003）

匿名ラベル: **financial-institution IT standards / legacy development standards pack**（監査・安全対策側）。銀行名・チェック行本文・円・人名は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 業界「金融機関等のシステム監査指針」改訂版（`.xls`） | `knowledge/patterns/fis-system-audit-as-assurance.md` | 様式メタ（要点→リスク→コントロール→CP）、buyer/assurance の使い方、開発・運用・設備への投影。**チェックポイント行・小項目本文は未登録** |
| 技術基準_v1.doc | `standards/development-standards-framework.md` §三基準レイヤ | 大分類のみ（災害障害／故意過失／監査機能）。項番本文未登録 |
| 運用基準_v1.doc | 同上 | 大分類のみ（体制・入退・運用・開発変更・設備管理・教育・委託・監査）。項番本文未登録 |
| 設備基準_v1.doc | 同上 | 大分類のみ（建物・電算室・電空・電源・空調・監視・回線）。項番本文未登録 |

**Note:** 原本は `Downloads/` 直下。業界指針は著作権・再配布に注意。リポジトリは**判断とカテゴリ骨格**のみ。公共防衛の情報保証とは別（`domains/public-defense.md`）。

---

## Program Line I: SAP Implementation Phase Model

| 原本の種別 | 抽出先（リポジトリ） | 登録範囲 |
|-----------|---------------------|---------|
| クライアント向け方法論概説 | `frameworks/sap-implementation-phase-model.md` | Phase 0–6、Activity Group、試験体系、WBS/WP概念（一般化のみ） |
| 内部研修（構想フェーズのテーラリング） | 同上 §Tailoring Principle | 構想フェーズ前提と実案件の差異・応用適用 |
| 内部研修（重複分） | **未登録** | 索引のみ |

**Note:** 原本はローカルのみ。Task ID・Work Product 番号・サンプル様式・Route Map 詳細・提案書事例はリポジトリに**登録しない**。ベンダー商標・クライアント名は一般化。

---

## Program Line J: Application Outsourcing / AMS（~2015）

| 原本の種別 | 抽出先（リポジトリ） | 登録範囲 |
|-----------|---------------------|---------|
| コース Day1 | `frameworks/application-outsourcing-solution-planning.md` | Course Map、SA 役割、As-Is/To-Be（一般化のみ） |
| コース Day2 | 同上 + `frameworks/service-transition-approach.md` | Risk、Estimating、Sourcing、Pyramid、Transition 概念 |
| コース Day3 | 同上 | Solution model、レビューゲート（ツール固有名除外） |
| Services Pyramid テンプレ | `frameworks/ams-services-pyramid.md` | L1/L2/L3 階層モデルのみ |
| Pyramid 事例 | 同上 + `application-outsourcing-solution-planning.md` | Solution Plan TOC のみ |
| SAP 案件概説（AM 文脈） | `sap-implementation-phase-model.md` 参照 | Post-go-live AM 文脈（1段落相当） |
| ロケーション販促資料 | **未登録** | マルチロケーション原則のみ（`ao-solution-planning` §Location） |
| To-Be 事例 | `application-outsourcing-solution-planning.md` | To-Be 構成要素のみ |
| Estimating 事例 | `application-outsourcing-solution-planning.md` §Estimating | 因子名のみ（FTE/時間数除外） |
| Sourcing 事例 | 同上 §Location Strategy | ロケーション決定軸のみ |
| Pyramid ミックス事例 | 同上 §Pyramid | 概念のみ |
| Transition Approach | `frameworks/service-transition-approach.md` | 原則・WS・マイルストーン型 |
| Solution Plan チェックリスト | `standards/ams-solution-plan-checklist.md` | 全章（一般化） |
| 提案骨子 | `standards/deliverable-archetypes.md` Archetype I | 章立てのみ |

**Note:** 原本はローカルのみ。社内秘・再配布禁止。クライアント事例名・FTE・コスト・拠点・人名・社内ツール名・レートカードはリポジトリに**登録しない**。

---

## Program Line M: Infrastructure Outsourcing SA（Intermediate / Advanced, ~2014–2016）

原本はローカルのみ。社内秘。ケース企業・原価ツール・レートカードは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Intermediate Day1 — SA role, qualification, requirements, detailed solution, transformation | `infrastructure-outsourcing-solution-planning.md`, `transition-vs-transformation-vs-realization.md` | 三角制約、Lead/tower SA、Read/Ask/Assume/DD、To-Be 完了条件、T vs T vs R |
| Intermediate Day2 — SLA, CFS, security, suppliers, discretionary, CI, PMO/SDM | 同上 | 手数料リスクの型、CFS 想定、Run vs project、PMO に SDM を混ぜない |
| Intermediate Day3 — multi-tower, risk, mobilization, TPA, financials | 同上 | ESA、動員、価格形態、ARC/RRC、インフレ/FX の存在 |
| Intermediate Day4 — price-to-win, response, orals, DD, negotiation, contracting, implementation | 同上 | 契約と承認解の双方向、DD 種別、口頭提案の型 |
| Intermediate ケース（架空 RFP） | **未登録** | 演習ケース |
| 原価ブック / Workbench | **未登録** | ツール・マスタ |
| Inflation / Currency 解説 ppt | 同上 § commercials | リスク分担の考え方のみ。数値・社内ポリシー番号は不登録 |
| Advanced — transformational IO, modeling, network/DC, third party, SLA, pricing, realization | 同上 | as-is vs transformed-only、prime/sub vs ops mgmt、realization は署名後も SA |
| Advanced クライアントケース、RFP、SOW、Orals | **未登録** | 実名・契約原本 |
| SA Certification Guide / 認定プレイブック | **未登録** | 社内認定 |

**Note:** 社内秘・再配布禁止。個人メールは索引にも載せない。

---

## Program Line N: Systems Integration SA / SI Delivery Lead（~FY16）

原本はローカルのみ。社内秘。ケース RFP・契約改訂・認定ツールは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| SI SA Day1–2 / Prep | `systems-integration-solution-planning.md`, `estimate-target-commitment.md` | 見積≠目標≠約束、Solution Plan 質問、ブループリント、Vモデル、2種コンティンジェンシー、tick-and-tie |
| SI Delivery Lead Day1–2 | `delivery-leadership.md` | SA→DL、契約 vs 期待、ODE/EAC、動員、変更管理 |
| Solution Plan / Blueprint / ケース RFP・契約 | **未登録** | クライアント演習・実契約 |
| ロジスティクス、認定ガイド | **未登録** | |

---

## Program Line O: Delivery Management training（~2014–2015）

原本はローカルのみ。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| マルチタワー・プログラム配信講義 | `delivery-leadership.md` | プロジェクト vs プログラム、価値スコアカード、リリース、期待管理、商業ライフサイクル |
| サービス管理モジュール | `delivery-leadership.md`, `transition-vs-transformation-vs-realization.md` | Introduction vs Transition、Warranty≠運用 |
| ケースメモ、レッスン学び発表 | **未登録** | ケース |
| ブランド方法論・アイスブレイク | **未登録** | |
| 個人テンプレ実ファイル | **未登録** | 様式 |

---

## Program Line K: Utility retail customer systems（CIS / CRM / CDP / CC / CX, 2022–2024）

原本はローカル Downloads。クライアント名・金額・製品名は書かない。抽出は一般化済み Domain / 標準 / パターンのみ。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| ポータル分科会セッション資料 | `experience-before-scope.md`, `domains/energy-utilities.md` §Retail | 体験→機能→業務→データ→範囲。機能一覧は不登録 |
| 重要顧客定義・ポータルニーズ検討 | `energy-utilities.md` §Retail | KGI/CSF/KPI の罠のみ |
| 料金予測アルゴリズム検討 | **未登録**（手法詳細） | 索引のみ |
| 現行業務調査・新業務一覧 / フロー | `energy-utilities.md` §Retail | As-Is 鳥瞰の必要性のみ。業務実名は不登録 |
| CDP 要求・定例・活用提案 | `platform-build-vs-enablement.md`, `energy-utilities.md` | 構築と利用の分離問題 |
| CDP 要件成果物の確認観点 | `standards/requirements-artifact-review.md` | 8観点（固有要件文は不登録） |
| 分析 PoC・データ課題、DR / キャンペーン分析報告 | `energy-utilities.md` §Data | 効果の前にデータ課題 |
| ロイヤルティ / LTV / ポイント会計 | `energy-utilities.md` §CX | 商品設計と会計制約。仕訳・按分実数は不登録 |
| 次期コンタクトセンター役員資料・費用対効果 | `energy-utilities.md` §Operating model | 継続性 vs 変革2軸。金額は不登録 |
| CX 立ち上げ・組織配置仮説 | `energy-utilities.md` §Operating model | 分析チームだけでは足りない |
| システム構築と利用教育の関係 | `platform-build-vs-enablement.md` | 教育をツール講習で終わらせない |
| CIS / CRM 工程完了・ステコミ・経営会議 | `deliverable-archetypes.md` C、索引のみ | ゲート報告の型。予実は不登録 |
| 30分値・シミュレーション過渡期 | `energy-utilities.md` §Retail | やる／やらない／暫定を先に切る |
| ヒアリングメモ、個人名セッション、Q&A 原表 | **未登録** | 機密 |

**Note:** 定例会資料（CDP 第10回以降など）は索引1行で足りる。中身の議事進行は登録しない。

---

## Program Line L: Change Management training（legacy Strategic Change / LPD CM, ~2001–2003）

原本は `Downloads/CM/Day1`, `Day2`。OLE `.ppt`。日本語本文はバイナリからほぼ復元不能。英語構造のみ一般化。ケース企業・性格診断アイスブレイクは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Change Readiness | `frameworks/change-management.md` §1 | ワークショップ成果、多次元レディネス、history/readiness/risk の区別 |
| Change Readiness case exercise | **未登録** | クライアント調査ケース |
| Change Strategy (Day1/Day2 重複) | `change-management.md` §2, `all-at-once-vs-stepwise-change.md` | all-at-once vs stepwise; 反復サイクル |
| LPD CM 本編 | `change-management.md` §3 | コミットメント、抵抗、移管 |
| LPD CM 添付 | `change-management.md` §3 | ステークホルダー行動ログ、時系列メッセージ、コミュニケーション1枚 |
| Summary / 2日目アジェンダ | 索引のみ | |
| 「4つの選択」アイスブレイク | **未登録** | 性格クイズ。CM方法論ではない |

---

## Program Line B: 公共OA刷新（2009）

| ローカル原本（例） | フェーズ | 抽出先（リポジトリ） |
|-------------------|---------|---------------------|
| `100…/実施計画書（省OA）_*.doc` | 100 | `program-phases-investigation-to-requirements.md` Phase 100 |
| `100…/01.官側要求事項_*.ppt` | 100 | Phase 100 |
| `100…/02.実施計画概要_*.ppt` | 100 | Phase 100, `deliverable-archetypes.md` |
| `300…/課題抽出、改善案のまとめ_*.ppt` | 300 | Archetype 4, `deliverable-archetypes.md` Archetype D |
| `300…/問題抽出表_*.xls` | 300 | `deliverable-archetypes.md` §問題抽出表 |
| `300…/換装時期の検討_*.ppt` | 320 | Phase 300 |
| `400…/次期省OA全体方式について_*.ppt` | 410 | Archetype 5, `deliverable-archetypes.md` Archetype E |
| `400…/メール及びウェブの流れ等_*.ppt` | 410 | Phase 410 詳細例 |
| `400…/全体方式案：各案評価シート_*.xls` | 410 | `vendor-proposal-evaluation.md`, Archetype E |
| `400…/次期省OA要件定義書（案）_*.doc` | 420 | `requirements-document-outline.md`（全章） |
| `400…/要件定義書ポンチ絵.ppt` | 420 | `deliverable-archetypes.md` |
| `400…/(別添)SLAについて_*.xls` | 420別添 | `requirements-document-outline.md` §Appendices |
| `500…/MODNW調査研究報告書_*.doc` | 500 | Phase 500 |
| `500…/調査研究報告会資料_*.ppt` | 500 | `deliverable-archetypes.md` Archetype F |

**Note:** 調査〜要件の骨格。調達仕様・見積精査の型は Program Line P。

---

## Program Line P: 公共／防衛IT 調達・精査・PMO・情報保証役務（〜2015、一部 2023 型）

原本はローカル Downloads。府省名・系統・円・現行提案本文は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 省OA調達支援（実施計画、調達方式、評価基準、仕様案） | `public-it-procurement-support.md`, `public-defense.md` | 官側調達ライフサイクル。仕様本文・適合実項目は不登録 |
| 次期構想／要件検討（調査〜報告書） | 既存 Line B と同一骨格 | 索引のみ。新規フェーズは作らない |
| 見積精査（ベースライン、ヒアリング、報告） | `public-it-procurement-support.md` §Estimate scrutiny | 手順のみ。各社見積・円は不登録 |
| 構築PMO支援役務（仕様案・社内見積ツール） | `public-it-procurement-support.md` §Construction PMO | 官側PMOの見るもの。金額ツール不登録 |
| 情報保証・RMF 関連の公示／応札／社内レビュー | `public-defense.md` §売手、`buyer-vs-seller-in-public-procurement.md` | 官の認可責任、分割ロット、未習熟負担。件数・予算・提案本文不登録 |
| 立入証、名簿、NDA、契約、機器一覧 | **未登録** | 機密 |

---

## Program Line Q: Azure 企業閉域 API チェーン／個人 Sandbox 課金（2026-08）

原本はローカル Downloads。ホスト・円・請求・リソース名は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 閉域 API チェーン検証の引継ぎ・判断記録 | `technology/azure-enterprise.md`, `playbooks/private-api-connectivity-diagnosis.md`, `knowledge/decisions/diagnose-from-gateway-not-client-error.md` | 通信チェーン、gateway 診断、環境切替。FQDN・ポート実値・path は不登録 |
| 個人 Azure 学習 Sandbox の検証・課金対応記録 | `technology/azure-enterprise.md`, `playbooks/azure-sandbox-cost-guard.md`, `knowledge/decisions/sandbox-cost-controls-before-resources.md` | 実行場所と認証、Budget、削除≠課金停止。円・請求書・サポート文・RG 名は不登録 |

---

## Program Line R: AI 変革プレイブック群（2026-08）

原本はローカル Downloads。事業者名・KPI実数・FQDNカタログは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 現場向け Before / After | `playbooks/ai-work-before-after.md` | 工程対称、人の判断残置。部門実例は不登録 |
| AI活用ロードマップ／部門方針 playbook | `playbooks/ai-utilization-roadmap.md` | 基盤→知識→高度化、6ゲート。年次実タスクは不登録 |
| AI PoC・ベンダー検証計画レビュー | `playbooks/ai-poc-quality-review.md`, `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md` | 発注者側品質。スコア実値不登録 |
| 変革オファリングレビュー | `playbooks/offering-review.md` | To-Be≠仕組み≠PMO≠CM。社内ブランド主張不登録 |
| Responsible AI 適用 | `playbooks/responsible-ai-assessment.md` | 確認順と証跡。原則カタログ転載なし |
| RAG 表データ品質 | `playbooks/rag-structure-diagnosis.md` | 検索≠構造。報告書の数値例不登録 |
| 閉域暫定接続の抽出 | `playbooks/interim-connectivity.md`, `knowledge/decisions/interim-connectivity-is-not-the-target.md` | 暫定≠本命。製品FQDNリスト不登録 |

---

## Program Line S: 多年民間／公共隣接案件（2013–2023、一般化のみ）

原本はローカル Downloads。社名・円・仕様・人名・現行入札本文は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 製造業 ERP／改革の PMO 立ち上げ資料 | `playbooks/pmo-function-standup.md`, `knowledge/patterns/hybrid-talent-in-transformation.md` | 規定が目次止まり、パイロット先行、知識×発想×行動。期番号・育成件数は不登録 |
| 公共・研究機関の DX グランドデザイン成果 | `frameworks/dx-grand-design.md` | 理解差・リソース評価・人事慣行の複合。機関名・人名不登録 |
| 法人営業 WF 改革提案（失注） | `knowledge/patterns/sales-capacity-via-center-functions.md` | センター機能と β 先行。失注事情・社名不登録 |
| 新規デバイス事業性／技術アセス | `frameworks/new-venture-three-track-assessment.md` | 市場シナリオ×技術×自社適合。製品仕様・他社インタビュー不登録 |
| 収益認識／オファリング／価格・購買 WS | `knowledge/patterns/borrowed-operating-model-must-fit.md` | 事業モデル差。会計数値・参照他社フロー実体は不登録 |
| 多年：戦略→実行→CX→コスト→人事→文化→システム→購買 | `knowledge/patterns/multi-year-transformation-sequence.md` | 順序と「遅延≠経営情報」。地域・原価比不登録 |
| リスク管理枠組みの制度運用支援（申請・計画）公告・提案・要員計画 | **未登録** | 現行入札。`domains/public-defense.md` の原則のみ既存 |
| 動画（`.qt`） | **未登録** | メディア。判断の一般化対象外 |

---

## Program Line T: PgMO / AI CoE / Change の役割分担（2026 手法＋2016–2018 計画の型）

原本はローカル。パイプライン金額、社名、計画本文、組織図、人名は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 2026 PgMO & Change 8枚（パイプライン／案件矢印） | **未登録** | 手法ではない。TCV・アカウント名を知識にしない |
| 2026 AI CoE / AI PgMO / AI Change 方法ノート | `knowledge/patterns/ai-coe-vs-pgmo-vs-change.md`, `frameworks/ai-management-office.md` | 三機能、フェーズ比重、中央→ハイブリッド、AI CM≠ERP。統計％・事例名・連絡先不登録 |
| 規制産業の変革推進計画（2016、本文） | `frameworks/change-management.md` §4 | 計画の位置づけとサイクルのみ。本文・組織・人数不登録 |
| CM 手法概要＋検討会設計（2018） | 同上 §4 | 層×フェーズ課題、受容度目標つきセッション、指揮系統。適用先社名・分刻み表不登録 |

---

## Program Line U: 地方公共団体の共同利用IT運用者／複数ロット工程管理（2022、一般化のみ）

原本はローカル。フォルダ名は識別子のため索引に書かない。匿名ラベル: **local-government shared IT operator / 2022**。団体名、円、仕様、提案本文、系統図、手順本文、名簿、契約IDは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 工程管理役務の公示一式（説明書、仕様、総合評価、契約案、様式） | **未登録**（手続の型は既存 Line P） | 仕様・評価実項目・契約案は不登録。`public-it-procurement-support.md` を増殖しない |
| 応札提案（表紙・目次・本文、前回提案） | **未登録** | 提案本文。評価項目対応の書き方は既存の売手原則のみ |
| 支援実施計画（工程管理の見る範囲） | `playbooks/public-multi-lot-construction-pmo.md`, `public-defense.md` | 進捗・品質・開始判定・運用準備・関連案件。WBS実体・体制人名不登録 |
| 開始判定・品質（計画確認／結果確認） | 同上 Playbook | ゲートの型のみ。試験実数・成績不登録 |
| 運用手順・操作手順のマージ、構成変更台帳 | 同上。引継の一般型は既存 `operations-handover-guide.md` | 目次とマージが成果。本文・機器操作は不登録 |
| 統合構成・設計書・環境表・セキュリティ範囲図 | **未登録** | 系統・在庫。Domain の「原本に残す」ルール |
| 執行部向け見解資料 | 高度を分ける、の判断のみ Playbook | 製品リスクの中身不登録 |
| 関連案件把握・対外調整支援テンプレート（`.xlsx`） | `knowledge/patterns/related-project-external-coordination-radar.md` | シート種別と列ジョブのみ。実データ・人名不登録 |
| 共同利用プログラム経験の社内 MM 共有デッキ（`.pptx`） | **抽出スキップ**（重複） | 横断工程・対外調整・切替政治は既存 Line U / W / Z / CM。索引のみ |

---

## Program Line AA: Enterprise Transformation 実践事例パッケージ骨格（2019、一般化のみ）

原本はローカル。匿名ラベル: **enterprise transformation case pack 2019**。事例ストーリー、クライアント識別子、人名、円、連絡先は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 2019 ET Monthly Meeting 事例パッケージ（`.pptx`） | `knowledge/patterns/transformation-practice-case-pack.md` | パック構成、ロール×案件タイプ行列、テーマカード欄。事例本文・固有名詞不登録 |

**未登録:** 各テーマの生ストーリー、参考文献の詳細書誌の写し、コンタクト先。

---

## Program Line V: プログラム運営リズム／Phase 1 事務局立ち上げ文書クラス（2026、一般化のみ）

原本はローカル。匿名ラベル: **multi-project program office cadence / 2026**。社名、円、議事本文、人名、組織図、KPI 実績、現場名、現行プログラム事実は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Phase 1 立ち上げ準備（管理／会議／作業／個人ワーク） | `playbooks/program-governance-cadence.md` | 文書クラスと会議階層。方針・ロードマップ・会議パックの**型**のみ |
| ステコミ | 同上。資料の型は既存 Archetype C | 層のジョブと全体会議との分離。議事・実スライド不登録 |
| プログラム全体会議 | 同上 | プログラム統合の場。本文不登録 |
| プロジェクト間調整会議 | 同上 | イベント駆動の依存解消。対象プロジェクト実名不登録 |
| プロジェクト定例会議 | 同上 | 週次（決定がなければ書面可）。実パック・議事不登録 |
| プロジェクト検査 | 同上 | 進捗と別の保証層。チェックシート実記入・結果不登録 |
| 管理文書（仕様、計画、受領、提案、要員、納品） | 同上（クラスのみ） | 管理対象の目次。本文・提案・要員計画は**未登録** |

**未登録（現行エンゲージメント）:** 議事録本文、検査結果、実管理文書本文。

---

## Program Line W: 複数ベンダー横断 PgMO 指導（2026、一般化のみ）

原本はローカル `Downloads/`。匿名ラベル: **multi-vendor cross-project PgMO coaching / 2026**。社名、円、契約事実、実プログラム事実は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Cross-Project Management Playbook（md / docx **v2.1**／2026-08-29 系列揃え） | `playbooks/cross-project-program-management.md` | PJ 間 5 領域、Control Cycle、Gate 2→Gate 3 引き渡し（Register / Matrix / RAID）、Health Assessment、①②③＋横串。2026-08-29 再採用（repo **v0.9.1**：図は位相／質問先行） |
| Templates.xlsx（Cover + 8 シート） | 同上 Playbook 本文 / Appendix | テンプレート**クラスとフィールド**のみ。xlsx 実体不登録 |
| SelfStudy（md / docx） | `playbooks/cross-project-program-management-selfstudy.md` | 本編と同一の型・表・演習。語りを二人称に。docx 不登録 |

**未登録:** xlsx / docx ファイル本体（main・SelfStudy）、作成日・対象読者などの表紙メタ、著者個人の全体レビュー記入欄・改訂履歴ダンプ、演習ケースのベンダー名・日付・費用、部下の実プログラム。

---

## Program Line AC: 運用移行・定着化指導（2026、一般化のみ）

原本はローカル `Downloads/20260829_1227/`・`Downloads/20260829_1309/`（docx）。匿名ラベル: **operations transition / AMS–IO–AI ops coaching / 2026**。社名、円、契約事実は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Operations Transition Playbook（md / docx） | `playbooks/operations-transition-playbook.md` | Transition Manager 一人称。シナリオA/B、Gate 3〜5、Core vs Experimental（Ch 5・6）。YAML・仮称・著者レビューダンプは除外。2026-08-29 再採用（repo **v0.2**） |
| SelfStudy（md / docx） | `playbooks/operations-transition-playbook-selfstudy.md` | 本編と同一。語りを二人称に。本文から repo パスを外した版。docx 不登録 |
| Templates.xlsx | 同上 Appendix | クラスのみ。xlsx は未作成／不登録 |

**未登録:** docx、xlsx、`ai-operations-role-design.md`（Draft・未レビュー）。

---

## Program Line AD: Stakeholder Activation 指導（2026、一般化のみ）

原本はローカル `Downloads/20260829_1227/`・`Downloads/20260829_1309/`（docx）。匿名ラベル: **stakeholder activation coaching / 2026**。人名付きマップは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Stakeholder Activation Playbook（md / docx） | `playbooks/stakeholder-activation-playbook.md` | 横串。Segment→Diagnose→Select→Tailor→Observe。YAML・草案メモ除外。2026-08-29 再採用（repo **v0.2**） |
| Templates.xlsx（Cover + 6） | 同上 Appendix | クラスのみ。xlsx 不登録 |
| SelfStudy（md / docx） | `playbooks/stakeholder-activation-playbook-selfstudy.md` | 本編と同一。語りを二人称に。docx 不登録 |

**未登録:** xlsx / docx、人名付きマップ。

---

## Program Line Y: 匿名レガシー大規模SI提案のプロジェクト管理方針章（一般化のみ）

原本はローカル `Downloads/` のみ。匿名ラベル: **requirements-to-cash style program / project management policy chapter**。Q2C は製品ラベルとして扱い、クライアント名・円・人名・組織図・RACI 実名・WBS ID・スケジュール実績は不登録。PPTX は git に入れない。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 提案／方針デッキ「プロジェクト管理方針」章（〜11枚） | `knowledge/patterns/project-management-policy-layer.md` | TOC、PJ vs プログラム境界、進捗測度、課題／リスク／ToDo、変更×QCD／ベースライン。表・実績・会議曜日・ツール名は不登録 |
| 同上 → 開発管理との接続 | `standards/development-management-guide.md`（方針境界節） | 監督5領域との差分確認のみ |
| 同上 → PMO／cadence | `standards/pmo-operating-guide.md`, `playbooks/program-governance-cadence.md` | ポインタ。会議階層の再定義はしない |

**未登録:** スライドダンプ、EVM数値例、製品・リモートツール節、失敗原因リストの全文。

---

## Program Line Z: 顧客向け週次／月次ステータス指導（2026-08-24、一般化のみ）

原本はローカル録音（2026-08-24）。匿名ラベル: **customer-facing weekly/monthly status coaching / 2026-08-24**。**内容（音声・文字起こし）はリポジトリにアーカイブしない。** 社名、円、人名、日程・稼働数字、生トランスクリプトは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| コーチング録音（週次／月次報告レビュー） | `standards/deliverable-archetypes.md` Archetype J | 週次 vs 月次の役割、問題ポートフォリオ物語、内側の評価枠、完了条件、表現衛生。固有事実なし |
| 同上 | `knowledge/patterns/project-management-policy-layer.md` | 顧客共有の未決・完了条件・不確定の可視化 |
| 同上 | `core/author-voice.md` §6 | 骨格＋口頭補足、「解決」語、不用意なオペ処方 |
| 同上 | `frameworks/top-down-thinking.md` | フレームは道具／実務から軸／抜け＝構造未完 |
| 同上 | `knowledge/patterns/support-effort-classification.md` | 個別／PJ間／横断＋課題管理 |
| 同上（相互参照のみ） | `playbooks/program-governance-cadence.md`, `playbooks/cross-project-program-management.md` | 薄いポインタ。本文改稿なし |

**未登録:** 録音・文字起こし全文、クライアント／メンティー固有の案件事実。

---

## Program Line AB: 複数ベンダー PgMO プレゼンス指導（Slack、2026、一般化のみ）

原本はローカル `.rtf` のみ。匿名ラベル: **mentor–mentee Slack coaching / multi-vendor PgMO presence / 2026**。**スレッド全文はリポジトリにアーカイブしない。** 社名、円、人名、プログラム識別子、生 RTF は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Mentor–mentee Slack スレッド（PgMO プレゼンス／打ち手） | `knowledge/patterns/pgmo-presence-via-client-stance.md` | クライアント側 PM／PO 姿勢、既存信頼者との同盟構図、交点リスク→状態→月次→週次逆算。固有事実なし |
| 同上 → 関連案件の広げ方 | `knowledge/patterns/related-project-external-coordination-radar.md` | 相互参照のみ（本スレッドでは新規型なし） |
| 同上 vs Line Z（週次／月次報告） | — | **別トピック**（重複抽出なし）。報告の見せ方は Line Z |

**未登録:** RTF／スレッド全文、ハンドル、人名、クライアント／案件識別子、ベンダー入替噂の事実化、社交 Tips。

---

## Program Line AE: 月次付録／チェンジ／工数／発注側ギャップ指導（2026-08-28、一般化のみ）

原本はローカル録音（2026-08-28）。匿名ラベル: **customer-facing monthly appendix / change artefacts / effort sketch / buyer-side gap coaching / 2026-08-28**。**内容（音声・文字起こし）はリポジトリにアーカイブしない。** 社名、円、人名、日程・稼働数字、生トランスクリプトは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| コーチング録音（月次付録・チェンジ成果物） | `knowledge/patterns/change-agent-vs-communication-plan.md` | エージェント探索 ≠ コミュニケーション計画。計画骨格が先、サンプルはサンプル。固有事実なし |
| 同上 → 現状工数の構造化 | `knowledge/patterns/unowned-work-in-effort-analysis.md` | 人紐づき PDC の漏れ、検討主体→実行／管理、アクチュアル ≠ WBS 再設計 |
| 同上 → 次フェーズ体制 | `knowledge/patterns/buyer-side-gap-vs-vendor-pmo.md` | 開発側 PMO ≠ 発注側ハザマ。継続 ≠ 増分価値。月次で経路リスク |
| 同上 → 月次衛生 | `standards/deliverable-archetypes.md` Archetype J | サンプル衛生、説明用 Appendix、選定印の基準、議題外の頭出し、稀頻度案件の火種 |
| 同上 | `knowledge/patterns/project-management-policy-layer.md` | 選定印・入れ子 vs 独立は基準がギロになる |
| 同上 | `frameworks/change-management.md` | エージェント vs 計画；計画が先 |
| 同上 | `frameworks/top-down-thinking.md` | 人軸の箱では未割当が漏れる |
| 同上 | `core/author-voice.md` §6 | サンプル衛生、並行ワークストリームの頭出し |
| 同上（相互参照のみ） | `playbooks/stakeholder-activation-playbook.md`, `playbooks/cross-project-program-management.md` | 薄いポインタ。本文改稿なし |

**未登録:** 録音・文字起こし全文、クライアント／メンティー固有の案件事実、出張・承認・私事、社内 B&P 手続き。

**Line Z / AB との差:** Line Z は週次／月次の物語（Archetype J の骨格）。Line AB はプレゼンスの構図。本ラインは付録・チェンジ計画の順序、工数構造の漏れ、発注側隙間。

---

## Program Line G: IT Strategy Foundations (legacy consulting, 2002)

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `Module1_final_20020417.pdf` | コース概要・5要素・Insight/Architecture/Investment | `frameworks/it-strategy-foundations.md` |
| `ITS_ModuleII_Revised.pdf` | シナリオ・プランニング・BSA・ITオプション | `frameworks/it-strategy-foundations.md` §Formulation, `standards/it-strategy-engagement-guide.md` |
| `Module3_final_20020416.pdf` | IATOアーキテクチャ・ギャップ・ガバナンス | `frameworks/it-strategy-foundations.md` §Architecture |
| `Module4_final.pdf` | ソーシング（英語） | `frameworks/it-strategy-foundations.md` §Sourcing, `standards/it-strategy-engagement-guide.md` §Sourcing |
| `Module5_final.pdf` | 導入計画・プログラム管理・BSC | `frameworks/it-strategy-foundations.md` §Implementation, `standards/it-strategy-engagement-guide.md` |
| `Module6_補足資料.pdf` | 価値分析・FCF/NPV/MVA | `frameworks/it-strategy-foundations.md` §Value, `standards/it-strategy-engagement-guide.md` §Value |

**Note:** 原本は `IT_Strategy_Foundation/` 配下。講師紹介・クライアント事例・PwC固有情報はリポジトリに登録しない。

---

## Program Line F: COS Tools & Techniques (legacy consulting strategy, 2001)

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `Sec01 Course Overview COS T&T.pdf` | エンゲージメント全体像 | `frameworks/consulting-strategy-process.md` |
| `Sec02 Defining the Problem COS T&T.pdf` | 4Cs & 1Q | `standards/strategy-engagement-guide.md` §Problem scoping |
| `Sec03 Structuring the Problem COS T&T.pdf` | ロジックツリー・MECE | `frameworks/consulting-strategy-process.md`, `standards/strategy-engagement-guide.md` |
| `Sec04 Developing the Approach COS T&T.pdf` | ア分析計画・ストーリーボード | `standards/strategy-engagement-guide.md` §Plan the approach |
| `Sec05 Strategy Analysis COS T&T.pdf` | 戦略分析・ツール群 | `frameworks/consulting-strategy-process.md` §Solve, `standards/strategy-engagement-guide.md` §Toolkit |
| `Sec06 Data gathering.pdf` | データ収集・インタビュー | `standards/strategy-engagement-guide.md` §Data gathering |
| `Sec07 Scenario Envisioning.pdf` | シナリオ構想 | `frameworks/consulting-strategy-process.md` §Scenario, `standards/strategy-engagement-guide.md` §Scenario |
| `Sec08 Solutions Identification COS T&T.pdf` | 意思決定基準・オプション評価 | `frameworks/consulting-strategy-process.md` §Solutions, `standards/strategy-engagement-guide.md` §Solutions |

**Note:** 原本は `COS T&T 011212/` 配下。クライアント事例・ベンダー名・PwC固有情報はリポジトリに登録しない。Sec05–08 は日英混在PDF。

---

## Program Line E: PMO Training（legacy consulting, 2003）

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `0. Introduction PMO_Ver3.0.pdf` | 研修構成・目的 | `legacy-source-index.md`（索引のみ） |
| `1. What_s PMO_Ver2.0.pdf` | 変革PMO方法論中核 | `frameworks/transformation-pmo.md` |
| `PMO LPD 20030403(Save).pdf` | pmo/PMO・実装・5か条 | `standards/pmo-operating-guide.md`, `knowledge/lessons/pmo-professional-principles.md` |

**Note:** 旧 `.ppt` は日本語抽出不可。PDF版を原本とする。事例・講師名・製品比較表はリポジトリに登録しない。

---

## Program Line D: SCN Training（IBM legacy, 2003–2005）＋ Strategy-SCN coaching（2026）

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `SCN概要(KM).pdf` | 概要・定義・KOPT・KPI・事例 | `frameworks/strategic-capability-network.md` |
| `SCN作成についての補足資料-SCN作成の勘どころ　-.pdf` | 作成勘どころ・As-Is/To-Be・広がり/深さ | `standards/scn-creation-guide.md` §Breadth/Depth, §Workflow |
| `SCN作成のポイント.pdf` | 記述ルール・WS運営・Q&A | `standards/scn-creation-guide.md` §Notation, §Prerequisites |
| `Strategy-SCN-Playbook.docx`／`strategy-scn.md`（2026-08-29） | 戦略→SCN→Gate 1、Gate 1〜5 図、通し演習 | `playbooks/strategy-scn.md`（repo **v0.3.1**／Landscape 用途を失敗例に追加） |
| `strategy-scn-selfstudy.md`／docx | 自己学習版 | `playbooks/strategy-scn-selfstudy.md`（repo **v0.3.1**） |
| `Strategy-SCN-Playbook-Templates.xlsx` | テンプレ9クラス＋Optional | 同上 Appendix（フィールドのみ；xlsx 不登録） |

**Note:** 旧 `.ppt` は日本語抽出不可。PDF版を原本とする。研修元・クライアント名・事例・円・演習 Data Pack 全文はリポジトリには一般化のみ／不登録。Strategy-SCN 原本はローカルのみ。

---

## Extraction Status

| 知識ファイル | 優先度 | 状態 |
|-------------|--------|------|
| `vendor-proposal-evaluation.md` | 高 | ✅ 登録済（2026-08-19 v1.1） |
| `private-it-rfp.md` | 高 | ✅ 登録済（2026-08-19） |
| `vendor-delivery-model-gap-analysis.md` | 中 | ✅ 登録済（2026-08-19） |
| `private-it-rfp-vendor-selection.md` | 高 | ✅ 登録済（2026-08-19） |
| `vendor-key-person-interview.md` | 高 | ✅ 登録済（2026-08-19） |
| `scoring-vs-calibration.md` | 中 | ✅ 登録済（2026-08-19） |
| `reproposal-as-uncertainty-reduction.md` | 中 | ✅ 登録済（2026-08-19） |
| `program-phases-investigation-to-requirements.md` | 高 | ✅ 登録済 |
| `author-voice-archetypes-legacy.md` | 高 | ✅ 登録済 |
| `deliverable-archetypes.md` | 中 | ✅ 登録済（Archetype G 2026-08-13；Archetype J 2026-08-25） |
| `project-management-policy-layer.md` | 高 | ✅ 登録済（2026-08-20；顧客共有未決節 2026-08-25） |
| `support-effort-classification.md` | 中 | ✅ 登録済（2026-08-25） |
| `pgmo-presence-via-client-stance.md` | 中 | ✅ 登録済（2026-08-26） |
| `requirements-document-outline.md` | 中 | ✅ 登録済 |
| `legacy-source-index.md` | 中 | ✅ 本ファイル |
| `strategic-capability-network.md` | 高 | ✅ 登録済 |
| `scn-creation-guide.md` | 高 | ✅ 登録済 |
| `transformation-pmo.md` | 高 | ✅ 登録済 |
| `pmo-operating-guide.md` | 高 | ✅ 登録済 |
| `pmo-professional-principles.md` | 中 | ✅ 登録済 |
| `consulting-strategy-process.md` | 高 | ✅ 登録済 |
| `strategy-engagement-guide.md` | 高 | ✅ 登録済 |
| `it-strategy-foundations.md` | 高 | ✅ 登録済 |
| `it-strategy-engagement-guide.md` | 高 | ✅ 登録済 |
| `development-standards-framework.md` | 高 | ✅ 登録済（2026-08-13）、v1.1 三基準レイヤ（2026-08-20） |
| `document-management-standard.md` | 高 | ✅ 登録済（2026-08-13） |
| `development-management-guide.md` | 高 | ✅ 登録済（2026-08-13） |
| `operations-design-guide.md` | 中 | ✅ 登録済（2026-08-13） |
| `operations-handover-guide.md` | 中 | ✅ 登録済（2026-08-13） |
| `environment-management-guide.md` | 低 | ✅ 登録済（2026-08-13） |
| `release-management-guide.md` | 中 | ✅ 登録済（2026-08-13） |
| `fis-system-audit-as-assurance.md` | 中 | ✅ 登録済（2026-08-20） |
| `sap-implementation-phase-model.md` | 中 | ✅ 登録済（2026-08-14） |
| `domains/energy-utilities.md` | 高 | ✅ 登録済（2026-08-19） |
| `requirements-artifact-review.md` | 高 | ✅ 登録済（2026-08-19） |
| `experience-before-scope.md` | 中 | ✅ 登録済（2026-08-19） |
| `platform-build-vs-enablement.md` | 中 | ✅ 登録済（2026-08-19） |
| `change-management.md` | 高 | ✅ 登録済（2026-08-19）、v1.1 計画の型（2026-08-20） |
| `all-at-once-vs-stepwise-change.md` | 中 | ✅ 登録済（2026-08-19） |
| `infrastructure-outsourcing-solution-planning.md` | 高 | ✅ 登録済（2026-08-19） |
| `transition-vs-transformation-vs-realization.md` | 中 | ✅ 登録済（2026-08-19） |
| `systems-integration-solution-planning.md` | 高 | ✅ 登録済（2026-08-19） |
| `delivery-leadership.md` | 高 | ✅ 登録済（2026-08-19） |
| `estimate-target-commitment.md` | 中 | ✅ 登録済（2026-08-19） |
| `public-defense.md` | 高 | ✅ 登録済（2026-08-19） |
| `public-it-procurement-support.md` | 高 | ✅ 登録済（2026-08-19） |
| `buyer-vs-seller-in-public-procurement.md` | 中 | ✅ 登録済（2026-08-19） |
| `azure-enterprise.md` | 高 | ✅ 登録済（2026-08-19） |
| `private-api-connectivity-diagnosis.md` | 高 | ✅ 登録済（2026-08-19） |
| `azure-sandbox-cost-guard.md` | 中 | ✅ 登録済（2026-08-19） |
| `diagnose-from-gateway-not-client-error.md` | 中 | ✅ 登録済（2026-08-19） |
| `sandbox-cost-controls-before-resources.md` | 中 | ✅ 登録済（2026-08-19） |
| `ai-work-before-after.md` | 高 | ✅ 登録済（2026-08-19） |
| `ai-utilization-roadmap.md` | 高 | ✅ 登録済（2026-08-19） |
| `ai-poc-quality-review.md` | 高 | ✅ 登録済（2026-08-19） |
| `offering-review.md` | 中 | ✅ 登録済（2026-08-19） |
| `responsible-ai-assessment.md` | 高 | ✅ 登録済（2026-08-19） |
| `rag-structure-diagnosis.md` | 中 | ✅ 登録済（2026-08-19） |
| `interim-connectivity.md` | 中 | ✅ 登録済（2026-08-19） |
| `interim-connectivity-is-not-the-target.md` | 中 | ✅ 登録済（2026-08-19） |
| `buyer-owns-ai-poc-ground-truth.md` | 中 | ✅ 登録済（2026-08-19） |
| `pmo-function-standup.md` | 高 | ✅ 登録済（2026-08-20） |
| `dx-grand-design.md` | 高 | ✅ 登録済（2026-08-20） |
| `new-venture-three-track-assessment.md` | 中 | ✅ 登録済（2026-08-20） |
| `hybrid-talent-in-transformation.md` | 中 | ✅ 登録済（2026-08-20） |
| `borrowed-operating-model-must-fit.md` | 中 | ✅ 登録済（2026-08-20） |
| `multi-year-transformation-sequence.md` | 高 | ✅ 登録済（2026-08-20） |
| `sales-capacity-via-center-functions.md` | 中 | ✅ 登録済（2026-08-20） |
| `ai-coe-vs-pgmo-vs-change.md` | 高 | ✅ 登録済（2026-08-20） |
| `shared-operator-vs-ministry-vs-municipality.md` | 高 | ✅ 登録済（2026-08-20） |
| `public-multi-lot-construction-pmo.md` | 高 | ✅ 登録済（2026-08-20） |
| `program-governance-cadence.md` | 高 | ✅ 登録済（2026-08-20） |
| `cross-project-program-management.md` | 高 | ✅ 登録済（2026-08-29 / v2.1 → repo v0.9.1） |
| `cross-project-program-management-selfstudy.md` | 高 | ✅ 登録済（2026-08-29 / ②自己学習 → repo v0.9.1） |
| `strategy-scn.md` | 高 | ✅ 登録済（2026-08-29 / Gate 1〜5・通し演習 → repo v0.3.1） |
| `strategy-scn-selfstudy.md` | 高 | ✅ 登録済（2026-08-29 / ①自己学習 → repo v0.3.1） |
| `operations-transition-playbook.md` | 高 | ✅ 登録済（2026-08-29 / ③ → repo v0.2） |
| `operations-transition-playbook-selfstudy.md` | 高 | ✅ 登録済（2026-08-29 / ③自己学習 → repo v0.2） |
| `stakeholder-activation-playbook.md` | 高 | ✅ 登録済（2026-08-29 / 横串 → repo v0.2） |
| `stakeholder-activation-playbook-selfstudy.md` | 高 | ✅ 登録済（2026-08-29 / 横串自己学習 → repo v0.2） |

---

## Program Line AF: 稼働中マルチ PJ の配置図／課題表（2026-09、一般化のみ）

原本はローカル週次パック（事前資料・wrap-up・議事）。匿名ラベル: **running multi-project landscape / between-PJ issues / 2026-09**。社名、発電所名、製品名を識別子として使ったもの、議事本文、録音は不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| 週次検討会の wrap-up・口頭補足 | `knowledge/patterns/scn-as-landscape-not-completeness.md` | SCN を配置図として使う。MECE・新規立ち上げではない |
| 同上 | `knowledge/patterns/topology-map-vs-issue-log.md` | 図は位相、表は課題。質問先行。5領域は②既存 |
| 同上（チェンマネ論点） | `knowledge/patterns/formulation-comms-vs-adoption-comms.md` | 策定の場 vs 定着の場。キック条件が先 |
| レビュー／思考の型 | `standards/consulting-review.md`、`core/author-voice.md` | 成果物の仕事を先に名指す |

**未登録:** 事前デック、wrap-up 本体、議事録、録音、記入済みマトリクス、ヒアリング票。

---

## Future Extraction (Optional)

以下はローカル原本からの**追加抽出候補**。自動化または手動レビューが必要。

| 候補 | 方法 | 出力先案 |
|------|------|---------|
| 提案書 v4.5 の章立て | LibreOffice/PPT→txt | `deliverable-archetypes.md` 精緻化 |
| 各案評価シートの評価軸一覧 | xlrd | `vendor-proposal-evaluation.md` 付録 |
| 200/900 フォルダ成果物 | ユーザー提供時 | Phase 200/900 詳細 |
| 開発管理本編 `.doc` 本文 | LibreOffice/PDF→txt | `development-management-guide.md` ✅ |
| 開発成果物様式目次 | 抽出済み | `deliverable-archetypes.md` Archetype G ✅ |

---

## Related Assets

| ファイル | 関係 |
|---------|------|
| `core/identity.md` | 機密境界 |
| `knowledge/lessons/author-voice-archetypes-legacy.md` | アーキタイプ定義 |
| `CONTEXT_ROUTING.md` | タスク別読込 |

---

## Maintenance

- 新規原本をローカルに追加したら、本索引に1行追加（中身は書かない）
- リポジトリ知識を更新したら「抽出先」列を更新
- パス変更時は Program Line 表のみ修正
