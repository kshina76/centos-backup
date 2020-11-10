# memo

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


- 従来のWebアプリケーション(サーバサイドレンダリング)
    - サーバ側で生成したHTMLをクライアントに返す
        - djangoでtemplateタグを使って一般的な方法で書かれたものは、この従来の方式になっている
        - 要は、サーバ側で完全なHTMLを生成してクライアントに返す方式
    - スクレイピングするのが簡単
    - SEO的に有利

    ![2020-11-10 23 22のイメージ](https://user-images.githubusercontent.com/53253817/98687119-b6041500-23ac-11eb-9d59-f9734d44d248.jpeg)

- 近年のWebアプリケーション(SPAやクライアントサイドレンダリング)
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

- ブラウザに搭載されている機能

    ![2020-11-11 0 03のイメージ](https://user-images.githubusercontent.com/53253817/98691358-4cd2d080-23b1-11eb-878a-54cb77264630.jpeg)

- HTMLにJSを読み込ませるためのscriptタグはどこに書いてもいいのか!
    - なぜかと言うと、JSファイル内でDOM操作が行われたり、ルーティングが行われているから、要素をjsファイルが自動で見つけてきてくれる

- 参考文献
    - https://qiita.com/Michinosuke/items/a70a349b447f16001f87#step3---webpackを使う
    - https://serip39.hatenablog.com/entry/2020/08/23/225000


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

# go言語のメソッドなどの使い方
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

---

# web開発の進めかた
- 全体像
    - https://qiita.com/oshou/items/6ef304c550260335716b

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

# 新しい技術に触るときの勉強の進め方
1. 前提としてオブジェクト指向の知識はあるものとする
    - 概念の知識がないと、ただ文法を覚えるだけになってしまうため
2. 選定したプログラミング言語の公式チュートリアルをやってみる
3. 選定したプログラミング言語の応用的なチュートリアルをやってみる
    - 例えば、web開発を行うための主要なライブラリなどを学べるチュートリアルとか
4. 何かを自分で作ってみる
    - RSSリーダーを作ると、webアプリケーションに必要な要素が網羅されているらしい
    - ブログを簡単に実装してみる
    - 言語の文法に慣れるためだけなら、データ構造とアルゴリズムを実装するのもいいかも
5. 選定した技術のベストプラクティスを学ぶ