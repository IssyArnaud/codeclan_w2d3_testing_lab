import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("brownie", 4, 4)
    
    def test_food_has_name(self):
        self.assertEqual("brownie", self.food.name)
    # tested and passed, not false positive