from PIL import Image
import numpy as np

from Pixel import Pixel


class Image:

    def __init__(self):
        imOpen = Image.open('Hexagon.jpg')
        self.im = imOpen.load()
        self.imSize = self.im.size
        self.marked = np.zeros(self.im.size).astype(bool)
        self.regions = None

    def findRegions(self):
        regions = []
        for x in range(self.imSize[0]):
            for y in range(self.imSize[1]):
                if not self.marked[x, y]:
                    self.marked[x, y] = True
                    region = self.findRegion(x, y)
                    regions = regions + region
        return regions

    def findRegion(self, x, y):
        curRegion = []
        curRegion.append((x, y))
        firstPixel = Pixel(self.im, (x, y))
        neighbors = self.getNeighbors(x, y)
        for neighbor in neighbors:
            visited = self.marked[neighbor[0], neighbor[1]]
            if not visited:
                self.marked[neighbor[0], neighbor[1]] = True
                similar = firstPixel.isSimilar(self.im, neighbor)
                if similar:
                    nextRegion = self.findRegion(neighbor)
                    curRegion = curRegion + nextRegion
        return curRegion

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
