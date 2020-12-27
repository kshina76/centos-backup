provider "aws" {
    region = "ap-northeast-1"
}

# VPCを作成
resource "aws_vpc" "example" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "example"
  }
}

# パブリックサブネットを定義する
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.0.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "ap-northeast-1a"
}

# インターネットゲートウェイ(IGW)を作成する
resource "aws_internet_gateway" "example" {
  vpc_id = aws_vpc.example.id
}

# ルートテーブルを作成するときはVPCを指定するが、ここでメインルートテーブル(デフォルトルートテーブル)を作ってるわけではない。
# メインルートテーブルはVPCを作ったときに暗黙的にできている。
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.example.id
}

# ルートテーブルの内容を決める
resource "aws_route" "public" {
  route_table_id         = aws_route_table.public.id
  gateway_id             = aws_internet_gateway.example.id
  destination_cidr_block = "0.0.0.0/0"
}

# ルーティングをする。ルートテーブルをどのサブネットに関連付けるかを指定する。ここで指定しないと暗黙的にデフォルトルートテーブルが指定される。
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# プライベートサブネットを作成する。map_public_ip_on_launchはtrueにするとサブネットにパブリックipが割り当てられる。
resource "aws_subnet" "private" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.64.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = false
}

# プライベートサブネット用のルートテーブルを定義する
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.example.id
}

# ルートテーブルの中身を定義していないが紐づけることはもちろんできる。ルートテーブルは作った時点でローカルのルーティングだけされている。
resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

# NATゲートウェイにはEIPという静的なパブリックIPを振る機能でIPを振る必要がある。AWSではパブリックIPが起動するたびに変わってしまうから。
# EIPは暗黙的にIGWに紐づいているからdepend_onを付けている。これによってIGWができてから作成するように保障される。
resource "aws_eip" "nat_gateway" {
  vpc        = true
  depends_on = [aws_internet_gateway.example]
}

# NATゲートウェイを作成して、allocation_idでEIPを紐づけて、パブリックサブネットに配置する。
# NATゲートウェイは暗黙的にIGWに紐づいているからdepend_onを付けている。
resource "aws_nat_gateway" "example" {
  allocation_id = aws_eip.nat_gateway.id
  subnet_id     = aws_subnet.public.id
  depends_on    = [aws_internet_gateway.example]
}

# プライベートサブネットのルートテーブルを編集してNATゲートウェイにルーティングする。ルートテーブルは紐づけた後でも編集可能。
resource "aws_route" "private" {
  route_table_id         = aws_route_table.private.id
  nat_gateway_id         = aws_nat_gateway.example.id
  destination_cidr_block = "0.0.0.0/0"
}

# マルチAZ(二つ目のパブリックサブネット)
resource "aws_subnet" "public_0" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = true
}
# マルチAZ(三つ目のパブリックサブネット)
resource "aws_subnet" "public_1" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "ap-northeast-1c"
  map_public_ip_on_launch = true
}

# マルチAZのパブリックサブネットをIGWが設定されているルートテーブルを紐づける
resource "aws_route_table_association" "public_0" {
  subnet_id      = aws_subnet.public_0.id
  route_table_id = aws_route_table.public.id
}
# 上と同様
resource "aws_route_table_association" "public_1" {
  subnet_id      = aws_subnet.public_1.id
  route_table_id = aws_route_table.public.id
}

# マルチAZ(二つ目のプライベートサブネット)
resource "aws_subnet" "private_0" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.65.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = false
}
# マルチAZ(三つ目のプライベートサブネット)
resource "aws_subnet" "private_1" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.66.0/24"
  availability_zone       = "ap-northeast-1c"
  map_public_ip_on_launch = false
}

# プライベートサブネットはNATゲートウェイも冗長化するのでやる事が多い 
# NATゲートウェイを一つで運用してしまうと、そのAZが死んだときにインターネットにつながらなくなってしまうから重要。
resource "aws_eip" "nat_gateway_0" {
  vpc        = true
  depends_on = [aws_internet_gateway.example]
}
resource "aws_eip" "nat_gateway_1" {
  vpc        = true
  depends_on = [aws_internet_gateway.example]
}
resource "aws_nat_gateway" "nat_gateway_0" {
  allocation_id = aws_eip.nat_gateway_0.id
  subnet_id     = aws_subnet.public_0.id
  depends_on    = [aws_internet_gateway.example]
}
resource "aws_nat_gateway" "nat_gateway_1" {
  allocation_id = aws_eip.nat_gateway_1.id
  subnet_id     = aws_subnet.public_1.id
  depends_on    = [aws_internet_gateway.example]
}

# デフォルトルート(デフォルトゲートウェイの事かな)はルートテーブル一つにつき一つしか定義できない。
# デフォルトゲートウェイは宛先が見つからなかったときに丸投げするところだから複数あるのは普通に考えればおかしい。
# なのでルートテーブルも冗長化する。デフォルトゲートウェイが違ったほうが柔軟性がある。
resource "aws_route_table" "private_0" {
  vpc_id = aws_vpc.example.id
}
resource "aws_route_table" "private_1" {
  vpc_id = aws_vpc.example.id
}
resource "aws_route" "private_0" {
  route_table_id         = aws_route_table.private_0.id
  nat_gateway_id         = aws_nat_gateway.nat_gateway_0.id
  destination_cidr_block = "0.0.0.0/0"
}
resource "aws_route" "private_1" {
  route_table_id         = aws_route_table.private_1.id
  nat_gateway_id         = aws_nat_gateway.nat_gateway_1.id
  destination_cidr_block = "0.0.0.0/0"
}
resource "aws_route_table_association" "private_0" {
  subnet_id      = aws_subnet.private_0.id
  route_table_id = aws_route_table.private_0.id
}
resource "aws_route_table_association" "private_1" {
  subnet_id      = aws_subnet.private_1.id
  route_table_id = aws_route_table.private_1.id
}

# セキュリティグループの枠組みを定義して、インバウンドとアウトバウンドを別々に定義することができる
resource "aws_security_group" "example" {
  name   = "example"
  vpc_id = aws_vpc.example.id
}
resource "aws_security_group_rule" "ingress_example" {
  type              = "ingress"
  from_port         = "80"
  to_port           = "80"
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.example.id
}
resource "aws_security_group_rule" "egress_example" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.example.id
}