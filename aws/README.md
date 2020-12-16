# AWSまとめ

## todo
- 一からAWSでサービスを構築する手順を学ぶ
  1. 設計
    - ネットワークの設計
    - 色々なデザインパターンを見つつ最適な設計をする
  2. 設計に沿ってAWSのコンソールで確認しつつ構築
    - AZ, VPC, Subnetなどのネットワークの設定
    - サーバ, DB, 各種ミドルウェアの設定
  3. terraformなどでコード化
  
---

<br></br>

## 学習教材
### 書籍
1. 図解即戦力　Amazon Web Services
  - 借りた
2. Amazon Web Servicesインフラサービス活用大全
  - 借りた
3. Amazon Web Services 基礎からのネットワーク＆サーバー構築　改訂3版 
  - kindleにある
4. Amazon Web Serviceネットワーク入門
  - kindleにある
  - もう一回読む
5. 実践terraform
  - kindleにある
  - もう一回読む
6. 基礎から学ぶサーバレス設計開発
  - 借りた


### 【AWS初心者向け】AWS学習方法まとめ【15時間で達成できる】
- https://qiita.com/toma_shohei/items/b7a001d26bd988d52021

---

<br></br>

## アーキテクチャ
### 個人開発・スタートアップで採用すべきアーキテクチャ
- https://qiita.com/yuno_miyako/items/fad33456d9c32d8f4483

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-234396-1ef837ac-7d97-e04c-4e73-04df56ed1a34](https://user-images.githubusercontent.com/53253817/100833545-86c55d00-34ad-11eb-9d83-97570cb246af.png)

### AWSを使ったモダンなアーキテクチャ
- https://d1.awsstatic.com/whitepapers/ja_JP/modern-application-development-on-aws.pdf

## AWSでのHTTPS化全パターン
- https://recipe.kc-cloud.jp/archives/11067

## Nginx、CloudFrontを使った負荷分散パターン
- https://dev.classmethod.jp/articles/nginx-cdn-redirect-cloudfront-custom-origin/

## AWS Lambdaのディレクトリ構成
- https://dev.classmethod.jp/articles/aws-lamda-deploy-package/

---

<br></br>

# 疑問解消

## OSI参照モデルを実際のAWSのサービスに当てはめると何になるのか？
- トラブルシューティングするときなどに役に立つかも
- AWSサービスのトラブルシューティングの手順(OSI参照モデルの3層からトラブルシューティング)
  1. 簡単にpingなどでそれぞれの層で原因を探る
  2. 1で解決しなかった場合は、AWSのCloudWatchLogsなどに記述されているログを解析する
  3. 2でも解決しなかった場合は、Linuxサーバに入って原因を調査する
    - Linuxのlogのディレクトリ内に記述されている内容
    - nginxなどのミドルウェアのログの確認
    - リソースが枯渇していないかなど
    - 詳しくはISUCONの方にまとめてある
- https://qiita.com/manamin0521/items/1df1ec65637ad1620329

## OSI参照モデルの実際の機能に当てはめる
- http://mya3306.blogspot.com/2016/04/osi.html

## CloudFrontで圧縮できるものできないもの
- https://dev.classmethod.jp/articles/cloudfront-hls-compress-objects-automatically/

## ALBで負荷分散して、CloudFrontでCDNを実現したらリバースプロキシ用途のNginxはいらないのではないか？
### コンテンツ（html）をAppサーバーで作成する場合
- 複雑なルーティングをしたい場合、ALBだけでは辛い
- Nginxでキャッシュコントロールをしたい（コンテンツを圧縮したい）
- ALBのログで良いんじゃね？という意見に対して
- ALBのアクセスログには5分程度のタイムラグがあり、リアルタイムでログを拾いたい場合はWebサーバーがあった方が良い
- ALBのアクセスログでは、クッキーやヘッダ等回収できないログ項目がいくつか存在する
- Appサーバー側でうまくログ出力できるようであれば、考慮不要
- 望まないリクエストの門前払いや、メンテ時のリダイレクト、ゆるくBasic認証を導入など、あると便利なケースが多い
- ただ、上記の予定もなく、全てバックエンドに流すだけであれば撤去できる可能性もあると思います。
### コンテンツ(html)をAppサーバで作成しない場合
- そもそも複雑なルーティングが発生しにくい
- 望まないリクエストの門前払いはWAFで代替可能
- コンテンツ（html）がないため、Nginxでキャッシュコントロールするほどでもない
- APIとして提供するコンテンツ（JSON）を圧縮したい場合はCloudFrontで代替可能
### 参考文献
- https://dev.classmethod.jp/articles/webserver-iru-iranai/
- https://dev.classmethod.jp/articles/alb-redirects/

---

<br></br>

# サービス一覧

## CloudFront
- https://qiita.com/sasasin/items/0f0ec1a90af6295589f9
