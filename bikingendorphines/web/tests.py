"""
Unit tests for web-application.
"""

# disabling because this import will be used in future
# pylint: disable=unused-import
from django.test import TestCase
from .models import User

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
        self.assertEqual(bart.bmi(), (80/(175*175)* 10000))
        self.assertEqual(trab.bmi(), (99/(175*175)* 10000))
