
/*
route53
・DNSサービス
・ドメインの登録はterraformからは行えないのでAWSコンソールから行ってからterraformを実行するようにする
・ドメインの登録をするとホストゾーンが自動的に作成される。
*/

# 自動作成されたホストゾーンの参照
# ホストゾーンはDNSレコードを束ねてくれるもの
data "aws_route53_zone" "example" {
  name = "kshina76.com"
}

# DNSレコードの定義
# typeはAレコードやCNAMEレコードなどが使われる。AWS独自のaliasを使うならAレコードを表すAを指定する。
# aliasにはALBの名前とゾーンIDを指定すると、(ドメイン名→ALBを示すIPアドレス)のように名前解決される。
# aliasにS3バケットをしてすると、S3バケットに名前解決されるようになっている。
resource "aws_route53_record" "example" {
  zone_id = data.aws_route53_zone.example.zone_id
  name    = data.aws_route53_zone.example.name
  type    = "A"

  alias {
    name                   = aws_lb.example.dns_name
    zone_id                = aws_lb.example.zone_id
    evaluate_target_health = true
  }
}
output "domain_name" {
  value = aws_route53_record.example.name
}

# SSL証明書の定義。AWSではACMというサービスでSSL証明書を扱うことができる。
# ACMはSSL証明書を管理してくれるマネージドサービスになっていて、SSL証明書の更新を忘れるなどの悲劇が無いようになっている。
# subject_alternative_namesは複数のドメインのSSL証明書を作成したいときにtest.sample.comのように追加する。いらない場合は空リストで。
# validation_methodはドメインの所有権の検証方式を決める。DNS検証かEメール検証を選択できるが、自動でSSLを更新したい場合はDNSを選択
# lifecycleは新しい証明書に置き換えるときの挙動
resource "aws_acm_certificate" "example" {
  domain_name               = data.aws_route53_zone.example.name
  subject_alternative_names = []
  validation_method         = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

# ここはSSLを学んでいかないとわからない、、、
resource "aws_route53_record" "example_certificate" {
  name    = aws_acm_certificate.example.domain_validation_options[0].resource_record_name
  type    = aws_acm_certificate.example.domain_validation_options[0].resource_record_type
  records = [aws_acm_certificate.example.domain_validation_options[0].resource_record_value]
  zone_id = data.aws_route53_zone.example.id
  ttl     = 60
}

# apply時にSSL検証が完了するまで待ってくれる。
resource "aws_acm_certificate_validation" "example" {
  certificate_arn         = aws_acm_certificate.example.arn
  validation_record_fqdns = [aws_route53_record.example_certificate.fqdn]
}