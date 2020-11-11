# ここは書籍memoではないが、有益な情報を置く場所(後々書籍のところに統合してもいい情報置き場)

<br></br>

## SPA(Single Page Application)、クライアントサイドレンダリングのまとめ

- アプリケーションの種類
    - Webアプリ
        - HTML、CSS、JavaScriptで開発されているアプリ
        - クライアントはブラウザ
        - ブラウザを通してHTMLをやりとりすることでユーザにコンテンツを提供する
            - HTMLはブラウザで使うことを目的としている
    - ネイティブアプリ
        - SwiftといったOSに依存した技術を使う
            - JavaScriptで開発をしたかったらReactNativeやVueNativeなどがある
            - バックエンドはもちろん自由
            - HTML、CSSは扱わないが、HTML5を使うとハイブリッドアプリといったネイティブアプリ上でWebアプリを表示できる
        - クライアントはiPhoneやPC
            - クライアントにインストールして扱うアプリケーション
        - デバイス自体が持っているカメラやプッシュ通知を使うことができる
    - ハイブリッドアプリ(WebViewアプリ)
        - Webアプリと同じ技術を使って開発できる
        - クライアントはiPhoneやPC
        - ネイティブアプリ上でWebアプリを表示するタイプのアプリ
        - https://tonari-it.com/monaca-hybrid-appli-development/

<br></br>

