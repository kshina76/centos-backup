
# AWS プロバイダの設定
provider "aws" {
  region = "ap-northeast-1"
  version = "2.20.0"
}

# terrafromのバージョン指定
terraform {
  required_version = ">=0.12.5"
}


data "aws_availability_zones" "available" {}

variable "project" {
  default = "eks"
}

variable "environment" {
  default = "dev"
}

variable "vpc_cidr_block" {
  default = "10.0.0.0/16"
}

variable "num_subnets" {
  default = 2
}

variable "instance_type" {
  default = "t2.small"
}

variable "desired_capacity" {
  default = 2
}

variable "max_size" {
  default = 2
}

variable "min_size" {
  default = 2
}

variable "key_name" {
  default = "KEY"
}

locals {
  base_tags = {
    Project     = "${var.project}"
    Terraform   = "true"
    Environment = "${var.environment}"
  }

  default_tags    = "${merge(local.base_tags, map("kubernetes.io/cluster/${local.cluster_name}", "shared"))}"
  base_name       = "${var.project}-${var.environment}"
  cluster_name    = "${local.base_name}-cluster"
  cluster_version = "1.12"
}