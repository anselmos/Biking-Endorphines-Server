"""
Unit tests for web-application.
"""
from django.test import TestCase

from parameterized import parameterized

from .models import User
from .utils import GPXReader

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

class GPXReaderTestCase(TestCase):
    """
    Tests all GPXReader class cases for methods access.
    """
    @parameterized.expand([
        ('bikingendorphines/example_data/15212277.gpx'),
    ])
    def test_get_points(self, gpx_file):
        """
        Tests if there will be data output from get_points.

        Test if:
        - points exists for different types.
        - what will happen if types exists, but no data?
        """
        gpxreader = GPXReader(gpx_file)
        points = []
        for point in gpxreader.get_points():
            points.append(point)
        self.assertGreater(len(points), 0)
