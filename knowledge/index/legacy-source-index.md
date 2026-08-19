# Legacy Source Index

**Version:** v1.12  
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

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `020829_提案書_全般_v4.5.ppt` | 提案書 | `deliverable-archetypes.md` Archetype A |
| `20020809最終報告_ver12(1).ppt` | 最終報告 | `author-voice-archetypes-legacy.md` Archetype 7（報告系） |
| `RP20030602-01_…(一次評価)結果.ppt` | 評価結果 | `vendor-proposal-evaluation.md`, Archetype B |
| `wk20030624-06_…(二次評価)報告.ppt` | 評価報告 | `vendor-proposal-evaluation.md` §Evaluation Process |
| `RP20030625-04_第4回SteeComm資料.ppt` | SteerComm | `deliverable-archetypes.md` Archetype C |
| `MM20030514-01_評価シートチェック.doc` | 評価設計議事 | `vendor-proposal-evaluation.md`（全章）、`scoring-vs-calibration.md` |
| `WK20030515-04_開発会社提案評価シート.xls` | 評価シート | `vendor-proposal-evaluation.md` 二層・枠定義。点数・社名は不登録 |
| `WK20030605-04_PM面接チェックシート.xls` | PM面接 | `vendor-key-person-interview.md`。人名は不登録 |
| `RFP/RFP/RFP結合版-取引会計*.doc` | RFP本文 | **未登録**（機密）。構造は `frameworks/private-it-rfp.md`。Appendix Map のみ `requirements-document-outline.md` |
| `RFP/RFP/RFP結合版-人事*.doc` | RFP本文 | **未登録**（機密） |
| `RFP/Appendices/AP_AC*.ppt/xls` | 業務Appendix | `requirements-document-outline.md` §AC category |
| `RFP/Appendices/AP_IF*.xls` | 連携Appendix | `requirements-document-outline.md` §IF category |
| `RFP/Appendices/AP_BS*.xls` | 帳票Appendix | `requirements-document-outline.md` §BS category |
| `RFP/Appendices/AP_ST*.ppt/xls` | 基盤Appendix | `requirements-document-outline.md` §ST category |
| `RFP/Appendices/AP_ST002_開発標準要件定義書.xls` | 開発標準要求 | Program Line H 相互参照 |
| `RFP/Appendices/Appendices_Index.xls` | 索引 | `requirements-document-outline.md` §RFP Appendix Category Map |

---

## Program Line H: 開発標準（2003/12）

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `20031219/開発標準の位置づけ.doc` | 全体位置づけ | `development-standards-framework.md` |
| `20031219/開発標準目次.xls` | 目次 | 本索引（Program Line H） |
| `20031219/ドキュメント分類.ppt` | 文書分類図 | **未登録**（`.ppt` 抽出困難）。`document-management-standard.md` §Document Types |
| `20031219/開発管理ガイドライン/01Z0C-第１編…` | 管理概要 | `development-management-guide.md` §Overview（Phase 3） |
| `20031219/開発管理ガイドライン/02Z0C-第２編…` | 管理本編 | `development-management-guide.md`（全章） |
| `20031219/開発管理ガイドライン/02Z0C-第２編　管理本編.pdf` | 管理本編（PDF原本） | 同上 |
| `20031219/開発管理ガイドライン/03Z0C-第３編…` | カスタム手順 | `deliverable-archetypes.md` Archetype G |
| `20031219/…/02_カスタム開発手順編様式/様式目次.doc` | C様式索引 | 同上 |
| `20031219/開発管理ガイドライン/04–05Z0C-*` | PS/SAP手順 | **未登録**（パッケージ固有） |
| `20031219/開発管理ガイドライン/…/Z0C-様式-M*.xls/doc` | 管理様式 | **未登録**（実様式）。`document-management-standard.md` §Form Archetypes |
| `20031219/開発管理ガイドライン/…/Z0C-様式-C*.xls/vsd` | 設計様式 | **未登録**（Phase 4 索引予定） |
| `20031219/ドキュメント標準/01Z0C-…` | 文書管理・作成基準 | `document-management-standard.md` |
| `20031219/ドキュメント標準/02Z0C-付録1-1　文書区分.doc` | 文書区分 | `document-management-standard.md` §Document Types |
| `20031219/ドキュメント標準/…/Z0C-様式-D101–D104` | 表紙・台帳様式 | **未登録**（実様式）。`document-management-standard.md` §Form Archetypes |
| `20031219/開発環境／試験環境ガイドライン/01–02Z0C-*` | 環境管理 | `environment-management-guide.md` |
| `20031219/運用設計ガイドライン/01Z0C-…` | 運用設計 | `operations-design-guide.md` |
| `20031219/運用引継ガイドライン/01Z0C-…` | 運用引継 | `operations-handover-guide.md` |
| `20031219/開発規約/第１–２編` | 命名・コード | **未登録**（クライアント固有ID）。`development-standards-framework.md` §規約系 |
| `20031219/開発規約/第３編` | リリース管理 | `release-management-guide.md` |
| `20031219/開発規約/第４–９編` | 維持/UI/DB/技法 | **未登録**（索引のみ） |

