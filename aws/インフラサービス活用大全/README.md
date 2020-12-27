# AWSインフラサービス活用大全 書籍メモ

## 2章まとめ
### 2-1. EFS, EBS, FSx, S3に違い
- EFS: オンプレでいうNAS
- EBS: EC2用仮想ハードディスク。EC2からマウントして使用
- FSx: EFSのWindows対応版。OSがWindowsのEC2で使用。
- S3: クラウド型オブジェクトストレージサービス。EC2と組み合わせて運用する場合はStorage Gatewayサービスを使用する。
- 参考文献
  - https://business.ntt-east.co.jp/content/cloudsolution/column-try-31.html
  - https://qiita.com/hayashier/items/6a315d8ca2cfd9826e5c

![2020-12-27 23 55のイメージ](https://user-images.githubusercontent.com/53253817/103173525-ff49ee80-489e-11eb-8b2b-8743c2eb84d6.jpeg)

<br></br>

## 3章まとめ
### 3-1. メトリクス(Metrics)、イベント(Event)、ログ(Logs)、トレース(Trace)
- https://blog.newrelic.co.jp/story/metrics-events-logs-and-traces/
- https://docs.microsoft.com/ja-jp/azure/architecture/microservices/logging-monitoring
#### 3-1-1. イベント(Event)
- ある瞬間に発生する個別のアクションをさす
- イベントは「いつ何が起こった」ということを記録する
- あくまでも結果を記録するだけなので、詳しいログなどは表示されない

![2020-12-24 13 59のイメージ](https://user-images.githubusercontent.com/53253817/103062421-81ad8680-45f1-11eb-9d2a-1283a5d3208f.jpeg)

- 「2019年2月21日午後3時34分に、BBQチップのバッグが1ドルで購入された」ということがわかる
#### 3-1-2. メトリクス(Metrics)
- 定期的にグループ化または収集された測定値の集合
- メトリクスは個別ではなく「特定の期間のデータの集計」を表す
  - 例えば、average(平均)、total(合計)、minimum(最小)、maximum(最大)、sum-of-squares(平方和)

![2020-12-24 14 01のイメージ](https://user-images.githubusercontent.com/53253817/103062431-84a87700-45f1-11eb-9af3-c4647e0a3936.jpeg)

- 「2019年2月21日の午後3時34分から3時35分まで、合計3回の購入があり、合計で$ 2.75」ということがわかる
#### 3-1-3. ログ(Logs)
- 特定のコードブロックが実行されたときにシステムが生成する単なるテキスト行
- 開発者がトラブルシューティングするときに使うもの
- 一つのイベントの詳細な動きを見たり
#### 3-1-4. トレース(Trace)
- マイクロサービスエコシステムの異なるコンポーネント間のイベント（またはトランザクション）の連鎖を記録したもの
- 一つのイベントがどのようなサービス(アプリケーション)を経由して処理されているかということがわかる

![2020-12-24 14 08のイメージ](https://user-images.githubusercontent.com/53253817/103062437-85d9a400-45f1-11eb-83ca-6464286cffb4.jpeg)

### 3-2. ENI
- NICのこと
- 1つのENIに対して最大で30IPまで設定でき、1つのインスタンス毎に最大で8枚のENIの設定できるので、240のIPアドレスを設定することができる
- 用途としては、バーチャルホストとか
- https://dev.classmethod.jp/articles/vpc-ec2-multi-eip/

### 3-3. VPC

### 3-4. ルートテーブル
- ルーターのこと
- サブネットを作ったばっかだと、VPCのルートテーブルがアタッチされてしまっているので、カスタムのルートテーブルを作成してアタッチする必要がある
- 一つのサブネットあたり、一つのルートテーブルをアタッチすることができる
- 一つのルートテーブルは、複数のサブネットにアタッチすることができる
  - 同じルーティングになるなら、一つのルートテーブルに複数のサブネットをアタッチする(多分)
#### 3-4-1.  ルートテーブルのルーティングの「target local」とは
- target localが指しているIPはVPC自体にアタッチされているデフォルトのルートテーブル
- これがあることによって、**同一VPC内のsubnet同士は通信できる**
#### 3-4-2. ルーティングでデフォルトゲートウェイを設定
- `0.0.0.0/0`を指定する

<br></br>
