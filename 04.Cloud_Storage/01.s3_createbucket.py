import boto3

AWS_REGION="us-west-1"
s3Service=boto3.resource("s3",region_name=AWS_REGION)

CrBktCnf={'LocationConstraint':AWS_REGION}
response=s3Service.create_bucket(Bucket='bkt0358priyanka',CreateBucketConfiguration=CrBktCnf)
print("Response = ",response)
print("Bucket created.Please check : aws s3 ls")

