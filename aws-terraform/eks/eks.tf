#resource "aws_security_group" "demo-cluster" {
#  name        = "terraform-eks-demo-cluster"
#  description = "Cluster communication with worker nodes"
#  vpc_id      = aws_vpc.eks-test-clueter-vpc.id

#  egress {
#    from_port   = 0
#    to_port     = 0
#    protocol    = "-1"
#    cidr_blocks = ["0.0.0.0/0"]
#  }

#  tags = {
#    Name = "terraform-eks-demo"
#  }
#}

#resource "aws_security_group_rule" "demo-cluster-ingress-workstation-https" {
#  cidr_blocks       = [local.workstation-external-cidr]
#  description       = "Allow workstation to communicate with the cluster API Server"
#  from_port         = 443
#  protocol          = "tcp"
#  security_group_id = aws_security_group.demo-cluster.id
#  to_port           = 443
#  type              = "ingress"
#}

resource "aws_eks_cluster" "test-cluster" {
    name     = "test-cluster"
    role_arn = aws_iam_role.eks-test-cluster-role.arn
    depends_on = [
        aws_iam_role_policy_attachment.eks-test-cluster-role-AmazonEKSClusterPolicy,
        aws_iam_role_policy_attachment.eks-test-cluster-role-AmazonEKSServicePolicy,
    ]

    version  = "1.14"

    vpc_config {
 #       security_group_ids = [aws_security_group.demo-cluster.id]
        subnet_ids = aws_subnet.eks-test-cluster-subnet[*].id
        endpoint_public_access = true
    }
}

resource "aws_eks_node_group" "test-cluster-node-group" {
    cluster_name    = aws_eks_cluster.test-cluster.name
    node_group_name = "test-cluster-node-group"
    node_role_arn   = aws_iam_role.eks-test-cluster-node-role.arn
    subnet_ids      = aws_subnet.eks-test-cluster-subnet[*].id

    depends_on = [
        aws_iam_role_policy_attachment.eks-test-cluster-node-role-AmazonEKSWorkerNodePolicy,
        aws_iam_role_policy_attachment.eks-test-cluster-node-role-AmazonEKS_CNI_Policy,
        aws_iam_role_policy_attachment.eks-test-cluster-node-role-AmazonEC2ContainerRegistryReadOnly,
    ]

    scaling_config {
        desired_size = 3
        max_size     = 3
        min_size     = 3
    }
}
