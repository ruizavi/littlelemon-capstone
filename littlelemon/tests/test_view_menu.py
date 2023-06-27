from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from restaurant import serializers, models


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.pizza = models.MenuItem.objects.create(
            title='Pizza', price=12.99, inventory=10)
        self.burger = models.MenuItem.objects.create(
            title='Burger', price=8.99, inventory=5)
        self.pasta = models.MenuItem.objects.create(
            title='Pasta', price=15.99, inventory=7)

    def test_getall(self):
        response = self.client.get(reverse('api_menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = models.MenuItem.objects.all()
        serializer = serializers.MenuItemSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
