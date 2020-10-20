# 1日で基本が身に付く Docker Kubernetes 書籍memo
- 体系化されたdockerコマンド
    - 以下のようにコマンドが区別されているからわかりやすい
    - docker <操作グループ> <操作種類>

```
                サブコマンド      操作       オプション

docker -------- help
         |
         |----- container ----- run ----- --help
         |                  |-- stop  |-- -d
         |                  |-- rm    |-- -it(-i + -t)
         |
         |----- image --------- pull
                            |-- rm

```

<br></br>

- dockerコンテナは停止した時に破棄するべき
    - ライフサイクル的には削除するべきらしい
        - 停止しても状態を保持する必要があるなら、ボリューム機能でデータを永続化しつつ、コンテナが不要になれば破棄して新規作成を行うことが望ましい
    - runコマンド時にrmオプションをつけると、停止したときに削除する

<br></br>

- dockerの使い所
    1. ホストマシンに依存しないで、色々な環境でインフラを構築できる
    2. インフラをコード化できる
    3. アプリを小分けで開発できる

<br></br>

- dockerで守るべきこと
    1. dockerfile内で環境依存してはいけない
        - 例えば、dockerコンテナから他のサービスのipを直接書き込んでしまうと、環境が変わった時にアクセスできなくなってしまう
    2. dockerfileを用いて独自イメージを作成する
        - 例えばnginxに独自の設定を入れたい場合は、dockerfile内でnginxの公式からpullしてきて、それに変更を加えて作成する
    3. dockerfileがなくならないようにgitで管理する
    4. 一つのコンテナに少ないプロセス
        - 小さなコンテナをメンテナンスして完璧にして、小さなコンテナ同士を連携させて一つの巨大なインフラを作る

<br></br>

- terraformとansibleとdockerの使い分け
    - クラウドでのベストプラクティス
        - terraform+docker
            - terraformでec2やlambdaといったインフラの構築
            - dockerでアプリケーションに関する設定(nginxやpythonk環境など)
            - terraform+ansibleでも実現できるが、dockerを使うならansibleは使わないかも
            - https://y-ohgi.com/introduction-terraform/first/about/
    - ベアメタルやVMや特にオンプレミスでのベストプラクティス
        - ansible+docker(要調査)
            - ansibleでdockerホストの作成やファイアーウォールやosの環境の設定
            - dockerでnginxやpython環境の設定
    - terraformとansibleは互いに補完し合う関係なので、一緒に使うのがベストプラクティス
        - terraformはawsのlambdaやec2やs3といったインフラを構築するのに使う
        - ansibleはインフラに載せるミドルウェア(nginxとかpython環境とかdockerとか)の構築と設定をするのに使う
            - ec2にdockerホストを乗せたりといったこと。ec2の立ち上げはterraformが行う
- 環境別のインフラ構築
    - 開発環境(ローカル開発環境)
        - 個人個人の手元にあるPCの環境のこと
        - vargrant(virtual box)またはdockerでササッと構築
            - python環境とか
    - 検証環境(テスト環境)
        - 個人の環境またはテスト担当者がunittestなどでテストを行うことかな？？
        - 特に新しくインフラを構築する必要はないかも
    - ステージング環境
        - webサーバなどといったインフラの設定を本番と全く同じ状態で構築する環境
        - クラウドを使うならAWSでterraformとdockerを使うなどして完璧に構築する
    - 本番環境
        - 実際に一般ユーザに使ってもらうときのインフラのこと

<br></br>

- dockerネットワークについて
    - docker network ls というコマンドdockerネットワークの構成を確認できる
    - 基本的にbridgeを利用する
