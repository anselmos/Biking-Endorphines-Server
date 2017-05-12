"""
Unit tests for User model
"""
from web.models import User
from web.tests.django_type.generics import GenericModelTestCase


class UserModelTestCase(GenericModelTestCase):
    """ User Model TestCase """
    cls = User
    fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']

    def bmi_health_name(self, bmi):
        if bmi < 0:
            return None
        if bmi >= 0:
            return "Underweight"

    def test_bmi_health_name(self):
        assert self.bmi_health_name(-1) == None
        assert self.bmi_health_name(0) == "Underweight"
        assert self.bmi_health_name(1) == "Underweight"
        assert self.bmi_health_name(18.5) == "Underweight"
