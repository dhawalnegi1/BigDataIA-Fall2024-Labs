import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def download_file_from_s3(bucket_name, s3_file_key, local_file_name):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_file_key, local_file_name)
        print(f"Download Successful: s3://{bucket_name}/{s3_file_key} to {local_file_name}")
    except FileNotFoundError:
        print("The specified key does not exist.")
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Client error: {e}")

local_file = ""
bucket = ""
s3_file = ""

download_file_from_s3(bucket, s3_file, local_file)