"""Testing "Place" class and objects"""
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Testing class"""

    def test_inheritacne(self):
        """Testing if "Place" inherites form "BaseModel" """

        p = Place()
        self.assertIsInstance(p, BaseModel)

    def test_id(self):
        """Testing "id" attribute presence and type"""

        p = Place()
        self.assertTrue(p.id)
        self.assertIs(type(p.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute presence, type and
        values"""

        p = Place()
        self.assertTrue(p.created_at)
        self.assertIs(type(p.created_at), datetime)
        self.assertEqual(p.created_at.year, datetime.now().year)
        self.assertEqual(p.created_at.month, datetime.now().month)
        self.assertEqual(p.created_at.day, datetime.now().day)
        self.assertEqual(p.created_at.hour, datetime.now().hour)
        self.assertEqual(p.created_at.minute, datetime.now().minute)

    def test_updated_at(self):
        """Testing "updated_at" attribute presence, type and
        values"""

        p = Place()
        self.assertTrue(p.updated_at)
        self.assertIs(type(p.updated_at), datetime)
        self.assertEqual(p.updated_at.year, datetime.now().year)
        self.assertEqual(p.updated_at.month, datetime.now().month)
        self.assertEqual(p.updated_at.day, datetime.now().day)
        self.assertEqual(p.updated_at.hour, datetime.now().hour)
        self.assertEqual(p.updated_at.minute, datetime.now().minute)

    def test_name(self):
        """Testing intial "name" attribute in terms of absence
        and type"""

        p = Place()
        self.assertFalse(p.name)
        self.assertIs(type(p.name), str)

    def test_city_id(self):
        """Testing "city_id" attribute in terms of absence
        and type"""

        p = Place()
        self.assertFalse(p.city_id)
        self.assertIs(type(p.city_id), str)

    def test_user_id(self):
        """Testing "user_id" attribute in terms of absence
        and type"""

        p = Place()
        self.assertFalse(p.user_id)
        self.assertIs(type(p.user_id), str)

    def test_description(self):
        """Testing "description" attribute in terms of absence
        and type"""

        p = Place()
        self.assertFalse(p.description)
        self.assertIs(type(p.description), str)

    def test_number_rooms(self):
        """Testing "number_rooms" attribute in terms of value
        and type"""

        p = Place()
        self.assertEqual(p.number_rooms, 0)
        self.assertIs(type(p.number_rooms), int)

    def test_number_bathrooms(self):
        """Testing "number_bathrooms" attribute in terms of
        value and type"""

        p = Place()
        self.assertEqual(p.number_bathrooms, 0)
        self.assertIs(type(p.number_bathrooms), int)

    def test_max_guest(self):
        """Testing "max_guest" attribute in terms of value
        and type"""

        p = Place()
        self.assertEqual(p.max_guest, 0)
        self.assertIs(type(p.max_guest), int)

    def test_price_by_night(self):
        """Testing "price_by_night" attribute in terms of value
        and type"""

        p = Place()
        self.assertEqual(p.price_by_night, 0)
        self.assertIs(type(p.price_by_night), int)

    def test_latitude(self):
        """Testing "latitude" attribute in terms of value
        and type"""

        p = Place()
        self.assertAlmostEqual(p.latitude, 0.0)
        self.assertIs(type(p.latitude), float)

    def test_longitude(self):
        """Testing "longitude" attribute in terms of value
        and type"""

        p = Place()
        self.assertAlmostEqual(p.longitude, 0.0)
        self.assertIs(type(p.longitude), float)

    def test_amenity_ids(self):
        """Testing "amenity_ids" attribute in terms of presence
        and type"""

        p = Place()
        self.assertFalse(p.amenity_ids)
        self.assertIs(type(p.amenity_ids), list)
