# データベースの実装の種類
- クライアントサーバ型と組み込み型
    - クライアントサーバ型
        - PostgreSQL, MySQL, etc
        - アプリケーション(クライアント側)がデータを欲しい時にデータベースにアクセスする際、別のマシン(サーバ側)にデータベースがある
        - 一つのマシンでアプリケーションとクライアントサーバ型のDBを共存させるにはDockerを使う
            - 本番ではこのような構成はないと思うが、学習用に。
            - 本番で導入するにはAWSを使ってDBサーバを別途構築すればいいと思う
    - 組み込み型
        - SQLite
        - アプリケーションそのものにデータベースが内蔵されている
    - https://bigdata-tools.com/sql-db/

# SQLの基礎
- データベースとテーブルは違う
    - データベースの中にテーブルが複数ある
    - データベースは複数作ることができる
        - db1、db2という名前で二つ作ったら、db1のなかにテーブルが複数、db2の中にテーブルが複数といった感じ

# PostgreSQL

## Centosなどに直接インストールして使う場合
- postgresqlを起動
    - 設定ファイルなど色々作成されるらしい

```bash
$ /etc/rc.d/init.d/postgresql start
```

- 初期設定
    - スーパーユーザの名前はpostgresで生成される
    - postgresユーザのパスワードを変更する
    - データベースを作成する
    - テーブルの定義などが書かれたsqlファイルを実行する

```bash
//postgresユーザのパスワードを変更する

$ passwd postgres
>New password
>Retype password
```

```bash
//データベースを作成する。今回はapp_dbという名前で

$ createdb app_db
```

```bash
//ファイルを指定して、テーブルなどを作成する(さっき作ったapp_dbデータベースを指定している)

$ psql -f setup.sql -d app_db
```

```sql
--setup.sqlの中身
drop table users;
create table users (
  id         serial primary key,
  uuid       varchar(64) not null unique,
  name       varchar(255),
  email      varchar(255) not null unique,
  password   varchar(255) not null,
  created_at timestamp not null   
);
```

## Dockerを使って構築した場合(go+postgresqlで構築している)

- docker-composeの環境変数で設定するもの
    - POSTGRES_USER: app_user
        - スーパーユーザの名前(デフォルトだとpostgres)
    - POSTGRES_PASSWORD: password
        - スーパユーザのパスワード
    - POSTGRES_DB: app_db
        - 作成するデータベースの名前

```Dockerfile
# postgresqlのDockerfile

FROM postgres:latest
# ロケールの設定(postgresql公式のdockerhubに書いてあった)
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
# 最初に作るテーブルを定義したsqlファイルをコンテナ起動時に実行できる設定(共通)
COPY ./chitchat/data/*.sql /docker-entrypoint-initdb.d/
```

```Dockerfile
# goのDockerfile

# ベースとなるDockerイメージ指定
FROM golang:latest
# コンテナ内に作業ディレクトリを作成
RUN mkdir /go/src/chitchat
# コンテナログイン時のディレクトリ指定
WORKDIR /go/src/chitchat
# ホストのファイルをコンテナの作業ディレクトリに移行
COPY ./chitchat /go/src/chitchat
# golangでdbを操作するためのパッケージ
RUN go get github.com/lib/pq
```

```yaml
version: '3' # composeファイルのバーション指定

services:

  postgres:
    container_name: postgres # 名前解決できるようになる(多分)
    build:
      context: .
      dockerfile: ./docker/postgresql/Dockerfile
    tty: true
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: app_db
    

  app: # service名
    container_name: app
    depends_on:
      - postgres
    build:
      context: . # どこをカレントディレクトリとしてみるかということ。Dockerfileの中のパスの書き方も変わるから注意
      dockerfile: ./docker/golang/Dockerfile # ビルドに使用するDockerfileがあるディレクトリ指定
    tty: true # コンテナの起動永続化
    ports:
      - "8080:8080"
    volumes:
      - ./chitchat:/go/src/chitchat # マウントディレクトリ指定
```

```go
//goにおいて、initはパッケージの初期化を行う
//sql.Openでdocker-composeで設定した内容を引数に渡す
/*
host : docker-composeのcontainer_nameで設定
port : docker-composeのportで設定(ポートフォワード)
user,password,dbname : docker-composeの環境変数のPOSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_DBでそれぞれ設定
*/
func init() {
	var err error
	Db, err = sql.Open("postgres", "host=postgres port=5432 user=app_user password=password dbname=app_db sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	return
}
```