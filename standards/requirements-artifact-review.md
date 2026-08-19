# Requirements Artifact Review Standard

**Version:** v1.0  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Origin:** Generalized from business-side review of customer-data-platform / CRM requirements packs (utility retail program). No client, vendor, or requirement text.

---

## Purpose

要件成果物を、開発者が正しいかだけでなく、**業務側が導入後に困らないか**で見る。  
確認結果は成果物修正と課題台帳に戻す。コメントの山で終わらせない。

`standards/requirements-document-outline.md` が章立て。本書は **レビュー観点の分担**。

---

## When to Use

- CDP / CRM / CIS など顧客系の要件・外部設計レビュー
- SI 成果物を事業側が短時間で見るとき
- 「ヒアリングしたのに要件に無い」「自動化しすぎた」を防ぐとき

---

## Two review benches

観点を一人に集めない。**構築側**と**業務側**で主担当を分ける。内製・ベンダ支援が後から入るなら、8観点を広く見る役割を明示する。

### Build-side (typically SI / requirements author)

1. **Hearing fidelity** — 記載はヒアリング結果と一致しているか（用語の層を取り違えていないか）。  
2. **Requirement coverage** — 集めた要求が要件に落ちているか。入力元の漏れ。  
3. **Open items** — 未確定が QA / 業務一覧から漏れていないか。  
4. **Internal consistency** — 機能・システム間で要件が矛盾していないか。

### Business-side (typically process / CX / operations owner)

5. **No dropped work** — 必要な業務を消していないか。  
6. **Simplification** — 詳細化した業務に、前工程へ寄せる効率化余地が無いか。  
7. **Operating capability** — 導入効果を出す体制（誰が使う・直す・測るか）があるか。  
8. **Adjacent change plans** — 連携システムの改修時期・方式と整合しているか。当面の暫定（手動アップロード等）が書いてあるか。

---

## HITL check (viewpoint 5)

一律自動化してよいものと、人が確認する余地を残すものを分ける。  
リスト確定・告知対象・苦情由来の除外などは、自動化が責任を消さないようにする。

See `frameworks/human-oversight.md`, `knowledge/patterns/exception-as-memory-entry.md`.

---

## Output of a review

| Output | Use |
|--------|-----|
| Artifact comments | 誤記・漏れの修正 |
| Issue log | 未確定・過渡期・連携 |
| Scope cuts | やらない機能（本設データが無い等） |
| Enablement gaps | 観点7で体制が無いなら、開発と同時に計画 |

---

## Related

- `standards/requirements-document-outline.md`
- `standards/consulting-review.md`
- `domains/energy-utilities.md`
- `knowledge/patterns/platform-build-vs-enablement.md`
- `knowledge/index/legacy-source-index.md` Program Line K
