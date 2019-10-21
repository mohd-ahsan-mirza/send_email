#!/bin/bash
read -p "Enter subject: " subject
encoded_subject="${subject//" "/%20}"
#echo $encoded_subject

read -p "Enter message: " message
encoded_message="${message//" "/%20}"
#echo $encoded_message

read -p "Enter Sender email(Verified): " sender_email

read -p "Enter Reciever email(Verified): " to_email

read -p "Enter Stack Name: " stack_name

api_url="$(aws cloudformation describe-stacks --stack-name $stack_name --query "Stacks[0].Outputs[?OutputKey=='SendEmailApi'].OutputValue" --output text)"
#echo $api_url

curl --request POST "$api_url/?fromEmail=$sender_email&toEmail=$to_email&subject=$encoded_subject&message=$encoded_message"

echo

