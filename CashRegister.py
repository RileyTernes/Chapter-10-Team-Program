#CashRegister
total = 0
class CashRegister:

    def __init__(self):
        self.__item = []
    
    def purchase_item(self, item):
        self._items.append(item)
        
    def get_total(self):
        for item in self._items
            total += item
            
        return total
    
    def show_items(self):
        return "\n".join(self._items)
    
            

