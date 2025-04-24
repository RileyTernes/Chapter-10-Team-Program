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
        retail_menu()
    elif choice == 2:
        #do cash register
        cash_register_system()
    elif choice == 3:
        quit()
    else:
        print('Please choose one of the above.')
        main()
def menu():
    #prints the menu
    #gets choice
    #validates choice and returns choice
    print('Welcome to the ACME inventory system.')
    print('Please choose an option.')
    print()
    print('Inventory system(1)')
    print('Retail system(2)')
    print('Quit(3)')
    print()
    choice = input('What would you like to do? ')
    return choice
    
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
    
def retail_menu():
    print()
    print('Display cart(1)')
    print('Display items(2)')
    print('Purchase cart(3)')
    print('Empty cart(4)')
    print('Quit(5)')
    print()
    choice = input('What would you like to choose? ')
main()