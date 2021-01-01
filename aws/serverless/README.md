# サーバレス

## サーバレスに必要な知識
- https://qiita.com/dyson-yamashita@github/items/7807fc3655a4d37e567f

<br></br>

## 開発環境
- docker-lambdaを使ってローカルで開発をすることができる
- https://munchkins-diary.hatenablog.com/entry/2020/02/05/002748
- https://dev.classmethod.jp/articles/app-fw-for-lamdba-jeffy-released/
## サーバレス開発でよく使われるツール

<br></br>

## AWS LambdaでAPI開発をするときのパターン集
### 1.Functions(別ソース)パターン

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-234396-a37a57da-4ab4-b301-72d9-ca3b41abfaea](https://user-images.githubusercontent.com/53253817/100832622-9774d380-34ab-11eb-8c6e-559c0414337f.png)

- 特徴
  - Lambda間でリソースもソースファイルもが共有されません
  - APIのパスの数だけLambda関数のリソースが作成されます
  - 共通ロジックがある場合はLayerにおきます
  - Cloud9で開発するとこのパターンになります
- メリット
  - Lambda間の依存関係がないため非常に疎結合になります。このためAPIの追加や修正が気軽に行えます。
  - リソースが分離されるので、Cloudwatchのログが関数ごとに出力され、エラーログがとても追いやすくなります。
  - 関数ごとにリソースが分離されるので、細かくポリシーを設定できるためセキュアな構成を作ることができます。
- デメリット
  - 共通ロジックをLayerに置いといたとしても、Layerのバージョン管理に悩まされます。Layerを更新しても、すでにデプロイ済みのLambda関数は古いLayerを参照しているため、一度全てのLambda関数をデプロイしなおさないといけません。
  - Layerに配置したロジックはエディタの補完が効かないため、開発効率が下がります。
  - SAM/ServerlessFrameworkのようなデプロイ支援ツールを使う場合、その設定ファイル(template.yaml/serverless.yaml)が煩雑になりがちです。環境変数を全てのリソースに渡す必要があると、それだけで設定ファイルの行数が増えてしまいます。
  - 関数ごとに細かくポリシーを設定することはメリットである一方で、管理が難しくなります。

### 2.Functions(同一ソース)パターン

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-234396-0f854adb-be5a-a915-2004-4e9c453e331b](https://user-images.githubusercontent.com/53253817/100832628-99d72d80-34ab-11eb-9177-a249d5faf824.png)

- 特徴
  - ソースファイルは同じものを利用しますが、各Lambdaのエントリーポイント(ファイル名/関数名)を切り替えることでLambda関数を作成するため、リソースは分離されます。
  - APIのパスの数だけLambda関数のリソースが作成されます
- メリット
  - Layerを使わずに共通ロジックを再利用することができます
  - リソースが分離されるので、Cloudwatchのログが関数ごとに出力され、エラーログがとても追いやすくなります。
  - 関数ごとにリソースが分離されるので、細かくポリシーを調整できるためセキュアな構成を作ることができます。
- デメリット
  - ソースファイルが各Lambdaで共有されるためAPIの追加や修正時に影響範囲を考慮する必要があります。
  - SAM/ServerlessFrameworkのようなデプロイ支援ツールを使う場合、その設定ファイル(template.yaml/serverless.yaml)が煩雑になりがちです。環境変数を全てのリソースに渡す必要があると、それだけで設定ファイルの行数が増えてしまいます。
  - 関数ごとに細かくポリシーを設定することはメリットである一方で、管理が難しくなります。

### 3.WebFrameworkパターン

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-234396-7c517643-9cd6-8c44-6674-93afa8cc815c](https://user-images.githubusercontent.com/53253817/100832633-9ba0f100-34ab-11eb-9752-cf49d08808cb.png)

- 特徴
  - API Gatewayは受け取ったリクエストをそのままLambdaにパススルーし、Lambdaに載っているWebフレームワークがルーティング等を行います
  - API Gatewayはプロキシリソースとの統合となります。(パス変数が/{proxy+}のようになります)
  - LambdaとWebFrameworkの間のインターフェイスをつなぐライブラリを利用する必要があります(例： aws-serverless-express, challice, Serverless Framework Pluginなど)
- メリット
  - WebFrameworkの知識があればLambdaの知識がなくても開発が可能です
  - WebFrameworkをライブラリでラップしているだけなので、サーバレスからEC2やオンプレへ移行する必要があったときにそれがとても容易にできます
- デメリット
  - ライブラリに対応しているWebフレームワーク以外では使用できません
  - モノリスになりがちな構成になります
  - デプロイパッケージのサイズが大きくなってしまいます。しかしこれはLayerに依存パッケージを載せることで解決可能です。

### 4.GraphQLパターン

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-234396-fb52e0dc-bd97-8491-7351-a53f83df598e](https://user-images.githubusercontent.com/53253817/100832643-9e034b00-34ab-11eb-971f-4c08ca8dd393.png)

- 特徴
  - Apollo Server on Lambdaを利用してGraphQLサーバをLambdaに載せます。
  - GraphQLサーバがリクエストのbodyを見てクエリを捌く形になります
  - API Gatewayは/graphqlの単一エンドポイントになります
- メリット
  - GraphQLの恩恵を得ることができます(クエリの柔軟性、アジリティ、パフォーマンス向上、PlayGround、型情報の自動生成 etc...)
  - API Gatewayにエンドポイントを追加できる余地があるため、RESTと共生することが可能です。
- デメリット
  - RESTに比べて知識が浸透していないため学習コストがかかります。教育コストや引継ぎコストに繋がるため慎重に選ぶ必要があると思っています。
  - GraphQLのデメリットを受けます(クライアント側でライブラリの利用がほぼ必須になるetc)

### 5.マイクロサービスパターン

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-234396-f34b9407-52f8-59e6-fc41-5ffef70d9818](https://user-images.githubusercontent.com/53253817/100832648-9fcd0e80-34ab-11eb-985e-371027bcc0d3.png)

### まとめ

![2020-12-02 14 36のイメージ](https://user-images.githubusercontent.com/53253817/100832761-dc990580-34ab-11eb-8103-b65b8033965b.jpeg)

- 影響範囲を考慮しなくていい
  - functionsパターン(ソースコード分離)はリソースとソースが両方とも分離されるため一切の依存関係がなく、影響範囲を考慮せずに機能の追加や修正を行うことができます。複数のメンバーで開発する場合などに大きなメリットがあると思います。その他のパターンはソースコードを共有するため、一定程度の影響範囲を考慮する必要があります。

- 細かなポリシー管理
  - Lambda関数ごとにポリシーを設定したいニーズがある場合は、functionsパターンを選択する必要があります。これはセキュリティ的にはメリットと言えますが、管理が大変になるデメリットでもあります。
GraphQLパターンの場合は必要に応じてREST APIを追加できるので、どうしてもこのニーズがあったときはそこだけ切り出してLambdaを作成しポリシーを設定することが可能です。

- 共通ロジックの利用
  - ソースコードを共有できる場合は共通ロジックを利用できますが、functionsパターン(ソースコード分離)ではできません。Layerを使えば共通ロジックを利用することができますが、補完が効かないことやバージョン管理が面倒なことを考えるとあまり良い選択肢とは言えないと思っています。

- 導入容易性
  - functionsパターンはSAM/ServerlessFrameworkを利用することですぐに始められますが、他パターンはライブラリやプラグインの設定が必要な分、少しだけ導入容易性が低いと言えます。

- サーバへの移行
  - パフォーマンスの観点からサーバレスからEC2/オンプレへ移行する可能性がある場合は、すぐにリソースを剥がせる構成であることが望ましいでしょう。WebFrameworkパターンとGraphQLパターンはラップしているライブラリを引き剥がすことですぐにオンプレに移行することができます。

- 学習コストの低さ
  - Lambdaを意識せずに開発できるWebFrameworkパターンが学習コストの面では軍配が上がります。現在はGraphQLが最も学習コストが高い選択肢であると言えるでしょう。

- 開発のしやすさ
  - functionsパターン(ソースコード分離)は共通ロジックが利用しにくいため開発がしにくいです。WebFrameworkパターンとGraphQLパターンはフレームワークの恩恵が受けられるため問題なく開発を行うことができます。

- エラーログの追いやすさ
  - デプロイした後のエラーログを追いたいときはリソースごとにCloudWatchが分かれているfunctionsパターンがエラーログが追いやすいです。

- デプロイ容易度
  - functionsパターンはどうしてもSAM/ServerlessFrameworkの設定ファイルが煩雑になりやすいことがネックになります。WebFrameworkパターンはプロクシパスに、GraphQLパターンは単一エンドポイントにまとまるため、設定ファイルをシンプルに保つことが可能です。

### 参考文献
- https://qiita.com/yuno_miyako/items/3fe75bf53fe0ae43e274

<br></br>

## AWS Lambdaの公式パターン集(APIだけじゃないよ)
- 以下を読んでまとめる
  - https://dev.classmethod.jp/articles/introduction-serverless-pattern/
  - https://aws.amazon.com/jp/serverless/patterns/pattern-design-examples/

<br></br>

## Apex/upとTerraformでLambdaを管理
### AWS Lambdaを定義するのに必要な4つのこと
1. AWSのオブジェクト管理（Lambda Function、IAM、triggerのためのCloudWatch Eventsなど）
2. Lambda関数のソースコード
3. Lambda関数のソースコードに依存するライブラリたち
4. ソースコードとライブラリを固めたzip
### Apex/upで2~4を定義
- S3にzipをuploadしないで直接Lambdaにuploadする
- これによってarchiveしたzipを入れるS3の管理や、zipファイルをterraformで管理する必要がなくなる
### Terraformで1を定義
- `apex infra`というTerraformのラッパーコマンドで使える
- LambdaのIAMの設定やCloudWatch EventsなりS3のEventなり好きなTriggerをこれまたtfファイルに書いてapex infraコマンドで適用するだけ
- zipはApex/upで管理してくれるので問題ない
### Terraformだけで管理することの大変さ
- インフラの状態を定義するツールであるTerraformで上記4点を管理すると、applyのたびにnpm installなりを実行せなばならず、意図せぬ差分が発生しやすい。
- これはequal意図して変更していないコードのデプロイとなり、applyするのが恐ろしい状況になってしまう。
- それを回避するためにライブラリ(node_modulesやgem等)とzipをgit上にあげて差分が発生しない状況をつくっていたが数千ファイルを超える依存ライブラリや、バイナリであるzipをガンガン突っ込んでいくとFileChangesが6000とかになってかなり辛い・・
### Apexの代替案
1. Apexはメンテナンスされていないので、後継のApex/upを使うか、日本製のlambrollを使うかどちらかになる
  - https://github.com/fujiwara/lambroll
  - https://sfujiwara.hatenablog.com/entry/lambroll
2. terraformとAWS Lambda Layerを使う方法
  - https://dev.classmethod.jp/articles/terraform-lambda-deployment/
  - https://micpsm.hatenablog.com/entry/2019/12/08/120000
3. サーバレスまわりだけAWS-CDKを使う方法
  - Lambdaを使うときだけはCDKで他の部分はTerraformを使用するとか
  - https://kotamat.com/post/compare-cdk-with-terraform/
4. pulumiを使う方法
  - pulumiはAWS-CDKを色々なクラウドに対応させたものといった感じ
  - https://qiita.com/sirotosiko/items/91490b22aa39b9705b0a
- terraform vs pulumi
  - https://kari-marttila.medium.com/terraform-vs-pulumi-experiences-c41a8774b637
  - https://qiita.com/kenseitogari1/items/0c16f2434a3b7178b7bb
### 参考文献
- https://tech.recruit-mp.co.jp/infrastructure/post-16931/
