"""
Unit tests for User Badge model
"""
from web.models import UserBadge
from web.tests.django_type.generics import GenericModelTestCase


class UserBadgeModelTestCase(GenericModelTestCase):
    " User Badge Model Test Case "
    cls = UserBadge
    fields = [
        'id',
        'id_user',
        'id_badge',
        'id_route',
        'active',
        'badge_acquiring_date',
        'activation_modification_date'
    ]
