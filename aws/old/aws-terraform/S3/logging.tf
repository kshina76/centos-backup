
# albからs3バケットに書き込むときに必要となる書き込み権限の事
resource "aws_s3_bucket" "alb_log" {
  bucket = "alb-log-pragmatic-terraform-kshina3"
  
  # ログローテーションで180日を経過したlogは自動的に削除するというような機能になっている
  lifecycle_rule {
    enabled = true

    expiration {
      days = "180"
    }
  }
}

# バケットポリシーというもの。IAMポリシーとは違うからiamモジュールを使っていない。
# バケットポリシーはALBのようなほかのリソースからの読み書きを許可するために使う。
# バケットのidとIAMポリシードキュメントを指定して、ロールのような役割を担っているので、ロールの定義がいらない。
resource "aws_s3_bucket_policy" "alb_log" {
  bucket = aws_s3_bucket.alb_log.id
  policy = data.aws_iam_policy_document.alb_log.json
}

# S3を有効にするには、バケットポリシーだけでなくてIAMポリシーも許可されていないと使えない。
data "aws_iam_policy_document" "alb_log" {
  statement {
    effect = "Allow"
    actions = ["s3:PutObject"]
    resources = ["arn:aws:s3:::${aws_s3_bucket.alb_log.id}/*"]

    principals {
      type = "AWS"
      identifiers = ["582318560864"]
    }
  }
}