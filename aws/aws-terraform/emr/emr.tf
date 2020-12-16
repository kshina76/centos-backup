/*
・aws_iam_instance_profileとは
サービスにロールを付与するときのように、インスタンスにロールを付与するときに使うもの。
https://cross-black777.hatenablog.com/entry/2015/12/04/233206
*/

# S3 bucket for emr logs
resource "aws_s3_bucket" "emr-log" {
  bucket        = "emr-logs-kshina76"
  acl           = "private"
  force_destroy = true
}

# emr cluster
resource "aws_emr_cluster" "cluster" {
  name          = "emr-test-arn"
  release_label = "emr-5.28.0"
  applications  = ["Hadoop"]
  service_role  = aws_iam_role.emr-service-role.arn
  log_uri       = "s3://${aws_s3_bucket.emr-log.id}/elasticmapreduce/"
  master_instance_group {
    instance_type = "m1.medium"
  }
  core_instance_group {
    instance_type  = "m1.medium"
    instance_count = 2
  }
  ec2_attributes {
    key_name                          = aws_key_pair.pub-key.id
    subnet_id                         = aws_subnet.public_0.id
    emr_managed_master_security_group = aws_security_group.emr_master.id
    emr_managed_slave_security_group  = aws_security_group.emr_slave.id
    instance_profile                  = aws_iam_instance_profile.emr-ec2-profile.name
  }
}

# security group
# revoke_rules_on_deleteをtrueにすることでdestory時にvpcが消えない問題が解消できる。
resource "aws_security_group" "emr_master" {
  vpc_id                 = aws_vpc.example.id
  revoke_rules_on_delete = true
}
resource "aws_security_group" "emr_slave" {
  vpc_id                 = aws_vpc.example.id
  revoke_rules_on_delete = true
}

# IAM role for EMR
data "aws_iam_policy_document" "emr-assume-role-policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["elasticmapreduce.amazonaws.com"]
    }
  }
}
resource "aws_iam_role" "emr-service-role" {
  name               = "EMR_DefaultRole"
  assume_role_policy = data.aws_iam_policy_document.emr-assume-role-policy.json
}
resource "aws_iam_role_policy_attachment" "emr-service-role" {
  role       = aws_iam_role.emr-service-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"
}

# IAM Role for EC2
data "aws_iam_policy_document" "ec2-assume-role-policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}
resource "aws_iam_role" "emr-ec2-role" {
  name               = "EMR_EC2_DefaultRole"
  assume_role_policy = data.aws_iam_policy_document.ec2-assume-role-policy.json
}
resource "aws_iam_role_policy_attachment" "emr-ec2-role" {
  role       = aws_iam_role.emr-ec2-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"
}
resource "aws_iam_instance_profile" "emr-ec2-profile" {
  name  = "emr_ec2_profile"
  roles = [aws_iam_role.emr-ec2-role.name]
}
