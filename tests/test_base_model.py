#!/usr/bin/python3

"""
Unit testing the test_base
"""

import sys
from os.path import join, dirname
sys.path.append(join(dirname(__file__), ".."))
from models.base_model import *  # noqa: E402
import unittest  # noqa: E402
import datetime as dt  # noqa: E402
import re  # noqa: E402


class TestBase(unittest.TestCase):
    '''
    class to test the test base model
    '''

    def test_init(self):
        """ stuff """
        b = BaseModel()
        self.assertEqual(type(b), BaseModel,
                         "Type mismatch")

    def test_id(self):
        """ stuff """
        list_ = []
        for _ in range(100):
            b = BaseModel()
            self.assertFalse(b.id in list_, "UUID exists")
            list_.append(b.id)

    def test_dates(self):
        """ stuff """
        o = dt.datetime.now()
        b = BaseModel()
        self.assertIsNotNone(b.created_at,
                             "Timing problem")
        self.assertIsNotNone(b.updated_at,
                             "Timing problem")

    def test_dates_good(self):
        """ stuff """
        b = BaseModel()
        reg = re.compile("[0-9]{4}-\d{2}-\d{1,2} \d{2}:\d{2}:\d{2}.\d{1,}")  # noqa: W605
        self.assertRegex(str(b.updated_at), reg, "iso format not matched")

    def test_load(self):
        """ loader and parsing """
        b = BaseModel()
        b2 = BaseModel(**b.to_dict())
        for k in b.__dict__.keys():
            self.assertEqual(getattr(b, k), getattr(b2, k), "Problem parsing using __init__")

if __name__ == "__main__":
    unittest.main()
