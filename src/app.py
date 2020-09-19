import flask
from werkzeug.utils import secure_filename

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
    # uploaded
    f = flask.request.files['upload_file']
    filename = f"./static/images/{username}"
    f.save(secure_filename("./static/images/"+f.filename))
    return(flask.jsonify({
        "status":200
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
