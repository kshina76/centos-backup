# 基礎から学ぶサーバレス開発

## サーバレスを使用することのメリットデメリット
### メリット
- コストを抑えることができる
- オートスケール
- ミドルウェアまではAWSが管理してくれる
- OSとミドルウェアの設定が不要なので、アプリケーションの開発に注力することができる
- サーバ攻撃の対象にならない
  - LambdaはデフォルトだとIPアドレスを公開しない
- マイクロサービスに向いている
### デメリット
- 制約がある
  - 起動時間、タイムアウトなど
- ステートレスな構造設計ができないと使いこなせない
- 監視が複雑になる
  - 二重起動の監視
  - 起動しなかった場合の監視
- コールドスタート
- RDSとの親和性がない可能性がある
  - LambdaをVPCに配置できるようになったので問題ない？

## 異なる3つのLambda呼び出しモデル
- 同期呼び出し
  - API Gateway
- 非同期呼び出し
  - SNSやS3
- プルベース
  - SQSやKinesis

![reinvent2020-svs303-scalable-serverless-event-driven-architectures-with-sns-sqs-lambda_6-640x364](https://user-images.githubusercontent.com/53253817/109839499-82663700-7c8a-11eb-91cf-87a24427baf4.png)

### 参考文献
- https://dev.classmethod.jp/articles/reinvent2020-svs303-scalable-serverless-event-driven-architectures-with-sns-sqs-lambda/

## サーバレスでよく使われるサービス
### Amazon Aurora Serverless
- Amazon RDSを自動でスケーリングするオプション
### AWS Step Functions
### AWS X-Ray

## サーバレス開発に必要なこと
### AWS SAM(サーバレスフレームワーク)
- サーバレス開発で使用されるフレームワーク
- CloudFormationやTerraformを簡略化した形で記述することが可能
- CodePipelineなどと親和性が高い
- SAM CLIとかをインストールすれば良さそうかな？
### CI/CD
- AWSのCI/CDは「CodeCommit, CodePipeline, CodeBuild, CodeDeploy, CodeStar, CloudFormation」を使用して実現することが多い
### デプロイ手法
- 一般的な方法
  - インプレースデプロイ
  - ローリングデプロイ
  - ブルー/グリーンデプロイ
  - イミュータブルデプロイ
- Lambdaにおけるトラフィックシフト(デプロイ)
  - AWS Lambdaのバージョニング機能を使用したトラフィックシフト
  - API Gatewayのカナリアリリース機能を使用したトラフィックシフト
### 運用
- コストの試算
  - AWSコンソールの機能としてあるっぽい
### 監視
- リソース監視(CPU,メモリ,ディスク,プロセス,ログ)
  - syslog,アプリログ
- セキュリティ監視
  - モジュールのバージョン
  - 不正アクセス
  - ログの改ざん
- ネットワーク監視
  - 疎通確認
### セキュリティ
