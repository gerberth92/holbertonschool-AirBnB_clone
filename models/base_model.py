#!/usr/bin/python3
import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.save()

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, 
                                      self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        return (self.updated_at)

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)
    