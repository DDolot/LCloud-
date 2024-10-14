import os
import boto3
import re
from dotenv import load_dotenv
import argparse

load_dotenv('AWS.env')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = "developer-task"
PREFIX = "TIE-sa/"


session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


sessionResource = session.resource('s3')

my_bucket = sessionResource.Bucket(BUCKET_NAME)




def list_files(prefix):
    for objects in my_bucket.objects.filter(Prefix=PREFIX):
        print(objects.key)



def upload_file(bucket_name, s3_file, file_path):
    if not s3_file.startswith(PREFIX):
        print(f'Error: The file key "{s3_file}" must start with the prefix "{PREFIX}".')
        return

    try:
        s3_object = sessionResource.Object(bucket_name, s3_file)

        with open(file_path, 'rb') as file_data:
            result = s3_object.put(Body=file_data)
        

        res = result.get('ResponseMetadata')
        if res.get('HTTPStatusCode') == 200:
            print("File uploaded succesfully")
        else:
            print("File was not uploaded succesfully")
    except Exception as e:
        print(f'Error uploading file: {e}')


def list_files_with_filter(bucket_name, prefix, regex):
    response = my_bucket.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)

    if 'Contents' in response:
        for obj in response['Contents']:
            if re.match(regex, obj['Key']):
                print(obj['Key'])
    else:
        print("No files found.")

def delete_files_with_filter(bucket_name, prefix, regex):
    response = my_bucket.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)

    if 'Contents' in response:
        for obj in response['Contents']:
            if re.match(regex, obj['Key']):
                sessionResource.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted: {obj['Key']}")
    else:
        print("No files found.")


def main():
   
    list_files(PREFIX)

    local_file = r'C:\Users\Admin\Desktop\LCloud\textfile'  
    s3_file = PREFIX + 'textfile.txt'  
    upload_file(BUCKET_NAME,local_file, s3_file)

   
    list_files_with_filter(BUCKET_NAME,PREFIX,r'.*\.py$') 

   
    delete_files_with_filter(BUCKET_NAME,PREFIX,r'.*\.txt$')  

if __name__ == "__main__":
    main()


