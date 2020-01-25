#!/bin/bash

aws emr describe-cluster --cluster-id j-21XCVRSV0XDJP --query Cluster.Status.State --region ap-northeast-1
