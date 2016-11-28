import Warehouse, RemoveBox, AddBox

print "Welcome to STG!"
testWarehouse = Warehouse.Create_Warehouse(30, 6, 9, 1) # small warehouse for testing visibility
# warehouse = Warehouse.Create_Warehouse(50, 50, 50, 2)
box = Warehouse.Box(60, 30, 30, "stuff", '001')
AddBox.AddBox(testWarehouse, box)
#box.setPosition(0, 0, 0, {(0, 0), (1, 0)})
box2 = Warehouse.Box(60, 30, 30, "stuff2", '002')
AddBox.AddBox(testWarehouse, box2)
#box2.setPosition(0, 0, 0, {(0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)})
box3 = Warehouse.Box(90, 40, 40, "stuff3", '003')
AddBox.AddBox(testWarehouse, box3)
#box3.setPosition(0, 0, 0, {(2, 0)})
box4 = Warehouse.Box(60, 30, 30, "stuff4", '004')
AddBox.AddBox(testWarehouse, box4)
#box4.setPosition(0, 0, 0, {(0, 3)})

#testWarehouse.placeBox(box, 0, 0, 0, 0, 0)
#testWarehouse.placeBox(box2, 0, 0, 0, 0, 1)
# testWarehouse.placeBox(box3, 0, 0, 0, 2, 0) # uncomment this to see gravity properly not falling the boxes
#testWarehouse.placeBox(box4, 0, 0, 0, 0, 3)
#warehouse.placeBox(Warehouse.Box(4, 2, 1, "2"), 0, 0, 0, 2, 0)
#warehouse.placeBox(Warehouse.Box(4, 2, 1, "3"), 0, 0, 0, 0, 2)
#warehouse.inventory[0][0][0].showShelf()
testWarehouse.showWarehouse()

# if box.id in testWarehouse.manifest:
#     print box.id, "is in manifest"
# if box2.id in testWarehouse.manifest:
#     print box2.id, "is in manifest"
# print "total manifest", testWarehouse.manifest
# print box.id, "is", (testWarehouse.manifest[box.id])
# print box2.id, "is", (testWarehouse.manifest[box2.id])
# print box.id, "is at", (testWarehouse.manifest[box.id]).coordinates
# print box2.id, "is at", (testWarehouse.manifest[box2.id]).coordinates

#RemoveBox.removeBox(box.id, testWarehouse)
#testWarehouse.showWharehouse()

print "Goodbye"
print ('qux' == ' x ')