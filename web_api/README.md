# Web API The Good Parts 書籍メモ

## 1.Web APIとは何か
### Web API
- HTTPプロトコルを利用してネットワーク越しに呼び出すAPI
- プロトコルがHTTPなので、エンドポイントはURIを指定して呼び出す
- 機械的にアクセスしてデータを得るものなので、人間がブラウザにアクセスしたりクリックしたりして使うものではない
### API
- ソフトウェアコンポーネントの外部インタフェース
- 機能はわかっているが、その中身の詳しい動作はわからない(知らなくても良い)機能のかたまり

### 1-2.Web APIのパターン
- 公開しているウェブサービスのデータや機能のAPI公開
  - Programmable Webというサイトで色々な企業のAPIが公開されている
- 他のページに貼り付けるウィジェットの構築
  - Amazonで公開している自社の商品ページを、自分のサイトに貼り付けたりするパターンのAPI
  - AmazonやFaceBookが提供しているJavaScriptのコードを自分のサイトに貼り付けるだけで実装できる
  - ブラウザにJavaScriptのコードを埋め込むから、何をしているかわかってしまうので、悪用される可能性は増える
- モダンなwebアプリケーションの構築
  - SPAのように、ページを読み込むのと別のタイミングで情報を取得してレンダリングするのに使うAPI
  - 一般的な方法は、JavaScriptのAJAXを使ってAPIを叩くことで、データを取得する
  - ブラウザにJavaScriptのコードを埋め込むから、何をしているかわかってしまうので、悪用される可能性が増える
- スマートフォンアプリケーションの開発
  - クライアントとサーバの間をのAPIを開発するパターン
  - ブラウザほど悪用することは簡単ではないが、スマホとサーバの間の通信を盗聴すればわかってしまうので、注意が必要
- ソーシャルゲームの開発
  - 他の人と協力して行うといった性質なのでサーバ側にデータを保存する必要があるから、APIが使われる
  - MMORPGほどのリアルタイム性はいらないから、手軽なAPIが使われることが多い
  - チートされないような設計にする必要がある
- 社内システムの連携
  - 各システムの連携をWebAPIを使って疎結合にすることで、変更に強いシステムにできるから、APIが使われる

### 1-3.何をAPIで公開するべきか
- 「そのwebサービスで行える全ての機能」または「コアとなるサービスの機能」
  - 例えば、ECサイトなら「商品の検索」や「商品の購入」といった機能

### 1-4.WebAPIを美しく設計する重要性
- 使いやすい
- 変更しやすい
- 頑強である
- 恥ずかしくない

### 1-6.RESTという言葉は曖昧
- WebベースのAPIを何でもかんでもRESTと呼んでいたりするから、そこまでRESTという言葉にこだわりすぎない方がいいかも

<br></br>

## 2.エンドポイントの設計とリクエストの形式

### 2-1.APIとして公開する機能を設計する
- まず自分のサービスに対して、どのパターンのWebAPIを作成するかを決める(例えば以下の二つのAPIを開発することを考える)
  - モバイルアプリのバックエンドとしてのAPI
  - 公開用のAPI

- モバイルアプリのバックエンドのAPI
  1. クライアントの画面遷移図を作る
  2. 1を参考にしながらユースケース図に落とし込む

### 2-2.APIエンドポイントの設計
#### 0.大前提
- WebAPIの場合は、URIを設計することと同値
- 前提として「覚えやすく、どんな機能を持つURIなのかが一目で判断できるようなもの」を考える
#### 1.短く入力しやすいURI

```bash
# 悪い例...apiという文字がかぶっている。serviceは他のAPIと被ってしまいそう
http://api.example.com/service/api/search

# 良い例...検索のAPIであることが見てわかる
http://api.example.com/serach
```

