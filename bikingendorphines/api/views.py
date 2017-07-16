"""
Views
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, UserBadgeSerializer,\
    PointSerializer
from web.models import User, UserBadge, Point


class UserList(ListCreateAPIView):
    """
    get:
    Return a list of all existing users.

    post:
    Create a new user instance.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    """
    delete:
    Deletes a user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserBadgeList(ListCreateAPIView):
    """
    get:
    Return a list of all existing user badges.

    """
    queryset = UserBadge.objects.all()
    serializer_class = UserBadgeSerializer


class PointView(ListCreateAPIView):
    """
    get:
    Return a list of all existing point elements.

    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointList(ListCreateAPIView):
    """
    get:
    Return a list of all existing point list of elements.

    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class FileUploadView(APIView):
    " A view for file upload "
    parser_classes = (JSONParser,)

    #pylint: disable=redefined-builtin
    def post(self, request, format='json'):
        """
        Make a post request with json-body
        """
        return Response(request.data)
