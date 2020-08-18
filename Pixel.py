from PIL import Image
import numpy as np

class Pixel:

    def __init__(self, image, x, y):
        self.img = image
        self.pixel = image[x,y]

    # TODO: implement function
    def isSimilar(self, toCompare):
        return None