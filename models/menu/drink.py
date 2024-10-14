from models.menu.menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return self._name
    
    def applyDiscount(self):
        self._price -= round(self._price * 0.08, 2 )