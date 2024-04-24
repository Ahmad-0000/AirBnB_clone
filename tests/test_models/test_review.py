"""Testing "Review" class and objects"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Testing class"""

    def test_inheritacne(self):
        """Testing if "Review" inherites form "BaseModel" """

        r = Review()
        self.assertIsInstance(r, BaseModel)

    def test_id(self):
        """Testing "id" attribute presence and type"""

        r = Review()
        self.assertTrue(r.id)
        self.assertIs(type(r.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute presence, type and
        values"""

        r = Review()
        self.assertTrue(r.created_at)
        self.assertIs(type(r.created_at), datetime)
        self.assertEqual(r.created_at.year, datetime.now().year)
        self.assertEqual(r.created_at.month, datetime.now().month)
        self.assertEqual(r.created_at.day, datetime.now().day)
        self.assertEqual(r.created_at.hour, datetime.now().hour)
        self.assertEqual(r.created_at.minute, datetime.now().minute)

    def test_updated_at(self):
        """Testing "updated_at" attribute presence, type and
        values"""

        r = Review()
        self.assertTrue(r.updated_at)
        self.assertIs(type(r.updated_at), datetime)
        self.assertEqual(r.updated_at.year, datetime.now().year)
        self.assertEqual(r.updated_at.month, datetime.now().month)
        self.assertEqual(r.updated_at.day, datetime.now().day)
        self.assertEqual(r.updated_at.hour, datetime.now().hour)
        self.assertEqual(r.updated_at.minute, datetime.now().minute)

    def test_place_id(self):
        """Testing initial "place_id" attribute in terms of
        absence and type"""

        r = Review()
        self.assertFalse(r.place_id)
        self.assertIs(type(r.place_id), str)

    def test_user_id(self):
        """Testing initial "user_id" attribute in terms of
        absence and type"""

        r = Review()
        self.assertFalse(r.user_id)
        self.assertIs(type(r.user_id), str)

    def test_text(self):
        """Testing initial "text" attribute in terms of
        absence and type"""

        r = Review()
        self.assertFalse(r.text)
        self.assertIs(type(r.text), str)
