# Goプログラミング実践入門 書籍memo

- スケーラビリティ
    - アプリケーションの処理能力を簡単に増強して処理できるリクエストの数を増やすことのできる能力
    - スケーラビリティの種類
        - 垂直スケーラビリティ
            - 単一のマシンでCPU数を増やして処理能力を向上させる
        - 水平スケーラビリティ
            - マシンの台数を増やして処理能力を向上させる
    - go言語はどちらのスケーラビリティにも優れている
        - 並行プログラミングのサポートにより垂直
        - ロードバランサー、k8sの利用により水平

---

- アプリケーションとは
    - ユーザとのやりとりによって、何かの活動を援助するもの
        - 財務管理システム、人事管理システム
- Webアプリケーションとは
    - Web経由で配信されるプリケーション
    - 機能としては以下を満たすもの
        1. 呼び出したクライアント(ブラウザ)にHTMLを返す。クライアントはHTMLをレンダリングしてユーザに提示
        2. データ(画像とか)はHTTPを使ってクライアントに送信される
- Webサービスとは
    - Webアプリケーションの1の機能を満たさないもの
- Webサーバとは
    - HTTPリクエストに応答してHTTPレスポンスとしてクライアントにHTMLを送り返すコンピュータのこと
    - Webアプリケーションは単にHTMLを返すだけではなくて、処理をしてから送り返すのに対してWebサーバは特定のディレクトリにあるHTMLを返すだけ
        - このことからWebサーバは特殊なWebアプリケーションとみれる

---

- HTTP
    - リクエスト/レスポンス　からなる二台のコンピュータが会話をする際の基本的な方法
    - ステートレス
        - 一つのリクエストとそれに対する一つのレスポンスで完結するから、以前のリクエストとレスポンスは記憶していない
        - 対して、FTPやTelnetTelnetのような接続型のプロトコルではクライアントとサーバの間に持続的な通信チャネルが形成される
    - 常にリクエスト側から会話を始める
    - HTTP 0.9にはGETメソッドしかなかった

- CGI
    - Webアプリケーションを実現するために生まれた最古の技術
    - Webサーバが別の外部プロセスで実行されているプログラムと通信することを可能にした
        - CGIが標準出力に書き出すものは全てサーバ経由でクライアントに返される
        - 例えば、「ユーザ->Webサーバ->CGI->コマンドプロンプト」みたいなことかな？
    - どんな言語でもかけるがCGIができた当時はPerlによって書かれていた
    - 他にもSSIやJSPやASPなど色々ある
        - http://www.tohoho-web.com/wwwxx036.htm

---

- HTTPリクエスト
    - 以下の行で構成される(以下の4行以上で一つのリクエスト)
        1. リクエスト行
            - 「リクエストメソッド、URI、HTTPのバージョン」　この順番
        2. リクエストヘッダ(0行以上)
            - 「<名前>: <値>」で表される
            - HOSTはサーバ側のこと
            - User-Agentはクライアント側のこと(今回はブラウザ)
        3. 空行
        4. メッセージ本体(省略可)
            - 多分htmlで書かれている
    - https://wa3.i-3-i.info/word1845.html
    ```
    リクエスト例

    1: GET /Protocol/rfc2616/rfc2616.html HTTP/1.1
    2: HOST: www.w3.org
    3: User-Agent: Mozilla/5.0
    4: 空行
    ```

- よく使われるHTTPリクエストヘッダ(説明は暇な時に本を見て追記)
    - Accept
    - Accept-Charset
    - Authorization
    - Cookie
    - Content-Length
    - Content-Type
    - Host
    - Referrer
    - User-Agent

- リクエストメソッドの種類(説明は暇な時に本を見て追記)
    - GET
        - 指定されたリソースを返すようにサーバに指示する
    - HEAD
        - レスポンスヘッダを入手したいが、重いメッセージ本体はネットワークに流したくない場合に使われる
    - POST
        - メッセージ本体のデータをURIで示されたリソースに渡すようにサーバに指示する。サーバがメッセージ本体をどのように処理するかはサーバに任せる
    - PUT
    - DELETE
    - TRACE
    - OPTIONS
    - CONNECT
    - PATCH
    - 

- 安全なリクエストメソッド
    - サーバの状態を変更しないものは安全、変更するものは安全でない
        - 安全
            - GET, HEAD, OPTIONS, TRACE
        - 安全でない
            - POST, PUT, DELETE

---

