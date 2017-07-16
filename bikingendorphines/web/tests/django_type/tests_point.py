"""
Unit tests for Point model
"""

from web.models import Point
from web.tests.django_type.generics import GenericModelTestCase


class PointModelTestCase(GenericModelTestCase):
    """ Point Model TestCase """
    cls = Point
    fields = ['id', 'lat', 'lon', 'elevation', 'time']
