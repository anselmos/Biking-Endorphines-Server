"""
Tests for GPXReader class
"""

import unittest
from nose_parameterized import parameterized

from web.utils import GPXReader

# pylint: disable=fixme
# TODO - create gpx file with all elements like TrackPoints, RoutePoints and WayPoints.
# (unlikely to happen, need to check)
DEFAULT_GPXFILE_SAMPLE = 'web/tests/example_data/fast_example.gpx'

class BaseGPXReaderTest(unittest.TestCase):
    """
    A Prof Of Concept for creating one generalized GPXReader test class.
    It will then be inherited by other classes that will use TrackPoints example data,
    Route Points data and Way Points data using pytest-fixtures.
    """

    def set_gpxreader(self, gpxfile):
        "Sets gpxreader - for parameterized gpx file."
        self.gpxreader.process_gpx_file(gpxfile)

    def setUp(self):
        "Setup for creating default GPXReader sample file"
        self.gpxreader = GPXReader(DEFAULT_GPXFILE_SAMPLE)

    @parameterized.expand([
        ('web/tests/example_data/fast_example_trackpoints.gpx'),
        ('web/tests/example_data/fast_example_waypoints.gpx'),
        ('web/tests/example_data/fast_example_routepoints.gpx'),
    ])
    def test_get_points(self, gpxfile=DEFAULT_GPXFILE_SAMPLE):
        """
        Tests if there will be data output from get_points.

        Test if:
        - points exists for different types.
        - what will happen if types exists, but no data?
        """
        self.gpxreader.process_gpx_file(gpxfile)
        points = []
        for point in self.gpxreader.get_points():
            points.append(point)
        assert len(points) > 0

    @parameterized.expand([
        ('web/tests/example_data/fast_example.gpx'),
        ('web/tests/example_data/fast_example_trackpoints.gpx'),
        ('web/tests/example_data/fast_example_waypoints.gpx'),
        ('web/tests/example_data/fast_example_routepoints.gpx'),
    ])
    def test_get_elevations(self, gpxfile=DEFAULT_GPXFILE_SAMPLE):
        """
        Tests if all elevations will be returned from input element.
        Test should check if elements are TrackPoints Route Points or Way Points.
        """
        self.gpxreader.process_gpx_file(gpxfile)
        elevations = self.gpxreader.get_elevations()
        assert len(elevations) > 0

    @parameterized.expand([
        ('web/tests/example_data/fast_example.gpx', 224),
        ('web/tests/example_data/fast_example_trackpoints.gpx', 224),
        ('web/tests/example_data/fast_example_waypoints.gpx', 224),
        ('web/tests/example_data/fast_example_routepoints.gpx', 224),
    ])
    def test_get_elevations_len(self, gpxfile=DEFAULT_GPXFILE_SAMPLE, elevations_len=224):
        """
        Test if proper amount of elevations are read by get_elevations method.
        """
        self.gpxreader.process_gpx_file(gpxfile)
        elevations = self.gpxreader.get_elevations()
        assert len(elevations) == elevations_len

if __name__ == '__main__':
    unittest.main()
