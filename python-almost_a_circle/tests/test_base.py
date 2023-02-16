import unittest
from models.base import Base
from models.rectangle import Rectangle

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
        
    def test_save_passed_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)
        
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        
    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        
    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])
        
    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        
    def test_from_json_string_one_dict(self):
        dict = [{'id': 89, 'x': 0, 'y': 0, 'width': 1, 'height': 1}]
        self.assertEqual(Base.from_json_string('[{"id": 89, "x": 0, "y": 0, "width": 1, "height": 1}]'), dict)
    
    def Test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)

    def Test_rectangle_2(self):
        r2 = Rectangle(1, 2, 3)
        self.assertIsInstance(r2, Rectangle)