**Note:** 原本は `Downloads/20031219/` 配下。クライアント名・担当者名・Z0C文書番号・実様式はリポジトリに登録しない。Program Line A の RFP 開発標準要求（AP_ST002）の**履行成果**が本 Line。

---

## Program Line I: SAP Implementation Phase Model（Ascendant SAP）

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） | 登録範囲 |
|-------------------|------|---------------------|---------|
| `Downloads/AsendantSAP/ascendantsap overview_ver3_0.pdf` | クライアント向け方法論概説 | `frameworks/sap-implementation-phase-model.md` | Phase 0–6、Activity Group、試験体系、WBS/WP概念（一般化のみ） |
| `Downloads/AsendantSAP/AscendantTraining_for_ChinaGDC_Day1PM_v0.2.pdf` | 内部研修 | 同上 §Tailoring Principle | 構想フェーズ前提と実案件の差異・応用適用（p6相当） |
| `Downloads/AsendantSAP/AscendantTraining_for_ChinaGDC_Day1AM_v0.2.pdf` | 内部研修 | **未登録** | 索引のみ（比喩・Team Building・overview と重複） |
| `Downloads/AsendantSAP/AscendantTraining_for_ChinaGDC_Day2AM_v0.2.pdf` | 内部研修 | **未登録** | 索引のみ（P3 は overview と重複） |
| `Downloads/AsendantSAP/AscendantTraining_for_ChinaGDC_Day2PM_v0.2.pdf` | 内部研修 | **未登録** | 索引のみ（P4–6 は overview と重複） |

**Note:** 原本は `Downloads/AsendantSAP/` 配下。Task ID・Work Product 番号・サンプル様式・Route Map 詳細・提案書事例はリポジトリに**登録しない**。ベンダー商標・クライアント名は一般化。

---

## Program Line J: Application Outsourcing SAE (AOSAE, ~2015)

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） | 登録範囲 |
|-------------------|------|---------------------|---------|
| `Downloads/AO Materials/Day 1/D1_AOSAE.pdf` | コース Day1 | `frameworks/application-outsourcing-solution-planning.md` | Course Map、SA 役割、As-Is/To-Be（一般化のみ） |
| `Downloads/AO Materials/Day 2/D2 00_AOSAE.pdf` | コース Day2 | 同上 + `frameworks/service-transition-approach.md` | Risk、Estimating、Sourcing、Pyramid、Transition 概念 |
| `Downloads/AO Materials/Day 3/D3.00_AOSAE.pdf` | コース Day3 | 同上 | Solution model、レビューゲート（ツール固有名除外） |
| `D1.01_INP_Services Pyramid Template.pdf` | テンプレ | `frameworks/ams-services-pyramid.md` | L1/L2/L3 階層モデルのみ |
| `D1.04_SS_Services Pyramid.pdf` | 事例 SS | 同上 + `application-outsourcing-solution-planning.md` | Solution Plan TOC のみ |
| `D1.10_SAP Project Overview 2015.pdf` | 事例背景 | `sap-implementation-phase-model.md` 参照 | Post-go-live AM 文脈（1段落相当） |
| `D1.15_INP_GDN OnePagers SM.pdf` | マーケ | **未登録** | マルチロケーション原則のみ（`ao-solution-planning` §Location） |
| `D1.16_SS_To Be Mode.pdf` | 事例 SS | `application-outsourcing-solution-planning.md` | To-Be 構成要素のみ |
| `D2.05_SS_… Estimating.pdf` | 事例 SS | `application-outsourcing-solution-planning.md` §Estimating | 因子名のみ（FTE/時間数除外） |
| `D2.06_SS_… Sourcing.pdf` | 事例 SS | 同上 §Location Strategy | ロケーション決定軸のみ |
| `D2.09_SS_… Pyramids CT_EP Mix.pdf` | 事例 SS | 同上 §Pyramid | 概念のみ |
| `D2.11_… Transition Approach v1.pdf` | 事例 | `frameworks/service-transition-approach.md` | 原則・WS・マイルストーン型 |
| `D3.02_INP_Solution Plan and Assumptions Checklist.pdf` | チェックリスト | `standards/ams-solution-plan-checklist.md` | 全章（一般化） |
| `D3.04_INP_… High Level Proposal Outline.pdf` | 骨子 | `standards/deliverable-archetypes.md` Archetype I | 章立てのみ |

