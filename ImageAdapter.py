from PIL import Image
import numpy as np
class ImageAdapter:

    def __init__(self):
        imOpen = Image.open('Hexagon.jpg')
        self.im = imOpen.load()
        marked = np.zeros(self.im.size).astype(bool)

    def findLines(self):
        for x in range(self.im.size[0]):
            for y in range(self.im.size[1]):
                curPixel = self.im[x,y]
