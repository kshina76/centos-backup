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
