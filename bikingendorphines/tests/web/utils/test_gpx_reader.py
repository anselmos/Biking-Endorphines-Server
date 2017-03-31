"""
Tests for GPXReader class
"""

import pytest

from web.utils import GPXReader

@pytest.fixture(
    scope='module',
    params=[
        'bikingendorphines/example_data/15212277.gpx',
        'bikingendorphines/example_data/15212277.gpx'
    ]
)
def gpxreader(request):
    """
    Creates GPXReader instance with predefined gpx file
    """
    return GPXReader(request.param)

# pylint: disable=redefined-outer-name
def test_get_points(gpxreader):
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
