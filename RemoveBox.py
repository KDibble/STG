def removeBox(id, warehouse):
    print '\tremoveBox(): removing box of id', id
    box = warehouse.manifest[id]
    warehouse.manifest[id] = None # remove the box
    layer = ((warehouse.inventory[box.floor])[box.aisle])[box.layer]
    footprint = set()
    for (x, y) in box.coordinates:
        # print coord
        layer.positions[(x, y)] = ' x '
        footprint.add(x)
    # print footprint
    footprint = list(footprint)
    # print footprint
    boxesAbove = []
    for x in footprint:
        for y in range(layer.height):
            element = layer.positions[(x, y)]
            if element != ' x ' and element not in boxesAbove:
                # print 'found box', element, 'above'
                boxesAbove.append(element)

    #call gravity on boxesAbove
    for boxId in boxesAbove:
        gravity(warehouse.manifest[boxId], warehouse)
    return box

def gravity(box, warehouse):
    # find the bottom row and see if we can move the box down
    # print '\tgravity(): gravity on box', box.id
    initElevation = float("inf")
    # print box.coordinates
    for (x, y) in box.coordinates:
        # print (x, y)
        if y < initElevation:
            initElevation = y
            bottomRow = list()
        if y <= initElevation:
            bottomRow.append((x, y))
    # print 'bottomRow', bottomRow

    positions = ((warehouse.inventory[box.floor])[box.aisle])[box.layer].positions
    newElevation = initElevation
    while newElevation >= 1:
        # print 'new elevation', newElevation
        newBottomRow = list()
        exitEarly = False
        for (x, y) in bottomRow:
            # check below and move down if possible
            coord = (x, y-1)  # Check the next lowest coord
            # print positions[coord]
            if positions[coord] == ' x ':
                newBottomRow.append(coord)
            else:
                # print "whoops, box", positions[coord], "is in the way"
                exitEarly = True
                break # no multi-loop break statements :_(
        if exitEarly: break

        # We didn't find a box underneith, so we're good to move it down
        bottomRow = newBottomRow
        newElevation -= 1 # Check the next lowest elevation

    if newElevation != initElevation: #if we actually need to gravity it
        shift = initElevation - newElevation
        newCoordinates = list()
        for (x, y) in box.coordinates:
            positions[(x, y)] = ' x ' # empty these
            newCoord = (x, y - shift)
            newCoordinates.append(newCoord)
        box.setPosition(box.floor, box.aisle, box.layer, newCoordinates)
        for (x, y) in box.coordinates:
            positions[(x, y)] = box.id