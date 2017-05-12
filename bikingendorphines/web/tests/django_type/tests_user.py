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
        if bmi >= 0 and bmi <= 18.5:
            return "Underweight"
        if bmi > 18.5 and bmi <= 24.9:
            return "Normal weight"
        if bmi > 24.9:
            return "Overweight"

    def assert_bmi_health(self, input, expected):
        assert self.bmi_health_name(input) == expected

    def test_bmi_health_name(self):
        self.assert_bmi_health(-1, None)
        self.assert_bmi_health(0, "Underweight")
        self.assert_bmi_health(1, "Underweight")
        self.assert_bmi_health(18.5, "Underweight")
        self.assert_bmi_health(18.6, "Normal weight")
        self.assert_bmi_health(25.0, "Overweight")
        self.assert_bmi_health(30.0, "Obesity")
