#!/usr/bin/python3
"""
Tests for base class
"""
import unittest
from models.base import Base
import json


class BaseClassTest(unittest.TestCase):
    """
    doc
    """

    def test_no_arg_base(self):
        """
        test id
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_increment(self):
        """
        is id increased
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_id_args(self):
        """
        is id set to value
        """
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_None(self):
        """
        id id set automatically
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)


class Test_methods(unittest.TestCase):
    """
    testing the to_json_string method
    """
    def test_to_json_string(self):
        """
        doc
        """
        b = Base()
        self.assertEqual(b.to_json_string(None), ("[]"))
        self.assertEqual(b.to_json_string([]), ("[]"))
        self.assertEqual((b.to_json_string([{'id': 24}])), json.dumps([{"id": 24}]))

    def test_from_json_string(self):
        """
        doc
        """
        b = Base()
        self.assertEqual(b.from_json_string(None), [])
        a = ""
        self.assertEqual(b.from_json_string(a), [])
        c = json.loads('[{"id": 24}]')
        self.assertEqual(b.from_json_string('[{"id": 24}]'), c)


if __name__ == "__main__":
    unittest.main()
