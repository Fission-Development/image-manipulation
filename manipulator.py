from colorthief import ColorThief
from PIL import Image
import struct


class Manipulator():
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)

    def get_color(self):
        color_thief = ColorThief(self.filename)
        dominant_color = color_thief.get_color(quality=1)
        return dominant_color

    def change_color(self, color):
        fromColor = self.get_color()
        toColor = struct.unpack('BBB', bytes.fromhex(color))
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