from django.urls import reverse
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
import json

from restaurant import serializers, models


class BookingViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='mock',
            password='mock@123!'
        )
        self.client.force_authenticate(user=self.user)

        self.booking1 = models.Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=timezone.now()
        )
        self.booking2 = models.Booking.objects.create(
            name='Jane Smith',
            no_of_guests=4,
            booking_date=timezone.now()
        )
        self.booking3 = models.Booking.objects.create(
            name='Jane Doe',
            no_of_guests=7,
            booking_date=timezone.now()
        )

        self.valid_payload = {
            'name': 'Test Booking',
            'no_of_guests': 3,
            'booking_date': timezone.now()
        }
        self.invalid_payload = {
            'name': '',
            'no_of_guests': '',
            'booking_date': ''
        }

    def test_get_all_bookings(self):
        response = self.client.get(reverse('booking-list'))
        bookings = models.Booking.objects.all()
        serializer = serializers.BookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_booking(self) -> None:
        response = self.client.post(
            reverse('booking-list'),
            data=json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_booking(self) -> None:
        response = self.client.post(
            reverse('booking-list'),
            data=json.dumps(self.invalid_payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_valid_single_booking(self) -> None:
        response = self.client.get(
            reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        booking = models.Booking.objects.get(pk=self.booking1.pk)
        serializer = serializers.BookingSerializer(booking)
        self.assertEqual(response.data, serializer.data)
