# -*- coding: utf-8 -*-

# lambda func : RequestSpotInstances

import boto3

# インスタンスタイプetc設定
instance_count = 2
image_id = "ami-xxxxxxxx"
security_groups = ["sg-xxxxxxxx"]
incetance_type = "t3.medium"
availability_zone = "ap-northeast-1a"
subnet_id = "subnet-xxxxxxxx"

client = boto3.client('ec2')


def lambda_handler(event, context):

    # Launch Instances
    run_request = client.run_instances(
        ImageId=image_id,
        MinCount=instance_count,
        MaxCount=instance_count,
        SecurityGroupIds=security_groups,
        InstanceType=incetance_type,
        Placement={"AvailabilityZone": availability_zone},
        SubnetId=subnet_id
    )

    instance_ids = []
    for instance in run_request['Instances']:
        instance_ids.append(instance['InstanceId'])
    response = {"LaunchedInstances": instance_ids}

    # 戻り値例：{ "LaunchedInstances": ["i-aaaaaaaaaaaaaaa", "i-bbbbbbbbbbbbbbbbb"]}
    return response
