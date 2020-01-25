
# AWS プロバイダの設定
provider "aws" {
  region = "ap-northeast-1"
  version = "2.20.0"  
}

terraform {
  required_version = ">=0.12.5"
}