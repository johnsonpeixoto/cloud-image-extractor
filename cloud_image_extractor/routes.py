from cmath import log
import logging

from botocore.exceptions import ClientError
from cloud_image_extractor import app
from flask import render_template, request
from werkzeug.utils import secure_filename

import boto3

S3_BUCKET = 'imagesstore'

@app.route('/')
def index():
    return render_template('file_upload_to_s3.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                print(filename)
                img.save(filename)
                
                # Upload the file
                s3_client = boto3.client('s3')
                try:
                    response = s3_client.upload_file(filename, S3_BUCKET, filename)
                    msg = "Upload Done !"

                except ClientError as e:
                    logging.error(e)
                    msg = "Upload Fail X"        

    return render_template("file_upload_to_s3.html",msg =msg)

@app.route('/add', methods=['POST'])
def post():
    return 'Post Method'
    