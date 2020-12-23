# IAM関連まとめ
- ポリシーがわかりやすい
  - https://devlog.arksystems.co.jp/2020/03/12/9338/
- IAMロール、信頼ポリシー、assume role、などがめちゃくちゃわかりやすい
  - https://dev.classmethod.jp/articles/iam-role-passrole-assumerole/

## 1. IAMの種類まとめ
- IAMユーザー: 人に与えられる
- IAMロール: サービス(Facebook、AWSサービス、etc)やプログラムやIAM(IAMユーザ、IAMグループ、他のIAMロール)や他のAWSアカウントに与えられる
  - よく誤解される点としてEC2やLambdaだけに与えるものではないので注意
  - IAMロールはお面のようなもので、複数ポリシーを持っている。しかし、IAMロールだけでは力を発揮することができない。IAMロールのお面を「サービス、プログラム、IAM、アカウント、etc」にかぶせることで、一時的に力(IAMロールに設定された複数ポリシーの権限の力)を発揮する。
- IAMグループ: IAMユーザーはIAMグループとしてグループにまとめられる
- IAMポリシー: 実行者(ユーザー、ロール、グループ)がどのサービスにアクセスできるか、権限を設定する機能

![awsaccount-IAMuser-IAMgroup-IAMRole-hikaku-image](https://user-images.githubusercontent.com/53253817/102968752-ce348b80-4537-11eb-9630-543d454c426e.png)

## 2. IAMポリシーの種類まとめ
- カスタマーポリシー
  - ユーザーが作成した再利用可能なポリシー
  - 複数のIAMユーザー、IAMグループ、IAMロール間で共有可能
- AWS管理ポリシー
  - AWSが用意している再利用可能なポリシー
  - 複数のIAMユーザー、IAMグループ、IAMロール間で共有可能
- インラインポリシー
  - 各IAMユーザー(やIAMグループ、IAMロール)専用にユーザーが個別作成するポリシー

### 2-2. アイデンティティポリシー(ユーザベースポリシー)
- 実行者(IAMユーザー、IAMロール、IAMグループ)が「何をできるか」の形で設定するポリシー
- アイデンティティポリシーは、主体となる実行者は明記しない
  - なぜかと言うと、アタッチした実行者が主体となることは明らかだから
- カスタマーポリシー、管理ポリシー、インラインポリシーのどれでも付与可能
### 2-3. リソースベースのポリシー
- 操作される側(サーバやフォルダなど)に対し「何を許可するか」の形で設定するもの
- アイデンティティベースと違って操作されるモノを明記しないといけない
- リソースベースのポリシーは、インラインポリシーしか作成できない
### 2-4. 信頼ポリシー
- IAMロールにのみ使うポリシー
- IAMロールの権限移譲操作に特化したポリシー
- https://dev.classmethod.jp/articles/aws-iam-policy/

## 3. Assume Roleとは
- AssumeRoleはRoleArnを入力するとCredentialsを返すAPI
- RoleArnは、IAM Roleの一意な名前で、arn:aws:iam::123456789012:role/role-nameといった文字列。返されるCredentialsは一時キーで、有効期限は1時間
- ロールに設定された権限を持った一時キーを入手することを「役割(role)の引き受け(assume)」
- 以下がわかりやすいので、以下を見て理解する
  - https://dev.classmethod.jp/articles/iam-role-and-assumerole/
  - https://dev.classmethod.jp/articles/aws-iam-policy/

![PassRoleAssumeRole](https://user-images.githubusercontent.com/53253817/102969997-0ccb4580-453a-11eb-9890-ec34de4a7b6a.jpeg)
