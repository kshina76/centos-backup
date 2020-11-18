# techblog開発memo

## 大まかな構成
- 作るもの
    - techblog

- 使用技術・ツール
    - docker
    - HTML/CSS/tempalte
    - Sass
    - JavaScript
        - 一部をスクロールさせたり、目次をクリックしたら飛んでいく動作をさせたりするため
        - staticファイルの中にjsを作成して、htmlからはscriptタグで読み出す
    - Go言語
    - Go言語標準ライブラリ
    - figma
    - NotePM

- アプリケーションアーキテクチャの構成
    - レイヤー構成
        - 4層(DDDではないパターンで行うので、domainはdataに依存していいこととする)
    - プレゼンテーション層の構成
        - MVC
        - URLディスパッチャ
            - main.go
        - コントローラー
            - presentationディレクトリに定義
            - Templateエンジン呼び出し
            - httpの流れはここで定義(redirectとか)
        - モデル
            - domainディレクトリに定義
            - データベース自体の定義
            - データベースへの処理はここが担当する
            - CRUDとかビューにデータを返したり
        - ビュー
            - Templateエンジン自体(http/templateライブラリを使用)
            - HTML/CSS/template
    - ビジネスロジック層
        - ドメインモデル
            - データと振る舞いを定義
            - 小規模だからデータベースのテーブルを参考にして決めていい

- 気をつけること
    - ちゃんとMVCに沿っているかを確認しながら開発をする
        - https://www.slideshare.net/MugeSo/mvc-14469802
    - オブジェクト指向を意識する
        - 自分のREADMEを読んだり、本を読み直したり

<br></br>

## 詳細な構成(作業する順に書いている)

- 機能設計(ユースケース)
    - スーパーユーザ(admin) 最初に作る
        - email,passwordでサインインできる(SQLで自分のadminを作っておけばいいか)
        - ログアウトすることができる
        - 管理者ページにアクセスできる
        - ブログの新規作成ができる(markdown実装したい)
        - ブログの編集ができる
        - ブログの削除ができる
        - ユーザを作ることができる(ブログ執筆者、とりあえずこれは無し)
    - 一般ユーザ(ブログ閲覧者) スーパーユーザができてから作る
        - 記事の一覧(トップ画面)にアクセスできる
        - 記事の一覧から同じカテゴリの記事一覧に飛ぶことができる
        - 記事の一覧から同じタグの記事一覧に飛ぶことができる
        - 記事の詳細を見ることができる
        - 記事の詳細から同じカテゴリの記事一覧に飛ぶことができる
        - 記事の詳細から同じタグの記事一覧に飛ぶことができる
        - サイドバーのタグからそのタグの記事の一覧に飛ぶことができる
        - サイドバーのカテゴリからそのカテゴリの記事の一覧に飛ぶことができる
        - 記事を検索できる（とりあえずこれはなし。出来上がってから機能拡張する）
        - 目次をクリックすると見出しのところに自動スクロールしてくれる
            - HTMLのページ内リンクという機能がある
    - ブログ
        - 自動で目次作成
        - ページネーション
        - ページ内リンク(目次を押したらそこにジャンプ)
            - https://saruwakakun.com/html-css/reference/link_jump

- 画面遷移設計とデザイン(ワイヤーフレームとか)
    - 「figma」というUI/UXツールでページのデザインを作成
        - Frameを意識することで、HTMLタグの付け方が頭に浮かんできて、後々のコーディング作業で楽になるという付加効果もある
        - 一つのページにFrameを分割して矢印を書けば、画面遷移図になる(今度からそうしよう)
    - ページネーションor無限スクロール
        - とりあえずページネーションを選択

- URL設計
    - スーパーユーザの操作

    | 画面・処理名                                 | URL                               | file/class#method | 
    | -------------------------------------------- | --------------------------------- | ----------------- | 
    | 管理者ページログイン画面                     | GET /admin/auth                   |                   | 
    | ログイン処理                                 | POST /admin/login                 |                   | 
    | ログアウト処理                               | POST /admin/logout                |                   | 
    | 管理者画面(一般記事の一覧にCRUDがついただけ) | GET /admin                        |                   | 
    | 記事作成画面                                 | GET /articles/create-article      |                   | 
    | 記事作成処理                                 | POST /articles/create             |                   | 
    | 記事削除画面                                 | GET /articles/{id}/delete-article |                   | 
    | 記事削除処理                                 | POST /articles/{id}/delete        |                   | 
    | 記事編集画面                                 | GET /articles/{id}/edit-article   |                   | 
    | 記事編集処理                                 | POST /articles/{id}/edit          |                   | 

    - 一般ユーザとスーパーユーザ共通の操作

    | 画面・処理                                 | URL                  | file/class#method | 
    | ------------------------------------------ | -------------------- | ----------------- | 
    | トップ画面                                 | GET /blog            |                   | 
    | 記事の詳細画面                             | GET /blog/{id}       |                   | 
    | タグでフィルタリングされた記事一覧画面     | GET /blog/{tag}      |                   | 
    | カテゴリでフィルタリングされた記事一覧画面 | GET /blog/{category} |                   | 


