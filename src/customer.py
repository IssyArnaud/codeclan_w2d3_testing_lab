class Customer:
    def __init__(self, input_name, input_age, input_wallet, input_energy):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.energy = input_energy
    
    def reduce_wallet(self, input_amount):
        self.wallet -= input_amount
    
    def buy_drink(self, input_drink):
        self.reduce_wallet(input_drink.price)
        self.energy += input_drink.caffeine_level
    
    def buy_food(self, input_food):
        self.reduce_wallet(input_food.price)
        self.energy -= input_food.digestion_level