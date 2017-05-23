"""
Unit tests for User model
"""
from mock import MagicMock

from web.models import User
from web.tests.django_type.generics import GenericModelTestCase



class UserModelTestCase(GenericModelTestCase):
    """ User Model TestCase """
    cls = User
    fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']

    def setUp(self):
        """SetUp"""
        self.user = User()

    def assert_bmi_health(self, bmi, expected):
        """ Asserts BMI health name"""
        self.user.bmi = MagicMock(return_value=bmi)
        assert self.user.bmi_health_name() == expected

    def test_bmi_health_name(self):
        """ tests for bmi_health_name method """
        self.assert_bmi_health(-1, None)
        self.assert_bmi_health(0, "Underweight")
        self.assert_bmi_health(1, "Underweight")
        self.assert_bmi_health(18.5, "Underweight")
        self.assert_bmi_health(18.6, "Normal weight")
        self.assert_bmi_health(25.0, "Overweight")
        self.assert_bmi_health(30.0, "Obesity")


    def test_height_less_hundred(self):
        """ tests for height less then hundred if not raises ZeroDivisionError"""
        self.user.height = 99
        self.user.weight = 50
        self.user.name = "under hundred height"
        self.user.surname = "under fifty weight"

        self.assertEquals(self.user.bmi(), 51.02)
