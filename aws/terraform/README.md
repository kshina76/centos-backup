# terraform

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

## terraformのawsのドキュメント
- 以下を参考にそれぞれのサービスのコードを書いていく
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs
