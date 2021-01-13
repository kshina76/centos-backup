# WebAPI開発フロー

## 技術選定
- 選定理由をテンプレートを使って埋める
  - https://github.com/kshina76/centos-backup/blob/master/web_application/framework選定/tmp.md

<br></br>

## 設計
### DB設計
- 設計の本を読んでから書く
### エンドポイント設計(URL設計)
1. 対象となるデータを認識する
2. 対象となるデータをリソースに分ける
3. リソースにURLで名前を付ける
4. URLに対してPOST,GET,PUT,DELETEを付ける
### ディレクトリ設計と依存設計
- ディレクトリ設計はフレームワーク毎にベストプラクティスがあるから、色々なサンプルを見て決めて従う。全体のディレクトリ構成を独自で決めないほうがいい。置き場に困ったものは自分で設計する
  - MVC以外の構成を取るなら独自で決めないといけないが、その場合もサンプルなどが転がっている場合があるので、それを参考にする
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
- 例外ハンドラの設計
  - エラーレスポンスの定義
  - エラー通知
  - エラーログ出力
- 例外ハンドラとは
  - 最終的に例外を処理してどのような処理を実行するかを決める関数(クラス)のこと
    - 最終的にエラーメッセージをreturnしたりするところ
  - 例外ハンドラの呼び出しは呼び出し元のルートで行う
  - 呼び出し元のルート以外では、returnではなくて、try-exceptのexcept内でraiseを使ってエラーを伝搬させる
  - FastAPIだと`@add.exception_handler`で追加する対象の関数(クラス)のこと
  - FastAPIでは`@app.get`などでルーティングされている関数で例外をraiseすると、対応する例外ハンドラをフレームワークが自動で呼び出してくれる
- if文とtry(例外)の使い分け
  - 「例外は、呼び出す側が契約条件を満たしたが呼び出された側が契約を履行できなかったときに投げるもの」と覚えておく
- pythonっぽいエラーハンドリングをする方法
  - https://pybit.es/pythonic-exceptions.html
- raiseした例外はtry-exceptしない限り上位に伝搬し続ける
  - 要は、「関数A->関数B->関数C->関数D」の場合、関数Dで例外がraiseされて関数B,Cでtry-exceptとraiseを使って伝搬しなくても、そのまま関数Aまで自動で伝搬してくれるということ
  - https://teratail.com/questions/308580
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
- 例外ハンドリングの設計
  - https://qiita.com/tmknom/items/08b69594e32a92bccee5#例外ハンドリング
- エラーと例外の歴史
  - https://nekogata.hatenablog.com/entry/2015/04/11/135231
- 例外のアンチパターン
  - https://www.slideshare.net/t_wada/exception-design-by-contract
  - 要は条件分岐はif文を使って、それ以外は例外
### テスト設計: テストの工程でどのようなデータでテストをするかの設計
- マインドマップを使ってテストは列挙して設計していくようにする
- ブラックボックステスト
  - 「同値クラステスト」の設計
  - 「境界値テスト」の設計
  - 「デシジョンテーブルテスト」の設計
  - 「ペア構成テスト」の設計
- 探索的テスト
  - 開発中にバグが混入しそうな部分で行えばいいかな
- https://github.com/kshina76/centos-backup/tree/master/web_application/app_test/ソフトウェアのテスト技法
### ロギング設計
- ログのフォーマット
  - https://qiita.com/nanasess/items/350e59b29cceb2f122b3
  - https://qiita.com/tmknom/items/08b69594e32a92bccee5#ロギング
  - https://qiita.com/__init__/items/91e5841ed53d55a7895e
  - https://medium.com/@PhilippeGirard5/fastapi-logging-f6237b84ea64
- 秘匿情報のマスキング
  - パスワードやEmail
  - アプリケーションの内部構造がわかってしまうものは出力しない
- 相関IDと分散トレーシング
  - マイクロサービスアーキテクチャの時に必要になる
