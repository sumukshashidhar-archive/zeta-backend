# module imports
import flask
import os
import shortuuid
from datetime import datetime
import requests

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
            "message": "Auth Required"
        }), 401
    print(token)
    response = jw.validate_token(token)
    if response[0] and response[1]['decodedToken']['role'] == 'device':
        # set a storage directory for the image. built using the username.
        storage_directory = f"./static/images/{response[1]['decodedToken']['username']}/"
        if os.path.isdir(storage_directory):
            pass
        else:
            os.mkdir(storage_directory)
        # uploaded
        f = flask.request.files['image']
        file_uuid = shortuuid.uuid()
        filename = storage_directory + file_uuid + ".png"
        f.save(filename)
        ilog.log(response[1]['decodedToken']['username'], file_uuid + ".png",
                 f"40.76.37.214:80/static/images/{response[1]['decodedToken']['username']}/{file_uuid}.png", str(datetime.now()))
        return (flask.jsonify({
            "message": f"Accepted the Image from user {response[1]['decodedToken']['username']}"
        })), 200
    else:
        return flask.jsonify({
            "message": "Malformed JWT."
        }), 403


@app.route('/api/getImages', methods=['GET'])
def get_image():
    try:
        with open('userlist.csv', 'r') as f:
            text = f.read()
            return text, 200
    except:
        return 500, {"message": "Something went wrong with the text parser"}


"""
App Route to Show the ML Options Page.
"""


@app.route('/functions', methods=['GET'])
def view_ml():
    return flask.render_template('ml_page.html')


@app.route('/snapper', methods=['GET'])
def snapper_view    ():
    return flask.render_template('ml_page.html')


@app.route('/api/snap_raspberry', methods=['POST'])
def snap_raspberry():
    """
    Should send an API request to the raspberry pi
    :return:
    """
    RASP_IP_ADDR = ""
    PERSONAL_TOKEN = ""
    response = requests.post(
        url = f"http://{RASP_IP_ADDR}:80/api/snap",
        data = {
            "token":PERSONAL_TOKEN
        }
    )
    if response.status_code == 200:
        # means that it succeeded in uploading the image
        print("Done.")
    else:
        print(response.status_code, response.text)


if __name__ == "__main__":
    # critical to have this conditional for gunicorn to work!
    app.run(host=HOST)
