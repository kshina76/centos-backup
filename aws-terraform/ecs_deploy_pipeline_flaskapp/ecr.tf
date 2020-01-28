/*
・デプロイメントパイプラインの大枠の流れ
github->CodePipeline->ECS
・Pipelineの中身
Sourceステージ->Buildステージ->Deployステージ
*/

# ECRというコンテナのストレージを定義。dockerhubのaws版みたいなもの。
resource "aws_ecr_repository" "example" {
  name = "example"
}

# ECRライフサイクルポリシーの定義
# ECRリポジトリは保存できる個数が決まっているので、増やしすぎないように設定するなどいろいろな設定ができる。
resource "aws_ecr_lifecycle_policy" "example" {
  repository = aws_ecr_repository.example.name

  policy = <<EOF
  {
    "rules": [
      {
        "rulePriority": 1,
        "description": "Keep last 30 release tagged images",
        "selection": {
          "tagStatus": "tagged",
          "tagPrefixList": ["release"],
          "countType": "imageCountMoreThan",
          "countNumber": 30
        },
        "action": {
          "type": "expire"
        }
      }
    ]
  }
EOF
}






