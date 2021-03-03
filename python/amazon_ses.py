#!/usr/bin/python3

# https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html

import boto3
from botocore.exceptions import ClientError
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--date', type=str, required=True, help='The date this is running for')
parser.add_argument('--symbol', type=str, required=True, help='The symbol this is running for')
args = parser.parse_args()

def mail(date, symbol):
    SENDER = ""
    RECIPIENT = ""
    AWS_REGION = ""
    SUBJECT = f'{symbol} Summary {date}'
    CHARSET = "UTF-8"

    # reading in the contents that will be used in the email body
    os.chdir(os.path.expanduser('~/data/fred_data'))
    with open(f'{symbol}_table.txt', 'r') as file:
        body_contents = file.read()

    BODY_TEXT = (body_contents)

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )

    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

mail(args.date, args.symbol)
