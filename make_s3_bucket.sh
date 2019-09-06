#!/bin/bash
echo -n "Enter of the S3 Bucket: " 
read bucket
aws s3 mb s3://$bucket
