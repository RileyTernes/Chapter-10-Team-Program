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