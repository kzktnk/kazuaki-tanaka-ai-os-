---
name: issue-structuring
description: 案件の論点整理・初期仮説づくり。「論点整理して」「初期仮説を作って」「イシューツリー」「4Cs & 1Q」「提案の骨子の前に問いを固めたい」、RFP・議事メモ・顧客資料から何を検討すべきかを構造化する依頼で使う。WBS 詳細化や提案書の体裁づくりには使わない。
---

# 論点整理・初期仮説（Issue Structuring）

入口だけを書く。手順は Rule、原典は Knowledge にある（`knowledge/patterns/skills-point-to-rules-not-source.md`）。

## 1. 読むもの（この順・最小限）

必ず:
- `standards/strategy-engagement-guide.md` の §Problem Scoping Workflow（Step 1〜3）と §Engagement Quality Checklist ← **手順の本体**
- `core/reasoning.md`（事実と仮定を分ける）

条件つき:
- 顧客の問いが症状レベル／打ち手先行 → `frameworks/thinking-patterns/pattern-01-why-what-how.md`
- 現状と目指す姿の差が論点 → `frameworks/thinking-patterns/pattern-02-as-is-gap-to-be.md`
- 業界が明確 → `domains/energy-utilities.md` / `domains/public-defense.md`
- 仕上げ前 → `frameworks/consulting-strategy-process.md` の §Common Failure Modes のみ

読まないもの: `frameworks/` 全体、`knowledge/source/`、`playbooks/wbs-design.md`（Gate 2 の仕事）。

## 2. 入力と置き場所

- 入力: ユーザーが指定したファイル（RFP、議事メモ、顧客資料）と一言の指示。足りなくても止まらない。
- 出力: `outputs/<案件名>/YYYYMMDD_論点整理_v01.md`（`outputs/` は .gitignore 済み）。
- 顧客の実名・機密情報をリポジトリの追跡対象ファイルに書かない（`projects/README.md`）。

## 3. 進め方

Rule の Step 1〜3 に従う。このスキルで足すのは次の規律だけ。

1. **4Cs & 1Q** を埋める。各項目に `[事実]` `[仮定]` `[不明]` のいずれかを付け、事実には入力資料の出典（ファイル名・該当箇所）を書く。
2. **ツリーの型を選ぶ**（Rule の Tree selection matrix）。選んだ理由を1行で残す。
3. **論点ツリー**を作る。末端は問いの形。各末端に初期仮説を1つ。
4. **仮説ごとに、支持する事実と支持しない事実の両方**を書く。反証材料が見つからなければ「未確認」と書き、空欄にしない。
5. **分析計画表**（Issue / Hypothesis / Analysis / Information source / End product）。End product は「どの図で何が言えるか」まで書く。
6. **ストーリーボード**は章タイトル（＝各章のメッセージ1文）だけ。スライド化はしない。

## 4. 人が判断する点

次の3点は AI が決めない。候補を並べ、`【要判断】` を付けて冒頭に集める。

- Key Question の一文（顧客が本当に答えを欲しい問いか）
- Criteria（顧客が実際に何で意思決定するか）
- どの仮説から検証に着手するか（優先順位）

ユーザーが不在（夜間に投げられた等）でも止まらない。最も妥当な読みで進め、その読みを冒頭に1行で書く。

## 5. 出力の形

冒頭に「朝いちばんに見る3点」:
1. 採用した Key Question（案）
2. `【要判断】` の一覧
3. 最も確度の低い仮説と、その理由

その後に 4Cs & 1Q → 論点ツリー → 仮説と賛否の事実 → 分析計画表 → ストーリーボード（章タイトル）→ 自己検証結果。
文体は `standards/writing.md`（結論先行、1セクション1メッセージ）。

## 6. 自己検証（出す前に必ず）

Rule の §Engagement Quality Checklist「Before analysis starts」と Step 1・2 の Quality checks / MECE tests を一項目ずつ判定し、満たさない項目は理由つきで出力末尾に残す。「全部OK」で済ませない。Work plan など本スキルの範囲外の項目は「範囲外・次工程」と書く。加えて:

- 入力資料にない事実を `[事実]` にしていないか
- 論点ツリーの各枝が Key Question に辿れるか
- 打ち手（How）が論点（What）より先に出ていないか

## やらないこと

- WBS・ベンダー選定・体制図（Gate 2 以降）
- 顧客の意思決定基準を推測で確定させること
- 提案書の体裁づくり（別スキル）
