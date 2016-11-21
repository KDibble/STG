import Warehouse

print "Welcome to STG!"
warehouse = Warehouse.Create_Warehouse()
warehouse.placeBox(Warehouse.Box(2, 2, 1, "1"), 0, 0, 0, 0, 0)
warehouse.placeBox(Warehouse.Box(4, 2, 1, "2"), 0, 0, 0, 2, 0)
warehouse.placeBox(Warehouse.Box(4, 2, 1, "3"), 0, 0, 0, 0, 2)
warehouse.inventory[0][0][0].showShelf()
print "Goodbye"