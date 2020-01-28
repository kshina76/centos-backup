
output "subnet_id" {
  value = aws_subnet.public_0.id
}

output "S3_bucket_log_id" {
  value = "s3://${aws_s3_bucket.emr-log.id}/elasticmapreduce/"
}

output "S3_bucket_output_id" {
  value = "s3://${aws_s3_bucket.emr-output.id}/output/"
}
