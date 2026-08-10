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
