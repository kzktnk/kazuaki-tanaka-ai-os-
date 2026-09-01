---
type: framework
title: "コンサルタント Capability／スキル／レベル モデル（v0.6 ― Capability IV統合・24 Skill）"
source: "v0.1パイロットへのレビュー（2026-09-01）を反映して全面改訂（v0.2）。③受領で事実関係を更新（v0.2.1）。v0.2.1へのレビューを反映しSkill粒度原則等を統合（v0.3）。v0.3へのレビューで構造設計を確定、Recommended Prerequisiteを追加し全Skillを展開（v0.4）。v0.4へのレビューで全18 SkillのEvidence均質性QC（v0.5）。Role／Responsibility層の検討（frameworks/consultant-role-responsibility-model.md）から導出されたCapability IV（Business/Management Literacy、6 Skill）をPrerequisite Knowledge付きで統合（v0.6）。"
status: draft
extracted: false
gap_fill: "frameworks/capability-model.md（クライアント組織のCapability階層＝SCN用）とは別物。本ファイルはコンサルタント本人／チームメンバーのスキル・習熟度を扱う。名称の衝突に注意。Role／Responsibility層とRequired Levelの一覧はframeworks/consultant-role-responsibility-model.md側で管理する。"
related:
  - frameworks/consultant-role-responsibility-model.md（Role／Responsibility層、Required Level一覧）
  - frameworks/consultant-learning-map-example.md
  - frameworks/pilot-assessment-strategy-consultant.md
  - frameworks/top-down-thinking.md
  - frameworks/thinking-patterns/
  - playbooks/wbs-design.md
  - playbooks/strategy-scn.md
  - playbooks/cross-project-program-management.md
  - playbooks/operations-transition-playbook.md
  - playbooks/stakeholder-activation-playbook.md
  - core/author-voice.md
  - standards/scn-creation-guide.md
  - playbooks/program-governance-cadence.md
last_updated: 2026-09-01
---

# コンサルタント Capability／スキル／レベル モデル
## ― 若手配布を前提にした育成マップ（v0.6 ― Capability IV統合・24 Skill） ―

**Status:** Draft（4 Capability・24 SkillともEvidence QC完了。次は実在メンバー1名での運用検証、§6）

## 0. 変更履歴

**v0.1→v0.2**（前回レビュー反映）：Capabilityの切り方をPlaybook逆算から独立layerへ、Level定義を状態描写からCurrent→Target→Learning/OJT→Evidenceの遷移へ、教材を「到達者への配布物」から「Learning Intervention」へ、Learn→OJT→Evidence→Review→Level upループの明示、AIを独立Skillから横断軸へ。

**v0.2→v0.2.1**：③受領によりCapability IIのTransition行の事実関係を更新。

**v0.2.1→v0.3**：Skillの粒度原則を明文化しTransitionを3分割・Ch7をCapability IIIへ再配置、Level定義を共通化しEvidenceと分離、再現性の原則を追加、判定者を個人名から役職名へ、横串を受領し3本目のSkill「Stakeholder Diagnosis」を展開、「仮説を作る」の教材マッピングを検証。

**v0.3→v0.4**：Recommended Prerequisite（推奨学習順序）を追加、Consultant Learning Mapのプロトタイプを別ファイルで作成、残り15 Skillを展開し3 Capability・18 Skillを埋めた。

**v0.4→v0.5**：全18 SkillのEvidence均質性QC、Learning MapへのAssessment Status追加、評価・意思決定するL1例の修正。

**v0.5→v0.6**（今回）：

1. **Capability IV｜Business / Management Literacyを新設・統合**：Role／Responsibility層の検討（`consultant-role-responsibility-model.md`）で、Strategy ConsultantのResponsibility「R7：分析・提言を事業実態に照らして妥当にする」がCapability I〜IIIでカバーされないGapとして特定され、その解として6 Skillを追加した（Company／Financial Analysis、Business Model／Economics、Investment／Business Case、Corporate Governance／Management、Commercial／Contract Literacy、Regulatory／Risk Literacy）
2. **各SkillにPrerequisite Knowledge（Pass／Not Yet）を付与**：KnowledgeはLevelを持たず、Skill本体のみ既存共通Level定義でL0〜L4を判定する
3. **「RoleがRequired Levelを決める」原則を明示**：SkillはL0〜L4まで常に定義し、Strategy Consultantとしてどこまで必要かはRole側（別ファイル）が指定する。Commercial／Contract LiteracyとRegulatory／Risk Literacyは、「法的判断はScope外」という範囲の狭さと「Levelの高さ」を混同していたのを修正し、Required LevelをL2とした（詳細は`consultant-role-responsibility-model.md`）
4. 新設した6 Skillも既存18 Skillと同じEvidence QC（L2＝自力実施＋主要判断理由の説明、L3＝問題発見＋なぜ問題か＋修正方向、L4＝非標準適応＋判断理由＋他者指導）を最初から適用し、24 Skill全体でギャップ0件を確認した
5. §1.5のRecommended Prerequisiteに6 Skill分を追加

---

## 1. Capability構造（Playbookと独立した上位層）

Playbookが増えてもCapability自体は増減しない状態を目指し、次の4系統に固定する。Skillはこの下にぶら下がる。Playbook／フレームワークはさらにその下（教材）に位置づけ、1つのSkillに複数教材が対応することも、1つの教材が複数Skillにまたがることもある。

### Skillの粒度原則

**Skillとは、単独でL0→L4を評価できる最小の実務能力単位**とする。1つのPlaybook全体を1つのSkillに対応させない（Playbookは複数Skillにまたがる教材の束であってよい）。この原則により、v0.2の「Transition」（③1冊分をそのまま1 Skillにしていた）を見直した。

### Capability I｜Thinking / Problem Solving

| Skill | 内容 | 対応教材（現状） |
|---|---|---|
| 問いを立てる | Key Question・4Cs＆1Qで論点を定義する | `playbooks/strategy-scn.md` Ch2.1 |
| 構造化する | 対象に合ったThinking Patternで箱を作る | `frameworks/top-down-thinking.md`、`frameworks/thinking-patterns/pattern-01〜08` |
| 仮説を作る | Fact→Issue→Hypothesisで仮説を組む | `core/author-voice.md` §1.1、`playbooks/strategy-scn.md` Ch3 |
| 分析する | Analysis Planを立て、Findingsに収束させる | `playbooks/strategy-scn.md` Ch2.3・Ch3.4 |
| 評価・意思決定する | オプションを評価し、意思決定につなげる | `playbooks/strategy-scn.md` Ch6 |

