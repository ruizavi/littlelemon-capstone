from datetime import datetime
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.core import serializers as sr
from . import models, serializers


# Static Content
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, 'about.html', {})


def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = models.Booking.objects.all()
    booking_json = sr.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})


# Api View
class MenuItemView(generics.ListCreateAPIView):
    serializer_class = serializers.MenuItemSerializer
    queryset = models.MenuItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if (self.request.method == "GET"):
            return []

        return super().get_permissions()


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MenuItemSerializer
    queryset = models.MenuItem.objects.all()

    def get_permissions(self):
        if (self.request.method == "GET"):
            return []

        return super().get_permissions()


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookingSerializer
    queryset = models.Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]
