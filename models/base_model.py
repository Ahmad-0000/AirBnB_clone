#!/usr/bin/python3
"""The base module"""
import uuid
import datetime


class BaseModel():
    """The base model class"""

    def __init__(self):
        """Initialization method"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Overriden __str__ method"""

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Setting the update time to now"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returning a dictionary representation"""

        dict_repr = self.__dict__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        dict_repr['__class__'] = self.__class__.__name__
        return dict_repr