- HTTPレスポンス
    - 以下の行で構成される(以下の行で一つのレスポンス)
        1. ステータス行
        2. 0個以上のレスポンスヘッダ
            - 「<名前>: <値>」で表される
        3. 空行
        4. メッセージ本体
            - htmlで書かれている
    ```
    HTTPレスポンスの例

    1: 200 OK
    2: Date Sat, 26 Nov 2016 12:58:58 GMT
    3: Server Apache/2
    4: Last-Modified: Thu, 25 Aug 2016 21:01:33 GMT
    5: Content-Length: 33115
    6: Content-Type: text/html; charset=iso-8859-1
    7: 
    8: <!DOCTYPE html> <html>  <head><head>  </html>
    ```

- レスポンスのステータスコード
    - 1桁目がクラスを表している
        - 1XX
            - 情報提供。サーバがリクエストを処理し始めていることをクライアントに伝える
        - 2XX
            - 成功。クライアントの要求が受け入れられた。標準的なレスポンスは200 OK
        - 3XX
            - リダイレクション
        - 4XX
            - クライアントエラー
        - 5XX
            - サーバエラー

- レスポンスヘッダ
    - Allow
    - Content-Length
    - Content-Type
    - Date
    - Location
    - Server
    - Set-Cookie
    - WWW-Authenticate

