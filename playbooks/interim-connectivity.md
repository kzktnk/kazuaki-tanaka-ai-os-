---
type: playbook
title: "Interim connectivity"
status: active
last_updated: 2026-08-19
related:
  - technology/azure-enterprise.md
  - knowledge/decisions/interim-connectivity-is-not-the-target.md
  - playbooks/private-api-connectivity-diagnosis.md
---

# Interim connectivity

本命の閉域構成（例: ポリシー面 → API 管理 → モデル／業務 API）がまだ使えないとき、原則を崩さず検証を進める暫定経路を決める。Gateway 製品のインストール手順ではない。

## Trigger

- 本命コンポーネントが未承認・未提供で PoC が止まる  
- 中継 VM / on-premises gateway が候補になる  
- Public IP を付ければ進むが、顧客標準に合わない  

## Sequence — design

1. **本命構成を先に書く。** 暫定を新しい本命にしない。  
2. 使えない理由を「技術的に不可」と「今は時間が足りない」に分ける。  
3. 守る制約: 不用意な Public IP、Internet RDP、顧客標準外の管理経路、不要な恒久リソース、本命移行を阻害する例外。  
4. 暫定は最小。管理は Bastion 等の承認済み経路。  
5. 出口: 何が揃ったら廃止か、何を消すか、本命で再検証する項目、暫定でしか成立しない設定。  

Stop: Public 公開が必須、移行方法が言えない、恒久例外、セキュリティ承認が必要な変更を黙って入れる。

## Sequence — gateway / outbound looks like auth failure

認証・RBAC を最初に疑わない。Windows ログイン、Azure RBAC、Gateway サインイン用アカウントは別問題。

順: 管理経路で VM に入れるか → DNS → 必要な outbound（通常 TCP 443）→ OS / サービス / 企業 Proxy の違い → その後にテナント・権限・ライセンス。

「Internet に出られる」と「そのアプリが必要な経路で出られる」は同義ではない。宛先リストは公式の最新要件を見、ここに固定しない。

## Outputs

- 本命図 / 暫定図 / 差分  
- 採用理由と廃止条件  
- 切り分けで止まった層  

## Related

- `knowledge/decisions/interim-connectivity-is-not-the-target.md`  
- `playbooks/private-api-connectivity-diagnosis.md`  
- `playbooks/azure-sandbox-cost-guard.md`  
