"""
Views
"""
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import UserSerializer
from web.models import User


class UserList(APIView):
    """
    List all User's, or create a new snippet
    """

    def get(self, request, format=None):
        "GET"
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
