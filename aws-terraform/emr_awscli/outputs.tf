
output "subnet_id" {
  value = aws_subnet.public_0.id
}

output "S3_bucket_id" {
  value = "s3://${aws_s3_bucket.emr-log.id}/elasticmapreduce/"
}
