import unittest

from models.base import Base
class mytestcases(unittest.TestCase):

    def testone(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        
    if __name__ == "__main__":
        unittest.main()
