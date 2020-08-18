from PIL import Image
import numpy as np
from Pixel import Pixel

class Image:

    def __init__(self):
        imOpen = Image.open('Hexagon.jpg')
        self.originalPic = imOpen.load()
        self.im = self.originalPic.convert("L")
        self.imSize = self.im.size
        self.marked = np.zeros(self.im.size).astype(bool)
        self.regions = None

    def findRegions(self):
        lineCoordinates = []
        for x in range(self.imSize[0]):
            for y in range(self.imSize[1]):
                if self.isContrasting(x, y):
                    lineCoordinates.append((x, y))
        return lineCoordinates

    def isContrasting(self, x, y):
        centerPixel = Pixel(self.im, x, y)
        neighbors = self.getNeighbors(x, y)
        for nbr in neighbors:
            if not centerPixel.isSimilar(nbr):
                return True

        return False

    def getNeighbors(self, x, y):
        neighbors = []
        temp = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        for point in temp:
            if self.isValidPoint(point):
                neighbors.append(point)
        return np.asarray(neighbors)

    def isValidPoint(self, point):
        return 0 <= point[0] < self.imSize[0] and 0 <= point[1] < self.imSize[1]
