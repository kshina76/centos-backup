

# CloudWatchLogsを定義
# retention_in_daysでログの保持する期間を設定する
resource "aws_cloudwatch_log_group" "for_ecs" {
  name              = "/ecs/example"
  retention_in_days = 180
}

# AmazonECSTaskExecutionRolePolicyというaws管理ポリシーを使う。cloudwatchlogsやECSの操作権限を持っている
# 先にポリシーを宣言しているのは、後で継承して使うから。これは直接ポリシーに使わない。
data "aws_iam_policy" "ecs_task_execution_role_policy" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# source_jsonでさっき定義したポリシーを継承できる。
# 継承して新たなポリシーを作成する。
data "aws_iam_policy_document" "ecs_task_execution" {
  source_json = data.aws_iam_policy.ecs_task_execution_role_policy.policy

  statement {
    effect    = "Allow"
    actions   = ["ssm:GetParameters", "kms:Decrypt"]
    resources = ["*"]
  }
}

# identifierでecs-task-executionを指定して、このIAMロールをECSで使うことを宣言してる。
module "ecs_task_execution_role" {
  source     = "./iam_role"
  name       = "ecs-task-execution"
  identifier = "ecs-tasks.amazonaws.com"
  policy     = data.aws_iam_policy_document.ecs_task_execution.json
}

