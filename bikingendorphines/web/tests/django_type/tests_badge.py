"""
Unit tests for Badge model
"""
from web.models import Badge
from web.tests.django_type.generics import GenericModelTestCase


class BadgeModelTestCase(GenericModelTestCase):
    " Badge Model Test Case "
    cls = Badge
    fields = ['id', 'name', 'description']
