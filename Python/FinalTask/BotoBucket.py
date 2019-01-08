"""
Final task - Class for working with AWS Buckets
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
        # In success case returns [True, name_of_new_bucket],
        # else - print Error info and return [False, error_info_data].
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

    def remove_bucket(self, arg_bucket_name):
        """ Remove bucket by name. """
        # In success case returns [True, name_of_deleted_bucket],
        # else - print Error info and return [False, error_info_data].
        try:
            self.s3_client.delete_bucket(Bucket=arg_bucket_name)
            return [True, arg_bucket_name]
        except ClientError as err:
            return [False, self.parse_exception('create_bucket', err)]

    def is_exist(self, arg_bucket_name):
        """ Check by name: Is buckets exists? """
        # In success case returns [True, name_of_bucket],
        # else - print Error info and return [False, name_of_bucket].
        if self.s3_resource.Bucket(arg_bucket_name) in self.s3_resource.buckets.all():
            return True
        else:
            return False

    @staticmethod
    def parse_exception(arg_action, arg_exception):
        """ Simple parsing of AWS Client Error exception. Print type of error and return information about error. """
        if arg_exception.response['Error']['Code'] == 'NoSuchBucket':
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f'Error: "Bucket Already Exists". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'IllegalLocationConstraintException':
            print(f'Error: "Wrong Region". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        elif arg_exception.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f'Error: "Bucket Already Owned By You". '
                  f'Class Method: {arg_action}, aws operation: {arg_exception.operation_name}')
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        else:
            print(f'Error: "Other Exception. Please parse the response.". '
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

    cls_bb.remove_bucket('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f')
    print(cls_bb.is_exist('epam-python-2b9868e7-49f2-46ac-97a8-caaf2f90491f'))
