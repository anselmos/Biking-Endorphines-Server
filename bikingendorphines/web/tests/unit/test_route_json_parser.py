"""
Tests for RouteJSONParser
"""
import json

from django.test import TestCase
# pylint: disable=import-error
from django.utils.six.moves import StringIO
# pylint: enable=import-error
from rest_framework.parsers import JSONParser

# pylint: disable=too-few-public-methods
class Point(object):
    """ Point object with lat/lon time and ele """

    def __init__(self, lat, lon, time, ele):
        self.lat = lat
        self.lon = lon
        self.time = time
        self.ele = ele

    def __repr__(self):
        return "{},{},{},{}".format(
            self.lat,
            self.lon,
            self.time,
            self.ele,
        )


# pylint: disable=too-few-public-methods
class RouteJSONParser(JSONParser):
    """ Route JSON Parser - parses JSON file into list of Points"""

    def parse(self, stream, media_type=None, parser_context=None):
        json_content = super(RouteJSONParser, self).parse(stream, media_type, parser_context)
        points = []
        for point in json_content:
            points.append(Point(point['lat'], point['lon'], point['time'], point['ele']))
        return points


class TestRouteJSONParser(TestCase):
    " Tests for RouteJSONParser class parse method overloaded"

    def setUp(self):
        self.parser = RouteJSONParser()

    def test_parse(self):
        " tests parser "
        input_dict = [
            {
                "lat": "53.126699",
                "lon": "18.072322",
                "time": "2000-01-01T07:47:02Z",
                "ele": 107.0
            },
            {
                "lat": "53.126699",
                "lon": "18.072322",
                "time": "2001-01-01T07:47:02Z",
                "ele": 99.0
            }
        ]
        expected = [
            Point(
                lat="53.126699",
                lon="18.072322",
                time="2000-01-01T07:47:02Z",
                ele=107.0
            ),
            Point(
                lat="53.126699",
                lon="18.072322",
                time="2001-01-01T07:47:02Z",
                ele=99.0
            )
        ]

        input_stream = StringIO(json.dumps(input_dict))
        output = self.parser.parse(input_stream)
        assert str(output) == str(expected)
