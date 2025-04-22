#RetailItem

class RetailItem:
    #has attributes; description, count, price
    def __init__(self, desc, count, price):
        self.__desc = desc
        self.__count = count
        self.__price = price
        
    #getter methods
    def get_desc(self):
        return self.__desc
    def get_count(self):
        return self.__count
    def get_price(self):
        return self.__price
    
    #setter methods
    def set_desc(self):
        desc = input('What is the name of the item? ')
        self.__desc = desc
    def set_count(self):
        count = int(input('How many units in the inventory? '))
        self.__count = count
    def set_price(self):
        price = float(input('What is the price of the item? '))
        self.__price = price
        
def main():
    cont = 'y'
    while cont == 'y':
        name = input('What item are you adding? ')
        item = RetailItem('none', 0, 0)
        item.set_desc()
        item.set_count()
        item.set_price()
        
      
main()