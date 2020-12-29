resource "aws_vpc" "wordpress_vpc" {
  cidr_block       = "10.1.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "test-vpc"
  }
}

output "vpc_id_output" {
  value = aws_vpc.wordpress_vpc.id
}
