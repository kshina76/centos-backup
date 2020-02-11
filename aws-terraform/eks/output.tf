
locals {
    kubeconfig = <<KUBECONFIG

apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: ${aws_eks_cluster.test-cluster.certificate_authority.0.data}
    server: ${aws_eks_cluster.test-cluster.endpoint}
  name: test-cluster
users:
- name: test-cluster
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1alpha1
      args:
      - --region
      - ap-northeast-1
      - eks
      - get-token
      - --cluster-name
      - test-cluster
      command: aws
      env: null
contexts:
- context:
    cluster: test-cluster
    user: test-cluster
  name: test-cluster
current-context: test-cluster

KUBECONFIG
}

output "api_endpoint" {
    value = "${aws_eks_cluster.test-cluster.endpoint}"
}

output "kubeconfig" {
  value = local.kubeconfig
}