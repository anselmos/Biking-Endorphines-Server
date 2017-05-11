"""
Views
"""
from rest_framework import generics

from api.serializers import UserSerializer
from web.models import User


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
