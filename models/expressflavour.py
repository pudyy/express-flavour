from models.avaliation import Avaliation
from models.menu.menu_item import MenuItem

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._avaliation = []
        self._menu = []
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def listRestaurants(cls):
        print(f"{'Name of the restaurant'.ljust(25)} | {'Category'.ljust(25)} | {'Avaliation'.ljust(25)} |{'Status'} ")
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.mediaAvaliation).ljust(25)} |{restaurant.active}')

    @property
    def active(self):
        return '⌧' if self._active else '☐'
    
    def alternateStatus(self):
        self._active = not self._active

    def receiveAvaliation(self, client, grade):
        if 0 < grade <= 5:
            avaliation = Avaliation(client, grade)
            self._avaliation.append(avaliation)


    @property
    def mediaAvaliation(self):
        if not self._avaliation:
            return 'Restaurant not avaliated yet' 
        sumGrades = sum(avaliation._grade for avaliation in self._avaliation)
        amountGrades = len(self._avaliation)
        media = round(sumGrades / amountGrades, 1)
        return media
        
    # def addDrinkToMenu(self, drink):
    #     self._menu.append(drink)

    # def addDishToMenu(self, dish):
    #     self._menu.append(dish)

    def addToMenu(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)

    @property
    def showMenu(self):
        print(f'Menu from restaurant {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item,'description'):
                dishMessage =f'{i}. Name: {item._name} | Price: ${item._price:.2f} | Description: {item.description}'
                print(dishMessage)
            else:
                drinkMessage =f'{i}. Name: {item._name} | Price: ${item._price} | Size: {item.size}'
                print(drinkMessage)
