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

    def test_empty_kwargs_and_empty_args(self):
        """Testing when no "**kwargs" and no "*args" are passed,
        particularly testing "id", "created_at" and "updated_at"
        attributes as in their previous tests"""

        m = BaseModel()
        self.assertIs(type(m.id), str)
        self.assertIs(type(m.created_at), type(datetime.datetime.now()))
        self.assertEqual(m.created_at.year, datetime.datetime.now().year)
        self.assertEqual(m.created_at.month, datetime.datetime.now().month)
        self.assertEqual(m.created_at.day, datetime.datetime.now().day)
        self.assertEqual(m.created_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.created_at.minute, datetime.datetime.now().minute)
        self.assertIs(type(m.updated_at), type(datetime.datetime.now()))
        self.assertEqual(m.updated_at.year, datetime.datetime.now().year)
        self.assertEqual(m.updated_at.month, datetime.datetime.now().month)
        self.assertEqual(m.updated_at.day, datetime.datetime.now().day)
        self.assertEqual(m.updated_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.updated_at.minute, datetime.datetime.now().minute)

    def test_empty_kwargs_and_present_arg(self):
        """Testing when no "**kwargs" are passed but "*args" is passed,
        this test is a copy of the previous, but adjusted to meet the
        test aim"""

        m = BaseModel(12, 124, 21)
        self.assertIs(type(m.id), str)
        self.assertIs(type(m.created_at), type(datetime.datetime.now()))
        self.assertEqual(m.created_at.year, datetime.datetime.now().year)
        self.assertEqual(m.created_at.month, datetime.datetime.now().month)
        self.assertEqual(m.created_at.day, datetime.datetime.now().day)
        self.assertEqual(m.created_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.created_at.minute, datetime.datetime.now().minute)
        self.assertIs(type(m.updated_at), type(datetime.datetime.now()))
        self.assertEqual(m.updated_at.year, datetime.datetime.now().year)
        self.assertEqual(m.updated_at.month, datetime.datetime.now().month)
        self.assertEqual(m.updated_at.day, datetime.datetime.now().day)
        self.assertEqual(m.updated_at.hour, datetime.datetime.now().hour)
        self.assertEqual(m.updated_at.minute, datetime.datetime.now().minute)

    def test_present_kwargs_and_empty_args(self):
        """Testing when "**kwargs" are present and "*args" are
        absent"""

        m1 = BaseModel()
        m2 = BaseModel(**(m1.to_dict()))
        self.assertEqual(m2.id, m1.id)
        self.assertEqual(m2.created_at, m1.created_at)
        self.assertEqual(m2.updated_at, m1.updated_at)
        self.assertEqual(m1.created_at.year, m2.created_at.year)
        self.assertEqual(m1.created_at.month, m2.created_at.month)
        self.assertEqual(m1.created_at.day, m2.created_at.day)
        self.assertEqual(m1.created_at.hour, m2.created_at.hour)
        self.assertEqual(m1.created_at.minute, m2.created_at.minute)
        self.assertEqual(m1.created_at.year, m2.updated_at.year)
        self.assertEqual(m1.created_at.month, m2.updated_at.month)
        self.assertEqual(m1.created_at.day, m2.updated_at.day)
        self.assertEqual(m1.created_at.hour, m2.updated_at.hour)
        self.assertEqual(m1.created_at.minute, m2.updated_at.minute)
        self.assertIs(type(m2.id), str)
        self.assertIs(type(m2.created_at), datetime.datetime)
        self.assertIs(type(m2.updated_at), datetime.datetime)

    def test_present_kwargs_and_present_args(self):
        """ Testing when "**kwargs" and "*args" are both present. This
        test is similar to the previous, but some tests to check the
        ignorance of "*args" values are introduced"""

        m1 = BaseModel()
        m2 = BaseModel(34, 56, 12, **(m1.to_dict()))
        self.assertEqual(m2.id, m1.id)
        self.assertEqual(m2.created_at, m1.created_at)
        self.assertEqual(m2.updated_at, m1.updated_at)
        self.assertEqual(m1.created_at.year, m2.created_at.year)
        self.assertEqual(m1.created_at.month, m2.created_at.month)
        self.assertEqual(m1.created_at.day, m2.created_at.day)
        self.assertEqual(m1.created_at.hour, m2.created_at.hour)
        self.assertEqual(m1.created_at.minute, m2.created_at.minute)
        self.assertEqual(m1.created_at.year, m2.updated_at.year)
        self.assertEqual(m1.created_at.month, m2.updated_at.month)
        self.assertEqual(m1.created_at.day, m2.updated_at.day)
        self.assertEqual(m1.created_at.hour, m2.updated_at.hour)
        self.assertEqual(m1.created_at.minute, m2.updated_at.minute)
        self.assertIs(type(m2.id), str)
        self.assertIs(type(m2.created_at), datetime.datetime)
        self.assertIs(type(m2.updated_at), datetime.datetime)
        for i in [34, 56, 12]:
            with self.subTest(i=i):
                for j in [m2.id, m2.created_at, m2.updated_at]:
                    with self.subTest(j=j):
                        self.assertNotEqual(j, i)

        def test___class___key_ignorance(self):
            """Testing that that the value paired with the key
            "__class__" is not added when initializing using
            "**kwargs" """

            m1 = BaseModel()
            m2 = BaseModel(**(m1.to_dict()))
            self.assertIsNot(m1.__class__, None)
            self.assertIs(m2.__class__, None)

        def test_if_they_are_the_same(self):
            """Testing if the instance created form "**kwargs"
            of an another instance is equal to this instance"""

        m1 = BaseModel()
        m2 = BaseModel(**(m1.to_dict()))
        self.assertIsNot(m1, m2)
        self.assertNotEqual(m1, m2)
