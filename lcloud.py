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








