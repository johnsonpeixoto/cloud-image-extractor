
import boto3
from cloud_image_extractor import config

import logging
from botocore.exceptions import ClientError

import exiftool
from exiftool import ExifToolHelper

import json
from utils.helpers import generate_id

# loading the local profile from AWS CLI
session = boto3.Session(profile_name='default')
dynamodb = session.resource('dynamodb')

s3 = boto3.client('s3')

def send_image(file):    
    try:
        response = s3.upload_file("./tmp/" + file, 'imagesstore', file)
        return True

    except ClientError as e:
        logging.error(e)
        return False

def extract_metadata(file_name):
    data = ""
    with ExifToolHelper() as et:
        for d in et.get_metadata("./tmp/" + file_name):
            data = json.dumps(d, indent = 4)

    return(data)


def put_metadata(uuid, file_name):
    if send_image(file_name):
        metadata = extract_metadata(file_name)

        table = dynamodb.Table("images-metadata")

        response = table.put_item(
            Item = {
                'uuid' : uuid,
                'filename' : file_name,
                'metadata' : metadata
            }
        )

        return response

def get_metadata():
    table = dynamodb.Table("images-metadata")

    response = table.scan()

    items = response['Items']

    for v in items:
        v['metadata'] = json.loads(v['metadata'])

    return items