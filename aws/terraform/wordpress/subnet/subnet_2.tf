resource "aws_subnet" "wordpress_subnet" {
  #vpc_id            = aws_vpc.wordpress_vpc.id
  vpc_id            = var.vpc_id
  cidr_block        = "10.1.0.0/24"
  availability_zone = "ap-northeast-1a"

  tags = {
    Name = "test-subnet"
  }
}
