provider "aws" {
  region = var.aws_region
}

resource "aws_sagemaker_model" "medifed_model" {
  name               = "medifed-anomaly-detector"
  execution_role_arn = aws_iam_role.sagemaker_role.arn

  primary_container {
    image = "123456789012.dkr.ecr.${var.aws_region}.amazonaws.com/medifed-sagemaker:latest"
  }
}

resource "aws_iam_role" "sagemaker_role" {
  name = "medifed_sagemaker_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "sagemaker.amazonaws.com"
        }
      }
    ]
  })
}
