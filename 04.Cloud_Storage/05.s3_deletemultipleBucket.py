def deleteBucketObjects(bktName):
    import boto3

    AWS_REGION="us-west-1"
    S3Service=boto3.resource("s3",region_name=AWS_REGION)

    selectedBucket=S3Service.Bucket(bktName)
    selectedBucket.objects.delete()
    print("Deleted Bucket All Objects")

    selectedBucket.delete()
    print("Deleted Bucket: ",bktName)

buckets=["bkt0358priyanka", "bkt0507priyankajcm", "bkt0507priyankaryp"]
for bn in buckets:
    deleteBucketObjects(bn)