provider "aws" {
  region = "ap-northeast-1"
}

variable "proxy_intance_type" {
  default = "t2.micro"
}

variable "main_intance_type" {
  default = "t2.micro"
}

variable "proxy_key_pub" {
  default = "ec2_for_emr"
}

variable "main_key_pub" {
  default = "ec2_for_emr"
}