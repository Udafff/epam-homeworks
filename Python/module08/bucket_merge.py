import boto3
from botocore.exceptions import ClientError
import uuid


class BotoBucket():
    def __init__(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')

    def merge_buckets(self, arg_params):
        print(f'Merge buckets: {arg_params[0]} to bucket: {arg_params[1]}')
        # print(self.s3_resource.get_available_subresources())
        # print(f'cl_ls_bucket: {self.s3_client.list_buckets()}')
        if not self.s3_resource.Bucket(arg_params[1]) in self.s3_resource.buckets.all():
            print(f'"{arg_params[1]}" is not exists! Create...')

    def create_bucket(self, arg_bucket_name=None, arg_location=None):
        if arg_bucket_name is None:
            arg_bucket_name = 'epam-python-' + str(uuid.uuid4())
            arg_bucket_name = input(f'Enter bucket name please [default: {arg_bucket_name}]:') or arg_bucket_name
        if arg_location is None:
            arg_location = input('Enter location [default: eu-central-1]:') or 'eu-central-1'

        try:
            self.s3_client.create_bucket(Bucket=arg_bucket_name, CreateBucketConfiguration={
                'LocationConstraint': arg_location})
            print('#####')
            print('Bucket is created: ', [arg_bucket_name, arg_location])
            return True
        except ClientError as err:
            self.parse_exception('create_bucket', err)
            return False

    def remove_bucket(self, arg_bucket_name):
        try:
            self.s3_client.delete_bucket(Bucket=arg_bucket_name)
            print('#####')
            print('Bucket is deleted: ', [arg_bucket_name])
            return True
        except ClientError as err:
            self.parse_exception('remove_bucket', err)
            return False

    def is_exist(self, arg_bucket_name):
        if self.s3_resource.Bucket(arg_bucket_name) in self.s3_resource.buckets.all():
            return True
        else:
            return False

    @staticmethod
    def parse_exception(arg_action, arg_exception):
        if arg_exception.response['Error']['Code'] == 'NoSuchBucket':
            print(f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            print(arg_exception.response['Error']['Code'])
            print(arg_exception.response['Error']['Message'])
            print(f"BucketName: {arg_exception.response['Error']['BucketName']}")

        elif arg_exception.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            print(arg_exception.response['Error']['Message'])

        elif arg_exception.response['Error']['Code'] == 'IllegalLocationConstraintException':
            print(f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            print(f'Incorrect region.')
            print(arg_exception.response['Error']['Message'])

        else:
            print(f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            print(arg_exception.response)


if __name__ == "__main__":
    cls_bb = BotoBucket()
    # cls_bb.merge_buckets([['1', '2', '3'], 'dest_bucket'])
    # cls_bb.create_bucket()
    cls_bb.create_bucket('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f', 'eu-central-1')
    print(cls_bb.is_exist('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f'))

    cls_bb.remove_bucket('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f')
    print(cls_bb.is_exist('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f'))
