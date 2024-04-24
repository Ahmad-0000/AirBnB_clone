"""Testing "State" class and objects"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Testing class"""

    def test_inheritacne(self):
        """Testing if "State" inherites form "BaseModel" """

        s = State()
        self.assertIsInstance(s, BaseModel)

    def test_id(self):
        """Testing "id" attribute presence and type"""

        s = State()
        self.assertTrue(s.id)
        self.assertIs(type(s.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute presence, type and
        values"""

        s = State()
        self.assertTrue(s.created_at)
        self.assertIs(type(s.created_at), datetime)
        self.assertEqual(s.created_at.year, datetime.now().year)
        self.assertEqual(s.created_at.month, datetime.now().month)
        self.assertEqual(s.created_at.day, datetime.now().day)
        self.assertEqual(s.created_at.hour, datetime.now().hour)
        self.assertEqual(s.created_at.minute, datetime.now().minute)

    def test_updated_at(self):
        """Testing "updated_at" attribute presence, type and
        values"""

        s = State()
        self.assertTrue(s.updated_at)
        self.assertIs(type(s.updated_at), datetime)
        self.assertEqual(s.updated_at.year, datetime.now().year)
        self.assertEqual(s.updated_at.month, datetime.now().month)
        self.assertEqual(s.updated_at.day, datetime.now().day)
        self.assertEqual(s.updated_at.hour, datetime.now().hour)
        self.assertEqual(s.updated_at.minute, datetime.now().minute)

    def test_name(self):
        """Testing intial "name" attribute in terms of absence
        and type"""

        s = State()
        self.assertFalse(s.name)
        self.assertIs(type(s.name), str)
