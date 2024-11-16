from rest_framework.serializers import ModelSerializer
from .models import CustomUser

import rest_framework.serializers as serializers


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerialize(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:

        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
