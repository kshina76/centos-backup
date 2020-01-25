

# pipelineのポリシードキュメントの定義
/*
定義する操作権限は以下の通り
1.ステージ間でデータを受け渡すためのS3操作権限
2.CodeBuildプロジェクトを起動するためのCOdeBuild操作権限
3.ECSにDockerイメージをデプロイするためのECS操作権限
4.CodeBuildやECSにロールを渡すためのPassRole権限
*/
data "aws_iam_policy_document" "codepipeline" {
  statement {
    effect    = "Allow"
    resources = ["*"]

    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:GetObjectVersion",
      "s3:GetBucketVersioning",
      "codebuild:BatchGetBuilds",
      "codebuild:StartBuild",
      "ecs:DescribeServices",
      "ecs:DescribeTaskDefinition",
      "ecs:DescribeTasks",
      "ecs:ListTasks",
      "ecs:RegisterTaskDefinition",
      "ecs:UpdateService",
      "iam:PassRole",
    ]
  }
}

# IAMロール
module "codepipeline_role" {
  source     = "./iam_role"
  name       = "codepipeline"
  identifier = "codepipeline.amazonaws.com"
  policy     = data.aws_iam_policy_document.codepipeline.json
}

# code pipelineの各ステージ間でのデータの受け渡しに使用するS3バケットを定義する
resource "aws_s3_bucket" "artifact" {
  bucket = "artifact-pragmatic-terraform-on-aws-kshina76"

  lifecycle_rule {
    enabled = true

    expiration {
      days = "180"
    }
  }
}

# CodePipelineの定義
/*
COdepipelineは以下のステージから構成される
1.sourceステージ
    GitHubからソースコードを取得する
2.Buildステージ
    CodeBuildを実行し、ECRにDockerイメージをプッシュする
3.Deployステージ
    ECSへDockerイメージをデプロイする

内容の解説
・sourceステージにはソースコードの取得先のGitHubリポジトリとブランチを指定する。
CodePipeLineの起動はwebhookから行うので、PollSourceChangesはfalseにしている。

・buildステージはさっき実装したCodeBuildを指定する。

・deployステージはデプロイ先のECSクラスタとECSサービスを指定する。
さらに重要なのが、imagedefinitions.jsonというところ。これはbuildspec.ymlの最後に作成しているjsonファイル。

・アーティファクトストアにはさっき作成したS3バケットを指定する
*/
resource "aws_codepipeline" "example" {
  name     = "example"
  role_arn = module.codepipeline_role.iam_role_arn

  stage {
    name = "Source"

    action {
      name             = "Source"
      category         = "Source"
      owner            = "ThirdParty"
      provider         = "GitHub"
      version          = 1
      output_artifacts = ["Source"]

      configuration = {
        Owner                = "kshina76"
        Repo                 = "test-codepipeline"
        Branch               = "master"
        PollForSourceChanges = false
      }
    }
  }

  stage {
    name = "Build"

    action {
      name             = "Build"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = 1
      input_artifacts  = ["Source"]
      output_artifacts = ["Build"]

      configuration = {
        ProjectName = aws_codebuild_project.example.id
      }
    }
  }

  stage {
    name = "Deploy"

    action {
      name            = "Deploy"
      category        = "Deploy"
      owner           = "AWS"
      provider        = "ECS"
      version         = 1
      input_artifacts = ["Build"]

      configuration = {
        ClusterName = aws_ecs_cluster.example.name
        ServiceName = aws_ecs_service.example.name
        FileName    = "imagedefinitions.json"
      }
    }
  }

  artifact_store {
    location = aws_s3_bucket.artifact.id
    type     = "S3"
  }
}

# CodePipeLine Webhookを作成
# githubからwebhookを受け取るために作成する。
# 受け取ったら起動するパイプラインをtarget_pipelineで指定する。
# 最初に実行するアクションをtarget_actionで指定する。
resource "aws_codepipeline_webhook" "example" {
  name            = "example"
  target_pipeline = aws_codepipeline.example.name
  target_action   = "Source"
  authentication  = "GITHUB_HMAC"

  authentication_configuration {
    secret_token = "VeryRandomStringMoreThan20Byte!"
  }

  filter {
    json_path    = "$.ref"
    match_equals = "refs/heads/{Branch}"
  }
}

# おそらく自分のgithubの名前を記述する。
provider "github" {
  organization = "kshina76"
}

# codepipelineではwebhookのリソースを、通知する側と通知される側の2種類実装することになる。ここでは通知する側の設定をする。
resource "github_repository_webhook" "example" {
  repository = "test-codepipeline"

  configuration {
    url          = aws_codepipeline_webhook.example.url
    secret       = "VeryRandomStringMoreThan20Byte!"
    content_type = "json"
    insecure_ssl = false
  }

  # pull requestなども指定できる。
  events = ["push"]
}