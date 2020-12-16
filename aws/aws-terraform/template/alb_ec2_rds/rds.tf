
# define RDS
resource "aws_db_instance" "default" {
  allocated_storage      = 20
  storage_type           = "gp2"
  engine                 = "mysql"
  engine_version         = "5.7"
  instance_class         = "db.t2.micro"
  name                   = "mydb"
  username               = "foo"
  password               = "foobarbaz"
  parameter_group_name   = "default.mysql5.7"
  multi_az               = true
  db_subnet_group_name   = aws_db_subnet_group.dbsubnet.name
  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.for_rds.id]
  depends_on = [aws_security_group.for_rds]
}

# define db-subnet-group(maybe db-replication)
resource "aws_db_subnet_group" "dbsubnet" {
  name       = "main"
  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_c.id]
  depends_on = [aws_subnet.private_a, aws_subnet.private_c]
  tags = {
    Name = "My DB subnet group"
  }
}

# SG for RDS
resource "aws_security_group" "for_rds" {
    name ="for-rds"
    vpc_id= aws_vpc.example.id
    depends_on = [aws_vpc.example]
    ingress{
        from_port = 3306
        to_port   = 3306
        protocol  = "tcp"
        cidr_blocks = [aws_vpc.example.cidr_block]
    }
   egress{
       from_port  = 0
       to_port    = 0
       protocol   = "-1"
       cidr_blocks = ["0.0.0.0/0"]
   }
}