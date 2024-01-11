#!/usr/bin/python3
"""
File storage data persist
"""

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
        return self.__objects

    def new(self, obj):
        """ appends a new file storage class """
        self.__objects[f"{str(type(obj).__name__)}.{obj.id}"] = obj

    def save(self):
        """ serialization """
        dct = {}
        for k,o in self.__objects.items():
            dct[k] = o.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            data = json.dumps(dct)
            file.write(data)
            file.flush()
            

    def reload(self):
        """ refresh everything """
        nm = self.__file_path
        if os.path.exists(nm):
            with open(nm, 'r', encoding='utf-8') as file:
                loaded = json.load(file)
                for k,v in loaded.items():
                    class_name, _id = k.split('.')
                    if class_name == "BaseModel":
                        from ..base_model import BaseModel  # noqa: 402
                        obj_ = BaseModel(**v)
                        self.__objects[k] = obj_
                    else:
                        print("UNKOWN CLASS ", class_name)
