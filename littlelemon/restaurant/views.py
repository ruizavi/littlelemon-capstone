from django.shortcuts import render
from rest_framework import generics
from . import models, serializers


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = models.MenuTable.objects.all()


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = models.MenuTable.objects.all()
