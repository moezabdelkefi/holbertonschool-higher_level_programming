import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        
    def test_id_increment_by_one(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def saving_the_id(self):
        b1 = Base(98)
        self.assertEqual(b1, Base)
        