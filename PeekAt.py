def Peek(warehouse, id):
    if warehouse.manifest[id] == None:
        print "Does not exist in manifest"
    else:
        print "Box ", id, "contents are ", warehouse.manifest[id].contents