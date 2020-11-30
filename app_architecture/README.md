# アプリケーションアーキテクチャ

- todo
  - CQRSについてまとめる

  - SOLID原則をまとめる
    - https://qiita.com/shunp/items/646c86bb3cc149f7cff9

  - YAGNI原則をまとめる
    - https://qiita.com/sesame525/items/fb2cfb23d0d7ef593014

  - DRY原則をまとめる
    - DRYを鵜呑みにして、なんでも共通化してはいけない
    - 用法容量を守って使わないとだめということ
    - https://qiita.com/yatmsu/items/b4a84c4ae78fd67a364c

<br></br>

## アーキテクチャパターン
### モノリシックアプリケーション
- 一枚岩でシステムを構築すること
- システム全体を一つのレイヤードアーキテクチャで構成した場合などがこれにあたる
- アプリケーションアーキテクチャの一番基礎の部分

### マイクロサービス・サービス指向アーキテクチャ(SOA)
- マイクロサービスとSOAの違いは「複雑度」
  - マイクロサービスはREST APIで連携させる
  - SOAはSOAP(XML)やWSDLやESBといった複雑な連携をしている
- https://news.mynavi.jp/itsearch/article/devsoft/1598


### CQRSとEventSourcing
- CQRSとはSQLを更新系(コマンド)と参照系(クエリ)に分けて、domain層を更新系のmodelと参照系のmodelに分けて実装する
  - https://www.slideshare.net/koichiromatsuoka/ddd-x-cqrs-orm

- CQRSはDDDのdomain層をさらにSQLの種類によって分割したもの
  - https://little-hands.hatenablog.com/entry/2019/12/02/cqrs

- CQRSのパターン(一番わかりやすい)
  - よくある誤解なども話している
  - CQRSを3段階に分けて、要件に対してどの段階まで取り込むかといった説明
  - https://little-hands.hatenablog.com/entry/2019/12/02/cqrs

- CQRSでDBを分割した場合にDBを反映させる方法はRDBに搭載されているレプリケーションを使うのが一般的

- CQSとCQRSの違い
  - https://qiita.com/hirodragon/items/6281df80661401f48731

- CQSのいろいろな例
  - https://qiita.com/pakkun/items/7dc5a9b6bc57225a3673

- 参考文献
  - https://speakerdeck.com/hirodragon112/ddddao-ru-nita-miqie-renaifang-hezeng-ru-2ceng-plus-cqs-akitekutiya-flyweight-ddd
  - https://hiroronn.hatenablog.jp/entry/20171106/1509972382
  - https://postd.cc/using-cqrs-with-event-sourcing/


### サーバレス
- AWS Lambdaなどを活用したもの

<br></br>

## アプリケーションの種類と開発パターン
### コンソールアプリケーション
- あまり詳しくないので、後々追記する
- Webアプリケーションなどとは違ったアーキテクチャを採用するパターンが使われる（pipes and filterとかかな？）
### IOS, Androidアプリケーション
- あまり詳しくないので、後々追記する
- クライアントサイドの開発が主になるパターンが多いと思う
- サーバサイドは別で構築してAPI接続で連携することが多い
### Webアプリケーション
- フルスタックフレームワークでフロントエンドからバックエンドまで一気に構築するパターン
- フロントエンドとバックエンドを別々のフレームワークで構築して、API接続で連携するパターン
- IOS,AndroidのサーバサイドとしてAPIを構築するパターン
### API
- アプリケーションがHTMLを返すのではなくてJSONを返すようになったパターンとして開発すればいい
  - ViewがHTMLでなくてJSONを返すということ
- goで色々なアーキテクチャでAPIを実装している
  - https://qiita.com/ogady/items/34aae1b2af3080e0fec4
  - https://qiita.com/hmarf/items/7f4d39c48775c205b99b
  - https://qiita.com/yuukiyuuki327/items/238814326964e06dd655
  - https://qiita.com/ryokky59/items/6c2b35169fb6acafce15

<br></br>

