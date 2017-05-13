"""
Tests for API
"""
import unittest
import json
from api.serializers import UserSerializer
from api.views import UserList
from web.models import User
from django.contrib.auth.models import User as AuthUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate


class APIGeneralTestCase(unittest.TestCase):
    "General Test Case for API"

    def setUp(self):
        self.client = APIClient()
        self.user = AuthUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.get(user_id=self.user.id).key
        self.api = APIRequestFactory().get

    def tearDown(self):
        "Removes all AuthUser and Users objects at the end of each test"
        self.user.delete()
        User.objects.all().delete()

    def get_response_user_api(self, api_data=None):
        " Creates response for /api/user List get with forcing login with Token-Authentication "
        self.client.force_login(user=self.user)
        view = UserList.as_view()
        request = self.api(
            "/api/user/",
            api_data,
            HTTP_AUTHORIZATION='Token {}'.format(self.token),
            content_type='application/json'
        )
        force_authenticate(request)
        response = view(request)
        return response

    def assert_status_code(self, response):
        " Asserts response status code with 200"
        self.assertEquals(response.status_code, 200)

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
                'bmi': 26,
                'bmi_health_name': u'Overweight'
            }
        )


class TestUserList(APIGeneralTestCase):
    "UserList tests"

    def test_user_get_return_json(self):
        "test if using get returns json data"

        self.client.force_login(user=self.user)
        response = self.get_response_user_api()
        self.assert_status_code(response)

    def test_user_list_return_json_list(self):
        " Test if setting up user returns user list"

        input_user = User.objects.create(name='Bart', surname="Trab", weight=80, height=175)

        self.client.force_login(user=self.user)
        response = self.get_response_user_api()
        self.assert_status_code(response)
        self.assertEquals(len(response.data), 1)
        self.assert_user_object(response.data[0], input_user)

    def test_get_two_user_list(self):
        " Test if setting up user returns user list"

        input_user = User.objects.create(name='Bart', surname="Trab", weight=80, height=175)
        input_user2 = User.objects.create(name='B222art', surname="Trabaaaa", weight=50, height=100)

        response = self.get_response_user_api()
        self.assert_status_code(response)
        self.assertEquals(len(response.data), 2)
        self.assert_user_object(response.data[0], input_user)
        self.assert_user_object(response.data[1], input_user2)


    def assert_user_object(self, input_json, expected):
        "Asserts response User input json object == expected user model object. "
        self.assertEquals(input_json['name'], expected.name)
        self.assertEquals(input_json['surname'], expected.surname)
        self.assertEquals(input_json['weight'], expected.weight)
        self.assertEquals(input_json['height'], expected.height)
        self.assertEquals(input_json['bmi'], expected.bmi())
        self.assertEquals(input_json['bmi_health_name'], expected.bmi_health_name())


class TestUser(APIGeneralTestCase):
    "UserList tests"


    def test_return_user_object(self):
        " Tests if making api request returns user object "

        self.api = APIRequestFactory().post
        data = json.dumps(
            {"name":"Test", "surname":"tester1", "weight":88, "height":173}
        )
        response = self.get_response_user_api(data)
        self.assertEquals(response.status_code, 201)