### Capability II｜Delivery / Execution

| Skill | 内容 | 対応教材（現状） |
|---|---|---|
| Work Planning／WBS | 成果物から逆算し、詳細タスクへ分解する | `playbooks/wbs-design.md` |
| Dependency Management | PJ間の受け渡し・依存を管理する | `playbooks/cross-project-program-management.md` Ch3 |
| Schedule Integration | 複数PJのスケジュールを統合する | `playbooks/cross-project-program-management.md` Ch4 |
| Scope／Responsibility | スコープ境界と責任分界を管理する | `playbooks/cross-project-program-management.md` Ch5 |
| Risk／Issue Management | RAID・エスカレーションを運用する | `playbooks/cross-project-program-management.md` Ch8 |
| Transition Due Diligence／Planning | 引き継ぎ前提（Operability・Warranty）を検証し、移行計画を設計する | `playbooks/operations-transition-playbook.md`（Ch2・Ch3.1〜3.4） |
| Knowledge Transfer | 暗黙知を運用チームへ移転する | `playbooks/operations-transition-playbook.md`（Ch2.5・Ch3.5） |
| Transition工数見積もり | 移行工数を前提条件付きで見積もる | `playbooks/operations-transition-playbook.md`（Ch4） |

③のChapter 7「定着化とチェンジマネジメント」は、内容的にはTransitionという作業ではなく**人の行動が変わるかどうか**を扱っているため、Capability IIではなくCapability IIIの「Influence／Activation」の教材として整理し直した（下表）。

### Capability III｜Stakeholder / Leadership

| Skill | 内容 | 対応教材（現状） |
|---|---|---|
| Stakeholder Diagnosis | Segment（誰から動かすか）とDiagnose（なぜ動かないか）で見立てる | `playbooks/stakeholder-activation-playbook.md`（横串 Ch2・Ch3） |
| Communication | 意思決定者向けに構造化して伝える | `core/author-voice.md` §3〜4 |
| Facilitation | ワークショップ・レビューを回す | `standards/scn-creation-guide.md` §Workshop |
| Influence／Activation | 原因に応じた打ち手を選び、個別化し、行動が変わったかを観察する | `playbooks/stakeholder-activation-playbook.md`（Ch4〜8）、`playbooks/operations-transition-playbook.md`（Ch7、定着化の文脈） |
| Governance／Escalation | Steering等への報告・エスカレーションを設計する | `playbooks/cross-project-program-management.md` Ch8.5、`playbooks/program-governance-cadence.md` |

### AIの扱い（独立Skillにしない）

AIは特定のSkillではなく、**どのSkillにも横断して効く軸**として扱う。`frameworks/top-down-thinking.md`が既にこの立場を取っている（目的→構造→AIへ質問→回答評価→構造修正、という順序でAIを構造化プロセスに組み込む）。したがって各Skillの「Learning／OJT」列には、該当する場合「AIとの協働」を明示的に含める（§3参照）が、Capability／Skill一覧には独立の行を作らない。

### 1.5 Recommended Prerequisite（推奨学習順序）

Skillは横並びで管理するが、実務上は習得しやすい順序がある。**「L2にならないと次へ進めない」という硬い資格制ではなく**、「この水準まで来ていると次が楽になる」という推奨（soft prerequisite）として運用する。

| Skill | 推奨Prerequisite |
|---|---|
| 問いを立てる | ―（入口） |
| 構造化する | 問いを立てる L1 |
| 仮説を作る | 構造化する L1 |
| 分析する | 問いを立てる L1、構造化する L1 |
| 評価・意思決定する | 分析する L2、仮説を作る L2 |
| Work Planning／WBS | 構造化する L1 |
| Dependency Management | ―（入口） |
| Schedule Integration | Dependency Management L1 |
| Scope／Responsibility | ―（入口） |
| Risk／Issue Management | Dependency Management L1、Scope／Responsibility L1 |
| Transition Due Diligence／Planning | Scope／Responsibility L2 |
| Knowledge Transfer | Transition Due Diligence／Planning L1 |
| Transition工数見積もり | Work Planning／WBS L2、Transition Due Diligence／Planning L1 |
| Stakeholder Diagnosis | ―（入口） |
| Communication | ―（仮説を作る L1と並行が望ましい） |
| Facilitation | ―（入口） |
| Influence／Activation | Stakeholder Diagnosis L2 |
| Governance／Escalation | Risk／Issue Management L2、Stakeholder Diagnosis L1 |
| Company／Financial Analysis | ―（入口。Capability IV内で最も基礎） |
| Business Model／Economics | Company／Financial Analysis L1 |
| Investment／Business Case | Company／Financial Analysis L1、Business Model／Economics L1 |
| Corporate Governance／Management | ―（入口） |
| Commercial／Contract Literacy | ―（入口） |
| Regulatory／Risk Literacy | ―（入口。Commercial／Contract Literacy L1と並行が望ましい） |

Learning Map（§5）では、本人のCurrent LevelとこのPrerequisite表を突き合わせ、「次にどのSkillへ進むのが自然か」を機械的に示唆する。ただし本人のRole／Assignment（今アサインされている案件で何が必要か）が優先されるべき場面もあるため、あくまで推奨であり強制はしない。

---

## 2. Level遷移フレーム

教材は「そのLevelにいる証明として渡すもの」ではなく、「次のLevelへ上げるための介入」である。したがって全Skill共通で、次の5列で定義する。

| 列 | 意味 |
|---|---|
| Current | 現在のLevel |
| Target | 到達させたいLevel |
| Learning／OJT | Targetに上げるために何を読ませ、何をやらせるか（該当すればAIとの協働も含む） |
| Evidence | Targetに達したと判定する、観察可能な基準（Skillごとに具体化） |
| 判定者 | 誰がEvidenceを確認するか（役職。個人名にしない＝後述） |

### Level共通定義（ものさし）とEvidence（測定方法）の分離

**Level定義＝全Skill共通のものさし**、**Evidence＝Skillごとの測定方法**、という二層にする。Level定義だけを見て「WBSのL2」と「Stakeholder DiagnosisのL2」が同じ意味だと言えるようにする。

