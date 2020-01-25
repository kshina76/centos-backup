

# ネットワーク
resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"

  instance_tenancy     = "default"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "example"
  }
}

# パブリックサブネット
resource "aws_subnet" "public_0" {
  vpc_id                  = aws_vpc.example.id
  cidr_block              = "10.0.0.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = true
}
resource "aws_internet_gateway" "example" {
  vpc_id = aws_vpc.example.id
}
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.example.id
}
resource "aws_route" "public" {
  route_table_id         = aws_route_table.public.id
  gateway_id             = aws_internet_gateway.example.id
  destination_cidr_block = "0.0.0.0/0"
}
resource "aws_route_table_association" "public_0" {
  subnet_id      = aws_subnet.public_0.id
  route_table_id = aws_route_table.public.id
}

# S3 bucket for emr logs
resource "aws_s3_bucket" "emr-log" {
  bucket        = "emr-logs-kshina76"
  acl           = "private"
  force_destroy = true
}