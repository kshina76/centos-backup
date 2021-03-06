# 技術選定(フレームワークを選定する時にサポートされているか調べる事項、勉強する時のポイント)
- フレームワークの調査は以下の項目がサポートされているかを調べて、技術選定の情報に使う
- また、フレームワークを学ぶ際には以下の項目を勉強するということを頭の片隅に入れておくと、開発をしながら調べて機能を付け加えるといった方法をとることもできる
- 以下の項目に関しての「正しい書き方」を学ぶ時は「公式のドキュメント」と「<フレームワーク> Open Source」とか「<フレームワーク> 30days」とかでググってサンプルを用意すると効率がいい

## 目次
- [ロギング](#ロギング)
- [例外ハンドリング](#例外ハンドリング)
- [URLディスパッチャー](#URLディスパッチャー)
  - メソッドの指定方法
  - クエリパラメータ
  - パスパラメータ
  - ルーティング機能
- [HTTPオブジェクト](#HTTPオブジェクト)
  - リクエストボディ、ヘッダー
  - レスポンスボディ、ヘッダー
  - Cookieの管理
- [ログイン機能](#ログイン機能)
- [ユーザ管理](#ユーザ管理)
- [データベース関連](#データベース関連)
  - ORM
  - ODM
  - クエリビルダー
  - データベースセッションの管理
  - トランザクション管理
  - マイグレーション
  - 非同期のサポート有無
  - コネクションプール
- [Webサーバ](#Webサーバ)
- [WebAPI](#WebAPI)
- [非同期(Async)サーバ](#非同期(Async)サーバ)
- [セットアップ](#セットアップ)
- [ディレクトリ構成](#ディレクトリ構成)
- [テスト](#テスト)
- [デバッグ](#デバッグ)
- [セキュリティ](#セキュリティ)
- [便利機能](#便利機能)

## ロギング
- ログを取る時の書き方

```python

```

<br></br>

## 例外ハンドリング
### 例外の扱い方
- 例外ハンドラを登録することで、例外をraise(throw)すると勝手に例外メッセージがJSONレスポンスとして返してくれるのかどうか
- または、例外ハンドラを登録する機能はなくて、開発者が明示的に例外ハンドラを呼び出さないといけないのかどうか
- ステータスコード設定の方法
- オリジナルのステータスコードの設定

```python

```

### 標準で用意されている例外ハンドラの有無

```python

```

### 標準の例外ハンドラをオーバーライドできる機能の有無
- 返す例外メッセージのJSONフォーマットを変更できるとか

```python

```

### ユーザ定義のカスタム例外ハンドラを作成する機能の有無
- フレームワークの高品質なサンプルがどのような例外ハンドリングをしているか見て、やり方を決める

```python

```

<br></br>

## URLディスパッチャー
- 種類
  - デコレーターを使うパターン(@app.getのように)
  - Djangoのurls.pyのようにURLセッティングファイルを使って、該当するクラスを呼び出すパターン
### メソッドの指定機能
- postとかgetを指定する機能

```python

```

### URLの分析機能(クエリパラメータ)
- クエリパラメータの取得機能
- クエリパラメータのバリデーション機能

```python

```

### URLの分析機能(パスパラメータ)
- パスパラメータの取得機能
- パスパラメータのバリデーション機能

```python

```

### ルーティング機能
- プログラムが大きくなってきたときに、ルーティングを階層化して分割できる機能

```python

```

<br></br>

## HTTPオブジェクト
### リクエストボディ
- リクエストボディの取得機能
- リクエストボディのバリデーション機能

```python

```

### リクエストヘッダー
- リクエストオブジェクトからヘッダーを取得する機能

```python

```

### レスポンスボディ
- レスポンスボディを返す機能

```python

```

### レスポンスヘッダー
- レスポンスヘッダーを定義する機能

```python

```

### Cookieの管理
- リクエストオブジェクトから取得する機能
- レスポンスオブジェクトから操作する機能

```python

```

<br></br>

## ログイン機能
- ログインとセッション管理はフレームワークレベルでサポートしてくれていないと採用するのは厳しい
  - セキュリティ的にもコード量的にも

### フレームワーク標準でサポートされているパターン

```python

```

### アドオンで提供されているパターン

```python

```

### 自分で実装するパターン

```python

```

<br></br>

## ユーザ管理
- 種類
  - 自分で実装するパターン
  - アドオンで提供されているパターン
  - 公式のサンプルがあるパターン
  - etc

<br></br>

## データベース関連
- データベースの種類
  - SQLAlchemy for DBMS
  - Django ORM for DBMS
  - KVS
  - Object DB
### ORM: RDBとオブジェクトのインピーダンスミスマッチを解消するもの
- ORM(O/Rマッパー)がどの程度、自動的に値をマッピングしてくれる確認
  - 文字列や数値などのプリミティブな値
  - 時刻型（LocalDateTime型など）
  - nullかもしれない値（Optional型など）
  - 列挙型（enumなど）
  - 独自定義したクラスの値（ValueObjectなど）
- CRUD操作やGROUPBYなど絞り込みをどのような構文で実行するか
  - SQlAlchemyの例だと以下のようなもの
    - https://qiita.com/tomo0/items/a762b1bc0f192a55eae8
    - https://carefree-se.hatenablog.com/entry/2017/12/20/000000
- リレーションの張り方
  - ForeignKeyの扱い方
  - 親が削除された時の動作の定義の仕方(cascadeとか)
  - 「one to many」「one to one」「many to many」の実現方法

```python

```

### ODM: NoSQLとオブジェクトのインピーダンスミスマッチを解消するもの

```python

```

### クエリビルダー
- 生のSRLを扱う機能の有無

```python

```

### データベースセッションの管理
- プログラミング言語を通してデータベースに接続したり、切断する機能の有無
- データベースセッションの生成方法

```python

```

### トランザクション管理
- トランザクション機能の有無
  - `begin`とか`commit`
  - デコレータでトランザクションを定義できるものもある

```python

```

### マイグレーション
- サードパーティのマイグレーションライブラリを使うのか、組み込まれているのか
- マイグレーションの自動化はサポートされているのか、スクリプトを自分で書くのか

```python

```

### ライブラリが非同期に対応しているか
- コネクションプールにコネクションを張る処理が非同期になっているか(以下のような処理)
  - https://www.encode.io/databases/database_queries/
- I/Oが非同期になっているか
- FastAPIの例だと、SQLAlchemyが非同期に対応していないから、SQLAlchemyはSQLを発行するのに使用して、実際にSQLを実行するのはencoded/databasesというライブラリが行うという方法を取っている
  - SLQAlchemy1.4からasyncに対応する予定がある

```python

```

### コネクションプール: コネクションをcloseしないで貯めておくところ

```pyhon

```

<br></br>

## Webサーバ
- 種類
  - WSGIサーバ
    - gunicorn
    - uWSGI
    - Waitress
  - ASGIサーバ
    - Uvicorn
  - オリジナルサーバ
    - Djangoとかは色々なサーバが組み合わさってる
### runサーバ機能

```python

```

### デーモン管理

```python

```

<br></br>

## WebAPI
- 種類
  - フレームワークでサポートされるパターン
  - アドオンでサポートされるパターン
  - 自分で作るパターン

```python

```

<br></br>

## 非同期(Async)サーバ
- フレームワークによってはサポートされている
- 機能
  - 依存関係の定義
    - 実行順序の制御(fastapiでいうDependsの機能、JavaScriptでいうPromiseの機能)ができる機能
    - 事前の状態を定義(例えば必ずログインされた状態で実行されないといけない関数で、事前に判定しておくような機能)
      - https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/

```python

```

<br></br>

## セットアップ
- インストール方法
  - pip
  - buildout
  - etc
- 環境設定(プロセス数とかのconfig)
  - ini file
  - python code
  - yaml
  - json
  - etc

```bash

```

<br></br>

## ディレクトリ構成
- 公式のドキュメントに記されていることが多い
- プロジェクトを生成するボイラーテンプレートを公開している人もいる
  - https://fastapi.tiangolo.com/project-generation/
- 「<キーワード> open source」とかでググると高品質なサンプルを用意している人がいる
- 依存関係を考えながら設計する
  - https://qiita.com/wm3/items/2c90bfd9e973d368ebd8

```bash

```

<br></br>

## テスト
- テストの方法
### CLI上でのテスト方法
- 標準でサポートされているのかアドオンなのか
- pytestとかCLI版のPostmanとか

```python

```

### GUI上でのテスト方法
- 標準でサポートされているのかアドオンなのか
- Postmanとか

```python

```

### CircleCIと組み合わせるときの方法

```python

```

<br></br>

## デバッグ
- フレームワークごとのデバッグの方法を調べる
  - vscodeのようなIDEでデバッグできるように方法がドキュメントに書いてあったりする

### CLI上でのデバッグ方法

```python

```

### vscode上でのデバッグ方法

```python

```

### リモートデバッグの方法

```python

```

<br></br>

## セキュリティ
### CORSの設定方法
- WebAPIの開発で必要になるCORSの設定
  - https://qiita.com/tomoyukilabs/items/81698edd5812ff6acb34
  - https://qiita.com/rooooomania/items/4d0f6275372f413765de
- プリフライトリクエストの設定
- 認証情報を含む場合のリクエストの設定
  - Access-Control-Allow-Credentialsをtrueにする

```python

```

### OAuthの実現方法

```python

```

### 入力値のバリデーション
- 以下の項目がサポートされているのか、自分で正規表現などを使用して実装するのか
  - 文字エンコーディングの妥当性チェック
  - 文字エンコーディングの変換機能
  - 入力値の妥当性


```python

```

### XSS対策


### SQLインジェクション対策
- 入力値の検証のサポート
- プレースホルダによってSQLを組み立てる方法のサポート
  - 静的プレースホルダ: RDBMSで行う方法
  - 動的プレースホルダ: アプリケーションのライブラリで行う方法

```python

```

### CSRF対策
- 対策
  - CSRF対策の必要なページを区別する
  - 利用者の意図したリクエストであることを確認する
  - 「重要な処理」の実行後に登録済みメールアドレスに通知メールを送信
- 「利用者の意図したリクエストであることを確認する」方法の種類(以下の機能をサポートしているかを確認)
  - 秘密情報(トークン)の埋め込み
  - パスワード再入力
  - Refererのチェック
- https://html-coding.co.jp/knowhow/security/csrf/

```python

```

### クリックジャッキング対策
- X-Frame-Optionsヘッダ
- https://itsakura.com/python-bottle-clickjacking

```python

```

### ヌルバイト攻撃対策

<br></br>

## 便利機能
- Django adminみたいな機能
