"""
All unit-type tests
For now Serializer's tests coexists here
"""
import unittest
from web.models import User, Route, Badge, UserBadge
from api.serializers import UserSerializer, UserBadgeSerializer, RouteSerializer

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


class TestUserBadgeSerializer(unittest.TestCase):
    "UserBadge Serializer test"

    def test_user_badge_serialize(self):
        "Tests if user_badge object serialize with RouteSerializer"
        user = User()
        user.id = 21
        user.name = "Anselmos"
        user.surname = "Somlesna"
        user.weight = 80
        user.height = 175

        badge = Badge()
        badge.id = 1
        badge.name = 'FasterThenUniverse'
        badge.description = 'you\'re average lap was faster then previous one'

        route = Route()
        route.id = 2
        route.route_name = "NameOfThisFancyRoute"
        route.avg_route = 19.9


        input_user_badge = UserBadge()
        input_user_badge.id_user = user
        input_user_badge.id_badge = badge
        input_user_badge.id_route = route
        input_user_badge.active = True
        input_user_badge.badge_acquiring_date = "2017-03-03T12:00:00+00:00"
        input_user_badge.activation_modification_date = "2017-03-03T12:00:00+00:00"

        input_serialized = UserBadgeSerializer(input_user_badge)
        self.assertEqual(
            (input_serialized.data),
            {
                'id': None,
                'id_badge': 1,
                'id_user': 21,
                'id_route': 2,
                'active': True,
                'badge_acquiring_date': '2017-03-03T12:00:00+00:00',
                'activation_modification_date': '2017-03-03T12:00:00+00:00',
            }
        )
