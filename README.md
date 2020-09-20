# zeta-backend

# Image Upload Guidelines

Send a POST Request to /api/image/upload

Sample Code.

```python
import time
import requests

url = "http://.../api/upload/image"

image = open("test.png", 'rb').read()

token = "..."


files = {'image': open('test.png','rb')}
values = {"token":token}


response = requests.post(url, files=files, data=values)
```

# Image Deletion
## GET - /api/deleteImage
```
@params:
token - the JWT token
path - the image path to delete
```

For example
```
http://0.0.0.0/api/deleteImage?token=somejwttokenhere&path=somerandompath.png
```

This is a valid request


# Machine Learning Routes
All Routes are prefixed with `/api/ml/` to indicate their nature. 

## GET - /api/ml/face_recognition
Returns face data. Draws Images for you. 
## GET - /api/ml/classifier
## GET - /api/ml/color_recognition
## GET - /api/ml/writing_recognition
