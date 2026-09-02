# Document ID Registry

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Purpose:** このリポジトリが払い出す文書・様式 ID の台帳。案件原本の番号は使わない。

---

## Issuance rule

```
AIOS-{KIND}-{NN}
```

| KIND | 対象 |
|------|------|
| **REC** | 記録類アーキタイプ（議事・進捗・問題・変更） |
| **COV** | 表紙・改定履歴・台帳アーキタイプ |
| **BLD** | 開発成果物アーキタイプ（要件・設計・試験） |

- 実様式ファイルはリポジトリに登録しない。**ID と用途**だけをここに置く。
- 新規 ID は末尾連番で追加する。欠番は再利用しない。
- 案件側の文書番号が必要なときは、案件リポジトリで別体系を定義する。本台帳をコピーしない。

---

## AIOS-REC — 記録類

| ID | 名称 | 用途 |
|----|------|------|
| **AIOS-REC-01** | 議事録 | 会議記録、決定・宿題の合意 |
| **AIOS-REC-02** | 進捗報告書 | 進捗・問題・確認事項の簡潔報告 |
| **AIOS-REC-03** | 進捗管理表 | 予実管理、遅延週数（±nW） |
| **AIOS-REC-04** | 問題管理表 | 問題/課題の一元管理（A–D重要度） |
| **AIOS-REC-05** | 設計連絡票 | 仕様確認・影響調査 |
| **AIOS-REC-06** | 設計連絡票管理簿 | 設計連絡の台帳 |
| **AIOS-REC-07** | 仕様確認書 | 仕様確定時の確認 |
| **AIOS-REC-08** | 仕様確認依頼書兼回答書 | 仕様変更の正式通知 |
| **AIOS-REC-09** | 仕様変更管理簿 | 変更履歴台帳 |
| **AIOS-REC-10** | 問題記述票 | レビュー指摘の記録・修正追跡 |
| **AIOS-REC-11** | 障害処理票 | 試験障害の記録・修正 |
| **AIOS-REC-12** | 障害処理管理簿 | 障害処理の台帳 |

本文の運用は `standards/development-management-guide.md` §Tool Catalog。

---

## AIOS-COV — 表紙・台帳

| ID | 用途 |
|----|------|
| **AIOS-COV-01** | 表紙 |
| **AIOS-COV-02** | 変更履歴 |
| **AIOS-COV-03** | 文書履歴管理台帳 |
| **AIOS-COV-04** | 文書配布管理台帳 |

本文の運用は `standards/document-management-standard.md` §Form Archetypes。

---

## AIOS-BLD — 開発成果物

### 要件定義

| ID | 成果物 | 作成単位（例） | MIN |
|----|--------|---------------|-----|
| **AIOS-BLD-01** | 機能一覧 | システム | ○ |
| **AIOS-BLD-02** | ビジネスルール定義書 | 業務/サブ業務 | ○ |
| **AIOS-BLD-03** | アクティビティ図 | サブ業務 | ○ |
| **AIOS-BLD-04** | ユースケース図 | サブ業務 | |
| **AIOS-BLD-05** | 画面一覧 | 業務 | |
| **AIOS-BLD-06** | 画面遷移図 | サブ業務 | |
| **AIOS-BLD-07** | 画面レイアウト | レイアウト | |
| **AIOS-BLD-08** | 帳票一覧 | 業務 | |
| **AIOS-BLD-09** | 帳票レイアウト | レイアウト | |
| **AIOS-BLD-10** | 外部I/F一覧 | 業務 | |
| **AIOS-BLD-11** | ドメイン定義書 | システム | |
| **AIOS-BLD-12** | コード定義書 | 業務 | |
| **AIOS-BLD-13** | 概念ER図 | 業務 | |
| **AIOS-BLD-14** | エンティティ定義書 | エンティティ | |
| **AIOS-BLD-15** | ファイル一覧 | 業務 | |

### 設計/製造

| ID | 成果物 | MIN |
|----|--------|-----|
| **AIOS-BLD-16** | プログラム一覧 | |
| **AIOS-BLD-17** | メッセージ定義書 | |
| **AIOS-BLD-18** | ユースケース記述 | |
| **AIOS-BLD-19** | ステートチャート図 | |
| **AIOS-BLD-20** | 画面仕様書 | |
| **AIOS-BLD-21** | 処理定義書（リクエスト/画面/バッチ） | |
| **AIOS-BLD-22** | 帳票仕様書 | |
| **AIOS-BLD-23** | 外部I/F仕様書 | |
| **AIOS-BLD-24** | 外部I/F定義書 | ○ |
| **AIOS-BLD-25** | ビュー定義書 | |
| **AIOS-BLD-26** | バッチ一覧 | |
| **AIOS-BLD-27** | バッチ構成図 | |
| **AIOS-BLD-28** | ファイル定義書 | |
| **AIOS-BLD-29** | ファイル定義書(XML) | |

### 試験

| ID | 成果物 | MIN |
|----|--------|-----|
| **AIOS-BLD-30** | 総合試験項目表 | ○ |
| **AIOS-BLD-31** | 総合試験シナリオ | ○ |

本文の運用は `standards/deliverable-archetypes.md` Archetype G。

---

## Related Assets

| ファイル | 関係 |
|---------|------|
| `standards/document-management-standard.md` | 番号の型・承認・台帳 |
| `standards/development-management-guide.md` | 記録類の使い方 |
| `standards/deliverable-archetypes.md` | 開発成果物カタログ |
