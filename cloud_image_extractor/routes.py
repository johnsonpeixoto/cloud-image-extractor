# from cmath import log

from cloud_image_extractor import app
from flask import render_template, request
from werkzeug.utils import secure_filename

from controller import put_metadata, get_metadata
from utils.helpers import generate_id

import boto3

@app.route('/')
def index():
    return render_template('file_upload_to_s3.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                uuid = generate_id()
                filename = secure_filename(img.filename)
                new_name = "{}-{}".format(uuid, filename)

                img.save("./tmp/" + new_name)

                response = put_metadata(uuid, new_name)
                print(response)

                msg = "Upload Done !"
        else:
            msg = "File invalid X"

    return ({"msg":msg})

@app.route('/add')
def post():
    response = put_metadata("d541b188-3545-4147-9b3a-3c07faec3b69", "testeteste")
    print(response)

    return (response)

@app.route('/get', methods=['GET'])
def get():
    response = get_metadata()

    return response