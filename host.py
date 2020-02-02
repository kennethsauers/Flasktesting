from PIL import Image
import base64
import io
import requests

API_ENDPOINT = 'http://127.0.0.1:5000/'
with open("image.jpg", "rb") as image:
    b64string = base64.b64encode(image.read())
    print(type(b64string))
    data = {"data" : list(b64string)}
    r = requests.post(url = API_ENDPOINT, json = data)
    print(r)