- bridge
    - ホストとは異なる内部ネットワークを構築する
    - docker0がNATの役割を果たして、ipマスカレード機能を使ってパブリックipとプライベートipを変換して外部と通信する
    ![https---qiita-image-store s3 amazonaws com-0-70152-0208a1da-2476-59b6-97e3-c8ec39fcc8f9](https://user-images.githubusercontent.com/53253817/96432026-4a140e00-123f-11eb-9ec2-771f992228bc.png)
- host
    - ホストとネットワークを共有する
    - 共有しているのでホストが80番ポートを使っていたらdocker0は使えないということになる
    ![https---qiita-image-store s3 amazonaws com-0-70152-f7d14c5d-9023-f55d-3b36-23d8a1b98df7](https://user-images.githubusercontent.com/53253817/96436815-06ba9f00-1241-11eb-8f11-1902d2d20860.png)
- none
    - 外部とのネットワークの繋がりは無いし、ホストのネットワークとの繋がりもない
    ![https---qiita-image-store s3 amazonaws com-0-70152-0783261c-c34e-9192-3dd1-4ebb7cb5dff9](https://user-images.githubusercontent.com/53253817/96437792-46818680-1241-11eb-9b1d-1ae803a67f7d.png)

<br></br>

- dockerコンテナのポートフォワードは、必要なコンテナのみに行う
    - データベースなどが入ったコンテナのポートを開けてしまうと、外部からの攻撃リスクがあるから
        - 攻撃されたくないデータベースなどはAWS側でプライベートサブネットにおけば問題ないから、ポートフォワードして大丈夫

<br></br>

- コンテナ間の名前解決
    - コンテナ間で連携する際にIPアドレスを指定して通信することはしない。その代わりにコンテナ名で通信する
        - コンテナ起動時にIPアドレスが決まるため、一々環境変数に設定しなければいけないから
        - 複数のコンテナを連携する際には、新しくbridgeを指定してネットワークを作って、そこにコンテナをつなげるようにする
            - DNSの名前解決が有効になるから
            - デフォルトのbridgeだと名前解決機能がない

<br></br>

- dockerのイメージを作成する際の注意点
    1. 開発するアプリはファイルにデータを書き出さない(データを永続化する場合を除く)
    2. yumなどでインストールしたアプリはログを標準出力と標準エラー出力に変更する
    3. イメージ作成に必要となった中間ファイル(yumのキャッシュなど)は消す

<br></br>

- データ永続化の手法
    1. そもそも大事なデータの管理にコンテナを使わない
        - DBだけ普通のVMを使うとか
    2. コンテナとして動くOSが外部ストレージにデータを直接置く
        - NFSやSambaやAWS S3とか
    3. dockerのデータ永続化手法を使う
        - Bind
            - ホスト上の任意ディレクトリを指定して、それをコンテナ内の任意のディレクトリにマウントする
            - ホストからそのディレクトリにファイルを入れるとコンテナ内で反映されるし、その逆も同じ
        - Volume
            - dockerエンジンが管理する特別なパスにボリュームがマウントされる
            - NFSやS3といった外部領域を指定することもできる
        - Bindはホスト上で永続化したデータを開発者がいじる可能性がある場合に使う
        - Volumeはホスト上で永続化したデータをいじらない場合に使う
    4. 永続化とは関係ないが、tmpfsを作業用ボリュームとして使う
        - tmpfsはramディスクとして動作するから高速でI/O処理などができる
    - 永続化するべきかしないべきかは、重要なデータかどうかで決めればいいと思う

<br></br>

- データのバックアップとリストア
    1. 永続化したボリューム領域ごとtar、zipでまとめる
    2. アプリケーションのバックアップ機能を使う
        - MySQLの機能とか

<br></br>

- dockerイメージの開発方法
    1. 公式からイメージをpullしてきて、端末でpython環境などを整えてcommitする
        - これは、dockerの仕組みを知るにはいいと思うが、本番の開発では使わない
    2. Dockerfileを利用したイメージ開発
        - こちらが現場で使われる方法

<br></br>

- 差分キャッシュを使った時短ビルド
    - すでに作成されたイメージに手を加えて、サイドビルドすること
    - dockerのイメージに手を加えて再度ビルドする場合は、ビルドがすでにされている部分は再度されないで、差分の部分だけビルドされる
    - pythonのインストールやパッケージのインストールといった変更する回数が少ないものはDockerfileの前半に記述して、アプリケーションのソースコードのコピーといった高頻度で変更する部分を後半に記述することで、高速ビルドを実現できる
        - もし、前半部分に記述してしまうと、変更がstepから先は全く同じ処理であっても再度ビルドされるので、無駄な時間になってしまう

<br></br>

- ディレクトリコピーと.dockerignore
    - COPY命令でディレクトリごとコピーしたいときに、コンテナに含めたくないファイルは.dockerignoreに記述する
    - Dockerfileが存在するディレクトリに置いておく

<br></br>

- マルチステージビルド(ステージングビルド)
    - ビルド環境と実行環境を分けてコンテナサイズを小さくする
    - ソースコードをビルドする環境とビルドし終わったバイナリファイルを実行する環境に分けてDockerfileを書いている
        - ビルドし終わったらバイナリファイルを実行環境にCOPYすることで、実行環境ではビルド環境分のイメージがいらないことから、コンテナサイズが小さくなる
    - as builderで踏み台のイメージにbuilderという名前をつけている

```
From golang:1.13.4-alpine3.10 as builder
WORKDIR /src
COPY ./main.go /src
RUN go build -o start_appserver main.go

From alpine:3.10.3
COPY --from=builder /src/start_appserver /bin/start_appserver
CMD ["/bin/start_appserver"]
```

<br></br>

- Dockerfileを作るコツ
    - 先に手動で手順を確認する
        - Dockerfileを一行一行追加して実行してというのを繰り返すといい
        - 例えば一行目で公式イメージをpullしたら、コンテナを作成して入って、自分が作りたい構成を手動で作って見てから必要な手順をDockerfileに落とし込むということをする
    - 余分な差分イメージを減らす
        - 例えば、パッケージインストールを一行で全て終わらせるとか

        ```
        RUN yum update ¥
            && yum install -y ¥
                package-bar ¥
                package-baz ¥
                package-foo ¥
            && rm -rf /var/cache/yum/* ¥
            && yum clean all
        ```

<br></br>

- 

# docker
## コマンド集
- コンテナ起動
    - docker container run nginx
        - --it bash
            - 端末操作可能
        - -d
            - detachの略で、バックグラウンド起動する
        - --rm
            - コンテナが停止された時にコンテナを削除する
            - --nameと併用すると便利で、停止した後に同じコンテナを起動しても名前の重複がしなくなる
        - --name <コンテナ名>
            - コンテナに名前をつける
        - --network <ネットワーク名>
            - 任意のdockerネットワークに接続する
            - 

<br></br>

- バックグラウンドで起動中のコンテナ内でコマンドを実行
    - デバッグとか、イメージに手を加えたい時とか
    - docker container exec nginx_container <コマンド>
        - -c
            - リダイレクトやパイプ処理を行いたい時に使う
            - docker container exec nginx_container bash -c "echo 'hello docker' > ./hello.txt"
                - bash -c "echo 'hello docker' > ./hello.txt" をexecで実行する
                - ちなみに、リダイレクトは出力の向かう先を変更する処理のこと

<br></br>

- コンテナの一覧を表示する
    - docker container ls -a
        - -a
            - 停止中のコンテナも含めて全て表示する

<br></br>

- コンテナの詳細情報を表示する
    - ボリュームとかネットワーク周りの設定を見ることができる
    - docker container inspect <コンテナ名>

<br></br>

- コンテナのログを確認
    - nginxの標準出力エラーとかを見たい時に使う
    - docker container logs <コンテナ名>
        - -f
            - ログをリアルタイムで表示し続ける(便利)
        - -t
            - タイムスタンプ付きでログを表示する

<br></br>

- コンテナの統計情報を確認
    - cpu使用率やプロセス数など
    - docker container stats --no-stream
        - -no-stream
            - コマンド結果をすぐに返す。statsは時々刻々と変化する内容なので、表示され続けてしまうことを防ぐ

<br></br>

- 出力フォーマットを指定
    - docker container ls --format='table {{.ID}}¥t{{.Names}}¥t{{.Ports}}'
        - --format
            - 出力のフォーマットを指定することができる（出力が長すぎるからかな？）
            - table指定の後に、波カッコ2つの間に表示したい要素を入れたものをタブ区切り(¥t)で並べる

<br></br>

- コンテナの起動と停止
    - dockerのライフサイクルに反するものなので多用する運用はよくない
    - docker container start <コンテナ名>
    - docker container stop <コンテナ名>
    - docker container stop $(docker container ls -q)
        - 起動しているコンテナを全停止

<br></br>

- コンテナの削除
    - docker container prune -f
        - 起動していないコンテナを全削除
    - docker container rm <コンテナ名>

<br></br>

- 公式イメージの検索
    - docker search <名称>
        - 名称にpythonと入力したらpythonに関するイメージがDockerHubから検索される
    - docker search -f "is-official=true" -f "stars=50" python
        - -f
            - 検索結果にフィルターをかける
            - is-official=true で公式かどうか
            - stars=50 でスター数が50個以上かどうか

<br></br>

- イメージのタグを検索
    - curlコマンドで取得する

<br></br>

- 公式イメージがコンテナ起動時に呼び出すコマンドを確認
    - docker image inspect <イメージ名>
    - Cmdのところで呼び出されるコマンドがわかる

<br></br>

- dockerネットワークの構成を確認する
    - docker network ls
    - bridgeとhostとnoneというネットワークのipなどが表示されると思う

<br></br>

- dockerネットワークを作成する
    - docker network create -d <ドライバ名> <ネットワーク名>
        - -d
            - 作成するネットワークドライバを選択できる
            - 例えば、NAT用のネットワークを作成したかったらbridgeを選択する
            - 複数のコンテナを連携する際には、新しくbridgeを指定してネットワークを作って、そこにコンテナをつなげるようにする
                - DNSの名前解決が有効になるから

<br></br>

- dockerfileからイメージを作る
    - docker image build -t <イメージ名>:<タグ> <dockerfileのパス>

<br></br>

- dockerでは軽量なlinuxが好まれる
    - Alpine Linuxがよく使われる
    - サイズが問題になる場合や、ビルドを軽量化したい場合など
    - しかし、実際にはCentosやUbuntuを利用して開発効率を高めた方がいい。
        - サイズはそんなに問題にならないことがほとんどだから

<br></br>

- 

## Dockerfileの命令集

- From
    - 利用するイメージの宣言
    - From python:3.7.5-slim
- Label
    - イメージに追加する情報、authorとか
    - Label author="myname@gmail.com"
- RUN
    - コンテナ起動前に発行するコマンド
    - RUN pip install django==2.0
- COPY
    - ファイルのコピー
    - COPY ./server.py /server.py
- ENV
    - 環境変数のデフォルトの設定
    - ENV PORT 80
- CMD
    - コンテナ起動後に発行されるコマンド
    - CMD ["python", "-u", "/server.py"]
- Volume
    - ボリュームが作成されてマウントされる領域
    - Volume /volume
- Expose
    - 外部に後悔するポート。ポートフォワードではないので、したかったらrun時にポートフォワードすること
    - Expose 80
- USER
    - コンテナが使うユーザを変更。デフォルトでroot
    - USER root
- ENTRYPOINT
    - イメージのデフォルト実行コマンドを強く定義
- WORKDIR
    - 作業ディレクトリを変更する際に使用
    - RUNでcdコマンドを実行するのは好ましくないからWORKDIRで移動するのが良いv
    - WORKDIR /



## わかったこと  
- ホストマシンとdockerコンテナのlocalhostは違う
    - なぜかというと、dockerコンテナを生成するとコンテナ毎に違うNICが割り当てられるから。以下のURLの図がわかりやすい  
        - http://tkyshm.hatenablog.com/entry/2014/08/11/155627  
        - https://www.itmedia.co.jp/enterprise/articles/1612/14/news013.html  
  
- dockerネットワークのdefault gateway  
    - dockerをインストールするとdockerネットワークを構築して、dockerのNICが作られるがこれはdockerネットワークのdefault gatawayとして動作する  
  
- dockerにflaskを載せたとたんlocalhostでflaskのサーバにつなげなくなる問題  
    - これはflaskがデフォルトだとlocalhostからの通信だけをLISTENしている事が原因。ホストマシンとdockerコンテナのlocalhostは違うため、ホストマシンからlocalhostにcurlを叩いてもdockerコンテナには届かない。  
        - 解決策としてはflaskで0.0.0.0でLISTENするか、nginxをプロキシにするかのどちらか  
            - https://qiita.com/amuyikam/items/01a8c16e3ddbcc734a46  

# サーバ
## わかったこと
- uWSGIはwebサーバとpythonフレームワークをつなぐためだけのものなので、サーバ機能はない  
- IP制御とLISTENでのIPアドレスの違い  
    - flaskの「host=192.168.99.100」のようにサーバでLISTENの動作を書くのはIP制御をかけているわけではない。「flaskが動いているホストマシンの192.168.99.100というNICで待ち受け(LISTEN)する」という意味。
        - IP制御をかけたいならファイアーウォールなどで制御する。  
  
# docker-compose  
- ポートマッピングの動作  
    - 「127.0.0.1:80:8080」 : ホストマシンのlocalhostの80番に向けて来たリクエストをコンテナの8080番ポートにフォワードする  
    - 「192.168.99.100:80:8080」 : ホストマシンの192.168.99.100の80番に向けて来たリクエストをコンテナの8080番ポートにフォワードする  
    - 「0.0.0.0:80:8080」 : ホストマシンすべてのNICの80番に向けて来たリクエストをコンテナの8080番ポートにフォワードする  
    - ホストIPを指定しないと暗黙的に0.0.0.0が指定される  
        - https://qiita.com/tksugimoto/items/23fcce1b067661e8aa46  

- makeコマンド一発のflaskのuWSGIのポートマッピングは不要  
    - docker-composeのuWSGIに3031:3031のポートマッピングが書かれていたが、ホストマシンからつなぐわけではないのでいらない気がする。
    - ポートマッピングはポートを開けている動作ではないので注意。

# 気になること
- nginxをリバースプロキシとキャッシュサーバとして使うというのはどういうことなのか？