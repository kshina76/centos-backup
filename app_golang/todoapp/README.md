# toapp開発
- go言語でMVC、3層、DIP無しのtodoアプリを作成する
- 参考文献
    - https://qiita.com/ogady/items/34aae1b2af3080e0fec4#作ったもの
    - https://eng-blog.iij.ad.jp/archives/2442
    - https://qiita.com/yuukiyuuki327/items/238814326964e06dd655
    - DDDのレイヤードと純粋なレイヤードの二つで解説している
        - https://qiita.com/tono-maron/items/345c433b86f74d314c8d

## ユースケース
- todoを登録できる
- todoを編集できる
- todoを削除できる
- todoの状態を選択できる
    - todoが「終了したのか、取り掛かっている最中なのか、取り掛かっていないのか」の3つの状態

## アクティビティ
- todoの登録
    - ユーザ
        1. todoの内容を入力
        2. 状態を選択
        3. submitボタンを押す
    - サーバ
        1. 登録内容をrequestから取得
        2. todoの内容と状態をDBに格納
        3. todoの内容全体をDBから取得
        4. todoの内容全体を表示
- todoの編集
    - ユーザ
        1. 既存のtodoの編集ボタンをクリック
    - サーバ
        1. 編集画面を表示(入力するところだけを表示する)
    - ユーザ
        1. 編集内容の入力(元の内容はテキストボックスに表示させておく。状態だけの変更かもしれないから)
        2. 状態を選択
        3. submitボタンを押す
    - サーバ
        1. 編集内容をrequestから取得
        2. 編集されたtodoの内容と状態を古いものと置き換える
        3. todoの内容全体をDBから取得
        4. todo内容全体を表示
- todoの削除
    - ユーザ
        1. 既存のtodoの削除ボタンをクリック
    - サーバ
        1. 本当に削除していいかの確認画面を表示
    - ユーザ
        1. yesかnoのボタンをクリック
    - サーバ
        - yes
            1. DBから指定されたデータを削除
            2. todoの内容全体をDBから取得
            3. todoの内容全体を表示
        - no
            1. ホーム画面に遷移
            2. todoの内容全体を取得
            3. todoの内容全体を表示

## 画面遷移設計、デザイン
- 簡単なアプリのため省略

## URL設計
- GET /todo
    - ホーム画面
- GET /todo/edit/id
    - 編集画面
- GET /todo/delete/id
    - 削除確認画面
- POST /todo
    - 新規作成したtodo登録
- POST /todo/edit/id
    - 編集したtodo登録
- POST /todo/delete/id
    - 選択されたtodo削除

## DB設計
- todo
    - id
    - title
    - status
    - date

## アーキテクチャ設計
- 3層アーキテクチャ
    - プレゼンテーション層
        - MVC2
    - ビジネスロジック層
        - Transaction Script
    - データアクセス層
        - データベースのテーブルそのまま
- インスタンスの生成と管理
    - mainでDI
    - レイヤー間はinterfaceで疎結合
    - DIPは無し
        - ビジネスロジック層とデータアクセス層の間はDTOでやりとりすることで、循環参照を回避している

## クラス設計
- todo
    - id
    - title
    - status
    - date

## システム構成
- postgreSQL
- nginx
- EC2

## 後々追加する機能
- まとめて削除ボタン
- 一つ一つのtodoの詳細を表示するページ
- ユーザ別のtodo(ログイン機能が必要)

## わかったこと
- URL設計で、一つのURLに対してGET,POST,PUT,DELETEなど色々な命令を割り当てることができる
    - わざわざGETはこのURL、POSTはこのURLとかやらなくてもいい
- vscodeのHTML Previewという拡張機能がめっちゃ便利
    - コード書きながら横にリアルタイムでページの確認ができる
- DDDにおいてrepositoryとは、データの永続化をするメソッドを定義するためのinterfaceを書くところ
    - つまりinfra層のためのinterface
- domain層は、repositoryとmodelとserviceに分かれていて、service->infra->model の順に依存している
    - repository
        - DIPを実現するための部分
        - infra層のためのinterfaceを定義する(infra層ではSQLを発行するためのメソッドを定義する)
    - model
        - ビジネスロジックのプロパティだけのものを実装する
    - service
        - ビジネスロジックの関数を定義する
- 依存するのは直下でなくてもいい
    - 提唱されているレイヤードアーキテクチャは直下のレイヤにしか依存してはいけないと言われているが、デメリットとしてコードが冗長になること。
    - 小規模でそれほど複雑でない時や、チームで話し合って、冗長化することによるメリットよりもコードをシンプルにした方がいいという結論に至れば一つ飛ばしの層に依存しても問題はない。
    - https://qiita.com/tono-maron/items/345c433b86f74d314c8d
- レイヤードアーキテクチャやクリーンアーキテクチャにおいて実装する順番は「内から外」
    - 依存関係は「handler->usecase->domain<-infra」なので
        - 「domain->infra->usecase->handler」の順番に実装する
    - https://qiita.com/yuukiyuuki327/items/238814326964e06dd655
