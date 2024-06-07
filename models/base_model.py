#!/usr/bin/python3
"""The base module"""
import uuid
import datetime
from models import storage


class BaseModel():
    """The base model class"""

    def __init__(self, *args, **kwargs):
        """Initialization method"""

        if kwargs:
            for key in kwargs.keys():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    value = datetime.datetime.fromisoformat(kwargs[key])
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = kwargs[key]
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.datetime.now()
                self.updated_at = self.created_at
            if 'updated_at' not in kwargs.keys():
                self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Overriden __str__ method"""

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Setting the update time to now and saving the
        object into JSON file through "storage" instance"""

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returning a dictionary representation"""

        dict_repr = {}
        for key in self.__dict__.keys():
            dict_repr[key] = self.__dict__[key]
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        dict_repr['__class__'] = self.__class__.__name__
        return dict_repr