#### 2.人間が読んで理解できるURI
- productsをprodのように略してはだめ
- 英語を使うようにする
  - findよりsearchを使う。というようにAPIではどのような単語が一般的かを知る必要がある
  - Programmable APIというサイトでどのような単語が使われているかを勉強するのがいい(Qiitaの記事に出来そう)
  - https://qiita.com/Ted-HM/items/7dde25dcffae4cdc7923

```bash
# 悪い例
http://api.example.com/sv/u

# 良い例
http://api.example.com/products/12345
```

#### 3.大文字小文字が混在していないURI
- 大文字と小文字は区別するようにする
  - 本来はusersだけど、Usersでアクセスが来た場合はNot Foundで返すのが一般的

```bash
# 悪い例
http://api.example.com/Users/12345

# 良い例
http://api.example.com/users/12345
```

#### 4.改造しやすいURI
- idを変えれば違うuserにアクセスできるとわかるようなURI

```bash
# 良い例
http://api.example.com/users/12345
```

#### 5.サーバ側のアーキテクチャが反映されていないURI
- どんな言語を使っているか、サーバサイドのディレクトリやシステム構成がどのようになっているかといったことを意識させない

```bash
# 悪い例...phpを使ってCGIとして動作しているということがわかってしまう
http://api.example.com/cgi-bin/get_user.php?user=100
```

#### 6.ルールが統一されたURI

```bash
# 悪い例
http://api.example.com/friends?id=100
http://api.example.com/friend/100/message

# 良い例
http://api.example.com/friends/100
http://api.example.com/friends/100/message

```

### 2-3.HTTPメソッドとエンドポイント
- メソッド...リソースに対して何をするか
- URI...リソース
- WebアプリのformではGETとPOSTしか使えないが、WebAPIでは様々なメソッドが用意されているので、それらを駆使する

#### 1.GET...リソースの取得
- URIで指定されたリソースを取得する

#### 2.POST...リソースの新規登録
- 指定したURIに属する新しいリソースを送信する
  - 簡単に言うと、新しい情報を登録するために使う
- 「リソースを送信すること」ではないので注意
  - リソースを送信して既存のリソースを置き換えるというのはPUTというメソッドが存在するから

#### 3.PUT...既存リソースの更新
- 既存のリソースを完全に上書きする

```bash
# POST
http://api.example.com/v1/friends
|
| POST(新規作成)
↓
http://api.example.com/v1/friends/12345

# PUT
http://api.example.com/v1/friends/12345
|
| PUT(置き換える)
↓
http://api.example.com/v1/friends/12345
```

#### 4.PATCH...リソースの一部変更
- 既存のリソースの一部を置き換える

#### 5.DELETE...リソースの削除
- 既存のリソースの削除をする


#### 6.HEAD...リソースのメタ情報の取得

#### GETとPOSTしか使えない環境の場合はどうするか
- X-HTTP-Method-Overrideヘッダを使う方法

- _Methodを使う方法

### 2-4.APIのエンドポイント設計
- リソースを集合論に当てはめて設計していく
- 「あるデータの集合」と「個々のデータ」の二種類に分類して、HTTPメソッドを適用していく
  - DBでいうとテーブルとレコードの関係を意識する
  - 以下の例だと、エンドポイントが二種類に分類できていることがわかる

| 目的                     | エンドポイント                      | メソッド  | 
| ------------------------ | ----------------------------------- | --------- | 
| ユーザ一覧取得           | http://api.example.com_v1/users     | GET       | 
| ユーザの新規登録         | http://api.example.com_v1/users     | POST      | 
| 特定のユーザの情報の取得 | http://api.example.com_v1/users/:id | GET       | 
| ユーザの情報の更新       | http://api.example.com_v1/users/:id | PUT/PATCH | 
| ユーザの情報の削除       | http://api.example.com_v1/users/:id | DELETE    | 

| 目的                 | エンドポイント                                  | メソッド | 
| -------------------- | ----------------------------------------------- | -------- | 
| ユーザの友達一覧取得 | http://api.example.com_v1/users/:id/friends     | GET      | 
| 友達の追加           | http://api.example.com_v1/users/:id/friends     | POST     | 
| 友達の削除           | http://api.example.com_v1/users/:id/friends/:id | DELETE   | 

