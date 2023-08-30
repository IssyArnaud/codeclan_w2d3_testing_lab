class CoffeeShop:
    def __init__(self, input_name, input_till, input_drinks, input_foods):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks
        self.foods = input_foods
    
    def sell_drink(self, input_drink, input_customer):
        if input_customer.age > 16 and input_customer.energy < 20:
            self.till += input_drink.price
            input_customer.buy_drink(input_drink)
            self.drinks[input_drink] -= 1
    
    def sell_food(self, input_food, input_customer):
        self.till += input_food.price
        input_customer.buy_food(input_food)
    
    def stock_value(self):
        stock_value = 0
        for drink, stock in self.drinks.items():
            stock_value += (drink.price * stock)
        return stock_value