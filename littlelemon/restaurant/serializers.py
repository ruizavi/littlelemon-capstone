from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuTable
        fields = "__all__"
