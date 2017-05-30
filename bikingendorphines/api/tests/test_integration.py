"""
Tests Integration for API
"""
import unittest
import json
from api.views import UserList, UserDetail, UserBadgeList, FileUploadView
from web.models import User, Badge, Route, UserBadge
from django.contrib.auth.models import User as AuthUser
# pylint: disable=import-error
from django.utils.six.moves import StringIO
# pylint: enable=import-error
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate


class APIGeneralTestCase(unittest.TestCase):
    "General Test Case for API"

    def setUp(self):
        self.path = "/api/user/"
        self.client = APIClient()
        self.user = AuthUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.get(user_id=self.user.id).key
        self.api = APIRequestFactory().get
        self.view = UserList.as_view()

    def tearDown(self):
        "Removes all AuthUser and Users objects at the end of each test"
        self.user.delete()
        User.objects.all().delete()

    def get_response_user_api(self, api_data=None, pk_id=None, **kwargs):
        " Creates response for /api/user List get with forcing login with Token-Authentication "
        self.client.force_login(user=self.user)
        request = self.api(
            self.path,
            api_data,
            HTTP_AUTHORIZATION='Token {}'.format(self.token),
            content_type='application/json'
        )
        force_authenticate(request)
        if pk_id is not None:
            return self.view(request, pk=pk_id)
        return self.view(request, **kwargs)

    def assert_status_code(self, response):
        " Asserts response status code with 200"
        self.assertEquals(response.status_code, 200)

    # pylint: disable=no-self-use
    def create_user_in_db(self):
        " Creates new user object in database "
        return User.objects.create(name='Bart', surname="Trab", weight=80, height=175)

    # pylint: disable=no-self-use
    def create_badge_in_db(self):
        " Creates new badge object in database "
        return Badge.objects.create(
            name='FasterThenUniverse',
            description='you\'re average lap was faster then previous one'
        )

    # pylint: disable=no-self-use
    def create_route_in_db(self):
        " Creates new route object in database "
        return Route.objects.create(route_name="NameOfThisFancyRoute", avg_route=19.9)

    # pylint: disable=no-self-use
    # pylint: disable=too-many-arguments
    def create_user_badge_in_db(self, user, badge, route, active, badge_date, activation_date):
        " Creates new UserBadge object in database "
        return UserBadge.objects.create(
            id_user=user,
            id_badge=badge,
            id_route=route,
            active=active,
            badge_acquiring_date=badge_date,
            activation_modification_date=activation_date,
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

        input_user = self.create_user_in_db()

        self.client.force_login(user=self.user)
        response = self.get_response_user_api()
        self.assert_status_code(response)
        self.assertEquals(len(response.data), 1)
        self.assert_user_object(response.data[0], input_user)

    def test_get_two_user_list(self):
        " Test if setting up user returns user list"

        input_user = self.create_user_in_db()
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


class TestPostUser(APIGeneralTestCase):
    "User Post tests"
    def setUp(self):
        super(self.__class__, self).setUp()
        self.api = APIRequestFactory().post

    def test_return_user_object(self):
        " Tests if making api request returns user object "

        data = json.dumps(
            {"name":"Test", "surname":"tester1", "weight":88, "height":173}
        )
        response = self.get_response_user_api(data)
        self.assertEquals(response.status_code, 201)


class TestDeleteUser(APIGeneralTestCase):
    "User Delete tests"
    def setUp(self):
        super(self.__class__, self).setUp()
        self.api = APIRequestFactory().delete
        self.view = UserDetail.as_view()

    def test_delete_user(self):
        " Tests if making api request deletes user with 204"

        user = self.create_user_in_db()
        self.path = "/api/user/{}/".format(user.id)
        response = self.get_response_user_api(pk_id=user.id)
        self.assertEquals(response.status_code, 204)


class TestUpdateUser(APIGeneralTestCase):
    "User Update tests"
    def setUp(self):
        super(self.__class__, self).setUp()
        self.api = APIRequestFactory().post
        self.view = UserList.as_view()

    def test_update_user(self):
        " Tests if making api request updates user with new name"

        user = self.create_user_in_db()
        self.path = "/api/user/{}/".format(user.id)
        response = self.get_response_user_api(
            json.dumps({"name": "newName", "weight": 88, "height": 111}),
            pk_id=user.id
        )
        self.assertEquals(response.status_code, 201)


class TestUserBadgeList(APIGeneralTestCase):
    "User Update tests"
    def setUp(self):
        super(self.__class__, self).setUp()
        self.view = UserBadgeList.as_view()

    def test_update_user(self):
        " Tests if making api request updates user with new name"

        badge = self.create_badge_in_db()
        route = self.create_route_in_db()
        user = self.create_user_in_db()
        date_badge_acquired = "2017-02-02T22:00:00"
        date_badge_activation = "2017-02-02T22:00:00"
        user_badge = self.create_user_badge_in_db(
            user,
            badge,
            route,
            True,
            date_badge_acquired + "+00:00",
            date_badge_activation + "+00:00"
        )

        self.path = "/api/badge/{}/".format(user_badge.id)
        response = self.get_response_user_api(
            pk_id=user.id
        )
        self.assertEquals(response.status_code, 200)
        self.assert_user_badge(
            response.data[0],
            user.id,
            badge.id,
            route.id,
            user_badge.active,
            unicode(date_badge_acquired + "Z"),
            unicode(date_badge_activation + "Z")
        )

    # pylint: disable=too-many-arguments
    def assert_user_badge(
            self, user_badge_object, user_id, badge_id, route_id,
            active, badge_acquiring_date, activation_modification_date):
        """ Asserts user badge object with parameters """

        self.assertEquals(user_badge_object['id_user'], user_id)
        self.assertEquals(user_badge_object['id_badge'], badge_id)
        self.assertEquals(user_badge_object['id_route'], route_id)
        self.assertEquals(user_badge_object['active'], active)
        self.assertEquals(
            user_badge_object['badge_acquiring_date'],
            badge_acquiring_date
        )
        self.assertEquals(
            user_badge_object['activation_modification_date'],
            activation_modification_date
        )


class TestFileUploadView(APIGeneralTestCase):
    "File Upload tests"
    def setUp(self):
        super(self.__class__, self).setUp()
        self.api = APIRequestFactory().post
        self.view = FileUploadView.as_view()

    def _create_test_file(self, path):
        f = open(path, 'w')
        f.write('test123\n')
        f.close()
        f = open(path, 'rb')
        return {'datafile': f}

    def test_update_user(self):
        " Tests if making api request updates user with new name"

        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_ = open(dir_path + '/samples/routesample.json', 'rb')

        api_data = {'filename':  file_ }

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
        request = APIRequestFactory().post(
            "/api/file/",
            api_data,
            format='json'
        )
        response = self.view(request, format='multipart')
        assert response.status_code == 200