- URI
    - URLとURNの総称
        - URLに慣れ親しんでいる
    - 構成
        - <スキーム名>:<階層部>[?<クエリ>][#<フラグメント>]
            - スキーム名
                - httpやftpなど
            - 階層部
                - //で始まった場合@までがオプションのユーザ情報
            - クエリ
            - フラグメント

---

- webアプリの構成
    1. HTTPを介し、HTTPリクエストの形でクライアントから入力を受け取る
    2. HTTPリクエストを処理して、必要な作業を行う
    3. HTMLを生成して、HTTPレスポンスの形でレスポンスを返す

- webアプリの処理手順
    1. **クライアントはサーバのURLをターゲットにリクエストを送信する**
    2. **サーバにはマルチプレクサがあり、URLを見て、処理を担当するハンドラにリダイレクトする**
        - これをルーティング処理という
            - djangoにはプロジェクトルーティング(ルートのurls.py)とアプリケーションルーティング(アプリ内のurls.py)がある
                - goのマルチプレクサはアプリケーションルーティングという処理を行う
        - goではListneAndServeでマルチプレクサを設置してサーバを立てる
        - マルチプレクサはdjangoではURLディスパッチャという。
            - djangoではURLディスパッチャにviewを登録するのにはURLPatternsで定義する
            - goではマルチプレクサにハンドラを登録するのにhttp.HandleFuncで定義する
    3. **ハンドラがリクエストを処理して、必要な仕事をする**
        - ハンドラはdjangoではviewという
    4. **ハンドラがテンプレートエンジンとモデルを呼び出して、クライアントに返信するための正しいHTMLを生成する**
    ![スクリーンショット-2020-07-10-15 18 38-1024x666](https://user-images.githubusercontent.com/53253817/96835455-8f724e80-147e-11eb-9098-4f760aecd4e6.png)

- ハンドラ
    - リクエストに対して具体的な処理が定義されているもの全般
        - このことから、マルチプレクサはハンドラの一種ということがわかる
            - なぜかというと、リクエストに対して「ハンドラに振り分ける」という具体的な処理だから
    - クライアントから送られてきたHTTPリクエストを受け付け、処理する
    - goに限らずhttpリクエストを引数にとる関数やメソッドはハンドラだと思う
        - さらにフレームワークによってユニークな引数がある
            - djangoならpkといったidで、goならResponseWriter
    - HTMLを生成するためにテンプレートエンジンを呼び出す
    - go言語ではhttp.ServeHTTPっというメソッドを持っているものをハンドラという
        - ServeHTTPの根本はhttp.Handlerというものだから
    - https://qiita.com/huji0327/items/c85affaf5b9dbf84c11e

- マルチプレクサ
    - ハンドラの一種
    - 多重通信の入り口
        - 色々なリクエストに対して、ハンドラへの振り分けをしてくれる
    - リクエストが来たらURLを調べて、リクエストを所定のハンドラにリダイレクトする
        - その後はハンドラがリクエストを処理する

- テンプレート
    - 静的テンプレート
        - よくわからない
    - アクティブテンプレート
        - 変数やIFやFORといったプログラミングの要素が埋め込まれたHTMLのこと
        - djangoでいうと{{}}で囲まれた変数とか

- テンプレートエンジン
    - テンプレートデータ(データベースにあるデータ)を埋め込んで最終的なHTMLを生成する

---

- ルートURL(/)
    - http://localhost:8080/src/code だったら、8080の隣の「/」がルートURLになる
        - srcはルート(/)のサブディレクトリ

---

- https
    - ユーザのログイン機能を搭載するなら必要
    - SSL/TLSの上にhttpのレイヤーを置いただけ
    - goではListenAndServeTLSで実装できる

---


# go言語の文法
- 関数
```
//書式

fucn 関数名(パラメーター　型[,...複数可])　戻り値の型[,...複数可] {
    処理
}
```

```go
//例1
func add(atai1 int, atai2 int) int {
    return atai1 + atai2
}

add(1, 2) // add関数使う

```

```go
//例2
func add(atai1 int, atai2 int) (ans int) {
    ans = atai1 + atai2
    return
}
```

```go
//例3
func main() {
    add, sub := calc(1, 2)
    fmt.Println(add)    // 3
    fmt.Println(sub)    // -1
}

func calc(atai1 int, atai2 int) (add int, sub int) {
    add = atai1 + atai2
    sub = atai1 - atai2
    return
}
```

<br></br>

- ここは書き直す。以下を参考に
    - https://qiita.com/tenntenn/items/45c568d43e950292bc31
    - https://qiita.com/tikidunpon/items/2d9598f33817a6e99860

- レシーバとは
    - メソッドを呼び出される対象のこと
        - pythonやjavaでいうクラスのインスタンスみたいなものかな？(golangにはクラスはないけど)
```
  p := Person{Name: "Taro"}
  p.Greet("Hi")
  ↑
コイツ
```

- 構造体
    - 中にフィールドを定義することができる
        - フィールド
            - 「<フィールド名> <型>」で定義
    - 普通の変数と同様にメソッドも定義することができる
        - メソッド
            - 値レシーバとポインタレシーバがある
            - 「func (レシーバ値 レシーバ型) 関数名」で定義
    - https://skatsuta.github.io/2015/12/29/value-receiver-pointer-receiver/

```go
/*
値レシーバ
*/

//メソッドは、構造体でなくてもintといった変数にも定義できる
type Person struct{ 
    Name string 
}

// Person 型に対してGreetメソッドを定義する
func (p Person) Greet(msg string) {
    fmt.Printf("%s, I'm %s.\n", msg, p.Name)
}

func main() {
    pp := &Person{Name: "Taro"} // ポインタ型の変数を用意する
    (*pp).Greet("Hi")           //=> Hi, I'm Taro. | 当然呼び出せる
    pp.Greet("Hi")              //=> Hi, I'm Taro. | コンパイラが上のコードに変換してくれる
}
```

```go
/*
ポインタレシーバ
*/

type Person struct{
    Name string
}

// *Person 型に対してメソッドを定義する
func (pp *Person) Shout(msg string) {
    fmt.Printf("%s!!!\n", msg)
}

func main() {
    p := Person{Name: "Taro"} // 値型の変数を用意する
    (&p).Shout("OH MY GOD")   //=> OH MY GOD!!! | 当然呼び出せる
    p.Shout("OH MY GOD")      //=> OH MY GOD!!! | コンパイラが上のコードに変換してくれる
}
```

- メソッド
    - 任意の型に結び付けられた関数のこと
        - 任意の型なので、変数や構造体やインターフェースなど何にでも定義することができる関数


- インターフェース
    - フィールドに関数の形だけを定義する
    - javaのimplementsみたいなものかな

# 気になること
- プログラミング言語の静的型付けと動的型付けの違い
- webにおけるマイクロサービスとは
    - 小さなサービスを組み合わせて大規模なサービスを実現することかな？
- Adobe Flashとは？
- ステートレスとは？
    - 「状態を持たない」という意味。前後の情報がないということなので、前後のことは記憶していない
- マルチプレクサとは？
- セッションとは？
- cookieとは？
- なぜListenAndServerの第二引数でハンドラを指定しないといけないのに、デフォルトがDefaultServeMuxというマルチプレクサなのか?
    - ServerMuxは構造体Handlerのインスタンス
    - ServerHTTPはServerMuxのメソッド
    - DefaultServerMuxはServerMuxのインスタンス
    - つまりDefaultServerMuxは元を辿ればHandlerから来ているからハンドラで指定している
    - go言語においてはServerHTTPがメソッドのものはハンドラ
    - https://qiita.com/gonza_kato_atsushi/items/5ae6fd9e977bbbffd6cd
- オブジェクト指向での抽象クラスとinterfaceとは
    - 以下がわかりやすい
    - https://qiita.com/yoshinori_hisakawa/items/cc094bef1caa011cb739