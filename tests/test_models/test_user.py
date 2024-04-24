"""Testing "User" class"""
import unittest
import uuid
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testing "User" class class"""

    def test_inheritance(self):
        """Testing if the class "User" inherites from "BaseModel" """

        u = User()
        self.assertIsInstance(u, BaseModel)

    def test_first_name(self):
        """Testing initial "first_name" attribute value and
        type"""
        u = User()

        self.assertEqual(u.first_name, "")
        self.assertIs(type(u.first_name), str)

    def test_last_name(self):
        """Testing initial "last_name" attribute value and
        type"""
        u = User()

        self.assertEqual(u.last_name, "")
        self.assertIs(type(u.last_name), str)

    def test_email_name(self):
        """Testing initial "email" attribute value and
        type"""
        u = User()

        self.assertEqual(u.email, "")
        self.assertIs(type(u.email), str)

    def test_password(self):
        """Testing initial "password" attribute value and
        type"""
        u = User()

        self.assertEqual(u.password, "")
        self.assertIs(type(u.password), str)

    def test_id(self):
        """Testing "id" attribute in terms of presence of and
        type"""

        u = User()
        self.assertTrue(u.id)
        self.assertIs(type(u.id), str)

    def test_created_at(self):
        """Testing "created_at" attribute in terms of presence,
        some values and type"""

        u = User()
        self.assertTrue(u.created_at)
        self.assertEqual(u.created_at.year, datetime.now().year)
        self.assertEqual(u.created_at.month, datetime.now().month)
        self.assertEqual(u.created_at.day, datetime.now().day)
        self.assertEqual(u.created_at.hour, datetime.now().hour)
        self.assertEqual(u.created_at.minute, datetime.now().minute)
        self.assertIs(type(u.created_at), datetime)

    def test_updated_at(self):
        """Testing "updated_at" attribute in terms of presence,
        some values and type"""

        u = User()
        self.assertTrue(u.updated_at)
        self.assertEqual(u.updated_at.year, datetime.now().year)
        self.assertEqual(u.updated_at.month, datetime.now().month)
        self.assertEqual(u.updated_at.day, datetime.now().day)
        self.assertEqual(u.updated_at.hour, datetime.now().hour)
        self.assertEqual(u.updated_at.minute, datetime.now().minute)
        self.assertIs(type(u.updated_at), datetime)

    def test___str___method(self):
        """Testing "__str__" method return value presence,
        value and type"""

        u = User()
        self.assertTrue(u.__str__())
        self.assertIs(type(u.__str__()), str)
        u_str = f'[{u.__class__.__name__}] ({u.id}) {u.__dict__}'
        self.assertEqual(u.__str__(), u_str)

    def test_save_method(self):
        """Testing "save" method functionality"""

        u = User()
        u.save()
        self.assertIs(type(u.updated_at), datetime)
        self.assertEqual(u.updated_at.year, datetime.now().year)
        self.assertEqual(u.updated_at.month, datetime.now().month)
        self.assertEqual(u.updated_at.day, datetime.now().day)
        self.assertEqual(u.updated_at.hour, datetime.now().hour)
        self.assertEqual(u.updated_at.minute, datetime.now().minute)

    def test_to_dict_method(self):
        """Testing "to_dict" method functioality and return value
        presence, type and properties"""

        u = User()
        dict_repr = u.to_dict()
        self.assertTrue(dict_repr)
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr['id'], u.id)
        self.assertEqual(dict_repr['created_at'], u.created_at.isoformat())
        self.assertEqual(dict_repr['updated_at'], u.updated_at.isoformat())
        self.assertEqual(dict_repr['__class__'], u.__class__.__name__)
        self.assertFalse(dict_repr == u.__dict__)
        self.assertFalse(dict_repr is u.__dict__)

    def test_empty_kwargs_and_empty_args(self):
        """Testing when no "**kwargs" and no "*args" are passed,
        particularly testing "id", "created_at" and "updated_at"
        attributes as in their previous tests"""

        u = User()
        self.assertIs(type(u.id), str)
        self.assertIs(type(u.created_at), type(datetime.now()))
        self.assertEqual(u.created_at.year, datetime.now().year)
        self.assertEqual(u.created_at.month, datetime.now().month)
        self.assertEqual(u.created_at.day, datetime.now().day)
        self.assertEqual(u.created_at.hour, datetime.now().hour)
        self.assertEqual(u.created_at.minute, datetime.now().minute)
        self.assertIs(type(u.updated_at), type(datetime.now()))
        self.assertEqual(u.updated_at.year, datetime.now().year)
        self.assertEqual(u.updated_at.month, datetime.now().month)
        self.assertEqual(u.updated_at.day, datetime.now().day)
        self.assertEqual(u.updated_at.hour, datetime.now().hour)
        self.assertEqual(u.updated_at.minute, datetime.now().minute)

    def test_empty_kwargs_and_present_arg(self):
        """Testing when no "**kwargs" are passed but "*args" is passed,
        this test is a copy of the previous, but adjusted to meet the
        test aim"""

        u = User(12, 124, 21)
        self.assertIs(type(u.id), str)
        self.assertIs(type(u.created_at), type(datetime.now()))
        self.assertEqual(u.created_at.year, datetime.now().year)
        self.assertEqual(u.created_at.month, datetime.now().month)
        self.assertEqual(u.created_at.day, datetime.now().day)
        self.assertEqual(u.created_at.hour, datetime.now().hour)
        self.assertEqual(u.created_at.minute, datetime.now().minute)
        self.assertIs(type(u.updated_at), type(datetime.now()))
        self.assertEqual(u.updated_at.year, datetime.now().year)
        self.assertEqual(u.updated_at.month, datetime.now().month)
        self.assertEqual(u.updated_at.day, datetime.now().day)
        self.assertEqual(u.updated_at.hour, datetime.now().hour)
        self.assertEqual(u.updated_at.minute, datetime.now().minute)

    def test_present_kwargs_and_empty_args(self):
        """Testing when "**kwargs" are present and "*args" are
        absent"""

        u1 = User()
        u2 = User(**(u1.to_dict()))
        self.assertEqual(u2.id, u1.id)
        self.assertEqual(u2.created_at, u1.created_at)
        self.assertEqual(u2.updated_at, u1.updated_at)
        self.assertEqual(u1.created_at.year, u2.created_at.year)
        self.assertEqual(u1.created_at.month, u2.created_at.month)
        self.assertEqual(u1.created_at.day, u2.created_at.day)
        self.assertEqual(u1.created_at.hour, u2.created_at.hour)
        self.assertEqual(u1.created_at.minute, u2.created_at.minute)
        self.assertEqual(u1.created_at.year, u2.updated_at.year)
        self.assertEqual(u1.created_at.month, u2.updated_at.month)
        self.assertEqual(u1.created_at.day, u2.updated_at.day)
        self.assertEqual(u1.created_at.hour, u2.updated_at.hour)
        self.assertEqual(u1.created_at.minute, u2.updated_at.minute)
        self.assertIs(type(u2.id), str)
        self.assertIs(type(u2.created_at), datetime)
        self.assertIs(type(u2.updated_at), datetime)

    def test_present_kwargs_and_present_args(self):
        """ Testing when "**kwargs" and "*args" are both present. This
        test is similar to the previous, but some tests to check the
        ignorance of "*args" values are introduced"""

        u1 = User()
        u2 = User(34, 56, 12, **(u1.to_dict()))
        self.assertEqual(u2.id, u1.id)
        self.assertEqual(u2.created_at, u1.created_at)
        self.assertEqual(u2.updated_at, u1.updated_at)
        self.assertEqual(u1.created_at.year, u2.created_at.year)
        self.assertEqual(u1.created_at.month, u2.created_at.month)
        self.assertEqual(u1.created_at.day, u2.created_at.day)
        self.assertEqual(u1.created_at.hour, u2.created_at.hour)
        self.assertEqual(u1.created_at.minute, u2.created_at.minute)
        self.assertEqual(u1.created_at.year, u2.updated_at.year)
        self.assertEqual(u1.created_at.month, u2.updated_at.month)
        self.assertEqual(u1.created_at.day, u2.updated_at.day)
        self.assertEqual(u1.created_at.hour, u2.updated_at.hour)
        self.assertEqual(u1.created_at.minute, u2.updated_at.minute)
        self.assertIs(type(u2.id), str)
        self.assertIs(type(u2.created_at), datetime)
        self.assertIs(type(u2.updated_at), datetime)
        for i in [34, 56, 12]:
            with self.subTest(i=i):
                for j in [u2.id, u2.created_at, u2.updated_at]:
                    with self.subTest(j=j):
                        self.assertNotEqual(j, i)

        def test___class___key_ignorance(self):
            """Testing that that the value paired with the key
            "__class__" is not added when initializing using
            "**kwargs" """

            u1 = User()
            u2 = User(**(u1.to_dict()))
            self.assertIsNot(u1.__class__, None)
            self.assertIs(u2.__class__, None)

        def test_if_they_are_the_same(self):
            """Testing if the instance created form "**kwargs"
            of an another instance is equal to this instance"""

            u1 = User()
            u2 = User(**(u1.to_dict()))
            self.assertIsNot(u1, u2)
            self.assertNotEqual(u1, u2)
