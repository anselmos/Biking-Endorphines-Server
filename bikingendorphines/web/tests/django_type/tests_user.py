"""
Unit tests for User model
"""
from django.test import TestCase
import logging

from web.models import User

class GenericModelTestCase(TestCase):
    cls = None
    fields = []

    def assert_fields(self, expected):
        """ testing if fields exists in model"""
        fields_in_model = []
        # fields as django fields:
        for field in self.cls._meta.get_fields(include_hidden=True):
            if field.name in expected:
                fields_in_model.append(field.name)
        # method as fields:
        for method in self.cls.__dict__:
            if method in expected and method not in fields_in_model:
                fields_in_model.append(method)
        assert sorted(set(fields_in_model).intersection(expected)) == sorted(expected)


class UserModelTestCase(GenericModelTestCase):
    cls = User
    fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']

    def test_fields(self):
        self.assert_fields(self.fields)
