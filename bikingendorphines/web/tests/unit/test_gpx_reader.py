"""
Tests for GPXReader class
"""

import unittest
import pytest

from web.utils import GPXReader

# TODO - find gpx file with : only TrackPoints
# TODO - find gpx file with : only Route Points
# TODO - find gpx file with : only Way Points

# TODO - find gpx file with all elements like TrackPoints, RoutePoints and WayPoints.

class BaseGPXReaderTest(unittest.TestCase):
    """
    A Prof Of Concept for creating one generalized GPXReader test class.
    It will then be inherited by other classes that will use TrackPoints example data,
    Route Points data and Way Points data using pytest-fixtures.
    """

    def setUp(self):
        'setUp'
        self.gpxreader = GPXReader('web/tests/example_data/fast_example.gpx')


    def test_get_points(self):
        """
        Tests if there will be data output from get_points.

        Test if:
        - points exists for different types.
        - what will happen if types exists, but no data?
        """
        points = []
        for point in self.gpxreader.get_points():
            points.append(point)
        assert len(points) > 0

    def test_get_elevations(self):
        """
        Tests if all elevations will be returned from input element.
        Test should check if elements are TrackPoints Route Points or Way Points.
        """
        elevations = self.gpxreader.get_elevations()
        assert len(elevations) > 0

    def test_get_elevations_len(self, elevations_len=224):
        """
        Test if proper amount of elevations are read by get_elevations method.
        """
        elevations = self.gpxreader.get_elevations()
        assert len(elevations) == elevations_len

if __name__ == '__main__':
    unittest.main()
