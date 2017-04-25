"""
Serializers for API
"""
from rest_framework import serializers
from web.models import User

class UserSerializer(serializers.Serializer):
    """
    User serializer
    """
    #pylint: disable=invalid-name
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    surname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    weight = serializers.IntegerField(required=False, default=0)
    height = serializers.IntegerField(required=False, default=0)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.save()
        return instance