- DB設計(今回は箇条書きで。普通はDB設計の本を学んで色々やらないとダメ)
    - session(プロになるためを参照)
        - id
        - session_id
        - email
        - user_id(なんのため？)
        - created_date
    - super_user
        - id
        - session_id
        - name
        - email
        - password
        - created_date
    - articles
        - id
        - author(外部キー)
        - title
        - eyecatch_img
        - text
        - tags : 多対多
        - category : 外部キー
        - created_date
        - public(公開、非公開、bool)
        - relation(関連記事)
    - author
        - id
        - name
        - author_img
    - tags
        - id(いらない？)
        - tag
        - count(タグの大きさを変更するため)
    - categories
        - id(いらない？)
        - category
        - count(カテゴリ内の数を示すため)

- アーキテクチャ設計、クラス設計
    - クラス設計（とりあえずプロパティはDBと同じ）
        - Users
        - Session
        - Articles
    - アーキテクチャ
        - MVCアーキテクチャ
        

- システム構成設計

- 注意点
    - 小規模な場合はこの設計でいいけど、大規模な場合はもっと詳細な設計を行う必要がある

- わかったこと
    - 画面遷移の設計はユースケース図を確認しながら設計する。漏れがないように
    - URL設計はユースケース図と画面遷移を参考にしながら設計すればいい
    - DBとクラスのプロパティは同じになるのかという疑問に関しては、DBは色々な情報を持っているがクラスのプロパティは処理に必要な最低限の情報しかない気がする（あっているかは知らない）
        - なので、クラスのプロパティを抽出するやり方としては(あっているかは知らない)
            1. クラスの抽出は他の方法でしておく
            2. とりあえずDBのカラムを全部クラスのプロパティに持たせておく
            3. メソッドを書いていく中で使わないプロパティが出てきたら削除する
    - HTMLのh1,h2などの見出しタグの使い方
        - https://html-css-wordpress.com/heading-tag-navigation/
    - go言語でWeb開発でのエラーハンドリングの仕方
        - log.fatalを使うと、エラーが起きた時にterminalに表示してくれる
        - fatalを使うとプログラムを強制終了するから、開発中はfmt.PrintとかPrintlnでいい
        - 実運用ではmain以外で発生したエラーはmainまで伝搬させるようにする
            - web開発においては、mainはルーティングなので、プレゼンテーション層でエラーハンドリングする
        - めちゃくちゃいい記事
            - https://waman.hatenablog.com/entry/2017/09/29/011614
            - https://qiita.com/nayuneko/items/3c0b3c0de9e8b27c9548
    - go言語ではerrの返り値は最後の返り値で返すことが暗黙のルール
        - どのライブラリも返り値の最後はerr(errorインタフェース)が返ってくるということ
            - この性質とlog.fatalで脳死でエラーハンドリングできる！！
    - go言語でのエラーハンドリングで、返り値にerrしかない場合はifの中に定義してしまおう!
        - 使用したい値も返ってるなら後者の書き方で

        ```go
	    if err := user.Create() != nil {
		    log.Fatal(err)
	    }
        ```

        ```go
	    id, err := user.Create()
	    if err != nil {
		    log.Fatal(err)
	    }
        ```

    - go言語で関数の返り値を事前定義するところの変数は関数内でゴニョゴニョできる
        - 当たり前だけど宣言がされているから、関数内で再定義はしてはだめ
            - 「:=」において、複数の返り値がある時に定義されていないものがある時には、再定義のような形で書いても問題ない

        ```go
        type Session struct {
        	Id        int
	        Uuid      string
	        Email     string
	        UserId    int
	        CreatedAt time.Time
        }
        func test() (err error, session Session) {
            //err := hoge()  errを再定義してしまっているのはダメ
            stmt, err := hogehoge()  //「:=」は定義されていないものが並んでいる時は、定義されているものも一緒に書いていい
	        session.Id = 1  //返り値の宣言で変数は定義できているから代入できる
	        return
        }
        ```

