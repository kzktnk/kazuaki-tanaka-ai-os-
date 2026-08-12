# Legacy Source Index

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** ローカル保管のレガシー原本と、リポジトリ内知識の対応索引。**原本の中身は含まない。**

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
| `MM20030514-01_評価シートチェック.doc` | 評価設計議事 | `vendor-proposal-evaluation.md`（全章） |
| `RFP/RFP/RFP結合版-取引会計*.doc` | RFP本文 | **未登録**（機密）。`requirements-document-outline.md` Appendix Map のみ |
| `RFP/RFP/RFP結合版-人事*.doc` | RFP本文 | **未登録**（機密） |
| `RFP/Appendices/AP_AC*.ppt/xls` | 業務Appendix | `requirements-document-outline.md` §AC category |
| `RFP/Appendices/AP_IF*.xls` | 連携Appendix | `requirements-document-outline.md` §IF category |
| `RFP/Appendices/AP_BS*.xls` | 帳票Appendix | `requirements-document-outline.md` §BS category |
| `RFP/Appendices/AP_ST*.ppt/xls` | 基盤Appendix | `requirements-document-outline.md` §ST category |
| `RFP/Appendices/Appendices_Index.xls` | 索引 | `requirements-document-outline.md` §RFP Appendix Category Map |

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
| `vendor-proposal-evaluation.md` | 高 | ✅ 登録済 |
| `program-phases-investigation-to-requirements.md` | 高 | ✅ 登録済 |
| `author-voice-archetypes-legacy.md` | 高 | ✅ 登録済 |
| `deliverable-archetypes.md` | 中 | ✅ 登録済 |
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

---

## Future Extraction (Optional)

以下はローカル原本からの**追加抽出候補**。自動化または手動レビューが必要。

| 候補 | 方法 | 出力先案 |
|------|------|---------|
| 提案書 v4.5 の章立て | LibreOffice/PPT→txt | `deliverable-archetypes.md` 精緻化 |
| 各案評価シートの評価軸一覧 | xlrd | `vendor-proposal-evaluation.md` 付録 |
| 200/900 フォルダ成果物 | ユーザー提供時 | Phase 200/900 詳細 |

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
