provider "aws" {
  region = "eu-west-2"
}

resource "aws_eks_cluster" "eks" {
  name     = "flytbase-cluster"
  role_arn = var.eks_role_arn

  vpc_config {
    subnet_ids = var.subnet_ids
  }
}

resource "aws_eks_node_group" "node_group" {
  cluster_name   = aws_eks_cluster.eks.name
  node_role_arn  = var.node_role_arn
  subnet_ids     = var.subnet_ids
  instance_types = ["t3.micro"]

  scaling_config {
    desired_size = 2
    max_size     = 5
    min_size     = 1
  }
}
