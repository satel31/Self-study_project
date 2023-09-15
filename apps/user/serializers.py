from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'city', 'avatar', 'phone', 'password')


class StrangerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'city', 'avatar', 'phone', 'telegram',)
