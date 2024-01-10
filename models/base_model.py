#!/usr/bin/python3
"""
Base model for the project
"""

import uuid
import datetime


class BaseModel:
    '''
    Base model class
    '''

    def __init__(self):
        '''
        initialiser
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        '''
        print stuff
        '''
        print(f"[{type(self)}] ({self.id}) {self.__dict__}")

    def __save__(self):
        '''
        saves the class
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        converts object to dict
        '''
        obj_dct = self.__dict__.copy()
        obj_dct['__class__'] = self.__class__.__name__
        obj_dct['created_at'] = self.created_at.iso_format()
        obj_dct['updated_at'] = self.updated_at.iso_format()
        return obj_dct
