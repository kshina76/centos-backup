# 開発手順

## 参考文献
- https://note.com/erukiti/n/nec8e3dbe4a53
- https://note.com/promitsu/n/n463792216407

## URLをブラウザに入れてから戻るまでの仕組み

![How-The-Web-Works jfif](https://user-images.githubusercontent.com/53253817/100647584-1a4e3f00-3383-11eb-9d81-aad2fb6c7d60.jpeg)

## システムデザイン
- https://github.com/donnemartin/system-design-primer

---

<br></br>


## 開発の進め方全体
### アジャイル開発
- 変更に強い開発スタイル
### スクラム
- 週1,2程度でガッツリとした打ち合わせ



---

<br></br>

## 開発をするときの鉄則
1. ある一つの作業をする時に複数のことをやらない
  - 人間は複数のことを行おうとすると混乱してしまう
2. 作業はなるべく小さく分割する（数をこなす）
  - トラブルシューティングがしやすい
3. まずはORM、問題があるところは生SQL
  - まず全てORMで書いてみてから、クエリを解析してN+1問題といった問題が起きていたらそこを生のSQLで書いて直す(ORMを工夫できるならそれでも可能)
  - ここでSQLチューニングの知識が必要になる
  - ORMと生SQLどっちもかけるフレームワークだと良い
4. 綺麗なアーキテクチャを作るのにinterfaceは別に必須ではない(依存方向をしっかりすればいい)
  - pospomeの書籍でもinterfaceを使っているのはクリーンアーキテクチャくらいだった
  - https://shinyorke.hatenablog.com/entry/fastapi
  - http://blog.fujimisakari.com/web_application_architecture_pattern/
5. マイクロフレームワークでもclassを使ったほうがいいのかもしれない(多分)
  - FastAPIのclass based view
  - https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/

## 技術選定
### 一般的な考え方
#### Webアプリケーションに必要な機能を抑えているフレームワークかどうか
- https://logmi.jp/tech/articles/322694
#### マイクロフレームワークかフルスタックフレームワークか
- Lambdaのように一つの機能を実装して、複数のLambdaを組み合わせて一つのサービスを構築するというパターンなら、マイクロフレームワークを組み合わせるのがいいと思う
  - マイクロサービス的な考え
  - それぞれのマイクロ
- モノリスなサービスの場合は、フルスタックフレームワークを使うべきだと思う。
- さらにマイクロフレームワークの場合は、関数ベースで書くかクラスベースで書くかどうかを規模によって決める
#### パフォーマンス
- Lambdaの場合はフレームワークのファイルサイズが大きくなるかどうかを見るといいかも。Lambdaのコールドスタートのせいで、ファイルサイズが大きいのは不利になるから。
#### AWS LambdaのようなFaaSを使う際のフレームワークは？
- https://aws.amazon.com/jp/builders-flash/202003/chalice-api/
- https://qiita.com/massa142/items/c59275237979fd939791
### プログラミング言語別
#### Python
- Awesome Flask
  - https://github.com/humiaozuzu/awesome-flask
- Awesome Python
  - https://qiita.com/hatai/items/34c91d4ee0b54bd7cb8b
- 小規模、中規模ならflask
  - APIとか簡単にサクッと開発できる
  - 中規模になったらblueprintでディレクトリ分割
  - https://qiita.com/gold-kou/items/00e265aadc2112b0f56a
- 綺麗なドキュメントも生成できるFastAPI
  - https://note.com/navitime_tech/n/nc0381517d067?magazine_key=mdafce2b0ebe1
- 大規模ならDjango
  - https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8
- Djangoでもflaskでも以下の機能はサードパーティのライブラリが必要
  - OpenAPI
  - JSON Schema
  - GraphQL
  - WebSocket
  - タイプヒントを使ったバリデーション
  - 非同期処理
  - CORS の設定
  - リバースプロキシとの連携サポート
- DjangoかFlaskか
  - モノリシックなWebアプリならDjango
  - マイクロサービスのようにWebAPIならFlaskで、フロントがReactの構成がよく使われる
  - https://www.youtube.com/watch?v=ogXfNQxA2LE
- FlaskかFastAPIか
  - https://zenn.dev/satto_sann/articles/b405ca8961d70fac99ff
  - https://qiita.com/bee2/items/75d9c0d7ba20e7a4a0e9
- SPAやMicroServiceの影響でFlaskやFastAPIやChaliceといったフレームワークが勢い付いてきている
  - https://python.ms/web/#_0-その前に
- FastAPI(Flaskよりこっちが流行ってきているかも)
  - https://qiita.com/bee2/items/75d9c0d7ba20e7a4a0e9
  - FastAPIのディレクトリ構成
    - https://note.com/yusugomori/n/n9f2c0422dfcd
  - FastAPIでアプリケーションを作っている(結構ちゃんとしているもの)
    - https://shinyorke.hatenablog.com/entry/fastapi
- フレームワーク一覧
  - https://www.acrovision.jp/career/?p=1897
- Pythonにおける技術選定(絶対見たほうがいい)
  - https://logmi.jp/tech/articles/322694
  - https://logmi.jp/tech/articles/322697
#### Golang
- Echo, Gin, Gormなどといったフレームワークを組み合わせる
  - routingはGinでORMにGormとか
  - Echoは結構パワフルな機能が揃っているのでフルスタックに分類されるかも
  - Golangのsqlの標準ライブラリは書くのが面倒
- フレームワーク一覧
  - https://qiita.com/yumin/items/5de33b068ead564ebcbf
- golangにおけるフレームワーク選定
  - https://www.pospome.work/entry/2020/04/27/153059
  - 上記のURLとpospomeさんの書籍をみる(アーキテクチャの部分)

<br></br>

## 設計
1. ユースケース図(箇条書きでも可)
  - 「誰が何をするか」ということを明確にして書いていく
2. シーケンス図(というよりアクティビティ図を書く)
  - ユースケース図で書いたそれぞれの機能にフォーカスする作業
  - 一つ一つの機能の流れをシーケンス図を使って書いていく
  - もっと細かくフローチャートのようにしたかったらアクティビティ図も書いてもいいかもしれないけど、シーケンス図で大枠を掴めればいい気がする
3. 画面遷移設計、デザイン
  - 「figma」というUI/UXツールでページのデザインを作成
  - Frameを意識することで、HTMLタグの付け方が頭に浮かんできて、後々のコーディング作業で楽になるという付加効果もある
  - 一つのページにFrameを分割して矢印を書けば、画面遷移図になる
  - 画面遷移設計は漏れが無いようにするためにユースケース図を参考にしながら進める
4. URL設計
  - 画面遷移設計やユースケース図を参考にしながらURLを考えていく
5. DB設計
  - ER図
  - 本でしっかり学ぶ
6. アーキテクチャ設計
  - 全体のレイヤー構成は、2層、3層、4層、クリーンアーキテクチャなどから選択する
  - プレゼンテーション層は、MVC、MVP、MVVMから選択する
  - フラットかレイヤー分割か
    - https://note.com/timakin/n/n02f6be6aa0bf?magazine_key=mdafce2b0ebe1
7. クラス設計
  1. ユースケース図とシーケンス図を参考にしてイベントフローやシナリオを文章で書き出す
  2. 固有名詞とかを抜き出してクラスにする
  - 詳しくは以下のREADME
    - https://github.com/kshina76/centos-backup/tree/master/OOP/oop_design
8. システム構成設計
  - インフラとか

<br></br>

## 開発
### 1. Github運用ルール
- ブランチの切り方のルール
  - git-flowモデル
    - develop(チームによってはmaster)から「feature/機能名orタスクID」ブラントを切って作業
    - featureに関してのルールが特にない場合、「feature/機能名」を英語で書く
- コメントのルール
  - 英語か日本語か
  - プログラムのコメントも英語か日本語か
- PRからマージ
  1. PushしたブランチからGitHub上でPRを作る
  2. PR用のテンプレート設定されているなら、それに入力
  3. Reviewersからレビューして欲しい人を選択
  4. PRのコメントに「close #issue番号(またはissueのURL)」を入力して、PRがマージされた際にissueも同時にcloseするようにする
  5. レビューを受けて承認をもらう(approve機能でマージがブロックされていと思うから)
  6. PRの画面で自分でマージする
  7. featureブランチを削除する
- レビュー後に直す必要がある場合(チームによって方針が異なるので聞く)
  1. 修正する
  2. ローカルで`git add` -> `git commit`
  3. `git rebase -i`でコミットを一つにまとめる
  4. `git push -f origin HEAD`
    - `-f`っていいんだっけ？？
- マージ完了後から次のタスクに備える
  1. `git checkout master`または`git checkout develop`
  2. `git pull origin master`または`git pull origin develop`
- 別のブランチで別のタスクに対応する
  - `git stash`コマンドを使うのでよく調べておく
- 直前のaddやcommitを取り消す
  - `git reset`コマンドを使うのでよく調べておく
- コンフリクトの発生は自分で発生させてみて、対処を覚えておく
- https://www.youtube.com/watch?v=wlY8YG-eB8E
### 2. 使用するツール
- コミュニケーション...Slack
- リモート会議...Teams
- タスク管理ツール...Jira, Trello
- API資料作成...Swagger
- 資料共有...Confluence
- CI...CircleCI
  - CIは自動ビルドと自動テスト
  - CDは自動デプロイ
- MacBookPro(16GB以上)
- https://www.youtube.com/watch?v=LT-dXBUnZdI
### 3. 開発環境構築
- DockerとDocker-Composeで作成する
  1. オンプレミスでインストールするときの手順を調べて必要なコマンドを抜き出す
    - マルチステージビルドを駆使すればいらないかも
    - パッケージをインストールする際などは必要
  2. 公式イメージと使い方をドキュメントでみる
  3. Dockerで構築してみる
  4. Docker-Composeで構築する
### 4. フロントエンドのコーディング
1. テンプレートタグを読み込めるようにバックエンドでハンドラを構築しておく
  - mainのを一つだけでいい
2. HTMLを全てコーディングする(HTML設計)
  - タグ付けはBEMという設計方法に従う(後々のCSSデザインに関わる)
    - https://qiita.com/pugiemonn/items/964203782e1fcb3d02c3
    - https://qiita.com/Takuan_Oishii/items/0f0d2c5dc33a9b2d9cb1#blockにはmarginを指定しない
    - 具体的に付ける場所はデザインを作った時のFrameを参考にすると良い
3. CSSでデザインをする
  - まず以下のURLのreset.cssを読み込む
    - http://html5doctor.com/html-5-reset-stylesheet/
  - googleフォントを使う
    - https://fonts.google.com/?sort=popularity
  - Sass記法を使って、BEMにしたがってデザインしていく
  - HTMLのコーディングが終わったらデザインをする作業に入っていく
  - 簡単なところはfigmaのcssをコピペ
    - 色くらいかな
### 5. バックエンドのコーディング
- 大前提
  - フローチャートを見ながら開発を進めていく(設計が大事ということ)
    - フローチャートを書かないと、処理を考えながらプログラムのことを考えないといけないので、同時に二つのことを考えてしまっているからだめ
  - メソッドの実装を呼び出すときは、返り値や引数をvscodeで確認しながら開発
    - 一々ファイル遷移で実装を見に行くのは非効率
  - 一つの機能を作ったらユニットテストを書く
    - 例えば、infra層のメソッドを作ったらテスト->usecase層のメソッドを作ったらテスト->...という感じ
  - DBのデータを削除したり作成したりは適宜コンテナに入ってSQLを発行すると楽
1. 下位層から作る
  - テストデータを駆使して開発を進める
  - データをDBにあらかじめ入れておく(コンテナに入ってcreateしておけばいいだけ)
  - 設計の段階で関数やクラスの入出力は決めておく
2. 次の層の開発をする
  - interfaceで疎結合に保つなら、infra層〜presentation層をつなげてから進める

### 6. インフラ構築
- AWS
- terraform

---

<br></br>

# WebAPIの開発
- リソース指向アーキテクチャの設計手順で行う
  - webを支える技術に手順が書いてあった
- RESTの設計
  - https://www.slideshare.net/pospome/rest-api-57207424
