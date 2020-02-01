
/*
作成の手順
1.ecsクラスタを作成
2.ecsクラスタで動かすタスク定義を作成
3.最後に1,2をまとめる。

*/

# ecsクラスタはコンテナをまとめたタスクを内包するためだけのものなので、名前だけを定義すればいい。
# ecsにおけるタスクは、eksやk8sにおけるポッドみたいなものだと思う。一つのタスクの中で複数のコンテナが動くみたいなので。
resource "aws_ecs_cluster" "example" {
  name = "example"
}

# タスクはタスク定義から生成される。そのタスク定義をここで行う。
# familyはタスク定義名のプレフィックスで、番号を付けたものがタスク定義名になる(example:1のように)
# network_modeはFargateを使うならawsvpcを指定する。
# requires_compatibilitiesは起動タイプ
# container_definitionsはコンテナ定義。yamlではなくjsonで書く。json内のパラメータは色々指定できる。
# execution_role_arn       = module.ecs_task_execution_role.iam_role_arnはdockerコンテナがlogを投げられるように設定している。
resource "aws_ecs_task_definition" "example" {
  family                   = "example"
  cpu                      = "256"
  memory                   = "512"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  container_definitions    = file("./container_definitions.json")
  execution_role_arn       = module.ecs_task_execution_role.iam_role_arn
}

# ECSサービスの定義
# ECSサービスはeksのdeploymentのような存在で、タスクの数を維持してくれり、ALBとコンテナのポートフォワードをしてくれる。
resource "aws_ecs_service" "example" {
  name                              = "example"
  cluster                           = aws_ecs_cluster.example.arn
  task_definition                   = aws_ecs_task_definition.example.arn
  desired_count                     = 2
  launch_type                       = "FARGATE"
  platform_version                  = "1.3.0"
  health_check_grace_period_seconds = 60

  # サブネットとセキュリティグループの設定をする
  # ecs自体はプライベートネットワークで動作して、パブリックIPはALBに振ってあるので、パブリックIPはFalseにしてある。
  network_configuration {
    assign_public_ip = false
    security_groups  = [module.nginx_sg.security_group_id]

    subnets = [
      aws_subnet.private_0.id,
      aws_subnet.private_1.id,
    ]
  }

  # コンテナ定義のjsonに書いた内容を記述する。
  # container_nameはタスク定義に書いたコンテナの中でエンドポイントになるものを選択する
  load_balancer {
    target_group_arn = aws_lb_target_group.example.arn
    container_name   = "web"
    container_port   = 80
  }

  # デプロイのたびにタスク定義が更新されるので、plan時に差分が出ることから、タスク定義の変更を無視するようにしておく。
  lifecycle {
    ignore_changes = [task_definition]
  }
}

module "nginx_sg" {
  source      = "./security_group"
  name        = "nginx-sg"
  vpc_id      = aws_vpc.example.id
  port        = 80
  cidr_blocks = [aws_vpc.example.cidr_block]
}