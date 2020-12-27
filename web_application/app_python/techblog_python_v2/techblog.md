# techblogの開発フロー
- 以下の記事を参考にしながらブラッシュアップする
  - 開発フロー、使いまわせるテンプレ、api設計のツール
    - https://qiita.com/tamitami/items/f9329bb51c9b76509c10
  - web api設計でやること
    - https://qiita.com/NagaokaKenichi/items/89c09354f08fc8d7387f
    - https://www.seplus.jp/dokushuzemi/blog/2020/07/make_webapi_with_python_fastapi.html#Swagger
- WebAPIテストツールまとめ
  - https://qiita.com/os1ma/items/9eadcfb91fa26af762be
  - https://future-architect.github.io/articles/20191008/

## わかったこと
- Pydanticは型ヒントのためのclassで、ユーザからPOSTされてきたものに対して使用する。
  - 型は合っているか、必須のパラメータは満たされているかのバリデーションを行う
- バリデーションするもの
  - クエリパラメータ、パスパラメータ
  - リクエストボディ
- QueryとPathはユーザから入力されていきたクエリパラメータとパスパラメータのバリデーション
- URI毎にディレクトリを分けるとわかりやすいかも
  - articlesのURIならarticlesディレクトリに
  - usersのURIならusersディレクトリに
- 最低限のディレクトリ分割
  - ORMのmodelクラスはmodelディレクトリにuserモデルならusers.py、postモデルならposts.py
  - DBの接続先の情報などはconfigディレクトリのdb.pyなどに外出しする
- SQLalchemyの使い方
  - postgresqlに繋ぎたい場合は、`psycopg2`のpythonライブラリをインストールする。URLに`psycopg2`を記述する
  - SQLalchemyを使って初期のテーブル作成をする(ちゃんとした開発なら、マイグレーションを実装するので以下の方法は使わないと思う)
    - https://outputable.com/post/start-sql-alchemy/
  - 以下を参考にするとできる
    - https://lonesec.com/2020/01/12/user-register-with-fastapi_auth/
    - https://fastapi.tiangolo.com/ja/tutorial/sql-databases/
    - https://outputable.com/post/start-sql-alchemy/
- SQLalchemyの完全解説(かなりわかりやすい)
  - 大まかにクエリビルダとして使う方法とORMとして使う方法の二種類があることに注意
    - クエリビルダは、生のSQLをpythonっぽく書くことができる
    - よく目にする記事としてはORMを使うことが前提になっているが、そんなことはない
  - https://www.slideshare.net/YasushiMasuda/playsqlalchemy-sqlalchemy
  - https://www.m3tech.blog/entry/sqlalchemy-tutorial
- マイグレーションとは
  - アプリケーションで使うデータベースの定義を自動的に作成・管理する機能です。
  - 旧来データベースに接続して直接変更を行っていた作業を、モデルから自動生成されるコードの実行で置き換えます。
  - 定義変更用のＳＱＬを作成する手間がなくなる。
  - データベースがバージョン管理されるので複数人での開発作業がやりやすくなる
  - おそらく初期のテーブルテーブル定義もマイグレーションで行うのだと思う
    - initコマンドみたいなもので、マイグレーションファイルの初期ファイルを作ることで初期化するのだと思われる
    - Djangoではそうだった
  - FastAPIでマイグレーションを行うには
  - https://qiita.com/okoppe8/items/c9f8372d5ac9a9679396
- FastAPIはなぜマイグレーションをalembicで行っているのか？以下のようにsqlalchemy-migrateではダメなのか？
  - https://carefree-se.hatenablog.com/entry/2017/12/20/000000
- DBのコネクションとセッションの違いについて
  - https://qiita.com/ftsan/items/62590571e36365416572
- SQLAlchemyのテーブル定義のtips(制約とかフィールドとかの網羅)
  - https://qiita.com/petitviolet/items/e03c67794c4e335b6706
- ForeignKeyの`ondelete='CASCADE'`や`onupdate='CASCADE'`の意味
  - 参照先が削除されたら自分自身をどうするかの設定。CASCADEの場合は自分自身も削除する
  - https://djangobrothers.com/blogs/on_delete/
- DBのリレーションとは(one to manyとmany to manyとone to oneをわかりやすく解説している)
  - https://akiyoko.hatenablog.jp/entry/2016/07/31/232754
- SQLAlchemyのリレーションにおけるパラメータのまとめ
  - https://poyo.hatenablog.jp/entry/2017/01/08/212227
- backrefとback_populatesはどちらも「one to many」「many to one」「one to one」の関係を定義するもの
  - UserとArticleの間に「one to many」を構築したい場合(一人のユーザは複数の記事を持っているから)
    - Userクラスに`relationship("Article", on_populates="users")`
  - backrefとback_populatesの違いは「明示的か暗黙的か」
    - https://qiita.com/1234224576/items/ba66838b32b99cce51d2