- レイヤードアーキテクチャ実装手順
    1. domain内のmodelを定義
        - ここは構造体を宣言するだけでいいのかな？多くの例はそうなっているけど
    2. domain内のrepositoryを定義
        - ユースケース、URL設計とかから必要な動作をあぶり出す 
- go言語でstructを&をつけてポインタとして渡す理由(関数がわで*model.TodoModelのように受け取る理由)
    - structにそのまま渡すと構造体をフルでコピーしてメモリの無駄になってしまうから。
    - &をつけて渡すことで参照渡しになってメモリを消費しないから。
- go言語で構造体の色々な初期化方法(インスタンス化)
    - newを使った初期化が一番インスタンス化っぽくてわかりやすい
    - newを使った場合は、&struct型を返す
    - https://qiita.com/cotrpepe/items/b8e7f70f27813a846431
- go言語の構造体の実装パターン
    - https://blog.monochromegane.com/blog/2014/03/23/struct-implementaion-patterns-in-golang/
- クリーンアーキテクチャのinjectorはmainで全てのコンストラクタを起動する感じ
    - https://qiita.com/ogady/items/34aae1b2af3080e0fec4#作ったもの
- go言語でのstructからstructへの埋め込みは継承ではなくて委譲
    - 埋め込みとinterfaceが合わさって初めて継承みたいなことができる
    - https://qiita.com/Maki-Daisuke/items/511b8989e528f7c70f80
- go言語のコンストラクタはpythonのinitのコンストラクタに置き換えて考えるとわかりやすい
    - ちなみにコンストラクタは他言語でもメソッドではないので、go言語でもレシーバは付けない
    - コンストラクタ名は、go言語だと慣例で「New+構造体名」
    - 他言語と同じように、コンストラクタは構造体のプロパティを初期化するために使われる
    - https://qiita.com/Sekky0905/items/10c8ae9cee719d66fa84
- go言語でのオブジェクト指向は他言語と同じように上から、「struct」「コンストラクタ」「メソッド1」「メソッド2」の順に書くとわかりやすい
- repositoryがdomain層のinterfaceとなってるけど、domain層のmodelが振る舞いを持った場合はどのようなinterfaceの構成になるのだろうか？
    - https://qiita.com/ogady/items/34aae1b2af3080e0fec4#作ったもの
