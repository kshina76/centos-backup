
# ロードバランサを定義するload_balancer_typeでnetworkを指定するとNLBにすることもできる。
# internalはtrueにするとVPC内部向け。falseにするとインターネット向け。
resource "aws_lb" "example" {
  name                       = "example"
  load_balancer_type         = "application"
  internal                   = false
  idle_timeout               = 60
  enable_deletion_protection = false

  # ALBが属するサブネットを指定する。パブリックサブネットの0,1に属するリソースにロードバランシングできるようになる。
  subnets = [
    aws_subnet.public_0.id,
    aws_subnet.public_1.id,
  ]

  # logging.tfで定義しているs3バケットを指定する。アクセスログの保存をすることができる。
  access_logs {
    bucket  = aws_s3_bucket.alb_log.id
    enabled = true
  }

  # lbはエンドポイントになるのでポート80,443を開けないといけない。加えてリダイレクトように8080も開けておく。
  # 作成したmoduleを使う。
  security_groups = [
    module.http_sg.security_group_id,
    module.https_sg.security_group_id,
    module.http_redirect_sg.security_group_id,
  ]
}

# lbのパブリックIPのDNSを標準出力する
output "alb_dns_name" {
  value = aws_lb.example.dns_name
}

# セキュリティグループのmoduleを使用する 
module "http_sg" {
  source      = "./security_group"
  name        = "http-sg"
  vpc_id      = aws_vpc.example.id
  port        = 80
  cidr_blocks = ["0.0.0.0/0"]
}
module "https_sg" {
  source      = "./security_group"
  name        = "https-sg"
  vpc_id      = aws_vpc.example.id
  port        = 443
  cidr_blocks = ["0.0.0.0/0"]
}
module "http_redirect_sg" {
  source      = "./security_group"
  name        = "http-redirect-sg"
  vpc_id      = aws_vpc.example.id
  port        = 8080
  cidr_blocks = ["0.0.0.0/0"]
}

# リスナーの定義
# protocolはhttpかhttpsのどちらかをサポートしている
# load_balancer_arnはid的なものだと思う。attributeがarnなのとidの違いはよく分からん
resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.example.arn
  port              = "80"
  protocol          = "HTTP"

  # デフォルトアクションforward,fixed-response,redirectを指定できる
  default_action {
    type = "fixed-response"

    fixed_response {
      content_type = "text/plain"
      message_body = "これはHTTPです"
      status_code  = "200"
    }
  }
}