- ハマったところ
    - postgresqlを永続化すると以下のエラーが発生する
        - docker-composeで永続化を解除したら出なくなったが、このエラーは出ても問題なさそうだから永続化したほうがいい気はする

        ```
        could not open statistics file "pg_stat_tmp/global.stat": Operation not permitted
        ```

    - dockerで起動しているpostgresqlにgolangから接続できない
        - 以下のように色々明示してあげると接続できる
        - 特にhostの部分は、localhostではなくて、dockerコンテナのipを指定することに注意する

        ```go
        Db, err = sql.Open("postgres", "host=postgres user=app_user dbname=app_db password=password sslmode=disable")
        ```

    - データが挿入されているかpostgresqlのターミナルからselect文を打って確認しても何も表示されない
        - SQL構文の末尾には必ず「;」を入れないとだめ

        ```sql
        ---usersテーブルから全てのデータを取得する
        select * from users;
        ```

- 使用ツール
    - 画面遷移設計とデザイン...figma
    - markdownの表作成...NotePM
        - https://notepm.jp/markdown-table-tool

- 参考文献
    - 全体の流れ
        - https://note.com/promitsu/n/n463792216407
    - URL設計
        - https://www.asobou.co.jp/blog/web/url-optimisation

<br></br>

## 開発の手順
- コーディング
    1. HTMLを全てコーディングする(HTML設計)
        - この部分に必要なタグはなにか？
            - 初心者でわからない時はdivやspanで囲みまくっても問題ない
            - とりあえずdivで囲って、あとで適切なタグにしてもいいし
        - 何回も出てきそうな要素なのか？
            - 例えば、ボタンに関しては統一したデザインだからbuttonというclassに全て割り当てようとか
        - 後のCSSのことを考えながらタグづけを行っていく
        - テンプレートタグとかを使うなら、テンプレートのパースと簡易サーバの部分のコーディングは作っておく
    2. CSSでデザインをする
        - HTMLのコーディングが終わったらデザインをする作業に入っていく
        - 簡単なところはfigmaのcssをコピペ
    3. バックエンドのロジックを考えていく
        - アーキテクチャの型(今回はMVC)に当てはめながらコーディングを進めるとスラスラ書ける

<br></br>

## to do
1. 設計を終わらせる(OOP_designのREADMEを参照)
    - URL設計も忘れずに
2. MVCアーキテクチャで実装してみる(app_architecutureのREADME参照)
3. レイヤードアーキテクチャにリファクタリングしてみる(app_architecutureのREADME参照)
4. CSS設計を学ぶ
    - CSS設計完全ガイド　～詳細解説＋実践的モジュール集

---

## 開発メモ

- ログインのプロセス
    1. login.htmlでフォームを設置
    2. ログイン画面を表示するハンドラ関数loginを定義
    3. login.htmlのフォームのactionで「/authenticate」のURIを指定
        - フォームのactionは指定されたURIにmethodで指定されたリクエストを送る動作をする
        - authenticateはhtmlを用意する必要はない。/authenticateにアクセスされた時に処理をするハンドラ関数を定義すればいいだけ
    4. ログイン処理をするハンドラ関数authenticateを定義

- テンプレート名が同じ場合は切り替えることでテンプレートを変えることができる

- go言語でMVCモデルを実現すると(開発を進める前にMVCを意識しながら開発を進めると何から進めればいいかわかりやすい)
    - コントローラー
        - マルチプレクサとURLディスパッチャが二つでコントローラとして機能する
        - main.goがURLディスパッチャ
    - モデル
        - データベース自体の定義
        - データベースへの処理はここが担当する
            - CRUDとかビューにデータを返したり
        - ハンドラ関数はここに定義しない
        - dataディレクトリにまとめる
    - ビュー
        - ハンドラ関数が定義されたgoファイルが複数
        - データとテンプレートを混ぜて表示する処理を担当
        - リダイレクトなども行う
        - 必要に応じてモデルにアクセスする
            - データの取得
            - 受け取ったデータをモデルに渡してCRUD操作をしてもらう

- go言語でのディレクトリの分け方
    - パッケージの分け方など
    - https://sanzo83.hatenablog.com/entry/2019/05/01/235039

---

# go言語のメソッドやライブラリの使い方
## template系
- template.ParseFiles(htmlfiles...)
    - htmlテンプレートを解析するメソッド
    - htmlファイルの順番はなんでもいい

- ExecuteTemplate(書き込む場所, テンプレートタグ名, テンプレートに渡す引数)
    - 書き込む場所
        - writerを指定するとhttpレスポンスに書き込む
        - os.Stdoutを指定すると標準出力に書き込む(デバッグに使える)
    - テンプレートタグ名
        - {{define "base"}}を指定したhtmlファイルを実行したかったら、"base"を渡す
        - 他のテンプレートタグは芋づる式に実行されるから渡さなくていい
    - テンプレートに渡す引数
        - なければnilを指定すればいい

- Execute(書き込む場所, テンプレートに渡す引数)
    - ExecuteTemplateの方を使えばいいと思う

- template内に値を渡す方法
    - https://qiita.com/tetsuzawa/items/0d043ad76b9705cdbb79