**Note:** 原本は `Downloads/AO Materials/` 配下。Accenture 社内秘・再配布禁止。クライアント事例名・FTE・コスト・拠点・人名・社内ツール名（Alpha/CDTS/CTA）・レートカードはリポジトリに**登録しない**。

---

## Program Line M: Infrastructure Outsourcing SA（IO SA Intermediate / Advanced, ~2014–2016）

原本は `Downloads/IOSA/`, `Downloads/IOSA_Advanced/`。社内秘。ケース企業・原価ツール・レートカードは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| Intermediate Day1 — SA role, qualification, requirements, detailed solution, transformation | `infrastructure-outsourcing-solution-planning.md`, `transition-vs-transformation-vs-realization.md` | 三角制約、Lead/tower SA、Read/Ask/Assume/DD、To-Be 完了条件、T vs T vs R |
| Intermediate Day2 — SLA, CFS, security, suppliers, discretionary, CI, PMO/SDM | 同上 | 手数料リスクの型、CFS 想定、Run vs project、PMO に SDM を混ぜない |
| Intermediate Day3 — multi-tower, risk, mobilization, TPA, financials | 同上 | ESA、動員、価格形態、ARC/RRC、インフレ/FX の存在 |
| Intermediate Day4 — price-to-win, response, orals, DD, negotiation, contracting, implementation | 同上 | 契約と承認解の双方向、DD 種別、口頭提案の型 |
| Intermediate ケース（架空 RFP） | **未登録** | 演習ケース |
| IOSM / サービス別原価ブック / Workbench | **未登録** | ツール・マスタ |
| Inflation / Currency 解説 ppt | 同上 § commercials | リスク分担の考え方のみ。数値・社内ポリシー番号は不登録 |
| Advanced — transformational IO, modeling, network/DC, third party, SLA, pricing, realization | 同上 | as-is vs transformed-only、prime/sub vs ops mgmt、realization は署名後も SA |
| Advanced AVA クライアントケース、RFP、SOW、Orals | **未登録** | 実名・契約原本 |
| SA Certification Guide / 認定プレイブック | **未登録** | 社内認定 |

**Note:** Accenture / Avanade 資料。再配布禁止。個人メールは索引にも載せない。

---

## Program Line N: Systems Integration SA / SI Delivery Lead（SISA / SIDL, ~FY16）

原本は `Downloads/SISA_SIDL/`。社内秘。ケース RFP・契約改訂・認定ツールは不登録。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| SISA FY16 Day1–2 / Prep | `systems-integration-solution-planning.md`, `estimate-target-commitment.md` | 見積≠目標≠約束、Solution Plan 質問、ブループリント、Vモデル、2種コンティンジェンシー、tick-and-tie |
| SIDL Day1–2 | `delivery-leadership.md` | SA→DL、契約 vs 期待、ODE/EAC、動員、変更管理 |
| Solution Plan / Blueprint / ケース RFP・契約 | **未登録** | クライアント演習・実契約 |
| ロジスティクス、認定ガイド | **未登録** | |

---

## Program Line O: Delivery Management Academy（DMA II–III, ~2014–2015）

原本は `Downloads/DMAⅡ/`, `Downloads/DMAⅢ/`。

