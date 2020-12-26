# ログに関するまとめ

## 1. メトリクス(Metrics)、イベント(Event)、ログ(Logs)、トレース(Trace)
- https://blog.newrelic.co.jp/story/metrics-events-logs-and-traces/
- https://docs.microsoft.com/ja-jp/azure/architecture/microservices/logging-monitoring
### 1-1. イベント(Event)
- ある瞬間に発生する個別のアクションをさす
- イベントは「いつ何が起こった」ということを記録する
- あくまでも結果を記録するだけなので、詳しいログなどは表示されない

![2020-12-24 13 59のイメージ](https://user-images.githubusercontent.com/53253817/103062421-81ad8680-45f1-11eb-9d2a-1283a5d3208f.jpeg)

- 「2019年2月21日午後3時34分に、BBQチップのバッグが1ドルで購入された」ということがわかる
### 1-2. メトリクス(Metrics)
- 定期的にグループ化または収集された測定値の集合
- メトリクスは個別ではなく「特定の期間のデータの集計」を表す
  - 例えば、average(平均)、total(合計)、minimum(最小)、maximum(最大)、sum-of-squares(平方和)

![2020-12-24 14 01のイメージ](https://user-images.githubusercontent.com/53253817/103062431-84a87700-45f1-11eb-9af3-c4647e0a3936.jpeg)

- 「2019年2月21日の午後3時34分から3時35分まで、合計3回の購入があり、合計で$ 2.75」ということがわかる
### 1-3. ログ(Logs)
- 特定のコードブロックが実行されたときにシステムが生成する単なるテキスト行
- 開発者がトラブルシューティングするときに使うもの
- 一つのイベントの詳細な動きを見たり
### 1-4. トレース(Trace)
- マイクロサービスエコシステムの異なるコンポーネント間のイベント（またはトランザクション）の連鎖を記録したもの
- 一つのイベントがどのようなサービス(アプリケーション)を経由して処理されているかということがわかる

![2020-12-24 14 08のイメージ](https://user-images.githubusercontent.com/53253817/103062437-85d9a400-45f1-11eb-83ca-6464286cffb4.jpeg)


<br></br>

## 2. ログの設計
### 設計で考えること
- ログフォーマット
- ログメッセージ
- ログレベル
  - ログには`Log4j`といった規格がある
- ログ出力タイミング
- ログ出力先
- ログローテート
### 参考文献
- https://www.bit-drive.ne.jp/managed-cloud/column/column_06.html

<br></br>

## 3. pythonのloggingとlogger
- loggingではなくてloggerを使う
  - https://qiita.com/amedama/items/b856b2f30c2f38665701
- pythonのloggingとloggerを徹底解説している
  - https://qiita.com/__init__/items/91e5841ed53d55a7895e
- loggingはグローバル変数のようなものなので、そのまま使ってはいけない。loggerを使うことでファイル毎にログを設定できて、ファイル名もログに含めることができるので、どこで発生しているエラーなのかといったトラブルシューティングがしやすい

<br></br>

# CloudWatch
- https://www.bit-drive.ne.jp/managed-cloud/column/column_06.html
## CloudWatch、CloudWatchLogs、CloudWatchEventsの違い
### CloudWatch
- リソースの監視を行う
- CPUやメモリなど複数項目をグラフ化してダッシュボードを作る
- よく使うものは標準メトリクスとして用意されている
- 監視するだけじゃなくてリソースの状況に応じて、メールを送ったり、再起動したり、AutoScalingしたりとアクションができる
### CloudWatch Logs
- ログを集めて監視する
- 「エージェントを入れたAWSサービスのOSのログ」と「アプリケーションのログ」を取得することができる
  - Pythonなどでログを吐き出すプログラムを書いたりしてアプリケーションのログをCloudWatchLogsから取得したりする。S3に書き出すことももちろんできる
- インスタンスにエージェントを入れて監視させる
  - ただし、Lambdaの場合はエージェントはいらないらしい
### Cloudwatch Events
- APIのイベントをトリガーに何らかのアクションを実行させる
- AWSはさまざまな(全て？)処理をAPIで実行しているから、AWSが処理を行うとにAPI(イベント)が発生する。そのイベントをEventsがキャッチして何らかのアクションをするということ

## CloudWatchLogsとpythonのloggerを連携
- https://cloudpack.media/30246
