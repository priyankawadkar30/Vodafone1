import boto3
s3Service=boto3.resource("s3")

for b in s3Service.buckets.all():
    print(b.name)