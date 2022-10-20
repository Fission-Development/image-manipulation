from manipulator import Manipulator
from flask import Flask, request, send_file
from io import BytesIO
from PIL import Image
import random
import string
import base64
import os

app = Flask(__name__)

@app.route("/changecolor", methods=["POST"])
def change_color():
    image = request.json["image"]
    color = request.json["color"]

    filename = "images/" + random_string(10) + ".png"
    with open(filename, "wb") as f:
        f.write(base64.decodebytes(bytes(image, "utf-8")))

    manipulator = Manipulator(filename)
    manipulator.change_color(color)

    with open(filename, "rb") as f:
        output = base64.b64encode(f.read())
    
    os.remove(filename)

    return output

def random_string(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))

# man = Manipulator(image)

# man.change_color((255, 114, 32))