- ログ出力を呼び出す場所: 最初の3つは必須、全て呼び出し元のルートで呼び出す
  - リクエスト開始時 ： リクエストパラメータや、実行しようとしたクラス名／メソッド名など。何を実行しようとしたか分かる情報を可能な限り出力する。
  - リクエスト正常終了時 ： HTTPステータスコードや実行時間などを出力する。ログが肥大化するので、ペイロードは出力しない。try-exceptブロックが終わったところとかに。
  - リクエスト異常終了時（例外発生時） ： 例外クラス名やエラーメッセージを出力する。必須ではないが、リクエストパラメータなど、リクエスト開始時に出力する内容も一緒に出力しておくと、障害調査が楽になる。exceptブロックの中に書くとか。
  - 外部システム連携時 ： 外部システムと通信する前に、リクエストパラメータを出力しておく。合わせて異常時には、エラーレスポンスを出力しておこう。正常終了時は、正常終了したことだけ分かればOKだ。
  - SQL実行時 ： フツーのO/Rマッパーは、実行したSQLをログ出力できる。デバッグ時に非常に役に立つので、少なくとも開発環境ではログ出力する。もし、本番環境でも出力する場合、大量のログが出力されるので、ディスクフルで死んだりしないように配慮しよう。
- 関数内のローカル変数をログ出力
  - except内でloggingを使用してraiseで呼び出し元にエラーを伝搬させれば、呼び出し元で別のログ出力することができる
  - この方法で全てをロギングしてはいけない。なぜかと言うと、何回も同じログがロギングされてしまうから。これを避ける簡単な方法は、呼び出し元のルートまで伝搬させ続けて、ルートでロギングの処理を書けばいい。
  - https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950
  - https://qiita.com/Kento75/items/b0f43943d300d0ed9586
### セキュリティ項目の設計
- 詳しくはフレームワーク選定のテンプレートに沿って設計していく
- 徳丸本で学んだ内容を記述するのが良い


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
  - APIの実装は最後に行うようにする
    - モデルより先に実装してしまうと、認証の機能などが後回しになってしまって面倒だから
- docstringの記述
  - https://qiita.com/simonritchie/items/49e0813508cad4876b5a
- 参考文献
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

### データベースを含めたテスト
- テスト方法
  - pytest-dockerでデータベースをフィクスチャする方法
    - https://qiita.com/hkato/items/6d137ee49f6eb2f8c426
    - https://qiita.com/skokado/items/6c179f0d46654963387a
  - テスト用のデータベースを手動で作っておいて、フィクスチャする方法
    - https://dev.classmethod.jp/articles/tried-to-test-crud-using-pytest/
- データベースを含めたテストで行うこと
  - テスト用データベースのマイグレーション
    - テスト実行時に一度だけテストデータベースをまっさらにして、マイグレーションが自動で実行されるようにしておく。テストデータベースのマイグレーションが自動化されてないと、いちいち開発者が手動でマイグレーションを実行するハメになり非効率である。
  - テスト用データベースの分離
    - 言うまでもないが、テストで使用するデータベースは、開発時に使用するデータベースとは分けておこう。設定ファイルで、テスト時のデータベースの向き先を変えて、いくら壊しても大丈夫な状態にしておくのだ。
  - テストケース単位のクリーンアップ
    - データベースのテストを行う場合は、テストケースごとに自動でクリーンアップする仕組みを作っておく。データベーステスト用の基底クラスを提供し、勝手にロールバックする仕組みにするのが一番簡単だ。
    - 要はテストケースが一つ終了する度に、自動でテストデータベースがまっさらになる仕組みを作れということ
  - テストに関しては、共通化をしすぎないように

- pytestのデータベースフィクスチャに関する記事
  - https://qiita.com/_akiyama_/items/9ead227227d669b0564e
  - https://dev.classmethod.jp/articles/tried-to-test-crud-using-pytest/
- FastAPIとpytestを使ったデータベースフィクスチャ
  - https://qiita.com/bee2/items/ff9c86d8d345dbcab497
  - https://fastapi.tiangolo.com/advanced/testing-database/

### モックやスタブを使用するか否か
- モックは依存しているクラスや関数を置き換えるためのもの
  - 自作の関数やクラスだが呼び出すのに手間がかかる時などに使用する
  - また外部のAPIやデータベースを使用している時にモックやスタブに置き換えてテストをする場合もある
  - 最近はデータベースのテストはdockerを使用すると楽だから、モックは使用されない可能性もある
- モックとスタブの違い
  - https://qiita.com/hirohero/items/3ab63a1cdbe32bbeadf1
- モックやスタブを使う場合と使わない場合
  - https://irof.hateblo.jp/entry/2019/07/17/233048

<br></br>

## 全体の参考文献
- https://www.slideshare.net/t_wada/restful-web-design-review
