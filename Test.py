import Warehouse, UI

print "Welcome to STG!"
myWarehouse = Warehouse.Create_Warehouse(30, 12, 18, 1)  # small warehouse for testing visibility
UI.runUi(myWarehouse)