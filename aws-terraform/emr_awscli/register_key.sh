#!bin/bash

aws ec2 import-key-pair --key-name id_rsa.pub --public-key-material file://~/.ssh/id_rsa.pub