| Level | 呼称 | 共通定義 |
|---|---|---|
| L0 | 未着手 | そのSkillにまだ触れていない |
| L1 | 型を知る | 標準的な型・手順・判断観点を説明でき、指導下で適用できる |
| L2 | 自走できる | 標準的な条件で、自力で実施し、成果物のQuality Checkと主要判断理由の説明ができる |
| L3 | レビューできる | 他者成果物の問題を発見し、理由と修正方向を示せる |
| L4 | 教えられる | 非標準条件で型を適応・変更し、その判断理由を説明して他者を指導できる |

各Skillの表のEvidence列は、この共通定義をそのSkillの実務に翻訳したものであり、共通定義そのものを緩めたり厳しくしたりしない。

### 再現性の原則

**1回の成功だけではLevel認定しない。** 特にL3・L4は、単発のレビュー・単発の指導実績で認定せず、条件の異なる複数ケース（目安：2ケース以上）で同じEvidenceを再現できることを確認してから認定する。L1・L2でも、Evidenceの記述が「1回できた」と読める場合は「標準的な条件で安定して再現できる」という含意があるものとして運用する。

---

## 3. Skill別 Level遷移表（24 Skill、全展開）

Round 1で検証した3 Skill（構造化する／Work Planning・WBS／Stakeholder Diagnosis）を含め、4 Capabilityの全24 Skillを同じ構造で展開する。

**判定者の運用**：「Capability Owner」はCapability全体に責任を持つ役職、「認定L4 Reviewer」はそのSkillでL4に到達した人のうち、Capability Ownerが認定した人を指す。Bootstrap（最初は誰も認定L4 Reviewerがいない）の期間は、Capability Ownerが直接判定する。認定L4 Reviewerが育ったら、以降のL3・L4判定はそちらに委譲してよい。個人名を判定者欄に置かないのはこのローテーションを前提にしているためである。

### 3.1 Capability I｜Thinking / Problem Solving

#### 問いを立てる

Key Question（4Cs＆1Q：Context／Client／Criteria／Constraints／Question）で論点を定義する型。Criteria／Constraintsを分析前に合意しないと「立派だが採用されない提言」になる。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | `playbooks/strategy-scn.md` Ch2.1を読み、指導者と一緒に実案件で4Cs＆1Qを1回組み立てる | 4Cs＆1Qの5要素を自分の言葉で説明でき、なぜCriteria／Constraintsを分析前に決めるのかを説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上の案件で、関係者と反復しながら自分で4Cs＆1Qを組み立てる | 2件以上で、関係者と合意したKey Questionを1文で言え、なぜその5要素の組み立てにしたかを説明でき、Criteria／Constraintsが分析着手前に合意されている | 指導者→OJT先PM |
| L2 | L3 | 他者が立てたKey Questionをレビューする | 複数の他者アウトプットで、Criteria／Constraints未合意のまま分析が進んでいる、またはKey Questionが1文で言えない状態を発見し、なぜ問題か・どう合意し直すべきかを示せる | Capability Iの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 関係者間でCriteria／Constraintsが対立するケースを複数経験する | 対立するCriteriaを持つ複数の非標準ケースで、収束させる進め方を設計し、理由を説明して他者に教えられる | Capability Owner |

#### 構造化する

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | `frameworks/top-down-thinking.md`を読む。1つのPattern（Pattern 1 Why→What→Howが導入しやすい）を指導者と一緒に1回適用する | Pattern選定の理由と、箱の中身を自分の言葉で説明できる | 指導者 |
| L1 | L2 | 実案件の論点を、自分でPatternを選んで構造化する。AIを使う場合は「箱を渡してから埋めさせる」順序を守らせ、埋まった中身は自分でレビューさせる | 標準的な論点2件以上において、Pattern選定・箱の中身・AIレビュー観点（`references/thinking-patterns-reference.md`）の3点を満たした状態で自力完成させ、選定理由を説明できる | 指導者→OJT先PM |
| L2 | L3 | 他者（L1〜L2）が作った構造化アウトプットを、`references/thinking-patterns-reference.md`のレビュー観点で読む練習をする | 条件の異なる複数の他者アウトプットで、問題点（Pattern誤選定、粒度バラつき等）を発見し、なぜ問題か・どう直すべきかを指摘できる | Capability Iの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 非標準の対象（Patternが1つに収まらない、複数Pattern併用が要る等）で構造化を経験する | 型が単純に当てはまらない複数の場面で、どのPatternをどう組み合わせる／変形するかを判断し、理由を添えて他者に教えられる | Capability Owner |

#### 仮説を作る

Fact→Issue→仮説→To-Be→Approach（`core/author-voice.md` §1.1）と、Findings 3〜5件への収束（`playbooks/strategy-scn.md` Ch3.4）が教材。仮説は「たたき台」であり断定しない。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | `core/author-voice.md` §1.1と`strategy-scn.md` Ch3.4を読み、指導者と一緒にFinding 1件を組み立てる | Fact→Issue→仮説→To-Be→Approachの連鎖と、仮説を断定でなく「たたき台」と明示する理由を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上の案件でFindingsを組み立て、3〜5件に収束させる | 2件以上で、Fact→Issue→Cause／Implicationの連鎖が明確なFindingsを3〜5件に収束させ、なぜその因果連鎖にしたかを説明でき、仮説であることを明示できる（単なる観察の羅列にしない） | 指導者→OJT先PM |
| L2 | L3 | 他者のFindings／仮説をレビューする | 複数の他者アウトプットで、「Findingsが観察の羅列で因果がない」（`strategy-scn.md` Ch8の既知の失敗パターン）状態を発見し、なぜ因果が繋がっていないか・どう繋ぎ直すべきかを示せる | Capability Iの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | Factが薄い・対立するケースを複数経験する | 材料が薄い・矛盾する複数の非標準ケースで、それでも責任を持てる仮説の立て方（またはエビデンス不足の明示）を、判断理由を説明した上で他者に教えられる | Capability Owner |

#### 分析する