- SSR(サーバサイドレンダリング)とCSR(クライアントサイドレンダリング)の違いの概要
    - 要は、完成されたHTMLが返されるのがSSRで、未完成のHTML(レンダリングされていない)が返されるのがCSR

    ![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-227791-9dd75e20-2a0c-eee9-0a5c-ab5f84f6eab4](https://user-images.githubusercontent.com/53253817/98690091-eb5e3200-23af-11eb-9d89-bba5889f237a.jpeg)


- 従来のWebアプリケーション(クライアントサイドレンダリング)
    - ブラウザからリクエストされると、サーバーは、JS のビルドされたファイルと必要最小限のHTML要素しか含まれないHTMLファイルを返却する。HTMLファイルの中身はほぼないので、初期表示は何も表示されない。それから、ブラウザ上でAPIなどを使い、初期データを取得して、HTML 要素をレンダリングする。
    
    - 実現方法1(S3に置いて実現)
        1. AWS-S3にjs(reactとか),css,htmlを置く
            - webpackで複数のjavascriptを一つにまとめる
            - 同時にbabelを使ってトランスコンパイルをしておく(webpackを使うと勝手にされる？)
        2. バックエンドはAPIとして構築する
        3. ブラウザからS3にHTTPリクエストが来る
        4. 指定されたHTMLファイルがレスポンスとしてブラウザに返ってくる
        5. HTMLファイルのレンダリングが開始する
            - HTMLに書かれているjsファイルとcssを取得するために、自動的にリクエストがS3に飛ばされる
            - 返ってきたjsやcssがブラウザ上で実行される。jsのなかにバックエンドのAPIにリクエストする文が書かれていたらリクエストをバックエンドのサーバに送る
            - 以下繰り返し
    
    - 実現方法2(node.jsやexpressでwebサーバを構築) <- これが普通のやり方
        1. Webサーバ(node.js)にHTML,CSS,JS(Reactなど)を置く
            - フロントエンド
        2. APIサーバはGoとかPython(Django)で提供する
            - バックエンド
        3. ブラウザからWebサーバにリクエストが来る
        4. Webサーバは未完成のHTMLを送る
        5. あとは1と同じ

        ![2020-11-10 23 19のイメージ](https://user-images.githubusercontent.com/53253817/98685832-36297b00-23ab-11eb-8abd-12e091ffe24f.jpeg)
        
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>test</title>
        </head>
        <body>
        <div id="content"></div>
        <script src="https://unpkg.com/react@15/dist/react.js"></script>
        <script src="https://unpkg.com/react-dom@15/dist/react-dom.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/redux/3.6.0/redux.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/react-redux/5.0.2/react-redux.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.19.0/babel.min.js"></script>
        <script type="text/babel">
            // コンポーネントの定義
            //ここは本来、jsファイルとして他で定義して、HTMLから呼び出すようにする
            var helloReact = <div>Hello! React!</div>;
            var content = document.getElementById('content');
            ReactDOM.render(helloReact, content);
        </script>
        </body>
        </html>
        ```

    - 実現例
        - React(S3に置く？)+Django(RestAPI-Framework)
        - Vue(S3に置く？)+Django(RestAPI-Framework)
        - vanilla-js(S3に置く？)+go(API)
        - etc...
    - ブラウザで動作するのはJavaScriptのみなので、フロントエンドにJavaScriptベースのフレームワークを使う
        - Djangoだけで書かれているものはブラウザで動作しないので、従来のアプリケーションに分類される
    - HTMLファイル内のscriptがクライアントサイドレンダリングを実現している
    - リアルタイム更新のサイトとかにも向いている方式
    - このようなサイトをスクレイピングするのには工夫が必要
        - https://gammasoft.jp/blog/how-to-download-web-page-created-javascript/

    ![2020-11-10 15 26のイメージ](https://user-images.githubusercontent.com/53253817/98635931-2a1cc980-2369-11eb-9c6f-14e88a4dc78f.jpeg)

- 近年のWebアプリケーション(サーバサイドレンダリング)
    - サーバ側で生成したHTMLをクライアントに返す
        - djangoでtemplateタグを使って一般的な方法で書かれたものは、この従来の方式になっている
        - 要は、サーバ側で完全なHTMLを生成してクライアントに返す方式
    - スクレイピングするのが簡単
    - SEO的に有利

    ![2020-11-10 23 22のイメージ](https://user-images.githubusercontent.com/53253817/98687119-b6041500-23ac-11eb-9d59-f9734d44d248.jpeg)

- 流行りのWebアプリケーションSPA(Single Page Application)
    - 最初の読み込みをサーバサードレンダリング(クライアントサイドでもどっちでもいいのかな？)で行って、そのあとは差分だけをjsonで受け取って、クライアントサイドレンダリングを行う方式(多分そうだと思う)
    - ReactだとReactJSというモジュールが差分レンダリングを行える
    - AJAXという技術がSPAを可能にしているのかな？？
    
- ブラウザに搭載されている機能

    ![2020-11-11 0 03のイメージ](https://user-images.githubusercontent.com/53253817/98691358-4cd2d080-23b1-11eb-878a-54cb77264630.jpeg)

- HTMLにJSを読み込ませるためのscriptタグはどこに書いてもいいのか!
    - なぜかと言うと、JSファイル内でDOM操作が行われたり、ルーティングが行われているから、要素をjsファイルが自動で見つけてきてくれる

- 参考文献
    - https://qiita.com/Michinosuke/items/a70a349b447f16001f87#step3---webpackを使う
    - https://serip39.hatenablog.com/entry/2020/08/23/225000
    - https://qiita.com/amakawa_/items/e7d0720e1ab8632769bf
    - 


<br></br>

- Webアプリのフロントエンド開発がHTML,CSS,JavaScriptの理由
    - ブラウザで動作するのはJavaScriptのみだから

- WebアプリでクライアントサイドレンダリングをPythonやPHPで実現する方法
    - 手順
        1. PythonをHTMLに埋め込む
        2. 埋め込まれたPythonをJavaScriptに変換
        3. ブラウザでJavaScriptを含んだHTMLが実行される
    - 実現するためのライブラリ
        - Brython(Python)
        - Uniter(PHP)
        - GopherJS(Go)
---

# web開発の進めかた
- 全体像
    - https://qiita.com/oshou/items/6ef304c550260335716b
    - https://note.com/promitsu/n/n463792216407

- 設計、デザイン

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
    3. バックエンドのロジックを考えていく
        - MVCの型に当てはめながらコーディングを進めるとスラスラ書ける

    - 参考文献
        - https://note.com/hi_roki/n/n4e889089c4d0
        - https://qiita.com/himatani/items/3b8301da2e889e962e5e
        - https://qiita.com/s_emoto/items/975cc38a3e0de462966a

---

## マルチスレッド、並列処理、並行処理
- スレッドとプロセスの違い
    - プロセスの中に複数のスレッドがある

![2020-11-09 21 50のイメージ](https://user-images.githubusercontent.com/53253817/98543325-aa91ea80-22d5-11eb-9fb8-73159c97ee95.jpeg)

- マルチスレッドとは
    - マルチスレッドはOSの機能で複数のスレッド同時に(のように)処理すること
    - マルチスレッドを用いた並行処理
        - CPUが一度に実行できるスレッドは一つだけど、CPUは一つのスレッドを一気に実行しないで、複数スレッドをそれぞれ少しづつ実行すること
        - これによってあたかもCPUが複数のスレッドを同時に実行しているように見せる
    - マルチスレッドを用いた並列処理
        - ある1つの時点で、実際に、物理的に、複数の仕事をしていること
        - これは、速くすることが目的
        - CPUのcore数が2つ以上の場合に可能


- 並行処理と並列処理の違い
    - 並行処理
        - ある1つの時点では、1つの仕事しかしていないが、複数の仕事間を切り替えることによって、同時にやっているように見えること。
        - これは、速くするとかいうより、単純に同時にやることあるいは他を待たせないことが目的
    - 並列処理
        - ある1つの時点で、実際に、物理的に、複数の仕事をしていること
        - A、B、Cの処理をよーいどん、で3つ同時にスタートする
        - これは、速くすることが目的
        - CPUのcore数が2つ以上の場合に可能
        - 複数のプロセス上で、複数のスレッドが立ち上がる
    
    ![https---qiita-image-store s3 amazonaws com-0-106693-ee7e9cb3-53b9-9b88-d335-1a71be17f0ee](https://user-images.githubusercontent.com/53253817/98650360-1f1f6480-237c-11eb-917d-d8aa37bdf778.png)

- 並行/並列処理のパターン

    ![2020-11-10 18 04のイメージ](https://user-images.githubusercontent.com/53253817/98653013-ceaa0600-237f-11eb-83ad-2c0ddebea529.jpeg)


- 同期処理とは
    - 書いた順番に実行されていく
    - 重たい処理が間にあると、そこで大きな待ち時間が生まれる

- 非同期処理とは
    - 並行処理のこと
    - 時間がかかる処理の完了を待たずに次の処理を進め、同時に複数の処理を進めることを非同期処理という
    - 例えば、外部のサーバと通信する関数を呼んだあと、レスポンスが返るまでに一旦関数から抜けて別の処理を進めて レスポンスを受け取り次第、呼び出し元に値を返す処理など
    - プログラムは基本的には逐次実行といって、一つの処理が終わったら次の処理を行うようにしているが、それだと非効率な場合があるから非同期処理という仕組みがある
    - コールバック関数
        - Aという関数が完了次第、実行したい関数(function)を引数として渡して実行させるもの
        - JavaScriptでは、上述のコールバック関数で処理順をコントロールできるが、ネストが深くなる

- プログラミングにおける並列/並行処理
    - core数が一つの時は並行処理になって、core数が複数の時は並列処理になる
        - 設定で扱うcore数の上限をあげると並列処理になる
    - go言語に関してはruntime パッケージの関数 GOMAXPROCS で指定するか、環境変数 GOMAXPROCS で指定するとgoroutineが並列で動く

- JavaScriptでの非同期処理
    - https://qiita.com/kiyodori/items/da434d169755cbb20447

- goが他の非同期プログラミングよりも優れている理由
    - https://qiita.com/methane/items/5ad7c092c0d426db4ab5

- 参考文献
    - https://qiita.com/Takagi_/items/84b4a2184f42ee77867c
    - https://qiita.com/Kohei909Otsuka/items/26be74de803d195b37bd
    - https://ascii.jp/elem/000/001/475/1475360/
    - http://www.nct9.ne.jp/m_hiroi/golang/abcgo14.html

<br></br>

---

## 用語とか
- 疎結合と密結合なプログラムとは

![2020-11-09 14 16のイメージ](https://user-images.githubusercontent.com/53253817/98502819-57e50e00-2296-11eb-822e-63333d8c07e0.jpeg)

<br></br>

- コンパイラ方式とインタプリタ方式と中間コード方式の違い
    - コンパイラ方式
        - メリデメ
            - 実行速度が速い
            - 実行するのに手間がかかる
            - プラットフォームが異なると実行できない(機械語がマシンによって異なるから)
        - 用途
            - 政府や銀行のシステム
            - 企業の基幹システム
    - インタプリタ方式
        - メリデメ
            - 異なるプラットフォーム(異なるOSなど)でもファイルを配布すればすぐに実行できる
            - 実行速度が遅い
        - 用途
            - インターネットを通じて、様々な種類のマシンにダウンロードされて動くソフトウェア
    - 中間コード方式
        - メリデメ
            - コンパイラ方式とインタプリタ方式のいいとこ取り

![2020-11-09 21 39のイメージ](https://user-images.githubusercontent.com/53253817/98542332-14a99000-22d4-11eb-9db5-e90fc39815cf.jpeg)

![2020-11-09 21 41のイメージ](https://user-images.githubusercontent.com/53253817/98542519-681bde00-22d4-11eb-9d9c-1ae898bad5fe.jpeg)


<br></br>

- プログラムのメモリ領域の種類
    - 静的領域はプログラムの開始に確保されて終了まで配置が固定される
    - プログラムの実行中にアプリケーションから必要なサイズを要求することで割り当てを行い、不要になれば元に戻す
    - スタック領域は一つのサブルーチン呼び出しが一つのスレッド

![2020-11-09 22 05のイメージ](https://user-images.githubusercontent.com/53253817/98544681-ae267100-22d7-11eb-9c61-1cd65a2d8081.jpeg)

- デザインパターンとは
    - 優れた設計のアイデアを後から再利用できるように、名前をつけて文書化したもの

<br></br>