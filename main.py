from flask import Flask, jsonify, request
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def saveImg():

    data = request.json
    print(data)
    data = bytes(data['data'])

    f = io.BytesIO(base64.b64decode(data))
    pilimage = Image.open(f)
    pilimage.save('pleaseGod0.png', "JPEG")
    return

if __name__ == "__main__":
    app.run()
