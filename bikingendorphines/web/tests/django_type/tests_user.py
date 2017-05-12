"""
Unit tests for User model
"""
from django.test import TestCase
import logging

from web.models import User

class UserModelTestCase(TestCase):

    def test_fields(self):
        """ testing if fields exists in model"""
        fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']
        fields_in_model = []
        # fields as django fields:
        for field in User._meta.get_fields(include_hidden=True):
            if field.name in fields:
                fields_in_model.append(field.name)
        # method as fields:
        for method in User.__dict__:
            if method in fields and method not in fields_in_model:
                fields_in_model.append(method)
        assert sorted(set(fields_in_model).intersection(fields)) == sorted(fields)