- クリーンアーキテクチャ(レイヤードアーキテクチャ)のわかりやすい図(自作)

    ![clean_architecture](https://user-images.githubusercontent.com/53253817/99709796-16006700-2ae3-11eb-8eab-8ac9c5445a54.png)

- レイヤードアーキテクチャの開発手順として、例えばCRUDアプリなら一つの機能に絞って(例えばCreateの機能だけ)作って、そこに他のRUDの機能を追加していくという開発手順がわかりやすいし、レイヤードアーキテクチャで疎結合にしている利点を感じやすい。機能追加するときに色々なところを書き換える必要がなくなるから
- レイヤードアーキテクチャの開発手順として、各層から下位層のメソッドを呼び出すときは相手のinterfaceの引数と返り値だけを見ながら実装すると、迷わないで開発できると思う。あとは、下位層から実装することを頭に入れる。実装するときにユースケース、アクティビティ図などが重要だということがわかったので、印刷して置きながら実装するのがいいかも(デュアルディスプレイとか)
- マルチプレクサはgorillaを使うといい
    - ルーティングするURLに色々なカスタマイズをすることができる
    - r.HandleFunc("/edit/{id:[0-9]+}", th.Edit) といった指定をすることができる
- 小規模なアプリケーションなら、3層、interfaceあり、トランザクションスクリプト、DIP、MVCがいいかも
    - DIPが無いとDTOを使ってデータのやりとりをしないといけないから面倒
        - go言語は循環参照が禁止されているから


---

# go言語でソフトウェアアーキテクチャを学ぶ前に理解しておく文法
- interfaceの基本
    - OOP言語でinterfaceを実現した場合
        1. interfaceを定義する
        2. クラスを作成してimplementsでinterfaceを継承
        3. クラス内のメソッドでオーバーライド

        ```java
        interface Calc {
            void calculation();
        }

        class Sum implements Calc {
            //オーバーライド
            public void calculation() {
                //処理
            }
        }
        ```

    - go言語でinterfaceを実現
        1. interfaceを定義する
        2. 構造体を作成
        3. 2で作成した構造体をレシーバとして、interfaceに定義したメソッドと同名のメソッドを定義
        4. Calcインタフェースを引数にした関数を定義して、Calcインタフェースのメソッドを呼び出す
        5. main側でSum構造体を引数に渡す(Sum構造体はCalcインタフェースとして振舞う)
            - https://qiita.com/tono-maron/items/345c433b86f74d314c8d

        ```go
        type Calc interface {
            calculation()
        }
        type Sum struct {
            X int
            Y int
        }
        func (sum *Sum) calculation() (result int, err error) {
            result = sum.X + sum.Y
            return
        }
        func printCalc(calc Calc) {  //Sumインスタンスが渡される。SumはCalcインタフェースとして振舞うから渡せる
            fmt.Println(calc.calculation())
        }
        func main() {
            sum := &Sum{1, 2}
            printCalc(sum)  //CalcインタフェースにSum構造体を渡しているが、Sum構造体はCalcインタフェースを満たしているので、Calcインタフェースとして振舞うから問題ない
        }
        ```

    - 意識すること
        - 常に構造体をクラスと置き換えて考える
        - レシーバを定義していたらすぐに構造体(クラス)と結び付けてメソッドということを意識する
        - インタフェースだけを外部にエクスポートして公開すること。具象クラスは先頭を小文字にすることで外部に設計の詳細を公開しないようにする

- interfaceの応用
    - https://qiita.com/tenntenn/items/eac962a49c56b2b15ee8
    - https://qiita.com/tenntenn/items/e04441a40aeb9c31dbaf
    - https://qiita.com/tenntenn/items/92928990173514c2adea

- 埋め込み(継承)
    - go言語に継承はないが、埋め込みを使うことで他の構造体をラップした構造体を作ることができる
    - 中に埋め込んだ構造体のフィールドやメソッドはあたかも外の構造体のもののように振る舞うことができる。
        - 構造体のメンバやメソッドを統合したように振舞うということ(継承と同じ動作)
    
    ```go
    type Hoge struct {
        N int
    }
    type Piyo struct {
        Hoge
        M int
    }
    func main() {
        piyo := &Piyo{Hoge{1}, 2}
        fmt.Println(piyo.N, piyo.M)  //継承した時と同じように呼び出せる
        fmt.Println(piyo.Hoge.N, piyo.M)  //素直に呼び出すこともできる
    }
    ```

    ```go
    //埋め込みを使うとこれを宣言したことと同値になるということ(継承ができているということ)
    type Piyo struct {
        N int
        M int
    }
    ```

- 埋め込みを使ったインタフェースの部分実装
    - 埋め込む構造体にあるインタフェース定義するメソッドの一部を実装させ、残りのメソッドは外側の構造体で実装するという手法

    ```go
    type Person interface {
        Name() string
        Title() string
    }
    func New(gender Gender, firstName, lastName string) Person {
        p := &person{firstName, lastName}
        if gender == Male {
            return &male{p}
        } else {
            return &female{p}
        }
    }
    type person struct {
        firstName string
        lastName  string
    }
    func (p *person) Name() string {
        return p.firstName + " " + p.lastName
    }
    type female struct {
        *person
    }
    func (f *female) Title() string {
        return "Ms."
    }
    type male struct {
        *person
    }
    func (m *male) Title() string {
        return "Mr."
    }
    func printFullName(p Person) {
        fmt.Println(p.Title(), p.Name())
    }
    func main() {
        taro := New(Male, "Taro", "Yamada")
        printFullName(taro)
        hanako := New(Female, "Hanako", "Yamada")
        printFullName(hanako)
    }
    ```

- オーバーライド
    - 埋め込み(継承)をしてから同名のメソッドを定義することで実現
    - オーバーライドする前の親クラスのメソッドを呼び出したかったら、「Parent.printName()」で呼び出せる
        - pythonでいうsuper()を行っているのと同じ

    ```go
    type Parent struct {
	    name string
    }
    func (p *Parent) printName() {
	    log.Println(p.name)
    }
    type Child struct {
	    Parent
    }
    func (p *Child) printName() {
	    log.Println("Child")
    }
    func main() {
	    p := &Parent{
		    name: "parent"
	    }
	    c := &Child{ *p }
	    c.printName() // "Child"
    }
    ```

- コンストラクタ
    - 構造体をインスタンス化して返す関数
    - 慣例でメソッド名にNewプレフィックスをつける

    ```go
    type Calc interface {
        Caluculation()
    }

    type Sum struct {
        X int
        Y int
    }

    func NewSum() Sum {
        return Sum{
            1,2
        }
    }
    ```

- 参考文献
    - https://qiita.com/tenntenn/items/e04441a40aeb9c31dbaf
    - https://qiita.com/tenntenn/items/eac962a49c56b2b15ee8
    - https://tomokazu-kozuma.com/how-to-override-methods-in-golang/

# go言語を使ってクリーンアーキテクチャを実現
- http://inukirom.hatenablog.com/entry/di-in-go
- https://qiita.com/ogady/items/34aae1b2af3080e0fec4
- https://qiita.com/Sekky0905/items/2436d669ff5d4491c527
- https://eng-blog.iij.ad.jp/archives/2442
- https://medium.com/eureka-engineering/pairs-engage-server-side-architecture-c056bd8f598

# 色々なメモ
- sassをまとめてコンパイル
    - https://qiita.com/tonkotsuboy_com/items/67d9fd4d054a45af9f34