import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST = "0.0.0.0"


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        "status": 200,
        "message": "All Systems are GO!"
    })


app.run(host=HOST)