## database.sql
- SELECT系
    - 複数件検索
        - Queryメソッド
        - 取得する系のクエリの実行に使う
        - SELECTとか
        - 複数件取得したそれぞれの行にアクセスするには、Nextメソッドをfor文で回して一つ一つアクセスする

    - 一件検索
        - QueryRowメソッド
        - 一行だけ取得する時に使われる

- INSERT系
    - 一件追加
        - Execメソッド
        - 行を一切返却しないクエリの実行に使う
        - INSERTとか

        ```go
        //resultには最終挿入行のIDや変更行数が入る
        result, err := db.Exec("INSERT INTO users (name, age) VALUES ($1, $2)","gopher",27,)
        ```

    - 一件追加かつ追加したデータを取得
        - QueryRowメソッド
            - PostgreSQLの場合は、更新系のクエリの時にもQueryRowが使われることがある。それが今回の場合。
            - QueryRowはinsertした後に結果セットを返す。insert後の値が結果セットの中に含まれているので、Scanメソッドで変数に書き込むことで取得
            - クエリ内でreturning句を使うことで結果を返してくれる
            - それ以外はExecでいいと思う

    - PreparedStatementを使用した複数件取得
        - PreparedStatementでQueryRowまたはExecを用意して、for文で回してinsetする
        - 普通にQueryRowやExecをfor文で回してもいいらしいが、何回もアクセスする場合はPreparedStatementを使用したほうがいい

- UPDATE系
    - 1件または複数件の更新
        - Execメソッド
            - INSERTと違って処理結果を取得することが少ないからExecでいい
        
        ```go
        query := "update table1 set display_name=$1, sex=$2, birthday=$3, age=$4, married=$5, rate=$6, salary=$7 "
        query += "where id=$8 returning id"
        result, err := db.Exec(query, nil, 0, nil, nil, nil, nil, nil, id)
        if err != nil {
            t.Fatalf("クエリーの実行に失敗しました。: %v", err)
        }
        if c, err := result.LastInsertId(); err != nil {
            t.Logf("LastInsertIdを取得できません。: %v", err)
        } else {
            t.Logf("LastInsertId: %v", c)
        }
        if c, err := result.RowsAffected(); err != nil {
            t.Errorf("RowsAffectedを取得できません。: %v", err)
        } else {
            t.Logf("RowsAffected: %v", c)
        }
        ```
    
    - PreparedStatementを使用した複数件の更新

        ```go
        stmt, err := db.Prepare(query)
        if err != nil {
            t.Fatalf("Prepareに失敗しました。: ", err)
        }
        for i := 0; i < 5; i++ {
            result, err := stmt.Exec(nil, 0, nil, nil, nil, nil, nil, id - i)
            // 省略
        }
        stmt.Close()
        ```

- DELETE系
    - 1件または複数件の削除

        ```go
        query := "delete from table1 where id=$1"
        result, err := db.Exec(query, id)
        if err != nil {
            t.Fatalf("クエリーの実行に失敗しました。: %v", err)
        }
        if c, err := result.LastInsertId(); err != nil {
            t.Logf("LastInsertIdを取得できません。: %v", err)
        } else {
            t.Logf("LastInsertId: %v", c)
        }
        if c, err := result.RowsAffected(); err != nil {
            t.Errorf("RowsAffectedを取得できません。: %v", err)
        } else {
            t.Logf("RowsAffected: %v", c)
        }
        ```

    - PreparedStatementを使用した複数件の削除

        ```go
        stmt, err := db.Prepare(query)
        if err != nil {
            t.Fatalf("Prepareに失敗しました。: ", err)
        }
        for i := 0; i < 5; i++ {
            result, err := stmt.Exec(id - i)
            // 省略
        }
        stmt.Close()
        ```

- トランザクション

    ```go
    tx, err := db.Begin()
    if err != nil {
        t.Fatalf("トランザクションの取得に失敗しました。: %v", err)
    }
    query := "insert into table1 (display_name, sex, birthday, age, married, rate, salary) "
    query += "values ($1, $2, $3, $4, $5, $6, $7) returning id"
    var r = createRecord()
    var newId int
    err := tx.QueryRow(query, r.displayName, r.sex, r.birthday, r.age, r.married, r.rate, r.salary).Scan(&newId)
    // 本来ならerrの内容を確認してcommitまたはrollbackを決める必要がある
    err = tx.Commit()
    // err = tx.Rollback()
    if err != nil {
        t.Fatalf("トランザクションのコミットに失敗しました。: %v", err)
    } else {
        t.Logf("トランザクションをコミットしました。")
    }
    ```

- 参考文献
    - https://taknb2nch.hatenablog.com/entry/20131123/1385222792

---