| 目的                   | エンドポイント                                      | メソッド | 
| ---------------------- | --------------------------------------------------- | -------- | 
| 近況の編集             | http://api.example.com_v1/updates/:id               | PUT      | 
| 近況の削除             | http://api.example.com_v1/updates/:id               | DELETE   | 
| 近況の投稿             | http://api.example.com_v1/updates                   | POST     | 
| 特定ユーザの近況の取得 | http://api.example.com_v1/users/:id/updates         | GET      | 
| 友達の近況一覧の取得   | http://api.example.com_v1/usres/:id/friends/updates | GET      | 

#### エンドポイント設計の注意点
- 複数系の名詞に気を付ける
  - 「集合」を表すものは複数形にするべき
  - 複数形になることで大きく変わるものにも注意...media->mediumとか
- 動詞はメソッドが担うので、リソースは名詞に徹する
- 利用する単語に気を付ける
  - findではなくてsearchなど
- スペースやエンコードを必要とする文字を使わない
  - パーセントエンコーディングされてしまうため
- 単語をつなげる必要がある場合はハイフンを利用する
  - スパイナルケース、チェインケース
    - profile-image
  - スネークケース
    - profile_image
  - キャメルケース
    - profileImage

### 2-5.検索とクエリパラメータの設計(P42)

#### 1.取得数と取得位置のクエリパラメータ...ページネーションの仕組みを提供するため
- page/per_page...自由度が低い
  - pageは取得するページ番号、per_pageは1ページあたりのアイテム数
  - per_page=50&page=3
    - 101番目から150番目までのアイテムを取得する

- offset/limit...自由度が高い(好まれる)
  - offsetは0から数えた時のアイテム番号、limitは1ページあたりのアイテム数
  - offset=100&limit=50
    - 101番目から150番目までのアイテムを取得する

- 相対位置を使用する際の問題点
  - データ数が増えるとパフォーマンスが悪い
    - 一件目から順番に検索するから
  - データに不整合が生じる可能性がある

- 絶対位置でデータを取得する

#### 2.絞り込みのためのパラメータ
- qはフィールドが一つの時、部分一致の検索をするときに使う
- searchを使っている理由は、量が多すぎて一覧は取ってこれないけど、検索をするapiですよということを表したい場合は有効

```
http://api.linkedin.com/v1/people-search?first-name=Clair

http://api.instagram.com/v1/users/search?q=jack
```

#### 3.クエリパラメータとパスの使い分け(リクエスト)
1. クエリストリングに含める
  - 何らかのリソースのフィルタリング、ソート、ページングを実現したいときに使う

```bash
# 検索
curl localhost:3000/items?name=hoge
# ソート
curl localhost:3000/items?sort_by=price&order=asc
# ページング
curl localhost:3000/items?page=3&limit=50
```

2. リクエストボディに含める
  - リソースの作成や更新で必要な情報はここに入れる
  - ユーザーの入力値とか

```bash
# 作成
curl -X POST localhost:3000/items -d '{"name": "hoge", "price": 200}'
# 更新
curl -X PUT localhost:3000/items/1 -d '{"name": "fuga", "price": 400}'
curl -X PATCH localhost:3000/items/1 -d '{"price": 500}'
```

3. パスに含める
  - 一意にリソースを特定できる識別子は必ずパスに含める
  - IDとか商品コードとか注文番号とか
  - 逆に複数リソースが該当する可能性がある場合は含めるべきではない

```bash
# 商品コードABC-123の商品の情報を取得する
curl localhost:3000/items/ABC-123
# 注文番号O-1239の注文のステータスを更新する
curl -X PATCH localhost:3000/orders/O-1239 -d '{"status": "delivered"}'
```

4. まとめると

