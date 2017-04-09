"""
Tests for GPXReader class
"""

import pytest

from web.utils import GPXReader

# TODO - find gpx file with : only TrackPoints
# TODO - find gpx file with : only Route Points
# TODO - find gpx file with : only Way Points

# TODO - find gpx file with all elements like TrackPoints, RoutePoints and WayPoints.

@pytest.fixture(
    scope='module',
    params=[
        {
            "route": 'bikingendorphines/example_data/15212277.gpx',
            "elevations_len": 22627,

        },
        {
            "route": 'bikingendorphines/example_data/15212277.gpx',
            "elevations_len": 22627,
        }
    ]
)
def test_data(request):
    """
    Pytest Fixture. Creates GPXReader instance with predefined gpx file.
    """
    return GPXReader(request.param["route"]), request.param["elevations_len"]

# pylint: disable=redefined-outer-name
def test_get_points(test_data):
    """
    Tests if there will be data output from get_points.

    Test if:
    - points exists for different types.
    - what will happen if types exists, but no data?
    """
    gpxreader = test_data[0]
    points = []
    for point in gpxreader.get_points():
        points.append(point)
    assert len(points) > 0

def test_get_elevations(test_data):
    """
    Tests if all elevations will be returned from input element.
    Test should check if elements are TrackPoints Route Points or Way Points.
    """
    gpxreader = test_data[0]
    elevations = gpxreader.get_elevations()
    print len(elevations)
    assert len(elevations) > 0

def test_get_elevations_len(test_data):
    """
    Test if proper amount of elevations are read by get_elevations method.
    """
    gpxreader, elevations_len = test_data

    elevations = gpxreader.get_elevations()
    assert len(elevations) == elevations_len
