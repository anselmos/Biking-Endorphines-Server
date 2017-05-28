"""
Views
"""
from rest_framework import generics

from api.serializers import UserSerializer, UserBadgeSerializer
from web.models import User, UserBadge


class UserList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing users.

    post:
    Create a new user instance.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    delete:
    Deletes a user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserBadgeList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing user badges.

    """
    queryset = UserBadge.objects.all()
    serializer_class = UserBadgeSerializer
