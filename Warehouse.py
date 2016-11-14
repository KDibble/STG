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