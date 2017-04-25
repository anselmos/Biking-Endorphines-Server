"""
Tests for API
"""
import unittest
from api.serializers import UserSerializer
from api.views import UserList
from web.models import User



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
            {'height': 175, 'surname': u'Somlesna', 'id': None, 'weight': 80, 'name': u'Anselmos'}
        )

