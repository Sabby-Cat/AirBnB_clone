#!/usr/bin/python3

"""
Unit testing the test_base
"""

from models.base_model import *
import unittest
import datetime as dt


class TestBase(unittest.TestCase):
    '''
    class to test the test base model
    '''

    def test_init(self):
        b = BaseModel()
        self.assertEqual(type(b), BaseModel, 
                         "Type mismatch")

    def test_id(self):
        l = []
        for _ in range(100):
            b = BaseModel()
            self.assertFalse(b.id in l, "UUID exists")
            l.append(b.id)

    def test_dates(self):
        o = dt.datetime.now()
        b = BaseModel()
        self.assertAlmostEqual(b.created_at, o, 
                               None, "Timing problem")
        self.assertAlmostEqual(b.updated_at, o, 
                               None, "Timing problem")
    
