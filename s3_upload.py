import boto3

#Define AWS details 
local_file = 'netflix_users.csv'
bucket_name = 'julian-netflix-data'
s3_file_name = 'netflix_users/netflix_users.csv'

#Start the S3 Client 
session = boto3.Session(profile_name='my-personal')
s3 = session.client('s3')

#Function that loads data to s3 

def upload_to_s3(local_file,bucket_name,s3_file_name):
    try:
        s3.upload_file(local_file, bucket_name, s3_file_name)

        print(f"File '{local_file}' uploaded to S3 bucket '{bucket_name}' as '{s3_file_name}'") 

    except Exception as e:

        print(f"Error uploading file: {e}") 

upload_to_s3(local_file, bucket_name, s3_file_name) 