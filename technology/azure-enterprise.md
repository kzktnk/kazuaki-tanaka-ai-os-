# Azure Enterprise Technology

**Version:** v0.1  
**Status:** Active  
**Owner:** Kazuaki Tanaka  
**Document role:** Parent file for reusable Azure / integration / identity principles  
**Does not contain:** subscription names, resource names, FQDNs, ports, yen, keys, ARM/Bicep, product click-paths

---

## Purpose

企業の Azure 実装で毎回ゼロから「何を設計単位にするか」を説明し直さないための親ファイル。

製品マニュアルは公式ドキュメントへ委譲する。ここは **拘束と切り分け** だけを持つ。

将来の分離先（厚くなったら。**今は分割しない**）:

- `technology/azure-networking.md`
- `technology/azure-apim.md`
- `technology/azure-ai.md`
- `technology/identity-and-secrets.md`

---

## How to use

閉域・API・502 切り分けなら先に `playbooks/private-api-connectivity-diagnosis.md`。  
本命が使えない暫定経路なら `playbooks/interim-connectivity.md`。  
個人／PoC サブスクの課金なら `playbooks/azure-sandbox-cost-guard.md`。  
RAG で検索は当たるが表の数字が違うなら `playbooks/rag-structure-diagnosis.md`。  
能力地図とトレードオフだけが必要ならこのファイルで止める。

---

## Principle — design the communication chain, not the connector

閉域でフロント（例: Power Platform）から API 管理面を経て業務システムの API に届ける構成は、コネクタ設定の話ではない。

少なくとも次は **一つのチェーン** として設計・障害解析する。

```text
Client / automation
        → Policy / private ingress
        → API gateway (often internal)
        → DNS
        → NSG
        → Route / UDR
        → Firewall
        → Peering / path
        → Backend entry (reverse proxy vs application)
        → Service / protocol
```

NSG が通っていることは、通信できていることと同義ではない。  
Route、Firewall、DNS、証明書、相手側の入口が欠けていれば止まる。

本番化では設定項目を担当別にバラバラに管理しない。**End-to-end の通信チェーン**として見る。

---

## Principle — the API gateway is a contract face, not the system

API Management はバックエンドの実装ではない。公開面・認証・観測・経路の契約である。

確認する単位:

- Backend URL は **どの環境の、どの入口の、どの path** か  
- Subscription / 認証は検証都合で外した条件を、本番へ持ち込めない  
- Gateway 診断ログは、フロントのエラーコードより先に読む  

ポータルの Test タブが無い／使えない API がある。そのときは **実クライアントからの要求 + gateway log** で経路を確認する。Test タブの有無を設計品質と混同しない。

---

## Principle — name the route, not “it connected”

「疎通できた」は記録として不足する。最低限セットで残す。

- environment (dev / test / prod)  
- FQDN  
- port  
- path  
- entry (reverse proxy / dispatcher vs application host)  
- who resolved DNS, from which VNet  

環境を切り替えたら URL だけ変えればよい、ではない。DNS、Firewall、NSG、Route、Peering、証明書、認証、相手サービスの有効化を **一括で** 確認する。ある環境で許可済みの宛先が、次の環境では未許可、はよく起きる。

---

## Principle — client HTTP status is a symptom

フロントの 502 / 500 は、フロントが原因だとは限らない。下流の到達失敗や相手システムのエラーが、フロントのコードに包まれる。

Gateway log で切る:

| Observation | Meaning |
|-------------|---------|
| Request never arrives at the gateway | Client → gateway path |
| Backend response code empty | Failed before an HTTP answer from the backend (DNS, network, TLS, wrong host/port) |
| Backend 401 / 403 | Identity / authorization on the backend |
| Backend 404 | Path or service not published |
| Backend 5xx | Backend processing |
| Backend 200, client still unhappy | Connectivity is done. Payload shape, connector mapping, or app logic is a **different** problem |

HTTP 200 は通信成立である。応答が structured / unstructured、JSON / XML であることは、別設計である。

---

## Principle — authentication follows the execution host

「SDK で Azure を呼ぶ」と「Managed Identity で認証される」は同じことではない。

- Azure の外で走るノートブック／手元のコード → ユーザー資格（device code 等）  
- Azure 上のサービス → Managed Identity + RBAC  

UI の世代が変わって Identity のスイッチが見えないことはある。検証を UI に固定せず、**実行場所に合う認証**を選ぶ。

ログイン失敗は Storage やコードの問題ではなく、**リソースのあるテナントと、選んだアカウントの所属が違う**ことが多い。

---

## Principle — treat high-fixed-cost SKUs as explicit decisions

学習や短期間の PoC でも、存在しているだけで大きく課金される SKU（例: Managed HSM 相当）が混ざり得る。

- 作るリソースと SKU を事前に一覧化する  
- Cost Analysis を作成当日・翌日に見る  
- Portal から消したことと、課金が止まったことを同義にしない（soft delete、固定時間課金）  
- 個人 Sandbox は Budget / alert を先に置く。不要ならサブスクリプション単位で止める  

円・請求書・サポート文面はリポジトリに置かない。手順は `playbooks/azure-sandbox-cost-guard.md`。

### Principle — interim is not the new target

本命の閉域チェーンが未承認でも、最小の暫定（gateway VM、Bastion 管理）で検証を続けてよい。

同時に記録する: 何が揃ったら暫定を殺すか、何を消すか、本命で何を再検証するか。

サインイン失敗に見えても、先に DNS・outbound 443・Proxy を見る。Identity / RBAC はその後。公式の宛先リストはベンダー文書に残し、ここには固定しない。

---

## Do not mix

- Domain（電力・公共）の事業拘束と、Azure の経路設計を一つの「業界ファイル」にしない  
- 公式ドキュメントの操作手順をここにコピーしない  
- クライアントの VNet 図・ホスト名・鍵を一般化せずに残さない  

---

## Related files

| Layer | File |
|-------|------|
| Technology parent | this file |
| Playbook | `playbooks/private-api-connectivity-diagnosis.md` |
| Playbook | `playbooks/interim-connectivity.md` |
| Playbook | `playbooks/rag-structure-diagnosis.md` |
| Playbook | `playbooks/azure-sandbox-cost-guard.md` |
| Decisions | `knowledge/decisions/diagnose-from-gateway-not-client-error.md`, `knowledge/decisions/sandbox-cost-controls-before-resources.md`, `knowledge/decisions/interim-connectivity-is-not-the-target.md` |
| Migration | `knowledge/migrations/azure-enterprise-2026-08.md`, `knowledge/migrations/ai-playbooks-2026-08.md` |
