# WebAPI開発フロー

## 技術選定
- 選定理由をテンプレートを使って埋める
  - https://github.com/kshina76/centos-backup/blob/master/web_application/framework選定/tmp.md

<br></br>

## 設計
### DB設計
### エンドポイント設計(URL設計)
1. 対象となるデータを認識する
2. 対象となるデータをリソースに分ける
3. リソースにURLで名前を付ける
4. URLに対してPOST,GET,PUT,DELETEを付ける
### ディレクトリ設計と依存設計
- ディレクトリ設計はフレームワーク毎にベストプラクティスがあるから、色々なサンプルを見て決める
- 依存設計は、ディレクトリ同士がどのような依存関係になっているかを図示する(クラス設計みたいなもの)
  - 自分がバカだからこれがないと混乱する
- 依存設計は、さらにコンポーネント(関数)がどのような依存関係になるかも図示しないと混乱する
  - 以下の図みたいに
    - https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
- 依存設計の手順としては、
  1. とりあえずディレクトリの構成を考える
  2. ディレクトリをレイヤーに分ける(依存関係はできるだけ上位レイヤーから下位レイヤーに一方向になるように)
  3. コンポーネントをディレクトリに配置していく(レイヤーの依存関係が一方向になるように配置)
  4. 3で依存関係がおかしくなりそうなら、2に戻ってディレクトリの構成を考え直してみる
  - https://qiita.com/wm3/items/2c90bfd9e973d368ebd8
- よく記事で書かれているレイヤードアーキテクチャのディレクトリ構造を「参考にする」程度に留めて、柔軟にディレクトリを設計して、依存方向を保つように設計すればいい感じになるのかなと思った
  - https://qiita.com/wm3/items/2c90bfd9e973d368ebd8
- https://note.com/yusugomori/n/n9f2c0422dfcd
- https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
### ルーティング設計
- 大きいアプリケーションになった時にエンドポイントを階層化して分けることで、分割できるようにするもの
- URI毎にディレクトリを分けて階層化することでルーティングを管理する感じかな
  - articlesのURIならarticlesディレクトリに
  - usersのURIならusersディレクトリに
- https://qiita.com/tmknom/items/08b69594e32a92bccee5#ルーティング定義とエンドポイント設計
- https://fastapi.tiangolo.com/tutorial/bigger-applications/
### リクエスト設計: ユーザからの入力に対しての設計
- クエリパラメータ、リクエストボディ、パスパラメータの設計と使い分け
  - https://github.com/kshina76/centos-backup/tree/master/web_application/web_api#2-5検索とクエリパラメータの設計
  - https://github.com/kshina76/centos-backup/tree/master/web_application/web_api#2-6-フィルタソート検索はリクエストパラメータでやろう
  - https://github.com/kshina76/centos-backup/tree/master/web_application/web_api#2-7-レスポンスのフィールドを絞れるようにしよう
- HTTPヘッダの設計
  - https://www.templarbit.com/blog/jp/2018/07/24/top-http-security-headers-and-how-to-deploy-them/
  - https://qiita.com/nightyknite/items/1b8070d1e31083ee79ee
  - https://spelldata.co.jp/blog/blog-2018-05-22.html
### レスポンス設計
- レスポンスボディの設計
- ステータスコード設計
  - ステータスコードのフローチャートに沿って使用するステータスコードを決める
    - https://postd.cc/choosing-an-http-status-code/
- HTTPヘッダの設計
### 例外設計: どのようにエラーをハンドリングするかの設計
- とりあえず以下を見て設計してみる
  - https://qiita.com/tmknom/items/08b69594e32a92bccee5#例外ハンドリング
  - https://nekogata.hatenablog.com/entry/2015/04/11/135231
- try-catchやtry-exceptで結果をreturnする処理は呼び出し元のルートに実装する。呼び出し元のルート以外では、returnではなくて、try-exceptのexcept内でraiseを使ってエラーを伝搬させる
- pythonっぽいエラーハンドリングをする方法
  - https://pybit.es/pythonic-exceptions.html
- 例外処理をする場所
  - https://codezine.jp/article/detail/1581
- 例外のアンチパターン
  - https://www.slideshare.net/t_wada/exception-design-by-contract
- if文とtry(例外)の使い分けは、「例外は、呼び出す側が契約条件を満たしたが呼び出された側が契約を履行できなかったときに投げるもの」と覚えておく
  - 要は条件分岐はif文を使って、それ以外は例外
