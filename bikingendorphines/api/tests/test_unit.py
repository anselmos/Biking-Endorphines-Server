"""
All unit-type tests
For now Serializer's tests coexists here
"""
import unittest
from web.models import User, Route
from api.serializers import UserSerializer, RouteSerializer

class TestUserSerializer(unittest.TestCase):
    "UserSerializer tests"

    def test_user_serialize_to_json(self):
        "test if serializing to JSON works"

        mocked = User()
        mocked.name = "Anselmos"
        mocked.surname = "Somlesna"
        mocked.weight = 80
        mocked.height = 175

        user_serialized = UserSerializer(mocked)
        self.assertEqual(
            (user_serialized.data),
            {
                'height': 175,
                'surname': u'Somlesna',
                'id': None,
                'weight': 80,
                'name': u'Anselmos',
                'bmi': 26.12,
                'bmi_health_name': u'Overweight'
            }
        )


class TestRouteSerializer(unittest.TestCase):
    "Route Serializer test"

    def test_route_serialize(self):
        "Tests if Route object serialize with RouteSerializer"
        input_route = Route()
        input_route.route_name = "NameOfThisFancyRoute"
        input_route.avg_route = 19.9
        input_serialized = RouteSerializer(input_route)
        self.assertEqual(
            (input_serialized.data),
            {
                'id': None,
                'route_name': "NameOfThisFancyRoute",
                'avg_route': 19.9
            }
        )
