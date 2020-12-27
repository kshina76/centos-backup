

# ポリシードキュメントの定義
/*
定義する権限は以下のことを実現するためにいっぱい必要。
・ビルド出力アーティファクトを保存するためのS3操作権限
・ビルドログを出力するためのCloudWatch Logs操作権限
・DockerイメージをプッシュするためのECR操作権限
※ビルド出力アーティファクトとはCodeBuildがビルド時に生成した成果物となるファイルのこと。
*/
data "aws_iam_policy_document" "codebuild" {
  statement {
    effect    = "Allow"
    resources = ["*"]

    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:GetObjectVersion",
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
      "ecr:GetAuthorizationToken",
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:GetRepositoryPolicy",
      "ecr:DescribeRepositories",
      "ecr:ListImages",
      "ecr:DescribeImages",
      "ecr:BatchGetImage",
      "ecr:InitiateLayerUpload",
      "ecr:UploadLayerPart",
      "ecr:CompleteLayerUpload",
      "ecr:PutImage",
    ]
  }
}

# CodeBuild用のIAMロールの定義
module "codebuild_role" {
  source     = "./iam_role"
  name       = "codebuild"
  identifier = "codebuild.amazonaws.com"
  policy     = data.aws_iam_policy_document.codebuild.json
}

# CodeBuildプロジェクトの定義
# CodePipelineから起動するように設定する
resource "aws_codebuild_project" "example" {
  name         = "example"
  service_role = module.codebuild_role.iam_role_arn

  # ビルド対称のファイルを定義
  source {
    type = "CODEPIPELINE"
  }

  # ビルド出力アーティファクトの格納先を指定
  artifacts {
    type = "CODEPIPELINE"
  }

  # ビルドをする環境設
  # privileged_modeはビルド時にdockerコマンドを使うので、そのための特権を付与する
  environment {
    type            = "LINUX_CONTAINER"
    compute_type    = "BUILD_GENERAL1_SMALL"
    image           = "aws/codebuild/ubuntu-base:14.04"
    privileged_mode = true
  }
}


