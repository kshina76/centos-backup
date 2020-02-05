# AWS プロバイダの設定
provider "aws" {
  region = "ap-northeast-1"
  version = "2.20.0"
}

# terrafromのバージョン指定
#terraform {
#  required_version = ">=0.12.5"
#}


# vpc
resource "aws_vpc" "example" {
    cidr_block = "10.0.0.0/16"
    instance_tenancy = "default"
    enable_dns_hostnames = true
    enable_dns_support   = true
}

# public subnet for alb
resource "aws_subnet" "public_a" {
    vpc_id                  = aws_vpc.example.id
    cidr_block              = "10.0.1.0/24"
    map_public_ip_on_launch = true
    availability_zone       = "ap-northeast-1a"
}
resource "aws_subnet" "public_c" {
    vpc_id                  = aws_vpc.example.id
    cidr_block              = "10.0.2.0/24"
    map_public_ip_on_launch = true
    availability_zone       = "ap-northeast-1c"
}

# public subnet for web server
resource "aws_subnet" "public_a_web" {
    vpc_id                  = aws_vpc.example.id
    cidr_block              = "10.0.3.0/24"
    map_public_ip_on_launch = true
    availability_zone       = "ap-northeast-1a"
}
resource "aws_subnet" "public_c_web" {
    vpc_id                  = aws_vpc.example.id
    cidr_block              = "10.0.4.0/24"
    map_public_ip_on_launch = true
    availability_zone       = "ap-northeast-1c"
}

# Internet gateway 
resource "aws_internet_gateway" "example" {
    vpc_id                  = aws_vpc.example.id
}

# make route-table
resource "aws_route_table" "public" {
    vpc_id = aws_vpc.example.id
}
resource "aws_route" "public" {
    route_table_id = aws_route_table.public.id
    gateway_id     = aws_internet_gateway.example.id
    destination_cidr_block = "0.0.0.0/0" 
}

# route-table associate to internet gateway
resource "aws_route_table_association" "public_a" {
    subnet_id      = aws_subnet.public_a.id
    route_table_id = aws_route_table.public.id
}
resource "aws_route_table_association" "public_c" {
    subnet_id      = aws_subnet.public_c.id
    route_table_id = aws_route_table.public.id
}
resource "aws_route_table_association" "public_a_web" {
    subnet_id      = aws_subnet.public_a_web.id
    route_table_id = aws_route_table.public.id
}
resource "aws_route_table_association" "public_c_web" {
    subnet_id      = aws_subnet.public_c_web.id
    route_table_id = aws_route_table.public.id
}

# private subnet for RDS
resource "aws_subnet" "private_a" {
    vpc_id                  = aws_vpc.example.id
    cidr_block              = "10.0.5.0/24"
    map_public_ip_on_launch = false
    availability_zone       = "ap-northeast-1a"
}
resource "aws_subnet" "private_c" {
    vpc_id                  = aws_vpc.example.id
    cidr_block              = "10.0.6.0/24"
    map_public_ip_on_launch = false
    availability_zone       = "ap-northeast-1c"
}
