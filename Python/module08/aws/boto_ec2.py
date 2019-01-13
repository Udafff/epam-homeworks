"""
BotoEc2 Class for working with AWS EC2 instances.
v. 0.1
"""
import boto3
from botocore.exceptions import ClientError


class BotoEc2():
    def __init__(self):
        """ Class for working with AWS EC2 instances. """
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')
    pass

if __name__ == "__main__":
    print('Hello Gold')