Analysis Plan（論点ごとに何を・なぜ・いつまでに、End Product／担当／期限を先に決める。Tool-first禁止）が教材（`playbooks/strategy-scn.md` Ch2.3・Ch3.4）。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Ch2.3を読み、指導者と一緒にAnalysis Planを1件組み立てる | なぜEnd Product・担当・期限を分析着手前に決めるのか（Tool-firstを避けるため）を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上でAnalysis Planを自分で組み立てる | 2件以上で、Analysis Planの各行がKey Questionに接続し、End ProductがTool-firstでなく着手前に定義されている理由を説明できる | 指導者→OJT先PM |
| L2 | L3 | 他者のAnalysis Planをレビューする | 複数の他者アウトプットで、Tool-firstパターンやKey Questionに接続しない行を発見し、なぜ問題か・どう組み直すべきかを示せる | Capability Iの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | Key Questionが分析途中で変わる非標準ケースを複数経験する | 複数の非標準ケースで、Key Question変化に応じてAnalysis Planを再設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### 評価・意思決定する

Suitability／Feasibility／Acceptability評価、重要度×実現可能性の優先順位付け、Stakeholder Awareness→Ownershipが教材（`playbooks/strategy-scn.md` Ch6）。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Ch6を読み、指導者と一緒にオプションをS／F／Aで評価する | Suitability／Feasibility／Acceptabilityの違いを説明でき、1つの観点だけでOptionを選ぶことの問題を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上でS／F／A評価を自分で行う | 2件以上で、都合の悪い制約を隠さずS／F／A評価を行い、なぜその優先順位（重要度×実現可能性）にしたかを説明でき、未合意事項をRisk／Assumptionとして明示できる（全員合意を待たない） | 指導者→OJT先PM |
| L2 | L3 | 他者の評価をレビューする | 複数の他者アウトプットで、隠れた制約や「全員合意済み」の見切り発車を発見し、なぜ問題か・どう評価し直すべきかを示せる | Capability Iの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 関係者間の利害が本質的に対立する非標準ケースを複数経験する | 複数の非標準ケースで評価の進め方自体を設計し、判断理由を説明して他者に教えられる | Capability Owner |

### 3.2 Capability II｜Delivery / Execution

#### Work Planning／WBS

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | `playbooks/wbs-design.md`（本編）を読み、指導者同席でStep1〜5を1回通す | Step1〜5の順序と、詳細化5問を自分の言葉で説明できる | 指導者 |
| L1 | L2 | `playbooks/wbs-design-selfstudy.md`で自分の担当タスクを分解し、`templates/wbs-breakdown-sheet.md`のSTEP4セルフチェックと分解チェックリストで自己採点する | 条件の異なる実案件（または実案件相当）2件以上で成果物からWBSを自力完成させ、STEP4セルフチェックを満たし、粒度判断（pt基準）の理由を説明できる | 指導者→OJT先PM |
| L2 | L3 | 他者が作ったWBSを、分解チェックリスト（12観点）でレビューする練習をする | 条件の異なる複数の他者WBSで、粒度・抜け・依存関係の問題を発見し、なぜ問題か・どう直すべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 案件特性（規模・不確実性）に応じてpt基準・分解粒度を調整する経験を積む | 非標準条件（大規模・高不確実性等）の複数案件で分解方針を自分で設計し、理由を説明した上で他者に教えられる | Capability Owner |

**現状の教材ギャップ**：L1→L2、L0→L1の教材（本編・セルフスタディ版）は揃っている。L2→L3・L3→L4のLearning／OJT列は現時点でPlaybook本文の一部を転用しているだけで、独立した教材にはなっていない。次点で着手するなら、`分解チェックリスト`を単体のレビュー訓練教材として独立させる価値がある。

#### Dependency Management

Dependency Register、Predecessor／Successor、Critical Dependency、IFレビューが教材（`playbooks/cross-project-program-management.md` Ch3）。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Ch3を読み、指導者と一緒にDependency Registerの1エントリを作る | Predecessor／SuccessorとCritical Dependencyの判定基準を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上のプログラムでDependency Registerを自分で維持する | 2件以上で、なぜそのDependencyをCriticalと判断したかを説明でき、IFレビュー状況を追跡したRegisterを維持できる | 指導者→OJT先PM |
| L2 | L3 | 他者のRegisterをレビューする | 複数の他者Registerで、抜けているDependencyやCriticality誤判定を発見し、なぜ誤りか・どう直すべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 循環依存・多対多依存など非標準の依存構造を複数経験する | 複数の非標準依存構造で追跡方法を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Schedule Integration

各PJ WBSの統合（Cross-Project Milestoneのみ抽出）、Hand-off／Lead-Lag、「日付の整合」から「意味の整合」へ、Critical Pathが教材（`playbooks/cross-project-program-management.md` Ch4）。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Ch4を読み、指導者と一緒にIntegrated Milestone Planを1件作る | なぜPgMOは全工程でなくCross-Project Milestoneだけを統合するのか、「日付の整合」と「意味の整合」の違いを説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上のプログラムで統合スケジュールを自分で作る | 2件以上で、日付だけでなく前提の一致（意味の整合）まで確認したIntegrated Milestone Planを作り、なぜそこをCritical Pathと判断したかを説明できる | 指導者→OJT先PM |
| L2 | L3 | 他者の統合スケジュールをレビューする | 複数の他者アウトプットで、日付は揃っているが前提が食い違っている（意味の不整合）ケースを発見し、なぜ不整合か・どう直すべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | ベンダーごとにスケジュール手法が異なる非標準ケースを複数経験する | 複数の非標準ケースで統合方針を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Scope／Responsibility

Scope Boundary Matrix、RACI、Gap／Overlap、ベンダー間責任分界（`playbooks/cross-project-program-management.md` Ch5、特に5.4）が教材。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Ch5を読み、指導者と一緒にScope Boundary Matrixを1件作る | Gap／Overlapの見分け方と、RACIがベンダー境界をどう明確にするかを説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上でMatrixを自分で作る | 2件以上で、Gap／Overlapを洗い出し、なぜその責任分界にしたかを説明できるMatrixを作れる | 指導者→OJT先PM |
| L2 | L3 | 他者のMatrixをレビューする | 複数の他者Matrixで、未解決のGap／OverlapやRACIの曖昧な割り当てを発見し、なぜ問題か・どう解消すべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | グレーゾーン境界（データクレンジング、結合テスト環境構築等、Ch5.4）の紛争を複数経験する | 複数の非標準境界紛争を、5ステップの判断で解決し、判断理由を説明して他者に教えられる | Capability Owner |

#### Risk／Issue Management

