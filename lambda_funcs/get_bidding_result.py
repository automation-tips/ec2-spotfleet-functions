# -*- coding: utf-8 -*-

# lambda func : GetBiddingResult

import boto3

ec2 = boto3.client('ec2')


def lambda_handler(event, context):

    # 例：["requestIds": "sir-aaaaaaa", "sir-bbbbbbb"]
    request_ids = event['requestIds']

    spot_response = ec2.describe_spot_instance_requests(
        SpotInstanceRequestIds=request_ids
    )

    instance_ids = []
    spot_request = spot_response[spot_response.keys()[0]]

    for resp in spot_request:
        if 'InstanceId' in resp:
            instance_ids.append(resp['InstanceId'])

    if len(instance_ids) != 0:
        # 落札できた場合
        response = {"LaunchedInstances": instance_ids}
        # 戻り値例：{ "LaunchedInstances": ["i-aaaaaaaaaaaaaaa", "i-bbbbbbbbbbbbbbbbb"]}
        return response
    else:
        # 落札できなかった場合
        response = {"LaunchedInstances": "0"}
        return response
