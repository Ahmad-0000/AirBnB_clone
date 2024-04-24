"""Testing "City" class and objects"""
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Testing class"""

    def test_inheritacne(self):
        """Testing if "City" inherites form "BaseModel" """

        c = City()
        self.assertIsInstance(c, BaseModel)

    def test_id(self):
        """Testing "id" attribute presence and type"""

        c = City()
        self.assertTrue(c.id)
        self.assertIs(type(c.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute presence, type and
        values"""

        c = City()
        self.assertTrue(c.created_at)
        self.assertIs(type(c.created_at), datetime)
        self.assertEqual(c.created_at.year, datetime.now().year)
        self.assertEqual(c.created_at.month, datetime.now().month)
        self.assertEqual(c.created_at.day, datetime.now().day)
        self.assertEqual(c.created_at.hour, datetime.now().hour)
        self.assertEqual(c.created_at.minute, datetime.now().minute)

    def test_updated_at(self):
        """Testing "updated_at" attribute presence, type and
        values"""

        c = City()
        self.assertTrue(c.updated_at)
        self.assertIs(type(c.updated_at), datetime)
        self.assertEqual(c.updated_at.year, datetime.now().year)
        self.assertEqual(c.updated_at.month, datetime.now().month)
        self.assertEqual(c.updated_at.day, datetime.now().day)
        self.assertEqual(c.updated_at.hour, datetime.now().hour)
        self.assertEqual(c.updated_at.minute, datetime.now().minute)

    def test_name(self):
        """Testing intial "name" attribute in terms of absence
        and type"""

        c = City()
        self.assertFalse(c.name)
        self.assertIs(type(c.name), str)

    def test_state_id(self):
        """Testing "state_id" attribute in terms of absence
        and type"""

        c = City()
        self.assertFalse(c.state_id)
        self.assertIs(type(c.state_id), str)