```ruby
if param == "一意にリソースを特定できるユニークな識別子である"
  # => パス
elsif param == "リソースを作成または更新する際の、リソースの情報/状態を表す値である"
  # => リクエストボディ
elsif param == "リソースのフィルタリング/ソート/ページングを表す"
  # => クエリストリング
elsif param == "認証情報である"
  # => クエリストリング または ヘッダー
elsif param == "コンテンツのデータには直接関係しないメタ情報である"
  # => ヘッダー
end
```

- 参考文献
  - https://qiita.com/sakuraya/items/6f1030279a747bcce648

### 2-6.ログインとOAuth2.0
- P49-57とqiitaとかを参考にして載せる
  - oauthにも色々な種類がある？あとで本からまとめる

#### WebAPI認証方式パターン
1. 標準化されたHTTP認証方式

2. APIキー認証

3. Form認証、アクセストークン認証

- OAuthの間違いやすい点
  - OAuthは認可をする仕組み
  - Bearerは認証をする仕組み
  - OAuthで認可をしてトークンを受け取り、Bearerでそのトークンを使って認証をする
  - AWS Cogniteは認可サーバの役割を担う

- 参考文献
  - https://architecting.hateblo.jp/entry/2020/03/27/033758

#### OAuthの説明

![https---qiita-image-store s3 amazonaws com-0-106044-d9119f21-736d-d5ed-964d-3068af0fcde9](https://user-images.githubusercontent.com/53253817/101063729-7eb50c80-35d6-11eb-8199-76d16868daab.png)

![https---qiita-image-store s3 amazonaws com-0-106044-f8dc0cca-15c1-569d-c6e4-2055ea8c97cb](https://user-images.githubusercontent.com/53253817/101062668-45c86800-35d5-11eb-8606-857e616ed3d5.png)

![https---qiita-image-store s3 amazonaws com-0-106044-319dd4e8-72b7-1af2-8bed-645120196b47](https://user-images.githubusercontent.com/53253817/101062672-46f99500-35d5-11eb-8f11-11282b19d5ae.png)

- 参考文献
  - https://qiita.com/TakahikoKawasaki/items/e37caf50776e00e733be

### 2-7.適切なホスト名
- api.example.com

### 2-8.SSKDsとAPIデザイン
- 誰が使うかわからない公開するAPIはきれいに作る必要がある
- モバイルアプリのバックエンドといった、内部の開発者しか使わない場合は綺麗さより、ユーザ体験を優先するべき
  - 例えば、「新着の商品」「人気の商品」「ログイン中のユーザ情報」などといったものを個別で用意するのではなくて、「初期画面」というAPIを作って一回のAPI通信で取得できるようにしたほうが、画面を一気に描画できるし、速度も上がってユーザ体験が上がる。

### 2-9.HATEOASとREST LEVEL3 API

| 目的        | エンドポイント                              | 
| ----------- | ------------------------------------------- | 
| REST LEVEL0 | HTTPを使っている                            | 
| REST LEVEL1 | リソースの概念の導入                        | 
| REST LEVEL2 | HTTPの動詞（GET/POST/PUT/DELETEなど）の導入 | 
| REST LEVEL3 | HATEOASの導入                               | 

<br></br>

## 3.レスポンスデータの設計

### 3-1.データフォーマット
- JSON、XMLなど

#### データフォーマットの指定方法
1. クエリパラメータを使う方法
  - 一番わかりやすい方法で、一番採用されている

```
http://api.example.com/v1/users?format=xml
```

2. 拡張子を使う方法

```
http://api.example.com/v1/users.json
```

3. リクエストヘッダでメディアタイプを指定する方法
  - Acceptヘッダで指定する方法
  - Acceptヘッダは複数行にわたって指定できる

```
GET /v1/users
HOST: api.exmaple.com
Accept: application.json
```

- どれがいいのか？
  - 一つだけサポートするなら1の方法
  - 複数サポートするなら1,3の方法

### 3-2.JSONPとXHTTPRequest(P69)
