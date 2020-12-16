#!/bin/bash

aws emr describe-cluster --cluster-id j-233C8KK4777DR --query Cluster.Status.State --region ap-northeast-1
