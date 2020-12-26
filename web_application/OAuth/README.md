# OAuth関連のまとめ、書籍メモ
- 読む本
  - https://authya.booth.pm/items/1296585
  - https://authya.booth.pm/items/1550861
  - https://authya.booth.pm/items/1877818
- DNS,SSLの読む本
  - DNSは買ったから届くのまち
  - https://booth.pm/ja/items/1834443

## 0. 自分のメモ
- https://dev.classmethod.jp/articles/deep-think-about-oauth-authentication/
- https://qiita.com/doyaaaaaken/items/02357c2ebca994160804
- https://christina04.hatenablog.com/entry/2016/06/07/123000
### 0-1. 認証とログインの違い
- 認証: 「システムを操作している人物が確かにこの ID の持ち主であると確認すること」を指す。あえて言えば、認証というのはその「瞬間」のことを指す
  - 認証は、自前で用意するパターン(勉強の際だけかな)、OAuthを使うパターン(本番では使ってはいけない)、OpenID Connectを使うパターン(本番ではこれ)などがある
- ログイン: 「その結果をいつまで信頼するのかというポリシーを適用し、認証に期間を与えること」を指す
  - 自分のサーバで自前でセッション管理をする
  - フレームワークのアドオンで提供されていたりするかも
    - Djangoならdjango-user-sessions
    - FastAPIならfastapi-userとかfastapi-utilとか
### 0-2. Webアプリの普通のログインの実現方法
- Cookie-Based Authenticationと呼ばれている
- 認証もログインも自分のサーバで提供するパターン
- 手順
  1. ID とパスワードを確認することによって 認証 (瞬間) を行う
  2. 1ができ次第、「セッション」という cookie ベースの仕組みを使ってログイン (期間)を実現
- 注意点
  - セッション管理はどの認証方法でも自前で管理する必要がある。OAuthやOpenIDを使ったからといって、自分のサーバでは何もしなくていいかというとそういうわけではないので注意する
### 0-3. WebアプリにおけるOAuthログインの実現方法
- Token-Based Authenticationと呼ばれている
- 認証をOAuthを使って、ログインは自前で提供するパターン
- OAuth は認証のためのプロトコルではないので、正しく外部連携認証を実装するのであれば OpenID Connect を使う。以下の手順は**認証**として使ってしまっているので参考までにとどめる
- 手順
  1. Facebook などの OAuth プロバイダーに対して所定の手続きを踏むと、Web アプリはアクセストークン (以下、AT) を手に入れる
  2. この AT を使って、Facebook 等のプロフィール API 的なものを叩けば、その人の ID が確定し、認証 (瞬間)ができる
  3. 普通のログインと同じように、認証できた段階でセッション ID cookie を発行してセッションを確立
  4. そのセッションの有効期限を AT の有効期限と一致するように設定
- 注意点
  - 自前のセッション管理を放棄してはいけない。セッション管理を OAuth サーバーに押し付けてはダメ
  - リクエストの度に AT がまだ有効かどうかを確かめるためだけにプロフィール API を叩きに行ったりしてはいけない。
    - もしプロジェクト内部で OAuth サーバーを運用するような環境では、まずコイツから過負荷で死んでいくことになる
### 0-4. Cookie-BasedとToken-Basedの違い
- Cookie-Based
  - サーバ側でsession情報を持つ。CookieにはsessionIdを入れており、リクエストの都度sessionIdに紐づくサーバ側sessionデータを参照
  - 一番最初に学ぶやつ。RDBにセッション情報を格納しておくパターン
- Token-Based
  - クライアント側で「認証に成功した」という情報（＝Token）を持ち、リクエストの都度それを送る。
  - RDBにセッション情報を格納しないで済む
  - トークンにも色々な種類がある。JWS,JWT,JWE,...
    - https://qiita.com/TakahikoKawasaki/items/8f0e422c7edd2d220e06
### 0-5. トークンの種類
- https://qiita.com/TakahikoKawasaki/items/8f0e422c7edd2d220e06
