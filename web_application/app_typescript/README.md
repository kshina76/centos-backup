# TypeScriptでアプリ開発

## 勉強の仕方
1. 「環境構築の方法」を調べる
2. 「エコシステム」を調べる
3. 「フレームワーク」を調べる
4. youtubeで言語やフレームワークの基礎を学ぶ

## TODO
- ESLintとPrettierの設定
  - https://www.youtube.com/watch?v=R35LJL6a-p0
- interfaceとtype aliasの違い
  - https://www.youtube.com/watch?v=J2vox52T4W8
- ジェネリック型とポリモーフィズム
  - https://www.youtube.com/watch?v=5JYZzB7MMvo
- 関数の使い方
  - https://www.youtube.com/watch?v=obdbskaarVQ
- type aliasの使い方
  - https://www.youtube.com/watch?v=2DoYdw-rvL0
- 非同期処理の完了を待つ方法！Promise＆async/await
  - https://www.youtube.com/watch?v=Vhnz1V-v1cU
  - https://www.youtube.com/watch?v=7BCC4psJXqQ
- DOM
  - https://www.youtube.com/watch?v=dZyYqVOnrBg
- 即時関数
  - https://www.youtube.com/watch?v=1VyEfy03NTg
- 基本の型
  - https://www.youtube.com/watch?v=KQhyHHQrcic
- expressでAPI作成
  - 環境構築とhello world
    - https://www.youtube.com/watch?v=DrxcoMMgZKg
  - リソース設計とDB設計
    - https://www.youtube.com/watch?v=x4ZrmnqoS1Y
  - GET用APIのハンズオン開発
    - https://www.youtube.com/watch?v=dURpu7Bjr_Y
  - HTMLのフォームからAPIを実行しよう
    - https://www.youtube.com/watch?v=pRoIxvhFbow
  - CRUDなAPIを開発しよう
    - https://www.youtube.com/watch?v=GffwSIY_7xE
  - ユーザー作成フォームとAPIを繋げよう
    - https://www.youtube.com/watch?v=ye5hs_ZBhcM
  - ユーザーの編集と削除を操作しよう
    - https://www.youtube.com/watch?v=QO39f8Ztc1E
  - ステータスコードを使った適切なエラーハンドリング
    - https://www.youtube.com/watch?v=faCCTvt1_Ic
  - 実務レベルのAPI設計と実装
    - https://www.youtube.com/watch?v=agtHuqHrhKA
- API入門
  - https://www.youtube.com/watch?v=GbHWlUs9AoE

<br></br>

