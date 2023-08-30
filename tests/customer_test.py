import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Laura", 27, 18, 3)
        self.drink_1 = Drink("latte", 3, 5)
        self.food_1 = Food("brownie", 4, 4)
    
    def test_customer_has_wallet(self):
        self.assertEqual(18, self.customer.wallet)
    # test fails with values other than 18 -> not a false positive!

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3)
        self.assertEqual(15, self.customer.wallet)
    # test fails with other values -> not a false positive!

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink_1)
        self.assertEqual(15, self.customer.wallet)
    # test fails with other values -> not a false positive!

    def test_increase_energy(self):
        self.customer.buy_drink(self.drink_1)
        self.assertEqual(8, self.customer.energy)
    # test fails with other values -> not a false positive!

    def test_buy_food(self):
        self.customer.buy_food(self.food_1)
        self.assertEqual(14, self.customer.wallet)
    # tested and passed, not false positive

    def test_decrease_energy(self):
        self.customer.buy_food(self.food_1)
        self.assertEqual(-1, self.customer.energy)
    # tested and passed, not false positive