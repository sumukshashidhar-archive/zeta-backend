# module imports
import flask
import os
import shortuuid
from datetime import date

# file imports
import image_upload_logger as ilog
import jwt_handler as jw

# initialization
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# global constants
HOST = "0.0.0.0"

# routes
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
            "message":"Auth Required"
        }), 401
    try:
        response = jw.decode(token)
    except:
        return flask.jsonify({
            "message":"JWT Deserialization Failed"
        }), 500
    if response[0]:
        # set a storage directory for the image. built using the username.
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
            "message":f"Accepted the Image from user {response[1]['username']}"
        })), 200
    else:
        return flask.jsonify({
            "message":"Malformed JWT."
        }), 403


@app.route('/api/getImages', methods=['GET'])
def get_image():
    try:
        with open('userlist.csv', 'r') as f:
            text = f.read()
            return text, 200
    except:
        return 500, {"message":"Something went wrong with the text parser"}


if __name__ == "__main__":
    # critical to have this conditional for gunicorn to work!
    app.run(host=HOST)
