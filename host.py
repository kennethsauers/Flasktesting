from PIL import Image
import base64
import requests
import array as arr

API_ENDPOINT = 'http://10.192.211.225:8080/screening'

with open("image.jpg", "rb") as image:
    b64string = base64.b64encode(image.read())
    print(type(b64string))
    data = {"imgdata" : b64string.decode()}
    print(type(data))
    r = requests.post(url = API_ENDPOINT, json = data)
    print(r.text)
