# express実践入門

## はじめに

あくまで「俺が考える最強のexpress実践入門」です。  

初学者がexpressを攻略する上でのつまづくポイントと、中規模開発をターゲットにしたベストプラクティスを経験ベースでお話します。  

おそらく、初〜中級者向けの内容です。

---

##  本コンテンツの使い方

- express初心者
  - 初学者向けチュートリアル(dotinstallとか)のあとに
- express経験者
  - ご自身のコードの見直しに
- 他の言語の経験者
  - 他の言語の「あれ」は、node.jsでは「これ」のマッピングに

(※)中で紹介するコードは抜粋したものであり、そのままでは動作しない場合があります。ご注意ください。  
(※)versionはnode v4.2.0, express v4.13.1です。

---
# expressの(超)概要

expressとはなにか？expressの初め方について

---
## express

**Fast, unopinionated, minimalist web framework for Node.js**

- Fast - 高速
- unopinionated - オープン
- minimalist - 軽量

Node.jsのための、高速で軽量でオープンなWebフレームワーク。

---
## Why express??

- ほぼデファクトの地位
- 豊富な情報量、サンプル
- 豊富な拡張機能（middleware）
- Pure node.jsで作成した場合、アプリを仕上げていく過程で「`そもそもexpressで良かったのでは？`」となることが多かった（経験談）

(※)ただし、3系と4系の違いに注意。世の中のサンプルは3系で書かれているものが多く、動作しないことがある。

他のWebフレームワーク

