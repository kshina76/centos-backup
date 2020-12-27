
provider "aws" {
    region = "ap-northeast-1"
}

# S3バケットの定義
resource "aws_s3_bucket" "private" {
  # 任意のbucketの名前。もし指定しなかったらterraformがランダムな名前を付ける
  # この名前は全世界で一意にしなければいけない
  bucket = "private-pragmatic-terraform-kshina"

  # バケット内の値を複数持つことでバージョンを上げたときに障害があったら戻すことができる機能(AWS S3の機能)
  versioning {
    enabled = true
  }

  # バケットに入れるデータを入れる前に暗号化してから入れて、出すときに復号するためのルール(これは絶対入れる)
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

# ブロックパブリックアクセスは予期しないで全世界に公開されないようにする機能。理由が無い限りすべて有効にする
resource "aws_s3_bucket_public_access_block" "private" {
  bucket                  = aws_s3_bucket.private.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

