import Warehouse

height = 6
length = 12
shelfHeight = 2
i = 0
j = 0
oneByOne = []
twoByTwo = []
boxTypes = dict()

#Create warehouse shelf object
testWarehouse = Warehouse.Create_Warehouse(height, length)

#Print out layout
while (i < height):
    while (j < length):
        print testWarehouse[(i, j)],
        j += 1
    print '\n',
    i += 1
    j = 0

i = 0
j = 0
#create array of available 1x1 spots
while (i < height):
    if not (((i+1) % shelfHeight) == 0):
        while (j < length):
            oneByOne.append(((i, j)))
            j += 1
    i += 1
    j = 0
boxTypes['1x1'] = oneByOne


i = 0
j = 0
#create array of available 2x2 spots
while (i < height-1):
    if not (((i + 1) % shelfHeight) == 0):
        while (j < length-1):
            twoByTwo.append(((i, j), (i, j+1), (i+1, j), (i+1, j+1)))
            j += 1
    i += 1
    j = 0
boxTypes['2x2'] = twoByTwo