RAGステータス判定基準、RAID、Decision Log／Change Control、Steering Committeeエスカレーション、ベンダー間板挟み対処（`playbooks/cross-project-program-management.md` Ch8）が教材。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Ch8を読み、指導者と一緒に1件をRAIDに分類する | RAIDの4区分と、Assumptionが最も見落とされやすい理由を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上のプログラムでRAID LogとRAGステータスを自分で運用する | 2件以上で、なぜその区分（R／A／I／D）に分類したかを説明できるRAID Logを維持し、感覚でなく数値基準（Variance日数等）に基づくRAGステータスを運用できる | 指導者→OJT先PM |
| L2 | L3 | 他者のRAID Logをレビューする | 複数の他者Logで、誤分類（例：AssumptionをIssueと誤記）や根拠のないRAG判定を発見し、なぜ誤りか・どう直すべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | ベンダー間対立の実エスカレーション案件を複数経験する | 複数の非標準対立案件で、事実と主張を分離するCh8.6の型を用いたエスカレーション／調停方針を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Transition Due Diligence／Planning

自PJからのService Introduction（Operability・Warranty）、他社からのTransitionにおけるデューデリジェンスが教材（`playbooks/operations-transition-playbook.md` Ch2・Ch3.1〜3.4）。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | ③Ch2〜3.4を読み、指導者と一緒にOperabilityチェックを1件実施する | 4点の準備状況チェック（Runbook／エスカレーション経路／監視閾値／リハーサル経験）とWarrantyの3設計点を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上のTransition（自PJ・他社いずれか）でDue Diligence／Readinessチェックを自分で行う | 2件以上で、必要チェックを網羅したGo／No-Go判定を、その根拠とともに行い、Warrantyの対象範囲・期間・体制を事前合意できる | 指導者→OJT先PM |
| L2 | L3 | 他者のTransition計画をレビューする | 複数の他者計画で、移行後のエスカレーション常態化につながる準備不足やWarranty定義の曖昧さを発見し、なぜ問題か・どう補うべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 複数ベンダー同時カットオーバー等、非標準のTransition構造を複数経験する | 複数の非標準構造でDue Diligenceの進め方を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Knowledge Transfer

暗黙知の運用チームへの移転設計（自PJ・他社共通、`playbooks/operations-transition-playbook.md` Ch2.5・Ch3.5）が教材。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | ③Ch2.5・Ch3.5を読み、指導者と一緒にKT設計を1件行う | 自PJ引き継ぎが「当たり前すぎて説明しない」暗黙知の観点で他社引き継ぎより見えにくいリスクを持つ理由を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上でKTを自分で設計・実施する | 2件以上で、なぜその暗黙知を優先的に掘り起こす対象と判断したかを説明でき、文書の受け渡しだけでなく能動的に掘り起こすKTを設計し、運用チームの独立対応可否で検証できる | 指導者→OJT先PM |
| L2 | L3 | 他者のKT計画をレビューする | 複数の他者計画で、文書受け渡しだけの受動的なKTを発見し、なぜ不十分か・どう能動的に掘り起こすべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 送り手側自身の文書化が薄い領域を複数経験する | 複数の非標準（低文書化）領域で暗黙知抽出の技法を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Transition工数見積もり

前提条件を明示した工数見積もり（`playbooks/operations-transition-playbook.md` Ch4）が教材。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | ③Ch4を読み、指導者と一緒に見積もりを1件作る | 前提条件を書き残さないことが見積もり崩れの最大要因である理由を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上で見積もりを自分で作る | 2件以上で、見積もり手法・主要前提・バッファ設定の判断理由を説明できる見積もりを作れる（Capability IIのRAID運用と接続） | 指導者→OJT先PM |
| L2 | L3 | 他者の見積もりをレビューする | 複数の他者見積もりで、数字の裏にある未記載の前提を発見し、なぜ問題か・どう補うべきかを示せる | Capability IIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 比較対象となる前例がない、不確実性の高い見積もりを複数経験する | 複数の非標準（前例なし）ケースで見積もり手法自体を設計し、判断理由を説明して他者に教えられる | Capability Owner |

③のChapter 7「定着化とチェンジマネジメント」は、内容的にはTransitionという作業ではなく**人の行動が変わるかどうか**を扱っているため、Capability IIではなくCapability IIIの「Influence／Activation」の教材として整理し直した（下表）。

### 3.3 Capability III｜Stakeholder / Leadership

#### Stakeholder Diagnosis

横串Playbook Ch2（Segment）・Ch3（Diagnose）が教材。「動きそう度×影響力」の2×2でSegmentし、「Logic／Emotion／Ability／Incentive-Environment」の4障壁でDiagnoseする型。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | `playbooks/stakeholder-activation-playbook.md` Ch1〜3を読み、指導者と一緒に実在の関係者1名をSegment＋Diagnoseしてみる | 2×2の4象限と4障壁を自分の言葉で説明でき、指導者同席でSegment・Diagnoseを1回実施できる | 指導者 |
| L1 | L2 | `playbooks/stakeholder-activation-playbook-selfstudy.md`で、実案件の関係者を自分でSegment・Diagnoseする | 条件の異なる関係者2名以上で、Segment（2×2のどこか）とDiagnose（4障壁のどれか）を自力で判定し、特にAbilityとIncentive／Environmentの境界（横串Ch3.2の典型的な混同ポイント）を誤らずに説明できる。診断が「自分の推測」のままでなく、本人への確認を経ていることを示せる | 指導者→OJT先PM |
| L2 | L3 | 他者が行ったSegment・Diagnoseをレビューする | 条件の異なる複数の他者診断で、Segment誤り・障壁誤判定（特にAbility／Incentive-Environment混同）を発見し、なぜ誤りか・どう診断し直すべきかを指摘できる | Capability IIIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 障壁が複数混在する非標準ケース（同じ抵抗の裏に複数原因がある等）を複数経験する | 単一の障壁に収まらない複数の非標準ケースで、どの障壁から手を付けるべきかの優先順位を判断し、理由を説明して他者に教えられる | Capability Owner |

AIとの協働：Segment・Diagnoseの一次仮説をAIに作らせることはできるが、横串Ch3.3が明示する通り「その仮説は本人に確認していない推測のままになっていないか」をL1→L2のEvidenceに明示的に含めている。AIが立てた仮説を検証なしで確定させないことを、他のSkill同様「箱を渡してから埋めさせ、必ず人が検証する」という一貫した扱いにしている。

