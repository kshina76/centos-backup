#!bin/bash

aws emr add-steps --cluster-id j-233C8KK4777DR --steps file://./wordcount_step.json --region ap-northeast-1
