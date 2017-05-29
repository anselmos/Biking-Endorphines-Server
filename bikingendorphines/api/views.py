"""
Views
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, UserBadgeSerializer
from web.models import User, UserBadge


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


class FileUploadView(APIView):
    " A view for file upload "
    parser_classes = (JSONParser,)

    def post(self, request, filename, format=None):
        return Response(request.data)
