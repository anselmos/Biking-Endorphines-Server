"""
Tests for GPXReader class
"""

import unittest
from nose_parameterized import parameterized

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

    @parameterized.expand([
        ('web/tests/example_data/fast_example.gpx'),
        ('web/tests/example_data/fast_example_trackpoints.gpx'),
        ('web/tests/example_data/fast_example_waypoints.gpx'),
        ('web/tests/example_data/fast_example_routepoints.gpx'),
    ])
    def test_get_points(self, gpxfile):
        """
        Tests if there will be data output from get_points.

        Test if:
        - points exists for different types.
        - what will happen if types exists, but no data?
        """
        gpxreader = GPXReader(gpxfile)
        points = []
        for point in gpxreader.get_points():
            points.append(point)
        assert len(points) > 0

    @parameterized.expand([
        ('web/tests/example_data/fast_example.gpx'),
        ('web/tests/example_data/fast_example_trackpoints.gpx'),
        ('web/tests/example_data/fast_example_waypoints.gpx'),
        ('web/tests/example_data/fast_example_routepoints.gpx'),
    ])
    def test_get_elevations(self, gpxfile):
        """
        Tests if all elevations will be returned from input element.
        Test should check if elements are TrackPoints Route Points or Way Points.
        """
        gpxreader = GPXReader(gpxfile)
        elevations = gpxreader.get_elevations()
        assert len(elevations) > 0

    @parameterized.expand([
        ('web/tests/example_data/fast_example.gpx', 224),
        ('web/tests/example_data/fast_example_trackpoints.gpx', 224),
        ('web/tests/example_data/fast_example_waypoints.gpx', 224),
        ('web/tests/example_data/fast_example_routepoints.gpx', 224),
    ])
    def test_get_elevations_len(self, gpxfile, elevations_len=224):
        """
        Test if proper amount of elevations are read by get_elevations method.
        """
        gpxreader = GPXReader(gpxfile)
        elevations = gpxreader.get_elevations()
        assert len(elevations) == elevations_len

if __name__ == '__main__':
    unittest.main()
