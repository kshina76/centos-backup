
# ALB
resource "aws_lb" "for_webserver" {
  name               = "webserver-alb"
  internal           = false             #falseを指定するとインターネット向け,trueを指定すると内部向け
  load_balancer_type = "application"

  security_groups    = [
    aws_security_group.alb.id
  ]

  subnets            = [
      aws_subnet.public_a.id,
      aws_subnet.public_c.id,
  ]
  depends_on = [aws_security_group.alb]
}

# SG for ALB
resource "aws_security_group" "alb" {
    name ="alb"
    vpc_id= aws_vpc.example.id
    ingress{
        from_port = 80
        to_port   = 80
        protocol  = "tcp"
        cidr_blocks =["0.0.0.0/0"]
    }
   egress{
       from_port  = 0
       to_port    = 0
       protocol   = "-1"
       cidr_blocks=["0.0.0.0/0"]
   }
}

# ALB listener
resource "aws_lb_listener" "for_webserver" {
  load_balancer_arn = aws_lb.for_webserver.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.for_webserver.arn
  }

}

# listener def
resource "aws_lb_listener_rule" "forward" {
  listener_arn = aws_lb_listener.for_webserver.arn
  priority     = 99

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.for_webserver.arn
  }

  condition {
    field = "path-pattern"
    values = ["/*"]
  }
}

# ALB target-group
resource "aws_lb_target_group" "for_webserver" {
  name        = "for-webserver-lb-tg"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = aws_vpc.example.id

  health_check {
        path        = "/index.html"
  }
  depends_on = [aws_lb.for_webserver]
}

# associate target-group with EC2
resource "aws_lb_target_group_attachment" "for_webserver_a" {
  target_group_arn = aws_lb_target_group.for_webserver.arn
  target_id        = aws_instance.a.id
  port             = 80
}

resource "aws_lb_target_group_attachment" "for_webserver_c" {
  target_group_arn = aws_lb_target_group.for_webserver.arn
  target_id        = aws_instance.c.id
  port             = 80
}