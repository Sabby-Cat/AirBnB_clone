#!/usr/bin/python3
"""
File storage data persist
"""

import uuid
from datetime import datetime
import json
import os


class FileStorage:
    '''
    Storage class
    '''
    __file_path = "persist.json"
    __objects = {}

    def all(self):
        """ returns the objects """
        return FileStorage.__objects

    def new(self, obj):
        """ appends a new file storage class """
        FileStorage.__objects[f"{type(obj)}.{obj.id}"] = obj

    def save(self):
        """ serialization """
        dct = {}
        for k,o in FileStorage.__objects:
            dct[k] = o.to_dict()
        json.dumps(FileStorage.__objects, FileStorage.__file_path)

    def reload(self):
        """ refresh everything """
        if os.path.exists(FileStorage.__file_path):
            FileStorage.__objects = json.loads(FileStorage.__file_path)

