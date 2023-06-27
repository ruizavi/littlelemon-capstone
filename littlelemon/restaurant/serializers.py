from rest_framework import serializers
from . import models


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuTable
        fields = "__all__"
