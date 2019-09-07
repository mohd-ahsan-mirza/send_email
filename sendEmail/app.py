import json
import boto3

# import requests

def send_email(subject,message,source_email,destination_email):
    response = SES.send_email(
        Destination={
            'BccAddresses': [
            ],
            'CcAddresses': [
                source_email,
            ],
            'ToAddresses': [
                destination_email,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': '<html><head></head><body>'+message+'</body></html>',
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': subject,
            },
        },
        Source=source_email
    )

def lambda_handler(event, context):
    """
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    response = 'ok'
    try:
        query = event['queryStringParameters']
        send_email(query['subject'],query['message'],query['toEmail'],query['fromEmail'])
    except as e:
        response = e
    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