#### Communication

意思決定者向けに構造化して伝える型（`core/author-voice.md` §3〜4：使う／避ける言葉、1スライド1メッセージ、削る勇気、読者別の説明チェーン）が教材。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | author-voice.md §3〜4を読み、指導者と一緒に1件のスライド／資料を編集する | 「1スライド1メッセージ」の原則と、避けるべきパターン（テンプレ見出し乱用、断定しすぎ等）を2つ以上挙げられる | 指導者 |
| L1 | L2 | 条件の異なる2件以上でクライアント向け資料を自分で作る | 2件以上で、なぜそのトーン・構成にしたかを説明でき、§3〜4の避けるパターンを踏まず、読者（作成者／PO／役員）に応じた説明チェーンに沿った資料を作れる | 指導者→OJT先PM |
| L2 | L3 | 他者のドラフトをレビューする | 複数の他者ドラフトで、「AIっぽい」パターン（author-voice.mdが名指しする回避対象）を発見し、なぜ問題か・どう直すべきかを示せる | Capability IIIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 想定外の読者層・場面での資料作成を複数経験する | 複数の非標準の読者・場面向けにトーンを設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Facilitation

ワークショップの前提条件（事前調査・事前学習・記法トレーニング・Facilitator/Scribe分離）とAnti-Patternsが教材（`standards/scn-creation-guide.md`）。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | scn-creation-guide.mdのPrerequisites・Anti-Patternsを読み、指導者と共同でワークショップを1回ファシリテートする | Facilitator役とScribe役をなぜ分けるのか、Prerequisites（事前調査・事前学習・記法トレーニング）を説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上のワークショップを自分でファシリテートする | 2件以上で、Facilitator／Scribeを分離し、議論が拡散したときになぜ「見える行動」テストで引き戻すべきかを説明しながら実行できる | 指導者→OJT先PM |
| L2 | L3 | 他者がファシリテートする場を観察・レビューする | 複数の観察セッションで、Anti-Pattern（兼務、テーマ過多、IT詳細のSCN混入等）を発見し、なぜ問題か・どう修正すべきかを示せる | Capability IIIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 大人数・高対立の場を複数経験する | 複数の非標準（大人数・高対立）セッションのファシリテーション方針を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Influence／Activation

原因（Diagnose結果）に応じた打ち手の選定（Select）、共通コアと個別化されたReason to Act（Tailor）、行動変化の観察（Observe）、Champion／Key Blocker対応、チャネル選定が教材（`playbooks/stakeholder-activation-playbook.md` Ch4〜8）。定着化のモニタリング（`playbooks/operations-transition-playbook.md` Ch7）も同じ文脈で扱う。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | 横串Ch4〜8を読み、指導者と一緒に診断済みの関係者1名にSelect→Tailorを適用する | 診断された障壁と打ち手の対応関係、共通コアと個別化Reason to Actの違いを説明できる | 指導者 |
| L1 | L2 | 自分のStakeholder Diagnosis（L2）を踏まえ、条件の異なる関係者2名以上でSelect→Tailor→Observeを自分で行う | 2名以上で、なぜその打ち手を選んだか（診断された障壁との対応関係）を説明でき、個別化したメッセージを届け、実際に行動が変わったかを観察・記録できる（打ち手を届けたかどうかで終わらせない） | 指導者→OJT先PM |
| L2 | L3 | 他者の打ち手選定をレビューする | 複数の他者ケースで、診断された障壁と噛み合わない打ち手（例：Logic以外の障壁に「もっと説明する」）を発見し、なぜ噛み合わないか・どう選び直すべきかを示せる | Capability IIIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | Champion／Key Blocker対応と、③Ch7の定着化モニタリング設計を複数経験する | 複数の非標準ケースでChampion活用・Key Blocker解消の方針を、判断理由とともに設計し、定着化指標のモニタリング体制を構築して他者に教えられる | Capability Owner |

#### Governance／Escalation

会議階層の命名とジョブの固定、エスカレーション条件の事前定義（`playbooks/program-governance-cadence.md`）、Steering Committeeの扱い（`playbooks/cross-project-program-management.md` Ch8.5）が教材。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | program-governance-cadence.mdと②Ch8.5を読み、指導者と一緒に会議階層を1件設計する | 5層の会議階層（定例／調整／全体会議／ステコミ／検査）と、なぜエスカレーション条件を「困ったら上へ」ではなく事前に決めるのかを説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上のプログラムでガバナンス設計を自分で行う | 2件以上で、なぜその層に論点を割り当てたかを説明でき、エスカレーション条件を依存／影響／決裁権限で（漠然とした重要性でなく）定義できる | 指導者→OJT先PM |
| L2 | L3 | 他者のガバナンス設計をレビューする | 複数の他者設計で、層の潰れ（例：ステコミが進捗報告会になっている）や曖昧なエスカレーション条件を発見し、なぜ問題か・どう整理し直すべきかを示せる | Capability IIIの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 複数スポンサー・JV等、非標準の統治構造を複数経験する | 複数の非標準統治構造で機能する階層を、判断理由とともに設計し、他者に教えられる | Capability Owner |

### 3.4 Capability IV｜Business / Management Literacy

Capability I〜IIIが「型（プロセス・技法）」であるのに対し、Capability IVは**型を実際のクライアントに正しく当てはめるための事業実務知識**である（詳細は`frameworks/consultant-role-responsibility-model.md` §3〜5）。各Skillに**Prerequisite Knowledge**（Pass／Not Yetで管理する前提知識）を付す。KnowledgeはLevelを持たず、Skill本体のL0〜L4のみ既存の共通Level定義（§2）を使う。「Strategy Consultant Roleとしてどこまで必要か」はRequired LevelとしてRole側（`consultant-role-responsibility-model.md` §5.2）が指定するものであり、Skill自体はL4まで定義する。

#### Company／Financial Analysis

