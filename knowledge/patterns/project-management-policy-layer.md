# Pattern: Project Management Policy Layer

**Status:** Active  
**Origin:** Anonymized legacy SI proposal chapter on project management policy (requirements-to-cash style program; Program Line Y). Slide tables, schedule actuals, tool brands, and program labels are **not** stored here.

## Pattern statement

提案やキックオフの「プロジェクト管理方針」は、PMO のポートフォリオ論でも、開発管理ガイドラインの様式カタログでもない。**プロジェクト層で何を測り、何を台帳にし、どの場で事実確認し、どの閾値で変更・課題・リスクとして扱うか**を一文で固定する章である。プログラム層の会議階層（`program-governance-cadence.md`）や発注側監督（`development-management-guide.md`）と重複してよいが、**決定権と報告、ベースラインと変更、課題とリスクと ToDo** の境界はここで明示する。

| Stance | Success | Forbidden |
|--------|---------|-----------|
| **Seller / delivery** | 方針章が TOC・境界・判定条件を持ち、週次で運用できる | 失敗原因の羅列やツール宣伝で章を埋める |
| **Buyer / oversight** | ベンダー方針が自社の進捗・仕様・品質監督と噛み合う | プログラム定例にタスク表を上げて「方針」と呼ぶ |
| **PgMO** | プロジェクト層の台帳と、プログラム層の横断決定が分離している | 課題一覧の読み合わせをステコミの代用にする |

## Signals

- 「管理方針」の見出しはあるが、進捗の測り方・変更の起票条件・課題／リスク／ToDo の切り分けが無い  
- タスク完了数％だけが進捗で、遅延の**規模**が見えない  
- 全体会議の直前に事実確認がなく、見込みと実績が混ざる  
- 品質は試験工程だけ見て、前工程の阻害要因を追跡していない  
- 変更が口頭合意のまま走り、ベースライン（要求・契約・WBS）との関係が不明

## What a project management policy chapter must define

最低限、次のブロックを定義する（中身の数値・会議曜日・製品名は案件原本）:

| # | Block | Judgment to lock |
|---|--------|------------------|
| 1 | **Intent** | なぜ定量管理か（並行作業を定性報告だけで見ない） |
| 2 | **Progress** | 進捗率の定義（作業量価値 vs タスク件数）と予実の見せ方 |
| 3 | **Cadence (project)** | チーム／ベンダー内／プロジェクト全体の場の役割（事実確認 vs 決定） |
| 4 | **Quality** | 工程ごとの品質目標と、**次工程の阻害要因**の早期抽出・消し込み |
| 5 | **Issue / risk / ToDo** | 損失×不確実性による分類と、報告する会議の層 |
| 6 | **Change** | 起票→影響分析→実施判定→終結。QCD 影響の判定条件 |
| 7 | **Baselines** | 何が合意済みか（要求仕様、契約金額、WBS レベル等） |

プログラム層のステコミ／横断調整／検査の設計は本パターンの外。`playbooks/program-governance-cadence.md` に委ねる。

## Project layer vs program layer

| Concern | Project layer (this policy) | Program layer |
|---------|----------------------------|---------------|
| Progress | WBS／作業量ベースの予実、遅延規模 | 横断依存・シナリオ・便益 |
| Quality gates | 工程レビュー・試験密度・指摘追跡 | マイルストン統合、検査（assurance） |
| Change | ベースライン変更票と QCD 影響 | ポートフォリオ／契約／複数 PJ 波及 |
| Risk / issue | 一覧と週次トラッキング | エスカレーション条件を満たすものだけ |
| Meetings | 事実確認 → 見通し | 権限のある決定、依存解消 |

**報告と決定を混ぜない:** 上位報告の前に、チーム進捗とベンダー内で進捗・課題・リスクの**事実確認**を行う。上位の場は「共有」ではなく、権限に応じた決定または横断調整に使う。

## Progress: work value vs task count

タスク件数ベースの進捗率は、軽いタスクと重いタスクを同列にするため**遅延規模を歪める**。方針では次を明示する:

- **計画価値（PV）** — 時点までに完了しているべき作業量  
- **出来高（EV）** — 完了した作業の計画価値（例: 総工数 × 進捗率）  
- **スケジュール差異（SV = EV − PV）** — 遅れの**大きさ**  

