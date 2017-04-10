"""
Tests for GPXReader class
"""

import pytest

from web.utils import GPXReader

# TODO - find gpx file with : only TrackPoints
# TODO - find gpx file with : only Route Points
# TODO - find gpx file with : only Way Points

# TODO - find gpx file with all elements like TrackPoints, RoutePoints and WayPoints.

@pytest.fixture
def gpxreader_trackpoint():
    """
    Creates trackpoint gpxreader
    """
    return GPXReader('bikingendorphines/example_data/15212277.gpx')


class AbstractGPXReaderTest(object):
    """
    A Prof Of Concept for creating one generalized GPXReader test class.
    It will then be inherited by other classes that will use TrackPoints example data,
    Route Points data and Way Points data using pytest-fixtures.
    """

    def test_get_points(self, gpxreader):
        """
        Tests if there will be data output from get_points.

        Test if:
        - points exists for different types.
        - what will happen if types exists, but no data?
        """
        points = []
        for point in gpxreader.get_points():
            points.append(point)
        assert len(points) > 0

    def test_get_elevations(self, gpxreader):
        """
        Tests if all elevations will be returned from input element.
        Test should check if elements are TrackPoints Route Points or Way Points.
        """
        elevations = gpxreader.get_elevations()
        print len(elevations)
        assert len(elevations) > 0

    def test_get_elevations_len(self, gpxreader, elevations_len):
        """
        Test if proper amount of elevations are read by get_elevations method.
        """
        elevations = gpxreader.get_elevations()
        assert len(elevations) == elevations_len

    def test_get_track_points(self):
        """
        Test if all track points are gathered
        """
        raise NotImplementedError()

    def test_get_route_points(self):
        """
        Test if all route points are gathered
        """
        raise NotImplementedError()

    def test_get_way_points(self):
        """
        Test if all way points are gathered
        """
        raise NotImplementedError()

    def test_get_lowest_elevation(self):
        """
        Checks method for:
        - If no elevations in route, method should return None.
        - If elevations are equal or only one available, return None.
        - If more then one elevation (different) available, return lowest.
        """
        raise NotImplementedError()

    def test_get_highest_elevation(self):
        """
        Checks method for:
        - If no elevations in route, method should return None.
        - If elevations are equal or only one available, return None.
        - If more then one elevation (different) available, return highest.
        """
        raise NotImplementedError()

    def test_animal_figure_route(self):
        """
        Tests if method named "animal_figure_route" will return proper name of animal
        for proper biking route.
        """
        raise NotImplementedError()

class TestTrackPointGPXReader(AbstractGPXReaderTest):
    """
    Specific version of Abstract test-class that uses mainly TrackPoints gpx file for tests.
    """
    def test_get_points(self, gpxreader_trackpoint):
        super(TestTrackPointGPXReader, self).test_get_points(gpxreader_trackpoint)
