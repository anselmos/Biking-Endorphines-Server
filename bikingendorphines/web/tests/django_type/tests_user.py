"""
Unit tests for User model
"""
from django.test import TestCase
import logging

from web.models import User

class UserModelTestCase(TestCase):

    def test_fields(self):
        """ testing if fields exists in model"""
        fields = ['id', 'name', 'surname', 'weight', 'height']
        fields_in_model = []
        for field in User._meta.get_fields(include_hidden=True):
            if field.name in fields:
                fields_in_model.append(field.name)
        assert sorted(set(fields_in_model).intersection(fields)) == sorted(fields)
