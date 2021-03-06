# ログインについてのまとめ

## Authorizationヘッダとは
- 認証の種類、ユーザ名、パスワードをサーバに知らせて認証するためのヘッダ

- ヘッダのフォーマット
  - typeは`Basic`や`Digest`や`Bearer`など色々ある
  - credentialsは`<ユーザ名>:<パスワード>`の形式を
  - http://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml

  ```
  Authorization: <type> <credentials>
  ```

## 認証の種類
### Basic認証
- Authorizationヘッダを用いた認証
- 動作
  - 1.ブラウザがあるページを要求する（この時点でクライアントは認証が必要なことを知らない）
  - 2.サーバがWWW-Authenticateヘッダに「Basic」をセットした401 Authorization Requiredを返信してBasic認証が必要なことを伝える
  - 3.ユーザがユーザ名とパスワードをブラウザに入力する
  - 4.ブラウザはユーザ名とパスワードを「:」でつなげてBase64でエンコードしてAuthorizationヘッダにセットしてRequestを送る
  - 5.サーバはユーザ名とパスワードをBase64でデコードして認証を行う
  - 6.認証が成功するとサーバは要求されたページを送る
  - 7.ブラウザは認証状態をキャシュし、キャッシュがクリアされるまでユーザが再認証を要求されることはない
- ログアウトの仕組みがないためネットショップのようにセッションを厳密に管理したい用途には向かない
### Digest認証
- Authorizationヘッダを用いた認証
- 動作
  - 1.ブラウザがあるページを要求する（この時点でクライアントは認証が必要なことを知らない）
  - 2.サーバがWWW Authenticateヘッダに「Digest」とランダムな文字列（nounce）をセットした401 Authorization Requiredを返信してDigest認証が必要なことを伝える
  - 3.ユーザがユーザ名とパスワードをブラウザに入力する
  - 4.ブラウザはパスワードをnouceとクライアントが生成したランダムな文字列（cnouce）を組みあせてハッシュ（response）を計算する
  - 5.ブラウザはAuthorizationヘッダにユーザ名、nouce、cnounce、responseをセットしてRequestを送る
  - 6.サーバはユーザDB内のパスワード、nouce、cnouceからハッシュを計算してresponseと一致するか確認する
  - 7.認証が成功するとサーバは要求されたページを送る
  - 8.ブラウザは認証状態をキャシュし、キャッシュがクリアされるまでユーザが再認証を要求されることはない
- ブラウザが前提だがWeb APIの場合は事前に認証が必要なことを知っているので手順1〜3がなくなる
- パスワードそのものを送らないことでBasic認証よりセキュリティを強化しているが、世間一般から見れば脆弱極まりない認証方式だ。Digest認証方式を採用する場合はHTTPSを使うことは必須となる
### Bearer認証
- Authorizationヘッダを用いた認証
- Bearer認証は, トークンを利用した認証・認可に使用されることを想定しており, OAuth 2.0の仕様の一部として定義されているが, その仕様内でHTTPでも使用しても良いと記述されている
### セッション&クッキー
- サーバサイドで認証状態を保持する
- はじめにサーバはクライアントにランダムな値のセッションIDを送る。
- サーバはセッションIDと紐付ける事でクライアントの状態を保持できるため、認証が成功すれば、その後はセッションIDの確認だけで認証が不要になる
- セッションIDは盗まれても、ワンタイムなのでそこまで痛くない。一定期間で無効になるし、パスワード情報が何もない
- また、セッションには認証だけでなく、それまでのやり取りのステート（例えばショッピングカートにアイテムを入れる）も保存することが可能
- セッションIDはクッキーに入れて送受信する
### OpenID Connect
- クライアントサイドで認証状態を保持する
### JWT認証
- クライアントサイドで認証状態を保持する
- 疑問点としては、authorizationヘッダのtypeは何を指定するのかということ
### 参考文献
- Basic、Digest、Bearer、OAuthの違い
  - https://architecting.hateblo.jp/entry/2020/03/27/130535
- Bearer認証まとめ
  - https://qiita.com/h_tyokinuhata/items/ab8e0337085997be04b1
- OpenID Connect、JWT、セッション
  - https://fintan.jp/?p=1387
- HTTPの認証でBearerを使ってもいいのかどうか
  - https://qiita.com/uasi/items/cfb60588daa18c2ec6f5
  - https://qiita.com/hirohero/items/d74bc04e16e6d05d2a4a
- JWTはBearerで送れる
  - https://qiita.com/YukiMiyatake/items/4c2162f85fe3c9c203a7#jwt
- 認証まとめ
  - https://qiita.com/YukiMiyatake/items/4c2162f85fe3c9c203a7

<br></br>

## アーキテクチャ別ログイン機構
- 最近はBearer認証にJWTを使うのが流行りっぽい
- https://qiita.com/hirohero/items/d74bc04e16e6d05d2a4a
### モノリシックなアーキテクチャを採用する場合、フロントエンドのバックエンドで使うAPIに徹する場合
- セッションIDをクッキーで送受信するのが良い
- クッキーを使用する際の利点
  - HttpOnlyなCookieでセッションを扱えるので、スクリプトを通じた窃取に強い
  - サーバサイドで利用者ごとにセッションデータを保持するので、有事のときに特定利用者のセッションを簡単に無効化できる
  - ウェブアプリケーションフレームワークでセッション機構がサポートされている場合、その機能を使うことでコードの見通しがよくなる

![spa-ssr-api-architecture](https://user-images.githubusercontent.com/53253817/103914696-93dd0800-514d-11eb-8c6f-8d2a7f5deace.png)

- 参考文献
  - https://tech.pepabo.com/2020/09/23/session-management-for-web-apps-using-spa-ssr-api/

### マイクロサービスアーキテクチャを採用する場合
- サーバでセッションを管理せず、クライアントが渡してくるクレデンシャルを使って都度認証するというステートレスな方式が用いられる


### 外部にも公開するAPIの場合
- Authorizationヘッダを使った方法が一般的
- このような場合だとクッキーは使用しないらしい

<br></br>

## JWT認証のフロー
- 認証に必要となる情報はすべてJWTの中に入っているため、ユーザー認証情報をサーバーで管理する必要がない。DB問い合わせを行う必要がない。
  - セッション情報をDBに保管しないということ
- https://techblog.roxx.co.jp/entry/2019/03/13/135739
### 初回ログイン
- フロント
  - ユーザー情報 (メールアドレス、パスワード等) を送信
- サーバー
  - リクエストされたユーザー情報を元にJWTでトークンを生成
  - トークンをフロントへ返す
- フロント
  - 返ってきたトークンがbase64urlでエンコードされているため、base64 に変換
  - 変換したものをLocalStorageに保存
### 二回目以降のログイン・画面更新時
- フロント
  - Tokenの有無の確認
  - LocalStorageにTokenがあるかどうかを確認
    - ある場合は、HTTPヘッダに入れてサーバーにアクセスする
    - ない場合は、そのユーザータイプによって適切なページへリダイレクトさせる
- フロント
  - Tokenの有効期限の確認
    - LocalStorageにTokenがある場合、その有効期限を確認
    - 有効期限が切れている場合、サーバーに問い合わせし、Tokenを更新
- サーバー
  - Tokenの更新リクエストがきたらJWTをリフレッシュして返す（このときフロントでは、初回登録時と同じように返ってきたトークンをLocalStorageに保存します）
- フロント
  - サーバーにアクセス
    - 有効なアクセスであることがフロントで確認されたらサーバーにアクセスをします
- サーバー
  - トークンの認証を確認しデータを返す
