import boto3
from botocore.exceptions import ClientError
from config import AWS_S3_BUCKET, AWS_REGION

s3 = boto3.client('s3', region_name=AWS_REGION)

def upload_to_s3(local_path: str, s3_key: str):
    try:
        s3.upload_file(local_path, AWS_S3_BUCKET, s3_key)
        return True
    except ClientError as e:
        print(f"S3 upload failed: {e}")
        return False

def download_from_s3(s3_key: str, local_path: str):
    try:
        s3.download_file(AWS_S3_BUCKET, s3_key, local_path)
        return True
    except ClientError as e:
        print(f"S3 download failed: {e}")
        return False