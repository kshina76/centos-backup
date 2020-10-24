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
                - リクエストメソッドはGETとかPOST
                - URIはクライアントからサーバに対するリクエスト対象のリソース（サーバ内に保管されているリソース）
                    - URIはURLとURNの総称だが、使われるのはURLがほとんど
                        - URLの一般形
                            - scheme://[userinfo@]host/path/[?query][#fragment]
                            - scheme:opaque[?opaque][#fragment]
            - go言語での取得方法
                - リクエストメソッド
                    - requestの中にMethodで定義されている
                - URL
                    - requestの中にurl.URL型で定義されている
                        - url.URLは構造体なので、フィールドとして「Scheme, Opaque, User, Host, Path, Rawquery, Fragment」が定義されている
                - HTTPのバージョン
                    - ドキュメントみないとわからん
        2. リクエストヘッダ(0行以上)
            - 「<名前>: <値>」で表される
            - HOSTはサーバ側のこと
            - User-Agentはクライアント側のこと(今回はブラウザ)
            - go言語だとrequestの中にHeader型で定義されている
            - djangoだとrequest.METAのなかに入っている
        3. 空行
        4. メッセージ本体(body)
            - GETでは空
            - POSTでformに入力された値やcurlの引数などが入ってくる
            - htmlではないと思う。「変数=値」といった情報が送られて、レスポンスでhtmlに変数が埋め込まれて返ってくるのだと思う
            - goではリクエスト、レスポンス共にrequestの中のBodyに定義されている

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

- ハンドラを登録する
    - 一つ目のコード
        - handler引数にマルチプレクサを指定しないで、自作のハンドラを指定する
        - マルチプレクサがないので、どんなURLにアクセスされても単一の処理を返すようになっている
    - 二つ目のコード
        - handler引数に何も指定しないことで、デフォルトのマルチプレクサのDefaultServeMuxが指定される
        - ハンドラを直接作ってマルチプレクサに登録している
    - 三つ目のコード
        - handler引数に何も指定しないことで、デフォルトのマルチプレクサのDefaultServeMuxが指定される
        - ハンドラ関数を作って、マルチプレクサに登録している
            - 三つ目のコードと違う点は、ハンドラのように振舞う関数を登録していること。それをハンドラ関数としている
        - 通常、この三つ目の方法を使う

```go
type MyHandler struct{}

func (h *MyHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World!")
}

func main() {
	handler := MyHandler{} // handlerはハンドラ。
	server := http.Server{
		Addr:    "127.0.0.1:8080",
		Handler: &handler,
	}
	server.ListenAndServe()
}
```

```go
type HelloHandler struct{}

func (h *HelloHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello!")
}

type WorldHandler struct{}

func (h *WorldHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "World!")
}

func main() {
	hello := HelloHandler{} // helloはハンドラ（http.Handler）。ServeHTTPを持っているので
	world := WorldHandler{}

	server := http.Server{
		Addr: "127.0.0.1:8080",
		// Handlerは指定しない -> DefaultServeMuxをハンドラとして利用
	}

	http.Handle("/hello", &hello) // ハンドラhelloをDefaultServeMuxに登録
	http.Handle("/world", &world)

	server.ListenAndServe()
}
```

```go
func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello!")
}

func world(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "World!")
}

func main() {
	server := http.Server{
		Addr: "127.0.0.1:8080",
		// Handlerは指定しない -> DefaultServeMuxをハンドラとして利用
	}
	http.HandleFunc("/hello", hello) // 関数をハンドラに変換して、DefaultServeMuxに登録
	http.HandleFunc("/world", world)

	server.ListenAndServe()
}
```

---

- ハンドラとハンドラ関数のチェイン
    - ハンドラはリクエストを処理することだけを記述して簡潔にしたいが、実際はlogを取る処理やエラー処理などいろいろな処理を書かなければいけない
        - 色々と処理を盛り込んでしまうと、記述が複雑になって何をするハンドラなのかわからなくなってしまう。
            - 関数を分けてチェインさせると独立した関数として関数の責務がわかりやすくなる
    - 呼び出すときに「protect(log(hello))」のように連なる形で呼び出すからチェインと言われている
    - 多くのフレームワークの裏側でユーザが意識しないでログが使えるようになっているのは、これのおかげだったりする
    - チェインを何個もつなげることをパイプライン処理という

```go
func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello!")
}

func log(h http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		name := runtime.FuncForPC(reflect.ValueOf(h).Pointer()).Name()
		fmt.Println("ハンドラ関数が呼び出されました - " + name)
		h(w, r)
	}
}

func main() {
	server := http.Server{
		Addr: "127.0.0.1:8080",
	}
	http.HandleFunc("/hello", log(hello))
	server.ListenAndServe()
}
```

```go
type HelloHandler struct{}

func (h HelloHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello!")
}

func log(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Printf("ハンドラが呼び出されました - %T\n", h)
		h.ServeHTTP(w, r)
	})
}

func protect(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// some code to make sure the user is authorized
		h.ServeHTTP(w, r)
	})
}

func main() {
	server := http.Server{
		Addr: "127.0.0.1:8080",
	}
	hello := HelloHandler{}
	http.Handle("/hello", protect(log(hello)))
	server.ListenAndServe()
}
```

---

- ServerMuxとDefaultServerMux
    - ルートURLである「/」がマルチプレクサに登録されていたら、URL一致しなかった場合ルートURLが呼び出されるようになっている
    - 以下の例だと、/hello/there にアクセスがきても一致しないので、/ が呼び出される
    ![2020-10-22 18 27のイメージ](https://user-images.githubusercontent.com/53253817/96852603-4b8a4400-1494-11eb-943f-bfc61bd5292f.jpeg)
    - DefaultServerMuxはServerMuxのインスタンス
    - ServerMuxは変数を使ったパターンマッチングが出来ないのが不満なので、HttpRouterというサードパーティのライブラリが使われる

---

- httpsはデフォルトでhttp/2 を使うので余計な処理が必要

---

- HTMLフォーム(名前=値 の形)とgo言語
    - HTMLフォームに入力されてサーバに送信されたデータは**リクエストのボディ部**に置かれる
        - HTMLフォームにおいて、送信されるデータは常に「名前と値のペア」で送信される
            - htmlのformのenctype(コンテンツタイプ)
                - 「名前と値のペア」をボディ部にどのような形式で置くかを指定する
                - html5からtext/plainを指定することもできる
                - 以下は、生のbody部。
                ```
                送信するデータ
                curl -id "first_name=sausheong&last_name=chang" 172.0.0.1:8080/body/


                enctype="application/x-www-form-urlencoded" が指定された場合は長いクエリ文字列としてbody部に配置する
                first_name=sausheong&last_name=chang


                enctype="multipart/form_data" が指定された場合は以下のようになる(わからん)
                ---WebKitFormBoundaryMPNjKpeO9cLiocMw
                ContentDisposition:formdat;name="first_name"sausheong---WebKitFormBoundaryMPNjKpeO9cLiocMwContentDisposition:formdata; name="last_name"chang---WebKitFormBoundaryMPNjKpeO9cLiocMw
                ```

- httpリクエストのbodyからgoでデータを取得する
    - 生のやり方
        - request.Body.Readで読み込む
            - このやり方はやられない
    - Requestのメソッドを使ったやり方
        1. ParseFormまたはParseMultipartFormを呼び出して、リクエストを解析する
        2. 以下から目的に応じたフィールドを呼び出す
            - Form
                - URLからデータ(クエリ)を取得
            - PostForm
                - ボディからデータを取得
            - MultiPartForm
                - URLとボディの両方

![2020-10-23 0 19のイメージ](https://user-images.githubusercontent.com/53253817/96893234-7640c080-14c5-11eb-84d4-b847f97fd311.jpeg)



- htmlのformのenctypeによってformに入力された値をどのように扱うか変わる
    - 多分enctypeの値がリクエストヘッダのcontent-typeに入るのだと思う

- formでファイルをアップアップロードする
    - enctype="multipart/formdata" をhtmlのformで指定する
    - go言語からはFormFileを使う

- JSON形式のボディを持ったPOSTリクエストの処理
    - jQueryやAngularといったフレームワークからのhttpリクエストがJSON形式のボディ
        - HTTPリクエストはHTMLフォームだけから来るわけではない
        - 「名前=値」はHTMLフォームから送られてきたもの
    - jQueryはapplication/x-www-form-urlencoded　でエンコードするからgoではParseFormで取り出せる
        - jQueryはリクエストヘッダのcontent-typeをapplication/x-www-form-urlencodedに設定してリクエストを投げてくる
    - Angularはapplication/json でエンコードするからParseFormでは取り出せない

---

- ユーザにレスポンスを送信する方法
    - ResponseWrite
        - 使用するメソッド
            - Write
                - バイト配列を受け取ってレスポンスのボディに書き込む
                - リクエストのヘッダにcontent-typeが設定されていない場合は、先頭512バイトで判別する
            - WriteHeader
                - HTTPレスポンスのステータスコードを引数に受け取り、レスポンスにステータスコードを設定して返す
                    - 例えば404のエラー処理を実装したかったら404をWriteHeaderに渡す
            - Header
                - 変更可能なヘッダのマップを返すメソッド
                    - ヘッダに設定をしたい時などに使う
                    - 例1、リダイレクトの実装をしたかったら、Headerメソッドを使って、ヘッダのlocationにリダイレクト先のURLを設定する
                        - ちなみにリダイレクトのステータスコードは302
                    - 例2、ボディにjsonを書き込んだときにヘッダの設定でcontent-typeにapplication/jsonを設定する
        - まとめ
            - Writeがボディ部、WriteHeaderがステータス行、Headerがヘッダ部 の書き込みに使われる
    
```go
type Post struct {
	User    string
	Threads []string
}

func writeExample(w http.ResponseWriter, r *http.Request) {
	str := `<html>
<head><title>Go Web Programming</title></head>
<body><h1>Hello World</h1></body>
</html>`
	w.Write([]byte(str))
}

func writeHeaderExample(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(501)
	fmt.Fprintln(w, "そのようなサービスはありません。ほかを当たってください")
}

func headerExample(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Location", "http://google.com")
	w.WriteHeader(302)
}

func jsonExample(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	post := &Post{
		User:    "Sau Sheong",
		Threads: []string{"1番目", "2番目", "3番目"},
	}
	json, _ := json.Marshal(post)
	w.Write(json)
}

func main() {
	server := http.Server{
		Addr: "127.0.0.1:8080",
	}
	http.HandleFunc("/write", writeExample)
	http.HandleFunc("/writeheader", writeHeaderExample)
	http.HandleFunc("/redirect", headerExample)
	http.HandleFunc("/json", jsonExample)
	server.ListenAndServe()
}
```

---

- cookie
    - セッションクッキーと永続性クッキー
        - go言語でクッキーのExpiresフィールドが設定されていないとセッションクッキー
            - セッションクッキーはブラウザが閉じると削除される
            - 設定されていると永続性クッキー
        - 有効期限はgo言語のクッキーのExpiresかMaxAgeで設定できる
- ブラウザへのクッキー送信
    - レスポンスのヘッダのSet-Cookieに設定すると送信できる
        - ヘッダに直接指定してもいいけど、go言語だとnet/httpにSetCookieメソッドが提供されている
- ブラウザからクッキー取得
    - ヘッダーから直接読み取る
        - requestのHeaderフィールドにアクセスしてとる
    - Cookie, Cookiesメソッド
        - 単一のクッキーを取得したい場合はCookie、複数のクッキーを取得したい場合はCookiesを使用する
        - requestに実装されている
- クッキーを利用したフラッシュメッセージ
    - cokkieの構造体のValueにメッセージを入れてレスポンスを送信すればいいのだと思う

```
goにおけるcookieの構造体

type Cookie struct {
    Name string
    Value string
    Path string
    Domain string
    Expires time.Time
    RawExpires string
    MaxAge int
    Secure bool
    HttpOnly bool
    Raw string
    Unparsed []string
}
```

---

- テンプレート
    - 静的テンプレート
        - よくわからない
    - アクティブテンプレート
        - 変数やIFやFORといったプログラミングの要素が埋め込まれたHTMLのこと
        - djangoでいうと{{}}で囲まれた変数とか

- テンプレートエンジン
    - テンプレートデータ(データベースにあるデータ)を埋め込んで最終的なHTMLを生成する
    - テンプレートエンジンの種類
        - ロジックなしテンプレートエンジン
            - 文字列を置換するだけの処理
        - ロジック埋め込みテンプレートエンジン
            - プログラミング言語のように変数やIFなどが使えるテンプレートを実行時に処理する
    - go言語はロジック有り無しどちらも対応しているハイブリッド型

- テンプレートからHTMLが生成されるまでの処理
    1. ハンドラがテンプレートエンジンを呼び出す
    2. ハンドラがテンプレートとデータ(モデルから取り出す)をテンプレートエンジンに渡す
    3. テンプレートエンジンがHTMLを生成
        1. ParseFilesでテンプレートファイルを解析する
        2. Executeで解析済みテンプレートにデータを埋め込んでHTMLを生成
            - ParseFilesで複数のテンプレートが引数に渡されていて、二つ目以降のテンプレートをexecuteしたかったら、ExecuteTemplatesを呼び出す
    4. テンプレートエンジンがResponseWriterにHTMLを書き込む
    5. ResponseWriterがHTTPレスポンスにそれを追加する

![2020-10-23 18 24のイメージ](https://user-images.githubusercontent.com/53253817/96986799-1695f400-155d-11eb-93d4-2aad1ed66e2f.jpeg)

- アクション
    - テンプレートにプログラミングの要素を追加できる
    - 一覧
        - 条件分岐
        - イテレータ(繰り返し処理)
        - 代入
        - インクルード
            - テンプレートを入れ子で扱うことができる
            - djangoのextendでテンプレートを拡張するのと同じ意味
            - アクションをHTML内に入れたら、ParseFilesで複数のHTMLを指定することで実現できる
                - ParseFileの第一引数にメインのベースとなるHTMLを渡す
                    - Executeは第一引数のHTMLを表示するから
            - もっと柔軟な方法がdefineやblockといったタグで実現できるので、詳しくは6章を見直す
        - 変数
        - パイプライン
            - unixのパイプ処理と同じで、左から右に渡していく処理
            - {{12 | prinf %d}}
        - 関数
            - 自作の関数をテンプレートに埋め込むことができる
            - FuncMapで作った関数を登録することで使える
            - パイプラインと連携
                - {{.|myfunc .}}
                    - 代入してきた変数をmyfuncの引数として渡すことができる

- データの記憶方法
    - メモリ内へ保存(プログラムの実行時)
        - 用途
            1. キャッシュやワークスペースとして使われる
        - どの言語でも同じように配列や構造体を定義するとメモリに一時的に記憶する
        - PostgerSQLといったデータベースに何度も同じデータを取りに行くのではなくて、構造体などでメモリ内にキャッシュすることが重要
        - 内部メモリだけではなくて、Redisといった外部メモリを使ってキャッシュすることもできる
    - ファイルシステム上のファイル内に保存
        1. テキスト形式のcsv
            - 用途
                1. ユーザからサーバにデータを移送したいとき
                    - ユーザからの情報が大量で、フォームに入力させるのが大変な時にcsvでアップロードしてもらう
                2. サーバにデータをcsvとして保存しておきたい時
                    - 一つのcsvにデータを書き込んだり読み込んだりというようにデータベースのように使う
                3. キャッシュのバックアップを取りたい時
            - go言語だとFileとかReadを使って読み出す
        2. go言語独自のパッケージgob
            - 用途
                - セッションやショッピングカートや一時的な退避として使うのに便利
    - RDMS(リレーショナルデータベース)へ保存
        - 用途
            - 一般的に永続的にデータを保管するために利用されている
        - データを関係づける方法
            - 1対1
            - 1対多
            - 多対1
            - 多対多
        - 使用方法
            1. .sqlファイルにテーブルを作る構文を書いて、go言語内でSQL構文を使ってデータベースを操作する
            2. サードパーティのライブラリやフレームワークを使用して簡単に操作する
                - 一般的にはこちらの方法で行われる

---

- Webサービスのベースの種類
    - SOAP
        - 複雑で柔軟性がない
        - 堅牢性が高い
    - REST
        - 単純で柔軟性がある
        - 最近はこれをベースにしたWebサービスが多い
        - 一つ一つのリソース(モデルの中のデータ一つ一つ)に固有のURIが振られていて、その固有のURIに対してPOST,GET,PUT,DELETEを使うことで、リソースを変更したり、新規作成したりできる(CRUDを実現)

        ![2020-10-24 5 15のイメージ](https://user-images.githubusercontent.com/53253817/97050244-fcd5ca80-15b7-11eb-85e5-ee9444d48db9.jpeg)

        - ブログを例に例えると
            - GET
                - GETが飛んできたら、全てCRUDのRに該当する処理を担当する
                    - Rはリソースの取得
                - 例
                    - 投稿済みの記事がクリックされたら詳細を表示する
            - POST
                - POSTが飛んできたら、全てCRUDのCに該当する処理を担当する
                    - Cはリソースの作成
                - 例
                    - 新たな記事を作成
            - PUT
                - PUTが飛んできたら、全てCRUDのUに該当する処理を担当する
                    - Uは指定されたURLによるリソースの更新
                - 例
                    - 記事の編集
            - DELETE
                - DELETEが飛んできたら、全てCRUDのDに該当する処理を担当する
                    - Dはリソースの消去
                - 例
                    - 記事の削除
            
            - 色々な処理を作成するには？
                - 例えば、GETは記事の詳細を表示するだけでなくて、「プロフィールの詳細を表示する」という処理もある
                    - このような時にはurlによって処理を変えればいい

        - RESTで複雑な機能を実現する方法
            1. アクションをリソースにかえる
            2. アクションをリソースの属性にする
                - 例えば、ユーザの有効化を実現するにはユーザのアクティベートフラグをtrueにするイメージ

    - XML-RPC

---

- XMLの解析と生成
    - XMLを解析して格納
        - 手順
            1. XMLを格納する構造体を定義
            2. XMLをデコードするデコーダを生成
            3. XMLを順次処理し、デコードして構造体に格納

    - XMLを生成
        - 手順
            1. 構造体を作成してXMLにしたいデータを格納する
            2. XMLに作成データを保存するためのXMLファイルを作成する
            3. 構造体をXMLにエンコードするためのエンコーダを作成する
            4. エンコーダを使って構造体をXMLファイルにエンコードする

- JSONの解析と生成
    - JSONを解析して格納
        - 手順
            1. JSONを格納する構造体を定義
            2. JSONをデコードするデコーダを生成
            3. JSONを順次処理し、デコードして構造体に格納

    - JSONを生成
        - 手順
            1. 構造体を作成してJSONにしたいデータを格納する
            2. JSONに作成データを保存するためのXMLファイルを作成する
            3. 構造体をJSONにエンコードするためのエンコーダを作成する
            4. エンコーダを使って構造体をJSONファイルにエンコードする



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
    - Cookieとは、Webサーバーがクライアント（PC等）に預けておく極小さなファイルのことをさす
    - 初めてそのwebサイトにアクセスするとwebサーバがクライアントに、そのサイト専用のcookieファイルを作成する
    - webサーバからhttpレスポンスに設定してクライアントに送られてくる
        - さらにクライアントからwebサーバにもhttpリクエストを通して送られる
    - cookieがhttpがステートレスであることを克服するために設計された
        - 状態を持つことができるようになった
    - https://www.soumu.go.jp/main_sosiki/joho_tsusin/security_previous/kiso/k01_cookie.htm
    - 使用用途
        1. ショッピングサイトでは一時的に商品を保存する「買い物かご」の役割
        2. Cookie(session)による認証方式
            - クライアントがWebサーバーに初めて接続（Login）した際に、Webサーバーがクライアントに対してCookieファイル（SessionID）を発行し、HTTPレスポンスのヘッダを利用して送ります。その際に発行されたSession情報（SessionID）にはログイン情報が含まれます。
            - 次回以降、クライアントがWebサーバーへアクセスした際は、リクエストヘッダに含まれるCookie（SessionId）をサーバーが参照し、実際にサーバーに保存されているSession情報と合致した際に認証されたとみなされます。
            - https://magazine.techcareer.jp/technology/skill/11273/
        3. フラッシュメッセージを表示する
- フラッシュメッセージとは
    - ユーザのアクションが成功したかどうかを一時的に表示する機能
    - 例えば、お問い合わせフォームで入力された内容が送信されたら「問い合わせは正常に送信されました」といったメッセージを表示する
        - https://www.soumu.go.jp/main_sosiki/joho_tsusin/security_previous/kiso/k01_cookie.htm
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