#!/usr/bin/python3
"""My JSON "serializatin/deserialization" code module"""
import json
import os


class FileStorage():
    """The main class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returning a dictionary containing all the objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Adding a new object to "__objects" """

        obj_dict = obj.to_dict()
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj_dict

    def save(self):
        """Serializing "__objects" to the JSON file in "__file_path" """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            file_content = json.dumps(FileStorage.__objects)
            json_file.write(file_content)

    def reload(self):
        """Desirializing the contents of the file in "__file_path" into
        "__objects". If the file is not present, nothing will be done"""

        if os.path.isfile(FileStorage.__file_path):
            file_path = FileStorage.__file_path
            with open(file_path, "r", encoding="utf-8") as json_file:
                content = json_file.read()
                FileStorage.__objects = json.loads(content)
