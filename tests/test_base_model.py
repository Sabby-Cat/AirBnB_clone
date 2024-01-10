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


class TestBase(unittest.TestCase):
    '''
    class to test the test base model
    '''

    def test_init(self):
        b = BaseModel()
        self.assertEqual(type(b), BaseModel,
                         "Type mismatch")

    def test_id(self):
        list_ = []
        for _ in range(100):
            b = BaseModel()
            self.assertFalse(b.id in list_, "UUID exists")
            list_.append(b.id)

    def test_dates(self):
        o = dt.datetime.now()
        b = BaseModel()
        self.assertIsNotNone(b.created_at,
                             "Timing problem")
        self.assertIsNotNone(b.updated_at,
                             "Timing problem")


if __name__ == "__main__":
    unittest.main()
