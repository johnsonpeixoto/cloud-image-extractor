from cloud_image_extractor import app
from flask import render_template 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def hello():
    return '<h2>Hello World</h2>'


@app.route('/add', methods=['POST'])
def post():
    return 'Post Method'