

- AWS Lambdaでマイクロサービスを実現
    - 一つ一つのLambdaが一つ一つのマイクロサービスとして動作するイメージだと思う
    - エンドポイントがAPI Gatewayとなる

- Kubernetesでマイクロサービスを実現
    - コンテナとマイクロサービスは相性がいい
        - https://avinton.com/blog/2019/07/micro-services-architecture/

- マイクロサービスは「サーバレス」と「コンテナ」どっちで実現するか？
    - コンテナ
        - Amazon ECS
        - Amazon EKS
        - Amazon Fargate
    - サーバレス
        - Lambda
    - 両方
        - 決められない場合は両方を活用した構成にしてもいい
    - https://dev.classmethod.jp/articles/reinvent-arc214/

- コンテナデザインパターン
    - https://qiita.com/MahoTakara/items/03fc0afe29379026c1f3