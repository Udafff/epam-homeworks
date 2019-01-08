""" pip install boto3 """
import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
bucket = s3.Bucket('epam-python')
print(bucket.name)

# Get list of files in a Bucket
# for obj in bucket.objects.all():
#     print(obj)

# Get Bucket list
# for bucket in s3.buckets.all():
#     print(f'{bucket.name} is: {bucket}')

# Download files from Bucket
# for obj in bucket.objects.all():
#     file = bucket.Object(obj.key)
#     print(file)
#     with open(obj.key, 'wb') as f_handler:
#         file.download_fileobj(f_handler)

# s3.Bucket('mybucket').download_file('hello.txt', '/tmp/hello.txt')
# bucket.download_file('.gitignore', '.gitignore')

# s3.Bucket('mybucket').upload_file('/tmp/hello.txt', 'hello.txt')
# bucket.upload_file('tag_counter_file.log', 'tag_counter_file.log')

s3_client = boto3.client('s3')
print(s3_client.list_buckets()['Buckets'][0]['Name'])
s3_client.create_bucket(Bucket='epam-uav-test01', CreateBucketConfiguration={
    'LocationConstraint': 'eu-central-1'})

for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket)

s3_client.delete_bucket(Bucket='epam-uav-test01')

print('=======')
for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket)

# #########
try:
    s3_client.create_bucket(Bucket='epam-uav-test01', CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'})
    print(s3_client.delete_bucket(Bucket='epam-uav-test01'))
except ClientError as err:
    if err.response['Error']['Code'] == 'NoSuchBucket':
        print(err.response['Error']['Code'])
        print(err.response['Error']['Message'])
        print(f"BucketName: {err.response['Error']['BucketName']}")
        print(err.response)
        print(err.operation_name)
    elif err.response['Error']['Code'] == 'IllegalLocationConstraintException':
        print(f'Incorrect region.')
        print(err.response['Error']['Message'])
    else:
        print(err.response)
