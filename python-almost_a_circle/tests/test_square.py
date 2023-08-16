#!/usr/bin/python3
"""
testing rectangle
"""

import unittest
import json
#from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    doc
    """
    def test_square(self):
        """
        doc
        """
        r1 = Square(1)
        r2 = Square(1,2)
        r3 = Square(1,2,3)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r3.y, 3)
        #self.assertEqual(r3.y, 4)

    def test_square_args(self):
        """
        doc
        """
        self.assertRaises(TypeError, Square, "1")
        #self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Square, 1,"4")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, 1, 2, -6,)
        self.assertRaises(ValueError, Square, 1, -3,4)
        self.assertRaises(ValueError, Square, -2,3,4)
        #self.assertRaises(ValueError,Rectangle, -1,2,3,4)
        self.assertEqual(Square(1,2,3,5).id, 5)
        self.assertRaises(ValueError, Square, 0, )
        #self.assertRaises(ValueError, Rectangle,1, 0)

    def test_methods(self):
        """
        doc
        """
        r2 = Square(2, id=24)
        self.assertEqual(r2.area(), 4)
        self.assertEqual(r2.__str__(), "[Square] (24) 0/0 - 2")

    def test_methods_update(self):
        """
        doc
        """
        r = Square(10, id=12)
        r.update(1)
        self.assertNotEqual(r.id, 12)
        r.update(1,2)
        self.assertNotEqual(r.size, 10)
        #r.update(1,2,3)
        #self.assertNotEqual(r.height, 12)
        r.update(1,2,3)
        self.assertNotEqual(r.x, 0)
        r.update(1,2,3,4)
        self.assertNotEqual(r.y, 0)
        #passing now a dict to update
        self.assertNotEqual(r.id, r.update(**{"id": 89}))
        self.assertNotEqual(r.width, r.update(**{"id": 89, "size": 3}))
        #self.assertNotEqual(r.height, r.update(**{"id": 89, "size": 4, "height": 21}))
        self.assertNotEqual(r.x, r.update(**{"id": 89, "width": 4, "x": 3}))
        self.assertNotEqual(r.y, r.update(**{"id": 89, "width": 4, "x": 3, "y": 6}))

    def test_to_dict(self):
        """
        doc
        """
        r = Square(1, id=12)
        self.assertEqual(r.to_dictionary(), {"id": 12, "x": 0, "y": 0, "size": 1})


    def test_create(self):
        """
        doc
        """
        r = Square.create(**{"id": 23})
        self.assertEqual(r.id, 23)
        r = Square.create(**{"id": 23, "size": 2})
        self.assertEqual(r.size, 2)
        #r = Rectangle.create(**{"id": 23, "width": 2, "height": 3})
        #self.assertEqual(r.height, 3)
        r = Square.create(**{"id":23, "size": 2, "x": 2})
        self.assertEqual(r.x, 2)
        r = Square.create(**{"id":23, "size": 2, "x": 2, "y": 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file(self):
        """
        doc
        """
        r = Square(1, id=23)
        Square.save_to_file(None)
        with open("Square.json") as f:
            cont = f.read()
            self.assertEqual(cont, '[]')
        Square.save_to_file([])
        with open("Square.json")as f:
            content = f.read()
            self.assertEqual(content, '[]')
        Square.save_to_file([r])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[{"size": 1, "x": 0, "y": 0, "id": 23}]')

    def test_load_from_file(self):
        """
        doc
        """
        Square.save_to_file([])
        my_list = Square.load_from_file()
        self.assertEqual(my_list, [])

    def test_load_from_file2(self):
        """
        doc
        """
        r = Square(2)
        Square.save_to_file([r])
        my_list = Square.load_from_file()
        self.assertEqual(type(my_list[0]), type(Square.create(**r.to_dictionary())))
