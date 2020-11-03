# API
- APIとは
    - HTTP(Webの仕組み)を用いてプログラムの呼び出しを実現している
        - 普通だったら関数やメソッドはローカルのコンピュータ内で連携し合うが、リモートの関数やメソッドを実行して結果を得る感じ

- APIの用途
    - 公開されていないAPI
        - スマホからサーバと通信をする場合、WebAPIを利用するのが一般的
            - スマホアプリのバックエンドとしてリモートのサーバで実装した機能を使うのにWebAPIを使う
                - フロントエンドがバックエンドにリクエストするというような使い方
                - このようなAPIは一般公開されることは少ない
    - 公開されるAPI
        - 自分が開発しているサイトにすでに開発されている機能を搭載したい場合に使われる
            - 自分では開発するのは難しい機能などを利用できるからすごい便利
        - GoogleのTTSや画像認識のAPIなどがこれに当たる

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

- webアプリを作るときもwebapiを作るときもサーバ側のバックエンドはほぼ同じ
    - 返すのがhtmlかjsonかの違いだけ。httpレスポンスボディにhtmlが入っていたらいつものwebアプリ(webサイト)、jsonが入っていたらwebapiって感じ。
    - 例えばgo言語で要求されたurlに対するhtmlを返すプログラムではResponseWriterにhtmlを書き込んでListenAndServeでリッスンしたところにリクエストを送ると、htmlが返ってくるし、書き込むファイルをjsonに変えるとjsonが返ってくるという感じ
        - webapiを理解する時に、webアプリはサイトを返してくれるものだという意識だと理解できないかも。あくまでもhttpレスポンス(文字列)を返してくれるに過ぎないという理解をしておく。クライアントがブラウザの場合はhtmlを整形して綺麗に表示してくれるが、それはブラウザの機能。pythonならurllibまたはrequestsライブラリでurlとパラメータを指定して叩けば、json型やhtmlがそのまま返ってくる。パラメータはクエリ文字列としてURLに書いたりで送れる(仕様にそってやる)curlでurlとパラメータを指定することで取得できるのと同じ

- Webapiについてみた方がいいところ
    - https://qiita.com/kawasukeeee/items/70403129f5a5338cd4ad
    - https://qiita.com/y-some/items/7e05540d7563f7c1c101


- マイクロサービス
    - システムを複数のサービスに分割して、サービスの集合体としてシステムを構築すること
    - それぞれのサービスはHTTPやMessagingなどで繋がれる
        - 多分それぞれのサービスをAPI化して連携するとかかな？
        - https://html5experts.jp/miyuki-baba/14776/

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