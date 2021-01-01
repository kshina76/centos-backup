# terraform
## todo
- プロビジョニングツールとの連携を調べる
  - ansibleとterraformの二つを使う意味はなんなのかとか
- プロビジョニングツールの種類
  - https://tapira.hatenablog.com/entry/2015/05/26/124710
- countとfor_eachで複数のリソースを簡単に作成
  - for_eachを使ったほうがいいらしい
  - countは以下のような問題点があるらしい
    - 作るだけなら問題ないが、後々ここ削除したい！となったときに意図しない動きをすることがある
  - どっちの例も出していてわかりやすい
    - https://dev.classmethod.jp/articles/terraform_count_delete/
- dataの使い方

## awscliの導入手順(mac)
- 参考文献
  - https://hacknote.jp/archives/57932/
### 1. awsコンソールでcredentialの発行
- プログラムからアクセスできるようにするためには、このキーが必要になる
- 当たり前だが、誤ってGithubにキーをアップしないように気を付ける
### 2. awscli v2のインストール
- 以下に沿ってインストールする
- https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-mac.html
### 3. awscliのcredentialを設定
1. `aws configure --profile <profile名>`を実行
  - 1で取得したcredentialを入力していく
  - `--profile`で複数のcredentialを管理したいときに、それぞれのcredentialの情報に名前をつけて保管しておくことができる
  - `~/.aws/credentials`に書き込まれている
2. `aws s3 ls --profile <<profile名>`で設定できたか確認する
  - 特にエラーが出ていなければ設定が完了している
- https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-quickstart.html

## terraformの導入手順
- 参考文献
  - https://hacknote.jp/archives/57932/
### 1. tfenvのインストール
1. `brew install tfenv`を実行
2. `tfenv --version`で確認
3. `tfenv list-remote`でインストールできるterraformのバージョンを確認
4. `tfenv install <バージョン>`でterraformをインストール
5. `tfenv use <バージョン>`で使用するterraformをアクティベート
6. `tfenv list`で確認

## vscodeの設定
- 本家のextentionをインストール
- `editor.formatOnSave: ture`をsetting.jsonに記述
- https://ryook.hatenablog.jp/?page=1572255384#vscode設定

<br></br>

## とりあえず覚えておくterraformの用語
- 用語を覚えておくとドキュメントが読みやすくなる

