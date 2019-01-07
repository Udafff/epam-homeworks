""" pip install boto3 """
import boto3

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

