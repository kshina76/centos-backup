data "aws_availability_zones" "available-zone" {
    state = "available"
}

resource "aws_vpc" "eks-test-clueter-vpc" {
    cidr_block = "10.25.0.0/16"
    enable_dns_support   = true
    enable_dns_hostnames = true

    tags = map(
        "Name", "terraform-eks-node",
        "kubernetes.io/cluster/${var.cluster-name}", "shared",
    )
}

resource "aws_subnet" "eks-test-cluster-subnet" {
    count = length(data.aws_availability_zones.available-zone.zone_ids)

    availability_zone = data.aws_availability_zones.available-zone.names[count.index]
    cidr_block        = cidrsubnet(aws_vpc.eks-test-clueter-vpc.cidr_block, 8, count.index)
    vpc_id            = aws_vpc.eks-test-clueter-vpc.id

    tags = map(
        "Name", "terraform-eks-node",
        "kubernetes.io/cluster/${var.cluster-name}", "shared",
    )
}

resource "aws_internet_gateway" "eks-igw" {
  vpc_id = aws_vpc.eks-test-clueter-vpc.id

  tags = {
    Name = "terraform-eks-igw"
  }
}

resource "aws_route_table" "eks-route" {
  vpc_id = aws_vpc.eks-test-clueter-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.eks-igw.id
  }
}

resource "aws_route_table_association" "route-associate" {
  count = 3

  subnet_id      = aws_subnet.eks-test-cluster-subnet.*.id[count.index]
  route_table_id = aws_route_table.eks-route.id
}
