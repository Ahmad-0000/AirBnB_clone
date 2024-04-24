import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    def test_all_method(self):
        """Testing the return value type of "all" """

        storage = FileStorage()
        self.assertIs(type(storage.all()), dict)

    def test_new(self):
        """Testing the functionality of "new" method"""

        m = BaseModel()
        storage = FileStorage()
        storage.new(m)
        objects = storage.all()
        self.assertEqual(m.to_dict(), objects[f'BaseModel.{m.id}'])

    def test_save(self):
        """Testing "save" method functionality, its created
        file existence and its content"""

        m = BaseModel()
        storage = FileStorage()
        storage.new(m)
        storage.save()
        json_file_name = FileStorage.__dict__['_FileStorage__file_path']
        self.assertTrue(os.path.isfile(json_file_name))
        with open(json_file_name, 'r', encoding='utf-8') as json_file:
            json_file_content = json_file.read()
            storage.reload()
            self.assertEqual(json_file_content, json.dumps(storage.all()))
            self.assertEqual(storage.all(), json.loads(json_file_content))
            self.assertIs(type(json.loads(json_file_content)), dict)

    def test_reload_method(self):
        """Testing "reload" method, in cases of file existence,
        file unexistence and effects on "__objects" attribute"""

        json_file_name = FileStorage.__dict__['_FileStorage__file_path']
        storage = FileStorage()
        if os.path.isfile(json_file_name):
            os.remove(json_file_name)
            m = BaseModel()
            storage.new(m)
            storage.save()
            self.assertTrue(os.path.isfile(json_file_name))
            with open(json_file_name, "r", encoding='utf-8') as json_file:
                storage.reload()
                self.assertEqual(json.load(json_file), storage.all())
                self.assertIs(type(storage.all()), dict)
        if os.path.isfile(json_file_name):
            os.remove(json_file_name)
            __objects_before = storage.all()
            storage.reload()
            __objects_after = storage.all()
            self.assertEqual(__objects_after, __objects_before)
            self.assertIs(type(__objects_after), dict)

    def test___init___effects(self):
        """Testing initialization effects on "__objects" dict.
        When a new uniqe instance is created and when it is
        created based on another instance dict"""

        __objects = storage.all()
        m1 = BaseModel()
        self.assertIn(f'BaseModel.{m1.id}', __objects.keys())
        m2 = BaseModel(**(m1.to_dict()))
        m1_state = __objects[f'BaseModel.{m1.id}']
        m2_state = __objects[f'BaseModel.{m2.id}']
        self.assertIs(m1_state, m2_state)
