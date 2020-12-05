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

#### 開発者用のIAMユーザ

#### 
