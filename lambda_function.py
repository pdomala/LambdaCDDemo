import boto3

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    return response
