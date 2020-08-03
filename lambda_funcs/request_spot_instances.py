# -*- coding: utf-8 -*-

# lambda func : RequestSpotInstances

import boto3

# SpotFleet、インスタンスタイプetc設定
spot_price = "0.01"
instance_count = 2
request_type = "one-time"
duration_minutes = 60
image_id = "ami-xxxxxxxx"
security_groups = ["sg-xxxxxxxx"]
incetance_type = "t3.medium"
availability_zone = "ap-northeast-1a"
subnet_id = "subnet-xxxxxxxx"

client = boto3.client('ec2')


def lambda_handler(event, context):

    # SpotFleetリクエスト
    response = client.request_spot_instances(
        SpotPrice=spot_price,
        InstanceCount=instance_count,
        Type=request_type,
        BlockDurationMinutes=duration_minutes,
        LaunchSpecification={
            "ImageId": image_id,
            "SecurityGroupIds": security_groups,
            "InstanceType": incetance_type,
            "Placement": {
                "AvailabilityZone": availability_zone
            },
            "SubnetId": subnet_id
        }
    )

    request_ids = []
    request_body = response[response.keys()[0]]
    for request_id in request_body:
        request_ids.append(request_id['SpotInstanceRequestId'])

    request = {"requestIds": request_ids}

    # スポットリクエストID
    # 戻り値例：{["requestIds": "sir-aaaaaaa", "sir-bbbbbbb"]}
    return request
