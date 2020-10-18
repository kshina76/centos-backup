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

- コマンド
    - コンテナ起動
        - docker container run nginx
            - --it bash
                - 端末操作可能
            - -d
                - detachの略で、バックグラウンド起動する
            - --rm
                - コンテナが停止された時にコンテナを削除する
                - --nameと併用すると便利で、停止した後に同じコンテナを起動しても名前の重複がしなくなる
            - --name
                - コンテナに名前をつける

<br></br>

- dockerコンテナは停止した時に破棄するべき（場合による？）
    - ライフサイクル的には削除するべきらしい
    - runコマンド時にrmオプションをつけると、停止したときに削除する

<br></br>

- 

# docker
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