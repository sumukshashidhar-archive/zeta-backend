import flask
from werkzeug.utils import secure_filename
import jwt_handler as jw
import os
import shortuuid
from datetime import date

import image_upload_logger as ilog


app = flask.Flask(__name__)
app.config["DEBUG"] = True



HOST = "0.0.0.0"


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        "status": 200,
        "message": "All Systems are GO!"
    })


@app.route('/api/upload/image', methods=['POST'])
def accept_incoming_image():
    try:
        token = flask.request.form['token']
    except:
        return flask.jsonify({
            "status":401,
            "message":"Auth Required"
        })
    try:
        response = jw.decode(token)
    except:
        return flask.jsonify({
            "status":500,
            "message":"JWT Deserialization Failed"
        })
    if response[0]:
        storage_directory = f"./static/images/{response[1]['username']}/"
        if os.path.isdir(storage_directory):
            pass
        else:
            os.mkdir(storage_directory)
    # uploaded
        f = flask.request.files['image']
        file_uuid = shortuuid.uuid()
        filename = storage_directory + file_uuid + ".png"
        f.save(filename)
        ilog.log(response[1]['username'], file_uuid+".png", f"40.76.37.214:80/static/images/{response[1]['username']}/{file_uuid}.png", str(date.now()))
        return(flask.jsonify({
            "status":200,
            "message":f"Accepted the Image from user {response[1]['username']}"
        }))
    else:
        return flask.jsonify({
            "status":403,
            "message":"Malformed JWT."
        })


@app.route('/api/getImages', methods=['GET'])
def get_image():
    with open('userlist.csv', 'r') as f:
        text = f.read()
        return text

@app.route('/post', methods=['POST'])
def post_test():
    print("hello world")

@app.route('/api/image', methods=['GET'])
def serve_image():
    return flask.jsonify(
        {

        }
    )

if __name__ == "__main__":
    # critical to have this conditional for gunicorn to work!
    app.run(host=HOST)
