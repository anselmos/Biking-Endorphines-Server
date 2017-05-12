"""
Unit tests for User model
"""
import logging

from web.models import User
from generics import GenericModelTestCase


class UserModelTestCase(GenericModelTestCase):
    cls = User
    fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']
