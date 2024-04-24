"""Testing "Amenity" class and objects"""
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Testing class"""

    def test_inheritacne(self):
        """Testing if "Amenity" inherites form "BaseModel" """

        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_id(self):
        """Testing "id" attribute presence and type"""

        a = Amenity()
        self.assertTrue(a.id)
        self.assertIs(type(a.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute presence, type and
        values"""

        a = Amenity()
        self.assertTrue(a.created_at)
        self.assertIs(type(a.created_at), datetime)
        self.assertEqual(a.created_at.year, datetime.now().year)
        self.assertEqual(a.created_at.month, datetime.now().month)
        self.assertEqual(a.created_at.day, datetime.now().day)
        self.assertEqual(a.created_at.hour, datetime.now().hour)
        self.assertEqual(a.created_at.minute, datetime.now().minute)

    def test_updated_at(self):
        """Testing "updated_at" attribute presence, type and
        values"""

        a = Amenity()
        self.assertTrue(a.updated_at)
        self.assertIs(type(a.updated_at), datetime)
        self.assertEqual(a.updated_at.year, datetime.now().year)
        self.assertEqual(a.updated_at.month, datetime.now().month)
        self.assertEqual(a.updated_at.day, datetime.now().day)
        self.assertEqual(a.updated_at.hour, datetime.now().hour)
        self.assertEqual(a.updated_at.minute, datetime.now().minute)

    def test_name(self):
        """Testing intial "name" attribute in terms of absence
        and type"""

        a = Amenity()
        self.assertFalse(a.name)
        self.assertIs(type(a.name), str)
