from flask import Flask, jsonify, request
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def saveImg():
    with open("image.jpg", "rb") as image:
        b64string = base64.b64encode(image.read())

    data = request.json
    f = io.BytesIO(base64.b64decode(b64string))
    pilimage = Image.open(f)
    pilimage.save('pleaseGod0.png', "JPEG")
    return

if __name__ == "__main__":
    app.run()