- UserとCompanyの間に「many to many」を構築したい場合(ユーザは複数の会社に属して、会社は複数のユーザを持っているから)
  - 中間テーブルというものを作らないといけないので、少し面倒
    - 結構面倒、、、Djangoなら暗黙的にやってくれたのに、、、
  - 以下でかなり詳しくやってくれているので参考にしながら書く
    - https://muoilog.xyz/web-development/sqlalchemy-many-to-many-save/
  - https://python5.com/q/ierxsbsl
- データベースのテーブルを定義する方法として二種類ある
  1. `Base.metadata.create_all(bind=ENGINE)`を使った方法
    - https://outputable.com/post/start-sql-alchemy/
  2. `alembic`のようなマイグレーションのライブラリを使う方法
    - マイグレーションは、テーブルの定義だけでなくてバージョニングまで行ってくれるし、自動化しやすい
- SQLAlchemyのORMでinsert,create,delete,update,selectを行う方法
  - https://www.wakuwakubank.com/posts/277-python-sqlalchemy/
  - さらにGROUPBYとかの方法を網羅
    - https://qiita.com/tomo0/items/a762b1bc0f192a55eae8
    - https://carefree-se.hatenablog.com/entry/2017/12/20/000000
- SQLAlchemyのsessionを生成する4つの方法
  - https://qiita.com/tosizo/items/86d3c60a4bb70eb1656e
  - https://podhmo.hatenadiary.org/entry/20120129/1327837366
- pythonでモジュールがインポートできない時に確認すること
  - https://qiita.com/ktgwaaa/items/6d1f54d5ff3c4559f96c
  - pythonではそれぞれのディレクトリがパッケージとみなされる
    - 環境変数のPYTHONPATHで設定されているパス以下からパッケージを探すようになっているから、PYTHONPATHに設定されていないとインポートできない可能性がある
      - dockerの場合はdockerファイルにENV命令で定義すればいいと思う
- `__init__.py`の意味
  - python3.3以前では`__init__.py`が置いてあるディレクトリをパッケージとみなすというものだったが、python3.3以降は書かなくてもパッケージとみなす
  - そのほかの用途としては、まとめてモジュールを`__init__.py`にインポートしておくと便利ということくらい
  - https://www.kangetsu121.work/entry/2018/09/16/004008
- インピーダンスミスマッチの意味がわかった
  - columnAとcolumnBの間で関係を定義するには(後の説明のためにforeign keyを導入しておく)
    1. foreign keyを設定することでcolumnBにcolumnAの値しか入らないように制約をかける
    2. columnAが属するテーブルAとcolumnBが属するテーブルBをjoinで結合することで関係を使ってデータを取得できる
    - https://www.dbonline.jp/postgresql/table/index11.html
  - OOP では、通常、階層的なデータ構造を持っている
  - RDB では、階層的にデータを持つことはできない
  - なので、OOP と RDB には、階層的データ構造とテーブル結合という方法論の差
  - 方法論の差をインピーダンスミスマッチといい、この差を埋めるのがORM(ORマッパー)というものになる
  - 以上の説明でわからない場合は以下を見ると必ずわかる
    - https://ufcpp.net/study/csharp/sp3_ormismatch.html
- 例外とエラーの違い
  - https://social.msdn.microsoft.com/Forums/ja-JP/ff0b34b6-248a-4200-9ce6-1b950f6149ef/124561252112540123922036322806123983694912356?forum=netfxgeneralja
- DBのセッションとは
  - http://uan.sakura.ne.jp/myoracle/session.html
- クラス変数とインスタンス変数と注意点(pythonで解説)
  - クラス変数はクラスに紐づく変数なので、インスタンス間で共有できる変数になっている
  - インスタンス変数は、インスタンスに紐づく変数なので、そのインスタンスだけが持つ変数になる
  - https://www.atmarkit.co.jp/ait/articles/1907/30/news021.html
  - https://engineer.dena.com/posts/2020.12/python_attributes/
- alembicの実行手順

  ```bash
  $ alembic init migrations  # 初回
  # 設定をして
  $ alembic revision --autogenerate -m 'create users, books'
  $ alembic upgrade head # ここでようやくテーブルが作られる
  ```

- pydanticは「レスポンスの際のフィールドの構造」と「リクエストの際のフィールドの構造」と「リクエストの際のバリデーション」の役割がある
  - response_modelにpydaticで作成したクラスを渡している理由はそういうこと
  - 公式のチュートリアルでpydanticで作成したクラスをやたらと分割しているのは、それぞれのリクエストに対して返すレスポンスを変えたりするため
