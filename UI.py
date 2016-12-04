import Warehouse, RemoveBox, AddBox, PeekAt, re

def runUi(warehouse):
    print "Welcome to STG!"
    loop = True
    while loop:
        print "\nPlease enter an instruction."
        print "Valid instructions are:\n" \
              "\tadd box\n" \
              "\tremove <id> (example \"remove 001\")\n" \
              "\tview <id> (example \"view 001\")\n" \
              "\tshow warehouse\n" \
              "\texit"
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
                type = raw_input('Enter box type: type 1 (90cmX60cmX40cm) or type 2 (60cmX60cmX30cm): ')
                try:
                    if '1' in type:
                        box = Warehouse.Box(90, 60, 40, contents, id)
                        AddBox.AddBox(warehouse, box)
                        break
                    elif '2' in type:
                        box = Warehouse.Box(60, 60, 30, contents, id)
                        AddBox.AddBox(warehouse, box)
                        break
                    else:
                        print 'Invalid entry:', type
                except TypeError:
                    print 'Warehouse full'

        elif 'remove' in line:
            while 'exit' not in line and 'back' not in line and 'finish' not in line:
                match = re.match(r'^\s*remove (\w{3})\s*$', line, re.IGNORECASE)
                if match:
                    try:
                        RemoveBox.removeBox(match.group(1), warehouse)
                    except KeyError:
                        print match.group(1), 'isn\'t in the warehouse'
                    break
                else:
                    print 'Invalid remove command:', match
                    line = raw_input('Please enter \"remove <id>\" (example \"remove 001\" or \"back\" to go to the main menu: ')
        elif 'view' in line:
            while 'exit' not in line and 'back' not in line and 'finish' not in line:
                match = re.match(r'^\s*view (\w{3})\s*$', line, re.IGNORECASE)
                if match:
                    try:
                        PeekAt.Peek(warehouse, match.group(1))
                    except KeyError:
                        print match.group(1), 'isn\'t in the warehouse'
                    break
                else:
                    print 'Invalid remove command:', match
                    line = raw_input('Please enter \"view <id>\" (example \"view 001\" or \"back\" to go to the main menu: ')
        elif 'show' in line:
            warehouse.showWarehouse()
        else:
            print 'Invalid instruction'