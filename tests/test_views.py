from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title='Menuitem 1', price=10.0, inventory=8)
        self.item2 = Menu.objects.create(title='Menuitem 2', price=20.0, inventory=9)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menuitems = Menu.objects.all()
        serializer = MenuSerializer(menuitems, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)