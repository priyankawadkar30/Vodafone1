def generateBucketNameList(preFixBktName):
    import string
    data=string.ascii_lowercase+string.digits
    import random
    randStringSize=3
    randString=''.join(random.choice(data) for _ in range(randStringSize))
    result=preFixBktName+randString
    return result

def createBucket(bktName):
    import boto3

    AWS_REGION="us-west-1"
    S3Service=boto3.client("s3",region_name=AWS_REGION)

    location={'LocationConstraint':AWS_REGION}

    response=S3Service.create_bucket(Bucket=bktName,CreateBucketConfiguration=location)
    print("Response: ",response)

for i in range(3):
    r=generateBucketNameList('bkt0507priyanka')
    createBucket(r)
    print("Bucket Created")