"""
Unit tests for Route model
"""

from web.models import Route
from web.tests.django_type.generics import GenericModelTestCase


class RouteModelTestCase(GenericModelTestCase):
    """ Route Model TestCase """
    cls = Route
    fields = ['id', 'route_name', 'avg_route']