- seedファイルは、ちょっとしたテストをしたいときに使うのも便利
- SQLAlchemyのall, first, one, scalarの違い
  - allやfirstは返り値がlistになるので、pydanticもlistにしないとエラーになるので注意
  - https://laplace-daemon.com/query-difference-between-first-one-scalar/
- foreign keyはあくまでも制約を与えているだけということを認識しておく。なので、データを新しく作成するときなどには特に意識せずにデータを入れて大丈夫。ただ、制約外のデータがきたらエラーになるだけ
- alembicを使う際に、initにまとめないとmodelを認識してくれなくてできなかったので注意
- Dependency Injectionは関数のようなコンポーネントもDIというらしい。公式のチュートリアルに書いてあった。要はメインの処理に依存性を注入しているから、コンポーネントもDIと呼ぶのだと思う
  - https://fastapi.tiangolo.com/tutorial/dependencies/#simple-usage
  - というより、dependencyは「オブジェクト」という単語に置き換えるべき。オブジェクトを注入という意味だとわかりやすい
    - http://blog.a-way-out.net/blog/2015/08/31/your-dependency-injection-is-wrong-as-I-expected/
- fastapiのdependsは、やはりメインの処理が実行される前に実行しておくべきものを明記することで実行してくれる仕組み
- fastapiはA->B->Cといった依存関係を定義することもできる
  - https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
- dependencyは複数指定できる。また、事前状態の判定(トークンを持っているかなど)の処理をdependsを使って書くとコードがすっきりする
  - https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
  - https://fastapi.tiangolo.com/tutorial/security/first-steps/
- pythonの非同期プログラミング、asyncとawaitの完全理解
  - https://note.crohaco.net/2019/python-asyncio/
  - https://qiita.com/kaitolucifer/items/3476158ba5bd8751e022
- encode/databasesライブラリを使ったときのマイグレーションの方法
  - https://www.encode.io/databases/tests_and_migrations/
- sqlalchemyのSessionを使って、Dependsにget_dbを指定する方法は、一つのリクエストに複数のSQLが含まれていたら、一つのコネクションを使い回す(セッション)、一つのリクエストが終了したらコネクションをクローズする。
  - https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-dependency
- 「encode/databases」と「asyncpg」と「SQLAlchemy」の関係
  - 「encode/databases」は「asyncpg」のラッパーで、SQLAlchemyのクエリとasyncpgの橋渡しを担う存在
    - asyncpgだけだと生のSQLしか扱えないが、「encode/databases」を挟んであげるとSQLAlchemyのクエリやORMを実行することができる
  - しかし、リリース予定となっているSQLAlchemy1.4がリリースされたら、asyncpgをサポートするみたいなので、「encode/databases」は使わなくなるかもしれない
    - https://magicstack.github.io/asyncpg/current/faq.html#can-i-use-asyncpg-with-sqlalchemy-orm
- fastapiのmiddlewareは、ルーティングの処理が行われる前に呼び出される処理を書く
  - cors関連の設定とか
    - https://fastapi.tiangolo.com/tutorial/cors/
- dependenciesで定義したものは、全てルーティングのDependsで呼び出している。dependenciesという名前だしDependsに定義するのも不思議なことではない
  - https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/app/api/routes/users.py


## 全体の方針
1. Stoplight StudioというAPI仕様を記載するためのGUIエディタで、Swaggerに沿ったドキュメントを作る
  - Stoplight StudioにはPrismというモックサーバも付属しているため、サーバサイドの開発が終わっていなくてもクライアントサイドの開発を進められる
  - OpenAPI Spec(OAP)というものがyamlで作成される
1. WebAPIの開発を進めていく
  - FastAPIに付属しているSwaggerは開発中に軽くAPIのレスポンスを試したいなどのデバッグ用途で使えばいいと思う
  - fastapi-code-generatorというpythonライブラリを使うと、OAPからfastapiのコードを自動生成してくれっぽい(まだ実験フェイズ)
    - https://github.com/koxudaxi/fastapi-code-generator
1. OAPからPostman Collectionを生成することで、Postmanを使って自動テストが行う
  - CircleCIに組み込みたい場合は、GUIではなくてCLIで行う必要があるので、Newmanというものを使う
    - Newmanの引数にPostman Collectionのjsonファイルを指定すると実行できる
    - https://qiita.com/developer-kikikaikai/items/74cedc67643ca93d2e0b

## 設計

### DB設計
- Post
  - post_id
  - author
  - tag
  - category
  - title
  - text
  - created_at
- User
  - user_id
  - name
  - email
  - password
  - sess_id
  - created_at
- tag
  - tag_id
  - name
- category
  - cat_id
  - name
- session
  - sess_id
  - email
  - password
