import unittest
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):
    def test_rectangle_1_2_exists(self):
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)

    def test_rectangle_1_2_3_exists(self):
        r2 = Rectangle(1, 2, 3)
        self.assertIsInstance(r2, Rectangle)