![2020-12-29 14 30のイメージ](https://user-images.githubusercontent.com/53253817/103260807-602e0f80-49e2-11eb-9b06-315d58c1b390.jpeg)

<br></br>

## TerraformとAnsibleの違いと使い分け
### 違い
- Terraform: OS以下のインフラを管理するツール
- Ansible: OSより上の構成を管理するツール
### 使い分け
- Terraform: EC2やRDSやELBやポリシーやLambdaといったインフラを定義して管理するのに使用
- Ansible: Webサーバ(Nginx)やAPサーバ(ASGI)などのインストール、設定をするのに使用
### 注意点
- terraformとansibleは競合しあうツールではなく、互いに補完し合う関係にある
### 参考文献
- https://www.mpon.me/entry/2017/07/07/194459
- https://www.haneca.net/how-to-distinguish-terraform-and-ansible/

<br></br>

## terraformに関連したプロジェクト
- terraformとCI連携で役に立ちそうな記事
  - https://zenn.dev/honmarkhunt/articles/2f03cba1ffe966
### terraformer
- 既存のインフラからterraformのファイルを出力する
- 他のツールだと`terraforming`というものもある
- 最新の記法に対応していない場合などがある
- 以下のような手順で導入すると開発効率がいいかも
  - 「検証でAWSコンソールからリソースを作成」->「良さそうならterraformerでコード生成」->「リファクタリング」
- 以下を参考にすると導入しやすいかも
  - https://beyondjapan.com/blog/2020/05/terraformer-import-existing-infrastructure/
### terratest
- インフラのテストツール
- インフラのテストって何を検証するのか
  - サーバの設定値やパッケージがインストール確認、特定サービスの状態確認、指定ポートでの通信のテストを自動化
- 今までのツールのインフラストラクチャテストツールはコンフィグのプロパティを確認するテスト。（httpd がインストールされて動作しているなど）terratest は「インフラストラクチャが本当に動いてるか？」を確認する
### tfsec
- terraformのセキュリティに問題があるコードを判定してくれるツール
- 導入などに関しては公式のリポジトリのREADMEがわかりやすい
  - https://github.com/tfsec/tfsec

<br></br>

## terraformの書き方などわかったことまとめ
- terraformの記法の公式ドキュメント
  - https://www.terraform.io/docs/configuration/index.html
- terraformのawsの公式ドキュメント
  - https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- terraformのいい記事
  - https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7
  - https://qiita.com/minamijoyo/items/3a7467f70d145ac03324

### 1. 変数を「$」で囲む場合と囲わない場合
- `""`の中で変数を使いたい時は`$`で囲む
  - `Name = "Server ${count.index}"`
- そのほかは囲わない
  - `vpc_id = aws_vpc.wordpress_vpc.id`

### 2. moduleの使い方
- module命令は、他のtfファイルを関数として呼び出すイメージ
- module命令の中のsourceでファイルをimportする
- 引数のようなものを与えることもできる
  - 呼び出される側でvariable命令で引数の変数を定義する
- 返り値のようなものも使える
  - 呼び出される側でoutput命令を使って返り値を定義する
- output命令は、デバッグ用途としても使える
  - outputで指定されたものは、コマンド実行時に指定した属性値がコンソール上に出力させる

### 3. terraformでのディレクトリ間の参照とファイル間の参照
#### 3-1. 同一のディレクトリ内のファイル間の参照
- 特に何もしなくても参照できる

#### 3-2. 異なるディレクトリのmodule間の参照(推奨)
- `main.tf`でmoduleをimportする方法
- importは`main.tf`だけで行うようにすると、モジュール間の依存関係がなくなるから良い
- `main.tf`が異なるディレクトリのモジュール間の橋渡しになるイメージ
- 「outputsは返り値、variablesは引数」という意識をしておくとわかりやすい
- https://www.mpon.me/entry/2016/12/13/030907

```
.
├── main.tf
├── vpc
│   ├── vpc.tf
│   └── outputs.tf
└── subnet
    │── subnet.tf
    └── variables.tf
```

```
# main.tf
module "network_vpc" {
  source = "./network"
}

module "subnet_vpc" {
  source = "./subnet"
  vpc_id = module.network_vpc.vpc_id_output
}
```

```
# vpc.tf
resource "aws_vpc" "wordpress_vpc" {
  cidr_block       = "10.1.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "test-vpc"
  }
}
```

```
# outputs.tf
output "vpc_id_output" {
  value = aws_vpc.wordpress_vpc.id
}
```

```
# subnet.tf
resource "aws_subnet" "wordpress_subnet" {
  vpc_id            = var.vpc_id
  cidr_block        = "10.1.0.0/24"
  availability_zone = "ap-northeast-1a"

  tags = {
    Name = "test-subnet"
  }
}
```

```
# variables.tf
variable "vpc_id" {}
```

#### 3-3. 異なるディレクトリのmodule間の参照(非推奨)
- `subnet.tf`から`vpc.tf`をmoduleを使って呼び出す
- 依存関係としては`subnet->vpc->main`となっている
- この方法はモジュールが増えていくごとにスパゲッティコードになるので、ダメな方法
- https://www.mpon.me/entry/2016/12/13/030907

```
.
├── main.tf
├── vpc
│   └── vpc.tf
└── subnet
    └── subnet.tf
```

```
# main.tf
module "subnet_vpc" {
  source = "./subnet"
}
```

```
# vpc.tf
resource "aws_vpc" "wordpress_vpc" {
  cidr_block       = "10.1.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "test-vpc"
  }
}

output "vpc_id_output" {
  value = aws_vpc.wordpress_vpc.id
}
```

```
# subnet.tf
module "module_vpc" {
  source = "../vpc"
}

resource "aws_subnet" "wordpress_subnet" {
  vpc_id            = module.module_vpc.vpc_id_output
  cidr_block        = "10.1.0.0/24"
  availability_zone = "ap-northeast-1a"

  tags = {
    Name = "test-subnet"
  }
}
```

### 4. variablesの使い方
- プログラミングでいうグローバル変数のようなもの
#### 4-1. 引数一覧
- description: 変数の説明
- type: 変数の型
- default: 変数の初期値
- validation: 変数のバリデーションを行う(値の範囲とか)
  - https://medium.com/@iashishhere/variables-validations-in-terraform-95a12542aa3a
- sensitive: 機密性の高い値をTerraform CLIやTerraform Cloudの出力結果から隠してくれる
  - https://dev.classmethod.jp/articles/terraform-0-14-ga/

```
# 引数有り
variable "availability_zone_names" {
  description = "List of availability zone"
  type        = list(string)
  default     = ["us-west-1a"]
}
```

```
# 引数無し
variable "vpc_id" {}
```

#### 4-2. 使い方
- 変数の参照
  - `var.<変数名>`
- 変数に値を代入する方法4種類
  1. terraformコマンドのコマンド引数で渡す

    ```bash
    $ terraform apply \
    -var 'access_key=AKIAXXXXXXXXXXXXXXXXXX' \
    -var 'secret_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ```

  2. exportで環境変数に設定して渡す
    
    ```bash
    $ export TF_VAR_access_key="AKIAXXXXXXXXXXXXXXXXXX"
    $ export TF_VAR_secret_key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```

  3. tfvarsファイルで代入式を書いて渡す

    ```
    aws_access_key = "AKIAXXXXXXXXXXXXXXXXXX"
    aws_secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```

  4. tfファイルから普通に代入する

#### 4-3. Mapの利用
- デフォルト値は単一の値ではなくMapを指定することも可能
- `var.images.ap-northeast-1`のように参照する

```
variable "images" {
    default = {
        us-east-1 = "ami-1ecae776"
        us-west-2 = "ami-e7527ed7"
        us-west-1 = "ami-d114f295"
        eu-west-1 = "ami-a10897d6"
        eu-central-1 = "ami-a8221fb5"
        ap-southeast-1 = "ami-68d8e93a"
        ap-southeast-2 = "ami-fd9cecc7"
        ap-northeast-1 = "ami-cbf90ecb"
        sa-east-1 = "ami-b52890a8"
    }
}
```

### 5. localsの使い方
- モジュール内でのローカル変数のようなもの
- variableブロックと同じく、変数の宣言を行う
- variableとの違いとしては2点「スコープ」と「関数の使用が可能」な点
  - variableを定義するとスコープがグローバルになることに対し、localsはスコープがmodule内だけになる
  - 以下のようなterraformの組み込み関数をlocalsブロック内で使用することができる
    - https://micpsm.hatenablog.com/entry/2018/12/04/000000

### 6. variableとlocals
#### 6-1. 違い
- スコープ
  - variableはどこからでも参照できるグローバル変数
  - localsはモジュール内だけで参照できるローカル変数
- 関数の使用
  - variableのブロック内は変数の値をそのまま入れることしかできない
  - localsのブロック内は組み込み関数を使用することができる
    - 「1」が渡されたら「true」、「2」が渡されたら「false」というように三項演算子で分岐したりできる
    - https://febc-yamamoto.hatenablog.jp/entry/2018/01/30/185416
    - https://micpsm.hatenablog.com/entry/2018/12/04/000000
#### 6-2. 使い分け
- tfファイル内の変数は基本的に`locals`を使おう
- 特に判定処理は`locals`で明確な名前をつけよう
- `variable`を使うのは外部からのインプットにする場合だけ
  - 引数の変数の宣言だけをvariableで行うということ

### 7. dataの使い方
- 外部のリソースを参照するときに使用する
- 用途
  - AWSが管理しているAMIのIDを取得する
  - AWSが管理しているポリシーのIDとかARNを取得する
  - 外部のプログラムの参照(JSとか)
- https://stackoverflow.com/questions/47721602/how-are-data-sources-used-in-terraform
- https://jkrsp.com/extending-terraform-with-external-data-sources/

### 8. resourceの使い方

#### 8-1. resourceの引数と属性
- 引数は、以下の例の`cidr_block`や`instance_tenancy`や`tags`といったもの
- 属性は、`id`とか`arn`のようなresourceが持っている属性のこと
  - 以下のvpcの属性にアクセスするには`<リソースの種類>.<リソース名>.<属性名>`で指定する
    - `aws_vpc.main.id`
    - `aws_vpc.main.arn`
    - `aws_vpc.main.cidr_block`

```
resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}
```

#### 8-2. lifecycleブロック
- リソースの差分を無視して欲しい時に使用する
  - リソース自体はTerraformで作るんだけど、運用の都合上、手動で設定いじっても無視して欲しい属性はlifecycleブロックで`ignore_changes`に指定すると差分を無視できる
- リソース再生成のときに新しいのを作ってから古いのを削除する
  - `create_before_destroy = true`を指定することで、新しいの作成=>古いの削除の順に実行できる
- リソースのうっかり削除の保護
  - `prevent_destroy`というリソースのうっかり削除を保護するフラグを使用する
  - プロダクションの環境といった、削除してはいけないリソースに設定するといい
- https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7

### 9. for_eachとcount
- リソースを複数作成するときに便利
- countではなくてfor_eachを使おう
- countを使ったやり方の問題点
  - 追加の際に追加分以外の差分が発生する
  - 途中の要素の削除においても、削除分以外の差分が発生する
- https://qiita.com/keiichi-hikita/items/9fd20e8ad6afe4e5ef72
- https://cloudfish.hatenablog.com/entry/2020/02/19/183548
- https://dev.classmethod.jp/articles/terraform-network-variable/

### terraform consoleを使おう
- Terraformには組み込み関数がいくつかあって、知ってるとtfファイルを書く時に便利なことがある
- 文字列とかを加工したくなったら、便利な組み込み関数がないか調べてみる
- その際に関数の挙動がわからなかったら、`terraform console`で挙動を調べることができる

```bash
$ terraform console
> coalesce("","hoge")
hoge
> coalesce("fuga","hoge")
fuga
```

### terraform関連のバージョンを厳密に強制する
- terraformブロックを使用する
- 開発チーム全員のバージョンを厳密に強制することなどが可能になる
- terraformのproviderのバージョンを強制したい場合は`required_providers`
- terraform自体のバージョンを強制したい場合は`required_version`

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.22.0"
    }
  }
}
```

### terraformのディレクトリ分割のベストプラクティス
- パターン3の「環境ごと分離 + module利用パターン」がわかりやすくて良さそうかな
- 各モジュールの`variables.tf`はモジュールの引数となるような変数を定義
- 各モジュールの`outputs.tf`はモジュールの返り値となるものを定義
- enviromentsディレクトリからmoduleをインポートして、それぞれのモジュールの設定を書くといった感じ
- developmentとproductionは環境を分けている
  - tfstateも分けて管理する
- 色々なディレクトリ構成の紹介をしている
  - https://blog.engineer.adways.net/entry/2020/07/03/150000

- https://eng.iridge.jp/post/2017/about-think-terraform-unit-of-execution/

```
terraform
  ├── module
  │   ├── s3
  │   │   ├── variables.tf
  │   │   ├── outputs.tf
  │   │   └── main.tf
  │   ├── rds
  │   │   ├── variables.tf
  │   │   ├── outputs.tf
  │   │   └── main.tf
  │   ├── network
  │   │   ├── variables.tf
  │   │   ├── outputs.tf
  │   │   └── main.tf
  │   ├── iam
  │   │   ├── variables.tf
  │   │   ├── outputs.tf
  │   │   └── main.tf
  │   ├── ec2
  │   │   ├── variables.tf
  │   │   ├── outputs.tf
  │   │   └── main.tf
  │   └── alb
  │       ├── variables.tf
  │       ├── outputs.tf
  │       └── main.tf
  └── environments
      ├── development
      │   ├── alb.tf
      │   ├── ec2.tf
      │   ├── iam.tf
      │   ├── network.tf
      │   ├── provider.tf
      │   ├── rds.tf
      │   ├── s3.tf
      │   ├── tfstate_backend.tf
      │   └── vars.tf
      └── production
          ├── alb.tf
          ├── ec2.tf
          ├── iam.tf
          ├── network.tf
          ├── provider.tf
          ├── rds.tf
          ├── s3.tf
          ├── tfstate_backend.tf
          └── vars.tf
```

### terraformをどの単位で分割するか(案の一つ)
- network
  - ネットワーク系の設定VPC、Subnet、NAT、Route Tables等の設定を管理
- securitygroup
  - セキュリティグループの管理
- iam
  - IAMの管理
- s3
  - S3回りの管理
- backend
  - DB等のデータストア関連のリソースを管理
- webservers
  - webサーバやALB等の管理
- opsservers
  - 運用系のサーバの管理
- https://eng.iridge.jp/post/2017/about-think-terraform-unit-of-execution/

### tfstateを分割して環境ごとに管理する
- productionとdevelopmentの環境を分けるという用途で使うことがある
- 二種類の方法がある
  1. 1つのディレクトリで複数のStateを扱うWorkspaceという機能を使用
  2. 普通にディレクトリを分けて管理する方法
- tfstateをまたいで値を参照する方法
  - `terraform_remote_state`を使用する
