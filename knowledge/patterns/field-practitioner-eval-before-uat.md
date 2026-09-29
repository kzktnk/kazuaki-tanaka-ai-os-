# Pattern: Field Practitioner Eval Before UAT

**Status:** Active  
**Origin:** Generalized from a buyer-side prototype briefing and blank feedback template (2026-09). Client names, plant names, people, filled rows, and vendor decks are **not** stored here.

## Pattern statement

> **プロトタイプの現場検証は、正解率コンテストではない。職種・拠点の実務者が、いまの仕事の問いをそのまま入れ、「使えるか／根拠を確認できるか／何を直せば使えるか」を見る。1問は1行。失敗の分類は改善の種類に直結させる。改善を挟んだ2波で測る。検証中の回答を業務判断に使わない。失敗の方が改善に効く。**

発注者側の PoC 品質（要求→指標→Go）は `playbooks/ai-poc-quality-review.md`。正解の持ち主は `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`。本パターンは **UAT の前に、現場がプロトタイプをどう試すか** である。

## Core distinction

| ベンダー／本社が見るもの | 実務者に見てもらうもの |
|---|---|
| 正解率、デモのきれいさ | 普段の言葉で聞けるか、業務で使えるか |
| 機能が動いた | 参照元が示され、原本で確かめられるか |
| 平均スコア | 職種・拠点で使い方が違うか |
| UAT で一括確認 | プロトタイプで直し、UAT はリリース前の別仕事 |

画面の「使える／使えない」ボタンは入口である。チューニングに使うなら、任意でも次が要る。

- 入力した質問文そのもの（再現用）  
- 気になった点の分類（改善の種類へ振る）  
- 期待していた回答（分かる範囲で）  
- 本来参照してほしい資料の名と置き場所  

これが現場から来る Ground Truth である。ベンダーだけで正解を決めない。

分類は不満の感想で止めない。改善の種類に写す。

| 現場の分類 | 改善の種類 |
|---|---|
| 内容が誤っている／不足 | 参照データ、生成の見直し |
| 参照元が出ない・的外れ | 検索精度、参照元表示 |
| あるはずの資料が出ない | 対象コーパスの追加 |
| 社内用語が通じない | 用語辞書、プロンプト |
| 正しいが使いにくい | 回答形式 |
| 画面が使いにくい | UI。中身の正解率と混ぜない |
| 良かった点 | 改善時に悪化させない確認用 |

優先は業務影響（判断を誤る／手直しすれば使える／好み）で切る。全部を同じ深さで直さない。

2波が基本である。1波の意見を反映してから、同じ問いで再確認する。1波だけで「現場は使えた」としない。

試す問いの作り方:

- 最近実際に調べた・困ったことをそのまま入れる  
- 言い方を変えて同じことを聞く  
- 他所の事例、複数資料にまたがる問いも入れる  
- うまくいかなかった問いこそ残す  

検証中は、回答を業務判断に使わない。原本確認が先である。

## Signals

- 正解率だけを現場検証の目的にしている  
- 本社／ベンダーが「使えるか」を代弁している  
- ボタン評価だけで、期待回答も参照資料も取っていない  
- 分類が感想のまま、改善バックログに落ちない  
- 1波のあと改善せずに「現場確認済み」としている  
- プロトタイプの答えを、検証期間中に業務判断へ使っている  
- 成功例だけ集め、失敗を恥として隠している  

## Core rule

> Practitioners judge field fitness. One query, one row. Map the miss to an improvement type. Two waves with an improvement window. Ground truth is the expected answer plus the document that should have been retrieved. Do not use prototype answers for live decisions.

## Related

- `playbooks/ai-poc-quality-review.md` — 発注者側の要求〜Go  
- `knowledge/decisions/buyer-owns-ai-poc-ground-truth.md`  
- `knowledge/patterns/define-success-before-prompt-change.md` — 成功条件が先、回帰を見る  
- `knowledge/patterns/activation-first-for-site-led-work.md` — 現場主体は役割が先  
- `knowledge/lessons/ai-output-evaluation-terms.md`  
- `domains/energy-utilities.md`  
