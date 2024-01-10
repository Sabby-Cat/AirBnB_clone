#!/usr/bin/python3
"""
File storage data persist
"""

import uuid
from datetime import datetime
import json
import os
from ..base_model import BaseModel


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
        nm = FileStorage.__file_path
        if os.path.exists(nm):
            with open(nm, 'r', encoding='utf-8') as file:
                loaded = json.loads(file)
                for k,v in loaded:
                    class_name, _id = k.split('.')
                    if class_name == "BaseModel":
                        obj_ = BaseModel(**v)
                        self.__objects[k] = obj_
                    else:
                        print("UNKOWN CLASS ", class_name)
                FileStorage.__objects = json.loads(nm)

