terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.22.0"
    }
  }
}

provider "aws" {
  profile = "test-terraform"
  region  = "ap-northeast-1"
}

module "network_vpc" {
  source = "./network"
}

module "subnet_vpc" {
  source = "./subnet"
  vpc_id = module.network_vpc.vpc_id_output
}
