#!/bin/bash

# set the poetry path (use: poetry env info --path)
source /home/ubuntu/.cache/pypoetry/virtualenvs/cloud-image-extractor-TSuaiKSy-py3.8/bin/activate

export FLASK_APP=cloud_image_extractor
export FLASK_ENV=development
export FLASK_DEBUG=0

flask run --host=0.0.0.0 --port=8080