# AWS Lambda実践ガイド 書籍メモ

## 1.Lambdaの概要
### Lambdaとは
- Lambdaはイベントの発生によってプログラムが実行される
  - S3にファイルがアップロードされた時
  - API Gatewayを使って、HTMLフォームやAjax通信によるリクエストを捌いたり

  ![2020-12-05 13 33のイメージ](https://user-images.githubusercontent.com/53253817/101233899-7d7eff00-36fe-11eb-96df-da813c74f280.jpeg)

  ![2020-12-05 13 33のイメージ (1)](https://user-images.githubusercontent.com/53253817/101233900-7eb02c00-36fe-11eb-8de3-bbee7dae0c1e.jpeg)

- 小さな関数を組み合わせて全体を作る
  - キューイングサービスであるSQSや通知サービスのSNSトピックを使うとLambdaを疎結合に繋げることができる
  - 拡張性、保守性、テスタブルに保てる
  - 100行程度のプログラムをLambdaに実装して組み合わせる
- ステートレスなのでログを残すようにする
  - Cloud Watch Logsなどに処理内容や状態を書き出す
  - 何か異常が起きたら「決まった文字列」を書き込むように設定すると、Cloud Watch Logsのアラートを使って管理者に伝えることができる
- LambdaはEC2と同じようにOS上で走るコンテナということを意識しておくと、ハマることは少なくなると思う
#### メリット
- 保守運用に手間がかからない
  - Lambdaはマネージドサービスで、実行環境がAWSによって用意されているから
- 高負荷に耐えられる
  - Lambdaによるプログラム実行は必要に応じてスケーリングするため、高負荷に耐えられる
- コストを削減できる
  - 実行時間に対する課金だから
#### デメリット
- 前回の状態を保持しない
  - 実行が終わったときに環境を破棄する
- 最大稼働時間が決まっている

### EC2の問題点とLambdaの良い点
#### 脆弱性のアップデートなどが大変

![2020-12-05 13 26のイメージ](https://user-images.githubusercontent.com/53253817/101233798-bf5b7580-36fd-11eb-9dab-b86a232242fd.jpeg)

#### スケーリングが面倒、コストもかかる

![2020-12-05 13 26のイメージ](https://user-images.githubusercontent.com/53253817/101233798-bf5b7580-36fd-11eb-9dab-b86a232242fd.jpeg)

#### Lambdaは勝手に仮想環境が作られる

![2020-12-05 13 30のイメージ](https://user-images.githubusercontent.com/53253817/101233835-1b25fe80-36fe-11eb-94b7-2f5c04ed0601.jpeg)

#### 単純な機能の組み合わせで実装できる

![2020-12-05 13 30のイメージ](https://user-images.githubusercontent.com/53253817/101233836-1bbe9500-36fe-11eb-9d83-5095abcaed5c.jpeg)

<br></br>

## 2.Lambdaの事始め
### Lambdaの構造と設計
#### Lambdaの書式
- 慣習的に「機能名_handler」という名前が付けられる
- 入力はS3やSESなどのイベントが、「event」に格納される
- 割り当てられているメモリや実行環境の情報は、「context」に格納される
- Lambdaからの出力はreturnで行う(書式は連携するイベントによって異なる)
- 標準出力は全てCloud Watch Logsに書き込まれる
  - Lambda内でprintした内容など全て

  ![2020-12-05 13 48のイメージ](https://user-images.githubusercontent.com/53253817/101234176-938dbf00-3700-11eb-8507-761a3bea09ce.jpeg)


```python
def myfunc_handler(event, context):
  # 関数の処理
  return 戻り値
```

```bash
# 入力はjsonで来るが、lambdaのeventに到着した時にはパースされるので、プログラミング言語に適したオブジェクトでアクセスできる

{"x" : 10, "y" : 5}
|
|
↓
event["x"]は10
event["y"]は5
```

### Lambdaの利用に必要なアクセス権
#### IAMグループ、IAMユーザ、IAMロール、ポリシーの違い
- IAMグループはユーザの集まりに同一の権限を一括で与える
- IAMユーザは一つのユーザが行える権限
  - 例えば、Lambdaを作ったりEC2を作ったり、といった権限
- IAMロールはLambdaなどのリソースの権限
  - 例えば、Lambdaが他のリソースにアクセスするための権限のこと
- ポリシーはグループやユーザやロールに与える権限の細かい詳細
  - カスタムポリシーは権限を実作するできるもの
  - 管理ポリシーはAWSが作成して管理したもの
  - インラインポリシーはIAMに直接埋め込まれたもの

![awsaccount-IAMuser-IAMgroup-IAMRole-hikaku-image](https://user-images.githubusercontent.com/53253817/101234414-67733d80-3702-11eb-860a-6f9173f1527c.png)

#### IAMユーザ(開発者)のためのポリシー
- AWSLambdaFullAccess
  - LambdaおよびS3などのLambda関連のリソースへのフルアクセス権
  - 開発者がLambdaの関数を作成したり実行したり
  - 開発者がS3にファイルを置いたり読み取ったりできるということ
- etc
#### IAMロール(Lambda)のためのポリシー
- AWSLambdaBasicExecutionRole
  - 3種類のCloudWatchLogsへの書き込み権限
- AWSLambdaKinesisExecutionRole
- AWSLambdaDynamoDBExecutionRole
- AWSLambdaVPCAccessExecutionRole
#### IAMユーザとIAMロールの権限の設定は開発に入る前に行う
- 開発に入ってからあれができないこれができないでは大変
- Lambdaの画面でIAMロールを作成することもできるが、その場合IAMユーザのCreateRoleなどの権限も必要になるから面倒

### Lambda関数の作成(一部省略)
#### 設計図の選択
- 用途に合わせた設計図を選択すると楽に開発できる
#### トリガーの設定
- まだテスト段階なら設定しなくていい
#### 環境変数の設定
- ランタイムの環境変数に設定されるので、os.environ["foo"]のようにアクセスする
#### ハンドラの設定
- pythonの場合、「ファイル名.関数名」で指定
#### 詳細設定
- DLQリソース
  - 非同期呼び出しが失敗したときにSNSやSQSで通知する設定
- VPC
  - LambdaからVPCに設置されたリソースにアクセスしたい場合に使う
- アクティブトレース
  - AWS X-Rayを使って、Lambda関数の呼び出しを追跡する
- KMSキー
  - 環境変数を暗号化する場合の鍵の指定

### テストイベントの定義と手動テスト
#### テストイベントの定義
- json形式で定義するだけ
- 正常系と異常系の二つを軽くテストしておくといいかも
- S3やCloudWatchLogs特有のイベントを発生させたりできるので、手動のテストが楽
#### 実行結果の確認
- Lambdaのコンソールで確認
  - そのままログのボタンを押す
- CloudWatchLogsで確認
  - ログをクリックしてグループ化されているlambdaをクリック

<br></br>

## 3.AWSLambdaの仕組み
### イベントの種類

![2020-12-06 11 43のイメージ](https://user-images.githubusercontent.com/53253817/101270040-5553d680-37b8-11eb-8479-9ac55d1ed988.jpeg)

#### プッシュモデル
- イベントソースがLambda関数を呼び出すタイプ
- 同期呼び出し
  - Lambda関数の実行が終わるまで、呼び出し元には戻らない。実行が完了すると、Lambda関数の戻り値が呼び出し元に渡される
- 非同期呼び出し
  - イベントはキューに送信され、呼び出し元にすぐに戻る。Lambda関数の戻り値は破棄される
  - キューからの取り出しは一つではなくて複数取り出され、並列で実行される

    ![2020-12-06 12 29のイメージ](https://user-images.githubusercontent.com/53253817/101270681-baaac600-37be-11eb-9dcf-ee0a8dbd69b5.jpeg)

  - 実行に失敗したら２回まで再試行されるから合計3回実行される
    - エラーはCloudWatchLogsに残る
  - 3回失敗したらDLQで通知することが可能(設定しないとイベントは消失する)

    ![2020-12-06 12 33のイメージ](https://user-images.githubusercontent.com/53253817/101270719-3442b400-37bf-11eb-9b48-a1e5e7c09720.jpeg)

  - Lambdaでは例外とエラーを区別するべき
    - 渡されるパラメータが違う場合にLambdaが失敗したら例外ではなくて、エラーにする
    - 例外だとLambdaが再試行してしまうから
  - 実行順序は保証されない
  - 正常な場合も二回実行されることがある
    - 何度呼び出されても同じ結果を返す冪等生が重要
    - 一回しかやってはいけない処理ならどっかにフラグを立てるようにして二回目が実行されないようにする
  - 同時実行はデフォルトで1000個まで
  

#### ストリームベース
- Lambda関数側がイベントソースを流れるデータ(ストリーム)をポーリング(監視)して、データを拾ってくるモデル
- アクセス権の設定に注意

![2020-12-06 12 38のイメージ](https://user-images.githubusercontent.com/53253817/101270804-10cc3900-37c0-11eb-90b8-ff27f06bd4b4.jpeg)

#### イベントの一覧

![2020-12-06 12 41のイメージ](https://user-images.githubusercontent.com/53253817/101270829-4e30c680-37c0-11eb-97a7-aab680526d16.jpeg)


### LambdaコンテナはLinux環境
#### OS
- Amazon Linux AMI
- EC2で同じOSを立てて、ある程度開発を進めたらLambdaに載せるという開発手法が一般的
  - vscodeでLambdaの開発環境を整えたほうがいい気もするけど
#### tmp領域
- 512MBまで一時退避のディレクトリとして使える

#### 環境変数

![2020-12-06 11 45のイメージ](https://user-images.githubusercontent.com/53253817/101270066-98ae4500-37b8-11eb-81bd-c829cc90ff9f.jpeg)

### コンテナの再利用
- 1回目の実行はコールドスタートだけど、2回目からはコンテナが再利用されるから起動時間がいらない

![2020-12-06 11 50のイメージ](https://user-images.githubusercontent.com/53253817/101270108-31dd5b80-37b9-11eb-9e3d-22c451636ada.jpeg)

#### 再利用の注意点
1. tmpなどに前回のデータが残っている場合がある
  - Lambdaの処理の最後にtmpを削除する処理を実装する
    - 処理の最初に実装してしまうと、権限がないユーザが削除できなかった場合に次の環境に残ってしまうから
    - 処理の最後に記述すればtmpを作成できたユーザなら必ず削除できるはずなので残らない
  - tmpディレクトリに書き込むファイル名はランダムなものにする
2. 実行ユーザが異なる場合がある
  - Linuxシステム上のいずれかのユーザで実行される

### VPCへのアクセス
#### デフォルトだとLambdaコンテナはインターネットと接続可能なパブリックな場所にある
  - VPCに配置されていないで浮いている？状態
#### VPCに配置されたEC2やRDSと通信するためにはLambdaをVPC内のサブネットに配置する
  - サブネットに配置することでルーティング対象になるからだと思う
#### VPC配置のデメリット
1. 起動に時間がかかる
2. 同時実効性が落ちる
  - VPCにLambdaを配置するということは、ルーティング対象になる。つまりIPアドレスが振られる。十分なIPアドレスがないと枯渇してしまい実行できなくなってしまう可能性がある

![2020-12-06 12 05のイメージ](https://user-images.githubusercontent.com/53253817/101270341-5c301880-37bb-11eb-9c1d-a8fad9785bd8.jpeg)

#### NATゲートウェイでIPアドレスを固定化
- サブネットにLambdaを配置するとルーティングがEC2と同じ振る舞いをする
- NATゲートウェイを構築すると、プライベートサブネットからでもインターネットに出ていける
  - 他のリソースと同じように
- Lambdaはパブリックサブネットに配置してもインターネットに接続はできないので注意。プライベートサブネットに配置してNATを噛ませないとだめ
  - https://michimani.net/post/aws-run-lambda-in-vpc/
- NATゲートウェイにElastic IPアドレスを設置するとIPアドレスを固定化できる
- インターネット外からLambdaにアクセスすることはできないのかな？

![2020-12-06 12 17のイメージ](https://user-images.githubusercontent.com/53253817/101270587-b500b080-37bd-11eb-8082-20537d322e83.jpeg)

#### LambdaではRDSではなくDynamoDBが使われる
1. RDSはデータベースコネクションを張らないといけないから
  - Lambdaは一回処理したら終了するというステートレスな性質のためコネクションを維持できない
2. RDSを使う場合はLambdaをVPCに配置しないといけないから
- RDSとLambdaを使いたい場合は、DynamoDBにいったん格納してからDynamoDBがLambdaをキックしてRDSに格納するという手順で行う

![2020-12-06 12 22のイメージ](https://user-images.githubusercontent.com/53253817/101270589-b5994700-37bd-11eb-934c-3eef63388322.jpeg)
