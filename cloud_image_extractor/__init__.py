#!python3

from flask import Flask, render_template

app = Flask(__name__, template_folder='template')
from cloud_image_extractor import routes

app.run(port=5000)