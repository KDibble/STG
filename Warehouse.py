import math

def Create_Warehouse(length, width, height, numFloors):
    warehouse = Warehouse(length, width, height, numFloors)
    # warehouse = Warehouse(50, 50, 2) # 180 cm per floor, so for 100', 17 floors
    return warehouse

# Use cm for all measurements let's say 1000 cm each for width and height
class Warehouse(object):
    def __init__(self, l, w, h, numFloors):
        self.length = l
        self.height = h
        self.numFloors = numFloors
        self.aislesPerFloor = int(math.floor(w / 6)) #60 cm width per aisle
        self.layerHeight = 9 # 90 cm height per layer
        self.layersPerAisles = int(math.floor((self.height/self.numFloors)/self.layerHeight))
        self.resetFloors()
        self.boxTypes = dict()
        self.manifest = dict() # What boxes are currently in the warehouse
        self.smallBoxes = 0
        self.bigBoxes = 0
        self.allBoxes = 0
        open60x30 = []
        for i in range(self.numFloors):
            for j in range(self.aislesPerFloor):
                for k in range(self.layersPerAisles):
                    for l in range(self.length-5):
                        for m in range(self.layerHeight-2):
                            coordinates=[]
                            for x in range(l, l+6):
                                for y in range(m, m+3):
                                    coordinates.append((x,y))
                            open60x30.append((i, j, k, (coordinates)))
        self.boxTypes['60x30'] = open60x30
        open90x40 = []
        for i in range(self.numFloors):
            for j in range(self.aislesPerFloor):
                for k in range(self.layersPerAisles):
                    for l in range(self.length-8):
                        for m in range(self.layerHeight-3):
                            coordinates=[]
                            for x in range(l, l+9):
                                for y in range(m, m+4):
                                    coordinates.append((x,y))
                            open90x40.append((i, j, k, (coordinates)))
        self.boxTypes['90x40'] = open90x40
        #((self.inventory[floor])[shelf]).showShelf()

    def resetFloors(self):
        print "reset floors ( numFloors", self.numFloors, "shelvesPerFloor", self.aislesPerFloor, ")"
        print "shelves are", self.length, "in length"
        self.inventory = dict()
        for i in range(self.numFloors):
        #How wide are shelves? Let's say they're 60 cm, which is just under 2'
            self.inventory[i] = dict()
            for j in range(self.aislesPerFloor):
                (self.inventory[i])[j] = dict()
                for k in range(self.layersPerAisles):
                    ((self.inventory[i])[j])[k] = Layer(self.length, self.layerHeight)
            print "finished floor", i

    def placeBox(self, box, floorIndex, aisleIndex, layerIndex, coordinates):
        print "placing into manifest:", box.id
        self.manifest[box.id] = box
        for coordinate in coordinates:
            ((self.inventory[floorIndex])[aisleIndex])[layerIndex].placeBox(box, coordinate[0], coordinate[1])

    def showWarehouse(self):
        for floor in self.inventory:
            print 'Floor', floor
            for aisle in self.inventory[floor]:
                print 'Aisle', aisle
                for layer in (self.inventory[floor])[aisle]:
                    ((self.inventory[floor])[aisle])[layer].showLayer()

    def showFloor(self, floor):
        print 'Floor', floor
        for aisle in self.inventory[floor]:
            print 'Aisle', aisle
            for layer in (self.inventory[floor])[aisle]:
                ((self.inventory[floor])[aisle])[layer].showLayer()

    def showAisle(self, floor, aisle):
        print 'Floor', floor, ' Aisle', aisle
        for layer in (self.inventory[floor])[aisle]:
            ((self.inventory[floor])[aisle])[self.layersPerAisles - layer].showLayer()

    def showLayer(self, floor, aisle, layer):
        print 'Floor', floor, ' Aisle', aisle, ' Layer', layer
        ((self.inventory[floor])[aisle])[layer].showLayer()

class Layer(object):
    def __init__(self, length, height):
        #How wide are shelves? Let's say they're 60 cm, which is just under 2'
        self.positions = dict()
        self.length = length
        self.height = height

        for i in range(length):
            for k in range(height):
                self.positions[(i, k)] = ' x '
        #self.showShelf()

    def placeBox(self, box, length, height):
            self.positions[(length, height)] = box.id

    def showLayer(self):
        print "showing shelf. height", self.height, "length", self.length

        #go through the top to bottom
            #go through the left to right
        for j in range(self.height, -2, -1):
            row = ""
            for i in range(self.length):
                if j < 0 or j == self.height: #The top or bottom
                    row += "==="
                    if i % 10 == 0:
                        row += "="
                else:
                    if i % 10 == 0:
                        row += "|"
                    row += str(self.positions[(i, j)])
            if (j < 0 or j == self.height): # print a row's ending visual shelf
                row += "="
            else: # print an ending "support beam" in the middle rows
                row += "|"
            print row

class Box(object):
    def __init__(self, length, width, height, contents, id):
        self.length = length
        self.width = width
        self.height = height
        self.size = str(length)+'x'+str(height)
        self.contents = contents
        self.id = id

    def setPosition(self, floor, aisle, layer, coordinates):
        self.floor = floor
        self.aisle = aisle
        self.layer = layer
        self.coordinates = coordinates