- try-exceptのexceptにはエラーのロギング処理とraiseでエラーを伝搬させる処理を書けばいい
- pythonの`raise`は呼び出し元に例外を発生させるもの、または伝搬させるもの
- webアプリ開発において例外をraiseするパターン
  - フレームワークで用意されている例外をraiseするパターン
    - フレームワークで例外があらかじめ用意されていて、その例外をraiseする
    - 呼び出し元のルートまでraiseで例外が伝搬されてくると、例外メッセージがクライアントにreturnされる
    - このパターンはフレームワークの例外の実装に例外メッセージをreturnする処理が書かれていて、raiseしてルートに到着すると自動的にクライアントに例外メッセージがレスポンスとして返されるようになっている
    - FastAPIにおける`呼び出し元のルート`は`@app.get()`などのフレームワーク内で実装されている部分に当たるので、returnの処理は自分で書く必要はない。
  - フレームワークにカスタムの例外を定義してraiseするパターン
    - FastAPIの場合は`@add.exception_handler`の中にクライアントに例外メッセージをreturnする処理を書くことで、例外ハンドラがフレームワークに追加される
    - 例外を発生させたい場所で、そのハンドラをraiseすると呼び出し元に例外が伝搬される
    - 呼び出し元のルート(@app.get()など)まで例外が伝搬されてくると、クライアントに例外メッセージが返るようになる
  - フレームワークを使わないで自作の例外ハンドラを作るパターン
    - pythonなら`Exceptクラス`を継承して、そのクラスをraiseする
    - try-exceptでキャッチしてreturnする

### テスト設計: テストの工程でどのようなデータでテストをするかの設計
- 正常系の設計
- 準正常系の設計
- (真の)異常系の設計
- https://swqa.qa-kobe.com/uncategorized/semi-normal-test
### ロギング設計
- とりあえず以下を見て設計してみる
  - https://qiita.com/tmknom/items/08b69594e32a92bccee5#ロギング
  - https://qiita.com/nanasess/items/350e59b29cceb2f122b3
- except内でloggingを使用してraiseで呼び出し元にエラーを伝搬させれば、関数内のローカル変数をログに出力を行い、呼び出し元で別のログ出力することができる
  - この方法で全てをロギングしてはいけない。なぜかと言うと、何回も同じログがロギングされてしまうから。これを避ける簡単な方法は、呼び出し元のルートまで伝搬させ続けて、ルートでロギングの処理を書けばいい。
  - https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950
  - https://qiita.com/Kento75/items/b0f43943d300d0ed9586
- ロギングを定義する場所
  - https://codezine.jp/article/detail/1581
- ログを取る場所
  - 業務ロジックの開始メッセージ: try句の先頭
  - 業務ロジック内で発生した例外のメッセージ: catch句
  - 業務ロジックの終了メッセージ: finally句
- ロギングを呼び出すのは、呼び出し元のルートで呼び出す。いろいろなところでロギングすると汚いコードになってしまうので避ける

<br></br>

## 開発: 設計に沿って実装していくことに集中する
- Docker環境構築
  - DBコンテナのセットアップ
  - APIコンテナのセットアップ
    
- モデルの実装
  - DBのコネクションのコード実装
  - ORMのモデルを定義
    - リレーションの設定はどのように行うのか(many to manyの実現方法は)
- マイグレーションの設定
  - FastAPIの場合は、`alembic`というライブラリを使ってマイグレーションを行う
  - その他は`SQLAlchemy-Migrate`というライブラリもある
- シードの設定
  - シードとはデータベースにあらかじめ入れておくデータのこと
  - ブログならadminを設定しておくのがいいと思う
  - djangoのadminページを作るような感じかな
- APIの実装
- https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5

<br></br>

## テスト
- WebAPIにおけるテストのピラミッド
  - `初めての自動テスト`という書籍では「Unit Test、Integration Test、GUI Test」というくくりだったが、WebAPIにおいて1つのAPIは1つ以上のメソッドが絡むので、「API」のテストということに関しては`初めての自動テスト`という書籍のピラミッドの図のIntegration Testを行うことと同値になる
  - バックエンドエンジニアは後述する「Unit Test、API Test」を行えばいい

  ![test-pyramid 86a621f c307ad325f27ba6104e18eb847c76ab4-1-300x200](https://user-images.githubusercontent.com/53253817/103407449-0ecc7e80-4ba2-11eb-97b5-84639a079ddb.png)

### Unit Test
- 1つのメソッド(関数)のテスト
- アプリケーションのコーディング同時並行で書いていく
### API Test
- Component Test
  - 1つのAPIのテスト
    - 複数のメソッド(関数)の連携テスト
  - Requestに対して、Responseが期待通りに返却されるかを確認
- Integration Test
  - 複数のAPIの連携テスト
    - 「部品」と「部品」との結合テスト、つまりAPIのシナリオテスト
  - 例えば以下の流れを一気通貫でテストする
    - 「ログインAPI->商品リストAPI->商品詳細 API->カート追加 API->決済API」
### GUI Test
- GUIを含めたE2Eテスト
- ここはQAのエンジニアとかが行うのかな？
### 参考文献
- https://quesqa.com/now-is-the-time-to-do-api-testing/

<br></br>

## 全体の参考文献
- https://www.slideshare.net/t_wada/restful-web-design-review
