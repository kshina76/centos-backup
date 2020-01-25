
/*
・IAMとはリソースに紐づける権限設定のサービスの名前の事。IAMポリシーといわれたらIAMというサービスのポリシーという意味。
・ポリシーはリソース(EC2とか)にアクセスするための権限設定で、AWSが最初から用意してくれている。
・ロールはAWSのリソースに付与するもので、ポリシーをグルーピングしたもの。
つまり、複数のポリシーをロールでまとめて、ロール自体をリソースに割り当てるというイメージ。
・S3にはバケットポリシーという別のポリシーも使わないといけないので注意。なので、S3を扱うときはこのモジュールは使わない。

・terraformで書くときは以下のような内包関係になっている。
ポリシードキュメント＜ポリシー＜ロール

・参考文献
https://qiita.com/montama/items/90bb8a3973d101be4690
https://dev.classmethod.jp/cloud/aws/s3-acl-wakewakame/
*/

variable "name" {}
variable "policy" {}
variable "identifier" {}

# ロールを定義する。ロールはポリシーを内包するので、ポリシーを指定する。
# data.aws_iam_policy_document.assume_role.jsonは後で実装してある。
resource "aws_iam_role" "default" {
  name = var.name
  assume_role_policy = data.aws_iam_policy_document.assume_role.json

}

# ポリシードキュメントの定義。これがポリシーの実体になって、操作するリソース名などを定義する。
data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type = "Service"
      identifiers = [var.identifier]
    }
  }
}

# ここはポリシードキュメントを入れておくための入れ物を定義する。これをポリシーという。
resource "aws_iam_policy" "default" {
  name = var.name
  policy = var.policy
}

# 最後はロールにポリシーをアタッチすることで完成させる。
resource "aws_iam_role_policy_attachment" "default" {
  role = aws_iam_role.default.name
  policy_arn = aws_iam_policy.default.arn
}

output "iam_role_arn" {
  value = aws_iam_role.default.arn
}

output "iam_role_name" {
  value = aws_iam_role.default.name
}