# TypeScriptでアプリ開発

## 準備
- [ ] Docker
- [ ] JavaScript
- [ ] npm
  - [ ] package.json
  - [ ] nodebrew
  - [ ] dockerでの構築
- [x] yarn
- [ ] Node.js
- [ ] TypeScript
- [ ] axios: WebAPI開発
- [ ] TSyringe: 軽量DIコンテナ
- [ ] swagger: ブラウザ上で使えるAPIスキーム定義

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

### npm
- Node.jsのパッケージを管理するもの
- package.jsonでプロジェクト毎にパッケージを管理することができる
  - Pythonでいうrequirmentsみたいなものかな
- [グローバルインストールは避ける](https://mosapride.com/index.php/2018/02/06/post-681/)
- [既存のnpmを削除してnodebrewをインスト](https://nabewakashi.com/how-to-switch-to-nodebrew)
- [package.jsonの使い方](https://qiita.com/righteous/items/e5448cb2e7e11ab7d477)
- [dockerでpackage.jsonを使ったNode.jsのパッケージ環境構築](https://qiita.com/niwasawa/items/9673d31ee2a6c532dc5b)

### yarn
- npmと同じようにNode.jsのパッケージを管理するもの
- npmと同じくpackage.jsonで管理
- 速度が改善されており、速い

## 4/9-4/12のTODO
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
  - zsh
  - シェルの設定
  - ブラウザの設定
- [ ] いい感じのtodoアプリを調べる
- [ ] その他業務効率系のアプリを調べる
- [ ] 確定拠出年金を決定する
- [ ] 飲み会での話のネタ

## 4/14,15でやること
- TypeScriptでのWebAPIの開発がどのように進むのかの雰囲気を掴むことが目標

## 調べること
- [ ] TypeScriptでWebAPIを開発していくにはどのような手順がベストプラクティスなのか
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
- [ ] kotlinを勉強
- [ ] kotlinでandroidアプリのフロントエンドを開発
- [ ] kotlin+expressの連携をしてandroidアプリの完成

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

## 開発手順
- 主に以下にまとめてある
  - [WebAPI開発フロー](https://github.com/kshina76/centos-backup/tree/master/web_application/開発フローまとめ/WebAPI)
- 追加項目
  - swaggerでAPI定義をしてから実装に入る

## テーマ
- 今走っている周りの店舗のクーポン情報の一覧をナビから取得して表示
  - 不況の時は、クーポンとかディスカウントとかが流行る
- 店の予約や何かしらの予約を車のタッチパネルからササッと行えると便利そう
- 既存のモビリティ向けスマホアプリを車のandroidにのっけるだけで便利になりそう


<br></br>

## TODO
- BFFとはなにか調べる
- kotlinでandroidのクライアントサイドを開発する方法を調べる。フレームワークはないのか？とか
- モビリティの本を読んでテーマを考える
  - チームとしてはandroidのアプリを一気通貫で

## フロントエンドフレームワーク
- React.js
- vue.js
  - JavaScriptのフレームワーク
- Nuxt.js
  - vue.jsのフレームワーク
- Next.js
  - Reactをベースにしたフレームワーク
- Angular

## バックエンドフレームワーク
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

## android開発のフレームワーク
