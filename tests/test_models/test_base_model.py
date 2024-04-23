"""A module to test BaseModel class"""
import unittest
import uuid
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing "BaseModel" class"""

    def test_id_type(self):
        """Testing "id" attribute type"""

        m = BaseModel()
        self.assertIs(type(m.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute type and values"""

        m = BaseModel()
        self.assertIs(type(m.created_at), type(datetime.datetime.now()))
        self.assertEqual(m.created_at.year, datetime.datetime.now().year)
        self.assertEqual(m.created_at.month, datetime.datetime.now().month)
        self.assertEqual(m.created_at.day, datetime.datetime.now().day)
        self.assertEqual(m.created_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.created_at.minute, datetime.datetime.now().minute)

    def test_updated_at(self):
        """Testing "updated_at" attribute type and values"""

        m = BaseModel()
        self.assertIs(type(m.updated_at), type(datetime.datetime.now()))
        self.assertEqual(m.updated_at.year, datetime.datetime.now().year)
        self.assertEqual(m.updated_at.month, datetime.datetime.now().month)
        self.assertEqual(m.updated_at.day, datetime.datetime.now().day)
        self.assertEqual(m.updated_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.updated_at.minute, datetime.datetime.now().minute)

    def test___str___method(self):
        """Testing "__str__" method return value type"""

        m = BaseModel()
        self.assertIs(type(m.__str__()), str)

    def test_save_method(self):
        """Testing "save" method functionality"""

        m = BaseModel()
        m.save()
        self.assertIs(type(m.updated_at), type(datetime.datetime.now()))
        self.assertEqual(m.updated_at.year, datetime.datetime.now().year)
        self.assertEqual(m.updated_at.month, datetime.datetime.now().month)
        self.assertEqual(m.updated_at.day, datetime.datetime.now().day)
        self.assertEqual(m.updated_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.updated_at.minute, datetime.datetime.now().minute)

    def test_to_dict_method(self):
        """Testing "to_dict" method functioality and return value type
        and properties"""

        m = BaseModel()
        dict_repr = m.to_dict()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr['id'], m.id)
        self.assertEqual(dict_repr['created_at'], m.created_at.isoformat())
        self.assertEqual(dict_repr['updated_at'], m.updated_at.isoformat())
        self.assertEqual(dict_repr['__class__'], m.__class__.__name__)
        self.assertFalse(dict_repr == m.__dict__)
        self.assertFalse(dict_repr is m.__dict__)

    def test_to_dict_method_return_value(self):
        """Testing "to_dict" method affect on "created_at" and "updated_at"
        attributes"""

        m = BaseModel()
        dict_repr = m.to_dict()
        self.assertIs(type(dict_repr['created_at']), str)
        self.assertIs(type(dict_repr['updated_at']), str)
