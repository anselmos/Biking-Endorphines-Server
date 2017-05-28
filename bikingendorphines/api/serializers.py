"""
Serializers for API
"""
from rest_framework import serializers
from web.models import User, UserBadge, Route

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'weight', 'height', 'bmi', 'bmi_health_name')

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


class RouteSerializer(serializers.ModelSerializer):
    """
    Route serializer
    """
    class Meta:
        model = Route
        fields = ('id', 'route_name', 'avg_route')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Route.objects.create(**validated_data)


class UserBadgeSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = UserBadge
        fields = (
            'id',
            'id_badge',
            'id_user',
            'id_route',
            'active',
            'badge_acquiring_date',
            'activation_modification_date'
        )

    def create(self, validated_data):
        """
        Create and return a new `UserBadge` instance, given the validated data.
        """
        return UserBadge.objects.create(**validated_data)