**Prerequisite Knowledge**（Pass／Not Yet）：PL／BS／CFの構造／三表のつながり／Revenue・EBITDA・EBIT等の主要指標／Working Capital／CAPEX／Cash Flow／ROIC等の投資効率指標

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Prerequisite Knowledgeを一通り学び、指導者と一緒に実在企業1社の開示資料を読む | PL／BS／CFの構造と三表のつながりを自分の言葉で説明でき、指導者同席で1社を読める | 指導者 |
| L1 | L2 | 条件の異なる実在企業2社以上の開示資料を自分で読む | 2社以上で、開示資料を自力で読み、Business Model・収益構造・財務状態・主要Riskを整理し、そこから経営課題の仮説を形成して、なぜその仮説に至ったかを説明できる | 指導者→OJT先PM |
| L2 | L3 | 他者の企業・財務分析をレビューする | 複数の他者分析で、誤りや見落とし（指標の読み違い、Working Capitalの見落とし等）を発見し、なぜ問題か・どう直すべきかを示せる | Capability IVの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 財務的に特殊な状況（債務超過、複雑なホールディング構造、海外子会社等）の企業を複数経験する | 複数の非標準企業で分析アプローチを適応させ、判断理由を説明して他者に教えられる | Capability Owner |

#### Business Model／Economics

**Prerequisite Knowledge**（Pass／Not Yet）：収益モデルの類型（サブスク・都度課金・ライセンス等）／固定費・変動費のコスト構造／Unit Economics（LTV・CAC等）／競争力学の基本（バリューチェーン、参入障壁等）

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Prerequisite Knowledgeを学び、指導者と一緒に実在企業1社のビジネスモデルを分析する | 収益モデル・コスト構造の基本を説明でき、指導者同席で1社を分析できる | 指導者 |
| L1 | L2 | 条件の異なる実在企業2社以上のビジネスモデルを自分で分析する | 2社以上で、収益モデル・コスト構造・競争ポジションを自力で識別し、なぜそう判断したかを説明した上でSCNのValue／Capability層に正しく反映できる | 指導者→OJT先PM |
| L2 | L3 | 他者のビジネスモデル分析・SCN Value層設計をレビューする | 複数の他者アウトプットで、ビジネスモデルの理解不足を発見し、なぜ問題か・どう直すべきかを示せる | Capability IVの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | プラットフォーム型・多面市場等、複雑なビジネスモデルを複数経験する | 複数の非標準ビジネスモデルで分析アプローチを適応させ、判断理由を説明して他者に教えられる | Capability Owner |

#### Investment／Business Case

**Prerequisite Knowledge**（Pass／Not Yet）：NPV／IRR／Payback Periodの基本概念／投資評価指標とPDCA用KPIの違い（`playbooks/strategy-scn.md` Ch5の既存記述と直結）／Business Caseの標準構成（コスト・便益・リスク・感度分析）

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Prerequisite Knowledgeを学び、指導者と一緒にBusiness Caseの1セクションを組み立てる | NPV／IRR／Paybackの基本と、投資評価指標とPDCA用KPIがなぜ違うかを説明できる | 指導者 |
| L1 | L2 | 条件の異なる2件以上でBusiness Caseを自分で構築・批評する | 2件以上で、投資ロジックが正しく適用されたBusiness Caseを構築または批評し、主要な前提（割引率、便益の算定根拠等）の判断理由を説明できる | 指導者→OJT先PM |
| L2 | L3 | 他者のBusiness Caseをレビューする | 複数の他者Business Caseで、ロジックの誤り（例：投資指標とKPIの混同）を発見し、なぜ問題か・どう直すべきかを示せる | Capability IVの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | ROIが不確実、または非財務的正当化が必要な非標準案件を複数経験する | 複数の非標準案件で正当化アプローチ自体を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Corporate Governance／Management

**Prerequisite Knowledge**（Pass／Not Yet）：取締役会・執行役員・経営会議の基本構造／上場企業と非上場企業のガバナンスの違い／権限委譲（Delegation of Authority）の基本パターン

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Prerequisite Knowledgeを学び、指導者と一緒に実在クライアント1社の意思決定者を特定する | 典型的な統治構造を説明でき、指導者同席で1社の意思決定者を特定できる | 指導者 |
| L1 | L2 | 条件の異なるクライアント2社以上で統治構造を自分で把握する | 2社以上で、真のSponsor・decision makerとその権限範囲を自力で特定し、なぜそう判断したかを説明した上で、Capability IIIのGovernance／Escalation設計に正しく反映できる | 指導者→OJT先PM |
| L2 | L3 | 他者のSponsor・decision maker特定をレビューする | 複数の他者ケースで、意思決定者の誤認を発見し、なぜ誤りか・どう特定し直すべきかを示せる | Capability IVの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | JV・複数スポンサー等、非標準の統治構造を複数経験する | 複数の非標準統治構造で権限マッピングの方法を設計し、判断理由を説明して他者に教えられる | Capability Owner |

#### Commercial／Contract Literacy

**Prerequisite Knowledge**（Pass／Not Yet）：契約の基本構造（SOW・責任分界・知財・検収条件等）／典型的なベンダー契約のリスクポイント

**範囲の明示**：法的判断を下すことは、L0からL4まで一貫してScope外である。要求するのは「論点を自力で発見し、Business Impactを整理し、Legal等の専門家に確認すべきQuestionへ変換できる」ところまで。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Prerequisite Knowledgeを学び、指導者と一緒に契約上の潜在論点を1件見つける | 典型的なリスクポイント（SOW・責任分界・知財・検収等）を説明でき、指導者同席で1件見つけられる | 指導者 |
| L1 | L2 | 条件の異なる2件以上の標準的な案件で自分で論点を見つける | 2件以上の標準的な案件において、契約・責任分界・知財・検収等の潜在論点を自力で発見し、Business Impactを説明した上で、Legalに確認すべきQuestionとして整理できる | 指導者→OJT先PM |
| L2 | L3 | 他者の論点発見をレビューする | 複数の他者ケースで、見落とされた契約論点を発見し、なぜ見落としたか・何を確認すべきだったかを示せる | Capability IVの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 複数ベンダー・国際契約等、非標準の契約構造を複数経験する | 複数の非標準契約構造で論点発見のアプローチを、判断理由とともに設計し、他者に教えられる（ここでも法的判断そのものは行わない） | Capability Owner |

#### Regulatory／Risk Literacy

**Prerequisite Knowledge**（Pass／Not Yet）：業界別規制の基本カテゴリ（データプライバシー、越境規制、業法等）／規制論点が経営判断に与える典型的な影響パターン

**範囲の明示**：法的・規制解釈の専門判断は、L0からL4まで一貫してScope外である。要求するのは論点発見とBusiness Impact整理まで。

