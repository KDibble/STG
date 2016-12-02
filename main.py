import Warehouse, RemoveBox, AddBox, PeekAt, re

print "Welcome to STG!"
testWarehouse = Warehouse.Create_Warehouse(30, 6, 9, 1) # small warehouse for testing visibility
# # warehouse = Warehouse.Create_Warehouse(50, 50, 50, 2)
# box = Warehouse.Box(60, 30, 30, "stuff", '001')
# AddBox.AddBox(testWarehouse, box)
# #box.setPosition(0, 0, 0, {(0, 0), (1, 0)})
# box2 = Warehouse.Box(60, 30, 30, "stuff2", '002')
# AddBox.AddBox(testWarehouse, box2)
# #box2.setPosition(0, 0, 0, {(0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)})
# box3 = Warehouse.Box(90, 40, 40, "stuff3", '003')
# AddBox.AddBox(testWarehouse, box3)
# #box3.setPosition(0, 0, 0, {(2, 0)})
# box4 = Warehouse.Box(60, 30, 30, "stuff4", '004')
# AddBox.AddBox(testWarehouse, box4)
# #box4.setPosition(0, 0, 0, {(0, 3)})
#
# #testWarehouse.placeBox(box, 0, 0, 0, 0, 0)
# #testWarehouse.placeBox(box2, 0, 0, 0, 0, 1)
# # testWarehouse.placeBox(box3, 0, 0, 0, 2, 0) # uncomment this to see gravity properly not falling the boxes
# #testWarehouse.placeBox(box4, 0, 0, 0, 0, 3)
# #warehouse.placeBox(Warehouse.Box(4, 2, 1, "2"), 0, 0, 0, 2, 0)
# #warehouse.placeBox(Warehouse.Box(4, 2, 1, "3"), 0, 0, 0, 0, 2)
# #warehouse.inventory[0][0][0].showShelf()
# testWarehouse.showWarehouse()
#
# # if box.id in testWarehouse.manifest:
# #     print box.id, "is in manifest"
# # if box2.id in testWarehouse.manifest:
# #     print box2.id, "is in manifest"
# # print "total manifest", testWarehouse.manifest
# # print box.id, "is", (testWarehouse.manifest[box.id])
# # print box2.id, "is", (testWarehouse.manifest[box2.id])
# # print box.id, "is at", (testWarehouse.manifest[box.id]).coordinates
# # print box2.id, "is at", (testWarehouse.manifest[box2.id]).coordinates
#
# RemoveBox.removeBox(box.id, testWarehouse)
# print 'removed box', box.id
# testWarehouse.showWarehouse()
# print "Goodbye"

print "Welcome to STG!"
loop = True
while loop:
    print "\nPlease enter an instruction."
    print "Valid instructions are:\n" \
          "\t\"add box\"\n" \
          "\t\"remove <id>\" (example \"remove 001\")\n" \
          "\tshow warehouse\n" \
          "\t\"exit\""
    line = raw_input()
    # print line

    if 'finish' in line or 'exit' in line or 'end' in line:
        loop = False
    elif 'add' in line:
        id = raw_input('Enter box id (3 digit): ')
        while len(id)!= 3:
            print 'Please enter a 3 digit string'
            id = raw_input('Enter box id (3 digit): ')

        contents = raw_input('Enter box contents: ')

        while True:
            type = raw_input('Enter box type: type 1 (60cmX90cmX40cm) or type 2 (60cmX60cmX30cm): ')
            if '1' in type:
                box = Warehouse.Box(60, 90, 40, contents, id)
                AddBox.AddBox(testWarehouse, box)
                break
            elif '2' in type:
                box = Warehouse.Box(60, 30, 30, contents, id)
                AddBox.AddBox(testWarehouse, box)
                break
            else:
                print 'Invalid entry:', type

    elif 'remove' in line:
        while 'exit' not in line and 'back' not in line and 'finish' not in line:
            match = re.match(r'^\s*remove (\w{3})\s*$', line, re.IGNORECASE)
            if match:
                try:
                    RemoveBox.removeBox(match.group(1), testWarehouse)
                except KeyError:
                    print match.group(1), 'isn\'t in the warehouse'
                break
            else:
                print 'Invalid remove command:', match
                line = raw_input('Please enter \"remove <id>\" (example \"remove 001\" or \"back\" to go to the main menu: ')
    elif 'show' in line:
        testWarehouse.showWarehouse()
    else:
        print 'Invalid instruction'