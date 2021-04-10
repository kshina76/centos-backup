# TypeScriptでアプリ開発

## 準備
- [x] Docker
- [ ] JavaScript
- [x] npm
  - [x] package.json
  - [x] nodebrew
  - [x] dockerでの構築
- [x] yarn
- [x] Node.js
- [ ] TypeScript
  - [ ] tsconfig.json
  - [ ] ts-loader
  - [x] webpack
  - [ ] ts-node
  - [ ] gulp: タスクランナー
  - [x] tsoa: コードからswaggerのドキュメントを生成するもの(とりあえず使わない)
- [ ] axios: APIを叩くクライアント
- [ ] TSyringe: 軽量DIコンテナ
- [x] swagger: ブラウザ上で使えるAPIスキーム定義

### DockerでTypeScript+express構成
- [dockerで構築](https://ichi.pro/typescript-swagger-ui-dockercompose-o-sonaeta-express-js-bakku-endo-272065836223432)
- 方針
  - ローカルでpackage.jsonを作って、色々ライブラリを構築する
  - package.jsonをコンテナにコピーする
  - コンテナ内でpackage.jsonを`npm install`する

### JavaScript

```bash
# サーバサイドのJSを実行
$ node test.js
```

### Node.js
- インストール方法: [ここを参照](https://liginc.co.jp/513122)
  - 一つ目の方法(非推奨): Node.jsの公式サイトからダウンロード（ZIPファイルを落とす）
  - 二つ目の方法(推奨): nodebrewを使う
  - 三つ目の方法(推奨): docker()
- 個人的な方法: nodebrewとdockerのハイブリッド
  - nodebrewをインストールして、package.jsonの雛形の作成などをローカルで行う
  - dockerではNode.jsを直接インストールして、ローカルで作成したpackage.jsonをベースに環境を構築する
  - package.jsonをコンテナ作成時に実行するようにしておけば、dockerでNode.jsの環境構築が楽になりそう
- [macにNode.jsをインスト](https://qiita.com/kyosuke5_20/items/c5f68fc9d89b84c0df09)

### nodebrew
- npmとnode.jsのバージョン管理を行ってくれる

### npm
- Node.jsのパッケージを管理するもの
- package.jsonでプロジェクト毎にパッケージを管理することができる
  - Pythonでいうrequirmentsみたいなものかな
- [グローバルインストールは避ける](https://mosapride.com/index.php/2018/02/06/post-681/)
- [既存のnpmを削除してnodebrewをインスト](https://nabewakashi.com/how-to-switch-to-nodebrew)
- [package.jsonの使い方](https://qiita.com/righteous/items/e5448cb2e7e11ab7d477)
- [dockerでpackage.jsonを使ったNode.jsのパッケージ環境構築](https://qiita.com/niwasawa/items/9673d31ee2a6c532dc5b)

### npm, npxまとめ
- 「Node Package Manager」の略
  - Node.jsのパッケージ（Package）を管理する（Manager）ツール
- [npmの基本的な使い方](https://techacademy.jp/magazine/16105)
  
  ```bash
  # インストール
  $ npm install express
  # バージョン指定をしてインストール
  $ npm install express@4.16.3
  # グローバルにインストールするとパスの設定がいらない
  $ npm install -g パッケージ名
  ```

### package.jsonの書き方
- [npmとpackage.jsonの使い方](https://qiita.com/righteous/items/e5448cb2e7e11ab7d477)
- [dependenciesの使い分け](https://qiita.com/cognitom/items/acc3ffcbca4c56cf2b95)
  - `--save-dev`や`--save`などの使い分け

```bash
# プロジェクトのディレクトリに移動
$ cd /path/to/project/dir

# package.jsonの初期化
$ npm init -y

# package.jsonにライブラリを書き込みつつ、ローカルにライブラリをインストール
$ npm install --save express
```

- `npm install <指定なし>`を実行するのは、Githubからcloneしてきたばかりでローカルにライブラリなどがインストされていない時などに行う
  - Dockerを使うときにもローカルでpackage.jsonを作って、コンテナにpackage.jsonを渡して`npm install`をする

### yarn
- npmと同じようにNode.jsのパッケージを管理するもの
- npmと同じくpackage.jsonで管理
- 速度が改善されており、速い

### TypeScript
- [TypeScriptの環境構築](https://qiita.com/ochiochi/items/efdaa0ae7d8c972c8103)
  - `npm install typescript`でpackage.jsonに追加しつつローカルにインストールできる
- [TypeScript+expressでrest](https://zenn.dev/tsuboi/articles/c679afd75be97b)
- [Typescript + Express + Webpack](https://qiita.com/isihigameKoudai/items/4b790b5b2256dec27d1f)
- [tsconfigの基礎](https://marsquai.com/a70497b9-805e-40a9-855d-1826345ca65f/1dc3824a-2ab9-471f-ad58-6226a37245ce/b5ce5f32-2afa-41f5-9fae-a3979f5c13df/)

### Webpack
- Webpack とは様々な形式のファイル、JavaScript や CSS、また png, jpeg などの画像ファイルなどをモジュールとして扱い、JavaScript ファイルにまとめる（bundleする）ためのツールでモジュールバンドラーとも呼ばれている
- Webpackを使わないと、CSSや画像をmetaタグでインポートする記述をHTML内で行わないといけないが、その必要がなくなり、該当するJSファイルだけを読み込めばよくなる
- まとめられたリソース、CSSや画像ファイルなどは、JavaScript からアクセスが可能になる
- ここを参考にすればわかる([Webpackの完全ガイド](https://qiita.com/soarflat/items/28bf799f7e0335b68186))
  - [消されたとき用](https://github.com/kshina76/centos-backup/blob/master/web_application/app_typescript/webpack/README.md)
- [webpackを使ったリソースへのアクセス](https://wk-partners.co.jp/homepage/blog/hpseisaku/javascript/typescript/)
- [webpackってどんなもの？](https://qiita.com/kamykn/items/45fb4690ace32216ca25)

```typescript
//Webpackを使うと、jsやts内からcssなどをimportするだけで扱えるようになる
import $ from "jquery";
import './style.css';
$(".hoge").addClass("active");
```

### swagger
- [swaggerをウェブ上で使える](https://editor.swagger.io)

### 4/9-4/12で準備に関するTODO
- [ ] node.jsとnpmの設定
  - https://qiita.com/nt_naito/items/972a40ee56a67f2a74cb
  - [既存のnpmを削除してnodebrewをインスト](https://nabewakashi.com/how-to-switch-to-nodebrew)
  - [macにNode.jsをインスト](https://qiita.com/kyosuke5_20/items/c5f68fc9d89b84c0df09)
  - [package.jsonの使い方](https://qiita.com/righteous/items/e5448cb2e7e11ab7d477)
  - [dockerでpackage.jsonを使ったNode.jsのパッケージ環境構築](https://qiita.com/niwasawa/items/9673d31ee2a6c532dc5b)
- [ ] macの設定
  - おすすめとかも調べつつ
  - vscode
  - homebrew
  - nodebrew
  - zsh
  - シェルの設定
  - ブラウザの設定
- [ ] いい感じのtodoアプリを調べる
- [ ] その他業務効率系のアプリを調べる
- [ ] 確定拠出年金を決定する
- [ ] 飲み会での話のネタ

<br></br>

## 実践

### 4/14,15での目標
- TypeScriptでのWebAPIの開発がどのように進むのかの雰囲気を掴むことが目標

### 調べること
- [ ] TypeScriptでWebAPIを開発していくにはどのような手順がベストプラクティスなのか
  - [ ] TypeScript + express + Webpack のディレクトリ構成
  - [ ] 構成のジェネレーターみたいなものがあるかどうか
- [ ] PythonでのWebAPIの開発と比べる
  - expressとaxiosを使っていたみたいなので、調べる
- [ ] データの受け渡しはDTOで行い、「Controller -> Service -> Data」の構成をinterfaceなどを使って疎結合に保ち、DIコンテナを使って依存注入を行う
- [ ] CDKを使ってTypeScriptでインフラの構成管理などを行う
- [ ] npm,npxを使ったパッケージ管理
- [ ] JavaScriptの書き方をザッとおさらい
  - 関数型の書き方とかよく使われているみたいかな？
- [ ] Node.jsの勉強と簡単なAPIを作る
  - [Node.jsとは](https://qiita.com/non_cal/items/a8fee0b7ad96e67713eb)
- [ ] typescriptを勉強
  - 関数型やオブジェクト指向なども確認
  - 基本文法はザッと。開発していれば嫌でも覚える
- [ ] expressを勉強とexpressで簡単なAPIを作る
  - [expressでAPI開発](https://qiita.com/k-penguin-sato/items/5d0db0116843396946bd)
- [ ] kotlinを勉強
- [ ] kotlinでandroidアプリのフロントエンドを開発
- [ ] kotlin+expressの連携をしてandroidアプリの完成


### 開発手順
- 主に以下にまとめてある
  - [WebAPI開発フロー](https://github.com/kshina76/centos-backup/tree/master/web_application/開発フローまとめ/WebAPI)
- 追加項目
  - swaggerでAPI定義をしてから実装に入る

### テーマ
- 今走っている周りの店舗のクーポン情報の一覧をナビから取得して表示
  - 不況の時は、クーポンとかディスカウントとかが流行る
- 店の予約や何かしらの予約を車のタッチパネルからササッと行えると便利そう
- 既存のモビリティ向けスマホアプリを車のandroidにのっけるだけで便利になりそう

### 気づいたこと
- システムアーキテクチャのところに、ディレクトリ構成とファイル構成を書いた図を用意しておくと、開発の最中にどこに何を書くか迷うことはなくなる気がする

<br></br>

## JavaScriptのフレームワークまとめ
- WebAPI開発に使うフレームワークを調べたかったら、「言語 REST API」でググると出てくる

### TODO
- BFFとはなにか調べる
- kotlinでandroidのクライアントサイドを開発する方法を調べる。フレームワークはないのか？とか
- モビリティの本を読んでテーマを考える
  - チームとしてはandroidのアプリを一気通貫で

### フロントエンドフレームワーク
- React.js
- vue.js
  - JavaScriptのフレームワーク
- Nuxt.js
  - vue.jsのフレームワーク
- Next.js
  - Reactをベースにしたフレームワーク
- Angular

### バックエンドフレームワーク
- express
  - Node上で動くフレームワーク
  - シェアナンバーワン
  - パフォーマンスが悪い
  - typescript対応
  - MVCフレームワーク
- koa.js
  - expressの後継となるもの
  - ジェネレーターやasync/awaitにも対応している
  - expressよりパフォーマンスが良い
- Fastify
  - パフォーマンスが一番良い
  - シェアが低い
- axios
  - WebAPIを開発するときに使われるフレームワーク
  - おそらくexpressがベースになっているっぽい
- 以下にかなり良くまとまっている
 https://www.wantedly.com/companies/company_3239475/post_articles/179467

### android開発のフレームワーク
