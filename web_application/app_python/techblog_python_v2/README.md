# flask+postgresqlでtechblog開発

## 開発環境
- https://ameblo.jp/kazusa-g/entry-12592477686.html
### 1.docker
#### Dockerfile動作確認
- pythonコンテナ

```dockerfile
FROM python:latest
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD [ "python", "./your-daemon-or-script.py" ]
```

```bash
$ docker build -t python .
$ docker container run -it --rm --name python python /bin/bash
```

- postgresqlコンテナ

```dockerfile
FROM postgres:latest
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG en_US.UTF-8
COPY ./project/data/*.sql /docker-entrypoint-initdb.d/
```

- elasticserchコンテナ

```dockerfile
FROM elasticsearch:7.10.1
RUN elasticsearch-plugin install analysis-kuromoji
```

```bash
$ curl -X GET "localhost:9200/_cat/health?v&pretty"
```

### 2.python
#### pythonバージョン
- python3.9.0
#### 今時のpythonの書き方
- https://qiita.com/nicco_mirai/items/c1810ed2a6fc8c53c006
#### インストールするパッケージ
- コード規約が強い順に「pep8 < flake8 < pylint」らしい
- black+flake8はflake8のエラーの解消など色々やってくれる(今後デファクトになる可能性が高いらしい)
  - https://www.macky-studio.com/entry/2019/07/04/152323

#### blueprint
- urlルーティングを分散させる感じかな？djangoにも似たようなのが標準で搭載されていた
- https://qiita.com/shimajiri/items/fb7d1d58de0b0d171c88

### 3.vscode
- blackとflake8を有効化、pylintを無効化、一行あたりの最大値をflake8の88行に合わせる
  - 以下を.devcontainer.jsonのsettingに書く

```json
// リンタの設定
"python.linting.pylintEnabled": false,
"python.linting.flake8Enabled": true,
"python.linting.lintOnSave": true,
"python.linting.flake8Args": [
	"--max-line-length",
	"88",
	"--ignore=E203,W503,W504"
],
// フォーマッタの設定
"python.formatting.provider": "black",
"editor.formatOnSave": true,
"editor.formatOnPaste": false
```

- 参考文献
  - https://www.macky-studio.com/entry/2019/07/04/152323
  - https://qiita.com/tsu_0514/items/2d52c7bf79cd62d4af4a

### 4.ElasticSearch
- 今回は開発ようなのでシングルノードで起動させる
- 環境構築
  - https://qiita.com/kiyokiyo_kzsby/items/344fb2e9aead158a5545
  - https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html
  - https://qiita.com/romiogaku/items/ad82180cf2cbc280c10e
- 日本語の設定
  - https://qiita.com/shin_hayata/items/41c07923dbf58f13eec4

<br></br>

### pythonでレイヤードアーキテクチャをやってみる(各種ライブラリの使い方は学びながら。techblogでいいかな)
- https://qiita.com/yu-sa/items/e0033ae312669256cd8a

---

<br></br>

## FastAPIを使ったWebAPI開発
### 1. 題材
- とりあえず以下の機能を持ったTechBlogのWebAPIを開発する
  - User
    - 一般ユーザのサインアップ、ログイン、ログアウト機能
    - adminユーザのサインアップ、ログイン、ログアウト機能
    - 一般ユーザの投稿、編集、削除機能
    - adminユーザの投稿、編集、削除機能
    - ユーザのプロフィール取得、作成、編集機能
    - ユーザ退会機能
  - Post
    - タグ、カテゴリ機能
    - Postを件数指定で取得
    - ユーザを指定して、Postを取得(userのsearch機能)
    - 特定のキーワードのsearch機能

- TechBlogが終わったら、「個人Webサイト」の紹介WebAPIを作成

### 2. アーキテクチャ、ディレクトリ構成
- FastAPIの公式ディレクトリ構成(大規模プロジェクト向け)
  - https://fastapi.tiangolo.com/tutorial/bigger-applications/
- pospomeさんのpdfに書いてある、縦割りのディレクトリで、機能ごとにMVCを作るといった方針
  - User機能、Posts機能の二つならMVCが二つできるイメージ(P110参照)
- その他のディレクトリ構成
  - https://teratail.com/questions/138820
  - http://www.morita-it-lab.jp/document/develop/PG-Language/Python/library/Flask/directory.md