| ローカル原本（種別） | 抽出先 | 登録範囲 |
|---------------------|--------|---------|
| DMA III Days 1–5 講義 | `delivery-leadership.md` | プロジェクト vs プログラム、価値スコアカード、リリース、期待管理、商業ライフサイクル |
| DMA II Module 9 サービス管理 | `delivery-leadership.md`, `transition-vs-transformation-vs-realization.md` | Introduction vs Transition、Warranty≠運用 |
| FutureTech / Client メモ、レッスン学び発表 | **未登録** | ケース |
| Playbook PDF、ソーシャルスタイル | **未登録** | ブランド方法論・アイスブレイク |
| KT テンプレ実ファイル | **未登録** | 様式 |

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

## Program Line D: SCN Training（IBM legacy, 2003–2005）

| ローカル原本（例） | 種別 | 抽出先（リポジトリ） |
|-------------------|------|---------------------|
| `SCN概要(KM).pdf` | 概要・定義・KOPT・KPI・事例 | `frameworks/strategic-capability-network.md` |
| `SCN作成についての補足資料-SCN作成の勘どころ　-.pdf` | 作成勘どころ・As-Is/To-Be・広がり/深さ | `standards/scn-creation-guide.md` §Breadth/Depth, §Workflow |
| `SCN作成のポイント.pdf` | 記述ルール・WS運営・Q&A | `standards/scn-creation-guide.md` §Notation, §Prerequisites |

**Note:** 旧 `.ppt` は日本語抽出不可。PDF版を原本とする。IBM/client名・X社事例はリポジトリには一般化のみ登録。

---

## Program Line C: JERA（2026）— リポジトリ内参照

| 原本 | 状態 | 抽出先 |
|------|------|--------|
| 発電所自立経営 v0.2–v0.6 | ローカル/Downloads | `client-deliverable-voice-jera-2026-08.md`, `author-voice.md` |
| McKinsey 6/29 DX戦略ディスカッション（メモ・事前送付 p.7 等） | ローカル/Downloads | `knowledge/patterns/jera-scn-ebitda-tree.md` |
| 7/2 DX戦略論点_fix、AMP rev009、DGD 第2版 | ローカル/Downloads | 同上 §出典 |
| `scripts/generate_jera_draft_*.py` | 未コミット（任意） | — |

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
| `deliverable-archetypes.md` | 中 | ✅ 登録済（Archetype G 2026-08-13） |
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
| `jera-scn-ebitda-tree.md` | 高 | ✅ 登録済（2026-08-12） |
| `development-standards-framework.md` | 高 | ✅ 登録済（2026-08-13） |
| `document-management-standard.md` | 高 | ✅ 登録済（2026-08-13） |
| `development-management-guide.md` | 高 | ✅ 登録済（2026-08-13） |
| `operations-design-guide.md` | 中 | ✅ 登録済（2026-08-13） |
| `operations-handover-guide.md` | 中 | ✅ 登録済（2026-08-13） |
| `environment-management-guide.md` | 低 | ✅ 登録済（2026-08-13） |
| `release-management-guide.md` | 中 | ✅ 登録済（2026-08-13） |
| `sap-implementation-phase-model.md` | 中 | ✅ 登録済（2026-08-14） |
| `domains/energy-utilities.md` | 高 | ✅ 登録済（2026-08-19） |
| `requirements-artifact-review.md` | 高 | ✅ 登録済（2026-08-19） |
| `experience-before-scope.md` | 中 | ✅ 登録済（2026-08-19） |
| `platform-build-vs-enablement.md` | 中 | ✅ 登録済（2026-08-19） |
| `change-management.md` | 高 | ✅ 登録済（2026-08-19） |
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

---

## Future Extraction (Optional)

以下はローカル原本からの**追加抽出候補**。自動化または手動レビューが必要。

| 候補 | 方法 | 出力先案 |
|------|------|---------|
| 提案書 v4.5 の章立て | LibreOffice/PPT→txt | `deliverable-archetypes.md` 精緻化 |
| 各案評価シートの評価軸一覧 | xlrd | `vendor-proposal-evaluation.md` 付録 |
| 200/900 フォルダ成果物 | ユーザー提供時 | Phase 200/900 詳細 |
| 開発管理本編 `.doc` 本文 | LibreOffice/PDF→txt | `development-management-guide.md` ✅ |
| カスタム開発 C様式目次 | xlrd / 様式目次.doc | `deliverable-archetypes.md` Archetype G ✅ |

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