| Current | Target | Learning／OJT | Evidence | 判定者 |
|---|---|---|---|---|
| L0 | L1 | Prerequisite Knowledgeを学び、指導者と一緒に規制上の潜在論点を1件見つける | 主要な規制カテゴリを説明でき、指導者同席で1件見つけられる | 指導者 |
| L1 | L2 | 条件の異なる2件以上の標準的な案件で自分で論点を見つける | 2件以上の標準的な案件において、Cross-border・Data・業規制等の潜在的規制論点を自力で発見し、なぜそこにBusiness Impactがあると判断したかを説明した上で、専門家確認事項として整理できる | 指導者→OJT先PM |
| L2 | L3 | 他者の論点発見をレビューする | 複数の他者ケースで、見落とされた規制論点を発見し、なぜ見落としたか・何を確認すべきだったかを示せる | Capability IVの認定L4 Reviewer（Bootstrap期はCapability Owner） |
| L3 | L4 | 新興技術規制・管轄不明瞭等、非標準の規制領域を複数経験する | 複数の非標準規制領域で論点発見のアプローチを、判断理由とともに設計し、他者に教えられる（ここでも規制解釈そのものは行わない） | Capability Owner |

---

## 4. Source of Truthの状態（更新）

**③ Operations Transition**：`playbooks/operations-transition-playbook.md`（本編）と `playbooks/operations-transition-playbook-selfstudy.md`（自習版）がリポジトリにある。Capability IIに反映済み（§1）。

**横串 Stakeholder Activation**：`playbooks/stakeholder-activation-playbook.md`（本編）と `playbooks/stakeholder-activation-playbook-selfstudy.md`（自習版）がリポジトリにある。Ch2 Segment・Ch3 DiagnoseをStakeholder Diagnosisの教材とし、Ch4〜8 Select／Tailor／Observe／Champion対応／チャネルはInfluence／Activationの教材として展開した（§1・§3.3）。

**「仮説を作る」の教材マッピング検証**：`core/author-voice.md`の中身を確認した。§1.1「思考の型」が Fact → Issue → 仮説 → To-Be → Approach そのものであり、One-Line Summaryも「クライアントのファクトから自分の仮説を立て」から始まっている。したがって仮説構築の教材として妥当と判断し、そのまま残した。ただし同ファイルは§3以降で文章表現・トーンも扱っているため、Communicationの教材としても併記した（§1のCapability III表）。1教材が複数Skillにまたがる例として、本ファイル冒頭の設計原則通りの扱いである。

**③のChapter 6「AI運用のスキル・レベル・教育ロードマップ」**は、`frameworks/ai-operations-role-design.md`（Experimental、確定待ち）に基づく**クライアント側AI運用チームのRole×Maturity Levelモデル**であり、本ファイルが扱う**コンサルタント本人のCapability／Skill／Level**とは対象が異なる別物である。判定を自己申告に頼らず観察可能な証跡（例：「過去3か月で改善提案を1件以上」）で行う方式は、§2のEvidence方式の社内先行事例として参考にした。

---

## 5. 配布物の分離

本ファイルは**Capability Model本体**として、育成担当・マネージャー側のSource of Truthに位置づける。若手本人に渡すのは、ここから生成する**Consultant Learning Map**に分ける。

### 設計原則の更新

前バージョンの例（「通ったら：次はWork Planning／WBSへ」）は次のSkillを固定していたが、これは早すぎる決め打ちである。Learning Mapが出す「次の一歩」は、

**Capability Model（本ファイル） × 本人のCurrent Level × 本人のRole／Assignment（今のアサイン）**

の掛け合わせで決める。§1.5のRecommended Prerequisiteはあくまで「ソフトな示唆」であり、実際のアサインで必要なSkillが優先される。

**Assessment Status**：現在地のLevelには、Confirmed（判定者・判定日つきで確定済み）かProvisional（自己申告・未判定）かを必ず明記する。「〜だと思います」のような曖昧な自己申告のまま配布すると、誰がCurrent Levelを認定したのかがぼやける。ProvisionalのままLearning／OJTへ進めることはできるが、次のLevel判定はConfirmedな現在地を前提に行う。

### プロトタイプ

この設計でSkill「構造化する」（対象者：Current L1・Confirmed、Roleは複数PJ横断案件にアサイン予定）の場合を1件プロトタイプ化した。別ファイル `consultant-learning-map-example.md` を参照。Capability Model（本ファイル）から次の情報だけを機械的に抜き出して組み立てている。

- 現在Level（L1）の共通定義（§2）とAssessment Status
- 該当Skillの L1→L2 行（Learning／OJT・Evidence、§3.1）
- §1.5のRecommended Prerequisiteのうち、次に自然な候補（Work Planning／WBS、ただしRoleが複数PJ横断アサインのため、次点としてDependency Managementも並記）

この変換がうまくいくことを確認できたので、全Skill分のLearning Map化は、§6の運用検証を経てから着手する。

---

## 6. 次に必要なもの

構造設計・4 Capability・24 SkillのEvidence QC・Learning Mapプロトタイプまで完了した。**24 SkillのLevel表は「運用検証前」**として扱う。机上のレビューだけでは、実データを判定したときに出る問題（Evidenceだけでは L1/L2 が決めきれない、案件経験がないSkillの扱い、Prerequisite Knowledgeの確認方法、質の低い2件はどうするか、Prerequisite未達のまま次に進んでいる場合の扱い、Evidence／Knowledgeの保管者は誰か等）が見えないため。

次のステップとして、実在メンバー1名について次を通しで試行する（Capability IVを含む24 Skill対象）。

1. 24 Skill全部のCurrent Level Assessment（自己申告＋Evidence確認）
2. Capability IVについてはPrerequisite Knowledge（Pass／Not Yet）の確認も併せて行う
3. Evidence確認（Confirmed／Provisionalの判定）
4. §1.5 Prerequisiteとの照合（Prerequisite未達のまま先行しているSkillがないか）
5. Assignmentとの照合
6. Learning Map生成（§5の形式で）
7. 次のOJTの決定

これを一度通し、運用上の問題が出なければ「Round 1 Operationally Validated」として確定する。その後で、他Role（PgMO、Transition Manager等）のRole／Responsibility定義へ展開する。1名の試行に使うメンバーの選定と、Evidence／Prerequisite Knowledge確認をどこに記録するかは、着手前に決めておきたい。