### 3. 使用フレームワーク、ライブラリ
- psycopg2
  - pythonからpostgresqlに接続するためのもの
- elasticsearch
- FastAPI(Flaskよりこっちが流行ってきているかも)
  - https://qiita.com/bee2/items/75d9c0d7ba20e7a4a0e9
  - FastAPIのディレクトリ構成
    - https://note.com/yusugomori/n/n9f2c0422dfcd
  - FastAPIでアプリケーションを作っている(結構ちゃんとしているもの)
    - https://shinyorke.hatenablog.com/entry/fastapi
  - asyncを使う場合と使わない場合(データベースへの問い合わせとかは使わないっぽい)
    - https://fastapi.tiangolo.com/ja/async/#in-a-hurry
#### 3-1. 参考文献
- Awesome Python
  - https://qiita.com/hatai/items/34c91d4ee0b54bd7cb8b
- SQL...psycopg2
  - https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
- Unittest
  - DBなどの外部サービスのテストはモックではなくてDockerで行う
- ElasticSearch
  - ブログ記事の内容から単語を検索してくるといったAPIを作りたい場合に、全文検索エンジンというのが使われる。その際のクエリパラメータはqを使って、サーバに投げて、qのクエリパラメータを全文検索エンジンに渡して、その結果をサーバからレスポストして返すといった感じ。elastic searchを使うが、サーバを立てたりするのでらdockerで組み込んでおく。実務ならAWSでElasticServiceというものがある。
  - https://agency-star.co.jp/column/elasticsearchとは？基礎と使い方をわかりやすく解説！デ/
  - https://qiita.com/nskydiving/items/1c2dc4e0b9c98d164329
  - https://www.slideshare.net/mobile/recruitcojp/elasticsearch-56355817
- SPAやMicroServiceの影響でFlaskやFastAPIやChaliceといったフレームワークが勢い付いてきている
  - https://python.ms/web/#_0-その前に

### 4. エンドポイントの設計(URI設計)

### 5. レスポンスデータの設計
- ステータスコードの設計も
  - https://qiita.com/NagaokaKenichi/items/eb85b5fbb719d60c6627

### 6. エラーの設計

### to do
- vanilla javascriptプロジェクトのバックエンドの実装を開発していけば、教材に困ることはなさそう
- 参考にするところ
  - asyncとdefを使い分けている理由はあとで調べる
  - https://dev.classmethod.jp/articles/implement-python-framework-fastapi-on-ec2-2/
  - https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/
- 上記に沿って開発を進める。テストを書きつつ開発を進める。(リソース指向の手順とwebapiのREADMEを合わせて進める)
  - docstringを書く
  - テストを書く
    - https://qiita.com/simonritchie/items/49e0813508cad4876b5a
  - とりあえずモノリシックに
  - URI設計
  - レスポンスデータの設計
  - ステータスコードの設計
  - Flaskのサンプル
    - https://qiita.com/tchnkmr/items/26d271886b46c4e52dc1
  - Chromeのネットワークタブなどでリクエストとレスポンスの中身を覗きながら開発してHTTPの理解も深める
- 検索機能のためにelasticsearchを学ぶ
- swaggerで載せ替えてみる
- セキュリティの懸念点を埋める
- 認証・認可に関して考える
- CI/CDツール(CircleCI)でテストを自動化する
- nginxの設定や使い方を学んで載せてみる
- Kubernetesに載せ替えてみる。macのローカルにインストールする
- 「入門　監視」を読んで監視の仕方を学ぶ。CloudWatchLogsでは足りない場面が出てくるので、Datalogなどのサードパーティを使う必要もある
- 開発が終わったらLambdaに載せ替えてみる
  - Lambdaのデザインパターンの書籍やサイトを読むべきかも
  - 複数のLambdaを使うときのパターンがいまいちわからないし
- マイクロサービス化もしてみる
  - オライリーの書籍を読むべきかも
- SQL関連の書籍を読んで、設計をし直す
- DBマイグレーションの自動化
  - VPC lambdaを使う方法
  - CodeBuildを使う方法

- 参考文献
  - https://qiita.com/poly_soft/items/fb649573c19b7a5c0227
