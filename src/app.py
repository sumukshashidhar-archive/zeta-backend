import flask
from werkzeug.utils import secure_filename
import jwt_handler as jw
import os
import shortuuid


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
    # first verify the token:
    token = flask.request.data['token']
    response = jw.decode(token)
    if response[0]:
        storage_directory = f"./static/images/{response[2]['username']}"
        if os.path.isdir(storage_directory):
            pass
        else:
            os.mkdir(storage_directory)
    # uploaded
    f = flask.request.files['image']
    filename = storage_directory + shortuuid.uuid() + ".png"
    f.save(secure_filename(filename))
    return(flask.jsonify({
        "status":200,
        "message":"Accepted the Image"
    }))

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
