import requests
import base64

with open("input.png", "rb") as image:
    image = base64.b64encode(image.read())

r = requests.post("http://localhost:5000/changecolor", json={"image": image.decode("utf-8"), "color": "4287f5"})

with open("output.png", "wb") as fh:
    fh.write(base64.decodebytes(bytes(r.text, "utf-8")))