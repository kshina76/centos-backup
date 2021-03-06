# AWSインフラ活用大全のP42の構成
- 進め方
  - terraformの書籍を見ながら進める
  - 実際に書くときには公式ドキュメントの書き方を参照する
  - 作るものはAWS大全の本を進めながら決める

## terraformでまず確認すること
1. `terraform init`を実行しておく
  - `.terraform.lock.hcl`というファイルにawsのproviderのバージョンが明記されているので、あとで使う
2. providerの設定
  - versionは1で確認したバージョンを明記する
  - profileは`aws configure --profile`で設定した時の名前を指定
    - これによってcredential情報をterraformから使えるようになる

  ```
  terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 3.22.0"
      }
    }
  }
  provider "aws" {
    profile = "test-terraform"
    region  = "ap-northeast-1"
  }
  ```

## terraformのコマンド
### 実行
1. `terraform init`
  - 初回のみ
2. `terraform plan`
  - 差分やエラーを確認
3. `terraform apply`
  - リソースを作成
4. `terraform destroy`
  - リソースを削除


## 構成内容
- P42を参照

## 開発手順
- 途中までコンソールで作ってから、terraformでコード化する
  - 例えばEC2が2台の冗長構成を作りたかったら、まずVPCとサブネットまでコンソールで作って確認して、そこまでをterraformでコード化して、またコンソールに戻るといった漢字の進め方
