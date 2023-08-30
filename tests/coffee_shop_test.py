import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("brownie", 4, 4)
        self.drink_1 = Drink("latte", 3, 5)
        self.drink_2 = Drink("flat white", 2, 6)
        self.drink_3 = Drink("mocha", 4, 5)
        self.coffee_shop = CoffeeShop("Blend", 180, {self.drink_1 : 45, self.drink_2 : 45, self.drink_3 : 30}, [self.food_1])
        self.customer_1 = Customer("Laura", 27, 18, 3)
        self.customer_2 = Customer("Hamish", 12, 10, 6)
    
    def test_coffee_shop_has_till(self):
        self.assertEqual(180, self.coffee_shop.till)
    # test fails with values other than 180 -> pass is not false positive!

    def test_coffee_shop_has_drinks(self):
        self.assertEqual({self.drink_1 : 45, self.drink_2 : 45, self.drink_3 : 30}, self.coffee_shop.drinks)
    # test fails when list differs -> pass is not false positive!

    def test_coffee_shop_drink_has_price(self):
        self.assertEqual(self.drink_1.price, 3)
    # test fails with values other than 3 -> pass is not false positive!

    def test_sell_drink(self):
        self.coffee_shop.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(183, self.coffee_shop.till)
        self.assertEqual(15, self.customer_1.wallet)
    # test fails with other values -> pass is not false positive!

    def test_refuse_underage_customer(self):
        self.coffee_shop.sell_drink(self.drink_1, self.customer_2)
        self.assertEqual(180, self.coffee_shop.till)
        self.assertEqual(10, self.customer_2.wallet)
    # test only passes when till and wallet unchanged, 'if' clause successful - pass is not a false positive!

    def test_sell_food(self):
        self.coffee_shop.sell_food(self.food_1, self.customer_1)
        self.assertEqual(184, self.coffee_shop.till)
    # tested and passed, not false positive

    def test_sell_drink_stock_check(self):
        self.coffee_shop.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(44, self.coffee_shop.drinks[self.drink_1])
    # test works, yay
    
    def test_stock_value(self):
        self.assertEqual(345, self.coffee_shop.stock_value())
    # test works, yay