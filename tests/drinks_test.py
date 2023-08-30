import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("latte", 3, 5)
    
    def test_drink_has_name(self):
        self.assertEqual("latte", self.drink.name)
    # test fails when "latte" is replaced with anything else -> pass is not false positive!

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)
    # test fails with values other than 3 -> pass is not false positive!
