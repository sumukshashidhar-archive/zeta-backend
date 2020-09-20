"""
This module validates token
"""

import requests

AUTHENTICATION_URL="http://40.76.37.214:3000/api/authenticate"

def validate_token(token):

    # okay, to validate this token, we send a post request to /api/authenticate

    response = requests.post(
        url = AUTHENTICATION_URL,
        data = {
            "token":token
        } 
    )
    # after the request, we check the response code.
    if response.status_code == 200:
        return True, eval(response.text)

    else:
        print(response.status_code)
        return (False, )