import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_1(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    def test_rectangle_2(self):
        r = Rectangle(1, 2, 3)
        self.assertIsInstance(r, Rectangle)
