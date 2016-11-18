import math

def Create_Warehouse(height, length):
    i = 0
    j = 0
    warehouse = dict()

    #Create a warehouse shelving unit with specified height and length
    while (i < height):
        while (j < length):
            warehouse[(i, j)] = 'x'
            j += 1
        i += 1
        j = 0

    return warehouse

# Using Feet as only measurment
class Warehouse(object):
    shelves = []
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.resetShelves()

    def resetShelves(self):
        numFloors = math.floor(self.height / 6) # 6' per floor
        numShelves = numFloors * 2 # 2 shelves per floor

class Shelf(object):
    def __init__(self, length, width):
        #How wide are shelves? Let's say they're 60 cm, which is just under 2'
        self.length = length
        self.width = width

    

class Box(object):
    def __init__(self, length, width, height, contents):
        self.height = length
        self.width = width
        self.depth = height
        self.contents = contents

    def setPosition(self, floor, shelf, distanceFromBeginning):
        self.position = dict(floor=floor, shelf=shelf, distance=distanceFromBeginning)