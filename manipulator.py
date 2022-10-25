from PIL import Image
import struct


class Manipulator():
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)

    def change_color(self, fromColor, toColor):
        fromColor = struct.unpack('BBB', bytes.fromhex(fromColor))
        toColor = struct.unpack('BBB', bytes.fromhex(toColor))
        deltaRank = 10

        img = self.image
        img = img.convert("RGBA")
        pixdata = img.load()

        for x in range(0, img.size[0]):
            for y in range(0, img.size[1]):
                rdelta = pixdata[x, y][0] - fromColor[0]
                gdelta = pixdata[x, y][0] - fromColor[0]
                bdelta = pixdata[x, y][0] - fromColor[0]
                if abs(rdelta) <= deltaRank and abs(gdelta) <= deltaRank and abs(bdelta) <= deltaRank:
                    pixdata[x, y] = (toColor[0] + rdelta, toColor[1] + gdelta, toColor[2] + bdelta, pixdata[x, y][3])

        img.save(self.filename)