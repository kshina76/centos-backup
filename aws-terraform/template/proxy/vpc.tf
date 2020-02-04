# vpc
resource "aws_vpc" "example" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "example"
  }
}



# public subnet for proxy
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.0.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "ap-northeast-1a"
}

# Internet Gateway
resource "aws_internet_gateway" "example" {
  vpc_id = aws_vpc.example.id
}

# define route-table for public-subnet
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.example.id
}
resource "aws_route" "public" {
  route_table_id         = aws_route_table.public.id
  gateway_id             = aws_internet_gateway.example.id
  destination_cidr_block = "0.0.0.0/0"
}
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}



# private subnet
resource "aws_subnet" "private" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.64.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = false
}

# define route-table for private-subnet
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.example.id
}
resource "aws_route" "private" {
  route_table_id         = aws_route_table.private.id
  nat_gateway_id         = aws_nat_gateway.example.id
  destination_cidr_block = "0.0.0.0/0"
}
resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

# nat-gateway
resource "aws_eip" "nat_gateway" {
  vpc        = true
  depends_on = [aws_internet_gateway.example]
}
resource "aws_nat_gateway" "example" {
  allocation_id = aws_eip.nat_gateway.id
  subnet_id     = aws_subnet.public.id
  depends_on    = [aws_internet_gateway.example]
}



# proxy and main server security group
resource "aws_security_group" "example" {
  name   = "example"
  vpc_id = aws_vpc.example.id
}
resource "aws_security_group_rule" "ingress_example" {
  type              = "ingress"
  from_port         = "22"
  to_port           = "22"
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

# 踏み台サーバ
resource "aws_instance" "proxy" {
    ami                         = "ami-045f38c93733dd48d"
    instance_type               = var.proxy_intance_type
    key_name                    = var.proxy_key_pub  # EC2 に登録済の Key Pairs を指定する
    vpc_security_group_ids      = [aws_security_group.example.id]
    subnet_id                   = aws_subnet.public.id
    associate_public_ip_address = "true"
    tags = {
        Name = "proxy_instance"
    }
}

# 作業サーバ
resource "aws_instance" "main" {
    ami                         = "ami-045f38c93733dd48d"
    instance_type               = var.main_intance_type
    key_name                    = var.main_key_pub  # EC2 に登録済の Key Pairs を指定する
    vpc_security_group_ids      = [aws_security_group.example.id]
    subnet_id                   = aws_subnet.private.id
    tags = {
        Name = "main_instance"
    }
}