- [hapi.js - A rich framework for building applications and services](http://hapijs.com/)
- [Koa - next generation web framework for node.js](http://koajs.com/#)

---
## Install 

Node.jsをインストールして、、、  
ほぼ一発。
```
mkdir myapp && myapp
npm init
npm install express
```

---
## Hello world

サーバー側のコード（app.js）
```js
var express = require('express');
var app = express();

// HTTPリクエストを受け取る部分
app.get('/', function (req, res) {
  res.send('Hello World!');
});

// サーバーを起動する部分
var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Example app listening at http://%s:%s', host, port);
});
```

サーバーを起動して、`http://localhost:3000`にアクセス
```
node app.js
curl http://localhost:3000 -> Hello World!
```

---
## express-generator

通常はこちらの方をよく使います。[Express application generator](http://expressjs.com/starter/generator.html)
```
(sudo)npm install express-generator -g

// expressコマンドでアプリのひな形を生成します
express myapp

   create : myapp
   create : myapp/package.json
   create : myapp/app.js
   ...
   create : myapp/bin
   create : myapp/bin/www
   
cd myapp 
// 依存モジュールをインストールします
npm install
// サーバーを起動します
node bin/www // or npm run start 
```

---

## express-generatorプロジェクト構成

基本最小構成。後ほどオレ色に染め上げて行きます。
```
.
├── app.js				// expressサーバーの設定
├── bin
│   └── www				// サーバーの起動
├── package.json
├── public				// 静的ファイル置き場
│   ├── images
│   ├── javascripts
│   └── stylesheets
│       └── style.css
├── routes				// サーバー側のコントローラ
│   ├── index.js
│   └── users.js
└── views					// サーバー側で画面を作成する際のテンプレート
    ├── error.jade
    ├── index.jade
    └── layout.jade
```

---
# express攻略

expressのここを理解すればOK！

---
## express攻略の勘所

expressを理解する上での最小構成要素。

- routing
- middleware

以上2つ

---
## expressの仕組み

![](https://cloud.githubusercontent.com/assets/1703219/10810648/6b7c795c-7e46-11e5-8ef8-7d406c68607c.jpg)

- routing
  - 外部からのHTTP(S)リクエストに対して、内部のロジックをマッピングすること。
- middleware
  - routingの過程で何らかの処理を差し込む仕組み。
  - 共通処理(認証、エラーハンドリング、リクエストデータの加工、etc)を本来のロジックから分離して、コードベースを健全に保つ。

---
## routing(1/2)
### 基本（Route paths, method, handler）
HTTPメソッド、Path、マッピングする内部ロジックを指定する方式。
```js
var app = express();

// GET http://localhost:3000/
app.get('/', (req, res) => {});

// POST http://localhost:3000/books
app.post('/books', (req, res) => {});

// PUT http://localhost:3000/books/1
app.put('/books/:id', (req, res) => {});

// DELETE http://localhost:3000/books/1
app.delete('/books/:id', (req, res) => {});
```

---
## routing(2/2)
### 基本（express.Router）

routing用のmiddlewareを作る仕組み。  routing部分をモジュール化（別ファイル化）することが多いため、こちらの方をよく利用します。

routingをモジュール化（router.js）
```js
var app = express();
var router = express.Router();

router.get('/:id', (req, res) => {
	// 何かの処理
});

module.exports = router;
```

モジュールを利用する。（app.js）
```
var router = require('./router');
...
app.use('/books', router); 
```
「http://localhost:3000/books/1」のroutingが有効になる

---
## routing(Request method)
よく利用するもの

```js
router.get('/', (req, res) => {
	// 何かの処理
});
```
- req.body
	- request bodyのkey-valueペア(body-parser middlewareが必要)
- req.cookies
	- cookieのkey-valueペア(cookie-parser middlewareが必要)
- req.params
	- `/books/:id`で`/books/1`の場合`req.params.id` => 1
	- url pathパラメータのkey-valueペア
- req.query
	- `/books?order=asc`の場合`req.query.order` => asc
	- リクエストパラメータのkey-valueペア
- req.get
	- HTTPヘッダーの値を取得する
- req.session
	- セッションのkey-valueペア(express-session middlewareが必要)

---
## routing(Response method)
よく利用するもの

```js
router.get('/', (req, res) => {
	// 何かの処理
});
```
- res.cookie
	- cookieを付与
- res.set
	- HTTPヘッダーを付与
- res.redirect
	- 指定したPathへリダイレクト
- res.render
	- テンプレートエンジンを利用して画面を生成して返却
- res.sendStatus
	- ステータスコードを返却(401, 404, 500, etc...)
	- ex) `res.sendStatus(401).json({...})`
- res.json
	- jsonを返却(200)

---
## middleware(基本)

middlewareのhandler(実体)の基本I/Fの形
(ただし、エラーハンドラを除く)

```
function(req, res, next) {
  // middlewareの処理
  next();
}
```
middlewareは1つのroutingに対して複数連結して処理されるため、次のmiddlewareへ移動するために`next`を利用する。  
middlewareの実行順序は宣言したもの順。エラーハンドラが最後にあるのは、それなりの理由がある。

middlewareは3種類ある

- Application-level
- Router-level
- Error-handling

---
## middleware(Application-level)
### Application-level
```js
var app = express();

// '/'に対するmiddleware
app.use(function (req, res, next) {
  next();
});

// 'GET books/:id'に対するmiddleware
app.get('books/:id', function (req, res, next) {
  next();
});
```

---
## middleware(Router-level)
### Router-level
```js
var router = express.Router();

// '/'に対するmiddleware
router.use(function (req, res, next) {
  next();
});

// 'GET books/:id'に対するmiddleware
router.get('books/:id', function (req, res, next) {
  next();
});
```
---
## middleware(TPO)
Application-level middlewareとRouter-level middlewareの違いについて、利用者レベルでは正直良くわからない。

使い分け方針(TPO)

- アプリ全体
	- Application-level middleware
	- `app.use()`
- 特定のrouting
	- Router-level middleware
	- `router.get('/:id', someMiddleware, businessLogic)`

---
## middleware(Error-handling)
### Error-handling

（後述）  エラーハンドリングの部分で紹介します。

---
# express開発のベストプラクティス

中規模Webアプリケーションを構築するために必要な要素とは

- アプリケーションのレイヤー化
	- プロジェクトストラクチャ
	- テンプレートエンジン
	- ORM
- 共通処理
	- エラーハンドリング、認証、ロギング、セッション、設定情報
- デリバリー
	- デプロイ(Heroku)

---
## プロジェクトストラクチャ(1/4)
### 概要
railsに似せた構成が好み。  
正直好みの問題です、悩みたくないならこれを使ってください(経験談)

```
app/                       // アプリケーション本体
  api/                    // REST APIのコントローラ
  controllers/            // 画面のコントローラ
  models/                 // Entiry
  repositories/           // DAO(CRUD部品)
  views/                  // 画面のテンプレート
bin/                        // サーバー起動
config/                   // アプリケーションの設定系
  environment/            // 環境定義
  middlewares/            // middlewareの置き場
  passport/               // 認証系のstrategyの置き場
  express.js              // express本体の設定
  router.js       // トップレベルのルーティング設定
  ...js         // 何かの共通設定系
public/           // 静的リソースの置き場(js, css)
util/             // ユーティリティ
package.json
bower.json
```

---
## プロジェクトストラクチャ(2/4)
### アプリケーション本体
REST APIと画面コントローラーの置き場所は毎回悩む(経験談)
```
app/                       // アプリケーション本体
  api/                    // REST APIのコントローラ
    users/
      index.js            // /users配下のルーティング設定
      user.controller.js  //
  controllers/            // 画面のコントローラ
    users/
      index.js            // user画面のactionのルーティング
      user.controller.js  // user画面のコントローラ
  models/                 // Entiry
    user.model.js
  repositories/           // DAO(CRUD部品)
    user.repository.js
  views/                  // 画面のテンプレート
    layout.jade           // 共通テンプレート
    user.jade
bin/
config/                   
public/
```

---
## プロジェクトストラクチャ(3/4)
### アプリケーション設定
設定系は小分けにする方が取り回しが良くていい。テストも楽(経験談)
```
app/                       
bin/
  www                      // サーバー起動
config/
  environment/             // 環境設定
    .env.development
  middlewares/             // middleware置き場
    authorization.js
    errorHandler.js
  passport/                // passportのstrategy置き場
	local.js
	twitter.js
  db.js                     // DB関連の設定(接続先など)
  passport.js               // 認証(passport)の設定
  express.js                // expressサーバー本体の設定
  router.js                 // トップレベルのルーティング     
public/
```

---
## プロジェクトストラクチャ(4/4)
### 静的リソース

あくまで最小構成。ViewをSPA(Single page application)にする場合は、最初からMEAN Stackを利用した方がいい(経験談)

```
app/
bin/
config/ 
public/
  bower_modules/
  javascripts/
  stylesheets/
package.json
```

MEAN Stack)

- [DaftMonk/generator-angular-fullstack](https://github.com/DaftMonk/generator-angular-fullstack)
- [MEAN - Full-Stack JavaScript Using MongoDB, Express, AngularJS, and Node.js.](http://mean.io/#!/)


---
## テンプレートエンジン

  - [Jade - Template Engine](http://jade-lang.com/)
  - [EJS - JavaScript Templates](http://www.embeddedjs.com/)
  - Javascriptのテンプレートエンジン
	  - [Handlebars.js: Minimal Templating on Steroids](http://handlebarsjs.com/)
	  - [Hogan.js](http://twitter.github.io/hogan.js/)

特にこだわりなければ、`Jade`にしておくのが最も平和(経験談)

app.js
```js
// テンプレートが格納されているフォルダを指定する
app.set('views', path.join(__dirname, '../app/views'));

// expressで利用するテンプレートエンジンを指定する
app.set('view engine', 'jade');
```

---
## テンプレートエンジン(QA)

Q：どうしても使い慣れたHandlebarsが使いたいです  
A：
Handlebarsはexpress内部のテンプレートエンジン処理のI/Fと異なるため、[consolidate.js](https://github.com/tj/consolidate.js)でHandlebarsをラップする必要がある。  
(他のJavascriptテンプレートエンジンを利用する場合も同様)

自信がない人は近づかない方がいい(経験談)

---
## ORM

ORM(Object-relational mapping)この2つでOK

  - [Mongoose - elegant mongodb object modeling for node.js](http://mongoosejs.com/)
	  - MongoDBならこれ
  - [Sequelize | The Node.js / io.js ORM for PostgreSQL, MySQL, SQLite and MSSQL](http://docs.sequelizejs.com/en/latest/)
	  - PostgreSQL, MySQL, SQLite, MSSQL ならこれ

---
## ORM(Mongoose)

MongooseのModelクラスを作成します。
```
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// スキーマ定義
var UserSchema = new Schema({
  email: {
    type: String,
    lowercase: true
  },
  password: String,
  admin: {
    type: Boolean,
    default: false
  }
});

// 外部に公開します
module.exports = mongoose.model('User', UserSchema);
```

---
## ORM(Mongoose)

利用するにはModelをロードして利用する。
```
var User = require('./models/user.model');

User.find({}}
  .exec()
  .then((users) => {
    // 正常系の処理
  }, (err) => {
    // 異常系の処理
  })
```

よく使うもの

- find
- findOne
- findById
- findByIdAndUpdate
- findByOneAndUpdate
- findByIdAndRemove
- findByOneAndRemove
- create
- save

findByIdAndUpdateではなく、findByIdしてからsaveしている方が多い気がします(経験談)

---
## ORM(Mongoose)
Modelクラスにロジックを寄せるのが綺麗です(経験談)

Mongoose Modelクラスの中身の例）
```
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = new Schema({
  ...
});

//////////// Virtuals
UserSchema
  .virtual('password')
  .set((password) => {
     this.cachedValue = password;
    // 何かのSetter処理
  })
  .get(() => { return this.cachedValue});

//////////// Validations
UserSchema
  .path('email')
  .validate((value) => {
    // 何かのバリデーション処理
  }, 'メッセージ');

//////////// Hooks
UserSchema.pre('save', (next) => {
  // 何かの処理
  return next();
});

//////////// Instance Methods
UserSchema.methods = {
  authenticate(password) {
	 // 何かの処理
  }
};

//////////// Static Methods
UserSchema.statics = {
  findOne(id) {
    // 何かの処理
  }
}

module.exports = mongoose.model('User', UserSchema);
```

---
## ORM(Sequelize)

さーせん！時間切れ。。。orz

---
## エラーハンドリング(1/3)

特殊なmiddleware。

あまり細かくtry-catchせずグローバルレベルでエラーハンドリングすることが多い。

```
function(err, req, res, next) {
  // エラー処理    
}
```

最初の引数`err`にエラーの情報が連携される。基本的には次の3処理を行う。

- エラーログ出力
- REST API用のレスポンス返却
- 画面用のレスポンス返却(エラーページ)

---
## エラーハンドリング(2/3)
エラーハンドリングの順番
```
// エラーログ出力 
app.use(logErrors);

// REST API用のエラーハンドラ(ここでは、/apiがAPIの想定)
app.use('/api', clientErrorHandler);

// エラーベージ表示用エラーハンドラ
app.use(errorHandler);
```

---
## エラーハンドリング(1/3)

エラーハンドリングの記述例
```
// エラーログ出力
function logErrors(err, req, res, next) {
  console.error(err.stack);
  next(err);
}

// REST API用のレスポンス返却
function clientErrorHandler(err, req, res, next) {
  res.status(500).json({
    message: err.message,
    error: err
  });
}

// 画面用のレスポンス返却
function errorHandler(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: err
  });
}
```

---
## 認証(Passport)

[Passport](http://passportjs.org/)

- ほぼ、node.jsの認証モジュールでデファクト
- 様々な認証に対応可能(Strategy)
- 下手に独自で認証を実装するくらいなら、Passportの使い方を習得したほうが後々潰しが効く(経験談)

対応例）
- [passport-local](https://github.com/jaredhanson/passport-local) - Username and password
- [passport-twitter](https://github.com/jaredhanson/passport-twitter) - Twitter
- [passport-facebook](https://github.com/jaredhanson/passport-facebook) - Facebook
- [passport-google-oauth](https://github.com/jaredhanson/passport-google-oauth) - Google
- and more 307 Strategies

---
## Passportのフォルダ構成

- passport全体の設定 => `passport.js`
- 個別のStrategyの設定 => `passport/`
- 認証フィルタはmiddleware化する

```
config
  app.js              - passportの初期化
  passport.js         - passportの全体的な設定 
  passport/           - Strategyごとの認証ロジックの設定
    local.js          - Username and password認証用
    twitter.js        - twitter認証用
  middlewares
    authorization.js  - routingで利用する認証フィルタ
```

---
## Passportの使い方(1/3)

passportモジュールの読み込み。Session用のmiddlewareの設定。

app.js
```js
var passport = require('passport');

// passportモジュールをLoad
require('./passport')(app);

// session用のmiddlewaresを有効化
app.use(passport.initialize());
app.use(passport.session());
```

---
## Passportの使い方(2/3)
Passport全体の設定。sessionのserializer/deserializer＆利用するStrategyの設定

config/passport.js
```js
module.exports = () => {

  // sessionにユーザー(のキー)情報を格納する処理
  passport.serializeUser((user, done) => {
    done(null, user.id);
  });
  
  // sessionからユーザー情報を復元する処理
  passport.deserializeUser((id, done) => {
    // DBのUserテーブルからユーザーを取得する処理
    User.findById(id).exec((err, user) => {
      done(err, user)
    });
  });

  // 利用するstrategyを設定
  passport.use(require('./passport/local'));
  ...

}
```

---
## Passportの使い方(3/3)
Strategyの個別設定。  
(※)詳細はそれぞれのStrategyの公式ページを参照してください。

config/passport/local.js
```js
// Strategyをロードする
var LocalStrategy = require('passport-local').Strategy;

// Strategyことの認証ロジックを追加する
module.exports = new LocalStrategy({
  // 認証ロジック
});
```

(ログインなど)特定のrouting時に認証を行うようにする。
```js
app.post('/login', 
  passport.authenticate('local', { failureRedirect: '/login' }),
  function(req, res) {
    // 認証成功時
    res.redirect('/');
  });
```

---
## Passport(認証フィルタ)

passportの作者が作ったものがある。  
[connect-ensure-login](https://github.com/jaredhanson/connect-ensure-login)

予めmiddleware化しておく。

config/middlewares/authorization.js
```js
// 認証フィルタに引っかかると`/badLoginRedirectPath`にリダイレクト
exports.authorize = require('connect-ensure-login').ensureLoggedIn('/badLoginRedirectPath');
```

routingでmiddlewareを設定する
```js
var auth = require('middlewares/authorization');
app.use('/some', auth.authorize, (req, res) => {
  // 何かの処理
});
```

---
## 設定情報

- 動作環境ごとで異なる情報(DB接続設定、APIKey、Secret)
- production環境の設定はリポジトリにCommitせず、動作環境の環境変数から取得する方がいい(経験談)

node.jsでの環境変数の取得方法

```
prosess.env.SOME_KEY
```

---
## dotenv(1/2)

[motdotla/dotenv](https://github.com/motdotla/dotenv)

- `.env`ファイルを環境変数にマッピングする
- ロードするファイルなどはカスタム可能

利用方法
```app.js
var app = express();

// nodeの動作環境(development/production)ごとにロードする設定情報を変更する
require('dotenv').config({
  path: 'config/environment/.env.' + app.get('env')
});
```

---
## dotenv(2/2)

よく使うディレクトリ構造
```
config
  environment
	.env.development   // 開発用
    .env.production    // 本番用(通常は空)
    .env.test          // テスト用
```

.env.development
```
MONGOLAB_URI=http://localhost:27017
```

express側で値を取得する
```js
console.log(process.env.MONGOLAB_URI) // => http://localhost:27017
```

とはいえ。。。  
[lorenwest/node-config](https://github.com/lorenwest/node-config)の方が良さそう。今度使ってみる。日々精進。


---
## セッション

[expressjs/session](https://github.com/expressjs/session)

```js
var app = express();
var session = require('express-session');

app.use(session({
  secret: 'secret-key',
  resave: false,
  saveUninitialized: true
}));
```

- Session IDがcookieに保存される
- デフォルトのSession ID名は`connect.sid`
- デフォルトはオンメモリ上で保持される。通常はSession Storesで永続化する

 Session Stores）
 - [tj/connect-redis](https://github.com/tj/connect-redis) - redis用
 - [kcbanner/connect-mongo](https://github.com/kcbanner/connect-mongo) - mongodb用
 - [mweibel/connect-session-sequelize](https://github.com/mweibel/connect-session-sequelize) - postgress, mssqlなどRDB用
 - and more ...

---
## セッション(Redis Session Store)

```js
var app = express();
var session = require('express-session');

// Session Storeをロードする
var RedisStore = require('connect-redis')(session);

app.use(session({
  secret: 'secret-key',
  resave: true,
  saveUninitialized: true,
  // Session Storeの設定
  store: new RedisStore({
    url: <REDIS_URL> // redis://localhost:6379
  })
}));
```

---
## セッション(MongoDB Session Store)

DBの接続情報は`mongoose`を利用する。(mondoDB URLでももちろん可)
```js
var app = express();
var session = require('express-session');

// Session Storeをロードする
var MongoStore = require('connect-mongo')(session);
var mongoose = require('mongoose');

app.use(session({
  secret: 'secret-key',
  resave: true,
  saveUninitialized: true,
  // Session Storeの設定
  store: new mongoStore({
    mongooseConnection: mongoose.connection
  })
}));
```

---
## ロギング

[expressjs/morgan](https://github.com/expressjs/morgan)

- アクセスログを出力する
- 出力先は標準出力(ファイル出力＆ローテション可能)
- expressに求める機能が薄いためなのか、今のところこれで十分(経験談)

app.js
```js
var logger = require('morgan');
// ログフォーマット
// combined, common, dev, short, tiny
app.use(logger('dev'));
```

出力内容
```
PUT /api/articles/5621dc5633d2c52b7c166873 500 12.569 ms - 47
GET /new-post 200 771.074 ms - 1885
GET /stylesheets/style.css 200 13.891 ms - 102
GET /bower_components/bootstrap/dist/css/bootstrap-theme.min.css 200 18.804 ms - 23357
```

---
## デプロイ(Heroku)

```
git push heroku master
```

- Herokuの話
	- アプリケーション直下に`package.json`があるとNode.jsと判定される。
	- node.js場合、`npm run start`が自動実行される。(Procfile必要なし)

package.json
```
{
  "name": "node-sample",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/www" ← これ
  },
  "dependencies": {
    "body-parser": "~1.13.2",
    "cookie-parser": "~1.3.5",
	...
  }
}
```

---
## デプロイ(Heroku Q&A)

Q: bowerモジュールがインストールされません  
A: package.jsonのdependenciesにbowerを追加して`postinstall`する

[ECMAScript 6で開発したアプリをHerokuにデプロイ - フレクトのHeroku Lab](http://blog.flect.co.jp/labo/2015/07/ecmascript-6her-ec6a.html)

package.json
```
{
  "name": "node-sample",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/www",
    "postinstall": "bower install" ← これ
  },
  "dependencies": {
    "body-parser": "~1.13.2",
    "cookie-parser": "~1.3.5",
    "bower": "^1.6.3", ← これ
	...
  }
}
```

---
## デプロイ(Heroku Q&A)

Q: augularとか使っているので、gulpでビルドをしたいです  
A: おじさんがいい方法知ってるから、後で裏に来なさい

---
## 小ネタ

レスポンスの`x-powered-by`ヘッダーを消す。

```
app.set('x-powered-by', false);
```

---
## まとめ

最初はこれくらい知ってれば、まぁ大丈夫じゃないかな。

---
### enjoy express :)

### It’s your turn.

---
![Analytics](https://ga-beacon.appspot.com/UA-56126469-5/fc48397a8e80f051a145)
