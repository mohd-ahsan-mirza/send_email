#!/bin/bash
aws cloudformation describe-stacks | grep StackName
echo -n "Get your stack name from the list above: "
read stack_name
aws cloudformation describe-stacks \
    --stack-name $stack_name \
    --query 'Stacks[].Outputs[?OutputKey==`SendEmailApi`]' \
    --output table
