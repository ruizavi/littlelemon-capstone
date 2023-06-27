from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ["id", "title", "price", "inventory"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"