### URI設計
- 記事
  - `GET /articles/{id}`: 特定の記事の取得 いらないかな
  - `GET /articles`: 記事の一覧取得
  - `POST /articles`: 記事の新規作成
  - `PUT /articles/{id}`: 記事の編集
  - `DELETE /articles/{id}`: 記事の削除
- ユーザ
  - `POST /users/register`: ユーザの新規作成
  - `POST /users/login`: ユーザのログイン(admin)
  - `DELETE /users/{id}`: ユーザの削除
- タグ
  - `GET /tags`: タグの一覧取得
- カテゴリ
  - `GET /category`: カテゴリの一覧取得
- わからない点
  - ユーザのログイン、ログアウト、ユーザ削除をURIで分けるにはどのように表現するのがいいのか
### クエリ設計
- 記事
  - `GET /articles/search?author={name}`: 執筆者を完全一致で記事を検索
  - `GET /articles/search?q={部分一致}`: 記事を部分一致のキーワードで検索
  - `GET /articles/search?title={name}`: タイトルの完全一致で記事を検索
  - `GET /articles/search?tag={name}`: タグ名の完全一致で記事を検索
  - `GET /articles/search?category={name}`: カテゴリ名の完全一致で記事を検索

### ステータスコード設計
- fastapiでオリジナルのステータスコードを返す場合
  - https://fastapi.tiangolo.com/advanced/additional-status-codes/
- ステータスメッセージは別ファイルにまとめてimportして呼び出す
- ステータスコードのフローチャートに沿って使用するステータスコードを決める
  - https://postd.cc/choosing-an-http-status-code/

### エラーハンドリング
- ライブラリなどが出す例外はtry-exeptでキャッチしてraiseで例外を上げる
- ユーザが入力してきたデータですでに登録されている場合の例外などはif文でキャッチして、raiseで例外を上げる
- fastapiの例外ハンドリングの種類
  - `HTTPException`
    - 通常のpythonの例外なので、例外をreturnするのではなく、raiseさせる方法
    - FastAPIによって自動的にJSONの型に変換される
    - オリジナルのヘッダーをレスポンスに含めることができる(エラー用のヘッダー)
  - `JSONResponse`と`@app.exception_handler()`でオリジナルの例外
    - https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers
    - 自分が使用するライブラリ毎に例外を定義すると可読性がよくなるので、その用途で使う
      - pythonの例外ハンドリングのベストプラクティスを参考
        - https://qiita.com/hasoya/items/05d4e49d492869875cca
  - 既存の例外ハンドリングのモジュールをオーバーライドする
    - validation exceptions
    - HTTPException error
    - RequestValidationError
    - https://fastapi.tiangolo.com/tutorial/handling-errors/#override-the-default-exception-handlers

### テスト(WebAPIのテストには色々な方法がある)
- pythonのライブラリで行う方法
  - webtestライブラリ
    - https://qiita.com/kchmz/items/be018f9d3f44ab72ebf3
  - requests-mockライブラリ
  - unittestライブラリ
    - https://dev.classmethod.jp/articles/python_unittest_mock/
  - fastapi標準のライブラリ
    - https://fastapi.tiangolo.com/tutorial/testing/
- GUIテストツールを使う方法
  - Postman
    - https://qiita.com/zaburo/items/16ac4189d0d1c35e26d1
  - Swagger Inspector
    - https://news.mynavi.jp/itsearch/article/devsoft/4034
  - Prism(マックサーバ)
    - https://future-architect.github.io/articles/20191008/

### CircleCIを使ったWebAPIのテスト
- CircleCIはyamlで書かれた通りにテスト環境を構築して、その環境上でアプリケーションのテストを走らせることができる。
- テスト環境はpostgresqlやpythonの dockerイメージを指定する事で構築するので、簡単にDBも含めたテストも行うことができる
- 導入のフローとしては
  - 機能の開発が終わってテストコードを書く
  - ローカルの開発環境のdockerコンテナ上でテストを走らせて確認する。
  - テスト環境をdockerコンテナで作成する
  - CircleCIにテスト環境とCircleCIの設定(yaml)をデプロイする(githubに)
  - 今後開発したコードをgithubにデプロイすれば勝手にテストが走る
  - https://qiita.com/kurodenwa/items/d4a05a0091ca2ab69911
- CircleCIとPostmanを組み合わせている事例
  - https://qiita.com/kurodenwa/items/d4a05a0091ca2ab69911
- CircleCIとfastapi標準のテストライブラリ
  - https://deadbearcode.com/serverless-fastapi-cicd/
- メルカリのCircleCI
  - https://engineering.mercari.com/blog/entry/2018-08-20-104435/
- ブランチごとにCircleCIのテストを分けることができるっぽい
  - https://pt.slideshare.net/mobile/junkpot1212/github-circle-ci/26
