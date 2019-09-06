import boto3
import re

regex_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Define a function for
# for validating an Email
def validate_email(email):
    return re.match(regex_email,email)
if __name__ == '__main__' :
    input = input("Please enter email address to verify: ")
    if validate_email(input):
        client = boto3.client('ses')
        response = client.verify_email_address(
            EmailAddress=input,
        )
        print(response)
    else:
        print("Please enter a valid email address")
