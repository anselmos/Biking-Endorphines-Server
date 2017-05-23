"""
Unit tests for UserRoute model
"""

from web.models import UserRoute
from web.tests.django_type.generics import GenericModelTestCase


class UserRouteModelTestCase(GenericModelTestCase):
    """ UserRoute Model TestCase """
    cls = UserRoute
    fields = ['id', 'id_user', 'id_route']
