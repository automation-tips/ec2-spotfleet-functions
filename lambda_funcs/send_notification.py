# -*- coding: utf-8 -*-

# lambda func : SendNotification


import boto3


def lambda_handler(event, context):
    instance_ids = event['LaunchedInstances']
    request = {
        'TopicArn': "arn:aws:sns:ap-northeast-1:xxxxxxxxxxxx:LaunchInstancesNotification",
        'Message': str(instance_ids),
        'Subject': "LaunchInstances"
    }
    response = boto3.client('sns').publish(**request)
