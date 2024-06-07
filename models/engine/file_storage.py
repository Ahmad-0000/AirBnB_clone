#!/usr/bin/python3
"""My JSON "serializatin/deserialization" code module"""
import json
import os
from datetime import datetime


class FileStorage():
    """The main class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returning a dictionary containing all the objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Adding a new object to "__objects" """
        from models.base_model import BaseModel
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {'BaseModel': BaseModel, 'Place': Place,
                   'Amenity': Amenity, 'City': City,
                   'Review': Review, 'State': State,
                   'User': User}

        obj_dict = obj.to_dict()
        k = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[k] = classes[obj.__class__.__name__](**obj_dict)

    def save(self):
        """Serializing "__objects" to the JSON file in "__file_path" """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict.update({key: value.to_dict()})
            json_file.write(json.dumps(obj_dict))

    def reload(self):
        """Desirializing the contents of the file in "__file_path" into
        "__objects". If the file is not present, nothing will be done"""

        if os.path.isfile(FileStorage.__file_path):
            file_path = FileStorage.__file_path
            with open(file_path, "r", encoding="utf-8") as json_file:
                from models.base_model import BaseModel
                from models.place import Place
                from models.amenity import Amenity
                from models.city import City
                from models.review import Review
                from models.state import State
                from models.user import User

                classes = {'BaseModel': BaseModel, 'Place': Place,
                           'Amenity': Amenity, 'City': City,
                           'Review': Review, 'State': State,
                           'User': User}
                file_content = json_file.read()
                dict_content = json.loads(file_content)
                for k, obj_repr in dict_content.items():
                    cls = k.split('.')[0]
                    FileStorage.__objects.update({k: classes[cls](**obj_repr)})
