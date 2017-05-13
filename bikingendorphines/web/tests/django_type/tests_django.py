"""
Unit tests for web-application.
"""
from django.test import TestCase

from web.models import User

class UserTestCase(TestCase):
    """
    A User-class test-case
    """

    def setUp(self):
        User.objects.create(name='Bart', weight=80, height=175)
        User.objects.create(name='Trab', weight=99, height=175)

    def test_user_bmi(self):
        """
        Tests if users has been created in db
        """
        bart = User.objects.get(name='Bart')
        trab = User.objects.get(name='Trab')
        self.assertEqual(bart.bmi(), 26)
        self.assertEqual(bart.bmi_health_name(), "Overweight")
        self.assertEqual(trab.bmi_health_name(), "Obesity")
