"""
Unit tests for User model
"""
from web.models import User
from web.tests.django_type.generics import GenericModelTestCase


class UserModelTestCase(GenericModelTestCase):
    """ User Model TestCase """
    cls = User
    fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']
