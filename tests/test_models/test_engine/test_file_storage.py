#!/usr/bin/python3

"""
Unit testing the FileStorage
"""

import sys
from os.path import join, dirname, exists, abspath
import os.path
par = abspath(join(dirname(__file__), os.pardir))
sys.path.append(par)
par = abspath(join(par, os.pardir))
sys.path.append(par)
par = abspath(join(par, os.pardir))
sys.path.append(par)
from models.base_model import BaseModel  # noqa: E402
from models.engine.file_storage import FileStorage  # noqa: E402
import unittest  # noqa: E402
import datetime as dt  # noqa: E402


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Ensure a clean state before each test
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path
        self.file_storage._FileStorage__objects = {}

    def tearDown(self):
        # Remove the test file after each test
        if exists(self.file_path):
            os.remove(self.file_path)

    def test_all_new_save_reload(self):
        # Create a new instance of BaseModel
        base_model_instance = BaseModel()
        # Add the instance to the FileStorage
        self.file_storage.new(base_model_instance)
        # Save the objects to the test file
        try:
            self.file_storage.save()
        except Exception as e:
            self.fail(e)

        # Create a new instance of FileStorage
        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = self.file_path

        # Reload objects from the test file
        new_file_storage.reload()

        # Get all objects from the new FileStorage
        all_objects = new_file_storage.all()

        # Check if the reloaded objects match the original objects
        self.assertEqual(len(all_objects), 1)
        loaded_instance = list(all_objects.values())[0]
        self.assertEqual(loaded_instance.id, base_model_instance.id)
        self.assertEqual(loaded_instance.created_at,
                         base_model_instance.created_at)
        self.assertEqual(loaded_instance.updated_at,
                         base_model_instance.updated_at)
        self.assertEqual(loaded_instance.__class__.__name__,
                         base_model_instance.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
