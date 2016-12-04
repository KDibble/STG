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


def AddBox(warehouse, box):
    tempWarehouse = warehouse
    validSpots = []

    validSpots = GetValid(warehouse.boxTypes, box, warehouse)

    #Need to determine which spot is optimal from valid
    chosenSpot = validSpots[0]

    #Remove newly occupied spots from lists
    box.setPosition(chosenSpot[0], chosenSpot[1], chosenSpot[2], chosenSpot[3])
    warehouse.placeBox(box, chosenSpot[0], chosenSpot[1], chosenSpot[2], chosenSpot[3])
