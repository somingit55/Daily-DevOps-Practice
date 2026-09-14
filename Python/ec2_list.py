import boto3   #importing boto3 library in python 

from pprint import pprint

ec2 = boto3.client("ec2", region_name="ap-south-1")   

instance_id = "i-06a3d6d5c52344a43"

response = ec2.stop_instances(InstanceIds=[instance_id])

pprint(response)