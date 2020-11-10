# API

## APIの基本や設計について
- APIとは
    - HTTP(Webの仕組み)を用いてプログラムの呼び出しを実現している
        - 普通だったら関数やメソッドはローカルのコンピュータ内で連携し合うが、リモートの関数やメソッドを実行して結果を得る感じ
        - 厳密にはHTTPを使わないものもあるが、最近はほとんどがHTTPを使うものなのでこのように書いた
    - 実行したプログラムと違うプロセスのサブルーチンを呼び出すための機能みたいな感じ


- 一般的なプログラムとAPIを利用したプログラムの違い

    ![2020-11-10 21 42のイメージ](https://user-images.githubusercontent.com/53253817/98675485-acbf7c00-239d-11eb-8e88-f899fa08551f.jpeg)

- APIの種類(大枠では2種類)
    - RPC
        - xmlRPC
        - SOAP(xmlRPCを拡張したもの)
        - json-rpc
        - Mprpc
        - gRPC
        - etc...
    - REST

    ![2020-11-10 21 34のイメージ](https://user-images.githubusercontent.com/53253817/98674743-99f87780-239c-11eb-80a2-7fd5902f1be4.jpeg)

- RESTとRPCの違い
    - RESTは制約が強いAPI
    - RPCは制約が少なく柔軟性のあるAPI
        - クライアント側がメソッドを実行するのと同じような感覚で、サーバーサイドのメソッドを実行できるようになるイメージ
    - 返すデータ型はHTMLでもjsonでもXMLなど色々。あくまでも設計の思想の違い程度に思っておけばいい
    - json-rpcをRESTで縛ると、いろいろなところで書かれているREST APIを指すのかな？

- gRPCとは
    - gRPCは異なるウェブサービス間でRPCを実現するフレームワークである
    - HTTP/2を使った高速な通信が使えるようになる
    - REST APIのようなURLとJSONベースのやり取りではなく、メソッド呼び出しのような感覚でバックエンドを呼び出せる
    - ブラウザから直接は使えないので、間にReverseProxy（envoy等）を建てる必要がある

- gRPCがjsonを返すようにするやり方
    - gRPCはprotocol-bufferというバイナリ形式のデータを返す
        - 読みにくいからjsonを返して欲しい場面がある
    - grpc-gatewayを使う

    ![2020-11-10 21 55のイメージ](https://user-images.githubusercontent.com/53253817/98676850-7e42a080-239f-11eb-9ef8-396bd3c1a908.jpeg)
    

- 参考文献
    - https://qiita.com/ara_tack/items/f1252d335a0f18f96a4c
    - https://qiita.com/jumpyoshim/items/a027f2f18f926d975683
    - http://portaltan.hatenablog.com/entry/2015/12/24/112253
    - https://qiita.com/disc99/items/cfca50a32240284578bb
    - https://hisa-tech.site/researching-about-grpc/

<br></br>

- APIの用途
    - 公開されていないAPI
        1. スマホからサーバと通信をする場合、WebAPIを利用するのが一般的
            - スマホアプリのバックエンドとしてリモートのサーバで実装した機能を使うのにWebAPIを使う
                - フロントエンドがバックエンドにリクエストするというような使い方
                - バックエンドがAPIを提供してフロントエンドがそのAPIを叩くとjsonなどといった形でデータが返ってくる
                - このようなAPIは一般公開されることは少ない
            - 例
                - ReactNative+Go
                - VueNative+GO
                - Swift+Go
        2. Webアプリ開発でフロントエンドとバックエンドで違うフレームワークを使用する時
            - GoでAPIを提供して、ReactからそのAPIを叩くことでjsonなどといった形でデータが返ってくる
            - 例えば、フロントエンドにReactを使って、バックエンドにDjangoやgoを使うといった場合など
            - 例
                - React+Django(Rest-Framework)
                - Vue+Django(Rest-Framework)
                - React+Express(Node.js)
                - vanilla-js+go
                - etc...
    - 公開されるAPI
        - 自分が開発しているサイトにすでに開発されている機能を搭載したい場合に使われる
            - 自分では開発するのは難しい機能などを利用できるからすごい便利
        - GoogleのTTSや画像認識のAPIなどがこれに当たる

<br></br>

- APIのURL設計
    - パラメータを入れる場所
        1. クエリストリングに含める
            - URL内にクエリ文字列を入れて渡す
        2. リクエストボディに含める
            - リクエストボディにjsonの形で。アクセスする時はcurlコマンドの場合オプションdでjsonで引数を渡せる。
        3. パスに含める
            - パスの名前で一意に定めている
    - URL設計に関してめっちゃわかりやすい 。RESTに沿ったAPIというものがわかる
        - https://qiita.com/sakuraya/items/6f1030279a747bcce648

<br></br>

- webアプリを作るときもwebapiを作るときもサーバ側のバックエンドはほぼ同じ
    - 返すのがhtmlかjsonかの違いだけ。httpレスポンスボディにhtmlが入っていたらいつものwebアプリ(webサイト)、jsonが入っていたらwebapiって感じ。
    - 例えばgo言語で要求されたurlに対するhtmlを返すプログラムではResponseWriterにhtmlを書き込んでListenAndServeでリッスンしたところにリクエストを送ると、htmlが返ってくるし、書き込むファイルをjsonに変えるとjsonが返ってくるという感じ
        - webapiを理解する時に、webアプリはサイトを返してくれるものだという意識だと理解できないかも。あくまでもhttpレスポンス(文字列)を返してくれるに過ぎないという理解をしておく。クライアントがブラウザの場合はhtmlを整形して綺麗に表示してくれるが、それはブラウザの機能。pythonならurllibまたはrequestsライブラリでurlとパラメータを指定して叩けば、json型やhtmlがそのまま返ってくる。パラメータはクエリ文字列としてURLに書いたりで送れる(仕様にそってやる)curlでurlとパラメータを指定することで取得できるのと同じ

<br></br>

- Webapiについてみた方がいいところ
    - https://qiita.com/kawasukeeee/items/70403129f5a5338cd4ad
    - https://qiita.com/y-some/items/7e05540d7563f7c1c101

<br></br>

- マイクロサービス
    - システムを複数のサービスに分割して、サービスの集合体としてシステムを構築すること
    - それぞれのサービスはHTTPやMessagingなどで繋がれる
        - 多分それぞれのサービスをAPI化して連携するとかかな？
        - https://html5experts.jp/miyuki-baba/14776/

<br></br>

- RESTとは
    - RESTはAPIの定義に使用されるアーキテクチャスタイルのこと
    - RESTの定義
        1. ステートレスなクライアント/サーバプロトコル
            - Cookieやセッションは情報を保持することからステートフルなので、RESTにはならない
        2. すべてのリソースに適用できる「よく定義された操作」のセット
        3. リソースを一意に識別する「汎用的な構文」
        4. アプリケーションの情報と状態遷移の両方を扱える「ハイパーメディアの使用」
    - https://qiita.com/sakuraya/items/6f1030279a747bcce648

- 参考文献
    - https://qiita.com/y-some/items/7e05540d7563f7c1c101
    - https://www.setouchino.cloud/blogs/81
    - https://www.ogis-ri.co.jp/pickup/renkei/docs/20170911_APIEconomy_Session2.pdf

- webapi設計において絶対見た方がいい
    - https://qiita.com/mserizawa/items/b833e407d89abd21ee72
    - https://qiita.com/howdy39/items/3b2b14ce73ec44c54f7b

---

## API実践

- 「Go言語 + gorilla/mux router」でREST APIサーバを作成
    - Go言語ならgRPCのような気がするが、基本の勉強としてREST(フォーマットはjson)で作成している
    - https://qiita.com/stranger1989/items/7d95778d26d34fd1ddef

- ReactとDjango(REST API Framework)を連携
    - https://www.kthksgy.com/web/make-react-django-blog2/
    - https://www.kthksgy.com/web/make-react-django-blog3/

- 「Vue.js + Go言語 + Firebase」でFrontend & Backend API 両方で認証するセキュアなSPA開発
    - https://qiita.com/po3rin/items/d3e016d01162e9d9de80

- 「vanilla-js + Node.js + Go言語(API)」でSPA
    - vanilla-jsではjqueryを使わずにDOM操作
        - https://wemo.tech/2101#index_id65
        - https://qiita.com/shshimamo/items/ba3a57a81d9780030969
    - Node.jsはHTML,CSS,JSを配信（レンダリングはブラウザで行う）
    - Go言語はAPIとしての役割
    - 例(以下にAPIを搭載して拡張するのでもいいかも)
        - https://vanillawebprojects.com
        - https://github.com/bradtraversy/vanillawebprojects
