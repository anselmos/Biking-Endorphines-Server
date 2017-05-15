"""
Unit tests for RoutePoint model
"""

from web.models import RoutePoint
from web.tests.django_type.generics import GenericModelTestCase


class RoutePointModelTestCase(GenericModelTestCase):
    """ RoutePoint Model TestCase """
    cls = RoutePoint
    fields = ['id', 'id_route', 'id_point']
