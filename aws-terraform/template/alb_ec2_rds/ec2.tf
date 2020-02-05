
# EC2 for Web-server on AZ-a
resource "aws_instance" "a" {
  ami                    ="ami-0c3fd0f5d33134a76"
  vpc_security_group_ids =[aws_security_group.for_webserver_ec2.id]
  instance_type          ="t2.micro"
  subnet_id              = aws_subnet.public_a_web.id
  user_data = <<EOF
  #!/bin/bash
  yum install -y httpd
  yum install -y mysql
  systemctl start httpd
  systemctl enable httpd
  usermod -a -G apache ec2-user
  chown -R ec2-user:apache /var/www
  chmod 2775 /var/www
  find /var/www -type d -exec chmod 2775 {} \;
  find /var/www -type f -exec chmod 0664 {} \;
  echo `hostname` > /var/www/html/index.html
  EOF
  depends_on = [aws_security_group.for_webserver_ec2]
}

# EC2 for Web-server on AZ-c
resource "aws_instance" "c" {
  ami                    ="ami-0c3fd0f5d33134a76"
  vpc_security_group_ids =[aws_security_group.for_webserver_ec2.id]
  instance_type          ="t2.micro"
  subnet_id              = aws_subnet.public_c_web.id
  user_data = <<EOF
  #!/bin/bash
  yum update -y
  yum install -y httpd
  yum install -y mysql
  systemctl start httpd
  systemctl enable httpd
  usermod -a -G apache ec2-user
  chown -R ec2-user:apache /var/www
  chmod 2775 /var/www
  find /var/www -type d -exec chmod 2775 {} \;
  find /var/www -type f -exec chmod 0664 {} \;
  echo `hostname` > /var/www/html/index.html
  EOF
  depends_on = [aws_security_group.for_webserver_ec2]
}

# SG for EC2
resource "aws_security_group" "for_webserver_ec2" {
    name ="for-ec2"
    vpc_id= aws_vpc.example.id
    ingress{
        from_port = 80
        to_port   = 80
        protocol  = "tcp"
        security_groups =[aws_security_group.alb.id]
    }
   egress{
       from_port  = 0
       to_port    = 0
       protocol   = "-1"
       cidr_blocks=["0.0.0.0/0"]
   }
   depends_on = [aws_security_group.alb]
}