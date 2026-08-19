---
type: playbook
title: "Private API connectivity diagnosis"
status: active
last_updated: 2026-08-19
related:
  - technology/azure-enterprise.md
  - knowledge/decisions/diagnose-from-gateway-not-client-error.md
---

# Private API connectivity diagnosis

フロント（Power Platform 等）から閉域の API ゲートウェイを経てバックエンドへ届ける構成で、エラーが出たときに使う。

## Trigger

- クライアントが 502 / 500 / timeout を返す  
- 「昨日まで通っていた」環境切替の直後  
- ゲートウェイの Test タブが無い、または Test と実経路が違う  

## Objective

フロントの HTTP コードを原因と確定せず、**失敗している層**を特定する。

## Do not start with

- コネクタやアプリだけを疑う  
- 「SAP / バックエンドへ疎通できた」という一文で打ち切る  
- NSG が許可されていることだけを根拠にする  

## Sequence

1. **ゲートウェイに要求は来たか**  
   来ていなければ、クライアント → ゲートウェイ（ポリシー、閉域入口、認証）を先に見る。

2. **Backend の HTTP 応答はあるか**  
   - 空 → 到達前（DNS、NSG、UDR、Firewall、Peering、FQDN、port、TLS）  
   - 401 / 403 → 相手の認証・権限。開発用の資格を流用していないか  
   - 404 → path / サービス未公開  
   - 5xx → 相手システムの処理  
   - 200 → 通信は成立。応答形式・コネクタ写像は別チケット  

3. **入口を取り違えていないか**  
   リバースプロキシ／ディスパッチャと、アプリケーションホストは別経路である。ポートとホストをセットで確認する。

4. **環境切替なら URL 以外を一括確認する**  
   Backend URL、DNS（想定 IP か）、Firewall、NSG、UDR、Peering、証明書、認証、相手サービスの有効化。

5. **記録する**  
   environment / FQDN / port / path / entry / 失敗層。金額・実ホストは原本のみ。

## Decision points

- Backend 200 なのにクライアントが失敗 → この playbook の対象外（データ形状・アプリ）。疎通担当を解放する。  
- 要求がゲートウェイに無い → ネットワーク担当ではなく、まずクライアント〜ゲートウェイ。  

## Quality checks

- 失敗層が、チケットの宛先（ネットワーク / API / 相手システム / アプリ）と一致している  
- 「通った」が経路セットで書ける  

## Outputs

- 失敗層  
- 次の確認オーナー  
- 環境切替チェックの過不足  

## Related

- `technology/azure-enterprise.md`  
- `knowledge/decisions/diagnose-from-gateway-not-client-error.md`  