手法名や表計算の様式は問わない。必要なのは「件数％ではなく作業量で遅延を語る」という判定である。詳細の週次監督は `development-management-guide.md` §進捗管理。

## Issue / risk / ToDo boundaries

| Class | Loss | Uncertainty | Treat as |
|-------|------|-------------|----------|
| **Risk** | Yes | Yes (not yet realized) | Risk register; prevent / mitigate |
| **Issue** | Yes | No (realized) | Issue register; root cause → action |
| **Neither** | No | — | Do not manage as risk/issue |
| **ToDo** | — | — | Concrete assigned work with owner/date (may close an issue/risk action) |

リスクの報告レベルは「発生確率 × 損失の大きさ」で層（チーム／プロジェクト／プログラム）を上げる。閾値の数値は案件で決める。重要度 A–D の提示ルールは既存の問題管理表（`development-management-guide.md`）と併用してよい。

## Customer-shared open items and completion criteria

プロジェクト層の台帳を**手元専用**にしない。顧客と共有する未決／課題は次を固定する:

| Element | Lock |
|---------|------|
| **Visibility** | 不確定は不確定として見せる。要件期に未決があること自体は可。「今ない／見えていない」ままが最悪 |
| **Completion criteria** | 誰と、何を合意したら閉じるか。状態ラベルだけでは閉じない |
| **Language** | 「解決」「解消」は完了条件を満たすまで使わない。閉じた／移した／継続を分ける |
| **Audience** | 顧客共有リストと内部深掘りリストを分ける。評価枠・MECE 表は内側；求められたら Appendix |

顧客向けの見せ方（週次／月次の物語）は `standards/deliverable-archetypes.md` Archetype J。会議の層は `program-governance-cadence.md`。

## Change control vs baseline (QCD)

一度合意した事項を見直すときは、変更単位で票を起こし、状態（起票→受付→判定→影響分析→実施判定→実施→終結）を追う。

**QCD 影響あり**の典型判定（方針に書く条件の型）:

| Dimension | Trigger (type) |
|-----------|----------------|
| **Quality** | ベースライン化された要求仕様への変更 |
| **Cost** | 工数等により契約金額が増減する変更 |
| **Delivery** | 合意済み WBS の管理レベル以上の変更 |

影響なしでも記録する／影響ありは実施判定前に影響分析を完了する、を方針で固定する。仕様確定前後の発注側フローは `development-management-guide.md` §仕様管理。プログラム横断の変更所有は `pmo-operating-guide.md`。

## Quality at project layer

品質目標を工程ごとに置き、レビュー指摘・試験実績を短周期で収集する。加えて、**次工程以降の品質阻害要因**を早い工程で抽出し追跡して消し込む。プログラム検査は「台帳が実在するか」の保証であり、プロジェクト品質プロセスの代替ではない。

## Implications

- 提案の「管理方針」章をレビューするときは、上表 TOC の欠落を先に指摘する（失敗事例リストの長さではない）。  
- PgMO 立ち上げ後は、本方針の会議を `program-governance-cadence.md` の層名にマッピングし、週次に進捗と検査を混ぜない。  
- ツール（ボード、共有、リモート会議）は方針の付録であり、境界定義の代替にしない。

## Response

1. 案件の「管理方針」がプロジェクト層 TOC のどれを欠けているか一覧する。  
2. 課題／リスク／ToDo と変更の QCD 条件を一文ずつ合意する。  
3. 進捗の測り方を件数％から作業量差異に直すか、意図的に件数を残す理由を書く。  
4. 会議を「事実確認」と「決定／横断」に分け、プログラム層へ上げる条件を既存 cadence playbook に接続する。

## Exceptions

- 単一チーム・短工期で台帳が過剰な場合は、Issue と ToDo を統合してよいが、Risk と Change の境界は残す。  
- 官側共同利用の複数ロット開始判定は `public-multi-lot-construction-pmo.md` が優先。

## Related

- `standards/development-management-guide.md`
- `standards/pmo-operating-guide.md`
- `playbooks/program-governance-cadence.md`
- `playbooks/cross-project-program-management.md`
- `frameworks/transformation-pmo.md`
- `standards/deliverable-archetypes.md` Archetype J（顧客共有の週次／月次）
- `knowledge/index/legacy-source-index.md` Program Line Y