## GUIアーキテクチャとシステムアーキテクチャ
- アプリケーションはGUIアーキテクチャとシステムアーキテクチャで構成される
  - GUIアーキテクチャは、「UIに関するロジック(プレゼンテーション層)」と「システムに関するビジネスロジック」を分離することが目的
  - システムアーキテクチャは、Modelにあたる「システムに関するビジネスロジック」をさらに細分化するためのアーキテクチャ
  - 小規模のアプリに関してはGUIアーキテクチャのみで構築することもある

  ![2020-11-29 14 28のイメージ](https://user-images.githubusercontent.com/53253817/100534209-b6772980-324f-11eb-9dda-dfa423f074f7.jpeg)
  [10分で振り返る_ソフトウェアアーキテクチャの歴史2017_v1.1.pdf](https://github.com/kshina76/centos-backup/files/5560641/10._.2017_v1.1.pdf)

<br></br>

## アーキテクチャの選択
### 小規模
- MVxアーキテクチャ+ORM
  - フレームワークに沿って開発するだけで構築できる
  - ORMを使うのでinfra層を隠蔽できる
### 中規模
- MVxアーキテクチャ+レイヤードアーキテクチャ(3層)
  - 「interfaceで疎結合にする」か「直接参照で密結合にする」かはどちらでもいい
- MVxアーキテクチャ+リラックスレイヤードアーキテクチャ(3層)
  - 上位層は一つ飛ばしで下位層にアクセスできるように条件を緩めたもの
- MVxアーキテクチャ+DDDレイヤードアーキテクチャ(3層)
  - infra層にDIPを適用したもの
- MVxアーキテクチャ+DDDリラックスレイヤードアーキテクチャ(3層)
### 大規模
  - MVxアーキテクチャ+レイヤードアーキテクチャ(4層)
  - MVxアーキテクチャ+リラックスレイヤードアーキテクチャ(4層)
  - MVxアーキテクチャ+DDDレイヤードアーキテクチャ(4層)
  - MVxアーキテクチャ+DDDリラックスレイヤードアーキテクチャ(4層)
  - MVxアーキテクチャ+クリーンアーキテクチャ
### マイクロサービスアーキテクチャ
- 上記のアーキテクチャで構成したサービスを一つの機能として、いろいろなサービスを連携させることで一つのシステムを構築するアーキテクチャ
- 「サーバレスアーキテクチャを使用するパターン」と「コンテナを使用するパターン」がある

<br></br>

## システムアーキテクチャ
### MVCアーキテクチャ+ORM...レイヤードアーキテクチャの2層のようなもの

### 純粋な3層レイヤードアーキテクチャ
- ドメインモデルパターンを使う場合
  - domain-service
    - 引数に入力値のDTOを受け取る
    - domain-serviceクラスでinfra層のCRUD操作を呼び出して、DBからmodelに格納したり、modelからDBに格納したりする
      - ORMを使う場合でもSQLをそのまま書く場合でも同じくdomain-serviceで。(以下の1枚目の図はORMを使用しているため、entityとRDBの間に矢印がある。生のSQLならdomain-serviceクラスからentityに保存する処理を書く)
      - 勘違いしやすいのが、modelのクラスにビジネスロジックとしてinfra層へのアクセス(CRUD)を書いてしまうこと。これはダメ。
    - domain-serviceクラスからmodelのインスタンス化とかを行う(多分)
    - modelの単純なビジネスロジックを呼び出すだけでも必ずdomain-serviceクラスを経由する
    - domain-serviceはpresentation層から依存される
      - domain-serviceがinterfaceを提供する
    - domain-serviceクラスはinfra層に依存する(プロパティにinfra層のinterfaceを持つ)
    - 複数のserviceクラスを作って良い
  - Entity、Value Object
    - domain層でさらに別にmodelのクラスを別ファイルで作成する。これがビジネスロジックのためのもの。単なるCRUDの場合、modelはドメインモデル貧血症になる。(簡単なアプリだからしょうがない)
    - ORMを使わない場合は、domain-serviceクラスからのみアクセスされる
  - P165の図

- トランザクションスクリプトパターンを使う場合
  - Presentation層
    - HTMLやJSONを生成する
    - ユーザ入力をDTOに詰めて、Domain層を呼び出す
  - Domain層
    - domain-serviceクラス
      - DTOを入力(メソッドの引数)、ビジネスロジックが適用されたDTOが出力
      - infra層を呼び出してDTOにビジネスロジックを適用してDBに保存したり、DBから取得してDTOに保存してpresentationに返したり
      - プロパティにinfra層のinterfaceを持つことで依存する
      - 一つのユースケースがdomain-serviceクラスの一つのメソッドに対応する(P162)
      - domain-serviceクラスは責務に応じて複数定義
    - modelは定義しない。代わりにDTOを定義する
  - Infra層
    - 外部API呼び出し
    - データベースアクセスのためのSQL発行
      - ORMの場合は隠蔽される
  - DTOを媒介としたパイプライン処理として見るとわかりやすい(これと下の図が特に重要)
  - アプリケーションアーキテクチャ設計パターンのP157-162を参考にするとわかりやすい
  - P157の図

### 純粋な4層レイヤードアーキテクチャ
- ドメインモデルパターンを使う場合
  - Presentation層
    - HTMLやJSONを生成する
    - Usecase層の呼び出し
  - Usecase層
    - BusinessLogic層のdomain-serviceクラスの呼び出し
    - ビジネスロジックに関係ない処理(通知処理とか)
  - BusinessLogic層
    - domain-service
      - Infra層を呼び出してmodelにCRUD操作を適用させて、modelを生成
      - ビジネスロジックの定義
    - model(entity, value-object)
      - ビジネスロジックの定義
        - プロパティとメソッドを持つ
  - Infra層
    - 外部API呼び出し
    - データベースアクセスのためのSQL発行
      - ORMの場合は隠蔽される

- トランザクションスクリプトパターンを使う場合(トランザクションスクリプトを使う場合は、4層はない気がしてきた)
  - 3層とあまり変わらない
  - Usecase層が、「通知処理」といったものを担当してくれるくらいかな

- リラックスレイヤードアーキテクチャの場合は、domain-serviceクラスの「infra層のCRUD操作の呼び出し」をusecase層が担当することがある
- 4層のDDDレイヤードアーキテクチャの場合もdomain-serviceクラスの「infra層のCRUD操作の呼び出し」をusecase層が担当する
  - https://little-hands.hatenablog.com/entry/2018/12/10/ddd-architecture

![layerd-architcture](https://user-images.githubusercontent.com/53253817/100541256-de817f80-3285-11eb-825c-d2f4aaa9ca10.jpg)



### DDD3,4層レイヤードアーキテクチャ
- https://little-hands.hatenablog.com/entry/2018/12/10/ddd-architecture
- https://qiita.com/tono-maron/items/345c433b86f74d314c8d
- https://github.com/jojoarianto/go-ddd-api

### オニオンアーキテクチャ

### クリーンアーキテクチャ

<br></br>

## システムアーキテクチャを採用したときのディレクトリ構成例

### 3層レイヤードアーキテクチャ
- トランザクションスクリプトを使ったパターン
  - account_xxx.goやindex_xxx.goにそれぞれの層のinterfaceが定義される
  - DTOは全体の層から共通に使用されるようにproject直下のディレクトリにDTOディレクトリを配置してdtoパッケージにしてしまってもいいかも

```
project
├── DI
│   └── di.go
├── infra
│   ├── DTO
│   │   ├── postsDTO.go
│   │   ├── sessionDTO.go
│   │   └── userDTO.go
│   ├── account_infra.go
│   └── index_infra.go
├── main.go
├── presentation
│   ├── DTO
│   │   ├── postsDTO.go
│   │   ├── sessionDTO.go
│   │   └── userDTO.go
│   ├── account_controller.go
│   └── index_controller.go
└── usecase
    ├── DTO
    │   ├── postsDTO.go
    │   ├── sessionDTO.go
    │   └── userDTO.go
    ├── account_usecase.go
    └── index_usecase.go
```

- ドメインモデルを使ったパターン

  ![2020-11-30 17 26のイメージ](https://user-images.githubusercontent.com/53253817/100585662-44771100-3331-11eb-8c9b-3774ad14741d.jpeg)
