"""
All generic type of classes used in django-tests
"""
from django.test import TestCase
from django.contrib.auth.models import User as AuthUser


class GenericModelTestCase(TestCase):
    """
    Generic Model Test Case.
    Contains:
    - assert_fields - assertion for checking if all fields in model exists
    """
    cls = AuthUser
    fields = []

    def assert_fields(self, fields):
        """ asserting if fields exists in model"""
        fields_in_model = []
        # fields as django fields:
        for field in self.cls._meta.get_fields(include_hidden=True):
            if field.name in fields:
                fields_in_model.append(field.name)
        # method as fields:
        for method in self.cls.__dict__:
            if method in fields and method not in fields_in_model:
                fields_in_model.append(method)
        assert sorted(set(fields_in_model).intersection(fields)) == sorted(fields)

    def test_fields(self):
        """ Uses asserting fields for checking with naming convention of django-type """
        self.assert_fields(self.fields)
