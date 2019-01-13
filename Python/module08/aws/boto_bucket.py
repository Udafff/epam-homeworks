"""
BotoBucket Class for working with AWS Buckets
v. 0.2
"""
import boto3
from botocore.exceptions import ClientError
import uuid


class BotoBucket():
    def __init__(self):
        """ Class for working with AWS Buckets. """
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')

    def create_bucket(self, arg_bucket_name=None, arg_location=None):
        # Bucket creation master.
        # In success case returns: [True, name_of_new_bucket],
        # else - print Error info and return: [False, error_info_data].
        if arg_bucket_name is None:
            arg_bucket_name = 'epam-python-' + str(uuid.uuid4())
            arg_bucket_name = input(f'Enter bucket name for new bucket please [default: {arg_bucket_name}]:') or arg_bucket_name
        if arg_location is None:
            arg_location = input('Enter location [default: eu-central-1]:') or 'eu-central-1'

        try:
            self.s3_client.create_bucket(Bucket=arg_bucket_name, CreateBucketConfiguration={
                'LocationConstraint': arg_location})
            return [True, arg_bucket_name]
        except ClientError as err:
            return [False, self.parse_exception('create_bucket', err)]

    def clean_bucket(self, arg_bucket_name):
        """ Clean all file in the bucket. """
        try:
            self.s3_resource.Bucket(arg_bucket_name).objects.all().delete()
            return [True, arg_bucket_name]
        except ClientError as err:
            return [False, self.parse_exception('clean_bucket', err)]

    def remove_bucket(self, arg_bucket_name):
        """ Remove bucket by name. """
        # In success case returns [True, name_of_deleted_bucket],
        # else - print Error info and return [False, error_info_data].
        try:
            self.s3_client.delete_bucket(Bucket=arg_bucket_name)
            return [True, arg_bucket_name]
        except ClientError as err:
            return [False, self.parse_exception('remove_bucket', err)]

    def is_exist(self, arg_bucket_name):
        """ Check by name: Is buckets exists? """
        # In success case returns: [True, name_of_bucket],
        # else - print Error info and returns: [False, name_of_bucket].
        if self.s3_resource.Bucket(arg_bucket_name) in self.s3_resource.buckets.all():
            return True
        else:
            return False

    def merge_bucket(self, arg_buckets):
        """ Copy all files from each source bucket in the list arg_buckets[0] to bucket arg_buckets[1]
        arg_buckets = [['b1', 'b2', 'b3', ...], 'dest_bucket'] """
        if self.is_exist(arg_buckets[1]) is False:
            print(f'Destination bucket {arg_buckets[1]} is not exists. Interupt merging...')
            return [False]

        for s_bucket in arg_buckets[0]:
            print(f'Copy "{s_bucket}" to "{arg_buckets[1]}"')
            if self.is_exist(s_bucket) is False:
                print(f'  Bucket "{s_bucket}" is not exists. Skipping it...')
                continue

            if not len(list(self.s3_resource.Bucket(s_bucket).objects.limit(1))):
                print(f'  Bucket "{s_bucket}" has no objects.')
                continue

            for file_obj in self.s3_resource.Bucket(s_bucket).objects.all():
                obj_source = {'Bucket': s_bucket, 'Key': file_obj.key}
                print(' ', obj_source)
                # s3.meta.client.copy(obj_source, 'otherbucket', 'otherkey')
                self.s3_resource.meta.client.copy(obj_source, arg_buckets[1], file_obj.key)

    @staticmethod
    def parse_exception(arg_action, arg_exception):
        """ Simple parsing of AWS Client Error exception. Print type of error and return information about error. """
        # print(arg_exception)
        if arg_exception.response['Error']['Code'] == 'NoSuchBucket':
            print(f'BotoBucket() Error: "NoSuchBucket". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f'BotoBucket() Error: "Bucket Already Exists". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'IllegalLocationConstraintException':
            print(f'BotoBucket() Error: "Wrong Region". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f'BotoBucket() Error: "Bucket Already Owned By You". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'InvalidBucketName':
            print(f'BotoBucket() Error: "The specified bucket name is not valid.". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'BucketNotEmpty':
            print(f'BotoBucket() Error: "The bucket you tried to delete is not empty.". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        else:
            print(f'BotoBucket() Error: "Other Exception. Please parse the response.". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            print(arg_exception.response)
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]


if __name__ == "__main__":
    """ Main Function for testing BotoBucket Class """
    cls_bb = BotoBucket()
    # cls_bb.create_bucket()
    cls_bb.create_bucket('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f', 'eu-central-1')
    print(cls_bb.is_exist('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f'))

    cls_bb.merge_bucket([['ecddf9e63475', 'unavailable_bucket', '360ea28220cc'],
                         'epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f'])

    cls_bb.clean_bucket('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f')
    cls_bb.remove_bucket('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f')
    print(cls_bb.is_exist('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f'))
