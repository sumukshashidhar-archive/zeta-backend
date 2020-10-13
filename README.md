# zeta-backend

This is the official cloud backend software for Zeta. The other components of Zeta can be found
[Raspberry Pi Software for Image Delivery](https://github.com/1sigmoid/zeta-pi)
[Authentication Server](https://github.com/1sigmoid/jwt-auth-server)
[ML Functions](https://github.com/1sigmoid/zeta-ml-functions)



Zeta is authenticated through tokens

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
Returns face data. Draws hitboxes for you. 
## GET - /api/ml/classifier
Returns classification data. For eg: people, cats, dogs, fruits, vehicles. 
## GET - /api/ml/color_recognition
Returns dominant color data
## GET - /api/ml/writing_recognition
Returns OCR data