## 環境構築(フロントエンド)
- [ここを参考にして環境構築〜HelloWorld](https://www.youtube.com/watch?v=qSHlXcSces8)
### Homebrew
- Homebrew
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`: インスト
  - `brew --version`: バージョン確認
### Node.js
- nodebrew
  - `brew install nodebrew`: インスト
  - `nodebrew ls`: インストされているNode.jsの一覧
  - `nodebrew install stable`: 安定版のインスト
  - `nodebrew use <バージョン>`: Node.jsを有効にする
  - `node -v`: Node.jsのバージョン確認
  - `npm -v`: npmのバージョン確認(nodeを入れれば入る)
- docker
### TypeScript
- `mkdir <開発用ディレクトリ>`: 開発用ディレクトリの作成と移動もしておく
- `npm init`: npmの初期化
- `npm install --save-dev typescript ts-loader webpack webpack-cli webpack-dev-server`: 関連パッケージのインストール
  - 開発環境でしか使わないパッケージは、`save-dev`オプションをつける
- [webpack.config.jsの作成と設定](https://www.youtube.com/watch?v=qSHlXcSces8) の19:40~
- `tsc --init`: tsconfig.jsonの作成と設定
  - baseUrl
    - ベースのURLを指定すると、他のファイルをimportするときにわかりやすく指定できる
    - これを指定しないと相対パスで指定することになり、どのように指定すればいいかわかりにくくなる
    - tsconfing.jsonが置かれているところから相対パスで指定
    - `./src`と指定すると、srcディレクトリからの絶対パスを使えるようになる
  - allowJs
    - JSからTSに以降する時などに便利
  - jsx
    - Reactで使うjsxファイルの扱い
  - lib
    - JSの使うライブラリを明示的にする場合
    - 基本いじらなくて良い
  - outDir
    - TypeScriptをトランスパイルした時のJavaScriptのファイルをどこに吐き出すかの設定
    - `./dist`とかに吐き出すようにしておくと良い

  ![2021-04-11 0 28のイメージ](https://user-images.githubusercontent.com/53253817/114275275-dff55c80-9a5c-11eb-9fa0-b5cb2a24638f.jpg)

- ESLintとPrettierの設定
  - https://www.youtube.com/watch?v=R35LJL6a-p0

## 環境構築(バックエンド)
- [ここを参考にした](https://www.youtube.com/watch?v=DrxcoMMgZKg)
### 必要なライブラリ
- express, sqlite3
- body-parser
  - HTMLフォームから送信された値をパース
- node-dev
  - ファイル編集を検知してサーバ再起動（ホットリロード）
### 手順
- `mkdir <プロジェクトディレクトリ>`
- `npm init`
- `npm install --save express sqlite3 body-parser`
- `npm install -g node-dev`: なぜグローバル？？
- package.jsonの編集
  - `mkdir app`
  - `touch app.js`: WebAPIのサーバを起動するコードを書くところ
  - scriptsに記述する内容
    - `"start": "node-dev app/app.js"`: APIサーバを`npm run start`で立てられるように設定
    - `"connect": "sqlite3 app/db/database.sqlite3"`: データベースに`npm run connect`で接続できるように設定
- expressの雛形

  ```ts
  const express = require('express')
  const app = express()

  //expressのテンプレート雛形
  //URLが叩かれたら、Hello World!と返す
  app.get('/api/v1/hello', (req, res) => {
    res.json({"message": "Hello World!"})
  })

  //listenするポートの設定
  const port = process.env.PORT || 3000;
  app.listen(port)
  console.log("Liste on port: " + port)
  ```

<br></br>

## 準備
- [x] Docker
- [ ] JavaScript
  - [ ] インデントの扱い
  - [ ] 変数の命名規則
  - [x] letとvarの使い分け
  - [ ] セミコロンの有無
- [x] npm
  - [x] package.json
  - [x] nodebrew
  - [x] dockerでの構築
- [x] yarn
- [x] Node.js
  - [ ] Node.jsとブラウザのjsの違い
- [ ] Babel
- [ ] TypeScript
  - [ ] tsc
  - [ ] tsconfig.json
  - [x] ts-loader
  - [x] ts-node
  - [x] webpack
  - [x] gulp: タスクランナー
  - [ ] npm-scripts
  - [x] tsoa: コードからswaggerのドキュメントを生成するもの(とりあえず使わない)
  - [] node-dev
- [ ] axios: APIを叩くクライアント
- [ ] TSyringe: 軽量DIコンテナ
- [ ] Jest: JavaScriptのテストライブラリ
- [x] swagger: ブラウザ上で使えるAPIスキーム定義

### 全体的な流れ
- 新しくライブラリを使用する際
  - `npm init -y`: ライブラリをローカルにインストするための準備
  - `npm install <パッケージ>`: ローカルにライブラリをインスト
  - `import <名前> from <ライブラリ名>`: コード内でライブラリを使用
- タスクランナー
  - `package.json`の`scriptsオプション`にシェルスクリプトを書く
    - 予約語(test, build, start, restart, など)以外は、productionとして記述する
    - テストしたかったら`npm run test`
    - ビルドしたかったら`npm run build`
    - サーバを立てたかったら`npm run start`

      ```json
      {
        "scripts": {
          "test": "eslint *.js ./components/*.js ./example/*/*.js",
          "build": "webpack --mode=production",
          "start": "webpack-cli serve --mode development",
          "production": "NODE_ENV=production node app.js"
        }
      }
      ```
  
  - あとは、`npm run test`や`npm run build`や`npm run start`を使って実行して開発を進めていくイメージ
- モジュールビルダー
  - webpack, webpack-cliを使用する

- tsconfigの設定

  ![2021-04-11 0 28のイメージ](https://user-images.githubusercontent.com/53253817/114275275-dff55c80-9a5c-11eb-9fa0-b5cb2a24638f.jpg)

- package.jsonの設定

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
- [Node.jsとブラウザのjsの違い](https://www.hypertextcandy.com/modern-javascript)
  - 環境特有の機能が追加されているかどうかの違い。言語仕様は同じ
    - ブラウザでいうと、DOMを操作するgetElementByIdや、音声や動画を再生する機能など。これらの機能は、ブラウザ上で実行するからこそ必要な機能。
    - サーバーでいうと、サーバー内のファイルの読み込み機能などが特徴的。ブラウザの実行環境には、セキュリティ上の理由からユーザーのコンピュータ内のファイルを読み込む機能はない

  <img width="722" alt="fig-node-01" src="https://user-images.githubusercontent.com/53253817/114272546-918e9080-9a51-11eb-978d-80eaf3cb0840.png">


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

<img width="620" alt="fig-npm-01" src="https://user-images.githubusercontent.com/53253817/114272598-c7cc1000-9a51-11eb-8fe4-d07ebe36319b.png">

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
- `--save-dev`は、開発環境でしか使わないパッケージをインストする場合に使う
- package.jsonには、開発中にターミナルで使う面倒なコマンドなどを登録してしまえば良いみたい
  - データベースへの接続
  - コンパイル系
  - DBマイグレーション
  - サーバ起動
  - など

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

### Babel
- ある構文の JavaScript を、別の構文の JavaScript に変換するツール
  - IEなどポンコツなブラウザでも動くようにES2015(ES6)以降の構文をあえて古い物に変換するための物
- TypeScriptのtsconfigで設定すれば、古いJavaScriptに変換できるからBabelはいらないのでは？？

<img width="658" alt="fig-babel-01" src="https://user-images.githubusercontent.com/53253817/114272662-f944db80-9a51-11eb-906d-1bfd55ce87bb.png">

### TypeScript
- なぜTypeScriptを使用するのか？
  - ドキュメントとしての側面を利用するため
    - 型の情報がコードに明示されていることで、わかりやすい
    - vscodeなどで、functionやclassの上で`cmd+クリック`をすると、定義にジャンプできるが、その際に型の情報があるとコードが読みやすいという側面がある
    - チームで開発をするときに定義にジャンプする際に、そのコードの挙動がわかりやすい
  - Linterとしての側面を利用するため
    - 型情報があることで、間違った書き方をしたときに教えてくれる
  - ES5へのコンパイラとしての側面を利用するため
    - ブラウザによってES6に対応していないものもあるので、ES3やES5のコードに変換されるようになっている
- [TypeScriptの環境構築](https://qiita.com/ochiochi/items/efdaa0ae7d8c972c8103)
  - `npm install typescript`でpackage.jsonに追加しつつローカルにインストールできる
- [TypeScriptの最低限の環境構築](https://blog.tilfin.net/2019/04/19/introduce-typescript-for-nodejs-app/)
- [TypeScript+expressでrest](https://zenn.dev/tsuboi/articles/c679afd75be97b)
- [Typescript + Express + Webpack](https://qiita.com/isihigameKoudai/items/4b790b5b2256dec27d1f)
- [tsconfigの基礎](https://marsquai.com/a70497b9-805e-40a9-855d-1826345ca65f/1dc3824a-2ab9-471f-ad58-6226a37245ce/b5ce5f32-2afa-41f5-9fae-a3979f5c13df/)

### tsc
- TypeScriptをJavaScriptにトランスパイルするコマンド
  - `tsc <test.ts>`を実行すると、`test.js`ファイルが作成される
  - そのあとは`node <test.js>`を実行するとプログラムが走る
- 型や使い方が間違っていたときには、tscコマンドでトランスパイルしたときに

### ts-loader
- webpackと連動して、バンドルする前にTypeScriptコンパイラを起動する。コンパイルでTSをJSにした後に、webpackが起動してバンドルするという流れ

### ts-node
- TypeScriptをJavaScriptに手動でトランスパイルをしなくても、そのまま実行できるようにするもの
- ts-loaderとの違いとしては、こちらのts-nodeはサーバサイド用で、ts-loaderはクライアントサイドといった感じかな？
- [ts-node で TypeScript + node をサクッと実行する](https://qiita.com/mangano-ito/items/75e65071c9c482ddc335)

### node-dev
- ファイル編集を検知してサーバを再起動

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

### webpack-cli
- コマンドラインでwebpackを使う

### webpack-dev-server
- 開発環境で使うもの
- 開発環境でwebpackのビルド, 開発用webサーバの起動, ホットリロード(ファイル保存時などに、ファイル変更の自動検知と再読み込み)

### gulp
- Sassを編集すればコンパイルを実行し、画像を編集すれば画像を圧縮するというように多くの手間がかかる作業を自動化するもの
- Sassは現在rubyをインストして使う人は少なく、Node.jsとgulpで使うのがほとんどらしい
- いまどきは、npm-scriptsの方を使う
- [gulpの解説1](https://www.codegrid.net/articles/2014-gulp-1/)
- [gulpの解説2](https://ics.media/entry/3290/)

```javascript
var gulp = require('gulp');

gulp.task('hello', function() {
  console.log('Hello gulp!');
});

gulp.task('default', ['hello']);

/*
「Hello gulp!」が実行された後に、「hello」が実行されるといった感じでパイプ処理されていく
実践的には、sassに変更があるかを監視して、変更があったら自動でコンパイルをして、該当するディレクトリにコンパイル後のファイルを吐き出すといった処理をする
*/
```

### npm-scripts
- いまどきはのタスクランナーはgulpではなくて、npm-scriptsを使う
  - [脱gulp](https://hibi-update.org/javascript/npm-scripts/#Frontend_Developer_Roadmap_2020)
  - [npm-scriptsを使ってみる](https://qiita.com/tminasen/items/986feac7150ed74e13d8)
- 手順や動作
  - `package.json`の`scriptsオプション`にシェルスクリプトを書く
    - 予約語(test, build, start, restart, など)以外は、productionとして記述する
    - テストしたかったら`npm run test`
    - ビルドしたかったら`npm run build`
    - サーバを立てたかったら`npm run start`

      ```json
      {
        "scripts": {
          "test": "eslint *.js ./components/*.js ./example/*/*.js",
          "build": "webpack --mode=production",
          "start": "webpack-cli serve --mode development",
          "production": "NODE_ENV=production node app.js"
        }
      }
      ```
  
  - あとは、`npm run test`や`npm run build`や`npm run start`を使って実行して開発を進めていくイメージ

- 直列実行
  - 2つのscriptsを直列実行したいときは、`run-s {コマンド1} {コマンド2}`でコマンド1の結果を待ってコマンド2を実行できる。
  - 例えばビルドして結果をどこかにコピーしたいとき。
  
  ```json
  "script": {
    "all": "run-s build copy"
    , "build": "ng build"
    , "copy": "cpx ./dist/* ../server/"
  }
  ```

- 並列実行
  - 2つの複数のスクリプトを走らせたいときは、`run-p {コマンド1} {コマンド2}`でコマンド1と2を同時に実行できる。
  - パッと用途が思いつかなかった。下記例だと、2種類のビルドを同時に実行している。

  ```json
  "script": {
    "parallel": "run-p build:tsc build:angular"
    , "build:tsc": "tsc test.ts"
    , "build:angular": "ng build"
  }
  ```

- 監視
  - ファイルの変更検知して自動でビルドしたいときは、`npm run watch {コマンド} {監視対象}`で監視対象の変更を検知してコマンドを実行できる。
  - 使い方としては、開発中にホットデプロイのようなことをしたい場合。
  - ローカルで開発中にいちいちビルドと再起動を行わなくて済むので便利。
  - 下記例はビルドからサーバにファイルを配置、サーバを起動ということをしている。

  ```json
  "script": {
    "watch": "watch \"npm run start:app\" ./src",
    "start:app": "run-s build boot:server",
    "boot:server": "nodemon ./app.js",
    "build": "run-s build:app copy",
    "build:app": "ng build",
    "copy": "cpx ./dist ../server/"
  }
  ```

- 予約語
  - `start`, `stop`, `restart`, `test`
- 個人的に使いたい命名
  - `build`: コンパイルとかのビルド作業
  - `clean`: 環境を綺麗にする作業。rmコマンドとか仕込むと良さそう

### swagger
- APIの定義をyamlで記述してドキュメントとして作成できるもの。これに沿って実装していくことになる
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
  - [ ] vscode
    - [ ] dockerのリモートコンテナ
    - [ ] codeコマンド
    - [ ] prettierの使い方
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
  - [ ] 基本文法はザッと。開発していれば嫌でも覚える
    - [ ] インデントの扱い
    - [ ] 変数の命名規則
    - [ ] letとvarとconstの使い分け
    - [ ] セミコロンの有無
    - [ ] コールバック関数とアノテーションに関して
    - [ ] unknown型
    - [ ] export defaultの意味
    - [ ] オプション引数の扱い
  - [ ] [tsconfig,webpackの使い方](https://www.youtube.com/watch?v=qSHlXcSces8)
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

<br></br>

## TypeScriptメモ
- [ここを参考に勉強した](https://www.youtube.com/watch?v=F9vzRz6jyRk)
  - tsconfigに関しては、2:30:30~
- [いまどきのJavaScriptの書き方1](https://qiita.com/shibukawa/items/19ab5c381bbb2e09d0d9)
- [いまどきのJavaScriptの書き方2](https://dev.classmethod.jp/articles/2020-javascript/)
- 「アノテーション」と「型推論」の使い分け
  - 「アノテーション」は型推論がうまくされないとき
    - タプルを使うときなど
  - 「型推論」を基本的に使用する
- var,let,constの使い分け
  - varは使わない
  - とりあえずconstを使う
  - 上書きが必要なところはletを使う
    - for文とか

### 基本の型
- オブジェクト
  - 構造体のことかな

  ```ts
  const person = {
    name: {
      first: 'Jack',
      last: 'Smith'
    },
    age: 21
  }

  // アクセスするには、person.name.first のようにする
  ```

- 配列

  ```ts
  //アノテーションする場合
  const fruit: string[] = ['Apple', 'Banana', 'Grape'];
  ```

- タプル
  - タプルはアノテーションしないとダメ
  - 第一引数はstring、第二引数はnumber、...のように決めたい場合にタプルを使う

  ```ts
  //アノテーションする場合
  const book: [string, number, boolean] = ['businnes', 1500, false];
  ```

- enum
  - 列挙型

  ```ts
  enum CoffeSize {
    SHORT = 'SHORT',
    TALL = 'TALL',
    GRANDE = 'GRANDE',
    VENTI = 'VENTI'
  }

  //イコールで明示的に書かない場合は、上から0,1,2,...と代入される
  enum CoffeSize {
    SHORT,
    TALL,
    GRANDE,
    VENTI
  }

  ```

- any型
  - なんでも代入できる型
  - 基本的に使わない

- union型
  - 型における「or」の役割

  ```ts
  //number型かstring型のどちらかを代入できる
  let unionType: number | string = 10
  //number型かsting型を代入できる配列
  let unionTypes: (number | string)[] = [21, 'hello']
  ```

- リテラル型
  - 定数

  ```ts
  //アノテーションする場合
  const apple = 'apple';
  const clothSize: 'small' | 'medium' | 'large' = 'large';
  ```

- タイプエイリアス
  - 別名をつける

- 関数
  - 関数を簡易に書けるようにしたものが無名関数
  - 無名関数を簡易に書けるようにしたものがアロー関数

  ```ts
  //関数の場合は、引数と返り値にアノテーションした方が良い
  function add(num1: number, num2: number): number {
    return num1 + num2
  }

  //voidの場合。undifiendというものもあるが、基本的にはvoidで
  function sayHello(): void {
    console.log('Hello');
  }

  //関数自体を変数に代入する方法
  //アノテーションする際に、「:」を2回使うのは変なので、返り値に限って「=>」というものを使用する
  //引数のアノテーションは「()」の中に書く
  const anotherAdd: (n1: number, n2: number) => number = add

  //無名関数
  const anotherAdd: (n1: number, n2: number) => number = function(num1: number, num2: number): number {
    return num1 + num2;
  }
  //無名関数における型推論
  const anotherAdd: (n1: number, n2: number) => number = function(num1, num2){
    return num1 + num2
  }

  //アロー関数でのアノテーション方法1
  const doubleNumber = (num: number): number => num * 2;
  //アロー関数でのアノテーション方法2
  const doubeleNumber: (num: number) => number = num => num * 2;
  ```

- unknown型
  - anyより少し厳しい型

  ```ts
  let unknownInput: unknown;
  ```

- never型
  - 決して何も返さないもの

  ```ts
  //エラーを投げるときは返り値がneverになっている
  function error(message: string): never {
    throw new Error(message);
  }
  ```

### class
- 昔はprototypeを使って表現していたが、今は必ずclassを使う

  ```ts
  class SmallAnimal extends Parent {
    constructor() {
      this.animalType = "ポメラニアン";
    }

    say() {
      console.log(`${this.animalType}だけどMSの中に永らく居たBOM信者の全身の毛をむしりたい`);
    }
  }
  ```

- 抽象クラス
- protected, public, private, export, readonly

- [オブジェクト指向は「モデル化すること」と考えると良いかも](https://www.youtube.com/watch?v=7u8o1r0LkHU)

  ![2021-04-10 22 33のイメージ](https://user-images.githubusercontent.com/53253817/114271550-e5e34180-9a4c-11eb-89c4-058687988131.jpg)

### interfaceとtype aliasの違い
- https://www.youtube.com/watch?v=J2vox52T4W8

### ジェネリック型とポリモーフィズム
- https://www.youtube.com/watch?v=5JYZzB7MMvo

### いまどきはアロー関数のみ

```ts
//古い関数定義
function name(引数) {
    本体
}

//いまどきの関数定義
const name = (引数) => {
  本体;
}
```

### 即時関数を排除する
- なぜ即時関数というものがあるのか？
- [即時関数を排除する](https://qiita.com/raccy/items/310b4353a757296f797f)

### 非同期処理
- コールバック関数
- promise
- async/await
- [ここを参照](https://qiita.com/shibukawa/items/19ab5c381bbb2e09d0d9#非同期処理)

### 繰り返し処理
- for
  - 今は使わないらしい
- for..of
  - 現在はこれを使う
  - pythonのfor..inと同じ

  ```ts
  let array = [1,2,3,4,5];

  for (let val of array) {
    console.log(val);  // 1,2,3,4,5
  }
  ```

- for..in
  - for..ofのインデックスを使うバージョン

### コンパイラをカスタマイズ(tsconfig)

- tsconfig.json
  - typescriptの設定ファイルのこと
  - `tsc --init`でtsconfig.jsonの作成
  - tsconfig.jsonを参照して実行したい場合は`tsc <オプション>`という使い方になる
    - 逆にtsconfig.jsonに沿って実行したくない場合は`tsc <指定ファイル> <オプション>`のように明示的にファイルを指定する

- watchモード
  - `tsc index.ts --watch`で起動
  - `tsc --watch`で全てのtsファイルをwatchモード対象にできる
  - ターミナル上にエラーをリアルタイムに表示してくれる

- 一気にコンパイルする方法
  - `tsc --init`で設定ファイルを作る
  - `tsc`で一気にコンパイルできる

- exclude
  - コンパイルから外したものを設定する
  - デフォルトだと`node_modules`ディレクトリは外されている
    - `node_modules`はライブラリのコードとか
  - 上書きした場合は`node_modules`を必ず加えること

- include
  - コンパイル対象にするものを設定する
  - デフォルトだと全てになっている
  - includeして、excludeされたものがコンパイル対象になる

- compilerOptions
  - target
    - どのバージョンのJSにトランスパイルするかの設定
  - lib
    - 型の定義ファイルを指定するもの
    - とりあえずコメントアウトしておけば良さそう
    - `ES6`: toUpperCaseなどのライブラリが定義されているもの
    - `DOM`: console.logなどのライブラリが定義されているもの
  - allowJs
    - JavaScriptのファイルもコンパイル対象に含める

<br></br>

## WebAPI開発
- [参考リポジトリ](https://github.com/kshina76/centos-backup/tree/master/web_application/app_typescript/とらゼミ/basic-rest-api)
- sqlite3の使い方を調べる
- データベースのロック、トランザクションを調べる
  - 「webを支える技術」の16章くらいに書いてある
- asyncとawaitの使いどころ
  - 参考コードで、postのときにasyncやawaitを使っていたので
- promiseの使い方
  - promiseとasyncとawaitを一緒に使っているけど、どういうことだ？

### リソース指向アーキテクチャ(APIを開発するフロー)
1. Webサービスで利用するデータを特定する
  - ユーザ情報(例): ユーザID、ユーザ名、プロフィール、写真、誕生日、...etc
  - フォロー情報(例): フォロワーID、フォローID、...etc
  - など
2. リソース設計(1を分類していく)
  - ユーザリソース
  - 検索結果リソース

3. DB設計
  - どのようなDB設計でも`created_at`と`updated_at`はほとんどの場合使うので、not nullでとりあえず設計に入れておく

  ![2021-04-11 10 33のイメージ](https://user-images.githubusercontent.com/53253817/114289246-54f28180-9ab1-11eb-897e-fabe13e73ab8.jpg)

4. URI設計

  ![2021-04-11 11 59のイメージ](https://user-images.githubusercontent.com/53253817/114290835-545fe800-9abd-11eb-8256-4d1ef2a14c9a.jpg)

5. リソースの表現を設計
  - json、XML、HTML、などどれなのか
  - jsonならkeyとvalueを設計する

  ![2021-04-11 12 00のイメージ](https://user-images.githubusercontent.com/53253817/114291017-f207e700-9abe-11eb-9a0e-84f8f67a3061.jpg)

  ![2021-04-11 12 00のイメージ (1)](https://user-images.githubusercontent.com/53253817/114291018-f3391400-9abe-11eb-8504-2277475fbfd5.jpg)

  ![2021-04-11 12 11のイメージ](https://user-images.githubusercontent.com/53253817/114291026-077d1100-9abf-11eb-942c-900f587c3bdc.jpg)


6. リンクとフォームでリソースを結びつける
  - ユーザがAPIにどのようにアクセスするかを設計する。ということかな
7. イベントの標準的なコースを設計
  - ユーザがAPIにアクセスした後に、どのような流れで処理されるかの設計かな
8. エラーを想定
  - エラーコードを設計

![2021-04-11 10 20のイメージ](https://user-images.githubusercontent.com/53253817/114289012-81a59980-9aaf-11eb-9ba8-6e20592f9a9c.jpg)

### 開発メモ
- Pythonのデコレータで`get`とか`post`を定義する感じで、TypeScriptでも`app.get(<URI>, <処理>)`のように書き並べていく
- Pythonと同じように、TypeScriptにもresとreqというオブジェクトに「ヘッダーやステータスコード」のフィールドが入る
- どちらの言語でも、`get`や`post`などの処理の初めにDB接続の処理を書いて、処理の終わりにDBクローズする処理を書いている
  
  ```ts
  //DB接続
  const db = new sqlite3.Database(dbPath)

  //DBクローズ
  db.close()
  ```

- JavaScriptのライブラリの慣習として最後の引数で、ライブラリからの返り値を引数としたアロー関数を渡している
  - 例えば、サーバとのやりとりがあるときには、第二引数に「リクエストとレスポンスを引数とするアロー関数」を書いて、リクエストとレスポンスの値を受け取る
  - DBのやりとりがあるときには、第二引数にDBからの返り値である、「errとrow」が引数のアロー関数を渡している

  ```ts
  //APIサーバのリクエスト、レスポンス
  app.get('/api/v1/users/:id', (req, res) => {
    const db = new sqlite3.Database(dbPath)
    const id = req.params.id

    db.get(`SELECT * FROM users WHERE id = ${id}`, (err, row) => {
      if (!row) {
        res.status(404).send({ error: "Not Found!" })
      } else {
        res.status(200).json(row)
      }
    })

    db.close()
  })

  //DBサーバのリクエスト、レスポンス
  db.get(`SELECT * FROM users WHERE id = ${id}`, (err, row) => {
    if (!row) {
      res.status(404).send({ error: "Not Found!" })
    } else {
      res.status(200).json(row)
    }
  })

  //sqlite3の基本メソッド
  db.all(sql, (err, rows))  //全ての結果を一度に取得
  db.get(sql, (err, row))  //1つだけ結果を取得
  db.run(sql, (err))  //SQLクエリを実行
  ```

- sqlite3の基本メソッド

  ![2021-04-11 12 18のイメージ](https://user-images.githubusercontent.com/53253817/114291145-0ac4cc80-9ac0-11eb-994e-baba30a7b482.jpg)
