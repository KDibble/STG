import math

def Create_Warehouse():
    # i = 0
    # j = 0
    # warehouse = dict()
    #
    # #Create a warehouse shelving unit with specified height and length
    # while (i < height):
    #     while (j < length):
    #         warehouse[(i, j)] = 'x'
    #         j += 1
    #     i += 1
    #     j = 0
    # warehouse = Warehouse(3000, 3000, 17) # 180 cm per floor, so for 100', 17 floors
    warehouse = Warehouse(30, 30, 1) # 180 cm per floor, so for 100', 17 floors
    return warehouse

# Use cm for all measurements let's say 1000 cm each for width and height
class Warehouse(object):
    def __init__(self, l, w, numFloors):
        self.length = l
        self.width = w
        self.numFloors = numFloors
        self.shelvesPerFloor = int(math.floor(self.width / 6))
        # self.shelvesPerFloor = int(math.floor(self.width / 60))
        self.resetFloors()
        floor = 0
        shelf = 0
        layer = 0
        self.inventory[floor][shelf][layer].showShelf()

    def resetFloors(self):
        print "reset floors ( numFloors", self.numFloors, "shelvesPerFloor", self.shelvesPerFloor, ")"
        print "shelves are", self.length, "in length"
        self.inventory = []
        for i in range(self.numFloors):
        #How wide are shelves? Let's say they're 60 cm, which is just under 2'
            shelves = []
            for j in range(self.shelvesPerFloor):
                layers = []
                bottom = Shelf(self.length)
                top = Shelf(self.length)
                layers.append(bottom)
                layers.append(top)
                shelves.append(layers)
            self.inventory.append(shelves)
            print "finished floor", i
            # self.shelves.append(Shelf(self.length, self.width))

    def placeBox(self, box, floorIndex, shelfIndex, layerIndex, x, y):
        self.inventory[floorIndex][shelfIndex][layerIndex].placeBox(box, x, y)

class Shelf(object):
    def __init__(self, length):
        #How wide are shelves? Let's say they're 60 cm, which is just under 2'
        self.positions = []
        self.length = length
        self.width = 6
        self.height = 9 # 3' is 90cm
        # self.width = 60
        # self.height = 90 # 3' is 90cm
        # print "Creating shelf with dimensions", self.length, self.width, self.height

        for i in range(self.length):
            twoD = []
            for j in range(self.width):
                oneD = []
                for k in range(self.height):
                    oneD.append(' ')
                twoD.append(oneD)
            self.positions.append(twoD)
        # self.showShelf()

    def placeBox(self, box, width, length):
        for i in range(width, width + box.width):
            for j in range(length, length + box.length):
                for k in range(0, 0 + box.height):
                    self.positions[i][j][k] = box.contents
        # self.positions[width][length][0] = box.contents
        # self.positions[width + box.width - 1][length + box.length - 1][0] = box.contents


    def showShelf(self):
        print "showing shelf. width", self.width, "length", self.length
        for j in range(-1, self.width + 1):
            length = ""
            for i in range(self.length):
                if j == -1 or j == self.width:
                    length += "-"
                    if i % 10 == 0: length += "-"
                else:
                    if i % 10 == 0: length += "|"
                    length += str(self.positions[i][j][0]) # Should print out the bottom layer of the shelf
            print length + "|"

class Box(object):
    def __init__(self, length, width, height, contents):
        self.length = length
        self.width = width
        self.height = height
        self.contents = contents

    def setPosition(self, floor, shelf, distanceFromBeginning):
        self.position = dict(floor=floor, shelf=shelf, distance=distanceFromBeginning)