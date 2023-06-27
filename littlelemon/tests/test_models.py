from django.test import TestCase
from restaurant import models

# Esta prueba crea y un objecto y y verifica que devuelva la información adecuada
class TestMenuItem(TestCase):
    def test_get_item(self):
        item = models.MenuItem.objects.create(
            title='IceCream', price=80, inventory=100)

        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
