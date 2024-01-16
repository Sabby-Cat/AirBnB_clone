#!/usr/bin/python3
"""
Base model for the project
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    Base model class
    '''

    def __init__(self, *args, **kwargs):
        '''
        initialiser with ability to load from json
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # call the method in the storage
            storage.new(self)

    def __str__(self) -> str:
        '''
        print stuff
        '''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def toStr(self) -> str:
        '''
        return stuff
        '''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        saves the class
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        converts object to dict
        '''
        obj_dct = self.__dict__.copy()
        obj_dct['__class__'] = self.__class__.__name__
        obj_dct['created_at'] = self.created_at.isoformat()
        obj_dct['updated_at'] = self.updated_at.isoformat()
        return obj_dct

    @classmethod
    def all(cls):
        """ return all classes """
        lst = []
        for o in storage.all().values():
            if type(o) == cls:
                lst.append(o)
        return lst


if __name__ == "__main__":
    b = BaseModel()
    b2 = BaseModel(**b.to_dict())
