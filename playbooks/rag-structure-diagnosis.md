---
type: playbook
title: "RAG structure diagnosis"
status: active
last_updated: 2026-08-19
related:
  - technology/azure-enterprise.md
  - playbooks/ai-poc-quality-review.md
---

# RAG structure diagnosis

検索は当たっているのに回答が誤るとき、検索・取得・構造化・生成のどこかを切る。製品のクリック手順ではない。表・KPI など行列が意味を持つ文書で特に使う。

## Trigger

- 検索ヒットに正しい値があるが、回答の数字が違う  
- 一般知識に逃げる  
- 表の項目名と値がずれる  
- 出典・ページが返せない  

## Principles

1. 回答だけ見て原因を推測しない。  
   **回答 → トレース → 取得クエリ／文書 → 検索単体 → Chunk → 元文書**  
2. 検索失敗と構造化失敗を分ける。正しい Chunk が取れているなら、最初に Embedding を疑わない。  
3. 表は通常テキストと同じ Chunk にしない。値だけでなく行・列見出しの対応が意味である。  

## Sequence

1. 質問と期待値を人間が原本から固定する（年度、指標名、単位、ページ）。  
2. Knowledge / Search が呼ばれたか。0件や一般知識のみなら、取得前の問題。推測禁止・出典要求を指示に足す。  
3. Agent を外し、検索サービス単体で同じ問いを見る。正しい Chunk が上位にない → Retrieval。ある → Chunk 内部か生成。  
4. 表: 指標名と値が同じ単位にあるか、見出しが落ちていないか、隣接指標と誤対応しやすいか。  
5. Chunk 長を変えても、表構造の崩壊は直らないことがある。本文 Chunk と表 Chunk を分けることを検討する。  
6. 一度に一つの変更で再検証する。  

数値例や特定報告書名はリポジトリに置かない。

## Outputs

- 失敗層（未検索 / Retrieval / Chunk 構造 / 生成）  
- 次の最小変更  
- Ground Truth 行（原本パスはローカル）  

## Related

- `playbooks/ai-poc-quality-review.md`  
- `technology/azure-enterprise.md`  
- `knowledge/lessons/ai-output-evaluation-terms.md`  
- `knowledge/patterns/logical-vs-physical-document-unity.md`  
