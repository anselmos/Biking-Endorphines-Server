"""
Tests for API
"""
import unittest
from api.serializers import UserSerializer
from api.views import UserList
from web.models import User
from django.contrib.auth.models import User as AuthUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate


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


class TestUserList(unittest.TestCase):
    "UserList tests"

    def setUp(self):
        self.client = APIClient()
        self.user = AuthUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.get(user_id=self.user.id).key

    def test_user_get_return_json(self):
        "test if using get returns json data"

        self.client.force_login(user=self.user)
        view = UserList.as_view()
        factory = APIRequestFactory()
        request = factory.get("/api/user/", HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request)
        response = view(request)
        self.assertEquals(response.status_code, 200)
