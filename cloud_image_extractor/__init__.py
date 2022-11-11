#!python3

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from . import helpers
from . import controller

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('file_upload_to_s3.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                uuid = helpers.generate_id()
                filename = secure_filename(img.filename)
                new_name = "{}-{}".format(uuid, filename)

                img.save("./tmp/" + new_name)

                response = controller.put_metadata(uuid, new_name)
                print(response)

                msg = "Upload Done !"
        else:
            msg = "File invalid X"

    return ({"msg":msg})

@app.route('/get', methods=['GET'])
def get():
    response = controller.get_metadata()

    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
