import math

def Create_Warehouse():
    warehouse = Warehouse(50, 50, 2) # 180 cm per floor, so for 100', 17 floors
    return warehouse

# Use cm for all measurements let's say 1000 cm each for width and height
class Warehouse(object):
    def __init__(self, l, h, numFloors):
        self.length = l
        self.height = h
        self.numFloors = numFloors
        self.aislesPerFloor = int(math.floor(self.length / 6))
        self.layerHeight = 9
        self.layersPerAisles = int(math.floor((self.height/self.numFloors)/self.layerHeight))
        self.resetFloors()
        self.boxTypes = dict()
        open60x30 = []
        for i in range(self.numFloors):
            for j in range(self.aislesPerFloor):
                for k in range(self.layersPerAisles):
                    for k in range(self.length-6):
                        for l in range(self.layerHeight-3):
                            coordinates=[]
                            for x in range(6):
                                for y in range(3):
                                    coordinates.append((x,y))
                            open60x30.append((i, j, (coordinates)))
        self.boxTypes['60x30'] = open60x30
        open90x40 = []
        #for i in range(self.numFloors):
            #for j in range(self.aislesPerFloor):
                #for k in range(self.length-9):
                    #for l in range(self.shelfHieght-4):
                        #self.open90x40.append((i, j, (k, l)))
        #self.boxTypes['90x40'] = open90x40
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
                    ((self.inventory[i])[j])[k] = Shelf(self.length, self.layerHeight)
            print "finished floor", i

    def placeBox(self, box, floorIndex, shelfIndex, x, y):
        (self.inventory[floorIndex])[shelfIndex].placeBox(box, x, y)

    def showWharehouse(self):
        for floor in self.inventory:
            print 'Floor', floor
            for aisle in self.inventory[floor]:
                print 'Aisle', aisle
                for layer in (self.inventory[floor])[aisle]:
                    ((self.inventory[floor])[aisle])[layer].showShelf()

    def showFloor(self, floor):
        print 'Floor', floor
        for aisle in self.inventory[floor]:
            print 'Aisle', aisle
            for layer in (self.inventory[floor])[aisle]:
                ((self.inventory[floor])[aisle])[layer].showShelf()

    def showAisle(self, floor, aisle):
        print 'Floor', floor, ' Aisle', aisle
        for layer in (self.inventory[floor])[aisle]:
            ((self.inventory[floor])[aisle])[layer].showShelf()

    def showLayer(self, floor, aisle, layer):
        print 'Floor', floor, ' Aisle', aisle, ' Layer', layer
        ((self.inventory[floor])[aisle])[layer].showShelf()

class Shelf(object):
    def __init__(self, length, height):
        #How wide are shelves? Let's say they're 60 cm, which is just under 2'
        self.positions = dict()
        self.length = length
        self.height = height

        for i in range(length):
            for k in range(height):
                self.positions[(i, k)] = ' x '
        #self.showShelf()

    def placeBox(self, box, width, length):
            for j in range(length, length + box.length):
                for k in range(0, 0 + box.height):
                    self.positions[(k, j)] = box.id

    def showShelf(self):
        #print "showing shelf. height", self.height, "length", self.length
        for j in range(-1, self.height+1):
            length = ""
            for i in range(self.length):
                if j == -1 or j == self.height:
                    length += "---"
                    if i % 10 == 0:
                        length += "-"
                else:
                    if i % 10 == 0:
                        length += "|"
                    length += str(self.positions[(i, j)])
            if not (j == -1 or j == self.height):
                length += "|"
            print length

class Box(object):
    def __init__(self, length, width, height, contents, id):
        self.length = length
        self.width = width
        self.height = height
        self.size = str(length)+'x'+str(height)
        self.contents = contents
        self.id = id
        self.floor = None
        self.shelf = None
        self.position = None

    def setPosition(self, floor, shelf, position):
        self.floor = floor
        self.shelf = shelf
        self.position = position