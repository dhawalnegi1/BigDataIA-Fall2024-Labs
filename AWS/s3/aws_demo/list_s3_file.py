import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def list_files_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Files in bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"No files found in bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Client error: {e}")
    except NoCredentialsError:
        print("Credentials not available")

bucket = ""

list_files_in_bucket(bucket)
