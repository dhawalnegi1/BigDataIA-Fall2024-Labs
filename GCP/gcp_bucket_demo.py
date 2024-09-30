from google.cloud import storage
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/filepath_to/credentials_file.json"
file_path = "object_file_path.txt"
bucket_name = "bigdatasysia_demo_bucket-1"
destination_blob_name = 'object_file_path.txt'

def authenticate_with_gcs():
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    if credentials_path:
        print(f"Using credentials from: {credentials_path}")
        storage_client = storage.Client()
        list_blobs(bucket_name,storage_client)
        upload_file(bucket_name,file_path,destination_blob_name,storage_client)


    else:
        print("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")
        return
    


def list_blobs(bucket_name,storage_client):
    """Lists all the files (blobs) in the specified bucket."""
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)

def upload_file(bucket_name,source_file_name,destination_blob_name,storage_client):

    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")
    
    except Exception as e:
        print(f"Failed to upload file: {e}")


authenticate_with_gcs()
