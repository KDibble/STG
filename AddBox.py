import math
import Warehouse

def GetValid(boxTypes, box, warehouse):

    validSpots = []
    occupied = 0

    #adds all valid spots to a list
    for spot in boxTypes[box.size]:
        floor = spot[0]
        aisle = spot[1]
        layer = spot[2]
        coordinates = spot[3]
        for coordinate in spot[3]:
            if not (((warehouse.inventory[spot[0]])[spot[1]])[spot[2]]).positions[(coordinate)] == ' x ':
                occupied += 1
        if not ((spot[3])[0])[1] == 0:
            if (((warehouse.inventory[floor])[aisle])[layer]).positions[((coordinates[0])[0], ((((coordinates)[0])[1]) - 1))] == ' x ':
                #or (((warehouse.inventory[floor])[aisle])[layer]).positions[((((coordinates)[0])[0]+int(.5*box.length)), (((spot[3])[0])[1] - 1))] == ' x ':
                occupied += 1
        if occupied == 0:
            validSpots.append(spot)
        occupied = 0

    return validSpots


def GetOptimal(validSpots, boxTypes, warehouse):
    chosenSpot = None
    minValue = 999999999
    value = 0
    removed = []

    for spot in validSpots:
        floor = spot[0]
        aisle = spot[1]
        layer = spot[2]
        coordinates = spot[3]
        for coordinate in coordinates:
            for type in boxTypes:
                if type == '60x30':
                    size = warehouse.smallBoxes
                else:
                    size = warehouse.bigBoxes
                for spot2 in boxTypes[type]:
                    floor2 = spot2[0]
                    aisle2 = spot2[1]
                    layer2 = spot2[2]
                    coordinates2 = spot2[3]
                    if coordinate in coordinates2 and not coordinates2 in removed and floor == floor2 and aisle == aisle2 and layer == layer2:
                        value += size / (warehouse.allBoxes + 1)
        if value < minValue:
            chosenSpot = spot
            minValue = value
        value = 0

    return chosenSpot


def AddBox(warehouse, box):
    tempWarehouse = warehouse
    validSpots = []

    validSpots = GetValid(warehouse.boxTypes, box, warehouse)

    #Need to determine which spot is optimal from valid
    chosenSpot = GetOptimal(validSpots, warehouse.boxTypes, warehouse)

    #Remove newly occupied spots from lists
    box.setPosition(chosenSpot[0], chosenSpot[1], chosenSpot[2], chosenSpot[3])
    warehouse.placeBox(box, chosenSpot[0], chosenSpot[1], chosenSpot[2], chosenSpot[3])
    if box.size == '60x30':
        warehouse.smallBoxes += 1
    else:
        warehouse.bigBoxes += 1
    warehouse.smallBoxes += 1
    warehouse.allBoxes += 1


    #return new warehouse