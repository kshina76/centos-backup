#!/bin/bash

aws emr create-cluster --auto-scaling-role EMR_AutoScaling_DefaultRole --applications Name=Hadoop \
  --ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-0365b245d5f84fca6"}' \
  --service-role EMR_DefaultRole --enable-debugging --release-label emr-5.5.0 \
  --log-uri 's3://emr-logs-kshina76/elasticmapreduce/' --name 'WordCount' \
  --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m1.medium","Name":"Master Instance Group"},{"InstanceCount":2,"InstanceGroupType":"CORE","InstanceType":"m1.medium","Name":"Core Instance Group"}]' \
  --scale-down-behavior TERMINATE_AT_INSTANCE_HOUR --region ap-northeast-1
