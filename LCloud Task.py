import os
import boto3
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
BUCKET_NAME = 'developer-task'
PREFIX = 'TIE-sa/'

