#ACME
import RetailItem
import CashRegister

def main():
    #calls menu to get choice
    choice = menu()
    #makes a decision based off of choice
    #calls the functions or quits
    if choice == 1:
        #do retail
        pass
    elif choice == 2:
        #do cash register
    elif choice == 3:
        quit()
    
def menu():
    #prints the menu
    #gets choice
    #validates choice and returns choice
    
    
def add_items():
    cont = 'y'
    outfile = open('inventory.dat', 'wb')

    while cont == 'y':
        name = input('What item are you adding? ')
        item = RetailItem('none', 0, 0)
        item.set_desc()
        item.set_count()
        item.set_price()

        print(f'{item.get_desc()} has {item.get_count()} units in inventory and is priced at ${item.get_price()}.')
        pickle.dump(item, outfile)
        cont = input('Would you like to continue? (y/n)')
    outfile.close()
    
def example_read():
    infile = open('inventory.dat', 'rb')
    lines = infile.read()
    lines = pickle.loads(lines)
    print()
    item = lines
    print(item.get_price())
    infile.close()