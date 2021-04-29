## 雑多なメモ
- 問題解決を始める前に、具体的な数値を設定して、目標設定をする
  - 数値でなくても、具体化することが大事

## TODO
- pythonでの二次元配列とかの定義方法を調べる
- スライド作成と発表練習
- 参考コードを見て、expressとかを使っているのかどうかを調べる
- todoアプリ
  - typescript, express, cdk
  - [lambdaとAPIGatewayとDynamoDBのローカル実行](https://dev.classmethod.jp/articles/cdk-local-develop/)
  - [expressでToDoアプリ](https://chobimusic.com/express/)
- バリデーションや例外処理などをリファレンスで見てみる

## AWS CDK
- 構成管理の役割だけでなくて、ボイラーテンプレートの役割も担っていて、コマンド一つでアプリケーションをデプロイするところまで自動で作成してくれるもの
- 従来の構成管理ツールは、ボイラーテンプレートまではできなかった

### ドキュメント(APIリファレンス)の読み方
- [ドキュメント](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/index.html#sidetoggle)
- `Constructors`と`Properties`のパラグラフを参考にして、引数を決定していけば良い
- 「AWSのサービス名　cdk」とかでググれば、どのライブラリを使えばいいか分かる

### CDKの共通の引数の渡し方
- 第1引数: `Construct`型を渡す。Constructを継承しているクラスの中で、thisを渡せば良い
- 第2引数: リソースを表す一意の任意のid(string)を付ける
- 第3引数以降: オブジェクト型で、AWSリソース毎に違う引数を渡す。APIGatewayなら、URIを渡すとか。

### ディレクトリ構成
- bin
  - 基本いじらない
- lib
  - AWSリソースの定義をしていくところ
- src
  - APIのコードを書いていくところ
  - Lambdaの実装とか
  - さらに「Controller, Model, Service」ディレクトリに分けるなどして、コードを書いていく
  - cdkコマンドではなく、自分で作成する

### コマンド
- `npm run build`
  - tsをjsに変換
- `npm run watch`
  - tsの変化を監視して、自動でコンパイルしてくれるっぽい
- `cdk init
- `cdk deploy`
  - 設定してあるAWSアカウントに、AWSリソースをデプロイする
- `cdk diff`
  - 現在デプロイされているスタックとの変更点を確認
- `cdk synth`
  - Cloud Formationのテンプレートを出力する
- [CDKコマンドまとめ](https://dev.classmethod.jp/articles/aws-cdk-command-line-interface/)

### 流れ
- `npm run build`
  - tsをjsに変換
- `cdk deploy`
  - 設定してあるAWSアカウントに、AWSリソースをデプロイする
- `cdk destroy`
  - デプロイしてあるリソース(スタックという)を削除

### CDKとSAM
- ローカルで実行するときにSAMを使う
  - 1.CDKでsynthコマンドを使ってCloudFormationのテンプレートを生成する
  - 2.SAM Cliで、「1」で生成したテンプレートを使って、ローカルにデプロイするなどをする
  - 3.DynamoDBなども絡めたい場合は、Dockerを使って構築する
- SAMだけでもサーバレス開発はできるが、CDKを使った方が、開発や管理もしやすい
- CDKだけでもサーバレス開発やその他の開発もできるが、ローカル実行ができないので、SAMも使う
- Lambdaを動作確認しながら使っていくのに、毎回デプロイはつらいから、この方法をとる
- [ここを参考](https://qiita.com/yhsmt/items/ebdb561e45c3cedf8f49)

### NodejsFunction
- CDKのLambdaFunctionの他の書き方
- [ここを参考](https://qiita.com/misaosyushi/items/104445be7d7d3ba304bc)

### CDKの拡張ボイラーテンプレート生成
- [ここを参考](https://this.aereal.org/entry/2020/08/06/144038)

### 参考文献
- [CDK基礎知識](https://blog.kentarom.com/learn-aws-cdk/)

<br></br>

## アプリの題材
- todoアプリ
- Slackアプリ
- ブログ
- teamsアプリ
  - SlackアプリをTeams版に作成するとか
  - [ここを参考](https://qiita.com/girlie_mac/items/97fa81e67ad6ba0f6f35)

<br></br>

## AWS SAM
- `sam local start-api`
- `sam local invoke`
- `sam local start-lambda`

<br></br>

## Controller,Service,Model
- [Webアプリのシステム構成まとめ](https://qiita.com/okeyaki/items/37eb4b66bd8ef62c1fe8)
- [MVCのServiceの役割](https://ja.stackoverflow.com/questions/4360/mvcモデルにおけるサービスの役割について教えて下さい)
- [Controllerにビジネスロジックを書くなへの対応](https://qiita.com/os1ma/items/66fb47f229896b32b2e8)
- [Service層を設けたMVCのわかりやすいUML](https://www.google.co.jp/amp/s/cpoint-lab.co.jp/article/202002/13855/amp/)

### 構成
- Controller
  - ルーティングを主に書くところ
  - URI毎、メソッド毎に振り分けていくところ
- Service
  - ユースケース層と同じ役割
  - Modelのメソッドを複数呼び出して、機能を満たす役割。つまり、Modelの処理をまとめる感じ。
  - DBアクセスはここに書くのかな？それとも、データベース層みたいなものを設けるのかな？
  - ルーティングによって振り分けられた後の処理を担当する
- Model
  - 最小単位の重要なビジネスロジックを技術するところ
  - ORMなどを使用する場合、ここからDBにアクセスしたりする

<br></br>

## express
- [APIリファレンス](http://hideyukisaito.github.io/expressjs-doc_ja/guide/)
  - バリデーション、例外処理など
### express-generator
- [ここを参考](https://expressjs.com/ja/starter/generator.html)
- expressのボイラーテンプレートを生成するもの
- WebAPIだけを作るときには、使わなそう
  - htmlとかimgとかを配置するディレクトリなども生成されるから
- cdkのチュートリアルのtodoアプリを作るときには、このジェネレーターをベースにしても良いかも

<br></br>

## huskyで自動lint
- [tslintからeslintへ](https://qiita.com/suzuki_sh/items/fe9b60c4f9e1dbc5d903)
  - tslintは非推奨になって、eslintにtypescriptのlintをプラグインとして導入したものが使用されている
- prettierとESLintを併用する理由
  - prettierはESLintよりコード整形が優れているので、コード整形にprettierを使用
  - prettierは言語毎の構文チェックはできなくて、あくまでもフォーマッターなので、構文チェックはESLintを使用
  - 結論として併用することがベター
  - [ここを参考](https://qiita.com/soarflat/items/06377f3b96964964a65d)
### huskyとは
- 導入方法
  - [ここを参考1](https://github.com/typicode/husky)
  - [ここを参考2](https://dev.classmethod.jp/articles/pre-commit/)
- huskyはNode.jsのcommit hook
  - commit hookは各言語にあるので、適宜調べる
- git commitする前に、自動で指定したコマンドを実行させるもの
### GitHub Hooksとの違い
- GitHub Hooksは、本来`.git/hooks/`の中のファイルにスクリプトを定義すると、CommitやPushした時に、自動で定義されたコマンドを叩いてくれるが、huskyを使うと、その定義をpackage.jsonから行えるようになるので、チーム内で設定を共有しやすいという利点がある
  - おそらく、huskyで定義したものが、自動で`.git/hooks/pre-commit`などに記述されるのだと思う。huskyインストール時に、`.git/hooks/pre-commit`が自動で作られることからも、そうだと思う。
### 便利ツール
- lint-stagedというものを使用すると、変更箇所だけにフォーマッターやLintが動いてくれるので、効率的
  - [ここを参考に](https://serip39.hatenablog.com/entry/2020/07/28/073000)

- webhookの設定はしなくていいのか？
  - webhookは、commitやpushが発生した時に、指定のURLにPOSTリクエストを送るもの
  - Slackなどに通知したい時に使うもので、指定URLに送る必要はない場合、webhookの必要はない
  - [ここを参考](https://qiita.com/soarflat/items/ed970f6dc59b2ab76169)

<br></br>

## dev-dependencyとdependencyの使い分け
- dev-dependencyは、Lintやフォーマッターやテストなどの、開発環境でしか使用しないものを入れる
- dependencyは、本番環境でも開発環境でも使うものを入れる。

<br></br>

## kotlin
- gRPC
- Ktor
- Exposed
- Kotest,MockK
- JUnit
- Spring boot
- My Batis
