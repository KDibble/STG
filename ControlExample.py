import Warehouse, ControlUI

testWarehouse = Warehouse.Create_Warehouse(30, 6, 9, 1) # small warehouse for testing visibility
ControlUI.runUi(testWarehouse)