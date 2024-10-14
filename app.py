from models.expressflavour import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish


restaurantZeBurguer = Restaurant('Zé Burguer', 'Hamburguer')
drinkJuice = Drink('Watermelon Juice', 4.99, 'Large')
drinkJuice.applyDiscount()
dishChicken = Dish('Chicken', 14.99, 'Delicious chicken from Texas')
dishChicken.applyDiscount()
restaurantZeBurguer.addToMenu(dishChicken)
restaurantZeBurguer.addToMenu(drinkJuice)

def main():
    restaurantZeBurguer.showMenu

if __name__ == '__main__':
    main()