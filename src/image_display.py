from app import app

@app.route('/test', methods=['GET'])
def test():
    return flask.jsonify({
        "status": 200,
        "message": "All Systems are GO!"
    })