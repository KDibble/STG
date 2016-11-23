def AddBox(boxTypes, warehouse, box):
    tempWarehouse = warehouse
    validSpots = []

    validSpots = GetValid(boxTypes, box, warehouse)

    #Need to determine which spot is optimal from valid
    chosenSpot = GetOptimal(validSpots)

    #Remove newly occupied spots from lists

    #return new warehouse


def GetValid(boxTypes, box, warehouse):

    validSpots = []
    occupied = 0

    #adds all valid spots to a list
    for spot in boxTypes[box.size]:
        for floor, shelf, coordinate in spot:
            if not ((warehouse[floor])[shelf])[coordinate] == ' x ':
                occupied += 1
        if occupied == 0:
            validSpots.append(spot)

    return validSpots


def GetOptimal():
    return 0
